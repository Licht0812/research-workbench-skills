---
name: clip
description: "Use or adapt CLIP encoders for image/text similarity, zero-shot classification, and retrieval. Use for CLIP 表示与匹配; caption generation is separate."
license: "MIT"
---

# CLIP

Own CLIP preprocessing, embedding comparison, and representation evaluation.

## Workflow

1. Match checkpoint, image processor, text tokenizer, embedding dimension, and supported input range.
2. Construct representative image/text pairs or class prompts, preserving preprocessing and truncation behavior.
3. Normalize embeddings consistently when using cosine similarity and treat scaled logits according to the selected model.
4. Evaluate retrieval/classification on held-out data and domain shifts; record prompt choices and calibration separately.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size image/text batches and embedding storage from actual device memory; include distributed feature gathering when computing contrastive losses.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Encoder pipeline, prompt/preprocessing contract, embeddings or retrieval results, and task-specific validation.
