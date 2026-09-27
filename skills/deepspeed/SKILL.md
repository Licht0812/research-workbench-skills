---
name: deepspeed
description: "Configure or debug DeepSpeed ZeRO, precision, offload, optimizer steps, and checkpoints. Use for DeepSpeed 显存优化、分片训练 and supported integrations."
license: "MIT"
---

# DeepSpeed

Own the DeepSpeed engine or the existing framework's DeepSpeed plugin configuration, never both as independent engines.

## Workflow

1. Measure which states dominate memory and inspect the model, optimizer, precision, installed DeepSpeed/PyTorch versions, and data-parallel degree.
2. Select ZeRO stage and optional CPU/NVMe offload based on memory savings and communication/I/O costs.
3. Reconcile train batch, microbatch, accumulation, optimizer, scheduler, and precision settings across the engine and caller.
4. Validate a step and checkpoint/resume under the chosen stage; profile before adding pipeline or expert complexity.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Engine/plugin configuration, memory/batch rationale, and verified training/checkpoint behavior.
