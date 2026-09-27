---
name: langchain
description: "Build or debug LangChain integrations and LangGraph stateful agent workflows. Use for an existing or requested LangChain/LangGraph application."
license: "MIT"
---

# LangChain

Own model/tool control flow and explicit state transitions in the selected LangChain/LangGraph application.

## Workflow

1. Inspect the installed package split and current project APIs; identify model provider, tools, state schema, and persistence requirements.
2. Define typed tool interfaces, expected errors, termination conditions, and state transitions before composing the agent.
3. Preserve conversation/session isolation and checkpoint semantics; use a supported graph or agent API rather than mixing legacy constructors.
4. Test a bounded success path, tool failure, retry, and resume/streaming behavior relevant to the request.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

If this workflow launches local models, GPU tools, or concurrent trials, size and schedule the combined workloads against the project's actual hardware and resource budget.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Application/graph code, state and tool contracts, and observed bounded tests.
