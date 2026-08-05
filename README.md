# DevOps Engineer Interview Agent（运维工程师面试智能体）

> 一份**标准化、可开源、跨工具通用**的运维 / SRE / DevOps 面试题库 + 面试智能体。  
> 既是一套「讲透概念」的备考知识库，也是一个能当真实面试官、逐题打分、出记分卡的 AI Agent。  
> 覆盖：Linux · 网络 · 容器/K8s · CI/CD/IaC · 监控可观测 · 故障/SRE · 中间件 · GPU/AI 运维 · 云/安全 · 行为与架构。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Questions](https://img.shields.io/badge/questions-520%2B-blue.svg)](#目录) [![Chinese](https://img.shields.io/badge/lang-中文-red.svg)](#) [![Tools](https://img.shields.io/badge/works%20on-Claude%20%7C%20Codex%20%7C%20WorkBuddy%20%7C%20any%20LLM-green.svg)](#如何导入与使用) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 这是什么

本项目由两部分组成，且**不绑定任何单一工具**：

1. **知识库（basics/ + modules/ + collections/）**：200+ 道自研标准化面试题 + 6 篇基础概念深度篇 + 320 道社区真实真题（崔亮高级 231 题 + 中级 89 题，标注来源，☆ 为高频题）。
2. **面试智能体（agent/ + CLAUDE.md + AGENTS.md + workbuddy/）**：把上面的知识库变成一个「运维面试教练」Agent，  
   可在 **Claude Code、Codex、WorkBuddy、ChatGPT 等任意支持系统提示词的 LLM 工具**里运行。

智能体的能力：

- **逐题模拟面试**：一次一题，按模块/难度/级别出题；答后给 ✅做对 ⚠️待改进 💡理想答案 📊1–10 分。
- **概念深度讲解**：用「速记 + 原理 + 对比表 + 误区」讲透 OSI、CRI/CNI/CSI、Dockerfile、Ansible、GPU 等。
- **完整记分卡**：结束输出各模块得分、总分、录用裁决、关键优势、待改进项、推荐学习主题。
- **简历驱动定制**：分析简历后针对性出题、动态调难度。

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
├── modules/                  # 标准化面试题（按主题，200+ 题）
│   ├── linux / network / kubernetes / cicd-iac
│   ├── observability / sre-reliability / middleware
│   └── gpu-ai / cloud-security / behavior
├── collections/              # 收录的社区真实真题（来源标注见 README）
│   ├── README.md             # 收录清单 / 版权口径 / 模块映射
│   ├── cuiliang-ops-interview-2024.md   # 崔亮 231 题高级（☆ 高频标记）
│   └── cuiliang-mid-ops-interview-2020.md  # 崔亮 89 题中级
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
git clone https://github.com/dongdonglog/DevOps-Engineer-Interview-Agent.git
cd DevOps-Engineer-Interview-Agent
claude          # 启动 Claude Code，它自动读取 CLAUDE.md 成为「运维面试教练」
```

然后直接对话，例如：

> 模拟一场高级运维工程师面试，从 Linux 与系统内核开始

> 讲透 OSI 七层模型以及它和真实排障的对应关系

---

### 方式二：Codex / OpenAI 系工具

本仓库根目录的 `AGENTS.md` 会被 Codex 等工具**自动加载**：

```bash
git clone https://github.com/dongdonglog/DevOps-Engineer-Interview-Agent.git
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

> 注：方式一~三使用的是本仓库 `basics/` + `modules/` + `collections/` 的 **520+ 题完整版**；  
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
| `switch [模块]`       | 切换模块：`linux` `network` `kubernetes` `cicd-iac` `observability` `sre-reliability` `middleware` `gpu-ai` `cloud-security` `behavior` |
| `end`               | 结束并输出最终记分卡                                                                                                                         |
| `restart`           | 重新开始                                                                                                                               |

---

## 如何贡献

欢迎 PR！新增题目请严格遵循 [docs/STANDARD.md](docs/STANDARD.md) 的格式，并在对应主题的 `modules/` 目录下提交；  
改进智能体提示词请同步更新 `agent/UNIVERSAL.md`、`CLAUDE.md`、`AGENTS.md` 三处。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## Roadmap

- [x] 仓库骨架与标准化规范
- [x] 基础概念深度篇（6 篇）
- [x] 十大主题面试题（520+）
- [x] 跨工具智能体（CLAUDE.md / AGENTS.md / UNIVERSAL.md / WorkBuddy 插件）
- [ ] 配套速查表（cheat-sheets/）
- [ ] 模拟面试脚本（mock-interviews/）
- [ ] 英文版（i18n/）
- [ ] 图表化（assets/ 架构图、流程图）

---

## License

[MIT](LICENSE) © DevOps-Engineer-Interview-Agent contributors
