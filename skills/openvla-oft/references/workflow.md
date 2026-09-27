# OpenVLA-OFT: decisions and validation

## Decision points

- Use the actual checkpoint/config as authority for camera count and FiLM; OFT/OFT+ labels alone are insufficient.

- The upstream reproduction recipe pins older core libraries. Use an isolated environment; a newer model used by Codex is not a reason to upgrade that scientific stack blindly.

- Cross-device or library changes call for an output parity test first, not automatic re-merging or replacing checkpoints.

## Verify the requested change

- Action-head type, statistics key, camera order, crop convention, and proprioception agree.

- Merged/unmerged checkpoints produce comparable actions on fixed observations.

- Reported task success uses explicit tasks, trial counts, seeds, termination rules, and failure records.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [moojink/openvla-oft](https://github.com/moojink/openvla-oft)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/18-multimodal/openvla-oft/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
