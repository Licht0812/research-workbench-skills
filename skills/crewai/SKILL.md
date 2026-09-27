---
name: crewai
description: "Implement or debug CrewAI agents, tasks, crews, flows, and tools. Use for an existing or requested CrewAI 角色协作 application."
license: "MIT"
---

# CrewAI

Own the selected CrewAI application, including task boundaries and tool contracts.

## Workflow

1. Identify the requested crew/flow, role responsibilities, task inputs/outputs, dependencies, and success criteria.
2. Prefer the smallest number of roles that adds a distinct capability; define tools with explicit input schemas and failure behavior.
3. Separate state orchestration from role prompts; configure budgets, retries, stopping, and structured task outputs using supported APIs.
4. Run a bounded end-to-end example and inspect handoff completeness, duplicate work, tool failures, and total model/tool cost.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

If this workflow launches local models, GPU tools, or concurrent trials, size and schedule the combined workloads against the project's actual hardware and resource budget.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Crew/flow configuration or code, tool and artifact ownership, and bounded execution evidence.
