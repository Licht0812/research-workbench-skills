---
name: academic-plotting
description: "Create reproducible scientific plots with Matplotlib/Seaborn and editable source. Use for 训练曲线、消融图、定量可视化; image synthesis is outside scope."
license: "MIT"
---

# Academic Plotting

Own a quantitative chart from supplied data to reproducible source and requested exports. Preserve an already selected visual workflow and canonical figure source.

## Workflow

1. Identify the scientific comparison, data columns/units, uncertainty definition, intended final size, and existing figure source.
2. Choose a plot that exposes the comparison: curves for trajectories, points/intervals for estimates, heatmaps for matrices, or another justified quantitative form.
3. Implement from the actual data, preserving values, missingness, sample counts, and statistical meaning; use an accessible restrained style and preserve the project's label-to-color mapping. A separately selected color specialist may supply the palette contract; this skill keeps ownership of the chart source.
4. Export requested vector/raster formats, inspect at final size, and fix clipping, illegible labels, inconsistent scales, or misleading encodings.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Requested chart exports and the minimal plotting source/data references needed to reproduce them.
