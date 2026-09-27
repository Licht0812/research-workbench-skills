---
name: ray-train
description: "Configure Ray Train workers, resources, dataset shards, checkpoints, and recovery. Use for Ray Train 多机训练任务与故障恢复."
license: "MIT"
---

# Ray Train

Own the Ray training job's resource/lifecycle orchestration; preserve a supported inner PyTorch or framework training implementation.

## Workflow

1. Inspect the installed Ray Train API, cluster allocation, per-worker CPU/GPU needs, and worker entrypoint.
2. Define worker count, resource reservations, rank/device behavior, and data sharding without a nested unmanaged launch.
3. Report metrics and checkpoints through the supported session/context API; use a durable path appropriate to the cluster.
4. Validate a small job, a controlled recovery, and aggregate concurrency before scaling or adding Ray Tune trials.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Worker function, resource/scaling configuration, checkpoint path contract, and recovery evidence.
