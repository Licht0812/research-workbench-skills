---
name: pytorch-lightning
description: "Build or refactor LightningModule, DataModule, Trainer, strategies, and callbacks. Use for PyTorch Lightning 训练组织、检查点与恢复."
license: "MIT"
---

# PyTorch Lightning

Own the Lightning training loop and Trainer lifecycle; use supported strategies instead of stacking a second loop manager.

## Workflow

1. Identify model, loss, optimizer, scheduler, data split, logging semantics, and existing training ownership.
2. Move only needed behavior into Lightning hooks and data modules, preserving the scientific computation.
3. Configure devices, nodes, precision, accumulation, callbacks, validation frequency, and one supported distributed strategy.
4. Compare a short baseline; test checkpoint resume, distributed metric reduction, and final inference/export.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Focused Lightning implementation, Trainer configuration, and equivalence/resume validation.
