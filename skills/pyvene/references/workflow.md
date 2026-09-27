# pyvene: decisions and validation

## Decision points

- Learned intervention success can reflect overfitting or information injection; include held-out pairs and capacity-matched controls.

- Different examples may tokenize to different lengths; align the represented concept rather than copying an index blindly.

- If a TransformerLens experiment already owns the hooks, choose one implementation path or an explicit adapter, not nested patching by default.

## Verify the requested change

- The no-intervention and identity-intervention paths reproduce the baseline.

- Interventions affect only intended batch items, positions, and components.

- Training data for an intervention are disjoint from the final causal test.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [stanfordnlp/pyvene](https://github.com/stanfordnlp/pyvene)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/04-mechanistic-interpretability/pyvene/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
