# DevOps Engineer Interview Agent（运维工程师面试智能体）

> 一份**标准化、可开源、跨工具通用**的运维 / SRE / DevOps 面试题库 + 面试智能体。  
> 既是一套「讲透概念」的备考知识库，也是一个能当真实面试官、逐题打分、出记分卡的 AI Agent。  
> 覆盖：Linux · 网络 · 容器/K8s · CI/CD/IaC · 监控可观测 · 故障/SRE · 中间件 · GPU/AI 运维 · 云/安全 · 服务网格/网关 · 系统设计 · 前沿部署工程师（FDE）· AI 工程 / Agentic 工具链 · 行为与架构。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Questions](https://img.shields.io/badge/questions-2000%2B-blue.svg)](#目录) [![Chinese](https://img.shields.io/badge/lang-中文-red.svg)](#) [![Tools](https://img.shields.io/badge/works%20on-Claude%20%7C%20Codex%20%7C%20WorkBuddy%20%7C%20any%20LLM-green.svg)](#如何导入与使用) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 这是什么

本项目由两部分组成，且**不绑定任何单一工具**：

1. **知识库（basics/ + modules/ + collections/ + system-design/）**：374 道自研标准化面试题 + 6 篇基础概念深度篇 + 2200+ 道社区真实真题（22 专题 1502 题 + 崔亮高级 231 题 + 中级 89 题 + MongoDB Zero-to-Hero 68 题 + K8s 本地资料库 159 题 + 经典论文 111 题 + K8s 网页存档与本地仓库 697 题 + Veeramalla 公司真题 3024 题 + Agentic 工具链生态 392 题 + AWS 托管服务改造 195 题 + 系统设计练习与笔记 63 题 + 系统设计题库 458 题，标注来源，☆ 为高频题）+ **630 个系统设计主题语料**（`system-design/` 子模块，每个主题含需求 / 架构 / 权衡 / 面试问答 / 速答表）。
2. **面试智能体（agent/ + CLAUDE.md + AGENTS.md + workbuddy/）**：把上面的知识库变成一个「运维面试教练」Agent，  
   可在 **Claude Code、Codex、WorkBuddy、ChatGPT 等任意支持系统提示词的 LLM 工具**里运行。

智能体的能力：

- **逐题模拟面试**：一次一题，按模块/难度/级别出题；答后给 ✅做对 ⚠️待改进 💡理想答案 📊1–10 分。
- **概念深度讲解**：用「速记 + 原理 + 对比表 + 误区」讲透 OSI、CRI/CNI/CSI、Dockerfile、Ansible、GPU 等。
- **完整记分卡**：结束输出各模块得分、总分、录用裁决、关键优势、待改进项、推荐学习主题。
- **简历驱动定制**：分析简历后针对性出题、动态调难度。
- **AI 面试**：`switch ai-engineering`，考 agentic 编码 / 运维工具的正确用法（记忆文件、上下文、权限、钩子、MCP、子代理、技能、无头 CI）、给 Agent 进生产的护栏设计、注入防护与评测体系。
- **FDE 案例面试**：`switch fde`，给客户场景，按 C.A.S.E.（澄清 → 架构 → 补 Delta → 评测）推进，考数据工程 / 云着陆区 / 应用 AI 与评测 / 隔离网络部署 / 干系人管理，五维评分。
- **系统设计面试**：`switch system-design [主题]`，按「需求澄清 → 估算 → 高层设计 → 深入 → 权衡与可运维性」五段推进，用五维评分表打分；主题从 630 个语料目录中选（限流器 / KV / 信息流 / IM / 监控 / 调度器 / RAG / LLM 推理……）。

---

## 目录结构

```text
DevOps-Engineer-Interview-Agent/
├── README.md                 # 本文件（含各工具导入说明）
├── CLAUDE.md                 # Claude Code 自动加载的系统提示词
├── AGENTS.md                 # Codex / OpenAI 自动加载的 Agent 指令
├── CONTRIBUTING.md           # 贡献指南
├── LICENSE                   # MIT
├── CODE_OF_CONDUCT.md
├── .github/                  # PR / Issue 模板
├── agent/
│   ├── UNIVERSAL.md          # 工具无关的系统提示词（可粘贴到任意 LLM）
│   └── README.md             # 智能体说明
├── docs/
│   ├── STANDARD.md           # 题目标准化规范（必读）
│   ├── LEVELS.md             # 难度分级定义
│   └── ROADMAP.md            # 学习路线
├── basics/                   # 基础概念深度篇（面试地基）
│   ├── 01-linux-basics.md
│   ├── 02-network-osi.md
│   ├── 03-docker-basics.md
│   ├── 04-kubernetes-concepts.md   # CRI / CNI / CSI
│   ├── 05-ansible-basics.md
│   └── 06-ai-gpu-basics.md
├── modules/                  # 标准化面试题（按主题，374 题）
│   ├── linux / network / kubernetes / cicd-iac
│   ├── observability / sre-reliability / middleware
│   ├── gpu-ai / cloud-security / service-mesh / behavior
│   ├── system-design/        # 35 题 + system-design-catalog.md（630 主题自动目录）+ system-design-resolver.md（181 条别名含 78 条中文 / 82 组重复主题折叠 / 薄主题与非标准编号主题分流）
│   ├── fde/                  # 30 题：前沿部署工程师（案例面试 + C.A.S.E. + 隔离网络部署）
│   └── ai-engineering/       # 27 题：AI 面试（Claude Code 等 agentic 工具、护栏、MCP、评测、注入）
├── system-design/            # git 子模块：github.com/ljluestc/system-design（630 个系统设计主题）
├── scripts/                  # build_system_design_catalog.py（生成目录 + 解析器；`--resolve "设计一个秒杀系统"` 可直接查主题）/ verify_system_design.py（12 项校验）
├── .mcp.json                 # 7 个 MCP 服务器（arXiv / 网页搜索 / 抓取 / K8s 只读 / Docker / Terraform / Context7），Claude Code 自动加载
├── collections/              # 收录的社区真实真题（来源标注见 README）
│   ├── README.md             # 收录清单 / 版权口径 / 模块映射
│   ├── ops-question-bank-1502.md       # 22 专题 1502 题大合集
│   ├── cuiliang-ops-interview-2024.md   # 崔亮 231 题高级（☆ 高频标记）
│   ├── cuiliang-mid-ops-interview-2020.md  # 崔亮 89 题中级
│   ├── mongodb-zero-to-hero.md          # MongoDB 68 题（教程提炼，附要点）
│   ├── k8s-local-library.md             # K8s 本地资料库 159 题（CKS / 官方安全审计 / 大厂实践 / 存储 / 排障，附要点）
│   ├── classic-papers.md                # 经典论文 111 题（Paxos / Raft / GFS / MapReduce / Lamport / HTTP/2 / REST / JVM GC，附要点 + 书架索引）
│   ├── k8s-web-archive.md               # K8s/云原生网页存档与仓库文档 697 题（手册全章 / Gateway API / 推理网关 / Istio API / 攻防 / AI Infra / RAG / 实验集群运维，附要点）
│   ├── veeramalla-devops-interview-guide.md  # Veeramalla DevOps/SRE 公司真题 3024 题（86 家公司 151 份写实：Amazon / JPMorgan / IBM / Infosys / TCS …，纯题目）
│   ├── awesome-claude-code.md           # Agentic 工具链生态 392 题（扩展点选型 / 命令 / 钩子 / 技能 / 编排 / 可观测 / 成本 / 沙箱与注入防护，附要点）
│   ├── aws-managed-services-only.md     # 「只用 AWS 托管服务」改造 195 题（选型表 / IRSA 与 Secrets Manager / CloudWatch vs AMP / AWS Backup 与 K8s 对象缺口 / GPU on EKS 托管边界 / VPC Lattice / CodePipeline / 未验证设计的写法 / 11 个经典系统设计题的 AWS-only 渲染，附要点）
│   ├── system-design-exercises-and-notes.md  # 系统设计练习与笔记 63 题（devops-exercises 系统设计主题原创题 / 推荐·搜索·对话·RAG 系统设计 / Meta PE 监控系统设计，附要点）
│   └── system-design-quiz-bank.md  # 系统设计题库 458 题（子模块 70 个主题的专属 quiz / drill / 速答，脚本生成，剔除模板题）
└── workbuddy/                # WorkBuddy 专家插件（可选，原生体验）
    └── ops-interview-coach/  # agent 型专家，含内置浓缩题库 + 头像
```

> 知识库是单一事实来源：`agent/UNIVERSAL.md`、`CLAUDE.md`、`AGENTS.md` 都让 Agent 直接读取  
> `basics/`、`modules/` 与 `collections/`，避免重复维护。`workbuddy/` 下的插件自带一份浓缩版，便于离线使用。

---

## 如何导入与使用

### 方式一：Claude Code（推荐，零配置）

克隆本仓库后，在仓库目录下启动 Claude Code 即可——`CLAUDE.md` 会被**自动加载**：

```bash
git clone --recurse-submodules https://github.com/dongdonglog/DevOps-Engineer-Interview-Agent.git
cd DevOps-Engineer-Interview-Agent
claude          # 启动 Claude Code，它自动读取 CLAUDE.md 成为「运维面试教练」
```

然后直接对话，例如：

> 模拟一场高级运维工程师面试，从 Linux 与系统内核开始

> 讲透 OSI 七层模型以及它和真实排障的对应关系

> switch system-design rate-limiter —— 来一场分布式限流器的系统设计面试

---

### 方式二：Codex / OpenAI 系工具

本仓库根目录的 `AGENTS.md` 会被 Codex 等工具**自动加载**：

```bash
git clone --recurse-submodules https://github.com/dongdonglog/DevOps-Engineer-Interview-Agent.git
cd DevOps-Engineer-Interview-Agent
codex           # 或任意读取 AGENTS.md 的 OpenAI 系 Agent
```



---

### 方式三：任意 LLM（ChatGPT 网页版 / API / 其他客户端）

把 `agent/UNIVERSAL.md` 的内容**粘贴到系统提示词（System Prompt）** 即可。  
若需要完整知识，可同时把 `basics/` 与 `modules/` 作为上下文附上（或告知模型读取这些文件）。

- 文件版：`cat agent/UNIVERSAL.md` 复制粘贴。
- API 版：将 `UNIVERSAL.md` 作为 `system` 消息；如遇概念/出题，让模型读取 `basics/`、`modules/`。

---

### 方式四：WorkBuddy（原生专家体验，含头像/记分卡 UI）

仓库已附带打包好的 WorkBuddy 专家插件 `workbuddy/ops-interview-coach`：

```bash
# 复制到你的 WorkBuddy 专家目录
cp -r workbuddy/ops-interview-coach \
  ~/.workbuddy/plugins/marketplaces/my-experts/plugins/

# 注册使其可见（脚本路径以你本地 WorkBuddy 为准）
python3 <workbuddy-expert-manager>/scripts/register_expert.py \
  ~/.workbuddy/plugins/marketplaces/my-experts/plugins/ops-interview-coach
```

注册后，在 WorkBuddy 专家中心即可直接使用「运维面试教练」，支持内置记分卡与头像。

> 注：方式一~三使用的是本仓库 `basics/` + `modules/` + `collections/` 的 **7400+ 题完整版**；  
> `workbuddy/` 插件内置的是 **80 题浓缩版**，便于插件离线自包含。两者口径一致。

---

## 难度分级

| 标记 | 级别 | 说明              |
| -- | -- | --------------- |
| 🟢 | 初级 | 概念认知、基础命令、常见现象  |
| 🟡 | 中级 | 原理理解、排障思路、配置实践  |
| 🔴 | 高级 | 架构权衡、复杂排障、性能优化与体系设计  |

详见 [docs/LEVELS.md](docs/LEVELS.md)。

---

## 题目标准化格式

每道题统一如下结构（具体字段含义见 [docs/STANDARD.md](docs/STANDARD.md)）：

```markdown
### Qxx. 题目
- **难度**：🔴 高级
- **关键词**：kubernetes, CRI, 容器运行时
- **概念速记**：CRI 是 kubelet 与容器运行时之间的 gRPC 接口……
- **问题**：kubelet 如何通过 CRI 管理容器？为什么需要这一层抽象？
- **参考答案**：要点 1（含 trade-off / 实战）……
- **易错点 / 面试官关注**：……
- **延伸**：Q48、[basics/04-kubernetes-concepts.md](basics/04-kubernetes-concepts.md)
```

---

## 智能体会话指令

面试过程中可使用这些指令控制流程：

| 指令                  | 作用                                                                                                                                 |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `skip`              | 跳过当前题                                                                                                                              |
| `hint`              | 给提示（不直接给答案）                                                                                                                        |
| `explain`           | 展开详解当前概念                                                                                                                           |
| `score`             | 查看当前累计记分卡                                                                                                                          |
| `harder` / `easier` | 升高 / 降低难度                                                                                                                          |
| `switch [模块]`       | 切换模块：`linux` `network` `kubernetes` `cicd-iac` `observability` `sre-reliability` `middleware` `gpu-ai` `cloud-security` `service-mesh` `system-design` `fde` `ai-engineering` `behavior`；`switch system-design <主题>` 直接指定语料主题（如 `rate-limiter`、`monitoring-system`、`rag-system`）|
| `quiz [主题]`         | 速答轮：从主题的 `06-quiz.md` / `20-interview-drills.md` 或模块速答表抽 10–15 道选择 / 一句话题，逐题作答后给 N/15 得分与逐题一句话解析（如 `quiz dropbox`、`quiz rate-limiter`）|
| `end`               | 结束并输出最终记分卡                                                                                                                         |
| `restart`           | 重新开始                                                                                                                               |

---

## MCP 工具服务器（论文 / 搜索 / 抓取 / K8s / Docker / Terraform / 文档）

仓库自带 [`.mcp.json`](.mcp.json)，注册了 7 个**本地运行、无需 API Key** 的 MCP 服务器（选自 [awesome-mcp-servers](https://github.com/blazickjp/awesome-mcp-servers)），
Claude Code 打开本仓库即自动加载并已在 `.claude/settings.json` 预批准。智能体在题库覆盖不到、需要实时或外部数据时才调用：

| 服务器 | 来源 | 用途 | 依赖 |
|---|---|---|---|
| `arxiv` | [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | 论文检索 / 下载 / 分节阅读 / 引用图 / BibTeX（「Raft 论文怎么描述 leader 选举」） | `uv` |
| `duckduckgo` | [nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server) | 免 Key 网页搜索（「K8s 1.3x 改了什么」「某 CVE 影响」） | `uv` |
| `fetch` | [modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/fetch) | 抓取任意 URL 转 Markdown（读官方文档 / 博客） | `uv` |
| `kubernetes` | [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) | 对当前 kubeconfig 上下文做 **只读** 排障（list / describe / logs / events），用于「找出这个集群哪里坏了」类实操题 | `node`、kubeconfig |
| `docker` | [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) | 本地容器列表 / 日志，容器排障题 | `uv`（Python 3.12）、Docker |
| `terraform` | [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) | Provider / Module 注册表与资源文档查询 | Docker |
| `context7` | [upstash/context7](https://github.com/upstash/context7) | 最新库 / 工具文档（Helm、Terraform Provider、client-go、Ansible 模块） | `node` |

```bash
claude mcp list                                   # 健康检查（7 个应为 Connected）
codex mcp add arxiv -- uvx arxiv-mcp-server       # Codex 用户按 .mcp.json 逐个手动注册
```

> `kubernetes` 服务器以 `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS=true` 启动，智能体不会对集群做写操作；需要 API Key 的服务器（GitHub / Grafana / Prometheus / Brave 等）未收录，按需自行 `claude mcp add`。

---

## 系统设计面试（system-design）

`modules/system-design/` 提供 **35 道标准化系统设计题**（方法论 / 基础构件 / 经典产品 / 运维与基础设施系统 / AI 系统）与
**面试官执行手册 + 五维评分表**；深度素材来自 `system-design/` 子模块（[ljluestc/system-design](https://github.com/ljluestc/system-design)，
630 个主题目录，每个目录按 `00-index` → `01-requirements` → `02-architecture` → `05-trade-offs` → `06-quiz` → `20-interview-drills` 编号组织）。

- 全量主题目录：[modules/system-design/system-design-catalog.md](modules/system-design/system-design-catalog.md)（自动生成，按类别分组，标注每个主题有哪些文档）。
- 智能体出题前会读主题的 `00-index / 01-requirements / 05-trade-offs`，追问取自 `06-quiz` 与 `20-interview-drills`。
- 若克隆时未带子模块：`git submodule update --init`（约 1.6 GB）。
- 维护：`python3 scripts/build_system_design_catalog.py` 重新生成目录；`python3 scripts/verify_system_design.py` 校验目录覆盖率、题目格式、链接与提示词接线。
- 全模块一致性：`python3 scripts/verify_modules.py`（题号 / 模板字段 / 链接 / 题量 / 各模块是否接入 switch 列表）。
- 端到端测试：`scripts/e2e/run_matrix.sh` 用 `claude -p` 对 25 个主题（各类别 + 中文点名 + 不存在的主题）跑无头面试并自动评分（是否读取语料、是否只问一题、语言是否匹配）。

---

## 如何贡献

欢迎 PR！新增题目请严格遵循 [docs/STANDARD.md](docs/STANDARD.md) 的格式，并在对应主题的 `modules/` 目录下提交；  
改进智能体提示词请同步更新 `agent/UNIVERSAL.md`、`CLAUDE.md`、`AGENTS.md` 三处；改动系统设计模块后运行 `python3 scripts/verify_system_design.py`。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## Roadmap

- [x] 仓库骨架与标准化规范
- [x] 基础概念深度篇（6 篇）
- [x] 十二大主题面试题（2100+ 题）
- [x] 系统设计模块（35 题 + 630 主题语料子模块 + 自动目录与校验脚本）
- [x] FDE 前沿部署工程师模块（30 题，案例面试，提炼自 Awesome-FDE-Roadmap）
- [x] AI 工程 / Agentic 工具链模块（26 题，提炼自 claude-code-crash-course + VIBE-CODING 真题）
- [x] 跨工具智能体（CLAUDE.md / AGENTS.md / UNIVERSAL.md / WorkBuddy 插件）
- [ ] 配套速查表（cheat-sheets/）
- [ ] 模拟面试脚本（mock-interviews/）
- [ ] 英文版（i18n/）
- [ ] 图表化（assets/ 架构图、流程图）

---

## License

[MIT](LICENSE) © DevOps-Engineer-Interview-Agent contributors
