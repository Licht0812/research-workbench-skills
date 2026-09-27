---
name: huggingface-tokenizers
description: "Train or audit Hugging Face Tokenizers vocabularies, normalization, offsets, padding, and truncation. Use for 自定义分词器、词表设计与序列对齐."
license: "MIT"
---

# Hugging Face Tokenizers

Own the tokenizer artifact and its data contract; changing a model vocabulary also requires an explicit embedding/checkpoint compatibility decision.

## Workflow

1. Identify the actual corpus, held-out split, tokenizer algorithm, normalization rules, special tokens, and downstream model contract.
2. Choose BPE, WordPiece, or Unigram from vocabulary coverage and sequence-length evidence. Keep train-only vocabulary fitting separate from evaluation.
3. Implement the normalizer, pre-tokenizer, model, post-processor, and decoder with the installed Tokenizers API; retain offsets and special-token semantics.
4. Save the complete tokenizer plus configuration. Test round trips where lossless encoding is intended, unknowns, Unicode, domain syntax, padding, and truncation.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Tokenizer files, a compact corpus/normalization contract, held-out coverage statistics, and reload checks.
