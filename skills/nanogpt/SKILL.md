---
name: nanogpt
description: "Modify nanoGPT models, training loops, or data preparation. Use for nanoGPT 原型、从零预训练 and small autoregressive research baselines."
license: "MIT"
---

# nanoGPT

Own a small nanoGPT experiment; avoid importing a larger trainer merely to reorganize a minimal implementation.

## Workflow

1. Inspect the local nanoGPT revision, data preparation, tokenizer metadata, model config, and checkpoint/resume path.
2. Define a falsifiable architecture, data, or optimization change against an unchanged baseline and a held-out split.
3. Verify token ranges, next-token targets, loss masking, effective batch size, and learning-rate schedule before a short run.
4. Measure validation loss and task quality; save enough model, optimizer, configuration, and data information to reproduce or resume.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

A focused code/config change, baseline comparison, data identity, and reproducible run or unexecuted launch plan.
