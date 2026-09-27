# LLaVA: decisions and validation

## Decision points

- LLaVA variants differ in image patching, conversation templates, and processing APIs; a generic name does not define a compatible checkpoint.

- Packing text examples must preserve image-to-token alignment and avoid cross-example loss leakage.

- A missing projector or mismatched vision tower can load partially yet produce invalid behavior; verify the full component set.

## Verify the requested change

- Image counts, visual tokens, labels, and masks agree on a representative batch.

- The requested modules receive gradients and frozen modules do not.

- Reloaded outputs and grounded-answer quality are checked after fine-tuning.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [haotian-liu/LLaVA](https://github.com/haotian-liu/LLaVA)
- [Hugging Face transformers / model_doc / llava](https://huggingface.co/docs/transformers/model_doc/llava)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/18-multimodal/llava/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
