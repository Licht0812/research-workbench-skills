# GRPO RL Training: decisions and validation

## Decision points

- All-equal group rewards yield no useful relative signal; check task difficulty, verifier granularity, and generation diversity.

- Loss sign or trend alone is not a pass/fail criterion for GRPO. Compare the implemented objective and measured task performance.

- Formatting rewards must not dominate scientific or task correctness. Preserve unsuccessful and truncated generations in diagnostics.

## Verify the requested change

- The reward cannot be won by empty output, repeated answers, delimiter tricks, or leaking the reference answer.

- Evaluation uses unseen prompts and a verifier independent of reward tuning where feasible.

- Rollout, actor, reference, reward, and evaluation workloads share a bounded total allocation.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Hugging Face trl / grpo_trainer](https://huggingface.co/docs/trl/grpo_trainer)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/06-post-training/grpo-rl-training/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
