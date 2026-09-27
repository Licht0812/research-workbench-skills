# MoE Training: decisions and validation

## Decision points

- Sparse activation reduces selected computation, not total stored weights or necessarily end-to-end cost.

- Top-k indices alone are not a differentiable routing objective. Check router gradients, gate weights, and the intended balancing loss.

- Overlapping data/tensor/expert parallel groups require the backend's actual mesh semantics; do not multiply GPU factors from unrelated examples.

## Verify the requested change

- Tokens reach the intended experts and recombine in the original sequence order.

- Expert utilization and token dropping expose collapse or capacity problems.

- Dense and MoE comparisons state whether total parameters, active parameters, FLOPs, or wall time are matched.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [DeepSpeed documentation](https://www.deepspeed.ai/tutorials/mixture-of-experts/)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/19-emerging-techniques/moe-training/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
