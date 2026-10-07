import csv
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "swablab_record_run", ROOT / "skills/swablab-log/scripts/record_run.py"
)
recorder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(recorder)


class SwablabLogTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def create_run(self, **kwargs):
        return recorder.create_run(
            self.root / "runs", "sft", "qwen3-8b", "lr2e-5", "reasoning",
            start_time="2026-10-07T16:12:05+08:00", **kwargs
        )

    def test_metrics_merge_same_step_and_resume_without_rewriting_history(self):
        run_dir = self.create_run()
        with recorder.MetricWriter(run_dir, ["epoch", "loss", "lr", "eval_loss"]) as writer:
            self.assertTrue(writer.log(
                10, {"epoch": 0.5, "loss": 0.4, "lr": 2e-5},
                timestamp="2026-10-07T16:13:00+08:00"
            ))
            self.assertTrue(writer.log(10, {"eval_loss": 0.45}))
            self.assertTrue(writer.log(
                11, {"loss": 0.38, "lr": 1.9e-5},
                timestamp="2026-10-07T16:13:10+08:00"
            ))

        path = run_dir / "metrics.csv"
        historical_bytes = path.read_bytes()
        with path.open(newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
        self.assertEqual([row["step"] for row in rows], ["10", "11"])
        self.assertEqual(rows[0]["loss"], "0.4")
        self.assertEqual(rows[0]["eval_loss"], "0.45")
        self.assertEqual(rows[0]["epoch"], "0.5")
        self.assertEqual(rows[0]["timestamp"], "2026-10-07T16:13:00+08:00")

        with recorder.MetricWriter(run_dir) as resumed:
            self.assertFalse(resumed.log(10, {"loss": 99}))
            self.assertFalse(resumed.log(11, {"eval_loss": 99}))
            resumed.flush()
            self.assertEqual(path.read_bytes(), historical_bytes)
            self.assertTrue(resumed.log(
                12, {"loss": 0.36, "lr": 1.8e-5},
                timestamp="2026-10-07T16:13:20+08:00"
            ))
            self.assertTrue(resumed.log(12, {"eval_loss": 0.41}))

        self.assertTrue(path.read_bytes().startswith(historical_bytes))
        with path.open(newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
        self.assertEqual([row["step"] for row in rows], ["10", "11", "12"])
        self.assertEqual(rows[-1]["loss"], "0.36")
        self.assertEqual(rows[-1]["eval_loss"], "0.41")

    def test_existing_native_checkpoints_are_linked_without_changing_weights(self):
        source = self.root / "trainer-output"
        native = source / "checkpoint-1000"
        native.mkdir(parents=True)
        weights = native / "model.safetensors"
        payload = b"native checkpoint weights\x00\xff\n"
        weights.write_bytes(payload)
        original_stat = weights.stat()
        original_entries = sorted(path.relative_to(source) for path in source.rglob("*"))

        run_dir = self.create_run(ckpt_source=source)
        self.assertTrue((run_dir / "ckpt").is_symlink())
        self.assertEqual((run_dir / "ckpt").resolve(), source.resolve())
        destination = recorder.checkpoint_path(run_dir, native_name="checkpoint-1000")
        self.assertEqual(destination.resolve(), native.resolve())
        self.assertEqual((destination / "model.safetensors").read_bytes(), payload)
        self.assertEqual(weights.read_bytes(), payload)
        self.assertEqual(weights.stat().st_ino, original_stat.st_ino)
        self.assertEqual(weights.stat().st_mtime_ns, original_stat.st_mtime_ns)
        self.assertEqual(
            sorted(path.relative_to(source) for path in source.rglob("*")), original_entries
        )
        self.assertFalse((run_dir / "ckpt" / "step-00001000").exists())

    def test_explicit_slurm_job_does_not_inherit_another_jobs_environment(self):
        run_dir = self.create_run()
        environment = {
            "SLURM_JOB_ID": "999999", "SLURM_JOB_NAME": "unrelated-training",
            "SLURM_JOB_NODELIST": "other-node", "SLURM_NTASKS": "32",
            "SLURM_GPUS": "8", "SLURM_CPUS_PER_TASK": "16",
            "CUDA_VISIBLE_DEVICES": "0,1,2,3,4,5,6,7",
        }
        with patch.dict(os.environ, environment, clear=True):
            recorder.record_slurm(
                run_dir, job_id="123456", fields={"SLURM_JOB_NODELIST": "training-node"}
            )

        fields = recorder.read_run(run_dir)
        self.assertEqual(fields["SLURM_JOB_ID"], "123456")
        self.assertEqual(fields["SLURM_JOB_NODELIST"], "training-node")
        for key in environment.keys() - {"SLURM_JOB_ID", "SLURM_JOB_NODELIST"}:
            self.assertNotIn(key, fields)

    def test_swanlab_v2_static_files_and_dependency_lines_in_local_mode(self):
        run_dir = self.create_run()
        files = self.root / "tracker-run" / "files"
        files.mkdir(parents=True)
        hardware = {
            "apple_silicon": None,
            "cpu": {"brand": "AMD EPYC", "physical_count": 64, "logical_count": 128},
            "memory": {"total": 512, "total_unit": "GB"},
            "accelerators": [{
                "vendor": "nvidia", "version": "570.124", "cuda_version": "12.8",
                "cann_version": None,
                "devices": [{"index": 0, "name": "NVIDIA H100", "memory": 80,
                             "memory_unit": "GB"}],
            }],
        }
        runtime = {
            "os": "Linux", "os_pretty": None, "hostname": "training-node",
            "pid": 2345, "cwd": "/workspace/training", "python_version": "3.12.9",
            "python_verbose": None, "python_executable": "/env/bin/python",
            "command": "python train.py --learning_rate 2e-5",
        }
        (files / "swanlab-metadata.json").write_text(json.dumps({
            "_version": 2, "hardware": hardware, "runtime": runtime, "git": None,
            "swanlab": {"version": "0.10.1", "run_dir": str(files.parent)},
        }), encoding="utf-8")
        requirements = files / "requirements.txt"
        requirements.write_text(
            "torch==2.6.0\ntransformers==4.50.0\n"
            "deepspeed 0.18.1 conda-forge\nunrelated==1.0\n", encoding="utf-8"
        )
        # This tracker deliberately exposes no URL: local mode must never ask for one.
        tracker = Mock(spec=["dir", "id", "mode"])
        tracker.dir = files.parent
        tracker.id = "static-local-run"
        tracker.mode = "local"
        recorder.record_swanlab(run_dir, tracker)

        fields = recorder.read_run(run_dir)
        self.assertEqual(fields["swanlab_run"], "static-local-run")
        self.assertNotIn("swanlab_url", fields)
        self.assertNotIn("git", fields)
        recorded_hardware = json.loads(fields["hardware"])
        self.assertEqual(recorded_hardware["cpu"], hardware["cpu"])
        self.assertEqual(recorded_hardware["memory"], hardware["memory"])
        self.assertEqual(recorded_hardware["accelerators"][0]["devices"],
                         hardware["accelerators"][0]["devices"])
        self.assertNotIn("apple_silicon", recorded_hardware)
        self.assertNotIn("cann_version", recorded_hardware["accelerators"][0])
        environment = json.loads(fields["environment"])
        for key in ("hostname", "cwd", "python_version", "python_executable", "command"):
            self.assertEqual(environment[key], runtime[key])
        self.assertNotIn("os_pretty", environment)
        self.assertEqual(environment["dependencies"], [
            "torch==2.6.0", "transformers==4.50.0", "deepspeed 0.18.1 conda-forge"
        ])
        self.assertEqual(environment["requirements_file"], str(requirements))


if __name__ == "__main__":
    unittest.main()
