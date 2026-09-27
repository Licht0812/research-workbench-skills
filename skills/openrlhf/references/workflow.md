# OpenRLHF: decisions and validation

## Decision points

- Sum dedicated allocations, but count a genuinely shared GPU once; still budget its combined peak memory and scheduling constraints.

- GPU sharing requires the backend's supported colocation/sleep behavior. Declaring overlapping resource numbers does not make concurrent models fit.

- Different RL objectives need different component sets. Do not allocate a critic or reference simply because an example includes one.

## Verify the requested change

- Placement groups can schedule without deadlock or hidden extra GPU workers.

- Rollout weights and policy log probabilities correspond to the intended update version.

- A resumed job restores training state and creates identifiable logs and checkpoints.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/06-post-training/openrlhf/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
