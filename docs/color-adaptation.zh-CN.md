# easyplot 配色模块的 CCF 会议适配

审核日期：2026-09-27。来源固定为 [Rimagination/easyplot](https://github.com/Rimagination/easyplot/tree/b54bbe4f9158a5d4bf5b532689ed34f66231ab35)，commit `b54bbe4f9158a5d4bf5b532689ed34f66231ab35`。

上游是一个完整绘图技能，颜色功能位于其中的参考资料、注册表和工具脚本。本版提取这些配色资源，整理为可独立使用的 [CCF Conference Colors](../skills/ccf-conference-colors/SKILL.md)。

## 保留与改造

| 内容 | 本版做法 |
|---|---|
| 色板数据 | 从 1,537 条记录中保留 205 条；每条的 HEX、顺序、native sizes、来源和 CVD 注记保持原样 |
| Python 读取器 | 保留固定版本的读取逻辑；基础查询只需标准库，可选 Matplotlib 接口复用项目环境 |
| 对比度检查 | 依据原模块的 sRGB/WCAG 计算整理独立工具，输出指定背景下的对比度诊断 |
| 科研语义 | 分类、顺序、带中心发散、周期量的选择原则；约定缺失值、归一化与跨面板一致性 |
| 论文适配 | 按具体会议、年份和track的模板，核对图宽、最终尺寸、灰度、标签与导出 |
| 跨图一致性 | 颜色契约示例固定方法到颜色的映射，避免随排名变化或类别缺失而换色 |
| 预览 | 从色板数据生成可离线搜索的图库和 SVG 参考图，页面资源随技能提供 |
| 职责边界 | 配色技能负责颜色，Academic Plotting 或现有流程负责图形构建与导出；可以单独使用 |

## 发布子集

| 色板家族 | 数量 | 许可处理 |
|---|---:|---|
| ColorBrewer | 35 | 完整 ColorBrewer 许可与要求的署名 |
| viridisLite | 8 | MIT；保留原始版权条目，补齐标准 MIT 条款 |
| Matplotlib | 10 | 完整 Matplotlib 许可集合 |
| Paul Tol | 6 | 保留作者 BSD 声明；以标准 BSD 三条款和作者署名组成完整文本；不扩展至 pale/dark |
| Scientific colour maps | 102 | 作者 8.0.1 数据与 MIT 许可文字，记录 DOI |
| cmocean | 44 | MIT 许可和原始来源 |
| **合计** | **205** | 数据许可独立于仓库根 MIT |

未打包的 1,332 条：ggsci 1,288 条（其中包含 1,202 个终端主题，源数据采用 GPL）；China/Dongfang/CUD 共 24 条及 Tol pale/dark 2 条（上游固定版本未确认通用公开再分发条款）；CET 12 条（另有 CC-BY/CC-BY-SA 条款，本版未纳入）；colorspace 6 条（当前工作流未需要）。

205 条记录均有单独内容哈希，来源文件有完整 Git blob 标识；见技能内的 [provenance.json](../skills/ccf-conference-colors/assets/provenance.json) 和 [逐来源许可](../skills/ccf-conference-colors/assets/palette-licenses/NOTICES.md)。

## 检查含义

本工具根据颜色值计算其对白底或指定背景的 sRGB 对比度、灰度 L* 间距和采样明度方向。源记录的 CVD 属性可能随类别数变化；色觉缺陷模拟需另行运行。最终图形应在实际尺寸下检查交叉曲线、细线、文字背景和透明带。

选择指南链接到具体会议模板与 W3C 原始说明，供配色和成图检查使用。本版提供 Python 工具，并保留色板数据的原始来源许可。版本工具测试结果见[更新记录](../CHANGELOG.md)。

## 图形检查状态

截至2026-09-27，色板生成和数值检查已通过，SVG预览已渲染检查。图库交互与响应式布局待验证，此前的本地文件浏览器检查被访问策略阻止。可选Matplotlib接口、色觉缺陷模拟、打印色彩配置和最终稿件检查尚未执行。
