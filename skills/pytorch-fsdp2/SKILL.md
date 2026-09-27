---
name: pytorch-fsdp2
description: "Implement PyTorch FSDP2 fully_shard, DeviceMesh, precision/offload, and distributed checkpoints. Use for 原生 FSDP2 分片改造与调试."
license: "MIT"
---

# PyTorch FSDP2

Own native FSDP2 sharding and state handling within the chosen training loop.

## Workflow

1. Verify installed fully_shard and distributed-checkpoint APIs; initialize the intended device and process mesh once.
2. Apply sharding to appropriate submodules before the root, then create the optimizer from the post-sharding parameters.
3. Materialize and initialize or load parameters correctly; call the module through its hook-aware invocation path.
4. Configure resharding, precision, accumulation, clipping, and checkpointing with that version's API; validate a small distributed save/resume.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Sharding code, mesh and precision configuration, memory observations, and checkpoint/resume evidence.
