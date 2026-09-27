# Academic Plotting: decisions and validation

## Decision points

- Keep one authoring script and update the existing canonical outputs. Do not create a new plotting stack when the project already has a suitable one.

- Use supplied replicates for uncertainty; label whether intervals represent SD, SE, bootstrap CI, or another defined quantity. Do not invent error bars.

- Smoothing, axis truncation, log scales, and aggregation change interpretation: state material transformations and retain enough source data to reproduce them.

## Verify the requested change

- Plotted values and labels reconcile with the input table, including units and categories.

- Fonts, legends, uncertainty bands, and panel labels remain readable at the destination size.

- Exports render correctly and rerunning the source reproduces them.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Matplotlib user guide](https://matplotlib.org/stable/users/index.html)
- [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/20-ml-paper-writing/academic-plotting/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
