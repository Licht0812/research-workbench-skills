# TRL: decisions and validation

## Decision points

- SFT, preference optimization, and online RL need different data and compute. A generic request for alignment does not select a full PPO pipeline.

- TRL APIs change across releases; inspect actual signatures and current primary docs before copying constructor arguments.

- For GRPO, use one reward implementation and one rollout path. Advice from a method skill must not create a second trainer.

## Verify the requested change

- Only intended tokens contribute to the objective and padding is masked correctly.

- A sampled reward or preference batch is checked independently of aggregate loss.

- Training, reference, reward, and rollout allocations fit the cap including simultaneous processes.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Hugging Face trl](https://huggingface.co/docs/trl)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/06-post-training/trl-fine-tuning/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
