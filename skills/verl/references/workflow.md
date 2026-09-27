# verl: decisions and validation

## Decision points

- Do not mix an example from one verl version with a different Hydra/config schema without verifying each changed field.

- Check microbatch, minibatch, prompt batch, completion multiplicity, and sequence limits in their actual units.

- Use supported backend combinations from the checked-out version. A requested FSDP backend does not authorize switching to Megatron.

## Verify the requested change

- A small batch moves through generation, reward, advantage calculation, and update without field or shape ambiguity.

- Rollout parameters refresh as intended and evaluation does not silently use a stale checkpoint.

- Resource pools include reference and reward inference as well as training.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [volcengine/verl](https://github.com/volcengine/verl)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/06-post-training/verl/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
