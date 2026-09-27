---
name: torchtitan
description: "Configure TorchTitan pretraining, DeviceMesh parallelism, precision, profiling, and checkpoints. Use for TorchTitan 配置与并行预训练."
license: "MIT"
---

# TorchTitan

Own a TorchTitan training job, including its launcher and model-parallel layout; do not add a second top-level training engine.

## Workflow

1. Inspect the checked-out TorchTitan revision, its supported PyTorch/CUDA versions, model configuration, and available node topology.
2. Select a supported model/configuration and map each parallel dimension to the actual process mesh. Validate a representative configuration, then scale to the intended hardware.
3. Establish a short baseline before enabling compilation, lower precision, extra sharding, or additional parallel axes.
4. Verify a training step, checkpoint save/resume, and numerical behavior; profile communication, memory, and throughput before scaling within the allocation.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Versioned configuration, resource map, launch instructions, checkpoint/resume evidence, and measured profiling results.
