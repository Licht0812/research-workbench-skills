---
name: blip-2
description: "Run or adapt BLIP-2 image captioning and visual question answering. Use for BLIP-2 推理与适配 with matched processors, Q-Former, and language backbone."
license: "MIT"
---

# BLIP-2

Own BLIP-2 inference or adaptation and its image-to-language data contract.

## Workflow

1. Identify the exact BLIP-2 checkpoint, processor, Q-Former configuration, and language backbone.
2. Validate image preprocessing, prompt form, input dtypes/devices, output decoding, and supported context limits.
3. For adaptation, define which modules are frozen/trainable and inspect gradient flow on a small paired dataset.
4. Evaluate visual grounding with counterfactual images, answerability controls, and held-out questions, not fluent output alone.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Budget the vision encoder, Q-Former, language backbone, trainable states, and image batches against available memory.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Version-matched inference/adaptation code, module-freezing contract, and visual-grounding evaluation.
