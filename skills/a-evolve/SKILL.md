---
name: a-evolve
description: "Develop A-Evolve experiments that improve an agent's prompts, skills, memory, or tools through held-out evaluation. Use for Agent 自改进; model-weight training is separate."
license: "MIT"
---

# A-Evolve

Own the candidate-evaluate-select experiment for an existing agent; keep a stable baseline and held-out acceptance criteria.

## Workflow

1. Define the allowed mutable artifacts, benchmark interface, cost budget, stopping condition, and immutable task constraints.
2. Partition development tasks from held-out acceptance tests; record baseline performance and failure categories.
3. Generate a bounded candidate change, evaluate it in an isolated workspace, and compare quality, cost, regressions, and task coverage.
4. Accept only evidence-supported changes with a recoverable previous version; stop according to the experiment budget or diminishing information.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

If this workflow launches local models, GPU tools, or concurrent trials, size and schedule the combined workloads against the project's actual hardware and resource budget.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Bounded evolution setup, baseline/candidate results, acceptance decision, and the chosen artifact with rollback information.
