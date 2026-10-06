# Collections — 收录的外部真题

本目录收录来自社区公开文章的**真实面试真题**，用于扩充智能体出题覆盖面。
与 `modules/`（自研标准化题库）不同，这里**保留原作者的分组与标记**，便于对照原始出处。

## 收录清单

| 文件 | 来源 | 题量 | 说明 |
|---|---|---|---|
| `ops-question-bank-1502.md` | 运维面试题目汇总（按专题整理） | 1502 题 | 22 专题大合集：Ansible / AWS / CI-CD / Cloud-Native / Docker / ELK / Jenkins / K8s / Linux / Middleware / MySQL / Network / Nginx / Other / Process / Prometheus / Python / Redis / Shell / Vibe-Coding / Website / Zabbix |
| `cuiliang-ops-interview-2024.md` | [崔亮博客：高级运维工程师面试题汇总](https://www.cuiliangblog.cn/detail/article/89) | 231 题 | 2024 年 7–8 月面试 20+ 家公司 50+ 场，☆ 标记高频题 |
| `cuiliang-mid-ops-interview-2020.md` | [崔亮博客：中级运维工程师面试题汇总](https://www.cuiliangblog.cn/detail/article/2) | 89 题 | 2020 年发布的中级运维面试题（含 MySQL/NoSQL/Docker/K8s/Prometheus/ELK/运维开发）|
| `cuiliang-entry-ops-interview-2020.md` | [崔亮博客：linux运维工程师面试题总结](https://www.cuiliangblog.cn/detail/article/1) | 88 题 | 2020 年 11 月发布（IBM/新浪/完美世界等），与中级篇高度重合，仅 2–3 题独有，存档备查 |
| `mongodb-zero-to-hero.md` | [iam-veeramalla/MongoDB-Zero-to-Hero](https://github.com/iam-veeramalla/MongoDB-Zero-to-Hero)（Apache-2.0 教程，题目由本项目提炼） | 68 题 | 6 章：关系型 vs 文档型 / BSON / Schema Validation → 库·集合·文档·索引 → Atlas & Compass → CRUD → DevOps Log Explorer 实战 → Atlas Vector Search（AI 应用）；每题附要点，🟢🟡🔴 标难度，☆ 高频 |
| `k8s-local-library.md` | 用户本机 Kubernetes 资料库（15 份 PDF：Saiyam Pathak《CKS Book》、NCC Group《Kubernetes 1.24 Security Audit》、The New Stack《Kubernetes Deployment & Security Patterns》、Conf42 Istio Ambient Mesh、IstioCon 腾讯音乐 Istio + Aeraki、阿里巴巴 k8s 超大规模实践、全速云 Linstor/DRBD 课件、四份社区笔记与排障手册、Aman Pathak 30DaysOfKubernetes 合订、两份 kubectl 速查表；题目由本项目提炼） | 159 题 | 10 组：CKS 实操 → 1.24 官方安全审计 → 部署与安全模式（2018）→ Ambient Mesh → Aeraki 落地 → 阿里超大规模 → DRBD/LINSTOR/Piraeus → 学习笔记与排障 → End to End 笔记 → kubectl 速查；每题附要点，🟢🟡🔴 标难度，☆ 高频 |
| `classic-papers.md` | 用户本机 `~/ebooks/`（frankyyyt/ebooks 克隆）中的 19 篇公开论文与白皮书：Paxos Made Simple、Raft（扩展版）、Spinnaker、VM-FT、Lamport 时钟、拜占庭将军、Harvest & Yield、GFS、MapReduce、Codd 关系模型、客户端缓存一致性（VLDB 1990）、Reactor、AQS、Why Events Are a Bad Idea、事务策略、http2 explained、InfoQ REST eMag、HotSpot 内存管理白皮书、accept() 惊群；题目由本项目提炼 | 111 题 | 4 组：共识与复制 → 容错 / 时钟 / 可用性取舍 → 大规模存储与计算 → 系统并发 / 协议 / 运行时；每题附要点，☆ 高频；文末附约 70 本教材的书架索引（不出题） |
| `k8s-web-archive.md` | 用户本机的网页存档与仓库文档（`~/Downloads/slurps/`、`~/dev/k8s/slurps/`、Go module cache、`~/dev/KubeHound`、用户自有实验集群与文章、按 URL 指定的 HummerRisk / kubernetes-security-checklist / rbac-police / awesome-cloud-native-security / awesome-mcp-servers / RAG-crash-course、六本 The New Stack 电子书、两套系统设计自测、HelloInterview 分布式缓存拆解；题目由本项目提炼） | 697 题 | 78 组：手册全 20 章 → Gateway API / 推理网关 / kgateway → Istio 安装与 API 字段 → Envoy·xDS 与网格工程博客 → GitOps / CNI / 运行时 / etcd → KubeHound 攻击路径 / rbac-police / 威胁矩阵与 CVE 家族 / HummerRisk / 安全清单 → GPU 多租户与 AI Infra → LLM 推理引擎与 LLMOps 工具 → MCP 协议与 Agent 工程 → RAG 实战（含代码）→ 架构 / ES / Spring Boot 生产化 / 事故复盘 → 中文社区 → 用户实验集群运维 → The New Stack ×6 → 系统设计拆解与速答；每题附要点，🟢🟡🔴 标难度，☆ 高频 |
| `veeramalla-devops-interview-guide.md` | [iam-veeramalla/DevOps-Interview-Guide](https://github.com/iam-veeramalla/DevOps-Interview-Guide)（2025–2026 年社区投稿的真实面试经历，151 份写实、86 家公司 + Others；仓库未声明许可证，仅收录题目文本） | 3024 题 | 按公司 / 岗位 / 年限分组（Amazon、JPMorgan、IBM、Infosys、TCS、Deloitte、EPAM、Capgemini、Oracle、SAP、Sony …），Kubernetes / Docker / Terraform / 云 / CI-CD / Linux / 脚本 / SRE 基础；文末附主题 → 模块映射 |
| `awesome-claude-code.md` | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)（榜单本体 CC BY-NC-ND 4.0，**未收录其点评文字**；题目与要点由本项目原创撰写） | 392 题 | 22 组：生态选型与准入尽调 → Start Here 官方心智模型 → From Anthropic 一手资料 → 扩展机制选型（CLAUDE.md / Rules / Skills / Subagents / Hooks / Plugins）→ Slash Commands → Hooks → Agent Skills → 记忆与上下文持久化 → 多 Agent 编排 → Ralph Wiggum 循环 → 会话可观测与事件流 → 用量成本与配额 → Status Lines → 安全 / 沙箱 / 供应链 → Provider 与运行时集成 → 替代客户端与远程控制 → 配置 lint 与规则治理 → IaC / K8s / OTel 专项技能 → 测试与审查质量门 → 文档知识与学习 → 设计写作创意 → 开放判断题；每题附要点，🟢🟡🔴 标难度，☆ 高频，文末附分组 → 模块映射与难度分层选题表 |
| `aws-managed-services-only.md` | 用户自有仓库 `~/dev/aws-demo`（58 篇 `docs/*-on-aws.md`、`docs/system-design/` 下 11 篇经典系统设计的 AWS-only 渲染页、`search-platform` 的 20 篇 Tip 文档，2026-09-25/26「AWS-only 改造」后的状态；题目与要点由本项目提炼撰写） | 195 题 | 13 组：「只用托管服务」这条约束 → 26 服务目标架构与 chosen/rejected 选型表 → IRSA 与 Secrets Manager（vs External Secrets / CSI）→ CloudWatch vs AMP+Managed Grafana vs 自建 → AWS Backup 与「没有服务备份 K8s 对象」的缺口（git 漂移检查 vs Velero）→ GPU on EKS 托管边界（加速 AMI / DCGM / gang scheduling / HyperPod）→ VPC Lattice vs 网格 → CodePipeline 与 EKS 托管 Argo CD（push vs pull）→ MSK/Kinesis、ElastiCache/MemoryDB 与 AI 存储 → MCP/Agent 在 AWS 上的缺口 → 未验证架构的写法（Verified, and not）→ **11 个经典系统设计题的 AWS-only 渲染**（短链 / IM / 票务 / 定时任务 / 通知 / 爬虫 / 信息流 / 直播 / 文件存储 / 分布式缓存 / Web 分析，65 题）；每题附要点，🟢🟡🔴 标难度，☆ 高频 |

> **合计**：collections 共收录 **6556 题**（1502 + 231 + 89 + 88 + 68 + 159 + 111 + 697 + 3024 + 392 + 195，去重前）。

## 版权与使用口径（重要）

- 本目录**仅收录题目列表**（公开网页上可直接阅读的问题文本），**不收录**原作者的参考答案、个人心得与付费内容。
- 每题保留原文措辞与 ☆ 高频标记；分组沿用原文。
- 如需商用或对题目做二次加工分发，请自行评估原作者版权声明；本项目以「学习与参考」为目的收录，并明确标注出处。
- 收录日期：2026-08-05（崔亮系列）、2026-08-19（1502 题合集）、2026-09-20（MongoDB Zero-to-Hero、K8s 本地资料库、经典论文、K8s 网页存档与本地仓库、Veeramalla DevOps 真题）、2026-09-21（Awesome Claude Code 生态）、2026-09-26（AWS 托管服务改造）、2026-10-03（K8s 网页存档补 HelloInterview 分布式缓存组）。
- `mongodb-zero-to-hero.md` 是例外：原仓库是 Apache-2.0 教程而非题库，题目与要点由本项目从教程改写提炼，可自由使用，保留出处即可。
- `k8s-local-library.md` 同为提炼件：来源是本机 15 份 PDF（商业电子书 / 公开审计报告 / 演讲 PPT / 社区笔记），题目与要点由本项目改写，不含逐字摘录；两份商业资料（CKS Book、全速云课件）只提炼主题与开源部分。文件头有逐份的版权口径表。
- `classic-papers.md` 同为提炼件：来源全部是公开论文 / 白皮书（版权归作者与出版方），题目与要点由本项目改写；书架索引里的教材**不出题**。
- `veeramalla-devops-interview-guide.md` 与崔亮系列同一口径：**只收录题目文本**（原文英文措辞），按原仓库的公司 / 岗位分组，不收录投稿者答案；仓库未声明许可证，作学习参考并标注出处。
- `awesome-claude-code.md` 口径**最严**：上游榜单采用 **CC BY-NC-ND 4.0**（禁止演绎），因此本文件**不是**该榜单的副本或改编版——不收录原作者撰写的条目点评，也不复制其分类排版；只以事实方式引用项目名称与仓库地址，题目与答案要点全部由本项目原创撰写，依据为 Claude Code 官方文档、Anthropic 工程博客与各项目自身的公开 README。需要读原榜单点评请直接访问上游链接。
- `k8s-web-archive.md` 同为提炼件：来源是网页存档 / 开源仓库文档 / 用户自有仓库与文章 / 免费电子书 / 演讲与博客，题目与要点由本项目改写，不含逐字摘录；用户自有实验集群文档只提炼做法与原理并做脱敏（不含主机名、IP、账号、凭据）；商业书籍只出主题级题目。文件头有逐份的版权口径表。
- `aws-managed-services-only.md` 来源是**用户自有仓库**（`~/dev/aws-demo`，自有版权），题目与要点由本项目从其文档集提炼撰写，可自由使用；文中引用的第三方资料（AWS 官方文档、Velero 升级说明、AWS China 与个人博客、The New Stack 电子书等）只引用结论与事实，不含逐字摘录。**重要口径**：来源文档描述的是一个**从未 apply 到 AWS 账号**的目标架构（Terraform 只 validate 过），因此其中的阈值、成本与恢复时间是推理值而非观测值——文件头已写明，出题时应把「哪些数字需要先测量」当作考点。

## 智能体如何用它

面试官出题时：**优先**从 `modules/` 抽取标准化题（有参考要点与难度），**补充**从 `collections/` 抽取真题（带 ☆ 的高频题优先）。

### 崔亮系列 → modules 映射

| 原分类 | 对应 modules 模块 |
|---|---|
| Linux | `linux` |
| MySQL / NoSQL | `middleware` |
| Docker | `kubernetes`（容器基础）|
| Kubernetes | `kubernetes` |
| Prometheus | `observability` |
| ELK | `middleware`（ES 部分）|
| DevOps / 运维开发 | `cicd-iac` |
| Python/VUE | 无直接对应（开发向，作为补充题源）|
| 日常工作 / 开放性问题 | `sre-reliability` + `behavior` |

### 1502 题合集 → modules 映射

| 合集专题 | 题量 | 对应 modules 模块 | 备注 |
|---|---|---|---|
| ANSIBLE | 42 | `cicd-iac` | 含 Terraform 2 题 |
| AWS | 103 | `cloud-security` | 云服务全覆盖 |
| CI-CD | 83 | `cicd-iac` | 含 DevOps 文化、GitOps、ArgoCD |
| CLOUD-NATIVE | 74 | `cloud-security` + `cicd-iac` | 含 Terraform 深度、Service Mesh、OTel |
| DOCKER | 88 | `kubernetes`（容器基础）| 镜像/网络/存储/安全/Compose |
| ELK | 50 | `observability` + `middleware` | ES 架构/调优 + Logstash/Filebeat |
| JENKINS | 30 | `cicd-iac` | Pipeline/Agent/HA/安全 |
| K8S | 200 | `kubernetes` | 最大专题，覆盖全链路 |
| LINUX | 138 | `linux` | 内核/文件系统/网络/性能/安全 |
| MIDDLEWARE | 25 | `middleware` | Kafka/RabbitMQ/RocketMQ |
| MYSQL | 100 | `middleware` | 索引/事务/复制/调优/高可用 |
| NETWORK | 68 | `network` | TCP/IP/DNS/LVS/防火墙 |
| NGINX | 75 | `network`（反向代理）+ `middleware` | 无独立模块，跨网络与中间件 |
| OTHER | 50 | 跨模块 | Windows/Python/Puppet/Chef/MongoDB/行为面 |
| PROCESS | 79 | `sre-reliability` + `behavior` + `cloud-security` | 运维体系/安全治理/编程基础 |
| PROMETHEUS | 64 | `observability` | 含 Thanos/VM/Grafana/Nagios |
| PYTHON | 49 | 无直接对应（开发向）| 补充题源 |
| REDIS | 27 | `middleware` | 缓存模式/高可用/调优 |
| SHELL | 53 | `linux`（Shell 部分）| 脚本实战/监控/自动化 |
| VIBE-CODING | 29 | 无直接对应（AI 向）| Agent/MCP/Skill/工作流 |
| WEBSITE | 43 | `network` + `middleware` + `sre-reliability` | Web 架构/排障/LVS |
| ZABBIX | 32 | `observability` | 传统监控体系 |

### MongoDB Zero-to-Hero → modules 映射

| 教程章节 | 题量 | 对应 modules 模块 | 备注 |
|---|---|---|---|
| 一、Introduction（关系型 vs 文档型 / BSON / Schema Validation / Vector Search 概念） | 14 | `middleware` Q19 | 概念与选型 |
| 二、Building Blocks（库 / 集合 / 文档 / 字段 / _id / 索引） | 11 | `middleware` Q19 | 建模与索引 |
| 三、Atlas & Compass（托管集群、账号、IP 白名单、连接串） | 10 | `middleware` + `cloud-security` | 托管服务责任边界 |
| 四、CRUD（insert / find / update 操作符 / delete / upsert / 原子性） | 14 | `middleware` Q19 | 命令与语义 |
| 五、DevOps Log Explorer（PyMongo、日志文档、TTL、复合索引、Change Streams） | 9 | `observability` + `middleware` | 日志存储选型 |
| 六、MongoDB for AI Apps（embedding、向量索引、$vectorSearch、RAG、向量库选型） | 10 | `middleware` Q20 + `gpu-ai` + `system-design` | AI 应用 |

### K8s 本地资料库 → modules 映射

| 本文件分组 | 题量 | 对应 modules 模块 | 备注 |
|---|---|---|---|
| 一、CKS 实操场景 | 19 | `cloud-security` Q15、Q10–Q12、Q14；`kubernetes` Q15 / Q25–Q27 / Q32 | NetworkPolicy、AppArmor / seccomp、RBAC、审计、kube-bench、Falco、准入 webhook |
| 二、1.24 官方安全审计 | 15 | `cloud-security` Q16、Q11；`kubernetes` Q25 / Q43 / Q49 | 威胁模型、nodes/proxy、CA 共用、RBAC 无 Deny、NetworkPolicy 局限 |
| 三、部署与安全模式（2018） | 24 | `kubernetes` Q10 / Q14 / Q29 / Q32；`cloud-security` Q1 / Q2 / Q11；`cicd-iac`；`observability` | 部署模式对比、认证 / 授权 / 准入、审计、配额（注意年代） |
| 四、Istio Ambient Mesh | 8 | `service-mesh` Q14 / Q15 / Q18 / Q24 | ztunnel / waypoint / HBONE / Gateway API |
| 五、Istio + Aeraki 落地 | 11 | `service-mesh` Q25、Q21 / Q22 / Q10 | MetaProtocol、外部服务发现、多控制面合并 |
| 六、阿里超大规模实践 | 10 | `kubernetes` Q51、Q38 / Q40 / Q41 | List & Watch / Bookmark / 缓存索引 / 面向终态 / OpenKruise |
| 七、DRBD / LINSTOR / Piraeus | 8 | `kubernetes` Q52、Q16 / Q17；`middleware` | 内核态复制、超融合、与 Ceph 的取舍 |
| 八、学习笔记与排障手册 | 26 | `kubernetes` Q3–Q9 / Q20 / Q23 / Q29 / Q30；`cicd-iac` | 三阶段排障法、Pending / CrashLoopBackOff / 抢占驱逐 |
| 九、End to End 笔记 | 30 | `kubernetes` 全模块；`cicd-iac`；`observability`；`cloud-security` | kubeadm → 托管集群 → DevSecOps 流水线 |
| 十、kubectl 速查 | 8 | `kubernetes` Q23；`quiz kubernetes` | 命令速答 |

### 经典论文 → modules 映射

| 本文件分组 | 题量 | 对应 modules 模块 | 备注 |
|---|---|---|---|
| 一、Paxos / Raft / Spinnaker | 27 | `system-design`（共识、复制、KV 存储主题）；`kubernetes` Q40（etcd）；`middleware` | 多数派、选举、日志复制、成员变更、一致性读 |
| 二、VM-FT / Lamport 时钟 / 拜占庭 / Harvest-Yield | 25 | `sre-reliability`；`system-design`（CAP 与降级） | 输出规则、happens-before、3f+1、harvest vs yield |
| 三、GFS / MapReduce / Codd / 客户端缓存一致性 | 25 | `system-design`（分布式文件、批处理）；`middleware`；`linux` | 单 master、租约、记录追加、备份任务、数据独立性 |
| 四、Reactor / AQS / 线程 vs 事件 / 事务策略 / HTTP/2 / REST / JVM 内存 / accept() 惊群 | 34 | `linux`（I/O 模型、并发）；`network`（HTTP/2、REST）；`middleware`（JVM、事务） | Nginx / Redis 的 Reactor 根源、HPACK、代际 GC、惊群 |

<!-- k8s-web-archive-mapping -->
### K8s 网页存档与本地仓库 → modules 映射

| 本文件分组 | 题量 | 对应 modules 模块 | 备注 |
|---|---|---|---|
| 一、Jimmy Song 手册：架构、开放接口与 Pod | 9 | `kubernetes` Q3 / Q16 / Q22 / Q40 / Q47；study guide Q1 / Q12 | 补 etcd 直读、CRI / CNI 协议细节、restartPolicy 退避、Init 资源计算、Hook 语义、PDB |
| 二、Jimmy Song 手册：集群资源、控制器与服务发现 | 11 | `kubernetes` Q6 / Q8 / Q9 / Q10 / Q29 / Q30 / Q39；study guide Q3 / Q4 / Q7 / Q8；`network` Q24；`gpu-ai` Q11 / Q26 | 补节点条件与内置污点、GC 级联删除、Label 语法、Deployment 高级行为、StatefulSet partition、Job / CronJob 参数、HPA 算法、EndpointSlice / 拓扑路由、Service 发现细节、IngressClass、Gateway API Inference Extension |
| 三、Jimmy Song 手册：网络、存储、安全与扩展 | 10 | `kubernetes` Q11 / Q14 / Q17 / Q25 / Q28 / Q43 / Q44 / Q48 / Q49 / Q50；`network` Q25 / Q26；`cloud-security` Q7 / Q11；study guide Q9 / Q10 | 补 Flannel host-gw 路由、Cilium L7 策略、hostPath / mountPropagation、local PV 与容量跟踪、ConfigMap 原子更新与 Reloader、etcd 静态加密、kubelet 认证授权、认证器映射与模拟、APIService 聚合层、CRD schema / 版本 / 子资源 |
| 四、Jimmy Song 手册：身份认证、集群访问与多集群 | 11 | `kubernetes` Q25 / Q33 / Q44 / Q49；`cloud-security` Q13；`service-mesh` Q8；`cicd-iac` Q20 | RBAC 细节、SA token 新机制、SPIRE 证明与注册器、kubeconfig 合并、SSA、多集群演进与 Karmada / k0rdent 追问 |
| 五、Jimmy Song 手册：集群运维、应用部署与开发指南 | 12 | `kubernetes` Q6 / Q11 / Q21 / Q29 / Q32 / Q41 / Q50；`cicd-iac` Q3 / Q14 / Q15 / Q18 / Q19；`observability` Q1 / Q5 / Q9 / Q18 / Q19；`gpu-ai` Q19 | 版本偏差与发布节奏、kubeadm HA / 证书、Terraform 所有权边界、Kustomize、StatefulSet vs Operator、Argo Rollouts、Volcano、Prometheus Adapter、Fluent Bit / LogQL、Jaeger / OTel 采样、informer 源码、Operator 测试 |
| 六、Jimmy Song 手册：Serverless、边缘计算与 AI 原生 | 9 | `kubernetes` Q36 / Q45；`gpu-ai` Q3 / Q9 / Q21 / Q23 / Q26；`observability` Q19 | Knative Serving / KPA / Eventing、OpenFaaS、KubeEdge 与 K3s / OpenYurt / SuperEdge 选型、vLLM on K8s、HAMi 策略与配额、DRA v1.34 流程 |
| 七、Gateway API：资源模型与角色 | 9 | `service-mesh` Q18（Gateway API vs Ingress、角色）/ Q10（Istio Gateway 等资源）；`kubernetes` Q10（Ingress 与 Service） | 本组是 Q18 的深挖：Listener distinct、hostname 交集、attach 握手、状态排障、GEP-1762 / 1713，均不与 Q18 的总览重复 |
| 八、Gateway API：路由、策略与 TLS | 12 | `service-mesh` Q18 / Q20；`network` 模块 TLS / HTTP 相关题 | 建议新增标准化模块题：HTTPRoute 匹配优先级与 filter 支持级别（🟡）、BackendTLSPolicy + 前端客户端证书校验（🔴）、Policy Attachment 模式（🔴） |
| 九、Gateway API：版本演进、一致性测试与迁移 | 9 | `service-mesh` Q19（Ingress → Gateway API 迁移步骤）/ Q20（Nginx Ingress / Istio Gateway / Envoy Gateway 选型）/ Q25（异构系统迁入网格） | Q19 只提到「用 ingress2gateway 转草稿」，本组补 provider / emitter、字段映射与冲突规则；Q20 的选型可引用本组的 Conformant 判定与 supportedFeatures 作为依据；GAMMA 题可作为 Q25 的追问 |
| 十、AI 推理网关：Gateway API Inference Extension 与 EPP | 11 | `service-mesh` Q18 / Q19 / Q20（Gateway API 基础）；`gpu-ai` Q9 / Q11 / Q23 / Q26；kubernetes-study-guide Q8 / Q14 | 推理网关是 Gateway API 之上的新层，建议在 service-mesh 或 gpu-ai 增一道标准化模块题（InferencePool + EPP + Flow Control），本组作追问 |
| 十一、kgateway / agentgateway：AI 网关与 Agent 流量治理 | 7 | `service-mesh` Q18 / Q20（网关选型）；`ai-engineering` Q13–Q26（MCP 网关、agent 安全边界）；`cloud-security`（JWT / API key 认证） | 与 ai-engineering 的「MCP gateway」判断题互补：这里给出具体 CRD 与合并规则 |
| 十二、GPU 共享、拓扑感知与推理部署（HAMi / vLLM / 主动扩缩） | 8 | `gpu-ai` Q2 / Q3 / Q21 / Q22 / Q23 / Q26；`kubernetes` Q42 / Q46 / Q47（调度扩展、Topology Manager、DRA） | 第 1、2、4 题是 Q21 的机制级追问；第 5 题是 Q22 的排查追问；第 8 题是 Q26 的实现级追问 |
| 十三、Istio 安装、升级与多集群拓扑 | 10 | `service-mesh` Q2 / Q5 / Q22 / Q23；`kubernetes` Q12 / Q26 | 安装机制、revision / tag 升级、CNI 与 iptables/nftables 内部、多集群与外部控制面的对象级步骤，是 Q5 / Q22 的深化追问 |
| 十四、Istio API 细节：DestinationRule / EnvoyFilter / WorkloadGroup / MeshConfig | 9 | `service-mesh` Q3 / Q10 / Q12 / Q16 / Q21 | 字段默认值与相互作用（LB / 连接池 / 异常剔除 / locality / TLS / EnvoyFilter 排序 / MeshConfig / ProxyConfig），可作 Q10 / Q12 的进阶 |
| 十五、Istio 安全与遥测 API：AuthorizationPolicy / RequestAuthentication / Telemetry / Wasm | 9 | `service-mesh` Q7 / Q8 / Q9 / Q13；`cloud-security` Q15 | CUSTOM / AUDIT / DENY-on-TCP / JWT 细节 / Telemetry 层级 / ext_authz 与 OTel provider / WasmPlugin→TrafficExtension，是 Q9 / Q13 的进阶 |
| 十六、Argo CD 进阶：ApplicationSet、同步策略与多集群 | 8 | `cicd-iac` Q19 / Q21 / Q22 / Q23；`kubernetes` Q13 | 模块题讲组件、漂移、wave/hook、AppProject；本组补 ApplicationSet generator、多源、Rendered Manifests、资源跟踪迁移、Notifications、Kargo 晋升 |
| 十七、CNI 深入：Cilium 服务网格 / Ingress 与 Calico 架构 | 7 | `network` Q25 / Q26；`kubernetes` Q14 / Q34；`service-mesh` Q24 | 模块题讲 kube-proxy 替代、身份模型、BGP 模式与选型；本组补 Cilium Ingress 数据路径 / 策略执行点 / 源 IP / pathType / host network，以及 Calico 组件分工与 Typha |
| 十八、容器运行时：CRI、containerd 配置、crictl、NRI 与 Security Profiles Operator | 8 | `kubernetes` Q16 / Q22；`cloud-security` Q12；`collections/k8s-local-library.md` 一-10（RuntimeClass） | 模块题讲三大接口是什么与落地；本组补 CRI 调用序列、config.toml 关键项与弃用、多运行时注册、crictl 排障、NRI、版本策略、SPO 录制 / 绑定 / 基线 |
| 十九、etcd 运维：etcdctl v3、快照恢复、压缩碎片整理与升级 | 7 | `kubernetes` Q1 / Q2 / Q40 | 模块题讲原理、HA 与调优；本组全是操作题（只读排查、快照恢复、compaction/defrag、endpoint/member/move-leader、lease/watch/txn、auth、滚动升级），并标注 3.3 → 3.5 的变化 |
| 二十、KubeHound：Kubernetes 攻击图与攻击路径 | 8 | `cloud-security` Q17（RBAC 攻击面/从 Pod 到 cluster-admin 路径）、Q10（HIDS/Falco 运行时检测）；`kubernetes` Q25（RBAC）、Q26（准入控制） | KubeHound 是「把 Q17 的攻击路径评审自动化/图化」的工具，可作 Q17 深追问 |
| 二十一、Kubernetes 攻击技术逐项 | 12 | `cloud-security` Q15（CKS 实操）、Q12（seccomp/AppArmor/SELinux）；`kubernetes` Q27（securityContext/PodSecurity）、Q25（RBAC）；与 `collections/k8s-local-library.md` 一/二组互补 | 逐项攻击机制+检测+防御，比 CKS 清单更深入到 MITRE 与逃逸原理 |
| 二十二、混合云 AI 平台上线前安全评审案例 | 5 | `cloud-security` Q6（合规 PCI/等保对运维的影响）、Q7（KMS/密钥）、Q13（摆脱长期 AK/SK）、Q3（VPC/安全组）；`fde` 案例方法论 | 案例题，适合 senior+/FDE 用 C.A.S.E./WAF 视角驱动 |
| 二十三、零信任与 DevSecOps 趋势（The New Stack） | 7 | `cloud-security` Q5（零信任接入）、Q6（合规）；`cicd-iac` Q7（CI/CD 安全）、Q1（流水线阶段）；`sre-reliability`（组织/文化） | 偏理念与组织，供行为/架构与 cloud-security 概念题补充 |
| 二十四、乔克语雀 K8s 系列：网络、调度、驱逐与发布实践 | 7 | `kubernetes` Q21（证书过期）/ Q5（Pending / ContainerCreating 排查）/ Q7（NotReady）/ Q44（kubelet TLS Bootstrapping）；`cicd-iac` Q19（Argo CD 组件与 sync）/ Q16（Tekton 事件驱动）/ Q18（GitOps 与 CI 推模式结合）；`linux`（内核内存 / slab 相关题） | 语雀 K8s 目录所列的网络 / 调度 / 驱逐 / 发布章节无正文，本组实为该作者「运维问题集合」+「DevOps相关」的追问题 |
| 二十五、乔克语雀 中间件系列：Zookeeper / RocketMQ / Apollo / OpenResty / Nginx 变量 | 7 | `middleware`（Zookeeper / 消息队列 / Nginx 相关题）；`cicd-iac` Q17（配置中心 Nacos / Apollo / Consul）；`cloud-security` Q9（DDoS / CC 防护） | 替代原定「源码与实现」组：etcd 存储 / Event / client-go / apiserver / GC 五章仅有目录 |
| 二十六、中文社区文章：网易云 / InfoQ / 官方博客补充 | 14 | `service-mesh` Q2（控制面 / 数据面）/ Q4（xDS）/ Q5（Sidecar 注入与 iptables）/ Q8（证书轮转与 SDS）；`kubernetes` Q1（容器底层 cgroup）/ Q20（kubelet 驱逐）/ Q39（Event）/ Q40（etcd）/ Q11（Reconcile）；`observability` Q9（K8s 里接入追踪）/ Q19（OTel Collector）；study guide Q1（架构与 etcd）/ Q2（控制面 HA） | Q8–Q14 来自 v1.36 官方文档，可作为「进阶追问」；Comate 页面为 AI 生成，仅取命令 |
| 二十七、家用 / 实验集群运维：备份、恢复与韧性 | 8 | `kubernetes` Q40（etcd）/ Q21 / Q4 / Q43；`sre-reliability`；`kubernetes-study-guide` Q1–Q2 | 备份分层、etcd 静态加密、Velero+GitOps 漂移、聚合 APIService SPOF 是新知识点；探针 / startupProbe 是 Q4 的追问 |
| 二十八、平台组件与交付：GitOps、GitLab 流水线、发布与验证闭环 | 8 | `cicd-iac` Q1 / Q7 / Q13 / Q19 / Q21 / Q24；`kubernetes` Q13 / Q24 / Q26 | 手动晋级坑、Terraform+Helm 所有权、kubectl patch 与 Helm 漂移、验证闭环脚本、镜像拉取三故障是 Q19–Q21 的实操追问 |
| 二十九、可观测性与安全加固实践 | 7 | `observability` Q6 / Q8 / Q9 / Q19 / Q22；`cloud-security` Q7 / Q11 / Q17 | 告警端到端验证、SkyWalking H2 死锁、RBAC 巡检报告与凭据泄漏整改是新场景题；Vault dev 模式坑是 Q7 的追问 |
| 三十、API 现代化与集群升级：废弃 API 清单、Pod 安全标准迁移、资源治理 | 7 | `kubernetes` Q18 / Q19 / Q20 / Q27 / Q32；`cloud-security` Q15；`network` Q24 | 废弃 API 迁移脚本、PSA 分阶段与回滚、ResourceQuota/LimitRange 事故、limits 超卖右调是 Q18/Q19/Q27/Q32 的更深追问 |
| 三十一、云原生可观测性（The New Stack） | 8 | `observability` Q4 / Q18 / Q22；`kubernetes` Q39；`sre-reliability` Q6 / Q24 | 2021 年 TNS 合订本；三支柱之外的统一分析、K8s 四类日志与日志策略、K8s 可观测性三难点；OpenTracing / sidecar 采集已过时 |
| 三十二、云原生 DevOps 指南（The New Stack） | 7 | `cicd-iac` Q7 / Q12 / Q13 / Q18 / Q21；`sre-reliability` Q16 / Q29；`behavior` | 2019 年 TNS 三部曲之三；运维四骑士、GitOps 的 pull/push 之争、CI/CD 攻击面、IaC 安全成熟度、NetDevOps、DORA 与仪表盘、on-call 角色 |
| 三十三、云基础设施效率与可持续性（The New Stack） | 6 | `cloud-security` Q4；`kubernetes` Q37；`gpu-ai` Q18 | 2025 年 Charles Humble 著；能耗比例性、GHG Scope、GreenOps 手段、SCI 公式、需求转移 / 整形；AMD 数字为赞助商口径 |
| 三十四、网络基础补充题（社区题单） | 6 | `network` Q1 / Q14 / Q15 / Q18 / Q25；`kubernetes` Q14 | 社区 66 题里只取模块未覆盖的 ARP / ICMP / 设备分层 / 流控 vs 拥塞 / 子网 / 组播，全部加运维视角改写 |
| 三十五、AWS 上的 AI 基础设施（用户自有文章）+ 网页爬虫系统设计速答 | 7 | `gpu-ai` Q2 / Q5 / Q6 / Q10 / Q12 / Q22 / Q26；`kubernetes` Q45 / Q46；`system-design` Q1–Q4 与 catalog 中的 `web-crawler-system-design` / `crawler` 主题 | 前 4 题为用户自有文章的三缺口 / roofline 选型 / 拓扑 / 存储与成本；后 3 题为 HelloInterview 爬虫题解的需求—礼貌—扩展三段速答 |
| 三十六、Instagram / 新闻流设计速答 | 15 | `system-design`（instagram / fb-news-feed / cdn / newsfeed 主题）；`middleware`（Redis 持久化）；`cloud-security`（预签名 URL 的最小权限） | fan-out 取舍、存储分层、大文件直传、缓存策略 |
| 三十七、Envoy / xDS 与 Sidecar 资源：协议、配置与排障 | 10 | `service-mesh` Q3 / Q4 / Q10 / Q17；`kubernetes` Q10 | 在 Q4（xDS 四变体 / ADS）之上追问 ACK-NACK、SotW 删除语义、warming 与 make-before-break；Sidecar 资源字段级细节补 Q10；clear_route_cache 与 proxy-status 排障补 Q17 |
| 三十八、Istio 维护者博客：ztunnel、ListenerSet、NetworkPolicy API、无 Pod 节点与客户端工程 | 10 | `service-mesh` Q14 / Q18 / Q19 / Q20 / Q24；`kubernetes` Q41 / Q50；`cloud-security`（NetworkPolicy / mTLS 身份） | Gateway API 实现选型基准与 ListenerSet 迁移补 Q18–Q20；NetworkPolicy 身份缺陷与 mTLS 四方案补 Q14 / Q24 与 cloud-security；kube.Client 与 GOMAXPROCS 补 Q41 / Q50；镜像构建加速可归 cicd-iac |
| 三十九、赵化冰博客：Aeraki / MetaProtocol、Envoy Gateway 与 Ambient waypoint、自定义控制器 | 10 | `service-mesh` Q3 / Q13 / Q15 / Q20 / Q21 / Q25；`kubernetes` Q11 / Q41 / Q50；`middleware` Q6 / Q16 / Q17 | HBONE 的 Envoy 实现层追问补 Q15；canonical label 优先级与 L4 Metadata Exchange 补 Q13；MetaProtocol / Aeraki Redis / EG waypoint 补 Q21 与 middleware Q16；List-Watch → Informer → Lease 选主补 kubernetes Q11 / Q41 |
| 四十、服务网格工程实践：流量、安全、多租户与排障（cloudnative.to 博客） | 12 | `service-mesh` Q7 / Q10 / Q12 / Q14 / Q15 / Q17 / Q22 / Q25；`observability` Q4 | ambient 授权 / mTLS 选型 / ztunnel 审计与测试 / Istiod 黄金指标为新追问；2017–2019 Mixer、RouteRule、xDS v1、cert-manager v1alpha1 内容已标「已过时」并给出现行对应物 |
| 四十一、网络与网关：Cilium BGP / Egress / Envoy Gateway / PROXY protocol / 源 IP / 限流 | 10 | `network` Q23 / Q25 / Q26 / Q27；`service-mesh` Q18 / Q20；`gpu-ai` Q11 / Q26 | PROXY 协议格式与安全约束、Cilium BGP 观测细节、ambient egress、Envoy Gateway 1.3 / Cilium 1.17、多副本限流、推理扩展端点选择规则；AWS NLB 一题标注 2020 做法已可被 ProxyConfig 取代 |
| 四十二、平台工程杂谈：KEDA vs HPA、裸金属 vs VM、kro、调度器模拟器、OpenTelemetry、OpenAPI→MCP | 8 | `kubernetes` Q6 / Q42；`observability` Q4 / Q19；`cicd-iac` Q18；`ai-engineering`（MCP / 提示注入 / 多智能体题） | 偏判断与取舍：KEDA 适用边界、裸机实验的控制变量、kro 是否可用于生产、调度器白盒化、OpenAPI 语义与工具投毒、Agent 置信度分流、构件 vs 代码 |
| 四十三、GPU 多租户平台：隔离层级、编排、监控与虚拟集群 | 10 | `gpu-ai` Q2 / Q3 / Q10 / Q17 / Q18 / Q21 / Q25；`kubernetes` Q45 / Q46 | 书稿六章：在 Q2（MIG/MPS/时间分片）与 Q21（HAMi）之上补「编排 vs 强制执行」判断、僵尸显存、囤积量化与 vCluster + KAI 平台题 |
| 四十四、GPU 效能与 HAMi 调度实践 | 8 | `gpu-ai` Q7 / Q18 / Q19 / Q21 / Q22；`ai-engineering` Q13–Q16（Agent 可靠性）；`sre-reliability`（检查点 / RTO-RPO） | Productive GPU-Hours、五层栈归属、mutex 语义与 kind 复现、异构控制面、Slinky、Agent 可靠性 |
| 四十五、AI Infra 系列：性能工程、NCCL / NIXL、存储层、训练调度 | 8 | `gpu-ai` Q5 / Q6 / Q7 / Q17 / Q19 / Q20 / Q25；`linux` Q10（NUMA）；`kubernetes` Q46（Topology Manager） | goodput / MFU、DDP 重叠与 NCCL 排障、NIXL、存储与 DataLoader、单机四旋钮、万卡调度容错、性能体检与 Roofline |
| 四十六、LLM 推理引擎：连续批处理、PagedAttention、KV Cache 管理、PD 分离部署 | 8 | `gpu-ai` Q9 / Q11 / Q12 / Q13 / Q23 / Q24 / Q26；`system-design`（LLM serving / KV cache 主题） | 在 Q23 / Q24 之上补批处理压测量级、MoE 并行、引擎选型与显存日志、投机 + 量化顺序、vLLM PD 源码、K8s PD 部署（LWS / Grove / KAI）、KV 卸载复用与跨 DC、CUDA Graph / compile 缓存 |
| 四十七、高可用与分布式架构：链路追踪、数据库选型、发号器、限流熔断 | 10 | `sre-reliability` Q3 / Q4 / Q5 / Q8 / Q9 / Q13；`observability` Q4 / Q9 / Q22；`middleware` Q8 / Q9；`system-design` Q3 / Q5（`rate-limiter`、`distributed-search` 目录）；`cicd-iac` Q24 | 补服务分级与故障分的量化、号段发号器、Share-Nothing / Share-Disk / 中间件三路线、Sentinel 生产落地与 K8s 阈值算法、Maven CI 构建；Sleuth 已过时标注 |
| 四十八、运维事故复盘：K3s 重启后 Service 全挂 与 SRE 复盘方法 | 6 | `kubernetes` Q5 / Q8；`network` Q16 / Q17；`observability` Q11；`sre-reliability` Q1 / Q7 / Q16 | 真实事故：kube-proxy ensureChainJumps、KEP-3453 版本差异、K3s 与 iptables 后端差异、黑盒探针与正确的 kube-proxy 指标、「根因未定性」的复盘写法；可作 Senior+ 排障 case |
| 四十九、Elasticsearch 实战：Mapping、查询、聚合、分页与写入性能（Spring ES 实战） | 9 | `middleware` Q11 / Q12；`gpu-ai` Q14；`system-design` `distributed-search`；`observability` Q18 | 补 8.x 安全默认值验证链、Text/Keyword 与 analyzer 重建、bool 四子句、function_score、terms 近似与 shard_size、from/size vs search_after/PIT/Scroll、Bulk 与 circuit breaker；作者数字仅作量级参考 |
| 五十、Spring Boot 应用的生产化：配置 / Profile / 日志证据链 / Actuator / 容器构建 / 上线清单（SpringBoot4 进阶实战） | 9 | `cicd-iac` Q3 / Q9 / Q11 / Q17 / Q24；`kubernetes` Q4；`observability` Q4 / Q22；`sre-reliability` Q1 / Q12 / Q16；`cloud-security` Q6 | 面向运维的应用侧契约：配置优先级与 Secret、Profile 治理、MDC / 结构化日志、liveness ≠ readiness 与 Actuator 授权、Observation 证据链、分层镜像、发布 / 优雅停机 / 恢复顺序、Flyway、启动链与默认值陷阱；2742257（PostGIS）与 2719328（本仓库自述）未出题 |
| 五十一、Agent 工程：Harness、Plan 模式、主子 Agent、四层记忆、Skills / Toolchain | 10 | `ai-engineering` Q1 / Q3 / Q8 / Q9 / Q10 / Q11 / Q17 / Q19 / Q20 / Q21；`fde` Q15 / Q18 | Q1（agent 循环）与 Q3（上下文）的机制级深挖：三层分离、压缩阈值与 Session JSONL；Q8「记忆是建议、钩子是保证」补插件权限隔离；Q10 / Q19 补主子 Agent 与 A2A（与 `fde` Q15 的 ADK 版本互补）；Q20 补四层记忆的 Redis / MySQL 与 Token Budget 实现 |
| 五十二、FDE 落地：RAG / Agent / MCP / Skill 选型、多智能体交付流水线、金融审计 | 7 | `fde` Q1 / Q2 / Q3 / Q14 / Q15 / Q16 / Q18 / Q26 / Q27 / Q30；`ai-engineering` Q9 / Q13 / Q16 / Q24 / Q25；`cloud-security` Q6 | 补 `fde` 没有的：Lean / Cynefin 复杂度判断、七层责任与「名词驱动架构」反模式、交付流水线的互卡 Gate、金融审计链与灰度四级（与 `cloud-security` Q6 的合规要求衔接）、知识图谱与 GraphRAG 选型 |
| 五十三、Agent 安全与事故：人类在环授权、Replit 删库、Skyscanner 两字符事故、agentgateway、Azure SRE Agent | 9 | `ai-engineering` Q4 / Q13 / Q15 / Q16 / Q18 / Q20 / Q22；`cloud-security` Q2 / Q5 / Q6 / Q13 / Q14；`fde` Q18 / Q30 | Q13（agent 进运维链路的护栏）的协议级与事故级支撑：HitL 五条判据、CHEQ / TAC / AAuth、MRTR vs Tasks 可直接作为 Q13 / Q16 的 🔴 追问；Replit 与 Skyscanner 两起事故适合做 `cloud-security` Q2 / Q6 的情景题；agentgateway 的 CEL 字段可见性是 `ai-engineering` Q16（MCP 网关）的实现级追问 |
| 五十四、MCP 生态：awesome-mcp-servers 的分类法、运维团队选型与供应链风险 | 8 | `ai-engineering` Q9 / Q16 / Q21 / Q22；`cloud-security` Q14；`fde` Q20 / Q21 | Q9「为什么要少接服务器」在这里有了量化解释（上下文税与工具选择错误）；Q16 扩展成注册中心 + 网关 + 隔离区的治理平面；Q22（提示注入）补「工具描述即指令」与 rug pull；`cloud-security` Q14 的 SBOM / 签名思路正好用于 MCP server 的安装方式与版本锁定 |
| 五十五、HelloInterview 系统设计拆解速答：Bitly / Dropbox / News Feed / GoPuff / Instagram / LeetCode / Ticketmaster / Tinder / Yelp | 18 | `system-design`（url-shortener / dropbox / fb-news-feed / instagram / leetcode / ticketmaster / tinder / yelp 主题，Q1–Q4 方法论）；`middleware` Q1 / Q13（队列 vs 缓存 vs 数据库）；`cloud-security` Q13（签名 URL 最小权限） | 短码生成与计数器、分块 / 断点续传 / CDC、DynamoDB 热分区与 GSI、判题同步 vs 异步、座位一致性、互滑竞争、分级评估标准 |
| 五十六、用户自制题库精选：Argo CD / DevSecOps / 文件存储 / Go for DevOps / Kafka / KEDA / MLOps / MongoDB / 网络 | 9 | `cicd-iac` Q7 / Q19 / Q22（Argo CD、供应链）；`cloud-security` Q7 / Q14（Vault、SBOM）；`middleware` Q1–Q3 / Q19（Kafka、MongoDB）；`gpu-ai` Q15 / Q26（MLOps、推理扩缩）；`kubernetes` Q6（HPA）；`network` Q7 / Q10 / Q16（DNS、CoreDNS、iptables）；`ai-engineering`（GitOps 下的模型发布） | 每份题库取一题合并为追问链：永远 OutOfSync 三根因、OIDC→Vault 动态凭据、两次写脑裂、GOMAXPROCS、rebalance 风暴、KEDA↔HPA 分工、storageUri 不变 bug、分片键与 ESR、ndots / TTL / apex CNAME |
| 五十七、用户自制 K8s 学习指南与运维手册：生产清单、事故 runbook、控制面内幕 | 6 | `kubernetes` Q4 / Q5 / Q11 / Q18 / Q30 / Q32（探针、排障、Operator、QoS、发布、升级）；`cloud-security` Q11 / Q15（加固清单、CKS）；`cicd-iac` Q3（蓝绿回滚）；`sre-reliability`（runbook 与事故分级） | 生产 Deployment 字段清单、CFS 节流数学、三阶段排障、发布事故 runbook、Operator 成熟度五级、apiserver / kubelet 加固（含已过时参数标注） |
| 五十八、补充：多架构 EKS、the-hard-way、vcluster、Anthos、Terway、iptables、SPIFFE、KIAMOL | 7 | `kubernetes` Q14 / Q16 / Q33 / Q35（CNI、CRI/CNI/CSI、多集群、多租户）；`network` Q16 / Q17 / Q25（iptables、conntrack、Calico）；`cloud-security` Q13（IRSA / SPIFFE）；`service-mesh` Q8（SPIFFE 身份）；`cicd-iac` Q2（多架构构建流水线）；`gpu-ai` Q18（GPU 多租户平台） | 多架构镜像 manifest、KTHW 与 kubeadm 对比、vcluster 四种架构、Anthos Fleet / Connect、Terway 三种模式与降级、节点 iptables / sysctl 与 ClusterIP 不可 ping、SPIFFE 用于 kubectl 认证与 Slurm 作业身份 |
| 五十九、HummerRisk：云原生安全平台的能力、架构与落地 | 8 | `cloud-security` Q15（CKS 实操清单）/ Q16（1.24 官方安全审计）；`kubernetes` 镜像扫描 / kube-bench 相关题；`cicd-iac` SBOM 与供应链题 | 开源 CSPM / KSPM 平台选型题，与第一批 KubeHound 攻击图题互为对照；注意项目 2023-10 后无 release |
| 六十、Kubernetes 安全检查清单：逐项控制的目的、验证与副作用 | 8 | `cloud-security` Q15 / Q16；`kubernetes` RBAC / NetworkPolicy / 审计 / PSA 题的追问层 | 只覆盖清单中知识库未有的条目：匿名认证、impersonation、人机身份、组件间 TLS、unsafe sysctl、capabilities、镜像构建与签名、网络 / OS 分区 |
| 六十一、网易云技术博客：容器、微服务与云平台实践 | 11 | `service-mesh` Q25（异构系统迁入网格）及 Istio 推送 / 限流题；`kubernetes` Q51（超大规模控制面）/ Q52（DRBD / LINSTOR 存储）；`observability` 日志采集题；`sre-reliability` 混部 / 容量题；`cicd-iac` Helm 题 | Slime、IstioCon 2022、Curve、KubeCube、Loggie、SparkSQL on K8s、KubeDiag / Kubeminer、Helm 私有化交付 |
| 六十二、杂项：iptables 运维、Proxygen、ACM Queue、Wireshark 等 | 6 | `linux` iptables 题；`network` 抓包 / Wireshark 题；`kubernetes` 架构 / 设计哲学题（Borg / Omega）；`cloud-security` etcd 静态加密题；`cicd-iac` GitOps 题 | 6 题；DigitalOcean iptables 页正文为空、freeCodeCamp 手册与 Twistlock 文章未出题 |
| 六十三、rbac-police：RBAC 权限提升策略扫描 | 8 | `cloud-security`（RBAC 提权/最小权限）；与 `kubernetes` RBAC 题、batch1 KubeHound 组互补 | 静态 RBAC 分析工具，补 KubeHound 攻击图之外的「谁有危险权限」 |
| 六十四、云原生安全知识图谱：威胁矩阵、标准与基准 | 8 | `cloud-security`（威胁建模/合规基准）；`service-mesh`（NIST 800-204B） | 判断题为主：怎么选标准/工具、事件复盘教训 |
| 六十五、经典漏洞与逃逸案例：Kubernetes CVE 家族、runc/containerd 逃逸、事件复盘 | 12 | `cloud-security`（CVE/容器逃逸）；`kubernetes`（控制面/组件补丁） | 只讲原理/防御/检测，不含利用载荷；多数 CVE 已修复 |
| 六十六、攻防靶场与补充攻击路径：Metarget、KubeHound 其余边 | 6 | `cloud-security`（靶场/攻击边）；与 batch1 KubeHound 组互补 | Metarget 靶场用法 + 4 条 batch1 未覆盖的 KubeHound 边 |
| 六十七、RAG 基础：为什么 RAG、调用 LLM、embeddings 的含义与度量 | 8 | `ai-engineering` Q23 / Q24；`gpu-ai` Q12 | LLM 基础与 RAG-vs-微调的前置概念，本组把「为什么 RAG」讲到代码层 |
| 六十八、RAG 检索层：分块策略、向量检索、top-k 与相似度 | 8 | `gpu-ai` Q14；`system-design` Q31；`middleware` Q20 | 向量库运维与切分 / 相似度细节；MongoDB `$vectorSearch` 那组（collections/mongodb-zero-to-hero 六）不再重复 |
| 六十九、RAG 流水线与 LangChain：端到端代码、评估、上线与运维 | 10 | `ai-engineering` Q21 / Q25 / Q27；`system-design` Q31；`cloud-security` Q7 | prompt 规则、评测体系、密钥管理与服务化上线；Q27 同为代码阅读案例 |
| 七十、秒杀与票务：库存预留、等待室与限流速答 | 15 | `system-design`（ticketmaster / rate-limiter / distributed-message-queue 主题）；`middleware`（数据库锁与事务、Redis 分片）；`sre-reliability`（限流、退避与惊群、容量与余量） | 事务边界与幂等、`SKIP LOCKED` 破热点行、等待室公平与签名准入、延时回收的重复投递 |
| 七十一、推理网关深水区：前缀缓存感知路由、调度器框架与流量控制 | 11 | `gpu-ai` Q?（新增「推理网关调度与流控」题）；追问 batch1 Q95 / Q97 / Q98；`service-mesh` 的 Gateway API 扩展点 | 本组是 batch1「EPP 怎么挑 Pod」的提案级深挖，面试时先问 batch1 再用本组追问 |
| 七十二、InferencePool 运维：滚动发布、多池服务、独立部署、GA 迁移与排障 | 10 | `kubernetes` / `cicd-iac` 的灰度发布题；追问 batch1 Q100（零停机升级）、Q101（错误码）、Q103（多集群） | 排障与迁移题适合做实操环节；Helm values 题可当速答 |
| 七十三、模型服务与推理观测：Model Server Protocol、延迟预测、饱和检测、OTel 追踪、vLLM 应用示例 | 9 | `observability` Q?（LLM 观测指标）；`gpu-ai` Q60（vLLM 部署参数）、batch1 Q96（模型服务器协议）、Q102（指标与 KEDA） | 与 `observability` 模块的黄金信号题成对使用：这里是「推理专属信号」 |
| 七十四、LLM 服务与网关工具选型：in-cluster 推理 operator 与 AI Gateway | 8 | `gpu-ai` Q9 / Q11 / Q12 / Q26；`cloud-security` （agent 沙箱隔离，可作新题）；第一批草稿 04-ai-gateway-gpu 的 Inference Gateway 系列 | 模块题讲引擎与网关内部机制，本组讲「项目这么多该选谁、怎么评估成熟度」，作为选型追问 |
| 七十五、LLM 可观测与评估：OpenLLMetry / Langfuse / Braintrust / 评估指南 / LLMOps | 8 | `observability` Q4 / Q19 / Q22；`ai-engineering` Q23 / Q25；`gpu-ai` Q15 | 第 1、5、7 题可直接升格为 `observability` 新模块题（LLM trace 语义、token 成本归因、答案退化排查） |
| 七十六、MCP 协议与 SDK：tools / resources / prompts、sampling、传输与安全评审 | 7 | `ai-engineering` Q9（MCP 是什么）/ Q16（MCP 网关）/ Q22（提示注入与供应链） | 模块题优先；本组补协议面（MRTR、废弃项、缓存语义）与实现面（schema 推断、会话、工具过滤），第 3、7 题适合做 🔴 追问 |
| 七十七、AI 辅助运维与 Agent 工程实践 | 7 | `ai-engineering` Q13 / Q15 / Q18 / Q26；`sre-reliability`（混沌工程题）；`cicd-iac`（GitOps 兜底） | 第 3 题可作混沌工程模块的 🔴 扩展；第 7 题带年份与赞助方限定，只做「怎么读厂商资料」的判断题 |
| 七十八、HelloInterview 分布式缓存拆解：需求与规模、TTL / LRU、高可用、分片与一致性哈希、热 key、性能 | 12 | `system-design`（distributed-cache / lru-cache / key-value-store 主题，Q1–Q4 方法论）；`middleware`（Redis 淘汰、持久化、Cluster 与 Sentinel）；`sre-reliability`（容量规划、限流熔断与回源保护） | 先用第 686–687 题做需求与估算，再按六个深挖逐个追问；第 696 题是 SRE 视角的加分题，第 697 题可作收尾的分级判断 |
<!-- /k8s-web-archive-mapping -->

<!-- veeramalla-devops-interview-guide-mapping -->
### Veeramalla 公司真题 → modules 映射

| 题目主题 | 对应 modules 模块 |
|---|---|
| Kubernetes / Docker | `kubernetes` |
| Terraform / Ansible / Jenkins / GitHub Actions / Azure DevOps | `cicd-iac` |
| AWS / Azure / GCP | `cloud-security` |
| Linux / Shell / Python 脚本 | `linux` |
| 网络（子网 / NAT / DNS / LB / TLS） | `network` |
| Prometheus / Grafana / ELK / EFK | `observability` |
| SLI / SLO / 事故 / 值班 | `sre-reliability` |
| 数据库 / Redis / Kafka | `middleware` |
| 项目经历 / 行为面 | `behavior` |
| 三层架构 / 高可用 / 迁移方案 | `system-design` |
<!-- /veeramalla-devops-interview-guide-mapping -->

### Awesome Claude Code 生态 → modules 映射

| 题目分组 | 题号 | 对应 modules 模块 |
|---|---|---|
| 生态总览与选型 / 官方心智模型 / 扩展机制选型 | 1–72 | `ai-engineering` |
| Slash Commands / Hooks / Agent Skills | 73–138 | `ai-engineering`（+ 安全类归 `cloud-security`）|
| 记忆与上下文持久化 | 139–156 | `ai-engineering` |
| 多 Agent 编排 / Ralph Wiggum 循环 | 157–190 | `ai-engineering` + `system-design` + `sre-reliability` |
| 会话可观测性 / 用量成本 / Status Lines | 191–242 | `observability`（成本与容量部分配 `sre-reliability`）|
| 安全、沙箱与供应链 | 243–270 | `cloud-security` |
| Provider 与运行时集成 / 替代客户端与远程控制 | 271–304 | `ai-engineering` + `cloud-security` + `network` |
| 配置 lint 与规则治理 | 305–318 | `cicd-iac` |
| IaC / K8s / OTel 专项技能 | 319–334 | `cicd-iac` + `kubernetes` + `observability` |
| 测试、质量门与代码审查 | 335–350 | `cicd-iac` + `sre-reliability` |
| 文档知识与学习 / 设计写作创意 | 351–376 | `behavior` + `fde` |
| 开放判断题（🔴） | 377–392 | `behavior` + `sre-reliability` |
<!-- /awesome-claude-code-mapping -->

<!-- aws-managed-services-only-mapping -->
### AWS 托管服务改造 → modules 映射

| 题目分组 | 题号 | 对应 modules 模块 |
|---|---|---|
| 一、「只用托管服务」这条约束 | 1–10 | `cloud-security` + `system-design` + `sre-reliability` |
| 二、目标架构与选型表（26 服务） | 11–24 | `system-design` + `cloud-security` + `network` |
| 三、身份与密钥（IRSA / Secrets Manager） | 25–34 | `cloud-security` + `kubernetes` |
| 四、可观测性（CloudWatch vs AMP vs 自建） | 35–50 | `observability` + `sre-reliability` |
| 五、备份与恢复（AWS Backup 与 K8s 对象缺口） | 51–63 | `sre-reliability` + `kubernetes` + `cloud-security` |
| 六、GPU on EKS 托管边界 | 64–76 | `gpu-ai` + `kubernetes` |
| 七、东西向流量与网关（VPC Lattice vs 网格） | 77–87 | `service-mesh` + `network` |
| 八、交付链（CodePipeline / EKS 托管 Argo CD） | 88–98 | `cicd-iac` |
| 九、数据、流与 AI 存储 | 99–112 | `middleware` + `gpu-ai` + `system-design` |
| 十、Agent / MCP 在 AWS 上的缺口 | 113–120 | `ai-engineering` + `cloud-security` |
| 十一、未验证架构的文档与验证方法论 | 121–130 | `behavior` + `fde` + `sre-reliability` |
| 十二、经典系统设计的 AWS-only 渲染（一）：短链 / IM / 票务 | 131–157 | `system-design` + `middleware` + `network` |
| 十三、经典系统设计的 AWS-only 渲染（二）：调度 / 通知 / 爬虫 / 信息流 / 直播 / 存储 / 缓存 / 分析 | 158–195 | `system-design` + `middleware` + `sre-reliability` + `observability` |
<!-- /aws-managed-services-only-mapping -->
