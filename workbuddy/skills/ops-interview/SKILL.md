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
- `references/collections-k8s-web-archive.md`：Kubernetes / 云原生网页存档与仓库文档专题（697 题，78 组，从两批本地资料提炼，每题附要点）：手册全 20 章 → Gateway API / 推理网关 / kgateway → Istio 安装与 API 字段 → Envoy·xDS 与网格工程博客 → GitOps / CNI / 运行时 / etcd → KubeHound 攻击路径 / rbac-police / 威胁矩阵与 CVE 家族 / HummerRisk / 安全清单 → GPU 多租户与 AI Infra → LLM 推理引擎与 LLMOps 工具 → MCP 协议与 Agent 工程 → RAG 实战（含代码）→ 架构 / ES / Spring Boot 生产化 / 事故复盘 → 中文社区 → 用户实验集群运维 → The New Stack ×6 → 系统设计拆解与速答；文末有分组 → 模块映射。
- `references/collections-veeramalla-devops-interview-guide.md`：DevOps / SRE 公司真题（3024 题，来自 iam-veeramalla/DevOps-Interview-Guide 的 151 份 2025–2026 真实面试写实，86 家公司：Amazon、JPMorgan、IBM、Infosys、TCS、Deloitte、EPAM、Capgemini、Oracle、SAP、Sony 等；按公司 / 岗位 / 经验年限分组，纯题目）：候选人报出目标公司时优先从这里抽「同款」题，参考答案回到分模块题库。
- `references/collections-awesome-claude-code.md`：Agentic 工具链生态专题（392 题，22 组，按 hesreallyhim/awesome-claude-code 的分类体系由本项目原创撰写，每题附要点；上游榜单为 CC BY-NC-ND，未收录其点评文字）：扩展点选型与准入尽调 → 官方心智模型（agent loop / 上下文工程 / Building Effective Agents）→ CLAUDE.md / Rules / Skills / Subagents / Hooks / Plugins 选型 → slash command 与钩子工程 → 技能编写与治理 → 记忆与上下文持久化 → 多 Agent 编排与 Ralph 循环 → 会话可观测与 hook 事件流 → 用量成本与配额 → 状态行 → 沙箱 / 提示注入 / 供应链安全 → Provider 与运行时集成 → 替代客户端与远程控制 → 配置 lint 与规则漂移 → Terraform/K8s/OTel 技能 → 测试与审查质量门 → 文档知识应用 → 开放判断题；候选人面试「AI 工程 / 平台工程 / 用 AI 做运维」方向时，与 `references/questions.md` 的 ai-engineering 模块搭配使用。
- `references/collections-system-design-exercises-and-notes.md`：系统设计练习与笔记（63 题，9 组：基础 / 扩展与韧性 / 缓存与迁移 / 设计题 / 推荐 / 搜索 / 对话与 RAG / Meta PE 监控系统 / 全量主机设计 + 排障；适合「一次 10 题」的系统设计批量轮次）
- `references/collections-system-design-quiz-bank.md`：系统设计题库（458 题，70 个主题，按 catalog 分类 7 组；🟡 quiz · 🔴 drill · 🟢 速答；适合「一次 10 题」的系统设计轮次）
- `references/system-design-resolver.md`：系统设计**主题解析器**（181 条别名，含 78 条中文题名；82 组重复主题折叠；2 个真薄主题 + 21 个用非标准编号的主题——后者要先 `ls` 目录再判断，别误说「语料薄」）。候选人说「短链 / 秒杀 / TinyURL / autocomplete / chatpgt」这类名字时，先查它拿到规范主题目录，再按 catalog 读文档；查不到也要用 Q1–Q4 方法论照常开面，并说明语料没有该主题。
- `references/collections-aws-managed-services-only.md`：「只用 AWS 托管服务」改造专题（195 题，13 组，从用户自有 aws-demo / search-platform 文档集提炼，每题附要点）：约束本身的得失、26 服务目标架构与 chosen/rejected 选型表、IRSA 与「Pod 自己读 Secrets Manager」（vs External Secrets / CSI）、CloudWatch vs AMP+Managed Grafana vs 自建（没有直方图与标签选择器的代价、按自定义指标计费与基数）、AWS Backup + 恢复演练计划 + 「AWS 没有服务备份 K8s API 对象」这个被命名的缺口（git 漂移检查 vs Velero）、GPU on EKS 的托管边界（加速 AMI 与 Operator 开关、CloudWatch agent 不发布的 DCGM profiling 指标、gang scheduling、SageMaker HyperPod）、VPC Lattice vs Istio ambient / Linkerd / Cilium 与 App Mesh 停服、CodePipeline 与 EKS 托管 Argo CD（push vs pull）、MSK/Kinesis/Firehose 与 ElastiCache/MemoryDB 的区域覆盖、AI 存储、MCP/Agent 在 AWS 上的缺口，「从未部署过的架构该怎么写」（Verified, and not / 推理值 vs 观测值 / 如何诚实地命名缺口），以及 **11 个经典系统设计题的 AWS-only 渲染**（65 题：短链的 CDN 即读路径与 301/302 成本决策、IM 的扇出选型与会话内原子计数器、票务的条件写即锁与边缘等候室、调度的三服务分类与「沉默即最坏失败」、通知的幂等边界与优先级队列、爬虫的礼貌即队列拓扑、信息流的混合扇出阈值、直播的延迟菜单与缓存键错误、文件存储的内容定义分块与 IAM 配额陷阱、缓存的四层位置与失效组合、分析的 Athena 文件布局）。

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
