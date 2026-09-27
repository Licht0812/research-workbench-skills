# Contributing

Contribute focused improvements to research workflows, reproducible tools, or documentation. Start from a concrete task the current collection handles poorly.

## Propose a change

Use an issue for a reproducible bug or substantial new capability. State the relevant skill, inputs, expected outcome, observed behavior, and environment. A small correction can go directly to a pull request. Include minimal public examples and relevant logs.

## Author a skill

Follow the [Agent Skills specification](https://agentskills.io/specification) and [OpenAI skill guidance](https://developers.openai.com/plugins/build/skills). Keep one independently usable directory per skill:

```text
skills/example-skill/
├── SKILL.md
├── LICENSE
├── NOTICE.md
├── agents/openai.yaml
└── references/       Add scripts/ and assets/ when the task needs them.
```

The core format requires `SKILL.md` with YAML metadata and a non-empty body. This collection also includes LICENSE, NOTICE, and OpenAI UI metadata in each distributed package. Keep referenced resources within the skill directory. The copy tool distributes complete folders and rejects symbolic links.

```yaml
---
name: example-skill
description: Compare supplied research options and propose a feasible first investigation.
license: MIT
---
```

Use a directory-matching name of 1–64 lowercase letters, digits, and single hyphens. Descriptions must be non-empty and at most 1,024 characters; this collection targets fewer than 200 characters. Put task and framework triggers first, with detailed decisions in the body or local references. The `license` field identifies applicable terms. Optional `compatibility` describes environment requirements in at most 500 characters, and `metadata` contains string key-value pairs. `allowed-tools` is experimental.

In `agents/openai.yaml`, supply a display name, a short description of 25–64 characters, and a default prompt mentioning `$skill-name`. Host settings govern model selection, reasoning, tools, and permissions. See the [local discovery guidance](https://learn.chatgpt.com/docs/build-skills) for supported installation locations.

Preserve the requested framework, evidence, and artifact format. Write task-specific decisions and keep each workflow proportional to the request. Link detailed examples and operational checks as local references. Retain pinned scientific software, model revisions, and data contracts when adapting instructions for another assistant model. Evaluate instruction changes using representative tasks and observed outputs; [OpenAI's compact instruction guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) provides additional authoring context.

Retain upstream copyright notices and record imported material at a fixed revision in `docs/sources.json` and `catalog.json`. Verify redistribution terms before adding copied material. Palette data retain their source-specific licenses and extraction records.

Update `catalog.json` and the [skill catalogue](docs/catalog.zh-CN.md) when names, categories, or responsibilities change. Update both READMEs when usage changes. Keep the release version in the catalogue and changelog.

## Validate

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python scripts/validate_evals.py
python -m unittest discover -s tests -v
```

`validate_skill_format` checks required metadata, optional field types, instruction bodies, and any present UI metadata. Repository validation also checks per-skill licenses, local references, catalogue coverage, source records, and documentation links. Tests exercise copying and rollback, standalone packages, format handling, palette tools, and evaluation definitions. Check the specification and validator revision when optional fields differ between tools.

Test changed executable behavior with meaningful inputs. Review instruction changes for content and evaluate their effect through actual task outputs. Record completed release checks in `CHANGELOG.md`.

Keep the [behavioral cases](evals/README.md) as optional definitions. Preserve useful prompts, add focused cases for changed decisions, and store observed outputs separately with the exact model and tool conditions.

## Community and security

Discuss technical decisions with evidence and respect, acknowledge corrections, and keep contributions relevant. Harassment, discriminatory abuse, threats, deliberate disruption, and disclosure of another person's private information are unacceptable in repository discussions. Maintainers may remove inappropriate contributions or restrict participation. Report private conduct concerns through an available maintainer contact or GitHub's reporting tools; a maintainer involved in a complaint should not be its sole reviewer.

For sensitive security reports, use GitHub private vulnerability reporting when enabled, or an available private contact listed by a maintainer. Include the affected file and revision, minimal reproduction, impact, and proposed correction using disposable inputs. Keep credentials, private research data, and actionable exploits out of public issues. Reports about third-party training frameworks should also reach their maintainers.

In a pull request, explain the problem, resulting behavior, source/license changes, and checks performed. New contributions to instructions and tooling use the repository's MIT license; source-specific data terms remain intact. No separate contributor agreement is required.

## Release

1. Update the version in `catalog.json`, `CHANGELOG.md`, and the release description in `NOTICE.md`.
2. Run the validation commands above, review the documentation links, and record the results in the changelog.
3. Review the source diff and Git status. Configure the intended public author identity and repository remote before committing or pushing.
4. Publish the source tree, including `.github/`, `.gitignore`, and `.gitattributes`. For manual uploads, exclude `.git/` internals, caches, environments, credentials, private inputs, model weights, and private evaluation outputs.
5. Check the hosted CI result and rendered documentation after publication. Keep the optional `evals/` definitions in the source repository; selected skill copies contain their own complete resources and notices.

Preserve each skill's licenses and notices, including the palette data terms described in [NOTICE](NOTICE.md). For optional plugin distribution, follow the manifest and packaging requirements in [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins).
