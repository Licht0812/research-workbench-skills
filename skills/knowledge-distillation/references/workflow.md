# Knowledge Distillation: decisions and validation

## Decision points

- A text-only model endpoint does not provide full logits or hidden states. Use response distillation unless the needed outputs are actually available.

- Token-level KL requires aligned distributions; different tokenizers need an explicit alignment method or a different objective.

- When applying temperature-scaled KL, verify reduction, target direction, and any T-squared scaling against the intended derivation. Forward and reverse KL optimize different behavior.

## Verify the requested change

- Teacher gradients are disabled and caches correspond to the documented teacher version.

- Masks and loss normalization reflect actual completion lengths.

- Teacher inference and simultaneous training fit the GPU budget; offline teacher data still count toward total experiment cost.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Research paper: arXiv 1503.02531](https://arxiv.org/abs/1503.02531)
- [microsoft/LMOps](https://github.com/microsoft/LMOps/tree/main/minillm)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/19-emerging-techniques/knowledge-distillation/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
