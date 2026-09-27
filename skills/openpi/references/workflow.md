# OpenPI: decisions and validation

## Decision points

- Recompute statistics when their dataset or transform inputs change; a logging-only config edit does not justify recomputing the corpus.

- JAX and PyTorch paths can require different kernels or model patches. Apply revision-specific changes only in the project environment, never a shared global installation.

- Flow-matching action generation is allowed here; image-generation workflows are excluded. Learned action output alone does not authorize commanding hardware.

## Verify the requested change

- Statistics, transforms, checkpoint, camera order, and action dimensions agree.

- Output actions have valid units, ranges, frame conventions, and chunk length.

- Save/serve and any backend conversion preserve representative policy outputs within a justified tolerance.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/18-multimodal/openpi/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
