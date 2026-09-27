# Ray Data: decisions and validation

## Decision points

- Ray Data operations may execute lazily; constructing a Dataset is not evidence that preprocessing completed.

- Batch format and model tensor layout must agree. Avoid loading a full model per row or collecting a large dataset on the driver.

- When connected to Ray Train, distinguish Dataset sharding from sampler sharding so each example is consumed as intended.

## Verify the requested change

- A sample round trip preserves row IDs, shapes, types, and transform meaning.

- Retries are idempotent for written outputs; partial shards are distinguishable from complete ones.

- Worker reservations and concurrent training/inference jobs fit the actual project allocation and scheduler.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Ray Data documentation](https://docs.ray.io/en/latest/data/data.html)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/05-data-processing/ray-data/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
