# Ray Train: decisions and validation

## Decision points

- Total trial concurrency times per-trial reservation can exceed the available cluster even when each individual job fits; include preprocessing and evaluation reservations.

- Ray Data shards and distributed samplers must compose intentionally, avoiding double sharding or repeated examples.

- Cluster orchestration does not automatically make the training function restartable: save optimizer, scheduler, step, and needed data state.

## Verify the requested change

- Resource requests can schedule with head-node and worker requirements accounted for.

- A retried worker does not duplicate final artifacts or silently restart from scratch.

- Only the intended process owns shared output and final model export.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Ray Train documentation](https://docs.ray.io/en/latest/train/train.html)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/08-distributed-training/ray-train/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
