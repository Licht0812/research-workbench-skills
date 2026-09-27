# SimPO: decisions and validation

## Decision points

- Reference-free means no separate reference model in this objective; it does not eliminate evaluation or data-quality costs.

- Do not assume a generic DPOTrainer exposes SimPO in the installed version. Use a verified implementation or an explicitly tested custom loss.

- Track response length and preference-label noise; average log probability changes the objective but does not guarantee absence of length bias.

## Verify the requested change

- Padding and prompt tokens are excluded from completion length and likelihood.

- A better chosen/rejected log-probability gap changes the loss in the expected direction.

- Held-out quality and length distributions are reported without importing upstream benchmark gains.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [princeton-nlp/SimPO](https://github.com/princeton-nlp/SimPO)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/06-post-training/simpo/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
