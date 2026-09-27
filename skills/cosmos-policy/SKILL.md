---
name: cosmos-policy
description: "Evaluate existing NVIDIA Cosmos Policy checkpoints in supported simulations. Use for Cosmos Policy rollout、归一化与延迟排查; from-scratch training is outside scope."
license: "MIT"
---

# Cosmos-Policy

Own a reproducible simulation evaluation of an existing Cosmos Policy checkpoint.

## Workflow

1. Match checkpoint, official repository/container revision, simulator assets, task suite, and headless renderer setup.
2. Validate camera transforms, image augmentation/crop/flip/compression conventions, proprioception, normalization, language embeddings, and action chunk settings from the chosen recipe.
3. Run one bounded episode and inspect observations, action ranges, termination, logs, and measured latency.
4. Scale to the requested tasks/trials with fixed protocol, retaining failed episodes and aggregating success and uncertainty.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Account for simulator processes, rendering, policy inference, and concurrent rollouts on the available CPU/GPU resources.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Evaluation configuration, environment/checkpoint identity, episode records, and measured success/latency with limits.
