# TransformerLens: decisions and validation

## Decision points

- Attention visualization and linear attribution are descriptive. A causal claim needs an intervention plus a controlled behavioral change.

- Check conversion parity before attributing effects to the original model.

- Cache size can dominate parameter memory; restrict layers, positions, dtype, and batch size to the hypothesis.

## Verify the requested change

- Unmodified hooked-model outputs match the intended reference closely enough for the experiment.

- Identity patches and irrelevant-position controls behave as expected.

- Effects persist on held-out prompts and are not explained by token-position mismatch.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [TransformerLensOrg/TransformerLens](https://github.com/TransformerLensOrg/TransformerLens)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/04-mechanistic-interpretability/transformer-lens/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
