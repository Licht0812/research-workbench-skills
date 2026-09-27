---
name: simpo
description: "Implement or evaluate SimPO reference-free preference optimization, length normalization, and target margin. Use for SimPO 训练与偏好对齐对照."
license: "MIT"
---

# SimPO

Own the SimPO objective, data interpretation, and faithful baseline comparison.

## Workflow

1. Identify the exact SimPO implementation/revision, initial model, preference data, chat template, and supported runtime.
2. Compute completion-only average log probabilities with correct masks; verify the beta scaling and target reward margin convention against that implementation.
3. Check a hand-computable pair and gradients before a short training run; use development data to set learning rate, beta, and margin.
4. Compare with the starting checkpoint and any requested preference baseline at matched data, decoding, and evaluation conditions.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Objective definition and implementation identity, masked-data example, controlled training config, and comparison results.
