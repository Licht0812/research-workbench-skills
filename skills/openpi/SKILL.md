---
name: openpi
description: "Adapt, fine-tune, convert, or serve a Physical Intelligence OpenPI policy. Use for OpenPI/pi0 动作模型 with matched datasets and action/observation contracts."
license: "MIT"
---

# OpenPI

Own OpenPI policy/data/config consistency. Work in simulation or offline checks unless robot execution is part of the user's authorized task.

## Workflow

1. Inspect the OpenPI revision's supported model/backend, checkpoint, dataset format, config registry, and environment setup.
2. Map observations, camera order, state, language, action units/frames, and prediction horizon to the policy's transforms.
3. Compute or validate normalization statistics for the actual dataset and transforms; train with a version-matched configuration and bounded allocation.
4. Serve or load the resulting checkpoint and verify actions offline/simulation; for conversion, compare outputs across backends before deployment.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Data/config mapping, normalization provenance, training/serving instructions, and offline or simulation validation.
