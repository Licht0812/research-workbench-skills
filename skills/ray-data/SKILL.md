---
name: ray-data
description: "Build Ray Data preprocessing, map_batches inference, and streaming input pipelines. Use for Ray Data 数据处理与吞吐诊断; training orchestration is separate."
license: "MIT"
---

# Ray Data

Own the data execution pipeline and batch contract, not the training optimizer or model-parallel strategy.

## Workflow

1. Identify input format, row identity, schema, transform semantics, and required output ordering or partitioning.
2. Build a small lazy pipeline and explicitly materialize or consume it to validate execution and output schema.
3. For model inference, use a stateful batch worker where appropriate, allocate its CPU/GPU resources, and bound concurrency and batch size.
4. Measure end-to-end throughput, serialization, object-store pressure, and downstream consumption; export deterministically identifiable output shards.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Account for object-store pressure, batch workers, model replicas, and downstream consumers before increasing concurrency.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Runnable data pipeline, schema and ID contract, measured throughput, and validated output shards.
