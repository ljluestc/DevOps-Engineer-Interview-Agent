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

> **合计**：collections 共收录 **2248 题**（1502 + 231 + 89 + 88 + 68 + 159 + 111，去重前）。

## 版权与使用口径（重要）

- 本目录**仅收录题目列表**（公开网页上可直接阅读的问题文本），**不收录**原作者的参考答案、个人心得与付费内容。
- 每题保留原文措辞与 ☆ 高频标记；分组沿用原文。
- 如需商用或对题目做二次加工分发，请自行评估原作者版权声明；本项目以「学习与参考」为目的收录，并明确标注出处。
- 收录日期：2026-08-05（崔亮系列）、2026-08-19（1502 题合集）、2026-09-20（MongoDB Zero-to-Hero、K8s 本地资料库、经典论文）。
- `mongodb-zero-to-hero.md` 是例外：原仓库是 Apache-2.0 教程而非题库，题目与要点由本项目从教程改写提炼，可自由使用，保留出处即可。
- `k8s-local-library.md` 同为提炼件：来源是本机 15 份 PDF（商业电子书 / 公开审计报告 / 演讲 PPT / 社区笔记），题目与要点由本项目改写，不含逐字摘录；两份商业资料（CKS Book、全速云课件）只提炼主题与开源部分。文件头有逐份的版权口径表。
- `classic-papers.md` 同为提炼件：来源全部是公开论文 / 白皮书（版权归作者与出版方），题目与要点由本项目改写；书架索引里的教材**不出题**。

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
