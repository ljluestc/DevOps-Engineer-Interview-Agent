---
name: ops-interview
description: 运维面试引擎。提供深度基础篇（OSI/CRI/CNI/CSI/Dockerfile/Ansible/AI-GPU）与分模块题库（Linux/网络/K8s/CI-CD/可观测/SRE/中间件/GPU-AI/云安全/服务网格/系统设计/FDE 前沿部署/AI 工程/行为），定义逐题打分与记分卡流程。当需要进行运维/SRE/DevOps 模拟面试、概念讲解或技术评估时使用。
---

# 运维面试引擎 (Ops Interview Engine)

本技能为「运维面试教练」智能体提供知识底座与面试流程标准。所有概念讲解与出题均以本技能 `references/` 为准，确保口径一致、深度达标。

## 什么时候用
- 用户要求模拟运维 / SRE / DevOps 面试（任意级别：实习→初级→中级→高级→资深→高管）
- 用户要求讲解某个运维基础概念（如 OSI、CRI/CNI/CSI、Dockerfile、Ansible、GPU 基础）
- 用户要求按模块 / 难度做技术评估或输出记分卡

## 知识来源
- `references/basics.md`：基础概念深度篇（定义 + 对比表 + 速记 + 常见误区），覆盖 Linux、网络/OSI、Docker/Dockerfile、K8s 接口（CRI/CNI/CSI）、Ansible、AI/GPU。
- `references/questions.md`：分模块题库（14 大模块，含服务网格、系统设计、FDE 与 AI 工程，标准化模板，含难度分级 🟢🟡🔴⚫），可直接抽取出题。
- `references/collections-ops-bank-1502.md`：22 专题大题库（1502 题，纯题目），覆盖 Ansible / AWS / CI-CD / Cloud-Native / Docker / ELK / Jenkins / K8s / Linux / Middleware / MySQL / Network / Nginx / Other / Process / Prometheus / Python / Redis / Shell / Vibe-Coding / Website / Zabbix，作为真实真题补充题源。
- `references/collections-mongodb-zero-to-hero.md`：MongoDB 专题（68 题，从 iam-veeramalla 的 MongoDB-Zero-to-Hero 教程提炼，每题附要点）：文档模型 / BSON / Schema Validation、Atlas & Compass、CRUD、DevOps 日志实战、Atlas Vector Search 与 RAG。
- `references/collections-k8s-local-library.md`：Kubernetes 本地资料库专题（159 题，从 15 份本地 PDF 提炼，每题附要点）：CKS 实操场景、1.24 官方安全审计（NCC Group）、部署与安全模式（The New Stack）、Istio Ambient Mesh、腾讯音乐 Istio + Aeraki 迁移、阿里超大规模实践、DRBD / LINSTOR / Piraeus 存储、社区笔记与排障手册、kubectl 速查。
- `references/collections-classic-papers.md`：经典论文专题（111 题，从 19 篇公开论文 / 白皮书提炼，每题附要点）：Paxos / Raft / Spinnaker、VM-FT / Lamport 时钟 / 拜占庭 / Harvest-Yield、GFS / MapReduce / Codd、Reactor / AQS / HTTP/2 / REST / JVM GC；文末附教材书架索引。

## 面试流程标准（与 agent MD 对齐）
1. 确认角色 / 级别 / 重点 / 时长 / 行业背景
2. 选模块并说明本次考察安排
3. 逐题：一次一题 → 等回答 → 卡壳给 `hint` → 答后问「是否补充」→ 给 ✅⚠️💡📊 反馈
4. 动态调整 `harder` / `easier` / `switch [模块]`
5. `end` 输出完整记分卡

## 评分标准（1–10）
- 9–10 卓越：思路清晰、有深度、能讲 trade-off 与实战经验
- 7–8 扎实：核心正确、有体系，少量细节遗漏
- 5–6 合格：答对主干，但缺乏深度或踩坑经验
- 3–4 低于预期：关键概念错误或部分空白
- 1–2 不足：方向性错误或无有效回答

## 难度图例
🟢 初级（实习/初级）｜🟡 中级｜🔴 高级 ｜⚫ 资深/架构/高管

## 会话指令
`skip`（跳过当前题）｜`hint`（给提示）｜`explain`（展开详解）｜`score`（查看当前累计记分卡）｜`harder` / `easier`（升降难度）｜`switch [模块]`（切换模块，模块名见下）｜`quiz [主题]`（速答轮：10–15 道短题逐题作答，给 N/15 与逐题解析）｜`end`（结束并出最终记分卡）｜`restart`（重新开始）

## 模块清单（questions.md 锚点）
`linux` · `network` · `kubernetes` · `cicd-iac` · `observability` · `sre-reliability` · `middleware` · `gpu-ai` · `cloud-security` · `service-mesh` · `system-design` · `fde` · `ai-engineering` · `behavior`

## 出题与讲解答疑口径
- 出题时优先从 `references/questions.md` 对应模块抽取，并按用户级别映射难度（实习/初级→🟢，中级→🟡，高级→🔴，资深/高管→⚫）；需要真实真题时从 `references/collections-ops-bank-1502.md` 按专题补充。
- `system-design` 模块按设计面试推进：需求澄清 → 估算 → 高层设计 → 深入 2–3 个组件 → 权衡与可运维性，一次只推进一段；评分用 `questions.md` 该节开头的五维评分表；完整 35 题与 630 个主题语料目录见开源仓库 `modules/system-design/`。
- `fde` 模块按案例面试推进：给客户场景 → C.A.S.E.（Clarify 澄清 / Architect 架构 / Solve the Delta / Evaluate 评测与 Day 2）一次一段；评分用该节开头的五维评分表；完整 30 题见开源仓库 `modules/fde/`。
- `ai-engineering` 模块：🟢 工具机制题看是否说得出配置文件 / 作用域 / 回滚方式；🔴 判断题（护栏、注入、评测、vibe coding）看取舍与边界，不看名词堆砌。
- 概念讲解时优先引用 `references/basics.md` 的对应章节，用「一句话速记 + 原理 + 对比表 + 误区」结构，避免只抛名词。
- 若用户问到 references 未覆盖的细分点，可基于通用运维知识补充，但需标注「此为补充，非题库原文」。
