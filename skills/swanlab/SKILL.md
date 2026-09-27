---
name: swanlab
description: "Track training configuration, metrics, media, and resume with SwanLab. Use for SwanLab 实验记录 in the selected local or hosted mode."
license: "MIT"
---

# SwanLab

Own SwanLab run identity and logging semantics while preserving the existing training framework.

## Workflow

1. Inspect installed SwanLab capabilities and the project's selected local, offline, self-hosted, or cloud mode.
2. Define run identity, configuration, metric names, step/epoch units, and which process logs shared results.
3. Connect the supported direct API or framework callback once; limit media size/frequency and avoid unnecessary data copies.
4. Verify a short run, finalization, resume, and the intended dashboard or stored record.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

SwanLab integration, mode and metric schema, and observed record/resume behavior.
