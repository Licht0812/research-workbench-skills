# PyTorch FSDP2: decisions and validation

## Decision points

- Use model(inputs), not direct forward calls that bypass registered hooks, unless an explicitly supported method registration/unshard path is implemented.

- Bottom-up grouping controls communication and peak memory. Choose meaningful module boundaries rather than wrapping every layer blindly.

- DCP checkpoint portability across PyTorch versions or topology changes needs explicit verification; gathering full tensors can exceed host/device memory.

## Verify the requested change

- The optimizer refers to the intended sharded parameters, including tied/shared weights.

- Gradient accumulation and synchronization agree with the installed FSDP2 API.

- Restored parameters, optimizer state, and training step match a controlled reference.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [PyTorch documentation](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)
- [PyTorch documentation](https://docs.pytorch.org/docs/stable/distributed.checkpoint.html)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/08-distributed-training/pytorch-fsdp2/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
