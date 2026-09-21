# 模块化面试题（modules）

> 每道题遵循 [../docs/STANDARD.md](../docs/STANDARD.md) 模板：`难度 / 关键词 / 概念速记 / 问题 / 参考答案 / 易错点 / 延伸`。
> 题号在各文件内连续；跨文件引用用「主题 + Q 号」。

## 目录

| 模块 | 路径 | 题量 | 侧重 |
|---|---|---|---|
| Linux 系统 | [linux/linux-questions.md](linux/linux-questions.md) | 28 | 进程/内存/IO/内核/Shell/容器运行时 |
| 网络 | [network/network-questions.md](network/network-questions.md) | 27 | OSI/TCP/DNS/负载均衡/CNI/源IP |
| Kubernetes | [kubernetes/kubernetes-questions.md](kubernetes/kubernetes-questions.md) | 52 | CRI/CNI/CSI/调度/排障/client-go/DRA/超大规模控制面/块存储选型 |
| CI/CD & IaC | [cicd-iac/cicd-iac-questions.md](cicd-iac/cicd-iac-questions.md) | 25 | 流水线/Terraform/Ansible/Argo CD/镜像构建 |
| 监控可观测 | [observability/observability-questions.md](observability/observability-questions.md) | 23 | Prometheus/三支柱/SLO/OTel/基数/Falco 运行时安全 |
| 故障/SRE | [sre-reliability/sre-questions.md](sre-reliability/sre-questions.md) | 29 | 排障/高可用/容量/复盘/真实事故 |
| 中间件 | [middleware/middleware-questions.md](middleware/middleware-questions.md) | 20 | Kafka/Redis/MySQL/ES/MongoDB 文档模型与向量检索/上云权衡 |
| GPU/AI | [gpu-ai/gpu-ai-questions.md](gpu-ai/gpu-ai-questions.md) | 26 | CUDA/调度/推理/监控/HAMi/拓扑 |
| 云/安全 | [cloud-security/cloud-security-questions.md](cloud-security/cloud-security-questions.md) | 17 | IAM/VPC/FinOps/合规/供应链/CKS 实操/官方安全审计/RBAC 攻击面审计 |
| 服务网格/网关 | [service-mesh/service-mesh-questions.md](service-mesh/service-mesh-questions.md) | 25 | Istio/Envoy/xDS/Ambient/Gateway API/异构系统迁入网格 |
| 前沿部署工程师 FDE | [fde/fde-questions.md](fde/fde-questions.md) | 30 | 角色/C.A.S.E./数据工程/GCP 着陆区/RAG 与评测/隔离网络/咨询与案例 |
| AI 工程 / Agentic | [ai-engineering/ai-engineering-questions.md](ai-engineering/ai-engineering-questions.md) | 27 | Agent 循环/记忆/上下文/权限/钩子/MCP/子代理/技能/无头 CI/护栏/注入/评测/LLM 流水线案例 |
| 系统设计 | [system-design/system-design-questions.md](system-design/system-design-questions.md) | 35 | 方法论/估算/限流/KV/缓存/MQ/信息流/IM/监控/日志/调度/发布/容灾/RAG/LLM 推理；630 主题目录见 [system-design-catalog.md](system-design/system-design-catalog.md) |
| 行为/架构 | [behavior/behavior-questions.md](behavior/behavior-questions.md) | 10 | STAR/推动/选型/AI 护栏/事故沟通 |

> 合计 **374 题**。系统设计模块另附 [system-design-catalog.md](system-design/system-design-catalog.md)（`system-design/` 子模块 630 个主题的自动目录，含面试官执行手册与五维评分表入口）。

## 难度图例

🟢 初级 · 🟡 中级 · 🔴 高级 · ⚫ 资深
