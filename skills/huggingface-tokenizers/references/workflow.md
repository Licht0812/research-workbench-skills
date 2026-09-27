# Hugging Face Tokenizers: decisions and validation

## Decision points

- Domain strings may contain case-sensitive atoms, charges, separators, or measurement units: normalization must preserve meaning; tokenization alone does not validate chemistry or physics.

- Compare held-out tokens per example, unknown-token rates, and semantic delimiter preservation rather than vocabulary size alone.

- When adding tokens to an existing model, record token IDs and explicitly reconcile resized embeddings, tied output weights, and checkpoints.

## Verify the requested change

- Train/evaluation documents do not leak across vocabulary fitting.

- Saved/reloaded tokenizer produces identical IDs and offsets on fixed examples.

- Padding, EOS, BOS, and loss masks match the downstream training objective.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Hugging Face tokenizers](https://huggingface.co/docs/tokenizers)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/02-tokenization/huggingface-tokenizers/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
