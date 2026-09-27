---
name: llava
description: "Configure, fine-tune, or evaluate a selected LLaVA model and its processor, projector, and chat format. Use for LLaVA 视觉指令微调与问答."
license: "MIT"
---

# LLaVA

Own the selected LLaVA variant's vision-language alignment and instruction-tuning implementation.

## Workflow

1. Identify the LLaVA variant/revision, vision tower, language backbone, projector, tokenizer/processor, and image token convention.
2. Inspect a rendered image/conversation example and its labels, loss mask, crop/resize policy, and multi-image support.
3. Select trainable components and a supported full/adapter tuning recipe; measure visual-token expansion and memory before scaling.
4. Evaluate grounded answers on held-out images/questions and reload the complete projector/adapter/model package.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Variant-specific configuration/code, data example, component checkpoint map, and visual-grounding evaluation.
