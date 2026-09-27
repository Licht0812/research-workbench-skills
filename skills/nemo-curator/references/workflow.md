# NeMo Curator: decisions and validation

## Decision points

- Choose a canonical record per duplicate cluster before splitting, or enforce group-aware deduplication across existing splits without silently moving evaluation data into training.

- Semantic similarity can collapse distinct experimental conditions or rare outcomes. Inspect threshold errors before bulk deletion.

- Use the dependency/runtime prescribed by the selected NeMo Curator release; do not combine every legacy RAPIDS/Dask example into a new environment.

## Verify the requested change

- Counts reconcile from source through each stage; excluded data remain identifiable.

- Unit labels, structured measurements, and meaningful symbols survive normalization.

- Deduplication and filtering do not introduce train/evaluation leakage or unmeasured class shifts.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [NVIDIA-NeMo/Curator](https://github.com/NVIDIA-NeMo/Curator)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/05-data-processing/nemo-curator/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
