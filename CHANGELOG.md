# Changelog

## Unreleased

- Add the original SWABLAB Log skill for raw training logs, append-only step metrics, native checkpoint paths, Slurm job associations, and SwanLab static environment information.
- Register 47 standalone packages; experimental-management category 13 now contains three skills. Update bilingual usage examples, the catalogue, and attribution records.
- Distinguish original skill provenance from pinned upstream adaptations without inventing upstream paths or blob identities. Preserve the existing upstream checks.
- Make the recorder example use the actual skill path, allowing direct repository use without a local installation.

### Local validation (2026-10-07)

- All 47 packages passed metadata, local-reference, license, and source-record validation.
- All 89 optional behavioral case definitions passed schema validation.
- All 62 program tests passed, including eight provenance checks and four SWABLAB recorder tests.
- SWABLAB recorder tests exercised same-step merge, append-only resume, native checkpoint linking, scoped Slurm association, and SwanLab v2 static-file extraction with local fixtures.
- Git whitespace checks passed. Real GPU training, live Slurm jobs, and online SwanLab sessions were not run.

## 1.0.0 (2026-09-27)

Initial release of Research Workbench Skills.

- 46 standalone skills across 16 categories, covering research ideation, model training, agents, vision/action policies, scientific writing, and figures.
- Independent Creative Thinking for Research and Brainstorming Research Ideas workflows with local method references and output guides.
- CCF Conference Colors with 205 palettes from six source families, exact HEX selection, contrast/grayscale diagnostics, a color-mapping example, and an offline gallery.
- A copy tool supporting individual skills, categories, combined selections, explicit all, listing, and previews. Selected folders include their resources and notices.
- Model-independent instructions with resource planning based on project hardware and budgets, plus framework and workflow selection guidance.
- 89 optional behavioral evaluation definitions, a schema validator, package checks, automated tool tests, and continuous integration.
- Bilingual project documentation, a skill catalogue with combination guidance, contribution and release instructions, and pinned source records with source-specific licenses.

### Local validation

Checks completed on 2026-09-27:

- All 46 packages passed metadata, local-reference, license, and source-record validation.
- All 89 behavioral case definitions passed schema validation.
- All 50 program tests passed, covering selection/copying, rollback, standalone packages, metadata handling, palette integrity and tools, and evaluation definitions.
- Repository links, Python syntax, and Git whitespace checks passed.

Model and runtime evaluation status is recorded in [evals](evals/README.md#evaluation-status); figure inspection status is recorded in the [color adaptation notes](docs/color-adaptation.zh-CN.md).
