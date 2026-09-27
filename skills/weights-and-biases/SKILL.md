---
name: weights-and-biases
description: "Track ML runs, configuration, metrics, artifacts, resume, and sweeps with Weights & Biases. Use for W&B/wandb 实验管理."
license: "MIT"
---

# Weights & Biases

Own the W&B integration and metric/run schema; training code remains the authority for scientific computation.

## Workflow

1. Identify the project's chosen tracker, online/offline mode, run ID, configuration schema, step axis, and permitted data logging.
2. Add one controlled initialization and finalization path, logging metrics at meaningful frequencies from the correct distributed rank.
3. Use artifact versions or stable references to connect data, code, configuration, and checkpoints; verify resume behavior.
4. For sweeps, bound trial concurrency and total GPU use, then compare runs using matched metric definitions and evaluation protocols.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

If this workflow launches local models, GPU tools, or concurrent trials, size and schedule the combined workloads against the project's actual hardware and resource budget.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Tracker integration, run/metric schema, artifact references, and a verified local or authorized remote test.
