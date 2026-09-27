---
name: openvla-oft
description: "Fine-tune and evaluate OpenVLA-OFT/OFT+ policies with matched action heads, LoRA, image streams, and normalization. Use for OpenVLA-OFT 机器人策略实验."
license: "MIT"
---

# OpenVLA-OFT

Own OpenVLA-OFT's model, action-head, adapter, and evaluation configuration.

## Workflow

1. Identify OFT versus OFT+, repository revision, base checkpoint, adapter/head assets, and the reproduction environment.
2. Match training/evaluation flags for action head, FiLM, image streams, proprioception, LoRA rank, crop policy, action horizon, and unnormalization key.
3. Validate a dataset batch, trainable modules, and short tuning run before longer fine-tuning within the allocation.
4. Save all required components, merge adapters only through the supported path, and compare unmerged/merged action outputs before a simulation evaluation.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Environment/revision record, train/eval configuration, complete checkpoint component map, and measured simulation results.
