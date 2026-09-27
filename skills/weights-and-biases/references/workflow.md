# Weights & Biases: decisions and validation

## Decision points

- Default to the existing project's logging mode; do not silently enable external upload of inputs, checkpoints, or unpublished data.

- Multiple ranks or nested framework integrations can duplicate runs. Choose a single owner or an explicit documented distributed logging pattern.

- A training tracker records learning curves and artifacts; detailed agent tool-call traces belong to an observability integration.

## Verify the requested change

- A short run has one intended identity, monotonic step semantics, and complete finalization.

- Resuming attaches to the intended run without overwriting another experiment.

- Logged results match local evidence; missing/failed runs are not silently excluded from comparisons.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Weights & Biases documentation](https://docs.wandb.ai/)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/13-mlops/weights-and-biases/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
