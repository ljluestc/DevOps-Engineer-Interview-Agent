# 运维工程师面试题库（Ops Interview）

> 一份**标准化、可开源、持续共建**的运维 / SRE / DevOps 工程师面试题库。
> 覆盖：Linux · 网络 · 容器/K8s · CI/CD/IaC · 监控可观测 · 故障/SRE · 中间件 · GPU/AI 运维 · 云/安全 · 行为与架构。
> 目标：从「背答案」升级到「讲清楚概念 + 排障思路 + 权衡判断 + 落地经验」。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Questions](https://img.shields.io/badge/questions-200%2B-blue.svg)](#目录)
[![Chinese](https://img.shields.io/badge/lang-中文-red.svg)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 为什么做这个项目

市面上的运维面试题大多「问题 + 一句答案」，存在三个问题：

1. **太表面**：只给结论，不讲概念边界（比如只问「K8s 网络怎么实现」，却不解释 CRI / CNI / CSI 到底是什么）。
2. **不成体系**：200 个问题堆在一个文件里，难以维护、检索、共建。
3. **不标准化**：每题写法各异，质量参差。

本项目借鉴了社区优秀开源项目的结构：

- [bregman-arie/devops-exercises](https://github.com/bregman-arie/devops-exercises)（按主题分目录的 Q&A 题库）
- [trimstray/test-your-sysadmin-skills](https://github.com/trimstray/test-your-sysadmin-skills)（Sysadmin Q/A）
- [NotHarshhaa/DevOps-Interview-Questions](https://github.com/NotHarshhaa/DevOps-Interview-Questions)（按难度分级 + 主题文件夹）
- [CS-Notes](https://github.com/CyC2018/CS-Notes)（中文、目录清晰、排版规范）

并做了两点增强：

- **基础概念深度篇（basics/）**：把 OSI、CRI/CNI/CSI、Dockerfile、Ansible、AI/GPU 等关键词讲透，作为面试前的「地基」。
- **题目标准化模板（docs/STANDARD.md）**：每题统一包含 `难度 / 关键词 / 概念速记 / 问题 / 参考答案 / 易错点 / 延伸`，方便社区共建与质量对齐。

---

## 目录结构

```text
ops-interview/
├── README.md                 # 本文件
├── CONTRIBUTING.md           # 贡献指南（如何新增/修改题目）
├── LICENSE                   # MIT
├── CODE_OF_CONDUCT.md        # 行为准则
├── .github/                  # PR / Issue 模板
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
└── modules/                  # 标准化面试题（按主题）
    ├── linux/
    ├── network/
    ├── kubernetes/
    ├── cicd-iac/
    ├── observability/
    ├── sre-reliability/
    ├── middleware/
    ├── gpu-ai/
    ├── cloud-security/
    └── behavior/
```

---

## 难度分级

| 标记 | 级别 | 说明 |
|---|---|---|
| 🟢 | 初级 | 概念认知、基础命令、常见现象 |
| 🟡 | 中级 | 原理理解、排障思路、配置实践 |
| 🔴 | 高级 | 架构权衡、复杂排障、性能优化 |
| ⚫ | 资深 | 体系设计、跨团队推动、技术决策 |

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
- **参考答案**：
  - 要点 1（含 trade-off / 实战）
  - 要点 2
- **易错点 / 面试官关注**：……
- **延伸**：Q48、[basics/04-kubernetes-concepts.md](basics/04-kubernetes-concepts.md)
```

---

## 快速开始

```bash
# 克隆（假设已发布到 GitHub）
git clone https://github.com/<your-org>/ops-interview.git
cd ops-interview

# 阅读顺序建议
# 1) 先看 docs/STANDARD.md 了解题目规范
# 2) 按 docs/ROADMAP.md 的路线补基础（basics/）
# 3) 按目标岗位刷 modules/ 对应主题
```

---

## 如何贡献

欢迎 PR！新增题目请严格遵循 [docs/STANDARD.md](docs/STANDARD.md) 的格式，并在对应主题的 `modules/` 目录下提交。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## Roadmap

- [x] 仓库骨架与标准化规范
- [x] 基础概念深度篇（6 篇）
- [x] 十大主题面试题（200+）
- [ ] 配套速查表（cheat-sheets/）
- [ ] 模拟面试脚本（mock-interviews/）
- [ ] 英文版（i18n/）
- [ ] 图表化（assets/ 架构图、流程图）

---

## License

[MIT](LICENSE) © ops-interview contributors
