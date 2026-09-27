---
name: autogpt
description: "Build or debug AutoGPT Platform blocks, graphs, integrations, and persistent tasks. Use for an existing or explicitly requested AutoGPT project."
license: "MIT"
---

# AutoGPT

Own an explicitly selected AutoGPT Platform workflow and its lifecycle.

## Workflow

1. Identify Platform versus legacy Classic, the actual repository revision, deployment mode, and intended workflow.
2. Define block inputs/outputs, credentials by reference, error paths, timeouts, retries, and termination behavior.
3. Implement the smallest graph that exercises the required tools, including persistent state and idempotency where relevant.
4. Test with bounded sample inputs and mocked external mutations; inspect execution logs before enabling authorized live or scheduled operation.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

If this workflow launches local models, GPU tools, or concurrent trials, size and schedule the combined workloads against the project's actual hardware and resource budget.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Workflow/graph source, component contracts, bounded test results, and necessary deployment configuration.
