# FlashAttention: decisions and validation

## Decision points

- Boolean and additive mask conventions can differ across APIs. Causal alignment also needs checking when query and key lengths differ.

- Dropout may require explicit zero probability at evaluation; do not infer semantics from module eval state alone.

- A kernel can reduce attention memory without eliminating all long-context memory costs or changing the full model's asymptotic computation.

## Verify the requested change

- Forward and backward comparisons pass a dtype-appropriate tolerance, including padding and causal edge cases.

- Unsupported devices/layouts follow a correct fallback or a clear error.

- Reported improvements include baseline, shapes, hardware, precision, warmup, and measured dispersion.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)
- [PyTorch documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/10-optimization/flash-attention/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
