---
name: accelerate
description: "Integrate Hugging Face Accelerate into a PyTorch training loop. Use for Accelerate 多卡启动、精度、梯度累积 and supported distributed strategies."
license: "MIT"
---

# Accelerate

Own the Accelerate integration and launcher; a supported plugin may supply sharding, while the existing training loop retains its scientific objective.

## Workflow

1. Inspect the current loop and identify who owns launch, distributed initialization, device placement, optimizer stepping, and saving.
2. Choose a supported strategy from model memory and topology; prepare model, optimizer, loader, and scheduler according to the installed API.
3. Preserve effective batch size, accumulation, mixed precision, and loss scaling across the conversion.
4. Compare a short single-process baseline and multi-process run; verify metric gathering and checkpoint/resume.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Focused loop changes, launch config, batch accounting, and distributed equivalence/resume checks.
