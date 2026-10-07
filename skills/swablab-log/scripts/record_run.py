#!/usr/bin/env python3
"""Small, standard-library run recorder. Import MetricWriter in the training process."""

import argparse
import csv
import json
import os
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


FIELD_GROUPS = (
    ("run_name", "start_time", "stage", "model", "dataset", "launcher", "command"),
    ("slurm_job_id", "SLURM_JOB_ID", "SLURM_JOB_NAME", "SLURM_JOB_NODELIST",
     "SLURM_NTASKS", "SLURM_GPUS", "SLURM_CPUS_PER_TASK", "CUDA_VISIBLE_DEVICES",
     "node", "world_size", "gpu_count"),
    ("swanlab_project", "swanlab_run", "swanlab_url"),
    ("precision", "batch_size", "gradient_accumulation", "effective_batch_size",
     "optimizer", "learning_rate", "scheduler", "warmup", "max_steps",
     "max_seq_length", "seed"),
    ("hardware", "environment"),
)
SLURM_FIELDS = (
    "SLURM_JOB_ID", "SLURM_JOB_NAME", "SLURM_JOB_NODELIST", "SLURM_NTASKS",
    "SLURM_GPUS", "SLURM_CPUS_PER_TASK", "CUDA_VISIBLE_DEVICES",
)


def read_run(run_dir):
    """Read only this run; an update never creates a directory."""
    fields = {}
    for line in (Path(run_dir) / "run.txt").read_text(encoding="utf-8").splitlines():
        if line:
            key, value = line.split(":", 1)
            fields[key] = value.strip()
    return fields


def update_run(run_dir, fields):
    run_dir = Path(run_dir)
    info = read_run(run_dir)
    for key, value in fields.items():
        if value is None or value == "":
            continue
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", key):
            raise ValueError("run.txt fields must use standard parameter names")
        if isinstance(value, (dict, list)):
            value = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        value = str(value).replace("\n", "\\n").replace("\r", "\\r")
        if key in ("run_name", "start_time") and key in info and info[key] != value:
            raise ValueError(f"{key} is the existing run identity; do not replace it")
        info[key] = value
    blocks = []
    known = set()
    for group in FIELD_GROUPS:
        lines = [f"{key}: {info[key]}" for key in group if key in info]
        known.update(group)
        if lines:
            blocks.append("\n".join(lines))
    extra = [f"{key}: {value}" for key, value in info.items() if key not in known]
    if extra:
        blocks.append("\n".join(extra))
    (run_dir / "run.txt").write_text("\n\n".join(blocks) + "\n", encoding="utf-8")


def create_run(root, stage, model, key_config, tag=None, start_time=None,
               timezone="Asia/Shanghai", fields=None, ckpt_source=None):
    moment = (datetime.fromisoformat(start_time.replace("Z", "+00:00"))
              if start_time else datetime.now(ZoneInfo(timezone)))
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=ZoneInfo(timezone))
    moment = moment.astimezone(ZoneInfo(timezone))
    # A model repository ID remains readable without becoming a subdirectory.
    parts = [stage, model.replace("/", "-"), key_config]
    if tag:
        parts.append(tag)
    if any(not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.+-]*", part) for part in parts):
        raise ValueError("name components must be readable tokens separated by hyphens")
    name = moment.strftime("%Y%m%d-%H%M%S") + "_" + "_".join(parts)
    source = Path(ckpt_source).resolve(strict=True) if ckpt_source else None
    run_dir = Path(root) / name
    run_dir.mkdir(parents=True)  # A name collision must not reuse another training run.
    for filename in ("run.txt", "train.txt", "metrics.csv"):
        (run_dir / filename).touch()
    if source:
        (run_dir / "ckpt").symlink_to(source, target_is_directory=True)
    else:
        (run_dir / "ckpt").mkdir()
    update_run(run_dir, dict(fields or {}, run_name=name,
                            start_time=moment.isoformat(timespec="seconds"),
                            stage=stage, model=model))
    return run_dir.resolve()


def record_slurm(run_dir, job_id=None, fields=None):
    # Do not attach the caller's job environment to a different explicitly named job.
    current_job = os.environ.get("SLURM_JOB_ID")
    info = {key: os.environ[key] for key in SLURM_FIELDS if key in os.environ}
    if job_id is not None and str(job_id) != current_job:
        info = {}
    info.update(fields or {})
    if job_id is not None:
        info["SLURM_JOB_ID"] = str(job_id)
    update_run(run_dir, info)


def checkpoint_path(run_dir, step=None, final=False, native_name=None):
    if native_name:
        if Path(native_name).name != native_name or native_name in (".", ".."):
            raise ValueError("native_name must be a checkpoint directory name")
        return Path(run_dir) / "ckpt" / native_name
    if final:
        return Path(run_dir) / "ckpt" / "final"
    if step is not None:
        return Path(run_dir) / "ckpt" / f"step-{int(step):08d}"
    return Path(run_dir) / "ckpt"


def record_swanlab(run_dir, tracker, dependencies=("torch", "transformers", "trl",
                   "deepspeed", "accelerate", "swanlab")):
    """Extract static data from SwanLab's v2 probe files, not from the host."""
    files = Path(tracker.dir) / "files"
    metadata_file = files / "swanlab-metadata.json"
    metadata = (json.loads(metadata_file.read_text(encoding="utf-8"))
                if metadata_file.exists() else {})
    requirements = files / "requirements.txt"

    def compact(value):
        if isinstance(value, dict):
            return {key: compact(item) for key, item in value.items()
                    if item is not None and item != "" and item != [] and item != {}}
        if isinstance(value, list):
            return [compact(item) for item in value]
        return value

    environment = compact(metadata.get("runtime") or {})
    if requirements.exists():
        names = {name.lower().replace("_", "-") for name in dependencies}
        lines = requirements.read_text(encoding="utf-8").splitlines()
        selected = []
        for line in lines:
            match = re.match(r"^\s*([A-Za-z0-9_.-]+)(?=\s|==|@|$)", line)
            if match and match[1].lower().replace("_", "-") in names:
                selected.append(line.strip())
        if selected:
            environment["dependencies"] = selected
        environment["requirements_file"] = str(requirements)
    info = {"swanlab_run": tracker.id}
    hardware = compact(metadata.get("hardware") or {})
    if hardware:
        info["hardware"] = hardware
    if environment:
        info["environment"] = environment
    if tracker.mode == "online":
        info["swanlab_url"] = tracker.url
    update_run(run_dir, info)


def _last_row(path):
    """Read the tail once on resume, without scanning historical metrics."""
    with path.open("rb") as file:
        file.seek(0, 2)
        end = file.tell()
        tail = b""
        while end and tail.count(b"\n") < 2:
            size = min(end, 4096)
            end -= size
            file.seek(end)
            tail = file.read(size) + tail
    return next(csv.reader([tail.splitlines()[-1].decode("utf-8")]))


class MetricWriter:
    """One global-rank-zero writer; merge same-step events before appending."""

    def __init__(self, run_dir, columns=None):
        self.path = Path(run_dir) / "metrics.csv"
        self.last_step = -1
        self.pending_step = None
        self.pending = {}
        if self.path.stat().st_size:
            with self.path.open(newline="", encoding="utf-8") as file:
                self.columns = next(csv.reader(file))
            if columns is not None and self.columns != self._columns(columns):
                raise ValueError("reuse the existing CSV columns when updating a run")
            row = _last_row(self.path)
            index = self.columns.index("step")
            if row[index] != "step":
                self.last_step = int(row[index])
        else:
            if columns is None:
                raise ValueError("choose this run's emitted metric columns before first logging")
            self.columns = self._columns(columns)
            with self.path.open("a", newline="", encoding="utf-8") as file:
                csv.writer(file).writerow(self.columns)

    @staticmethod
    def _columns(columns):
        return ["timestamp", "step"] + list(dict.fromkeys(
            key for key in columns if key not in ("timestamp", "step")))

    def log(self, step, metrics, timestamp=None):
        step = int(step)
        if step <= self.last_step:
            return False
        if self.pending_step is not None and step < self.pending_step:
            return False
        unknown = set(metrics) - set(self.columns)
        if unknown:
            raise ValueError(f"metric columns were not selected for this run: {sorted(unknown)}")
        if "step" in metrics and int(metrics["step"]) != step:
            raise ValueError("metric step differs from the supplied optimizer/global step")
        if any(isinstance(value, (dict, list, tuple)) or "\n" in str(value)
               or "\r" in str(value) for value in metrics.values()):
            raise ValueError("metrics.csv stores scalar step-level metrics")
        if self.pending_step is not None and step > self.pending_step:
            self.flush()
        if self.pending_step is None:
            self.pending_step = step
            self.pending = {"timestamp": timestamp or datetime.now().astimezone().isoformat(
                timespec="seconds"), "step": step}
        self.pending.update({key: value for key, value in metrics.items()
                             if key not in ("step", "timestamp") and value is not None})
        return True

    def flush(self):
        if self.pending_step is not None:
            with self.path.open("a", newline="", encoding="utf-8") as file:
                csv.DictWriter(file, fieldnames=self.columns).writerow(self.pending)
            self.last_step = self.pending_step
            self.pending_step = None
            self.pending = {}

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.flush()


def trainer_callback(run_dir, columns):
    """Local CSV hook for HF/TRL; SwanLab's official callback handles cloud logging."""
    from transformers import TrainerCallback

    class RunMetrics(TrainerCallback):
        def __init__(self):
            self.writer = None

        def on_log(self, args, state, control, logs=None, **kwargs):
            if not state.is_world_process_zero or not logs:
                return
            if self.writer is None:
                self.writer = MetricWriter(run_dir, columns)
            aliases = {"learning_rate": "lr"}
            values = {aliases.get(key, key): value for key, value in logs.items()
                      if aliases.get(key, key) in self.writer.columns and value is not None}
            if values:
                self.writer.log(state.global_step, values)

        def flush(self):
            if self.writer is not None:
                self.writer.flush()

        def on_train_end(self, args, state, control, **kwargs):
            self.flush()

    return RunMetrics()


def _pairs(values):
    result = {}
    for value in values:
        key, separator, data = value.partition("=")
        if not separator:
            raise ValueError("use --set key=value")
        result[key] = data
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    create = commands.add_parser("create", help="create one training run")
    create.add_argument("--root", default="runs")
    create.add_argument("--stage", required=True)
    create.add_argument("--model", required=True)
    create.add_argument("--key-config", required=True)
    create.add_argument("--tag")
    create.add_argument("--start-time", help="ISO start time; default is now")
    create.add_argument("--timezone", default="Asia/Shanghai")
    create.add_argument("--ckpt-source", help="existing native checkpoint root, linked without copying")
    create.add_argument("--set", action="append", default=[])
    update = commands.add_parser("update", help="update the same run.txt")
    update.add_argument("run_dir")
    update.add_argument("--set", action="append", default=[], required=True)
    metric = commands.add_parser("metric", help="append one complete step; skip recorded steps")
    metric.add_argument("run_dir")
    metric.add_argument("--step", type=int, required=True)
    metric.add_argument("--timestamp")
    metric.add_argument("--columns", help="comma-separated per-run columns, needed for the first row")
    metric.add_argument("--set", action="append", default=[], required=True)
    slurm = commands.add_parser("slurm", help="attach the current environment or an explicit job")
    slurm.add_argument("run_dir")
    slurm.add_argument("--job-id")
    slurm.add_argument("--set", action="append", default=[])
    ckpt = commands.add_parser("ckpt", help="print a native save path; never copy checkpoints")
    ckpt.add_argument("run_dir")
    naming = ckpt.add_mutually_exclusive_group()
    naming.add_argument("--step", type=int)
    naming.add_argument("--final", action="store_true")
    naming.add_argument("--native-name")
    args = parser.parse_args()
    try:
        if args.action == "create":
            print(create_run(args.root, args.stage, args.model, args.key_config,
                             args.tag, args.start_time, args.timezone,
                             _pairs(args.set), args.ckpt_source))
        elif args.action == "update":
            update_run(args.run_dir, _pairs(args.set))
        elif args.action == "metric":
            columns = args.columns.split(",") if args.columns is not None else None
            with MetricWriter(args.run_dir, columns) as writer:
                accepted = writer.log(args.step, _pairs(args.set), args.timestamp)
            print("appended" if accepted else "skipped recorded step")
        elif args.action == "slurm":
            record_slurm(args.run_dir, args.job_id, _pairs(args.set))
        elif args.action == "ckpt":
            print(checkpoint_path(args.run_dir, args.step, args.final, args.native_name))
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
