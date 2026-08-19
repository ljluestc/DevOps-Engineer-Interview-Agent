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

> **合计**：collections 共收录 **1910 题**（1502 + 231 + 89 + 88，去重前）。

## 版权与使用口径（重要）

- 本目录**仅收录题目列表**（公开网页上可直接阅读的问题文本），**不收录**原作者的参考答案、个人心得与付费内容。
- 每题保留原文措辞与 ☆ 高频标记；分组沿用原文。
- 如需商用或对题目做二次加工分发，请自行评估原作者版权声明；本项目以「学习与参考」为目的收录，并明确标注出处。
- 收录日期：2026-08-05（崔亮系列）、2026-08-19（1502 题合集）。

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
