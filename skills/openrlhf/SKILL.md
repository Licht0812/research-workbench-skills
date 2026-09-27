---
name: openrlhf
description: "Configure or debug OpenRLHF actor, critic, reference, reward, and rollout components. Use for OpenRLHF 后训练与资源编排."
license: "MIT"
---

# OpenRLHF

Own the OpenRLHF job and placement plan. Select only components required by the chosen objective.

## Workflow

1. Match the OpenRLHF revision, environment, supported objective, model family, and rollout backend.
2. Map actor, optional critic, reference, reward, and generation components to dedicated or documented shared GPU placements.
3. Validate prompt formatting, reward interfaces, sampled log probabilities, and checkpoint synchronization on a small job.
4. Check resource accounting, rollout freshness, failure recovery, and held-out task quality before longer training.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Budget actor, critic, reference, reward, rollout, and evaluation workers together; verify peak memory and supported co-location before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Component/resource map, versioned launch config, reward/data interface, and observed smoke-run/evaluation results.
