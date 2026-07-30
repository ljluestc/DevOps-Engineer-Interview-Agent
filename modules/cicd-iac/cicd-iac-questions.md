# CI/CD & IaC 面试题（18 题）

> 模板见 [../../docs/STANDARD.md](../../docs/STANDARD.md)。Ansible 基础见 [../../basics/05-ansible-basics.md](../../basics/05-ansible-basics.md)；Docker 见 [../../basics/03-docker-basics.md](../../basics/03-docker-basics.md)。

---

### Q1. 设计从代码提交到生产的 CI/CD 流水线，包含哪些阶段？
- **难度**：🟡 中级
- **关键词**：CI/CD, 流水线, 门禁, 回滚
- **概念速记**：CI 持续集成（构建/测试），CD 持续交付/部署。
- **参考答案**：代码扫描→单测→构建（缓存/分层）→制品入库（版本签名）→测试环境部署→自动化测试→安全扫描（镜像漏洞/DAST）→灰度（金丝雀/蓝绿）→生产。关键：不可变制品、环境一致、快速失败、审批门禁、回滚预案。
- **易错点**：把「部署到生产」等同于「发布给用户」（应解耦，见 Feature Flag）。
- **延伸**：kubernetes Q30；Q3（蓝绿/金丝雀）

### Q2. Jenkins / GitLab CI / GitHub Actions / Argo Workflows 适用场景？
- **难度**：🟡 中级
- **关键词**：Jenkins, GitLab CI, Argo Workflows, 选型
- **概念速记**：各有侧重：自托管重、云托管轻、K8s 原生 DAG。
- **参考答案**：Jenkins（老牌、插件多、自托管）；GitLab CI（一体、YAML）；GitHub Actions（生态、托管）；Argo Workflows（K8s 原生、复杂 DAG、数据/ML 流水线）。看代码托管、规模、是否 K8s 原生。
- **易错点**：小团队硬上 Jenkins 维护成本高。
- **延伸**：Q1

### Q3. 蓝绿发布与金丝雀发布的取舍？如何自动化回滚？
- **难度**：🔴 高级
- **关键词**：蓝绿, 金丝雀, 自动化回滚, 错误预算
- **概念速记**：蓝绿切换快但资源翻倍；金丝雀风险小但流程长。
- **参考答案**：蓝绿：两套环境切流量，秒级回滚，资源翻倍。金丝雀：小比例放量+指标分析逐步推进，用户影响可控。自动化回滚：基于 SLO/错误率/延迟阈值（Argo Rollouts/Flagger）自动 abort + 回退上一稳定版本。
- **易错点**：金丝雀放量不看业务指标只看部署状态。
- **延伸**：kubernetes Q30；observability Q（SLO）

### Q4. Feature Flag 在发布中的作用？
- **难度**：🟡 中级
- **关键词**：Feature Flag, 部署发布解耦, 灰度
- **概念速记**：解耦「部署」与「发布」，代码上线但功能默认关。
- **参考答案**：按用户/比例开启，可秒级关；用于灰度、A/B、紧急止血（不回滚代码）。关注：开关残留清理、配置中心一致性、与灰度配合。
- **易错点**：开关长期不清理导致代码腐化。
- **延伸**：Q1、Q3

### Q5. Git 工作流（GitFlow / Trunk Based / GitHub Flow）怎么选？
- **难度**：🟡 中级
- **关键词**：GitFlow, Trunk Based, 分支策略
- **概念速记**：Trunk Based 单一主干+短分支，CI 友好。
- **参考答案**：GitFlow（develop/main + feature/release/hotfix，重，适合有版本发布）；Trunk Based（单一主干+短分支，适合持续交付）；GitHub Flow（main+PR，简单）。高级团队多推崇 Trunk Based + 特性开关。
- **易错点**：小团队用 GitFlow 分支管理成本过高。
- **延伸**：Q8（不可变基础设施）

### Q6. 制品仓库（Harbor / Nexus / Artifactory）管什么？
- **难度**：🟢 初级
- **关键词**：制品仓库, 镜像, 版本, 漏洞扫描
- **概念速记**：统一存储镜像/包/通用制品，是 CI/CD 与合规基础。
- **参考答案**：存 Docker 镜像、Helm chart、Maven/npm/PyPI 包。功能：版本、代理上游、权限、漏洞扫描、复制、清理策略。
- **易错点**：制品不入仓库，直接构建即部署，难回滚/溯源。
- **延伸**：kubernetes Q24

### Q7. 如何保证 CI/CD 的安全（依赖、密钥、供应链）？
- **难度**：🔴 高级
- **关键词**：供应链安全, SCA, cosign, SLSA
- **概念速记**：CI/CD 是攻击面，需全链路防护。
- **参考答案**：依赖扫描（SCA，Trivy/Dependabot）、密钥不入仓库（Vault 注入）、镜像签名验证（cosign/Notary）、SBOM 生成、流水线最小权限、制品可追溯、SLSA 等级、防篡改审计。
- **易错点**：把密钥写进仓库环境变量。
- **延伸**：cloud-security Q（密钥管理）；kubernetes Q24

### Q8. 不可变基础设施（Immutable Infrastructure）理念？
- **难度**：🔴 高级
- **关键词**：不可变基础设施, 镜像, 滚动替换
- **概念速记**：服务器/镜像一旦构建不再改，变更靠重建替换。
- **参考答案**：优点：环境一致、回滚简单、防漂移、易审计。实现：Packer 构建镜像 + TF/K8s 编排 + 滚动替换。对比传统「登录改配置」易腐化。
- **易错点**：镜像频繁手改后变成「雪花服务器」。
- **延伸**：Q5、kubernetes Q29

### Q9. 如何在流水线里做数据库变更（schema migration）安全发布？
- **难度**：🔴 高级
- **关键词**：数据库迁移, 在线DDL, 向前兼容
- **概念速记**：DB 变更要前向兼容，避免锁表。
- **参考答案**：用迁移工具（Flyway/Liquibase/Atlas）；前向兼容（先加列后删列、online DDL/gh-ost）；小步可回滚；与代码解耦（先 DB 后代码或双向兼容）；评审+备份+灰度验证。
- **易错点**：大事务锁表拖垮线上。
- **延伸**：middleware Q（MySQL 慢查询）

### Q10. 流水线如何做到「快速失败」与合理缓存？
- **难度**：🟡 中级
- **关键词**：快速失败, 缓存, 并行
- **概念速记**：尽早跑快而广的检查，缓存复用依赖。
- **参考答案**：尽早跑 lint→单测→构建；缓存依赖（Maven/npm、Docker layer、BuildKit）；并行阶段；失败立即中止精准通知。权衡缓存命中率 vs 重建成本。
- **易错点**：缓存未加 key 导致用到旧依赖。
- **延伸**：Q1

### Q11. 多环境（dev/test/staging/prod）如何用一套配置管理？
- **难度**：🟡 中级
- **关键词**：环境配置, overlay, 配置中心
- **概念速记**：环境差异外置，基础一致、差异最小。
- **参考答案**：Kustomize overlay 或 Helm values 分环境；配置中心按环境/集群下发；机密分环境隔离。目标「一次构建，多处部署」。
- **易错点**：各环境各自维护导致漂移。
- **延伸**：kubernetes Q31；Q4

### Q12. 如何做流水线的可观测与审计？
- **难度**：🟡 中级
- **关键词**：可观测, 审计, 制品元数据
- **概念速记**：每次构建可追溯到「谁/何时/改了什么」。
- **参考答案**：每步耗时/结果/产物记录（git sha、镜像 digest）；可追溯；与监控/日志打通；审计日志防篡改；失败根因聚合。满足合规与复盘。
- **易错点**：只记成功失败不记产物 digest，无法精确回滚。
- **延伸**：observability Q；cloud-security Q（审计）

### Q13. 持续部署（CD）与持续交付（Continuous Delivery）区别？
- **难度**：🟡 中级
- **关键词**：CD, 持续交付, 持续部署, 自动发布
- **概念速记**：交付=可发布（人工按键）；部署=自动上生产。
- **参考答案**：持续交付到「可发布」状态需人工；持续部署通过门禁后自动上生产。CD 提速但要求强测试/监控/回滚，金融等强合规常保留人工审批。
- **易错点**：以为上了 Jenkins 就是持续部署。
- **延伸**：Q1、Q3

### Q14. Ansible 与 Terraform 区别？解决什么问题？
- **难度**：🟡 中级
- **关键词**：Ansible, Terraform, IaC, 幂等
- **概念速记**：TF 管基础设施（建资源）；Ansible 管已有机器配置。
- **参考答案**：Terraform=IaC，声明式，有 state，面向创建/变更/销毁；Ansible=配置管理，无 agent（SSH），幂等。常配合：TF 建资源，Ansible 初始化。Ansible 幂等靠模块自身。
- **易错点**：用 Ansible 批量 `shell echo >>` 以为幂等（实际不幂等）。
- **延伸**：[basics/05-ansible-basics.md](../../basics/05-ansible-basics.md)

### Q15. Terraform 的 state / plan / module / workspace 是什么？
- **难度**：🔴 高级
- **关键词**：Terraform, state, plan, 远程锁
- **概念速记**：state 记录真实资源映射，需远程锁防并发。
- **参考答案**：state 映射（远程锁如 S3+DynamoDB）；plan 预览变更；module 复用；workspace 隔离环境（慎用，多用目录）。陷阱：state 损坏/泄露（含密钥）、大 state 慢、provider 升级破坏性需 review plan。
- **易错点**：state 文件提交 Git 泄露密钥。
- **延伸**：Q14

### Q16. 如何用 Argo Events / Tekton 构建事件驱动流水线？
- **难度**：🔴 高级
- **关键词**：Argo Events, Tekton, 事件驱动, DAG
- **概念速记**：Tekton 提供 K8s 原生 Pipeline CRD；Argo Events 触发。
- **参考答案**：Tekton Pipeline/Task CRD；Argo Events 把 Git push/Webhook/定时触发 Workflow。关注触发器安全（签名校验）、资源配额、失败重试。
- **易错点**：触发器无签名校验被伪造事件触发。
- **延伸**：Q2、kubernetes Q13

### Q17. 配置中心（Nacos / Apollo / Consul）与配置管理怎么结合？
- **难度**：🟡 中级
- **关键词**：配置中心, 动态配置, 灰度推送
- **概念速记**：配置中心管动态配置（热更新），与静态基建配置互补。
- **参考答案**：动态配置热更新/灰度/回滚；与 Ansible/TF 管理的静态配置互补。关注：配置漂移、推送失败、错误引发故障（需校验+灰度+回滚）、权限安全。
- **易错点**：配置错误直接全量推送无灰度。
- **延伸**：cloud-security Q；sre Q（配置故障）

### Q18. GitOps 与「传统 CI 推模式」在 IaC 上的结合？
- **难度**：⚫ 资深
- **关键词**：GitOps, IaC, 拉模型, 多集群
- **概念速记**：基础设施即代码 + Git 为事实源 + 持续 reconcile。
- **参考答案**：Terraform/Argo CD 结合：TF 产出计划存 Git，Argo CD 同步到集群；多集群一致、可审计、防漂移。关注 secret 管理（ sealed-secret / external）、敏感 state 加密。
- **易错点**：GitOps 仓库明文存密钥。
- **延伸**：kubernetes Q13；Q15
