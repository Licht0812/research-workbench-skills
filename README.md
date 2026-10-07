# Research Workbench Skills

**47 standalone agent skills for research ideation, model training, agents, vision/action policies, scientific writing, and figures.**

[中文](README.zh-CN.md) · [Skill catalogue](docs/catalog.zh-CN.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

This independent project adapts 45 skills from [Orchestra Research](https://github.com/Orchestra-Research/AI-Research-SKILLs) and one scientific-color skill from [easyplot](https://github.com/Rimagination/easyplot), and adds the original [SWABLAB Log](skills/swablab-log/SKILL.md) training-run recorder. Each `skills/<name>/` directory contains its own instructions and resources. The collection follows the [Agent Skills format](https://agentskills.io/specification) used by [OpenAI skills](https://learn.chatgpt.com/docs/build-skills).

## Choose and use a skill

Browse the [47-skill catalogue](docs/catalog.zh-CN.md) by its 16 categories. To install a skill, copy its complete directory from `skills/` into a location supported by your host. For current Codex, documented local discovery locations include `~/.agents/skills` for personal use and `.agents/skills` inside a project. See [OpenAI's local skill guidance](https://learn.chatgpt.com/docs/build-skills).

The optional copy tool requires Python 3.9+ and no third-party packages:

```sh
python3 scripts/install.py --list-categories
python3 scripts/install.py --skill creative-thinking-for-research --dry-run
python3 scripts/install.py --skill creative-thinking-for-research
python3 scripts/install.py --category 08 --dest ./selected-skills
python3 scripts/install.py --category 20 --skill brainstorming-research-ideas --dest ./selected-skills
python3 scripts/install.py --all --dest ./selected-skills
```

The default destination is `~/.agents/skills`. Use `--dest` for a project, an inspection folder, or another host's documented location, including legacy paths. Select skills by name, category, or `--all`; overlapping selections are deduplicated. The tool copies the selected folders with their local resources and notices, and stops if a destination folder already exists. Root documentation, tests, and evaluation definitions remain in the repository.

In Codex, explicitly invoke a skill with `$skill-name`, or let the host match its description:

```text
Use $brainstorming-research-ideas to compare directions for my research question.
Use $torchtitan to inspect my existing pretraining configuration and checkpoint plan.
Use $swablab-log to record this training run or update its existing logs and metrics.
Use $ccf-conference-colors to preserve method colors across my paper's figures.
```

Choose skills around your task and established project setup. The [catalogue](docs/catalog.zh-CN.md) explains overlapping implementations and complementary components. Skills provide model-independent task instructions; the host manages model selection, reasoning settings, tools, and permissions. The research project supplies scientific libraries, weights, datasets, and compute. Preserve pinned experiment environments when changing the assistant model.

## Scientific colors

![Scientific palette reference](skills/ccf-conference-colors/assets/palette-preview.svg)

[CCF Conference Colors](skills/ccf-conference-colors/SKILL.md) includes 205 palettes from six source families, exact HEX selection, label-to-color mappings, and contrast/grayscale diagnostics. Its core Python tools use the standard library; Matplotlib is optional. Open the [offline gallery](skills/ccf-conference-colors/assets/palette-gallery.html) in a local browser to browse the collection. Check final figures against the target venue's template and at their intended size. See [color adaptation and licenses](docs/color-adaptation.zh-CN.md).

## Repository layout

```text
skills/          Independent skill folders: SKILL.md and relevant local resources
evals/           Optional behavioral prompts and acceptance checks
scripts/         Skill selection, structural validation, and case-format validation
tests/           Automated tests for the tools and package boundaries
docs/            Skill catalogue, source records, and color adaptation
.github/         Continuous integration
```

The core format requires `SKILL.md` and supports optional reference files and OpenAI UI metadata. This collection includes per-skill UI metadata, licenses, and notices for independent distribution. [CONTRIBUTING](CONTRIBUTING.md) explains the format, repository conventions, checks, and release steps.

## Development and evaluation

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python scripts/validate_evals.py
python -m unittest discover -s tests -v
```

PyYAML supports the repository's development checks. The 89 [behavioral case definitions](evals/README.md) provide optional maintenance prompts and acceptance criteria. The schema checker validates their structure; model evaluation uses actual task runs with separately recorded outputs. Release checks are recorded in the [changelog](CHANGELOG.md), and model evaluation status is maintained in [evals](evals/README.md#evaluation-status).

## Contribute, get help, and publish

Use this repository's issues for reproducible bugs and focused skill improvements. Include the skill, host/model, relevant versions, expected outcome, and observed behavior. See [CONTRIBUTING](CONTRIBUTING.md) for collaboration and private reporting guidance.

Publish the source folder using the [release steps](CONTRIBUTING.md#release). Optional plugin packaging is described there as well.

## License and attribution

Instructions and repository tools use the [MIT license](LICENSE), with original copyrights retained. **Palette data retain their source-specific licenses.** Read [NOTICE](NOTICE.md), [pinned sources](docs/sources.json), and [palette terms](skills/ccf-conference-colors/assets/palette-licenses/NOTICES.md). Preserve each selected skill's notices and bundled data terms when redistributing it.
