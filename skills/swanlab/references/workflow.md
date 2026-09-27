# SwanLab: decisions and validation

## Decision points

- Local/offline/self-hosted behavior depends on the installed release and optional dashboard dependencies; verify the actual mode instead of assuming names are interchangeable.

- Keep a single canonical experiment record. Add W&B fan-out only when the user specifically needs both.

- Schedule parameter sweeps and background evaluation together with training against the actual cluster allocation.

## Verify the requested change

- Metrics and steps match the training loop without duplicate callback logging.

- Offline/local mode does not unexpectedly require a remote login or upload.

- A resumed run preserves configuration and prior records.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [SwanLab documentation](https://docs.swanlab.cn/)
- [SwanHubX/SwanLab](https://github.com/SwanHubX/SwanLab)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/13-mlops/swanlab/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
