# CLIP: decisions and validation

## Decision points

- Similarity scores are not automatically calibrated probabilities or measures of scientific correctness.

- Prompt ensembling and class descriptions change the baseline; record them as part of the method.

- Scientific images may differ from pretraining data; validate relevant distinctions instead of assuming zero-shot transfer.

## Verify the requested change

- Repeated preprocessing/reload produces consistent embeddings.

- Matched/mismatched controls and class balance reveal trivial shortcuts.

- Metrics reflect the actual retrieval direction or classification task.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [openai/CLIP](https://github.com/openai/CLIP)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/18-multimodal/clip/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
