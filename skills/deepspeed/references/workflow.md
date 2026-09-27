# DeepSpeed: decisions and validation

## Decision points

- ZeRO stages shard different state categories; use the lowest complexity that meets the measured constraint.

- CPU or NVMe offload exchanges GPU memory for host memory, bandwidth, and I/O demand; account for all of them.

- Stage-3 sharded checkpoints are not ordinary single-file model weights. Export using the matching supported tool when a standalone checkpoint is required.

## Verify the requested change

- Batch equations and the data-parallel degree agree with the launcher.

- Only one optimizer/scheduler performs updates; precision settings are not contradictory.

- Distributed saving completes across required ranks and a fresh process resumes correctly.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [DeepSpeed documentation](https://www.deepspeed.ai/)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/08-distributed-training/deepspeed/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
