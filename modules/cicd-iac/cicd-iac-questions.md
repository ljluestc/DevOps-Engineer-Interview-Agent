# CI/CD & IaC 面试题（25 题）

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

### Q19. Argo CD 的核心组件有哪些？一次 sync 到底发生了什么？
- **难度**：🔴 高级
- **关键词**：argocd-server, application-controller, repo-server, OutOfSync, 健康状态
- **概念速记**：Argo CD 是运行在 K8s 上的微服务架构，三个核心组件分工明确——**repo-server**（拉 Git、渲染 Helm/Kustomize 产出最终 manifest）、**application-controller**（对比实际状态与期望状态并执行同步）、**argocd-server**（API/UI/CLI 入口 + RBAC + SSO）；另有 Redis 做缓存、Dex 做 SSO。
- **参考答案**：
  1. **一次 sync 的链路**：controller 触发 → repo-server 拉取指定 revision 并**渲染模板**（`helm template` / `kustomize build`）→ 得到期望 manifest → 与集群实际对象做 **diff** → 状态标为 `Synced`/`OutOfSync` → 执行 apply（按 sync wave 排序）→ 用**健康检查**（内置 + 自定义 Lua）判定 `Healthy`/`Progressing`/`Degraded`。
  2. **两个状态维度别混**：`Sync Status` 回答「集群里的 YAML 和 Git 一样吗」；`Health Status` 回答「这些对象跑起来了吗」。**Synced ≠ 可用**——apply 成功但 Pod CrashLoopBackOff，就是 `Synced + Degraded`。
  3. **常见 OutOfSync 假阳性**：其他控制器/webhook 回写了字段（如 HPA 改 replicas、istio 注入的 sidecar、云 LB 回填的 annotation）。解法是 `ignoreDifferences`（按 jsonPointers/jqPathExpressions 忽略）或在 Deployment 里干脆不写 replicas。
  4. **性能关注点**：repo-server 的模板渲染是 CPU 大头（大 Helm chart 尤其明显），应用多时要扩副本 + 调 `--parallelismlimit`；`timeout.reconciliation` 决定轮询周期，配 Git webhook 可以把「改完等 3 分钟」变成秒级。
  5. **排障**：`argocd app diff <app>` 看具体差异；`argocd app get <app>` 看每个资源的 sync/health；controller 日志里能看到 apply 的实际报错。
- **易错点**：把 Synced 当成「发布成功」；OutOfSync 假阳性反复自愈导致和 HPA 打架；repo-server 不扩容导致大规模下同步排队。
- **延伸**：Q18、Q20、Q21、来源：[Kubernetes Handbook - Argo CD](https://jimmysong.io/book/kubernetes-handbook/devops-argocd/)

### Q20. App-of-Apps 与 ApplicationSet 有什么区别？几十个集群怎么管？
- **难度**：🔴 高级
- **关键词**：App-of-Apps, ApplicationSet, 生成器 generator, 多集群, 模板化
- **概念速记**：
  - **App-of-Apps**：用一个 Application 去部署「一堆 Application 的 YAML」，本质是**手写**每个子应用，靠嵌套实现分层管理。
  - **ApplicationSet**：由 **ApplicationSet Controller** 根据**生成器（generator）+ 模板**自动产出 Application，是声明式的「批量生成」。
- **参考答案**：
  1. **选择标准**：应用数量少、彼此差异大 → App-of-Apps 够用且直观；应用**同构且要铺到很多集群/环境** → ApplicationSet，避免几百份复制粘贴的 YAML。
  2. **常用生成器**：
     - `List`：写死一组参数，最简单。
     - `Cluster`：遍历 Argo CD 里注册的所有集群 → **「这个基础组件要装到每个集群」的标准解法**。
     - `Git`（directory / file）：按仓库目录结构或配置文件生成 → 新增一个目录就自动多一个应用，**最贴近「配置驱动」**。
     - `SCM Provider` / `Pull Request`：按 GitHub/GitLab 的仓库或 PR 生成 → 每个 PR 自动拉起预览环境。
     - `Matrix` / `Merge`：组合多个生成器（如 集群 × 应用列表）。
  3. **最危险的开关——`applicationsSync` 策略**：ApplicationSet 默认会**删除**不再被生成器匹配的 Application。生成器输入一旦出错（Git 目录被误删、集群标签写错），可能批量删应用。生产建议先设 `preserveResourcesOnDeletion: true` 或 `applicationsSync: create-update`（只增改不删），并配合 Git 侧的保护。
  4. **大规模实践**：集群本身也纳入 GitOps（cluster registry 用 Secret 管理）；用 `goTemplate: true` 让模板可读；分层——平台组件用 Cluster 生成器全量铺，业务应用用 Git 生成器由各团队自助。
- **易错点**：用 ApplicationSet 但没考虑「生成器输入出错会删应用」；把环境差异硬塞进模板导致模板不可维护（应该用 Kustomize overlay 承载差异）。
- **延伸**：Q19、Q21、Q11

### Q21. GitOps 的漂移检测与自愈（selfHeal / prune）怎么配？有什么风险？
- **难度**：🔴 高级
- **关键词**：drift, selfHeal, prune, 手工变更, 逃生舱
- **概念速记**：GitOps 的核心承诺是「**Git 是唯一事实来源**」。`selfHeal` 把集群里的手工改动自动改回 Git 的样子；`prune` 删除 Git 里已经不存在的资源。
- **参考答案**：
  1. **收益**：杜绝「有人 kubectl edit 了但没人知道」的配置漂移；集群被误删后能自动重建；所有变更都有 Git 记录可审计可回滚。
  2. **风险一：应急操作被自动回滚**。事故中工程师手动扩容救火，selfHeal 在几分钟内把副本数改回去 —— 必须提前约定**逃生舱**：临时 `kubectl patch app <x> -p '{"spec":{"syncPolicy":null}}'` 关掉自动同步，或用 `argocd app set --sync-policy none`。**这个动作要写进 runbook**，不能事故当场现学。
  3. **风险二：prune 的破坏力**。资源在 Git 里被误删 → prune 直接从集群删掉。防护：对有状态资源加 `Prune=false` 注解；开 `PruneLast=true` 让删除发生在最后；**开启 prune 前先用 dry-run 看会删什么**。
  4. **风险三：和其他控制器抢写**。HPA 改 replicas、VPA 改 resources、sidecar 注入器加容器 —— 都会被判为漂移。用 `ignoreDifferences` 精确忽略这些字段。
  5. **务实的渐进策略**：`自动 sync 关闭（手动点）→ 自动 sync + selfHeal 关闭 → 全开 + prune`。非生产环境先全开，生产环境按团队成熟度逐步放开。
  6. **配套**：漂移本身要**告警**（有人绕过 Git 改了东西是流程问题，不只是技术问题）；结合 Skyscanner 那类事故（见 sre Q26），**GitOps 的自动化威力是双向的**——正确的配置能秒级铺满全球，错误的配置也一样。
- **易错点**：一上来就全开自动同步 + prune；事故时不知道怎么关自愈；不对漂移做告警，只是默默改回去。
- **延伸**：Q18、Q19、sre Q26

### Q22. Argo CD 的 sync wave 和 hook 怎么控制部署顺序？
- **难度**：🟡 中级
- **关键词**：sync-wave, PreSync/Sync/PostSync, Job, 数据库迁移
- **概念速记**：K8s 的 apply 本身没有顺序保证，但真实部署常有依赖（先建 CRD 再建 CR、先跑 DB 迁移再发应用）。Argo CD 用 **sync wave**（数字排序）和 **resource hook**（阶段钩子）解决。
- **参考答案**：
  1. **sync wave**：注解 `argocd.argoproj.io/sync-wave: "-1"`，**数字小的先执行**，同一 wave 内并行；Argo CD 会等前一个 wave 的资源变 Healthy 才进入下一个。典型编排：CRD/Namespace（-2）→ ConfigMap/Secret（-1）→ Deployment（0）→ Ingress/监控（1）。
  2. **hook 阶段**：
     - `PreSync`：同步前执行，典型用途是**数据库 schema 迁移 Job**。
     - `Sync`：与主同步一起。
     - `PostSync`：同步后执行，典型是冒烟测试、通知。
     - `SyncFail`：同步失败时执行，做清理或回滚。
     - `Skip`：不由 Argo CD 应用。
  3. **hook 的清理策略**：`hook-delete-policy` 可选 `HookSucceeded`（成功后删，最常用）/`HookFailed`/`BeforeHookCreation`。**不设会留下一堆历史 Job** 污染 namespace。
  4. **数据库迁移的正确做法**：PreSync Job 跑迁移，迁移必须**向前兼容**（先加列不删列、分两次发布），因为流量可以秒级回滚但 schema 不能（见 kubernetes Q30、service-mesh Q11）。
  5. **和 Helm hook 的关系**：Argo CD 能识别 Helm 的 hook 注解并映射到自己的阶段，但语义有细微差异，混用时以 Argo CD 的文档为准。
- **易错点**：以为 wave 内也有顺序；hook Job 不设删除策略导致堆积；迁移 Job 不幂等，重试就炸。
- **延伸**：Q9、Q19、kubernetes Q30

### Q23. AppProject 怎么划多租户边界？GitOps 下的权限模型是什么样的？
- **难度**：🔴 高级
- **关键词**：AppProject, sourceRepos, destinations, 白名单, RBAC
- **概念速记**：**AppProject** 是 Argo CD 的租户边界对象——它回答「这个团队能从**哪些仓库**、部署**哪些资源**、到**哪些集群/namespace**」。没有它，任何能创建 Application 的人都等于集群管理员。
- **参考答案**：
  1. **四道闸门**：
     - `sourceRepos`：允许的 Git 仓库白名单（防止从任意仓库拉 manifest）。
     - `destinations`：允许的 `(cluster, namespace)` 组合。
     - `clusterResourceWhitelist`：允许创建的**集群级**资源（默认应该是空的——业务团队不该能建 ClusterRole）。
     - `namespaceResourceBlacklist`：禁止的 namespace 级资源（如 ResourceQuota、LimitRange 这类该由平台方控制的）。
  2. **为什么 `clusterResourceWhitelist` 是重点**：允许业务团队创建 ClusterRole/ClusterRoleBinding，等于让他们能给自己提权到 cluster-admin —— **这是 GitOps 场景最典型的提权路径**。
  3. **Argo CD 自身的 RBAC**：`policy.csv` 定义谁能对哪个 project 的 application 做 get/sync/override/delete，结合 SSO（Dex/OIDC）映射组。注意 `sync` 权限 ≈ 部署权限，要和 Git 仓库的 CODEOWNERS 一起看——**真正的门禁应该在 PR 评审，Argo CD 的 RBAC 是第二道**。
  4. **和 K8s RBAC 的关系**：Argo CD 的 controller 通常有很大权限（要能 apply 各种资源），所以**限制必须在 AppProject 这一层做**，不能只依赖目标集群的 RBAC。
  5. **审计**：所有变更在 Git 有记录 + Argo CD 有操作事件；合规场景把两者都接入 SIEM。
- **易错点**：所有应用都放在 `default` project（等于没有隔离）；`clusterResourceWhitelist` 配 `*`；以为 Argo CD RBAC 能替代 Git 侧的评审门禁。
- **延伸**：Q7、Q19、cloud-security Q2、kubernetes Q25

### Q24. 镜像构建怎么做快？Docker build / BuildKit / bake / ko / apko 怎么选？
- **难度**：🔴 高级
- **关键词**：BuildKit, 构建缓存, 多阶段构建, ko, apko, 可复现构建
- **概念速记**：CI 里镜像构建慢，通常不是「机器不够快」，而是**缓存没命中**和**做了大量无谓的拷贝与压缩**。
- **参考答案**：
  1. **先把缓存用对**（收益最大，成本最低）：
     - Dockerfile 指令顺序按**变更频率从低到高**排：先 `COPY go.mod go.sum` + 下载依赖，再 `COPY . .` —— 否则改一行代码就重新拉全部依赖。
     - CI 上是全新 runner，本地层缓存没用，必须用 **`--cache-to/--cache-from`** 把缓存推到 registry（`type=registry,mode=max`）。
     - 用 **BuildKit 的 cache mount**（`RUN --mount=type=cache,target=/root/.cache/go-build`）缓存编译中间产物，这是 Go/Rust/npm 构建提速最明显的一招。
  2. **多阶段构建**：编译阶段用完整工具链，运行阶段只 `COPY --from` 出二进制，基础镜像用 distroless/alpine —— 镜像从几百 MB 降到几十 MB，同时大幅减少 CVE 面。
  3. **buildx + bake**：`bake` 用一个文件描述多个 target（多架构、多镜像），一次并行构建，避免脚本里串行调 N 次 `docker build`。**多数项目到这一步就够了**。
  4. **ko / apko（跳过 Docker）**：
     - **ko**：Go 专用，直接把编译好的二进制打成镜像层并推送，**不需要 Dockerfile、不需要 Docker daemon**，秒级出镜像。
     - **apko**：从 APK 包声明式地构建镜像，产出**可复现（reproducible）**、无 shell 的最小镜像，是 Chainguard Images 的底座。
     - 适用面窄但在其适用场景里快得多；社区从业者的普遍建议是「ko/apko 若符合场景就用，否则 buildx/bake 对大多数项目足够」。
  5. **别忽略的隐性开销**：镜像压缩 + 推到 registry + 节点再拉取解压，这一串复制在本地开发循环里占比很高——本地 kind 集群可以直接 `kind load` 或用本地 registry 省掉一跳。
- **易错点**：CI 上不配 registry cache，以为 BuildKit 自动就快；Dockerfile 里 `COPY . .` 放在依赖安装之前；把编译工具链留在最终镜像里。
- **延伸**：Q7、Q10、cloud-security Q14、来源：[Building Docker Images Fast (howardjohn)](https://blog.howardjohn.info/posts/docker-builds/)

### Q25. 气隙 / 离线（air-gapped）环境怎么做交付？
- **难度**：🔴 高级
- **关键词**：air-gap, 镜像同步, Helm chart 仓库, 依赖清单, 摆渡
- **概念速记**：气隙环境（金融、政府、工控）没有公网，所有依赖必须**显式清点、打包、摆渡进去**。难点从来不是技术，而是**「你根本不知道自己依赖了什么」**。
- **参考答案**：
  1. **先解决「清单」问题**：
     - 镜像：从渲染后的 manifest 里提取全部 image（`helm template | grep image:`、`kustomize build | yq`），注意 initContainer、sidecar 注入器要用的镜像、**CRD controller 拉起的临时 Job 镜像**（最容易漏）、以及 `pause` 镜像（漏了所有 Pod 起不来，见 kubernetes Q47）。
     - 制品：Helm chart、OS 包、语言依赖（Go module / npm / pip / maven）、Terraform provider。
  2. **摆渡工具**：`skopeo copy --all`（保留多架构 manifest list）或 `oras` 打包 OCI artifact；Helm chart 也能以 OCI 形式存进 registry，统一成一种载体最省事。**务必用 digest 而非 tag**，保证两边一致。
  3. **进去之后的改写**：所有 manifest 里的镜像地址要指向内网 registry —— 用 Kustomize 的 `images:` 或集群级的 **镜像重写 webhook / containerd 的 registry mirror 配置**，后者对业务无侵入，更适合大规模。
  4. **持续运维才是难点**：
     - 安全补丁怎么进？要有**定期同步窗口**和自动化流水线（外网侧构建 → 扫描 → 签名 → 导出 → 内网导入 → 验签）。
     - 漏洞库（Trivy DB）、时间同步（NTP）、证书吊销列表也都要离线更新。
  5. **验证**：在一个**真正断网**的环境里做全量部署演练。「以为配了 mirror 就行」和「真的断网能装起来」是两回事——大多数团队第一次演练都会失败在某个漏掉的镜像上。
- **易错点**：只同步了业务镜像，漏掉 pause/CNI/CSI/webhook 这些基础镜像；用 tag 同步导致两边内容不一致；没有持续更新机制，半年后集群跑着一堆高危 CVE。
- **延伸**：Q6、Q7、cloud-security Q14、kubernetes Q47
