# 技能目录

当前版本包含 **47 个独立技能**，按 Orchestra 原有类别组织；easyplot 配色改编归入论文写作与可视化类别，原创 SWABLAB Log 归入实验管理。计算规模按项目实际硬件与预算配置。

| 类别 | 技能 / 目录名 | 用途与分工 |
|---|---|---|
| 01 模型架构 | [nanoGPT](../skills/nanogpt/SKILL.md)<br>`nanogpt` | 小型自回归模型与训练循环原型。以精简训练循环开展快速机制原型实验。 |
| 01 模型架构 | [RWKV](../skills/rwkv/SKILL.md)<br>`rwkv` | 循环状态、流式推理与序列模型研究。采用独立的架构与工程实现，使用对应版本的状态和检查点。 |
| 01 模型架构 | [TorchTitan](../skills/torchtitan/SKILL.md)<br>`torchtitan` | PyTorch 原生并行预训练。与 nanoGPT/RWKV 是模型训练入口的替代选择；FSDP2 可作为内部技术。 |
| 02 分词与序列表示 | [Hugging Face Tokenizers](../skills/huggingface-tokenizers/SKILL.md)<br>`huggingface-tokenizers` | 分词器训练、词表与序列对齐。处理离散分词与词表，训练循环和科学连续编码器由相应项目管理。 |
| 04 机制可解释性 | [pyvene](../skills/pyvene/SKILL.md)<br>`pyvene` | 声明式表示干预与因果假设检验。与 TransformerLens 的任务重叠，但实现与适用模型不同。 |
| 04 机制可解释性 | [TransformerLens](../skills/transformer-lens/SKILL.md)<br>`transformer-lens` | 激活缓存、修补和模型回路分析。与 pyvene 都可干预；本项使用 TransformerLens 的钩子实现，按模型和任务择一。 |
| 05 数据处理 | [NeMo Curator](../skills/nemo-curator/SKILL.md)<br>`nemo-curator` | 训练数据清洗、去重与筛选。负责清洗规则，Ray Data 可执行同一套规则。 |
| 05 数据处理 | [Ray Data](../skills/ray-data/SKILL.md)<br>`ray-data` | 并行预处理、批量推理与数据供给。与 NeMo Curator 可组合；与 Ray Train 分别负责数据和训练任务。 |
| 06 后训练 | [GRPO RL Training](../skills/grpo-rl-training/SKILL.md)<br>`grpo-rl-training` | GRPO 奖励、分组采样与学习诊断。负责方法设计，由选定的 TRL、OpenRLHF 或 verl 后端执行训练。 |
| 06 后训练 | [OpenRLHF](../skills/openrlhf/SKILL.md)<br>`openrlhf` | OpenRLHF 多组件资源与后训练流程。与 verl/TRL 属于主后训练框架替代项；GRPO 方法指导可共用。 |
| 06 后训练 | [SimPO](../skills/simpo/SKILL.md)<br>`simpo` | 无参考模型的偏好优化。与 DPO/GRPO 是不同训练目标；可与统一实验记录平台组合。 |
| 06 后训练 | [TRL](../skills/trl-fine-tuning/SKILL.md)<br>`trl-fine-tuning` | TRL 后训练 Trainer 实现与调试。TRL 是实现后端；GRPO 是方法，SimPO 是另一目标，OpenRLHF/verl 是替代主后端。 |
| 06 后训练 | [verl](../skills/verl/SKILL.md)<br>`verl` | verl 混合训练与采样配置。与 OpenRLHF/TRL 选一个主后端；可承接 GRPO 目标与奖励设计。 |
| 08 分布式训练 | [Accelerate](../skills/accelerate/SKILL.md)<br>`accelerate` | 训练启动、设备和精度协调。可组合 DeepSpeed/FSDP 插件；与 Lightning 按项目需要选择一个训练循环管理方式。 |
| 08 分布式训练 | [DeepSpeed](../skills/deepspeed/SKILL.md)<br>`deepspeed` | ZeRO、卸载与训练状态管理。与原生 FSDP2 通常二选一；可通过 Accelerate/Lightning 支持的方式集成。 |
| 08 分布式训练 | [PyTorch FSDP2](../skills/pytorch-fsdp2/SKILL.md)<br>`pytorch-fsdp2` | 原生参数分片与分布式检查点。与 DeepSpeed 通常是替代分片策略；TorchTitan 可内部使用 FSDP2。 |
| 08 分布式训练 | [PyTorch Lightning](../skills/pytorch-lightning/SKILL.md)<br>`pytorch-lightning` | 结构化训练循环与实验组织。负责训练循环；DeepSpeed/FSDP 为可选策略，Ray Train 可提供外层任务环境。 |
| 08 分布式训练 | [Ray Train](../skills/ray-train/SKILL.md)<br>`ray-train` | 有限集群训练任务、资源与恢复。负责集群任务；Ray Data 负责数据；内层策略可为 DDP/FSDP 等。 |
| 10 优化 | [FlashAttention](../skills/flash-attention/SKILL.md)<br>`flash-attention` | 注意力内核选择与正确性、性能检查。负责内核优化，Long Context 负责上下文扩展训练和长度泛化。 |
| 11 模型评估 | [BigCode Evaluation Harness](../skills/bigcode-evaluation-harness/SKILL.md)<br>`bigcode-evaluation-harness` | 代码生成基准与 pass@k 评测。可为 A-Evolve 提供代码生成评估，Agent 的其他能力使用相应任务评测。 |
| 13 实验管理 | [SwanLab](../skills/swanlab/SKILL.md)<br>`swanlab` | SwanLab 本地或托管实验跟踪。与 W&B 二选一或明确双写；Agent 调用链由观测工具记录。 |
| 13 实验管理 | [SWABLAB Log](../skills/swablab-log/SKILL.md)<br>`swablab-log` | 按训练 run 维护原始日志、step 指标和原生 checkpoint。SwanLab 提供硬件与环境信息；同一 run 保持同一身份，不生成实验分析、对比或科研笔记。 |
| 13 实验管理 | [Weights & Biases](../skills/weights-and-biases/SKILL.md)<br>`weights-and-biases` | W&B 实验记录、比较与产物追踪。与 SwanLab 功能替代；与 LangSmith/Phoenix 的调用链观测互补。 |
| 14 智能体 | [A-Evolve](../skills/a-evolve/SKILL.md)<br>`a-evolve` | Agent 提示、技能、工具的评估驱动改进。围绕已选 Agent 改进，沿用 LangChain、CrewAI 或 AutoGPT 等运行框架。 |
| 14 智能体 | [AutoGPT](../skills/autogpt/SKILL.md)<br>`autogpt` | AutoGPT 平台工作流与持久任务。与 CrewAI/LangChain 是主编排平台替代项，按现有项目选。 |
| 14 智能体 | [CrewAI](../skills/crewai/SKILL.md)<br>`crewai` | 角色与任务驱动的 Agent 编排。与 LangChain/AutoGPT 属于编排选择；可调用 LlamaIndex 检索组件。 |
| 14 智能体 | [LangChain](../skills/langchain/SKILL.md)<br>`langchain` | 模型、工具与状态化 Agent 工作流。负责控制流程，复用 LlamaIndex、FAISS 或 Qdrant 的检索与索引组件。 |
| 14 智能体 | [LlamaIndex](../skills/llamaindex/SKILL.md)<br>`llamaindex` | 研究资料摄取、索引与检索应用。与 LangChain 有应用层交集；可作为其数据与检索组件，底层选 FAISS/Qdrant。 |
| 15 检索增强生成 | [FAISS](../skills/faiss/SKILL.md)<br>`faiss` | 向量近邻检索与索引比较。与 Qdrant 都检索向量；FAISS 负责库级索引，Qdrant 负责服务与元数据。 |
| 15 检索增强生成 | [Qdrant](../skills/qdrant/SKILL.md)<br>`qdrant` | 向量集合、过滤、持久化与检索服务。可替代自建 FAISS 服务；与 LlamaIndex/LangChain 为上下层组合。 |
| 17 运行观测 | [LangSmith](../skills/langsmith/SKILL.md)<br>`langsmith` | Agent 调用链、数据集与在线离线评测。与 Phoenix 通常二选一；与 W&B/SwanLab 的训练指标记录互补。 |
| 17 运行观测 | [Phoenix](../skills/phoenix/SKILL.md)<br>`phoenix` | OpenTelemetry 调用链与检索评估。与 LangSmith 是观测后端替代项；可与训练日志平台组合。 |
| 18 多模态 | [BLIP-2](../skills/blip-2/SKILL.md)<br>`blip-2` | 冻结视觉编码器与语言模型的桥接。与 LLaVA 为不同 VLM 基线；与 CLIP 的表示匹配职责不同。 |
| 18 多模态 | [CLIP](../skills/clip/SKILL.md)<br>`clip` | 视觉语言编码、匹配与检索。CLIP 输出表示和匹配分数；BLIP-2/LLaVA 输出条件文本。 |
| 18 多模态 | [Cosmos-Policy](../skills/cosmos-policy/SKILL.md)<br>`cosmos-policy` | Cosmos Policy 仿真评估与故障定位。基于现有策略检查点完成仿真评估和运行排查。 |
| 18 多模态 | [LLaVA](../skills/llava/SKILL.md)<br>`llava` | 视觉指令微调与视觉问答基线。与 BLIP-2 是视觉语言模型的不同选择；动作策略由 OpenPI/OpenVLA 等流程处理。 |
| 18 多模态 | [OpenPI](../skills/openpi/SKILL.md)<br>`openpi` | OpenPI 动作策略适配、训练与服务。与 OpenVLA-OFT 是不同策略栈；Cosmos-Policy 是另一策略的评估流程。 |
| 18 多模态 | [OpenVLA-OFT](../skills/openvla-oft/SKILL.md)<br>`openvla-oft` | 连续动作头、LoRA 与机器人策略评估。与 OpenPI 为替代策略；须隔离其特定复现依赖。 |
| 19 进阶模型技术 | [Knowledge Distillation](../skills/knowledge-distillation/SKILL.md)<br>`knowledge-distillation` | 教师学生训练与能力压缩。规定蒸馏目标与对齐方式，复用既定训练后端和循环。 |
| 19 进阶模型技术 | [Long Context](../skills/long-context/SKILL.md)<br>`long-context` | 上下文扩展与长距离能力验证。与 FlashAttention 互补；RWKV 按自身架构配置状态和序列处理。 |
| 19 进阶模型技术 | [MoE Training](../skills/moe-training/SKILL.md)<br>`moe-training` | 专家路由、负载均衡与并行扩展实验。负责模型机制，由 DeepSpeed 等支持该机制的既定后端执行训练。 |
| 20 论文写作与学术表达 | [Academic Plotting](../skills/academic-plotting/SKILL.md)<br>`academic-plotting` | 可复现科研数据图与编辑源文件。与现有科学绘图技能重叠时沿用既定主绘图流程；本包不含图像生成。 |
| 20 论文写作与学术表达 | [CCF Conference Colors](../skills/ccf-conference-colors/SKILL.md)<br>`ccf-conference-colors` | 会议论文配色、跨图颜色一致性与对比度/灰度诊断。负责颜色规范；Academic Plotting 或既有绘图流程仍负责图形构建。205 套精选色板，可独立使用。 |
| 20 论文写作与学术表达 | [ML Paper Writing](../skills/ml-paper-writing/SKILL.md)<br>`ml-paper-writing` | 由研究证据组织机器学习论文。按主要贡献选择本技能或 Systems Paper Writing；已有 ccf-paper-writer 流程时沿用主稿与写作分工。 |
| 20 论文写作与学术表达 | [Systems Paper Writing](../skills/systems-paper-writing/SKILL.md)<br>`systems-paper-writing` | 系统设计、实现与性能论证。与 ML Paper Writing 按系统贡献或算法贡献选一个主流程，可借用对方局部建议。 |
| 21 研究构思 | [Brainstorming Research Ideas](../skills/brainstorming-research-ideas/SKILL.md)<br>`brainstorming-research-ideas` | 生成、比较和收敛研究方向。独立完成候选方向的展开、比较与收敛，交付研究方向和下一步调查计划。 |
| 21 研究构思 | [Creative Thinking for Research](../skills/creative-thinking-for-research/SKILL.md)<br>`creative-thinking-for-research` | 通过类比、重构与假设变化提出新机制。独立运用类比、问题重构和假设变化，交付可检验的机制假设。 |

各技能可独立使用，也可按任务组合互补能力。根据请求和既有项目选择适用流程；影响结果的关键选择无法推断时，再向用户澄清。

每个文件夹包含独立入口、引用、许可和来源。实际训练依赖属于具体项目环境；色板技能另外包含配色数据、逐来源许可、离线预览和小型工具。技能的组合方式见下文，来源与版本见[sources.json](sources.json)。

## 按单个、类别或全部选择

类别编号沿用原目录，下表列出本版本包含的16个类别，供查找和批量选择。

| 类别编号 | 名称 | 技能数 |
|---|---|---:|
| `01` | 模型架构 | 3 |
| `02` | 分词与序列表示 | 1 |
| `04` | 机制可解释性 | 2 |
| `05` | 数据处理 | 2 |
| `06` | 后训练 | 5 |
| `08` | 分布式训练 | 5 |
| `10` | 优化 | 1 |
| `11` | 模型评估 | 1 |
| `13` | 实验管理 | 3 |
| `14` | 智能体 | 5 |
| `15` | 检索增强生成 | 2 |
| `17` | 运行观测 | 2 |
| `18` | 多模态 | 6 |
| `19` | 进阶模型技术 | 3 |
| `20` | 论文写作与学术表达 | 4 |
| `21` | 研究构思 | 2 |

`python3 scripts/install.py --category 08 --list` 只列出该类别；`--category 08 --dest ./chosen-skills` 复制该类完整技能文件夹。用 `--skill <name>` 选择单项，用 `--all` 明确选择全部；可组合多个 `--skill` 与 `--category`，重叠项自动去重。

## 组合与分工

沿用用户明确选择和现有项目的框架与产物。任务需要互补能力时按职责组合；关键选择无法推断且会影响方法、成本或结果时，再向用户澄清。

| 组合 | 重叠或冲突 | 本版分工 |
|---|---|---|
| nanoGPT / RWKV / TorchTitan | 不同模型实现和训练入口 | 依据选定架构和项目选择主入口，使用匹配的状态、tokenizer和检查点 |
| TRL / OpenRLHF / verl | 同为后训练主框架 | 单次训练选一个主后端；保留现有选择 |
| GRPO / TRL、OpenRLHF、verl | 方法与实现有交集 | GRPO 管奖励、采样与学习诊断；后端管实际 Trainer |
| SimPO / GRPO / DPO | 不同优化目标 | 按研究目标选择损失函数；SimPO 需核对实际实现与归一化 |
| Accelerate / Lightning | 都能管理训练生命周期 | 由其中一个管理同一模型和训练循环 |
| DeepSpeed / 原生 FSDP2 | 通常是替代分片/状态管理策略 | 一个模型由一个选定策略管理；可通过受支持的 Accelerate/Lightning 插件集成 |
| Ray Train / Ray Data | 同一生态、不同层次 | Train 管 worker/资源/恢复，Data 管预处理和数据流；防止重复分片 |
| NeMo Curator / Ray Data | 都能处理数据 | Curator 管清洗规则和数据审计，Data 可执行这套规则 |
| TransformerLens / pyvene | 都能做激活干预 | 按实际模型和干预方式选择一个钩子实现，保留对照和对齐验证 |
| FlashAttention / Long Context | 都影响长序列效率 | 前者管注意力实现与数值等价，后者管位置机制、训练和长度泛化 |
| W&B / SwanLab | 实验记录功能替代 | 默认一个主记录源，确需双写时显式设计 run ID 与指标映射 |
| SWABLAB Log / SwanLab | 训练记录约定与 tracker 后端 | SWABLAB Log 管 run 身份、本地原始日志、CSV 与原生 checkpoint；SwanLab 管指标追踪和设备环境采集，不另建重复 tracker |
| LangSmith / Phoenix | 调用链与应用评测功能替代 | 默认一个观测后端，防止双重自动 instrumentation |
| 训练记录 / 调用链观测 | 分别记录训练实验与应用调用 | W&B/SwanLab 与 LangSmith/Phoenix 可组合，通过 run ID 关联 |
| AutoGPT / CrewAI / LangChain | Agent 主编排能力交叉 | 沿用指定或现有项目的主框架 |
| LlamaIndex / LangChain | RAG 和工具应用有交集 | 可让 LlamaIndex 管摄取/检索，LangChain 管控制流程；接口明确 |
| A-Evolve / Agent 框架 | 改进循环与运行框架不同 | A-Evolve 围绕既有 Agent 做有预算、带保留集的评估和更新 |
| FAISS / Qdrant | 向量检索能力交叉 | FAISS 是索引库，Qdrant 提供集合、过滤和持久化服务；每个索引由一个组件负责写入 |
| CLIP / BLIP-2 / LLaVA | 都使用视觉语言信息 | CLIP 管表示/匹配；BLIP-2 和 LLaVA 是不同条件文本模型基线 |
| OpenPI / OpenVLA-OFT / Cosmos-Policy | 都涉及机器人策略 | 前两者各管自己的适配/训练栈，后者专注现有策略评估 |
| Knowledge Distillation / 后训练框架 | 目标与实现分层 | 蒸馏规定教师输出、对齐和损失；复用既定训练后端 |
| MoE Training / 分布式技能 | 模型机制与执行策略分层 | MoE 管专家路由/容量/负载，选定后端管执行和检查点 |
| ML Paper Writing / Systems Paper Writing | 共用写作基础原则 | 按算法、模型或系统贡献选定主写作流程，并参考另一技能的局部建议 |
| Brainstorming Research Ideas / Creative Thinking for Research | 都能生成研究想法 | 前者侧重候选方向的展开、比较与收敛，后者侧重类比、重构和假设变化；均可独立完成，按用户意图选择 |
| 新写作/绘图技能 / 已有 CCFA 和科学视觉技能 | 自动触发与产物职责会重叠 | 已有稿件和图形沿用现行写作或绘图流程，用户指定新技能时切换 |

配色技能负责色板、固定系列映射、颜色语义与对比度/灰度诊断；选定绘图流程负责图形源码和导出。单独的配色请求由配色技能完成，图宽与最终检查按具体会议模板确定。包内Python工具使用标准库，可选Matplotlib接口复用项目环境。

## 环境与资源

各研究项目分别管理Python、CUDA和JAX依赖。OpenVLA-OFT的复现材料使用特定旧版本；TorchTitan/FSDP2的支持范围跟随选定的PyTorch版本；OpenPI的JAX/PyTorch路径和模型补丁也有各自要求。根据选定commit、官方环境与现有锁定文件配置项目，更新辅助模型时保留科学实验所用的软件版本。

计算规模按项目硬件与预算配置。资源核算覆盖同时运行的训练、rollout、参考/奖励模型、教师推理、评估、数据处理和多试验；共享GPU时检查显存占用与调度。可支持的规模由具体实现、节点互联和实测结果确定。

技能格式、独立分发和维护检查见[贡献指南](../CONTRIBUTING.md)。[行为评估材料](../evals/README.md)提供可选任务，用于检查技能选择与实际输出。
