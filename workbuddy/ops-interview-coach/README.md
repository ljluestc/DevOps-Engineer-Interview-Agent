# Ops Interview Coach（运维面试教练）

一个基于结构化运维知识体系的面试模拟智能体：既能**逐题模拟面试并打分**，也能**讲透基础概念**（OSI、CRI/CNI/CSI、Dockerfile、Ansible、GPU 等）。覆盖 Linux、网络、Kubernetes、CI/CD、可观测性、SRE、中间件、GPU/AI、云安全、系统设计、FDE 前沿部署、AI 工程 / Agentic、行为与架构共 13 大模块，适配实习到高管各层级。

> 本智能体的题库与基础篇源自开源项目 [ops-interview](https://github.com/)（200 题 + 深度基础篇），本专家内置其浓缩版，可离线独立使用。

## 类型
Agent 型（单个 AI 专家）

## 核心能力
- **逐题模拟面试**：一次一题，按模块/难度/级别动态出题；作答后给 ✅⚠️💡📊 结构化反馈与 1–10 评分；支持 `hint`/`skip`/`explain`/`score`/`harder`/`easier`/`switch`/`end`/`restart` 指令。
- **概念深度讲解**：用「速记 + 原理 + 对比表 + 误区」讲清高频基础词，拒绝只抛名词。
- **完整记分卡**：结束输出各模块得分、总分、录用裁决（Strong Hire → No Hire）、关键优势、待改进项与推荐学习主题。
- **简历驱动定制**：可分析简历并针对性出题、动态调难度。

## 内置知识（skills/ops-interview）
- `references/basics.md`：深度基础篇（Linux / 网络·OSI / Docker·Dockerfile / K8s·CRI·CNI·CSI / Ansible / AI·GPU）
- `references/questions.md`：分模块题库（14 模块含服务网格、系统设计、FDE 与 AI 工程，标准化模板 + 🟢🟡🔴⚫ 难度图例）
- `references/collections-cuiliang-2024.md`：高级真题 231 题（☆ 高频标记）
- `references/collections-cuiliang-mid-2020.md`：中级真题 89 题
- `references/collections-ops-bank-1502.md`：22 专题大题库 1502 题（Ansible→Zabbix 全覆盖，真实真题）
- `references/collections-mongodb-zero-to-hero.md`：MongoDB 专题 68 题（文档模型 → CRUD → 日志实战 → 向量检索，附要点）
- `references/collections-k8s-local-library.md`：K8s 本地资料库 159 题（CKS 实操 → 官方安全审计 → 部署与安全模式 → Ambient / Aeraki → 阿里超大规模 → DRBD/LINSTOR → 排障笔记 → kubectl 速查，附要点）
- `references/collections-classic-papers.md`：经典论文 111 题（Paxos / Raft / GFS / MapReduce / Lamport / HTTP/2 / REST / JVM GC，附要点 + 书架索引）

## 使用示例
- 「模拟一场高级运维工程师面试，从 Linux 与系统内核开始」
- 「考我一道 Kubernetes 网络面试题（CNI/CRI/CSI）」
- 「讲透 OSI 七层模型以及它和真实排障的对应关系」

## 头像
头像已自动生成在 `avatars/` 目录下。如需替换，要求：PNG/JPG、512×512 px、≤500KB。

## 安装 / 注册
专家包已置于专家目录：
```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/ops-interview-coach/
```
注册后即在 WorkBuddy 中可见：
```bash
python3 scripts/register_expert.py <expert-dir>
```

## 打包分享
```bash
zip -r ops-interview-coach.zip ops-interview-coach/
```
