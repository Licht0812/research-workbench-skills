# TorchTitan: decisions and validation

## Decision points

- Validate mesh divisibility and tensor/head/expert constraints against that revision's configuration; do not multiply replication dimensions twice.

- Use the repository's supported config schema and launch entrypoint instead of copying obsolete flags from an upstream recipe.

- Treat Float8 as a hardware- and implementation-dependent option. Preserve a comparison in the model's supported baseline precision.

## Verify the requested change

- Every worker maps to the intended device and all parallel groups fit the allocation.

- Resuming recovers optimizer, scheduler, step, and relevant data state.

- Reported tokens/second and memory come from this run; large-cluster benchmark numbers are not predictions.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [pytorch/torchtitan](https://github.com/pytorch/torchtitan)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/01-model-architecture/torchtitan/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
