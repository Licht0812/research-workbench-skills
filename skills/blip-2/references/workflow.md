# BLIP-2: decisions and validation

## Decision points

- BLIP and BLIP-2 name different architectures; this package implements the upstream BLIP-2 selection and resolves a shorthand only in that context.

- Language priors can answer without using the image. Test image changes and unanswerable questions.

- Changing the language model or processor may require connector and token handling changes; do not mix arbitrary checkpoints.

## Verify the requested change

- Trainable parameter lists and actual gradients match the adaptation plan.

- Image/question pairs remain aligned throughout batching.

- Generated claims agree with supplied visual evidence or state uncertainty.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [salesforce/LAVIS](https://github.com/salesforce/LAVIS)
- [Hugging Face transformers / model_doc / blip-2](https://huggingface.co/docs/transformers/model_doc/blip-2)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/18-multimodal/blip-2/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
