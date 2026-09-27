# Source and adaptation notice

This standalone skill extracts the color-selection responsibilities of [Rimagination/easyplot](https://github.com/Rimagination/easyplot/tree/b54bbe4f9158a5d4bf5b532689ed34f66231ab35), fixed at commit `b54bbe4f9158a5d4bf5b532689ed34f66231ab35`, reviewed on 2026-09-27.

Easyplot supplies one complete plotting skill with a palette module, not a separate upstream CCF skill. Its Python palette reader is copied without logic changes. No R runtime helper is distributed. The registry contains 205 unchanged records selected from 1,537 upstream entries. The workflow, conference guidance, command-line diagnostics, contract example, and gallery are adapted or newly authored here. The compact luminance/contrast diagnostics follow the same sRGB/WCAG calculations used by easyplot's audit module, without its general plotting dependencies.

Easyplot code and instructions: Copyright (c) 2026 Rimagination, MIT. Adaptations: Copyright (c) 2026 Research Workbench Skills contributors, MIT. See the full [LICENSE](LICENSE).

**Palette data retain their own terms.** The package's MIT license does not relicense third-party color tables. Keep [palette notices](assets/palette-licenses/NOTICES.md), every referenced license, and [provenance](assets/provenance.json) with the registry, even when distributing this skill by itself. This product includes color specifications and designs developed by Cynthia Brewer (http://colorbrewer.org/).

Selected families: ColorBrewer (35), viridisLite (8), Matplotlib (10), six corroborated Paul Tol schemes (6), Scientific colour maps 8.0.1 (102), and cmocean (44). Original palette IDs, order, class-count schemes, CVD annotations, and source URLs are retained. None is presented as an official CCF palette.

Excluded: ggsci's GPL source tables and terminal-theme collection; China/Dongfang/CUD and Tol pale/dark entries for which the frozen upstream notices do not establish general redistribution rights; CET's separately licensed CC-BY/CC-BY-SA data; and unneeded colorspace-generated tables. Exclusion does not assert that these sources are unusable: this release deliberately has a narrower distribution scope. Exact counts and selection hashes are recorded in provenance.
