# Cosmos-Policy: decisions and validation

## Decision points

- A policy may use video-derived representations internally; this skill exposes action evaluation, not a new image-generation service.

- Read logs belonging to the current run ID, not simply the latest file in a shared directory.

- EGL device mapping, policy CUDA device, simulator version, and assets can cause failures independently of model quality.

## Verify the requested change

- The renderer produces valid observations and the intended device is used.

- Checkpoint statistics and preprocessing match the selected environment.

- Metrics reconcile with episode-level records and distinguish setup failures from policy failures.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [NVlabs/cosmos-policy](https://github.com/NVlabs/cosmos-policy)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/18-multimodal/cosmos-policy/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
