# RWKV: decisions and validation

## Decision points

- A recurrent state can have fixed size while losing information. Do not describe the model as remembering arbitrary context without task evidence.

- Reset or separate states across independent documents, conversations, and evaluation examples to avoid contamination.

- Architecture-specific kernels and checkpoint formats can differ across RWKV generations; verify the selected implementation.

## Verify the requested change

- State isolation holds across batch items and sessions.

- Chunked inference matches the supported reference within an appropriate tolerance.

- Long-range recall is evaluated at multiple distances instead of inferred from computational complexity.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [BlinkDL/RWKV-LM](https://github.com/BlinkDL/RWKV-LM)
- [BlinkDL/ChatRWKV](https://github.com/BlinkDL/ChatRWKV)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/01-model-architecture/rwkv/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
