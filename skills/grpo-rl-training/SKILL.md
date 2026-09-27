---
name: grpo-rl-training
description: "Design and diagnose GRPO rewards, grouped completions, objectives, and evaluation. Use for GRPO 奖励设计与奖励投机排查 within the selected training backend."
license: "MIT"
---

# GRPO RL Training

Own GRPO method and reward decisions. Use a chosen existing backend; use TRL only as a disclosed starting choice when no backend is established.

## Workflow

1. Define the target behavior, verifier, task split, and rival shortcut before writing reward code.
2. Specify grouped completions per prompt, sampling settings, reward components, normalization, optional KL/reference treatment, and token accounting.
3. Unit-check the verifier on valid, invalid, malformed, and adversarial shortcut examples before a small rollout.
4. Inspect reward distributions, zero-variance groups, completion lengths, entropy, and held-out success; tune only against training/development feedback.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Account for grouped rollouts, policy updates, reward evaluation, and any reference model in the actual resource budget.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Reward/verifier contract, objective and sampling choices, backend-specific config, and diagnostic evidence.
