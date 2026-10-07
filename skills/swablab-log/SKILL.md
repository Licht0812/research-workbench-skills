---
name: swablab-log
license: MIT
description: 为 SWABLAB 创建和更新深度学习训练 run，维护原始 stdout/stderr、step 级 CSV 指标、原生 checkpoint、Slurm 关联与 SwanLab 环境信息。适用于 PyTorch、HF Trainer、DeepSpeed、torchrun/DDP、SFT 和 GRPO/RL；不用于实验分析、对比或科研笔记。
---

# SWABLAB training runs

## Trigger

用户说“记录这个训练”“更新这个 run”“记录 job 123456”时执行。已有上下文足够就直接处理；只补问无法确定的 run 身份或必要接入信息。只读取当前训练相关的代码、配置和日志，不扫描整个 repository。保持简洁工程风格：标准参数名、数字优先，无 hypothesis、conclusion、结果判断、参数建议、周报或 Git 操作。

## Run naming

一次独立训练对应一个身份和一个目录；续训、补日志或更新同一训练沿用原身份。

```text
YYYYMMDD-HHMMSS_<stage>_<model>_<key-config>[_<tag>]
20261007-154932_grpo_qwen3-8b_lr1e-6_math
20261008-021530_pretrain_moe-16b_seq32k
```

使用完整启动时间、可读 model、通用 stage（sft/grpo/rl/eval/pretrain）和最关键变量。lr/bs/seq/exp/ckpt/tp/pp/dp 可用，不发明私人缩写，不用 a1/test2/new_exp_final，不堆超参数或句子。时间戳明确时区：脚本默认 Asia/Shanghai，可用 `--timezone` 指定训练约定；`start_time` 保存 ISO 时间和偏移。名称碰撞不自动加随机后缀或合并训练。

## Local layout

```text
runs/<run_name>/
├── run.txt
├── train.txt
├── metrics.csv
└── ckpt/
```

只维护这四项。未经明确要求，不创建 README.md、summary.md、experiment.md、metadata.json、config_snapshot.yaml、git.txt 或 daily/weekly/monthly。SwanLab 自己的 tracker 存储放在 `runs/` 外，保留其原生产物。

使用 [scripts/record_run.py](scripts/record_run.py)，它的本地操作仅依赖 Python 3.9+ 标准库。将下面的技能根目录替换为当前技能的实际绝对路径；可直接从仓库使用，不要求安装：

```bash
rec="/absolute/path/to/swablab-log/scripts/record_run.py"
run_dir=$(python3 "$rec" create --stage grpo --model qwen3-8b \
  --key-config lr1e-6 --tag math \
  --set dataset=math --set launcher=torchrun --set learning_rate=1e-6)
```

`run.txt` 只写真实使用的静态字段，不补 N/A：run_name/start_time/stage/model/dataset/launcher/command；Slurm 原始变量及 node/world_size/gpu_count；swanlab_project/swanlab_run（tracker ID）/swanlab_url；precision/batch_size/gradient_accumulation/effective_batch_size/optimizer/learning_rate/scheduler/warmup/max_steps/max_seq_length/seed；hardware/environment。命令记录实际启动命令；effective_batch_size 依实际数据并行和 batch 语义计算，不把 TP/PP 数量当作 DP 数量。

`train.txt` 保存原始 stdout + stderr，不重排、改写或反向从 tracker 重建。新启动用 `实际命令 > "$run_dir/train.txt" 2>&1`；续训使用 `>>`。Slurm 使用同一路径的 `--output`、`--error`，续训指定 `--open-mode=append`。多节点输出由现有 launcher/Slurm 汇入该文件，不并行用多个覆盖式重定向。

## SwanLab integration

在训练进程初始化 SwanLab，开启硬件、runtime、requirements、monitor，关闭 git 和额外 conda 导出。以下为 online 接入示例，接口与静态采集格式按 SwanLab v0.10.1 官方实现核实：[Settings](https://docs.swanlab.cn/api/py-settings.html)、[Run](https://github.com/SwanHubX/SwanLab/blob/v0.10.1/swanlab/sdk/internal/run/__init__.py)。

```python
import swanlab
from record_run import read_run, update_run, record_swanlab

settings = swanlab.Settings(
    probe=swanlab.Settings.Probe(hardware=True, runtime=True,
        requirements=True, monitor=True, git=False, conda=False),
    terminal=swanlab.Settings.Terminal(proxy_type="all"),
)
info = read_run(run_dir)
project = info.get("swanlab_project", "SWABLAB")
identity = ({"id": info["swanlab_run"], "resume": "must"}
            if info.get("swanlab_run") else {"resume": "never"})
tracker = swanlab.init(project=project, name=info["run_name"],
                       settings=settings, **identity)
update_run(run_dir, {"swanlab_project": project})
record_swanlab(run_dir, tracker)
```

将当前技能的 `scripts/` 加入训练进程的导入路径。上段仅由 **global rank 0** 执行；用已初始化的 distributed rank 或 launcher 的 RANK/SLURM_PROCID，不用 LOCAL_RANK 判断全局唯一写入者。其他 rank 不创建第二个 tracker 或 CSV writer。多机传递同一 `run_dir`，使用训练节点可访问的路径。

`record_swanlab` 从公开 `tracker.dir` 下 `files/swanlab-metadata.json` 的 v2 格式抽取静态 hardware/runtime，并从 tracker 的 requirements.txt 提取 torch/transformers/trl/deepspeed/accelerate/swanlab 原始依赖行；可通过 `dependencies=` 传入该训练额外使用的包名。完整依赖保留在 tracker，run.txt 记录来源路径。记录 GPU/CPU/memory、Python、hostname/cwd/command 等实际存在的信息，不查询 nvidia-smi、pip freeze、conda env export 或任何 Git 信息。文件约定见 [SwanLab probe schema](https://github.com/SwanHubX/SwanLab/blob/v0.10.1/swanlab/sdk/internal/probe_python/typings/__init__.py)；不访问私有 probe 属性，不为缺失项重做环境扫描。

动态 GPU/CPU utilization 留在 SwanLab，不持续复制进 metrics.csv。单个 rank 0 tracker 的硬件表示其所在节点，不能声称代表全部节点。在线续训复用原 project 和 tracker ID，`resume="must"`；offline/local 沿用本地 run，但不假设具有在线恢复语义，不自动新建 tracker 身份。[init 语义](https://docs.swanlab.cn/api/py-init.html)

## Metrics rules

以 optimizer/global step 驱动，不以 microbatch 或日志行号当 step。优先 timestamp,step,epoch,loss,lr,grad_norm；其余列按本次训练实际输出选择。SFT 可有 train_loss/eval_loss/token_accuracy/tokens_per_second/samples_per_second；GRPO/RL 可有 reward/reward_std/kl/entropy/clip_ratio/response_length/advantage 及清晰的 reward_correctness/reward_format/reward_length；分布式可有 global_step/samples/tokens/throughput。不虚构缺失 metric；保留原生明确名称，不把真实不同的指标覆盖成一个名称。多个 reward 只有训练原本如此命名时才使用 reward1/reward2/r1/r2。

CSV 为每个 run 自选宽表，不强制统一列。接入日志 hook 时依据该训练实际会输出的 scalar keys 确定列（包括评估时才出现的键），第一次写入固定表头；缺失值留空。此后只追加，不重写历史或自动改表头。新加指标时先解决该 run 的列约定，不静默丢弃用户要求记录的新指标。

训练代码导入 `MetricWriter(run_dir, columns)`，调用 `writer.log(step, metrics)`。它将同一步的 train/eval 等事件合并，下一 step 到达时追加上一行；训练结束或正常退出时 `writer.flush()`，异常出口也在 `finally` 中 flush。同一步须收齐后再 flush，不可每个事件都 flush。最多缓冲一个 step；骤停可能丢失这一行，原始 train.txt 和 tracker 日志保留各自已记录的输出。恢复时只读取 CSV 表头和末行，跳过已落盘 step，避免重放历史或重复追加。

已收齐的一行也可直接追加：

```bash
python3 "$rec" metric "$run_dir" --step 1840 \
  --columns epoch,loss,lr,grad_norm,reward \
  --set epoch=0.2 --set loss=0.4231 --set lr=8.2e-7 \
  --set grad_norm=0.91 --set reward=0.734
```

PyTorch/自定义 DeepSpeed 循环的 rank 0 将同一组真实 metrics 交给 CSV writer 和 `swanlab.log(metrics, step=global_step)`，checkpoint 保存仍按框架原有分布式要求参与，不把 rank 0 日志约束套到 collective checkpoint 保存上。

## Framework-specific handling

- **HF Trainer / TRL SFT / GRPO：**采用 SwanLab 自带的 `swanlab.integration.transformers.SwanLabCallback()`，并在训练开始前按上段由 global rank 0 初始化 tracker，确保禁用 git；设置 `report_to="none"` 防止重复 callback。另加 `record_run.trainer_callback(run_dir, columns)` 记录本地 CSV，使用 state.is_world_process_zero/global_step，learning_rate 映射为 lr。依据真实 logs 选择 loss/eval_loss/epoch/grad_norm/train_runtime/train_loss/train_samples_per_second/train_steps_per_second 及实际 reward keys；该 hook 仅写选定列。`try: trainer.train(...)` 的 `finally` 调用本地 callback.flush()。不另造 Trainer summary。[官方集成](https://github.com/SwanHubX/SwanLab/blob/v0.10.1/swanlab/integration/transformers.py)
- **DeepSpeed ZeRO-1/2/3：**记录实际 precision、world_size、gradient_accumulation、effective_batch_size、optimizer、scheduler、learning_rate；保留框架 checkpoint 格式，不复制或重打包。
- **Checkpoint：**新训练的框架 output/save root 指向 `run_dir/ckpt`。HF checkpoint-N、DeepSpeed global_stepN 等原名保留；自定义保存可用 `python3 "$rec" ckpt "$run_dir" --step 1000`（打印 ckpt/step-00001000 路径）或 `--final`。脚本只提供保存路径，不假装已经保存权重。接入已有训练时 `create --ckpt-source /实际原生checkpoint根目录` 使 ckpt 成为直接链接，不搬移现有权重或生成第二套。
- **Slurm：**在当前 job 内 `python3 "$rec" slurm "$run_dir"` 直接记录存在的 SLURM_JOB_ID/SLURM_JOB_NAME/SLURM_JOB_NODELIST/SLURM_NTASKS/SLURM_GPUS/SLURM_CPUS_PER_TASK/CUDA_VISIBLE_DEVICES；不把 SLURM_NTASKS 当作 torchrun 的 WORLD_SIZE。从登录节点关联指定 job 用 `slurm "$run_dir" --job-id 123456`，必要时只查该 job 的 squeue、scontrol show job 或 sacct，结果用 `--set` 补入。不要混入调用者的另一个 job 环境。不扫描集群、检查节点可用性或执行 scancel/kill/pkill。

## Update workflow

先用已有明确路径、run 身份或 job 关联定位当前 run，不重新命名、创建目录或 tracker。不重复查询已知信息；用 `update "$run_dir" --set key=value` 只更新当前 run.txt，身份和 start_time 保持不变；CSV 只追加新 step；train.txt 续写；checkpoint 仍用原生目录。

接入已经运行的 job 时记录其真实启动时间、原日志与 checkpoint 路径；只能从实际可获取的日志、现有 callback 或 tracker 接入指标，不能假装新加的 Python callback 已注入运行中的进程。既有原日志可原样链接为 train.txt，无需复制重排；从已有日志/追踪记录补入数据时只导入本地尚未记录的真实 step。无法接入时保留已完成的关联并明确缺少的具体信息，不启动第二个训练、不反复 fallback。完成后只简短返回 run 路径、tracker 链接和实际接入状态，不总结训练表现。
