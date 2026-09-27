# PyTorch Lightning: decisions and validation

## Decision points

- Automatic and manual optimization differ in ownership of backward, optimizer, scheduler, and accumulation. Select intentionally.

- Batch-size, step/epoch logging, and distributed metric reduction affect comparisons; preserve their meaning during a refactor.

- A Trainer strategy may internally use DeepSpeed/FSDP. Do not also prepare the same model independently with another engine.

## Verify the requested change

- Loss and updates agree with the original loop on a controlled small example.

- Metrics are reduced once with the correct sample weighting.

- Checkpoint selection uses the intended metric and resume restores the necessary state.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [PyTorch Lightning documentation](https://lightning.ai/docs/pytorch/stable/)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/08-distributed-training/pytorch-lightning/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
