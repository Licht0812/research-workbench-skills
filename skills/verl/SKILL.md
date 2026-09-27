---
name: verl
description: "Build or debug verl PPO/GRPO jobs, actor-rollout-reference configuration, rewards, and resource pools. Use for verl 采样训练协同与后训练排查."
license: "MIT"
---

# verl

Own the verl controller, workers, resource pools, and backend-specific configuration for one job.

## Workflow

1. Read the selected verl revision's recipe and config schema; identify supported training, rollout, and model combinations.
2. Define dataset fields, tokenizer/chat handling, reward function, and actor/rollout/reference behavior.
3. Map worker pools and batch sizes to the actual data-parallel and model-parallel layout within the allocation.
4. Run a small generate-score-update cycle, inspect synchronization and resource peaks, and validate save/resume plus held-out behavior.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Budget concurrent actor, rollout, reference, reward, and evaluation workloads against the actual process topology and memory limits.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Validated verl configuration, data/reward example, allocation map, and observed job diagnostics.
