# 学习路线（ROADMAP）

> 按「地基 → 专题 → 冲刺」三阶段准备。每个阶段给出必读文件与建议时长。

---

## 阶段一：地基（1–2 周）

先把概念讲清楚，再刷题。否则题目答了也不透。

| 主题 | 必读 | 重点 |
|---|---|---|
| Linux 基础 | [basics/01-linux-basics.md](basics/01-linux-basics.md) | 进程/内存/IO/内核参数/Shell |
| 网络与 OSI | [basics/02-network-osi.md](basics/02-network-osi.md) | OSI 七层、TCP、DNS、HTTP |
| Docker | [basics/03-docker-basics.md](basics/03-docker-basics.md) | 镜像分层、Dockerfile、存储驱动 |
| K8s 概念 | [basics/04-kubernetes-concepts.md](basics/04-kubernetes-concepts.md) | CRI/CNI/CSI、对象模型 |
| Ansible | [basics/05-ansible-basics.md](basics/05-ansible-basics.md) | 幂等、Playbook、Inventory |
| AI/GPU | [basics/06-ai-gpu-basics.md](basics/06-ai-gpu-basics.md) | CUDA/显存/调度/推理 |

> 目标：能不看资料，用一句话讲清 README 里每个关键词。

---

## 阶段二：专题突破（2–4 周）

按目标岗位选主题刷 `modules/`，每题先口述再对照参考答案。

| 方向 | 模块路径 | 优先级 |
|---|---|---|
| 通用运维/SRE | `modules/linux` `modules/network` `modules/sre-reliability` | ★★★★★ |
| 云原生 | `modules/kubernetes` `modules/cicd-iac` `modules/observability` | ★★★★★ |
| 中间件 | `modules/middleware` | ★★★★ |
| AI 基础设施 | `modules/gpu-ai` | ★★★（目标公司做模型/推理平台时拉满） |
| 云/安全 | `modules/cloud-security` | ★★★（金融/合规加码） |
| 管理与架构 | `modules/behavior` | ★★★★（高级以上必考） |

---

## 阶段三：冲刺（1–2 周）

1. **项目复盘**：准备 2–3 个体现「高级」深度的项目故事（STAR + 量化结果 + 技术决策 + 踩坑）。
2. **排障清单**：把 modules/sre-reliability 的排障题整理成自己的 checklist（止血 → 定位 → 根治）。
3. **模拟面试**：找同伴或用 mock-interviews/（待建）互考，重点练「边想边说」。
4. **查漏**：用 `modules/behavior` 打磨软技能与架构表达。

---

## 按目标公司裁剪

- **大模型 / 推理平台**：GPU/AI（modules/gpu-ai + basics/06）拉满，K8s 重点看调度与 Device Plugin。
- **传统互联网**：Linux/网络/SRE/中间件为主，GPU 了解即可。
- **金融 / 政企**：云安全（modules/cloud-security）与合规加码，等保/审计相关题重点准备。
- **云厂商 / 基建团队**：K8s 大规模、IaC、可观测性深度加大。
