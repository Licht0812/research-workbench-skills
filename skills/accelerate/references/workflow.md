# Accelerate: decisions and validation

## Decision points

- Accelerate plus a documented DeepSpeed/FSDP plugin can be valid. Independently wrapping the model again or creating another optimizer owner is not.

- Data-parallel replicas contribute examples; tensor/pipeline parallel ranks are not additional batches.

- Gather metrics without double-counting padded/repeated samples; write shared files from the appropriate process.

## Verify the requested change

- Each process binds to the correct device and receives the intended data shard.

- Accumulation steps, optimizer updates, and scheduler steps remain consistent.

- Saving and reloading uses the selected backend's supported state handling.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Hugging Face accelerate](https://huggingface.co/docs/accelerate)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/08-distributed-training/accelerate/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
