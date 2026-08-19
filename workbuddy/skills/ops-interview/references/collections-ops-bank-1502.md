# 运维面试题库 — 22 专题 1502 题（收录）

> **来源**：运维面试题目汇总（按专题整理，仅保留题目，不含答案）
> **收录日期**：2026-08-19
> **说明**：覆盖 22 个专题、1502 道题目，涵盖 Ansible / AWS / CI-CD / Cloud-Native / Docker / ELK / Jenkins / K8s / Linux / Middleware / MySQL / Network / Nginx / Other / Process / Prometheus / Python / Redis / Shell / Vibe-Coding / Website / Zabbix。
> **版权**：仅收录题目列表，不含参考答案与付费内容。分组保留原文。

---

## ANSIBLE（42 题）

1. Ansible 核心架构，Inventory、模块、Task、Playbook、Role 之间的关系？
2. Ansible 与 Puppet、Chef 在架构和运维场景上的核心差异？
3. Ansible 是声明式还是过程式？它和可变基础设施、幂等收敛有什么关系？
4. 哪些自动化任务不适合用 Ansible 做，为什么？
5. ansible-pull 和 ansible-playbook 的执行模型有什么不同？
6. Ansible Tower/AWX 能解决哪些集中化治理问题？
7. Ansible 与 Terraform 应该如何分工协作？
8. 静态 Inventory 如何定义主机、分组和执行范围，生产中如何避免误操作？
9. 动态 Inventory 适合哪些场景，如何保证它在生产环境稳定可靠？
10. 多环境配置和变量传递应如何组织，才能兼顾复用与隔离？
11. 如何安全处理变量默认值、可选变量和环境变量 lookup？
12. 变量类型导致条件判断异常时，如何做类型转换和排查？
13. Facts 是什么，如何基于系统事实做条件执行和排障？
14. 变量优先级冲突时，如何定位最终取值并治理覆盖风险？
15. Jinja2 模板在 Ansible 配置生成中怎么用，如何处理变更触发？
16. Ansible Vault 如何管理敏感数据，生产中还要注意哪些边界？
17. Playbook 的定位是什么，核心字段应该如何组织？
18. handlers 和 notify 如何实现“配置变更后才 reload”？
19. Playbook 中 tags 有什么用，生产中如何做选择性执行？
20. blocks、rescue、always 适合解决什么编排问题？
21. 如何用 when、loop、stat/assert 编排基于系统状态的任务？
22. 如何用 host pattern、组排除和 limit 精确选择目标主机？
23. include_tasks 和 import_tasks 有什么区别，什么时候分别使用？
24. Ansible 的执行策略、主机顺序和 serial 批次控制应该怎么理解？
25. 如何设计一个可回滚的 Ansible 应用灰度发布 Playbook？
26. Ansible 模块体系如何理解，常用模块和文档查询怎么用？
27. Ansible 过滤器和自定义 filter plugin 如何使用和开发？
28. 回调插件 callback plugin 能扩展什么执行结果能力？
29. Ansible Collection 的定位和价值是什么？
30. Playbook 与 Role 的职责如何分层？
31. 一个可复用 Role 应该有哪些目录，如何用于批量加入 K8s 集群？
32. Ansible 工程最佳实践有哪些，如何落到团队规范？
33. become 和 become_user 如何设计权限提升，生产中有哪些风险？
34. Permission denied 和 unreachable 应该按什么链路排查？
35. 包管理任务执行失败时，如何修复并兼容不同发行版？
36. Ansible 中如何处理任务错误、失败条件和补偿动作？
37. forks、serial、throttle 如何影响大规模执行性能和风险？
38. lineinfile 修改配置文件时，如何保证幂等和可回滚？
39. 如何测试 Ansible 项目，Molecule 和幂等性测试失败代表什么？
40. 如何判断 Ansible 基础规则中的常见说法是真还是假？
41. Terraform 的工作原理是什么，state 在 IaC 中解决什么问题？
42. Terraform 在阿里云上自动创建 ECS 的流程是什么，如何与 Ansible 后续配置衔接？

## AWS（103 题）

1. AWS 基础概念、云平台对比与服务边界在生产运维中怎么设计、配置和排障？
2. 区域、可用区、边缘节点、ARN、账号与访问方式的定位、适用场景和边界是什么？
3. 区域、可用区、边缘节点、ARN、账号与访问方式的核心机制和生产限制是什么？
4. Cognito、身份联合与应用访问控制在生产运维中怎么设计、配置和排障？
5. IAM 用户、角色、策略、MFA 与权限边界怎么串成生产级答案？
6. KMS、ACM、CloudHSM 与密钥证书管理的定位、适用场景和边界是什么？
7. KMS、ACM、CloudHSM 与密钥证书管理的核心机制和生产限制是什么？
8. 责任共担、合规、WAF、Shield、GuardDuty 与 Inspector 的定位、适用场景和边界是什么？
9. 责任共担、合规、WAF、Shield、GuardDuty 与 Inspector 的核心机制和生产限制是什么？
10. 责任共担、合规、WAF、Shield、GuardDuty 与 Inspector 的配置和变更在生产环境如何落地？
11. 责任共担、合规、WAF、Shield、GuardDuty 与 Inspector 的权限、安全和访问边界如何设计？
12. Auto Scaling、启动模板、扩缩策略与生命周期钩子的定位、适用场景和边界是什么？
13. Auto Scaling、启动模板、扩缩策略与生命周期钩子的核心机制和生产限制是什么？
14. Auto Scaling、启动模板、扩缩策略与生命周期钩子的配置和变更在生产环境如何落地？
15. EBS、EFS、Storage Gateway、Snowball 与基础存储的定位、适用场景和边界是什么？
16. EBS、EFS、Storage Gateway、Snowball 与基础存储的核心机制和生产限制是什么？
17. EBS、EFS、Storage Gateway、Snowball 与基础存储的配置和变更在生产环境如何落地？
18. EBS、EFS、Storage Gateway、Snowball 与基础存储的权限、安全和访问边界如何设计？
19. EBS、EFS、Storage Gateway、Snowball 与基础存储的典型故障如何排查？
20. EBS、EFS、Storage Gateway、Snowball 与基础存储的高可用、备份和恢复方案如何设计？
21. EBS、EFS、Storage Gateway、Snowball 与基础存储的容量、性能和成本如何评估？
22. EBS、EFS、实例存储、快照与存储性能的定位、适用场景和边界是什么？
23. EBS、EFS、实例存储、快照与存储性能的核心机制和生产限制是什么？
24. EBS、EFS、实例存储、快照与存储性能的配置和变更在生产环境如何落地？
25. EC2 定价、Spot、预留实例、专用主机与容量预留的定位、适用场景和边界是什么？
26. EC2 定价、Spot、预留实例、专用主机与容量预留的核心机制和生产限制是什么？
27. EC2 定价、Spot、预留实例、专用主机与容量预留的配置和变更在生产环境如何落地？
28. EC2 定价、Spot、预留实例、专用主机与容量预留的权限、安全和访问边界如何设计？
29. EC2、AMI、实例类型、启动配置与生命周期怎么串成生产级答案？
30. CloudFront、Global Accelerator 与边缘加速在生产运维中怎么设计、配置和排障？
31. ELB、ALB、NLB、目标组与流量分发怎么串成生产级答案？
32. Route 53、DNS 记录、路由策略与健康检查的定位、适用场景和边界是什么？
33. Route 53、DNS 记录、路由策略与健康检查的核心机制和生产限制是什么？
34. Route 53、DNS 记录、路由策略与健康检查的配置和变更在生产环境如何落地？
35. VPC、子网、路由表、IGW、NAT 与默认 VPC 的定位、适用场景和边界是什么？
36. VPC、子网、路由表、IGW、NAT 与默认 VPC 的核心机制和生产限制是什么？
37. VPC、子网、路由表、IGW、NAT 与默认 VPC 的配置和变更在生产环境如何落地？
38. VPC、子网、路由表、IGW、NAT 与默认 VPC 的权限、安全和访问边界如何设计？
39. VPC、子网、路由表、IGW、NAT 与默认 VPC 的典型故障如何排查？
40. VPC、子网、路由表、IGW、NAT 与默认 VPC 的高可用、备份和恢复方案如何设计？
41. 公网 IP、Elastic IP、ENI 与实例网络属性的定位、适用场景和边界是什么？
42. 公网 IP、Elastic IP、ENI 与实例网络属性的核心机制和生产限制是什么？
43. 安全组、NACL 与网络访问边界的定位、适用场景和边界是什么？
44. 安全组、NACL 与网络访问边界的核心机制和生产限制是什么？
45. 安全组、NACL 与网络访问边界的配置和变更在生产环境如何落地？
46. 混合网络、Direct Connect、VPN、Peering 与 PrivateLink 在生产运维中怎么设计、配置和排障？
47. S3 存储桶、对象、多部分上传与静态站点的定位、适用场景和边界是什么？
48. S3 存储桶、对象、多部分上传与静态站点的核心机制和生产限制是什么？
49. S3 存储桶、对象、多部分上传与静态站点的配置和变更在生产环境如何落地？
50. S3 存储桶、对象、多部分上传与静态站点的权限、安全和访问边界如何设计？
51. S3 存储类、生命周期、版本控制与传输加速的定位、适用场景和边界是什么？
52. S3 存储类、生命周期、版本控制与传输加速的核心机制和生产限制是什么？
53. S3 安全、预签名 URL 与服务端加密的定位、适用场景和边界是什么？
54. S3 安全、预签名 URL 与服务端加密的核心机制和生产限制是什么？
55. 灾难恢复、RTO/RPO 与跨区域可用性的定位、适用场景和边界是什么？
56. 灾难恢复、RTO/RPO 与跨区域可用性的核心机制和生产限制是什么？
57. Aurora、Serverless、多主与高可用数据库的定位、适用场景和边界是什么？
58. Aurora、Serverless、多主与高可用数据库的核心机制和生产限制是什么？
59. DocumentDB、DMS 与专项数据库迁移在生产运维中怎么设计、配置和排障？
60. DynamoDB 表、PITR、全局表与 DAX 在生产运维中怎么设计、配置和排障？
61. ElastiCache、Redis/Memcached 与缓存架构的定位、适用场景和边界是什么？
62. ElastiCache、Redis/Memcached 与缓存架构的核心机制和生产限制是什么？
63. RDS、多 AZ、只读副本、备份与加密的定位、适用场景和边界是什么？
64. RDS、多 AZ、只读副本、备份与加密的核心机制和生产限制是什么？
65. RDS、多 AZ、只读副本、备份与加密的配置和变更在生产环境如何落地？
66. RDS、多 AZ、只读副本、备份与加密的权限、安全和访问边界如何设计？
67. RDS、多 AZ、只读副本、备份与加密的典型故障如何排查？
68. RDS、多 AZ、只读副本、备份与加密的高可用、备份和恢复方案如何设计？
69. Redshift、Athena、Glue、EMR、Kinesis 与数据分析的定位、适用场景和边界是什么？
70. Redshift、Athena、Glue、EMR、Kinesis 与数据分析的核心机制和生产限制是什么？
71. Lambda、API Gateway 与无服务器运行模型的定位、适用场景和边界是什么？
72. Lambda、API Gateway 与无服务器运行模型的核心机制和生产限制是什么？
73. SQS、SNS、SWF、队列语义与事件解耦的定位、适用场景和边界是什么？
74. SQS、SNS、SWF、队列语义与事件解耦的核心机制和生产限制是什么？
75. SQS、SNS、SWF、队列语义与事件解耦的配置和变更在生产环境如何落地？
76. SQS、SNS、SWF、队列语义与事件解耦的权限、安全和访问边界如何设计？
77. ECS、ECR、Fargate、共享存储与容器事件的定位、适用场景和边界是什么？
78. ECS、ECR、Fargate、共享存储与容器事件的核心机制和生产限制是什么？
79. CloudWatch、CloudTrail、Config、SSM 与审计监控的定位、适用场景和边界是什么？
80. CloudWatch、CloudTrail、Config、SSM 与审计监控的核心机制和生产限制是什么？
81. Organizations、SCP、资源组与架构最佳实践的定位、适用场景和边界是什么？
82. Organizations、SCP、资源组与架构最佳实践的核心机制和生产限制是什么？
83. Organizations、SCP、资源组与架构最佳实践的配置和变更在生产环境如何落地？
84. X-Ray、应用性能诊断与链路追踪在生产运维中怎么设计、配置和排障？
85. 成本估算、账单、标签、预算与优化工具在生产运维中怎么设计、配置和排障？
86. CloudFormation 模板、Stack、Change Set、StackSet 与宏的定位、适用场景和边界是什么？
87. CloudFormation 模板、Stack、Change Set、StackSet 与宏的核心机制和生产限制是什么？
88. CloudFormation 模板、Stack、Change Set、StackSet 与宏的配置和变更在生产环境如何落地？
89. CloudFormation 模板、Stack、Change Set、StackSet 与宏的权限、安全和访问边界如何设计？
90. CodeDeploy、Elastic Beanstalk、CDK、Quick Starts 与交付平台的定位、适用场景和边界是什么？
91. CodeDeploy、Elastic Beanstalk、CDK、Quick Starts 与交付平台的核心机制和生产限制是什么？
92. AWS 综合概念、服务边界与未归类题的定位、适用场景和边界是什么？
93. AWS 综合概念、服务边界与未归类题的核心机制和生产限制是什么？
94. AWS 综合概念、服务边界与未归类题的配置和变更在生产环境如何落地？
95. AWS 综合概念、服务边界与未归类题的权限、安全和访问边界如何设计？
96. AWS 综合概念、服务边界与未归类题的典型故障如何排查？
97. 专项服务认知、支持计划与服务目录的定位、适用场景和边界是什么？
98. 专项服务认知、支持计划与服务目录的核心机制和生产限制是什么？
99. 服务选型题与跨服务能力匹配的定位、适用场景和边界是什么？
100. 服务选型题与跨服务能力匹配的核心机制和生产限制是什么？
101. 服务选型题与跨服务能力匹配的配置和变更在生产环境如何落地？
102. 高可用、零停机、流量激增与架构排障场景的定位、适用场景和边界是什么？
103. 高可用、零停机、流量激增与架构排障场景的核心机制和生产限制是什么？

## CI-CD（83 题）

1. 如何区分持续集成、持续交付和持续部署，并说明各自的落地边界？
2. 什么时候适合引入 CI/CD，如何向业务说明它的价值？
3. 一次代码提交到生产发布，标准 CI/CD 流水线应如何设计？
4. 怎样判断一条 CI/CD 流水线是否达到生产级成熟度？
5. 一个应用依赖多个服务时，CD 流水线应该怎样设计？
6. 流水线为什么要代码化管理，Webhook 触发链路如何设计？
7. CI/CD Runner、Agent 和队列容量应该如何规划和优化？
8. 如何用指标衡量 CI/CD 流水线质量，而不是只看是否跑完？
9. 如何在 CI 阶段落地持续测试、测试左移和质量门禁？
10. 你如何理解 DevOps，它解决了开发和运维之间的什么问题？
11. DevOps 工程师和高效 DevOps 团队的核心职责是什么？
12. 一个典型 DevOps 工作流应该怎样从需求流转到线上反馈？
13. 在公司推行 DevOps 前要准备什么，常见阻力如何处理？
14. DevOps 工具和 CI/CD 平台应该如何选型或迁移？
15. 敏捷、精益 IT、DevOps 和持续交付之间是什么关系？
16. 实践 DevOps 是否天然会让软件更安全，安全文化该如何落地？
17. 开源协作模型对 DevOps 团队有什么启发，如何说明贡献经验？
18. 常见 DevOps 反模式有哪些，如何系统提升研发效能？
19. 为什么 CI/CD 必须依赖版本控制，Git 提交应如何治理？
20. Git 合并冲突应该如何解决，怎样降低协作风险？
21. SCM 团队在 DevOps 中承担什么治理职责？
22. 功能分支流程和 GitLab Flow 在 CI/CD 中应如何使用？
23. QA 团队在 DevOps 中如何参与质量门禁和发布验收？
24. GitLab 仓库代码如何备份、恢复和保护？
25. Jenkins 适合什么 CI/CD 场景，它的优势和限制是什么？
26. Jenkins 的核心对象、作业类型和插件生态如何理解？
27. 如何设计 Jenkinsfile 流水线，并支持阶段控制和失败恢复？
28. Jenkins Agent、并发构建和队列优先级应该如何治理？
29. Jenkins 如何做权限、凭据、通知和构建结果报告？
30. 大量 Jenkins 作业如何自动化管理，什么时候需要脚本或插件？
31. GitHub Actions 的 workflow、job、step、action 和 on 如何组织？
32. GitHub Actions Runner 和 job 依赖关系如何设计？
33. GitLab CI 如何通过 .gitlab-ci.yml 实现多阶段自动化测试和部署？
34. GitLab Runner 在生产中可以从哪些方面优化？
35. GitLab CI 中 cache、artifacts、include 和 environment 各解决什么问题？
36. Travis CI 如何通过 .travis.yml、变量和 GitHub 集成完成自动构建？
37. Travis CI 如何做多语言和多版本构建矩阵测试？
38. Azure DevOps 如何覆盖从需求到制品的 CI/CD 管理？
39. Zuul 的 check 和 gate 流水线有什么区别，为什么适合门禁合并？
40. 构建工件和制品仓库在 CI/CD 中应该如何治理？
41. 软件分发有哪些方式，不同分发渠道如何选择？
42. 构建缓存为什么能加速 CI，缓存失效和污染如何控制？
43. 无状态和有状态服务会如何影响 CI/CD 和部署架构？
44. 部署 Web 服务器时应如何说明安装、配置、启动和验证流程？
45. 如何在 Ubuntu、RHEL 等不同系统上做幂等包安装自动化？
46. 什么是 IaC，它给 CI/CD 和运维治理带来什么收益？
47. 只在开发机本地测试再推送有什么问题，如何改造成 CI 门禁？
48. 跨仓库、跨服务依赖变更如何做集成验证？
49. 选择 CI 方案时应比较哪些维度，如何说明你的偏好？
50. 滚动、蓝绿、灰度和金丝雀部署分别适合什么场景？
51. 如何描述一个生产网站从构建到灰度再到回滚的真实发版流程？
52. 多集群发布如何做到逐个集群晋级、暂停和回退？
53. 配置到部署、部署到配置和不可变基础设施应该如何取舍？
54. 配置漂移为什么危险，如何建立检测、修复和审计闭环？
55. 声明式和过程式自动化有什么区别，CI/CD 中如何选用？
56. 应用配置和基础设施代码放同仓还是独立仓，如何设计权限边界？
57. DevOps 下的变更审批和部署频率目标应该如何治理？
58. 什么是 GitOps，为什么 Git 仓库能成为交付的事实来源？
59. ArgoCD 相比 Jenkins 等传统 CI/CD 系统的价值和边界是什么？
60. 使用 ArgoCD 的 GitOps 工作流如何支撑日常发布和灾难恢复？
61. ArgoCD 如何处理漂移、同步、自愈和自动修剪？
62. ArgoCD Application CRD 的核心字段和 YAML 结构是什么？
63. ArgoCD 如何通过 Project、ApplicationSet 或 App of Apps 管理多应用？
64. ArgoCD 如何渲染 YAML、Helm 和 Kustomize，Helm 应用语义有什么变化？
65. ArgoCD reconciliation 周期做什么，timeout.reconciliation 如何影响同步？
66. ArgoCD 应用状态异常或命名空间未创建时如何排障？
67. 常用 argocd CLI 如何创建、查看和同步应用？
68. ArgoCD 如何管理多集群，并隔离 dev、staging、prod？
69. ArgoCD 如何帮助收敛 Kubernetes 访问权限？
70. ArgoCD 如何判断应用健康状态，并为 CRD 配置自定义健康检查？
71. Argo Rollouts 解决什么问题，它和 ArgoCD 是什么关系？
72. Argo Rollouts 回滚新版本时发生什么，如何操作？
73. Argo Rollouts 如何实现蓝绿和金丝雀发布？
74. Argo Rollouts Analysis 如何替代人工烟雾测试和发布观察？
75. Argo Rollouts CLI 如何查询、提升和监控发布进度？
76. 可靠性、可用性和 SLO 应如何设定，为什么通常不追求 100%？
77. SRE 和 DevOps 的职责边界与协作方式是什么？
78. 错误预算如何约束发布节奏，SRE KPI 应如何使用？
79. MTTF、MTTR 能衡量什么，如何提升恢复能力？
80. CI/CD 和 SRE 中应该如何设计监控、追踪和反馈闭环？
81. 什么是 Toil，如何把重复运维工作转化为自动化改进？
82. 事故复盘和无责文化如何帮助团队持续改进？
83. 混沌工程如何做故障注入，并保证实验安全？

## CLOUD-NAVITE（74 题）

1. Terraform 在云原生 IaC 中解决什么问题，核心机制是什么？
2. 为什么生产环境要用 IaC，哪些操作仍可以保留手工边界？
3. Terraform 适合管什么，和 Ansible、Puppet、Chef 如何分工？
4. Terraform 和 CloudFormation 在多云与 AWS 原生场景下如何选型？
5. 从 main.tf 到生产变更，Terraform init、plan、apply 应如何落地？
6. 如何安全清理 Terraform 资源，为什么 destroy 必须谨慎？
7. Terraform plan/apply 中的符号如何帮助做生产变更评审？
8. 拿到一段 Terraform 配置时，应该从哪些维度解释它的执行影响？
9. Terraform 如何通过资源引用推导依赖和创建顺序？
10. 如何查看 Terraform 依赖图，什么时候才需要 depends_on？
11. Terraform Provider 在云 API 和 HCL 之间承担什么职责？
12. terraform init 安装 Provider 时发生了什么，如何治理版本和来源？
13. Terraform variable 如何提升配置复用，类型和默认值应该怎么设计？
14. 生产流水线中如何给 Terraform 变量赋值并避免交互式提示？
15. Terraform 中 var 引用和字符串插值的正确写法是什么？
16. 如何用对象变量和类型约束建模复杂 Terraform 输入？
17. Terraform sensitive 能保护什么，生产 Secret 应该如何治理？
18. Terraform output 如何在模块和流水线之间传递结果？
19. 不重新 apply 时如何查询 Terraform 输出，适合哪些自动化场景？
20. locals 和 input variables 有什么区别，生产配置中怎么使用？
21. Terraform data source 如何读取已有资源并参与新资源编排？
22. 什么时候需要组合多个 data source，它会带来哪些耦合风险？
23. Terraform 中列表和对象列表如何建模并提取属性？
24. Terraform count 如何批量创建资源，索引漂移风险怎么处理？
25. for_each 和 dynamic block 如何表达差异化多实例配置？
26. 为什么团队 Terraform 必须使用 remote state 和 state locking？
27. Terraform state 文件是什么，里面保存了哪些关键数据？
28. 为什么 tfstate 不能随意本地存放或提交到 Git？
29. Terraform state 应如何治理，为什么不能手工编辑？
30. Terraform 如何管理 dev、stage、prod 的状态和配置隔离？
31. Terraform workspace 如何隔离状态，适合哪些环境场景？
32. 为什么 workspace 不一定适合强隔离生产环境？
33. Terraform backend 的职责是什么，如何配置远程后端？
34. 使用远程 backend 后 apply 工作流有什么变化，如何安全迁移回本地？
35. backend 有哪些限制，如何安全读取 remote state 输出？
36. Terraform state list/show/mv 适合解决哪些生产问题？
37. Terraform workspace 的创建、切换和识别命令怎么用？
38. Terraform 代码如何纳入版本控制、评审和回滚治理？
39. Terraform 更新资源时如何决定原地修改或替换，lifecycle 怎么控制风险？
40. Terraform provisioner 能做什么，为什么常被替代为 cloud-init？
41. local-exec 和 remote-exec 的执行位置、连接方式和风险是什么？
42. Terraform tainted resource 和强制替换在什么场景下使用？
43. Terraform module 如何设计复用边界并传递跨模块依赖？
44. 如何把已有云资源导入 Terraform，并避免导入后漂移？
45. Terraform 管理多云基础设施时，Provider、认证和状态如何治理？
46. 云原生和传统应用的核心差异是什么，为什么不能等同于 Kubernetes？
47. 不可变基础设施如何支撑云原生交付，技术栈应如何分层？
48. 云原生应用如何设计弹性扩展和高可用？
49. 微服务要如何设计，才能真正适配云原生运行环境？
50. Service Mesh 主要解决服务间通信治理的哪些问题？
51. Service Mesh 如何做流量拆分、熔断、故障注入和金丝雀？
52. Serverless、App Engine、GKE 和 Cloud Functions 的运维边界有什么不同？
53. 限流、熔断和降级分别保护什么，生产中如何组合？
54. 有状态和无状态应用在云原生扩缩容中有什么差异？
55. 建设云原生可观测性时，第一步为什么不是先装工具？
56. Observability 和传统监控在云原生环境中有什么差异？
57. Metrics、Tracing、Logging 三大信号如何统一落地？
58. OpenTelemetry 的架构是什么，如何设计接入和采样策略？
59. 你如何使用 Jaeger、Zipkin、SkyWalking 或 Tempo 做链路排障？
60. GitOps 的核心理念是什么，和 CI/CD 应如何配合？
61. Argo CD 如何通过 Application 和同步策略实现 K8s 持续部署？
62. 容器运行时安全和 Kubernetes 安全基线应该怎么做？
63. Azure Monitor 能提供哪些托管可观测能力，如何接入告警闭环？
64. Azure Resource Manager 如何支撑资源组、权限、标签和审计治理？
65. Azure Virtual Network 应如何规划子网、NSG、路由和混合网络？
66. Azure App Services 适合托管哪些应用，生产运维关注点是什么？
67. Azure Storage Account 和 Blob 静态网站托管如何设计与治理？
68. Azure VM 在创建、网络、安全、磁盘和运维上应如何管理？
69. Azure Cosmos DB 的全球复制、一致性和 RU 模型如何影响设计？
70. GCP BigQuery 和 Bigtable 如何按分析与低延迟场景选型？
71. GCP Cloud Storage Bucket 如何配置区域、IAM、生命周期和公开访问？
72. GCP Compute Engine 如何管理单实例、模板和 MIG？
73. GCP Pub/Sub 如何实现发布订阅，消费端怎样保证幂等？
74. GCP Dataflow 如何基于 Apache Beam 做批流统一处理？

## DOCKER（88 题）

1. 容器的本质、目标和收益是什么？
2. Docker Engine、镜像、容器和仓库如何协同工作？
3. Docker 镜像和容器的边界应该怎么解释？
4. 容器和虚拟机在架构、隔离和资源开销上有什么差异？
5. 容器、虚拟机、LXC 和 Vagrant 分别适合什么场景？
6. Docker 在 Windows 和 macOS 上为什么还需要虚拟化层？
7. 应用容器化时为什么强调单主进程和不可变镜像？
8. namespace、cgroups 和 rootfs 如何共同实现容器隔离？
9. 执行 `docker run hello-world` 背后发生了什么？
10. `docker pull image:tag` 的客户端、daemon 和 registry 链路是什么？
11. dockerd、containerd 和 runc 的职责边界是什么？
12. containerd-shim 为什么存在，dockerd 异常会不会杀掉容器？
13. OCI 规范解决什么问题，容器运行时必须支持哪些操作？
14. 容器内进程和资源在宿主机上为什么仍然可见？
15. 如何搜索、查看和只拉取 Docker 镜像而不运行？
16. 镜像被容器引用、悬空或废弃时应该怎么删除？
17. Docker 镜像和容器文件默认存在哪里，排障时怎么看？
18. `latest` 标签到底表示什么，生产为什么不该依赖它？
19. 团队如何管理镜像 tag，避免多版本协作混乱？
20. Docker 镜像层、联合文件系统和共享层怎么讲清楚？
21. 如何用 history、inspect 和 diff 追踪镜像层与文件变化？
22. 镜像 digest 和分发哈希如何保证可重复拉取？
23. 多架构镜像如何工作，怎样避免架构不匹配？
24. 如何查看镜像默认启动命令和环境变量元数据？
25. Dockerfile、commit 和调试镜像分别适合什么场景？
26. 不经过 Registry 时如何离线共享 Docker 镜像？
27. Dockerfile 的核心指令和构建流程应该怎么回答？
28. build context 和 `.dockerignore` 对性能与安全有什么影响？
29. Dockerfile 里 ADD 和 COPY 怎么选？
30. RUN 和 CMD 的构建期、运行期边界是什么？
31. ENTRYPOINT、CMD 和 `docker run` 参数的覆盖关系是什么？
32. `docker image build` 从 Dockerfile 到镜像产物经历哪些步骤？
33. Docker 构建缓存如何命中，哪些指令会生成新层？
34. 多阶段构建为什么能缩小运行镜像并提升安全性？
35. 如何系统优化 Docker 镜像体积，压缩镜像有什么取舍？
36. Dockerfile 和镜像构建有哪些生产级最佳实践？
37. Registry、Repository、Index 和镜像命名层级有什么关系？
38. 如何查看和配置 Docker 默认 Registry？
39. 镜像 push/pull 到私有仓库时要注意哪些命名和认证问题？
40. Harbor 由哪些组件组成，各自承担什么职责？
41. Harbor 高可用架构应该如何设计？
42. Docker daemon 配置文件在哪里，修改后如何安全生效？
43. `docker run` 常见参数如何组织，前台和后台运行有什么区别？
44. 容器启动后立即退出通常是什么原因？
45. 如何用 `docker ps` 和 `docker inspect` 看清容器状态？
46. `docker attach`、`docker exec` 和退出不停止容器怎么区分？
47. 停止、重启、删除容器时有哪些安全边界？
48. `--rm`、停止容器和历史容器应该如何清理？
49. 如何在不牺牲可观测性的前提下优化容器启动时间？
50. 容器和宿主机、容器之间如何安全复制数据？
51. 容器退出或删除后，可写层和持久化数据分别会怎样？
52. Docker bridge、host、none、container、overlay 网络怎么选？
53. bridge 网络下如何把容器服务发布到宿主机 localhost？
54. Docker 容器之间如何通信和按名称发现服务？
55. 容器内如何访问宿主机上的 localhost 服务？
56. 跨主机容器通信为什么通常需要 overlay 网络？
57. veth、bridge、iptables 和 namespace 如何实现 Docker 网络？
58. CNM、libnetwork、sandbox、endpoint 和 network 如何对应？
59. 容器可写层为什么是临时存储，持久化边界在哪里？
60. Docker volume 如何创建、挂载、备份和迁移？
61. bind mount 权限不足时如何从 UID/GID 和 SELinux 排查？
62. Docker storage driver 解决什么问题，overlay2 为什么常用？
63. 停止容器仍占用存储时如何安全回收？
64. 如何迁移 Docker 默认数据目录，风险点有哪些？
65. 生产环境如何选择 volume、bind mount 和外部存储？
66. Docker Compose 适合解决什么问题，不适合替代什么？
67. Compose 文件编写、启动、更新和停止的标准流程是什么？
68. Compose、Swarm、Kubernetes 等编排工具如何定位？
69. Docker Swarm 的 manager、worker、service 和 task 如何协作？
70. 如何用 Docker Swarm 部署高可用集群？
71. Docker Interlock 如何为容器服务动态配置入口流量？
72. Docker 默认安全吗，生产安全基线应该怎么做？
73. Docker 容器 CPU 和内存限制如何配置并验证？
74. 容器共享内核会带来哪些主机风险，如何防护？
75. Docker API 和 daemon socket 暴露有什么安全风险？
76. 容器内 root 和宿主机 root 是什么关系，风险在哪里？
77. Rootless Docker 带来哪些安全收益和限制？
78. Rootless 模式下网络和分层文件系统如何实现？
79. 如何查看 Docker 后台容器日志并定位日志驱动问题？
80. 容器启动报 exec format error 应该如何排查？
81. 非官方仓库 invalid registry endpoint 如何处理？
82. `docker port` 提示 No public port published 是什么意思？
83. 容器时区或时间和宿主机不一致怎么处理？
84. Docker 服务器磁盘超过阈值时如何定位和清理？
85. 误删 `/var/run/netns` 下网络命名空间文件后如何恢复？
86. 生产环境使用 Docker 容器有哪些总原则？
87. Docker 健康检查、自愈和重启策略如何设计？
88. 如何把一台宿主机的 Docker 环境迁移到另一台？

## ELK（50 题）

1. Elastic Stack 的组件职责和日志流转链路是什么？
2. ELK 架构中为什么要引入消息队列？
3. Redis 和 Kafka 作为日志缓冲队列应该怎么选？
4. 每天百 GB 日志量的 ELK 架构如何设计？
5. Fleet Server 架构和传统 ELK 架构的适用边界是什么？
6. ELK、Loki、Graylog 和 ClickHouse 做日志平台时如何选型？
7. Grafana Loki 的日志管理工作流程是什么？
8. Elasticsearch 的基础术语和数据模型如何串起来讲？
9. Elasticsearch 有哪些节点角色，各自承担什么职责？
10. Elasticsearch 集群架构和读写工作原理是什么？
11. Elasticsearch 主节点选举机制如何保证不脑裂？
12. 业务搜索型 ES 和日志检索型 ES 架构有什么差异？
13. Elasticsearch 常用插件和扩展能力应该如何理解？
14. Elasticsearch 的 version、seq_no 和 primary_term 解决什么问题？
15. ES 数据量越大是否一定需要越多 JVM 内存？
16. 日志索引的 Mapping 应该如何设计，为什么它会影响查询和聚合？
17. Elasticsearch 写入索引的完整流程是什么？
18. ES 底层存储和 Lucene Segment 机制如何影响日志平台运维？
19. 单文档 GET 的路由与读取流程是什么？
20. ES 全文搜索的 query/fetch 流程如何解释？
21. 全文检索和精确搜索在日志查询里有什么区别？
22. 如何提升 Elasticsearch 查询结果的相关性评分？
23. Elasticsearch 聚合有哪些类型，日志平台使用时有哪些边界？
24. ILM 如何管理日志索引生命周期并自动删除历史数据？
25. ES 集群磁盘快满时如何扩容和治理容量？
26. ES 集群数据如何做快照备份和恢复？
27. ES 集群一般要监控哪些指标？
28. ES 综合性能优化应该从哪些层面入手？
29. ES 写入性能如何优化？
30. ES 查询性能如何优化？
31. 如何在 ES 集群中添加或移除节点？
32. ES JVM 调优要关注哪些经验和边界？
33. ES 集群 green、yellow、red 分别代表什么？
34. ES 集群 red 状态如何恢复？
35. ES 集群 yellow 状态如何排除？
36. ES 查询慢和写入慢如何分层排查？
37. ES JVM 使用率过高如何排查？
38. ES Young GC、Old GC 和 Full GC 如何理解并排查？
39. Logstash 的工作流程和架构模型如何说明？
40. Logstash 有哪些输入源和典型应用场景？
41. Logstash Pipelines 多管道机制是什么，生产中怎么用？
42. Logstash 常用过滤器插件有哪些，如何避免解析质量和性能问题？
43. Logstash 如何提升吞吐并定位性能瓶颈？
44. Filebeat 是如何读取日志文件的？
45. Filebeat 如何保证可靠投递、断点续传和连续发送？
46. 如何提高 Filebeat 采集和发送性能？
47. ELK 如何采集 Kubernetes 和容器日志？
48. Kibana Discover 在日志排障中怎么用？
49. Kibana Dashboard 应该如何设计日志图表和可视化？
50. ELK 如何实现告警通知并治理误报？

## JENKINS（30 题）

1. Jenkins 在 CI/CD 编排中的价值和边界怎么讲清楚？
2. Jenkins 与 GitLab CI/CD 的架构和选型差异是什么？
3. Jenkins 插件生态在生产环境应该怎么使用和治理？
4. Blue Ocean 适合解决什么可视化问题，生产使用边界是什么？
5. 如何设计一条生产可用的 Jenkins Pipeline 覆盖构建、测试和部署？
6. Freestyle、Declarative、Scripted 和 Multibranch Pipeline 如何区分？
7. Jenkinsfile 的作用、结构和版本化治理应该怎么回答？
8. Jenkins Pipeline 从触发到阶段执行的工作原理是什么？
9. Groovy 在 Jenkins Pipeline 中应该如何使用，边界在哪里？
10. Shared Library 如何复用公共流水线逻辑并控制风险？
11. Pipeline 的 post 阶段如何处理归档、通知、清理和失败闭环？
12. Jenkins 多分支流水线如何发现分支、PR/MR 并自动维护 Job？
13. Git 提交后如何通过 Webhook 自动触发 Jenkins CI？
14. Jenkins 常见触发器有哪些，如何选择触发策略？
15. Jenkins Controller/Agent 分布式构建架构如何协同工作？
16. Jenkins 高可用应该如何设计，Controller 故障恢复的边界是什么？
17. 大量 Jenkins Job 如何管理与优化，避免配置失控？
18. Jenkins 构建队列和并发调度机制怎么排查与优化？
19. Jenkins 大规模构建环境如何做容量、隔离和平台化治理？
20. 构建历史、日志、制品和 workspace 如何设置清理策略？
21. Jenkins 数据备份与恢复演练应该覆盖哪些内容？
22. Jenkins 凭据和敏感信息如何安全管理，避免在流水线中泄露？
23. Jenkins 用户权限、RBAC 和凭据隔离应该如何设计？
24. Jenkins 如何与 Docker 集成实现容器化 CI/CD？
25. Jenkins 如何通过参数化构建和配置管理支持多环境部署？
26. Jenkins 如何调用 Ansible 实现自动化配置管理和部署？
27. Jenkins 如何在上下游 Job 和多项目发布链路中传递参数、制品和状态？
28. Jenkins 如何集成 SonarQube 做代码质量扫描和质量门禁？
29. Jenkins 如何根据构建结果自定义通知和反馈链路？
30. Jenkins 构建失败时如何按阶段、日志、环境和依赖逐层排查？

## K8S（200 题）

1. Kubernetes 适合解决什么问题，哪些场景反而不该上 K8s？
2. 从功能和对象两个角度，如何说明 Kubernetes 的核心能力？
3. Kubernetes 对象模型和集群概念应该怎么讲清楚？
4. 云原生、不可变基础设施和宠物/牛模型与 K8s 有什么关系？
5. Kubernetes 和 Docker 是什么关系，常见部署方式怎么选？
6. Kubernetes 如何实现集群化管理，它的优势和边界是什么？
7. Kubernetes 的优势、短板和应用场景如何系统复盘？
8. 控制面和工作节点分别负责什么，核心组件怎么分工？
9. 从组件关系看 Pod 归属、kubelet 和控制面的职责边界是什么？
10. Worker 节点如何加入集群，架构图里应重点说明哪些组件？
11. Kubernetes 核心组件如何支撑高可用集群设计？
12. 生产环境里 K8s 控制面高可用应该怎么落地和验证？
13. kubectl 查询对象时背后的访问链路是什么？
14. 多集群场景下 kubectl 如何切换上下文和发现资源类型？
15. kubectl 发起创建或查询请求时 API Server 处理了哪些步骤？
16. 如何解读 kubectl 输出，并用 exec 与服务信息辅助排查？
17. 声明式管理和 kubectl exec 的工作机制怎么解释？
18. 实际排障中如何使用 kubectl exec，并区分命令式和声明式管理？
19. Kubernetes 各组件如何通过 API Server 通信，kubectl exec 又走哪条链路？
20. etcd 在 Kubernetes 中保存什么状态，一致性边界是什么？
21. 为什么通常只有 API Server 直接访问 etcd，业务数据该不该放进去？
22. 为什么 Kubernetes 选择 etcd，而不是普通 SQL 或 NoSQL？
23. etcd 性能调优应该关注哪些参数和指标？
24. Namespace、Label、Selector 和 Annotation 分别解决什么问题？
25. 生产中如何设计标签和选择器，避免 Service 或控制器选错对象？
26. Namespace 的隔离边界是什么，Annotation 和 Label 怎么区分？
27. 为什么不能只用 default 命名空间，Namespace 应该怎么规划？
28. 默认命名空间有哪些，删除 Namespace 会影响什么？
29. 如何查询和切换 Namespace，并理解它不等于网络隔离？
30. 跨命名空间访问资源时，作用域和查询方式要注意什么？
31. 如何确认当前 Namespace，以及 kube-public 这类命名空间的用途？
32. 命名空间内对象管理和跨命名空间资源清单怎么查？
33. 多团队环境下如何用 Namespace、Label 和 RBAC 做资源可见性治理？
34. 对象组织、标签选择和团队资源治理应该怎么设计？
35. Controller 的控制循环和期望状态机制是什么？
36. 控制循环在生产故障恢复中是如何工作的？
37. Pod 抽象、容器边界与创建建议在生产环境中怎么区分？
38. 多容器 Pod 有哪些典型协作模式，Pod 在调度和网络上有哪些硬边界？
39. Pause 容器在 Pod 内部扮演什么角色，Pod 的设计取舍如何影响生产选型？
40. Pod 的创建方式、YAML 结构和生命周期阶段分别是什么？
41. Pod 运行状态怎么验证，Pod 被删除时发生了什么？
42. 什么是静态 Pod，它的清单位置在哪，怎么正确删除？
43. 如何在实际集群中区分静态 Pod 和普通 Pod，它们的故障排查思路有何不同？
44. 如何用 kubectl 查询和过滤 Pod，多容器场景下怎么看日志？
45. Pod 日志排障有哪些常见场景，静态 Pod 的日志查看有何特殊之处？
46. 怎样在特定命名空间中创建和查找 Pod，标签如何将 Pod 和 Service 联动？
47. 命名空间内 Pod 创建、查找与服务联动在生产环境中如何落地和排查？
48. Pod 删除不是瞬时的——优雅终止窗口内发生了什么？Init Container 如何改变启动语义？
49. Init Container 反复失败、Pod 优雅删除卡住——生产排障的完整路径是什么？
50. Pod 创建全链路与生命周期钩子——从 YAML 提交到容器就绪，postStart 和 preStop 在何时介入？
51. Pod 删除卡住、生命周期钩子导致的滚动更新故障——如何从现象出发一步步定位？
52. Pod 出现的 Running 不等于可用——状态原因分类与 Init Container 的典型模式如何理解？
53. 生产 Pod 异常状态的系统性排查——从 STATUS 列出发，如何形成可复用的排障决策树？
54. Liveness 探针和 Readiness 探针的本质区别是什么？它们各自如何影响 Pod 的存活状态和 Service 流量？
55. 探针配置错误导致的线上事故——如何从信号、日志、Events 中快速定位 readiness/liveness 失败的根因？
56. Pod 的 restartPolicy 与探针方法（exec/httpGet/tcpSocket/gRPC）在生产中如何选型和组合？
57. 重启策略、探针方式与健康检查排障在生产环境中如何落地和排查？
58. Deployment、StatefulSet、ReplicaSet 和 ReplicationController 在机制上到底有什么区别？
59. 生产环境中怎么决策用 Deployment 还是 StatefulSet？选错了怎么发现和纠正？
60. 一次 Deployment 从创建到验证到编辑到删除，内部发生了什么？
61. Deployment 的创建、编辑、删除操作卡住或失败时怎么排查？
62. 如何排查和修复一个写错了的 Deployment 清单？副本声明有哪些常见错误？
63. 线上 Deployment 因为清单错误导致服务异常，如何应急和修复？
64. Deployment 扩缩容的内部机制是怎样的？ReplicaSet 在其中的角色是什么？删除操作如何级联？
65. 线上扩缩容操作出问题怎么排查？ReplicaSet 异常怎么定位？
66. ReplicaSet 从创建到维持副本的全过程是怎样的？默认副本和选择器有什么规则？
67. ReplicaSet 创建事件、默认副本与选择器规则在生产环境中如何落地和排查？
68. ReplicaSet 的标签漂移、孤儿 Pod 与级联删除的机制和边界是什么？
69. 生产环境中 ReplicaSet 标签不匹配的排查路径和必填字段校验是如何工作的？
70. ReplicaSet 的删除影响、标签漂移触发机制和状态验证在生产中如何操作？
71. ReplicaSet 与 Service 联动排障、清单修复和镜像验证的标准流程是什么？
72. 如何将 ReplicaSet 公开为 Service，以及 YAML 清单的常见错误怎么排查修复？
73. 生产环境下如何排查控制器链路——从 RS 状态异常到 Deployment 命令链的完整排障路径？
74. Deployment 与 ReplicaSet 的层级管理和 RC 的差异复盘——如何理解三层控制器模型？
75. 生产环境里如何验证控制器关系——Deployment 与 RS 的调谐机制及 RS 与 DaemonSet 的对比？
76. `kubectl create deployment` 背后的完整对象创建链路是什么？为什么有 RS 还需要 Deployment？
77. 工作负载控制器选型与副本管理复盘应该如何落地？
78. DaemonSet 解决了什么问题？它的工作方式和典型运维场景是什么？
79. StatefulSet、Job、CronJob 三者各自解决什么问题？它们的能力边界在哪里，什么场景下不能互相替代？
80. CronJob 在 YAML 清单中有哪些常见的配置风险？Job 和 CronJob 的差异如何指导批处理工作负载的选型？
81. Deployment 的升级过程是怎样工作的？RollingUpdate 和 Recreate 两种策略分别在什么场景下适用？maxSurge 和 maxUnavailable 如何控制滚动窗口？
82. Deployment 滚动更新卡住（stuck rollout）时，如何系统性地排查和恢复？
83. Deployment 回滚机制的底层原理是什么？蓝绿部署在 K8s 中如何实现，和滚动更新有什么区别？
84. K8s 中如何实现金丝雀发布？流量按照什么粒度拆分？有哪些实现方式，各自适用于什么场景？
85. 如何控制 Deployment 滚动更新的快慢？回滚操作有什么注意事项？滚动更新、蓝绿、金丝雀三种策略各自适合什么场景？
86. Helm 解决了 K8s 原生 YAML 管理的什么问题？Chart 的目录结构和模板引擎有什么价值？
87. Helm 作用、Chart 结构与模板价值在生产环境中如何落地和排查？
88. Helm 的部署、版本控制与发布管理的核心机制和边界是什么？
89. Helm Release 排障和生产落地中应该关注哪些关键环节？
90. Helm 的 Chart 查找、Values 覆盖、升级与回滚操作有哪些关键点？
91. Helm 日常操作命令在生产中如何落地与排障？
92. Kustomize 解决什么问题，它的 Base / Overlay 模式与 Helm 有什么本质区别？
93. Kustomize build 排障和生产落地中应该关注哪些关键环节？
94. Operator 模式解决了什么问题，它由哪些核心组件构成？
95. CRD 的定义结构、OLM 和 Operator 生命周期管理应该怎么讲？
96. Operator SDK / Operator Framework 有哪些组件，构建 Operator 的工具怎么选？
97. CRD 的使用场景、Operator 选型和 Kubernetes 扩展模式应该怎么系统复盘？
98. Scheduler 作用、过滤打分与调度流程的核心机制和生产边界是什么？
99. Scheduler 作用、过滤打分与调度流程在生产环境中如何落地和排查？
100. nodeName、自定义调度器与多调度器选择的核心机制和生产边界是什么？
101. nodeName、自定义调度器与多调度器选择在生产环境中如何落地和排查？
102. 节点亲和性 required/preferred 规则实践的核心机制和生产边界是什么？
103. 节点亲和性 required/preferred 规则实践在生产环境中如何落地和排查？
104. 污点、容忍度与 NoSchedule 故障修复的核心机制和生产边界是什么？
105. 污点、容忍度与 NoSchedule 故障修复在生产环境中如何落地和排查？
106. 调度方式、节点放置与约束策略复盘的核心机制和生产边界是什么？
107. 调度方式、节点放置与约束策略复盘在生产环境中如何落地和排查？
108. 资源限制目的、requests/limits 与容器边界的核心机制和生产边界是什么？
109. 资源限制目的、requests/limits 与容器边界在生产环境中如何落地和排查？
110. 资源请求配置、OOM 行为与不可压缩内存的核心机制和生产边界是什么？
111. 资源请求配置、OOM 行为与不可压缩内存在生产环境中如何落地和排查？
112. cgroup、QoS 等级与资源限制底层机制的核心机制和生产边界是什么？
113. cgroup、QoS 等级与资源限制底层机制在生产环境中如何落地和排查？
114. HPA 作用、自动扩容机制与实现链路的核心原理和生产边界是什么？
115. Metrics Server、资源指标与监控数据来源怎么讲清楚？
116. 生产环境中如何处理指标驱动扩缩容、采集链路与容量联动？
117. ResourceQuota 作用、创建方式与团队资源限制的核心机制和生产边界是什么？
118. ResourceQuota 作用、创建方式与团队资源限制在生产环境中如何落地和排查？
119. 对象数量配额、大规模集群容量与多租户治理应该如何落地？
120. Pending 原因、资源不足与调度失败排查应该如何排查和验证？
121. Evicted、大量驱逐与资源压力处理怎么讲清楚？
122. Service 概念、创建方式与基础暴露能力的核心机制和生产边界是什么？
123. Service 概念、创建方式与基础暴露能力在生产环境中如何落地和排查？
124. Service 类型、ClusterIP/NodePort/LoadBalancer 边界的核心机制和生产边界是什么？
125. Service 类型、ClusterIP/NodePort/LoadBalancer 边界在生产环境中如何落地和排查？
126. Endpoint、EndpointSlice 与后端关联机制的核心机制和生产边界是什么？
127. Endpoint、EndpointSlice 与后端关联机制在生产环境中如何落地和排查？
128. 服务发现、Headless Service 与 StatefulSet 依赖的核心机制和生产边界是什么？
129. 服务发现、Headless Service 与 StatefulSet 依赖在生产环境中如何落地和排查？
130. Service 公开、Pod/Service 联动与外部访问入口的核心机制和生产边界是什么？
131. Service 公开、Pod/Service 联动与外部访问入口在生产环境中如何落地和排查？
132. 负载均衡、服务发现与资源配额关联场景应该如何落地？
133. Service 功能、公开类型与 Endpoint 复盘应该如何落地？
134. kube-proxy 作用、Service 转发与负载均衡基础怎么讲清楚？
135. iptables、IPVS 模式与后端分发策略的核心原理和生产边界是什么？
136. kube-proxy 代理模式、规则修改与性能差异的核心机制和生产边界是什么？
137. kube-proxy 代理模式、规则修改与性能差异在生产环境中如何落地和排查？
138. iptables 负载均衡实现与 kube-proxy 功能复盘的核心原理和生产边界是什么？
139. Ingress 作用、Service 对比与外部访问路径的核心机制和生产边界是什么？
140. Ingress 作用、Service 对比与外部访问路径在生产环境中如何落地和排查？
141. Ingress 规则、Host、Backend 与通配符风险的核心机制和生产边界是什么？
142. Ingress 规则、Host、Backend 与通配符风险在生产环境中如何落地和排查？
143. Ingress Controller、默认后端与 TLS 配置的核心机制和生产边界是什么？
144. Ingress Controller、默认后端与 TLS 配置在生产环境中如何落地和排查？
145. 公网访问、Service/Ingress 差异与控制器选型的核心机制和生产边界是什么？
146. 公网访问、Service/Ingress 差异与控制器选型在生产环境中如何落地和排查？
147. Ingress 故障、客户端 IP 与上传限制处理应该如何排查和验证？
148. Gateway 迁移、Traefik 对比与入口流量演进在生产环境中怎么区分？
149. Pod DNS 解析流程与集群内服务寻址怎么讲清楚？
150. 网络模型、CNI 模型与 Flannel/Calico 基础的核心机制和生产边界是什么？
151. 网络模型、CNI 模型与 Flannel/Calico 基础在生产环境中如何落地和排查？
152. Calico、Flannel、Cilium 工作模式与选型的核心机制和生产边界是什么？
153. Calico、Flannel、Cilium 工作模式与选型在生产环境中如何落地和排查？
154. CRI/CNI/CSI 边界、运行时选择与网络插件复盘在生产环境中怎么区分？
155. NetworkPolicy 概念、默认连通性与流量控制对象怎么讲清楚？
156. 入口/出口策略、用例与冲突判定的核心原理和生产边界是什么？
157. 生产环境中如何处理 NetworkPolicy 原理、实现与使用场景复盘？
158. 应用不可访问、Pod 跨节点通信与连通性排查应该如何排查和验证？
159. Ingress 暴露失败与访问慢排查链路应该如何排查和验证？
160. 生产环境中如何处理 ConfigMap、Secret 作用与配置注入场景？
161. Secret 创建方式、类型与安全边界在生产环境中怎么区分？
162. 生产环境中如何处理 Secret 清单风险、Git 加密与 ConfigMap 用法？
163. 生产环境中如何处理 ConfigMap/Secret 使用方式与敏感信息治理？
164. 持久化存储、PV/PVC 与 Volume 边界的核心机制和生产边界是什么？
165. 持久化存储、PV/PVC 与 Volume 边界在生产环境中如何落地和排查？
166. PV 类型、可用性、PVC 与卷快照的核心机制和生产边界是什么？
167. PV 类型、可用性、PVC 与卷快照在生产环境中如何落地和排查？
168. StorageClass、动态供给与访问模式的核心机制和生产边界是什么？
169. StorageClass、动态供给与访问模式在生产环境中如何落地和排查？
170. CSI、回收策略与存储生命周期的核心机制和生产边界是什么？
171. CSI、回收策略与存储生命周期在生产环境中如何落地和排查？
172. 共享存储、数据持久化方式与 PV 生命周期的核心机制和生产边界是什么？
173. 共享存储、数据持久化方式与 PV 生命周期在生产环境中如何落地和排查？
174. 数据库上 K8s、常见存储方案与 CSI 复盘的核心机制和生产边界是什么？
175. 数据库上 K8s、常见存储方案与 CSI 复盘在生产环境中如何落地和排查？
176. Volume 基础、卷类型与容器间共享怎么讲清楚？
177. 临时卷、emptyDir、hostPath 与数据边界在生产环境中怎么区分？
178. RBAC、Role/RoleBinding 与 ClusterRole 边界的核心机制和生产边界是什么？
179. RBAC、Role/RoleBinding 与 ClusterRole 边界在生产环境中如何落地和排查？
180. ServiceAccount、用户账户与默认账户行为的核心机制和生产边界是什么？
181. ServiceAccount、用户账户与默认账户行为在生产环境中如何落地和排查？
182. 安全上下文、集群安全配置与最佳实践的核心机制和生产边界是什么？
183. 安全上下文、集群安全配置与最佳实践在生产环境中如何落地和排查？
184. Gatekeeper、Conftest、Datree 与策略校验的核心机制和生产边界是什么？
185. Gatekeeper、Conftest、Datree 与策略校验在生产环境中如何落地和排查？
186. 准入控制、PodSecurityPolicy 与服务网格边界在生产环境中怎么区分？
187. kubeconfig 内容、证书续签与访问凭据治理的核心机制和生产边界是什么？
188. kubeconfig 内容、证书续签与访问凭据治理在生产环境中如何落地和排查？
189. ContainerCreating、ErrImagePull 与镜像策略排查的核心机制和生产边界是什么？
190. ContainerCreating、ErrImagePull 与镜像策略排查在生产环境中如何落地和排查？
191. CrashLoopBackOff、Terminating 与频繁重启排查应该如何排查和验证？
192. kubelet 停止、节点 NotReady 与维护影响应该如何排查和验证？
193. 节点关机维护、磁盘压力与大文件定位怎么讲清楚？
194. K8s 日志管理、EFK 与日志采集方案的核心机制和生产边界是什么？
195. K8s 日志管理、EFK 与日志采集方案在生产环境中如何落地和排查？
196. 监控方案、关键指标与集群巡检怎么讲清楚？
197. Velero、PVC、etcd 与集群备份恢复怎么讲清楚？
198. AKS、集群联邦、KubeVirt 与多集群平台治理的核心机制和生产边界是什么？
199. AKS、集群联邦、KubeVirt 与多集群平台治理在生产环境中如何落地和排查？
200. K8s 运维最佳实践、服务验证与故障经验复盘应该如何排查和验证？

## LINUX（138 题）

1. Linux、发行版和 GPL 如何关联？
2. CPU 如何执行指令，补码和 MESI 解决什么问题？
3. Linux 内核负责什么，怎样查看版本和管理模块？
4. 用户态、内核态和硬件访问边界是什么？
5. 内核配置在编译、启动和运行阶段如何生效？
6. sysctl 如何查看、修改和持久化内核运行时参数？
7. 容器内修改内核参数会不会影响宿主机？
8. /proc 为什么是内核信息入口？
9. /sys、/dev 和 udev 如何表示设备？
10. Linux 从上电到 systemd 完成启动经历哪些阶段？
11. GRUB、/boot 和内核启动参数如何配合？
12. Secure Boot 如何保护启动链路？
13. FHS 目录结构中关键目录如何分工？
14. 如何查看 BIOS、CPU、内存和块设备信息？
15. Linux namespace 有哪些类型，隔离边界是什么？
16. cgroups 如何限制和统计资源？
17. KVM、QEMU 和 libvirt 如何组成 Linux 虚拟化栈？
18. 虚拟内存、地址空间、分页、分段和 swap 如何工作？
19. 常用 Linux 命令怎样按运维场景选择并解释输出？
20. 递归参数 -r/-R 会怎样影响文件操作？
21. `ls -l` 输出字段和隐藏文件应该怎么解释？
22. 命令路径、PATH 和 `command not found` 应该怎么排查？
23. 文件重命名、创建、删除和截断怎样避免误操作？
24. 管道如何组合命令并保留失败信号？
25. 标准输入、标准输出、标准错误和重定向怎么用？
26. 历史命令和退出码如何用于排障与脚本控制？
27. 通配符和 globbing 的匹配边界是什么？
28. `grep` 文本匹配和正则边界怎样用于日志排查？
29. Shell 引号、转义和双破折号怎样影响命令参数？
30. 环境变量、Shell 启动文件和 `cd -` 的行为怎么解释？
31. TTY、`man`、`info` 和帮助体系怎样用于命令确认？
32. alias、Shell 执行流程和通配符展开时机怎么说明？
33. `find`、`locate` 和文件定位命令应该怎么选？
34. `awk` 字段处理如何用于配置和日志分析？
35. `sed` 提取和批量替换怎样控制范围与风险？
36. 文件拆分、行数和词数统计怎么做才可靠？
37. 随机字符串、Base64 编码和解码在脚本中怎么用？
38. 远程复制和服务器间同步如何选择 `scp`、`rsync`、`tar`？
39. `dd`、`/dev/null` 和特定大小文件分别适合什么场景？
40. 文件权限、属主属组与 chmod/chown/chgrp 如何设计、修改和验证？
41. setuid、setgid 与 sticky bit 分别解决什么权限问题？
42. sudo、root 与超级用户权限如何授权、审计和收敛？
43. ACL 适合哪些场景，权限排查时如何确认它生效？
44. 创建文件失败和误执行 chmod -x 时如何定位并恢复？
45. umask 如何影响新建文件和目录的默认权限？
46. 用户、组的创建修改删除命令如何落地到账号文件？
47. 密码设置、/etc/shadow 与 root 密码恢复如何处理？
48. /etc/passwd 字段如何解释，账号异常怎么排查？
49. nologin、/etc/skel 与 UID 范围如何用于账号初始化？
50. su/root 切换与 UID 规则如何判断权限边界？
51. 登录用户查看与审计如何定位异常会话？
52. 如何查看、筛选和管理线上进程？
53. 进程、线程和协程在 Linux 上有什么区别？
54. 进程状态、D 状态和不可中断等待怎么排查？
55. 僵尸进程如何产生，应该怎么处理？
56. Daemon、init 和 1 号进程分别负责什么？
57. systemd 服务管理和自定义 unit 如何落地？
58. 业务高峰期如何安全重启服务？
59. crontab 定时任务无法执行怎么排查？
60. 信号、kill、trap、Ctrl-C 和后台任务怎么理解？
61. 进程优先级、CFS 和调度算法怎么回答？
62. fork、wait、exec 和进程创建流程是什么？
63. 系统调用如何让用户进程执行特权操作？
64. 文件和目录相关系统调用如何串起 `ls`、读文件和执行程序？
65. 文件描述符、打开文件数和线程上限怎么排查与调整？
66. pipe 和 Linux 进程间通信方式怎么选？
67. 上下文切换和线程切换会带来什么开销？
68. task_struct、进程描述符和内核线程是什么？
69. socket 调用和网络连接生命周期如何串起来？
70. lsof 如何定位文件、端口和 deleted 文件占用？
71. 运行中脚本被删除和误删除文件如何恢复？
72. 动态链接库缺失和 ldd 排查怎么做？
73. CUPS、Web Server 和应用服务类型如何归入服务管理？
74. malloc 返回值和进程地址空间有什么关系？
75. inode、block 与目录链接计数怎样影响容量和排障？
76. 软链接与硬链接在生产中怎样使用和验证？
77. 如何查看挂载信息、df 输出和文件系统类型？
78. 磁盘分区、MBR/GPT 和分区管理怎样安全操作？
79. ext4、XFS 与日志文件系统如何选型和维护？
80. Swap、交换分区与 tmpfs 分别解决什么问题？
81. 磁盘空间满、inode 满与 df/du 不一致如何排查？
82. du 统计目录大小时怎样避免误判？
83. LVM 如何划分、扩容和验证？
84. RAID 0、1、5、6、10 怎样选择和排障？
85. NFS、df 卡住与 lazy umount 应该怎样处理？
86. fsck、只读文件系统与启动恢复如何处理？
87. 磁盘配额如何限制用户、组或目录容量？
88. 线上新增硬盘或扩容已有磁盘的完整流程是什么？
89. Linux 文件读写流程与存储排障怎样关联？
90. SSH 远程登录、密钥、known_hosts 与隧道如何排查？
91. 静态 IP、nmcli 与主机名配置如何落地并验证？
92. 接口、lo、MAC 与基础网络命令如何解释？
93. 路由表、默认网关与 Linux 路由器如何配置和排查？
94. DNS 解析、resolv.conf 与解析失败如何排查？
95. 端口监听、连接列表与 ss/netstat 如何使用？
96. TCP 统计、TIME_WAIT、conntrack 与端口耗尽如何分析？
97. 丢包、抓包与 traceroute 如何定位链路问题？
98. iptables、nftables、firewalld 与 NAT 如何理解和排障？
99. 网络命名空间如何打通连通性？
100. VIP、bonding、bridge 与 Keepalived 如何保障高可用网络？
101. telnet、HTTP 请求与 FTP 工作模式有哪些网络边界？
102. IPv6 邻居发现如何触发和排查？
103. Select/Poll/Epoll、I/O 模型与 Reactor 如何关联到高并发网络服务？
104. NTP 时间同步为什么影响运维排障？
105. 常用性能分析诊断命令如何按资源维度使用？
106. top/htop 中哪些字段能快速判断资源瓶颈？
107. load average、CPU 使用率和高负载如何区分？
108. Linux 系统 CPU 持续飙高如何定位？
109. 用户反馈“系统很慢”时怎样建立排障证据链？
110. iostat、磁盘 I/O 和 iowait 高如何排查？
111. free、/proc/meminfo、Buffer/Cache 和进程内存如何解读？
112. 内存泄漏、JVM 内存和系统内存持续升高如何排查？
113. OOM Killer 与进程被杀如何排查？
114. 如何测量程序执行时间并解释 real、user、sys？
115. strace、ltrace 和二进制调试如何定位程序问题？
116. eBPF、BCC 和线上观测工具适合解决什么问题？
117. 软中断、硬中断和网络软中断高如何分析？
118. Linux 服务器调优应该从哪些证据开始？
119. 监控系统应该覆盖哪些对象和指标？
120. 数据库服务器 load 100+ 能不能直接重启？
121. 系统日志位置、常见日志与日志管理如何落地？
122. journalctl、dmesg 与 tail 实时跟踪如何取证？
123. SELinux 机制与作用如何排查和验证？
124. Kerberos 认证机制如何解释和排障？
125. CA 私钥、公钥与证书基础如何管理？
126. 服务器加固、数据安全与运维安全怎么做？
127. chroot 隔离场景如何使用和限制？
128. 包管理器、DNF/YUM/APT 与安装删除如何落地？
129. RPM spec 与软件包构建要关注哪些字段和风险？
130. 包内容、文件归属和仓库查询怎么排查？
131. 归档创建、提取与包管理边界怎么把握？
132. 批量服务器管理、自动化和旧服务器下线怎么做？
133. SRE 理念、效率提升与核心工作如何回答？
134. 上线网站时如何设计高可用、高并发架构？
135. 故障经历、复盘和团队接手怎么讲得可信？
136. Paxos/Raft 与分布式一致性在运维中解决什么问题？
137. CDN 刷新后如何验证资源真的生效？
138. Bug 分歧沟通与线上问题推进怎么处理？

## MIDDLEWARE（25 题）

1. 什么时候应该引入消息中间件，生产上要同步补哪些治理能力？
2. Kafka、RabbitMQ、RocketMQ 在运维选型上怎么取舍？
3. Kafka 的事件流定位和适用场景应该怎么讲？
4. Kafka 核心组件和常用术语如何串成一条完整数据链路？
5. Broker 在 Kafka 集群中承担哪些职责，故障时会影响什么？
6. Topic、Partition、Replica 三者关系如何影响吞吐、顺序和容灾？
7. Producer 写入客户端需要关注哪些分区、可靠性和吞吐参数？
8. ZooKeeper 模式和 KRaft 模式下 Kafka 控制面有什么差异？
9. Kafka 从 Producer 到 Broker 的写入链路如何描述？
10. Kafka 的 `acks=0/1/all` 如何在吞吐和可靠性之间取舍？
11. Kafka 的消息在磁盘上如何组织，保留策略如何影响运维？
12. Kafka 为什么吞吐高，调优时不能只盯零拷贝？
13. 为什么 Kafka 通常不采用传统主写从读的读写分离？
14. Kafka 如何降低消息丢失风险，同时为什么还要处理重复消费？
15. ISR、AR、OSR 分别是什么，ISR 伸缩对生产写入有什么影响？
16. Follower 如何与 Leader 同步数据，HW/LEO 在复制中起什么作用？
17. Kafka 分区 Leader 选举如何在可用性和数据安全之间取舍？
18. Consumer Group 如何实现并行消费和故障接管？
19. Kafka Rebalance 什么时候触发，生产上如何降低它的影响？
20. Kafka 消息堆积时如何定位瓶颈并安全恢复？
21. RabbitMQ 普通集群、镜像队列和仲裁队列如何选型？
22. RabbitMQ 仲裁队列的 Leader/Follower 和多数派确认如何工作？
23. RabbitMQ 消息堆积时如何区分 ready 和 unacked 并恢复？
24. RocketMQ 常见集群部署模式如何影响可用性和数据可靠性？
25. 多主多从加 DLedger 的写入复制和故障切换流程是什么？

## MYSQL（100 题）

1. 数据库类型、关系数据库和 SQL 的基础边界是什么？
2. SQL 和 NoSQL 在生产选型中怎么比较？
3. 如何评价 MySQL 的产品定位以及和 Oracle、国产数据库的差异？
4. 什么是 OLTP，MySQL 在在线事务场景中承担什么角色？
5. OLAP、数据仓库和 MySQL OLTP 库应该如何分工？
6. 时间序列数据库适合什么场景，和 MySQL 有什么边界？
7. ORM 能解决什么问题，为什么仍要理解 SQL 和 MySQL 执行细节？
8. 数据库规范化和三大范式在 MySQL 表设计中如何取舍？
9. 主键、外键和逻辑外键在生产 MySQL 中如何选择？
10. MySQL 建表设计需要重点检查哪些维度？
11. DDL 是什么，线上 MySQL 结构变更为什么要谨慎？
12. 逻辑删除、DELETE、TRUNCATE 和 DROP 在 MySQL 中有什么区别？
13. MySQL 字段类型如何选择，金额为什么不应使用浮点数？
14. CHAR、VARCHAR 以及 VARCHAR 长度在 MySQL 中如何取舍？
15. DATETIME、TIMESTAMP、TEXT、AUTO_INCREMENT 和单表列数有哪些边界？
16. 为什么不建议把大文件直接存 MySQL，中文乱码如何排查？
17. 视图、游标和存储过程在 MySQL 中应该怎么用？
18. 一条 SQL 从逻辑执行顺序到 MySQL 内部执行链路怎么讲？
19. 基础 SELECT 查询为什么也要避免 SELECT *？
20. MySQL ORDER BY 是如何执行的，什么时候会 filesort？
21. COUNT、SUM 等聚合统计在 MySQL 中有哪些语义和性能边界？
22. EXISTS 和 IN 在 MySQL 中如何选择？
23. INNER JOIN、LEFT JOIN、RIGHT JOIN 的差异和写法要点是什么？
24. 笛卡尔积和复杂多表 JOIN 在生产中有什么风险？
25. WITH/CTE 在 MySQL 复杂查询中适合解决什么问题？
26. MySQL 常用函数怎么分类使用，为什么函数也可能拖慢 SQL？
27. 数据库游标、Cursor 分页和深度分页优化有什么区别？
28. 运维脚本连接 MySQL 查询时要注意什么？
29. MySQL 索引的作用和常见类型如何系统回答？
30. MySQL 索引管理和全文索引与其他数据库有什么差异？
31. 创建 MySQL 索引时应该按什么原则评估？
32. 哪些场景不适合给 MySQL 字段建索引？
33. 联合索引的最左前缀原则如何影响查询、排序和范围条件？
34. 为什么 MySQL InnoDB 主要选择 B+ 树做索引？
35. 三层 B+ 树能存多少数据，一次索引查询如何走完整路径？
36. InnoDB 聚簇索引和非聚簇索引有什么区别？
37. MySQL 回表是什么，如何降低回表成本？
38. 覆盖索引如何避免回表，设计时有什么取舍？
39. Index Condition Pushdown 是什么，为什么能减少回表？
40. 使用索引一定有效吗，如何排查索引没有按预期生效？
41. MySQL 索引是不是越多越好，过多索引有什么代价？
42. 二级索引里有没有完整 MVCC 快照，查询如何判断可见性？
43. ACID 四个特性在 MySQL/InnoDB 中分别如何体现？
44. MySQL 隔离级别有哪些，生产为什么常在 RR 和 RC 间取舍？
45. 脏读、不可重复读和幻读分别是什么，MySQL 如何处理？
46. InnoDB 是如何实现事务的？
47. redo log 和 binlog 的二阶段提交为什么必要？
48. MVCC、ReadView 和 undo 版本链如何支撑并发读写？
49. MySQL 长事务会造成哪些生产问题？
50. MySQL 常见锁类型和表锁、行锁、间隙锁如何区分？
51. 乐观锁和悲观锁在 MySQL 中怎么实现？
52. MySQL 死锁为什么发生，线上如何处理？
53. MySQL 常见存储引擎怎么选，为什么生产默认 InnoDB？
54. InnoDB 和 MyISAM 至少从哪些方面比较？
55. InnoDB 的核心特性如何系统说明？
56. MySQL 读数据一定从磁盘吗，Buffer Pool 有什么作用？
57. Change Buffer 是什么，为什么主要作用于二级索引写入？
58. Doublewrite Buffer 如何解决页部分写问题？
59. Log Buffer 在事务提交和 redo 写入中起什么作用？
60. WAL 思想和 MySQL redo log 分别解决什么问题？
61. binlog 有什么作用，STATEMENT、ROW、MIXED 如何选择？
62. MySQL 常见日志有哪些，分别用于什么场景？
63. InnoDB 表空间是什么，系统表空间和独立表空间有什么运维意义？
64. 用户访问慢时如何判断是不是 MySQL 瓶颈并排查慢查询？
65. MySQL 查询优化和 SQL 调优有哪些常用方法？
66. MySQL 优化器如何选择执行计划，为什么有时选错索引？
67. 如何用 EXPLAIN 读懂 MySQL 执行计划？
68. 如何建立慢 SQL 监控、分析和优化闭环？
69. 数据库连接池和连接泄漏会如何影响 MySQL？
70. SHOW PROCESSLIST 能排查哪些 MySQL 问题？
71. performance_schema 在 MySQL 排障中有什么作用？
72. MySQL 大量 Sleep 线程是什么原因，怎么治理？
73. MySQL 运维一般监控哪些指标？
74. MySQL CPU 飙升到很高时如何定位和应急？
75. 高并发场景下 MySQL 如何系统优化？
76. 分片、分库分表和分区分别解决什么问题？
77. 如果主导分库分表项目，实施流程怎么设计？
78. 分库分表会引入哪些新问题？
79. 全量同步和增量同步如何组合用于迁移和数仓链路？
80. CDC 是什么，MySQL 基于 binlog 的 CDC 如何工作？
81. 多线程同步 MySQL 数据到数仓时要注意什么？
82. MySQL 批量入库和导入导出如何提高效率并控制风险？
83. TB 级 MySQL 如何做不停服在线迁移？
84. MySQL 主从复制原理和基础配置步骤是什么？
85. 异步复制、半同步复制和同步语义有什么区别？
86. 主从复制常见问题和延迟如何处理？
87. 如何判断 MySQL 主从延迟，Seconds_Behind 是否可靠？
88. 主从数据一致性如何校验和修复？
89. MySQL 主从模式如何尽量保证强一致性，代价是什么？
90. MySQL 读写分离如何实现，最大风险是什么？
91. MySQL 如何避免单点故障，主流高可用方案有哪些？
92. MHA 的故障切换原理是什么？
93. MySQL Group Replication 的工作原理是什么？
94. InnoDB Cluster 由哪些组件组成，和 MGR 有什么关系？
95. 一主多从中从库宕机或复制中断如何恢复？
96. MySQL 备份方案如何设计，恢复流程怎么验证？
97. XtraBackup 全量、增量备份和恢复原理是什么？
98. 误执行 DROP 后如何用备份和 binlog 恢复？
99. MySQL 用户权限管理和安全加固有哪些要点？
100. MySQL root 密码忘记后如何安全重置？

## NETWORK（68 题）

1. IP 地址、子网和私有地址在主机通信中分别解决什么问题？
2. 公网地址、DHCP 分配流程和多 DHCP 场景怎么解释？
3. IPv6、APIPA 和地址自动配置在故障现场怎么判断？
4. MAC、广播 MAC、ARP/RARP 和 ARP 欺骗的关系是什么？
5. 从一次跨网段访问看 MAC 和 IP 如何配合转发？
6. OSI 七层和 TCP/IP 四层模型怎样对应到真实协议栈？
7. TCP/IP 协议栈中封装、解封装和层间职责如何工作？
8. 如何用分层思维解释常见 TCP/IP 协议和排障路径？
9. 以太网、CSMA/CD、ICMP 和常见端口在运维中怎么用？
10. 一次网络通信需要哪些条件，为什么不能把可靠性都放在 IP 层？
11. MTU、分片、差错控制和应用层协议边界怎么解释？
12. 互联网、万维网、ISP、网络层协议和 MTU 问题如何联系到生产访问？
13. TCP 如何保证可靠传输，拥塞控制和超时重传分别解决什么？
14. TCP 滑动窗口、SACK、快速重传和连接容量怎么理解？
15. TCP 粘包拆包、网络拥塞和指数退避在真实服务中怎么处理？
16. TCP 三次握手、四次挥手、RST 和 TIME_WAIT 的核心逻辑是什么？
17. SYN 后宕机、ISN 选择和非 FIN 断开连接怎么分析？
18. 生产中如何配置和观察 TCP 握手、挥手与 TIME_WAIT？
19. TCP 各状态在网络排障中分别提示什么问题？
20. TCP 和 UDP 的差异、RTT 与套接字语义怎么解释？
21. 怎样选择 TCP/UDP，并纠正常见的 ping、报文格式和 socket 误区？
22. Cookie、Session、JWT Token 等登录鉴权方式如何选型和排障？
23. HTTP/1.0、HTTP/2 和 HTTP/3 的关键差异是什么？
24. HTTP 请求由哪些部分组成，GET/POST 和状态码如何回答？
25. 服务端如何解析 HTTP 请求，遇到 HTTP 错误码怎么定位？
26. HTTPS/TLS 握手如何保证身份、加密和完整性？
27. SSL 隧道、TLS 终止和 HSTS 在入口架构中怎么落地？
28. 长连接、短连接和 WebSocket 的区别及适用场景是什么？
29. CDN 如何加速访问，运维需要关注哪些缓存和回源边界？
30. DNS TTL、IP TTL、区域类型和 DNS 负载均衡分别是什么？
31. DNS、名称服务器、注册商和根域在解析链路中各自负责什么？
32. 如何拆解 FQDN，并用它定位域名委派和解析问题？
33. DNS 解析工作流和记录类型的基础框架是什么？
34. A、AAAA、CNAME、MX、NS、TXT 等 DNS 记录如何选择？
35. AAAA、CNAME、PTR 记录配置时容易踩哪些坑？
36. MX、NS 和杂项 DNS 问题如何排查到权威边界？
37. DNS 使用 TCP 还是 UDP，区域和记录在生产变更中如何整体复盘？
38. 正向代理、反向代理在网络入口链路中有什么区别？
39. NAT 的工作原理是什么，它在家庭路由器和云网络中解决什么问题？
40. SNAT 在 Linux 和云出口中怎么配置、验证和排障？
41. SDN 中控制平面、数据平面、管理平面分别负责什么？
42. GRE、VXLAN 等覆盖网络和 Spine-Leaf 架构如何支撑数据中心网络？
43. 交换机、VLAN、拓扑、冲突域和广播域的基础关系是什么？
44. 广播域、VLAN 和 STP 如何防止二层网络失控？
45. 交换机转发、链路聚合和 VLAN 故障如何在现场排查？
46. 路由器、默认网关、路由表和非对称路由如何影响转发？
47. Linux 添加路由、traceroute 原理和转发路径排查怎么做？
48. 静态路由、动态路由、OSPF 和 BGP 的适用边界是什么？
49. Keepalived 和 VRRP 如何实现 VIP 高可用？
50. Keepalived 脑裂为什么发生，如何预防和处理？
51. 负载均衡有什么作用，LVS 和 DNS 负载均衡算法如何理解？
52. LVS 由哪些组件和术语组成，为什么性能高？
53. LVS-NAT 和 LVS-DR 模式的原理、特性和配置要点是什么？
54. LVS 三种模式、调度算法和与 Nginx 的差异如何排障说明？
55. LVS、Nginx、HAProxy 等负载均衡实现该如何选型？
56. SYN Flood 和 ARP 欺骗分别攻击哪一层，如何防护？
57. VPN 和 IPSec 如何工作，运维要排查哪些隧道问题？
58. 防火墙基本原理是什么，Linux iptables 和 Windows 规则如何配置排查？
59. QoS 在网络中解决什么问题，如何配置和验证流量保障？
60. 延迟、带宽、吞吐量和影响网络性能的因素如何区分？
61. 搜索查询和视频上传场景中，延迟与吞吐量哪个更重要？
62. Linux 中如何配置和查看网络接口、路由与连接状态？
63. Linux 服务器网络不通、丢包和网络慢应该如何分层排查？
64. SNMP 的工作原理是什么，网络设备监控如何落地？
65. Windows 中如何检查网络连接、防火墙和端口状态？
66. ping 和 traceroute 的原理是什么，如何用于网络故障排查？
67. 如何用 tcpdump 抓指定主机和端口，并分析抓到的数据包？
68. 常用网络故障排查工具如何组合成一条完整排障链路？

## NGINX（75 题）

1. Nginx 在生产架构里解决什么问题，边界在哪里？
2. Nginx、Apache 和 Tomcat 在架构选型上怎么区分？
3. Nginx 版本如何选择，生产升级流程怎么做？
4. Nginx 常用模块有哪些，分别解决什么问题？
5. Nginx 为什么能抗高并发，和 C10K 问题有什么关系？
6. Nginx 的 IO 事件模型、epoll 和惊群问题怎么解释？
7. Nginx 为什么采用多进程模型，而不是每连接一个线程？
8. Nginx master 和 worker 进程分别负责什么？
9. 一个 HTTP 请求进入 Nginx 后会经历哪些处理阶段？
10. Nginx 目录结构和 nginx.conf 上下文应该怎么掌握？
11. Nginx 常用命令和 `-s` 信号如何安全使用？
12. 如何用 include 管理多虚拟主机配置？
13. Nginx 虚拟主机、server_name 和非默认端口如何配置？
14. 如何阻断未定义域名或直接 IP 访问？
15. location 匹配优先级怎么判断，如何做精准匹配？
16. root 和 alias 有什么区别，静态资源如何正确配置？
17. try_files 如何做静态文件和应用路由回退？
18. Nginx rewrite 规则和 flag 如何使用，和 Apache 有什么边界？
19. URL 重定向、301/302 和地址栏保持怎么区分？
20. Nginx 常用变量怎么用，如何在日志或配置里取值？
21. Nginx 如何处理 URL 双斜杠，什么时候需要保留？
22. Nginx 如何按语言做内容分发或国际化入口？
23. 正向代理和反向代理有什么区别，Nginx 常用在哪里？
24. proxy_pass 怎么配置，后面加斜杠和不加斜杠有什么区别？
25. 反向代理时如何正确透传客户端信息和自定义 Header？
26. 如何通过 Nginx 处理前端跨域和预检请求？
27. Nginx 如何代理 WebSocket，关键 Header 是什么？
28. 如何通过 Nginx 提供安全的 WSS 连接？
29. Nginx 代理超时有哪些，如何影响 502/504？
30. Nginx resolver 有什么作用，动态 DNS 上游怎么配置？
31. Nginx 支持哪些协议，HTTP/2 如何与代理协同？
32. Nginx 如何用 upstream 配置负载均衡？
33. Nginx 支持哪些负载均衡算法，适用场景是什么？
34. ngx_http_upstream_module 如何支撑反向代理和负载均衡？
35. ip_hash、url_hash 和会话保持应该怎么选？
36. Nginx 如何发现和处理后端服务故障？
37. Nginx stream 如何做四层代理，和七层代理有什么区别？
38. Nginx 和 LVS 在负载均衡架构里怎么分工？
39. Nginx 服务高可用应该怎么设计？
40. Nginx 如何实现灰度发布和按比例导流？
41. Nginx 如何配置静态文件缓存和过期策略？
42. proxy_cache 和 fastcgi_cache 分别怎么用，风险是什么？
43. Nginx gzip 如何启用，哪些参数最关键？
44. 开启压缩有哪些收益和副作用，如何选择策略？
45. Nginx 是否会把客户端请求体压缩后再转发上游？
46. sendfile、tcp_nopush 对静态文件传输有什么作用？
47. Nginx 如何实现动静分离，收益和边界是什么？
48. Nginx 如何配置访问控制和 IP 黑白名单？
49. 如何禁止敏感目录访问并配置防盗链？
50. Nginx 常见安全加固和爬虫限制怎么做？
51. Nginx 如何配置限流，能解决什么问题？
52. 如何限制单个 IP 的请求频率？
53. 如何限制每个 IP 的并发连接数？
54. Nginx 限流底层机制和常见算法怎么理解？
55. Nginx 如何配置 HTTPS，生产要关注哪些安全项？
56. worker_processes、worker_connections 和连接上限如何估算？
57. keepalive 如何影响连接复用和长请求处理？
58. Nginx 性能优化应该按什么方法论推进？
59. 哪些 Linux 内核参数会影响 Nginx 容量？
60. Nginx FastCGI 参数如何优化，PHP-FPM 场景要看什么？
61. proxy_buffering 有什么作用，什么时候关闭？
62. 上传文件过大或请求体缓冲问题怎么处理？
63. Nginx access_log 和 error_log 如何配置才利于排障？
64. 如何用 stub_status 观察 Nginx 运行状态？
65. 如何从 Nginx 日志统计 Top IP 和高频访问 IP？
66. 如何统计热点页面和响应内容总大小？
67. 如何按状态码统计异常 IP 和每个 IP 的状态分布？
68. Nginx 常见状态码应该如何理解？
69. 500、502、503、504 在 Nginx 场景中怎么区分？
70. Nginx 502 Bad Gateway 常见原因和排查步骤是什么？
71. Nginx 499 状态码常见原因是什么，怎么排查？
72. Nginx 403 Forbidden 常见原因和排查步骤是什么？
73. Nginx error_page 如何定义错误页和替换错误码？
74. OpenResty 和 Lua 能给 Nginx 带来什么能力？
75. Nginx 如何新增模块，静态编译和动态加载有什么区别？

## OTHER（50 题）

1. 如何用 Windows 任务管理器做进程初筛，并判断何时升级到生产可观测性工具？
2. Linux 与 Windows 软件安装卸载在包管理、自动化和验证上有什么差异？
3. 如何配置跨平台环境变量，并验证 JAVA_HOME 与 Path 是否真正生效？
4. Windows 与 Linux 的虚拟内存机制有哪些差异，运维调优时该看什么？
5. Windows 磁盘分区、清理和系统优化如何做才不影响业务？
6. Windows 用户账户、用户组和命令行管理如何兼顾权限与审计？
7. Windows 注册表的结构、作用和排障使用边界是什么？
8. Windows 设备驱动程序如何安装、更新、回滚和控制变更风险？
9. Windows 计划任务如何可靠运行脚本，并排查没有执行的问题？
10. 如何用事件查看器串起一次 Windows 常见故障排查？
11. Windows 命令行如何排查磁盘问题并保护数据？
12. Windows 蓝屏和 BSOD 应该按什么步骤排查？
13. Windows 应用程序崩溃如何定位到配置、依赖、权限或代码问题？
14. Python 文件读取脚本如何处理编码、路径和异常，避免在线上静默失败？
15. Python 做文件复制、移动和批量重命名时，如何设计 dry-run、日志和回滚？
16. Python 如何遍历目录并统计大小，同时处理权限、符号链接和大目录性能？
17. Python requests 做 HTTP 请求和定时抓取时，如何处理超时、重试和内容校验？
18. Python subprocess 执行外部命令时，如何避免注入、卡死和误判成功？
19. argparse 如何把运维脚本做成可维护的命令行工具？
20. Python logging 如何让运维脚本具备可观测性，而不是只靠 print？
21. Python 读写 JSON 配置或接口数据时，如何处理格式、编码和兼容性？
22. Python 多线程如何提升 I/O 型运维脚本效率，GIL 和线程安全边界是什么？
23. 如何用 Python 设计一个可恢复、可校验的增量备份脚本？
24. Python 简单 HTTP 服务器适合哪些调试场景，为什么不能直接当生产服务？
25. Python TCP 客户端和服务器如何处理连接、超时、粘包和关闭？
26. Python pandas 处理 CSV 运维报表时，如何兼顾清洗、性能和数据质量？
27. Python asyncio 适合哪些运维自动化场景，和多线程如何取舍？
28. Python smtplib 发送邮件告警时，如何处理 TLS、认证、附件和失败重试？
29. Python 解析 XML 时，如何处理命名空间、不可信输入和配置变更？
30. Python 图像处理脚本在批处理场景中如何处理格式、尺寸和失败文件？
31. Puppet 如何管理多台服务器配置，声明式收敛模型的价值是什么？
32. Puppet Manifest 是什么，如何用资源声明表达服务期望状态？
33. Puppet Hiera 如何做分层数据管理，为什么它能减少配置硬编码？
34. Puppet Facter 如何采集节点事实，并影响节点分类和配置渲染？
35. Puppet 代码组织和 Class 分级系统如何支撑大规模配置治理？
36. Chef 的工作流程是什么，它如何完成配置管理和节点收敛？
37. Chef Cookbook、Recipe、Resource 和 Provider 分别是什么，如何保证幂等？
38. Chef Node 和 Environment 如何表达节点差异、版本约束和环境隔离？
39. 如何用 Chef 实现一次可验证、可回滚的应用自动化部署？
40. MongoDB 作为文档数据库的定位是什么，BSON 模型对运维有什么影响？
41. MongoDB 的优势和适用场景如何表达，哪些场景不建议使用？
42. MongoDB 备份与恢复如何设计，如何保证备份真的可用？
43. MongoDB 分片机制如何工作，分片键选择和扩容风险有哪些？
44. 面试中如何表达当前业务规模和个人负责边界，既具体又不夸大？
45. 平时如何学习新技术，并把近期研究方向讲成可验证的能力？
46. 如何讲一个有意义的运维工作案例，并体现对公司的真实价值？
47. 你如何看待运维发展方向和日常工作重点？
48. 与上级意见不一致时，运维如何沟通风险并推动可执行方案？
49. 面试中如何表达个人优点、缺点和改进闭环，避免模板化？
50. 如何回答“相比其他候选人，你的核心竞争力是什么”？

## PROCESS（79 题）

1. 如何建设一套能支撑稳定交付的运维保障体系？
2. 如何设计变更、发布和上线流程，避免一次发布拖垮服务？
3. 如何把权限申请和日常操作规范落到最小权限和可审计？
4. 巡检发现问题后，如何通过工单和 SLA 做到闭环治理？
5. CMDB 应该如何建模，才能真正支撑排障、发布和审计？
6. 运维、开发、测试、安全和业务之间的责任边界怎么划？
7. 如何提升运维效率，同时控制自动化误操作和 Toil？
8. SRE 和传统运维的核心差异是什么，如何落到工程实践？
9. 如何设计 SLI/SLO/SLA，并用自动化率衡量运维成熟度？
10. 错误预算如何影响发布节奏、可靠性投入和成本控制？
11. 如何治理监控告警，让覆盖率和准确率都能被衡量？
12. 如何在不牺牲稳定性的前提下提升资源使用率并降本？
13. 面对稳定性和新技术试点冲突，SRE 应该如何决策？
14. 生产故障从发现到复盘，完整处理链路应该怎么讲？
15. 人为误操作造成故障时，如何止损、恢复和预防复发？
16. 事件分级、故障指挥和升级路径应该如何设计？
17. 应急响应和备份恢复如何一起保障 RTO/RPO？
18. 如何用日志证据链还原故障，并把复盘改进落到闭环？
19. DevSecOps 如何从口号变成安全运维闭环？
20. FIPS 兼容意味着什么，生产系统如何验证安全控制？
21. 如何用 CVE/CVSS 建立漏洞、威胁和风险治理链路？
22. 如何把安全情报转成可执行的安全架构基线？
23. 零信任、最小权限和 RBAC 在运维接入中如何落地？
24. 认证、授权和认证因素应该如何区分并落到系统设计？
25. 令牌认证和风险自适应认证如何降低会话被盗风险？
26. SSO 和 Kerberos 在企业身份集成中如何工作？
27. MFA 与 OAuth 分别解决什么问题，边界在哪里？
28. 敏感信息、密码攻击和加盐哈希应如何统一治理？
29. Cookie 会话认证为什么是有状态机制，生产中如何保护？
30. SSH 如何建立安全连接，密钥治理要管哪些风险？
31. HTTPS/TLS 的证书信任链在生产中如何工作？
32. 对称加密和非对称加密如何配合，常见误区有哪些？
33. 密钥交换和前向保密如何保护会话密钥？
34. 哈希和加密的区别与各自适用场景？为什么哈希不能解密、可信来源还需要签名？
35. SSH 如何组合非对称认证、对称加密和哈希来建立安全连接？
36. TLS 终止和 SNI 如何工作？设计时要考虑哪些风险（后端链路加密、证书轮换、真实客户端 IP、reload）？
37. Nonce 如何防重放，生产协议中应该如何使用？
38. 如何用 OWASP Top 10 指导 Web 安全治理？
39. XSS 和 CSRF 的攻击面有什么不同，如何防护？
40. SQL 注入如何产生，生产中如何治理到位？
41. 格式化字符串和缓冲区溢出漏洞为什么危险？
42. HTTP 头注入和 SSRF 如何突破服务端信任边界？
43. 缓存投毒、缓存 DoS 和 Web 缓存欺骗如何治理？
44. 防火墙和 DMZ 如何构建边界隔离，而不是制造安全幻觉？
45. DDoS 和端口洪水应该如何分层防护和应急？
46. 端口扫描如何用于攻击面发现，授权边界怎么控制？
47. 中间人、ARP 和 DNS 欺骗如何劫持流量，如何防护？
48. TCP/UDP 风险、VLAN 和气隙网络如何看待边界隔离？
49. MAC 洪水攻击如何影响交换网络，二层安全怎么做？
50. APT 和后门风险如何被发现、遏制和清除？
51. 如何从 Stuxnet、BootHole 和 Spectre 提炼安全治理经验？
52. 软件供应链治理为什么是稳定交付的一部分？
53. 第三方包和开源依赖如何被攻击者利用？
54. 包管理器和构建工具在交付链路中承担什么信任责任？
55. 依赖膨胀会带来哪些风险，如何治理？
56. 如何选择可信包，并用签名、校验和验证完整性？
57. 公共代码仓库如何防止凭证泄露和供应链污染？
58. 为什么需要微分割，传统防火墙为什么不够？
59. 微分割策略如何适配临时环境和动态工作负载？
60. 微分割如何阻断横向移动，规模化时难点在哪里？
61. 敏捷、看板和 Scrum 如何影响运维与研发协作？
62. DevOps 自动化任务应该如何选择编程语言？
63. OOP、组合和四大支柱在运维平台代码中如何应用？
64. SOLID、YAGNI 和 DRY 如何避免运维平台过度设计？
65. IoC 和 DI 如何提升平台代码的可测试性和可替换性？
66. 设计模式如何解决真实工程问题，而不是只背名字？
67. 代码审查如何成为质量门禁，而不是走形式？
68. 静态类型、动态类型和鸭子类型如何影响自动化脚本可靠性？
69. 表达式、语句和字符串插值在脚本编写中容易踩什么坑？
70. 编译器和解释器有什么差异，对运维工具选型有什么影响？
71. 递归和大 O 如何用于判断脚本是否会拖垮系统？
72. 二分搜索为什么要求有序数据，边界条件怎么处理？
73. 回文和变位词题如何写出清晰、低复杂度的实现？
74. 最基础的循环输出题如何体现边界意识？
75. 常见数据结构操作复杂度如何影响日志和资产处理程序？
76. 如何实现栈和哈希表，并说明复杂度和冲突处理？
77. 链表和环检测怎么讲清结构、指针和边界条件？
78. 整数溢出为什么是可靠性和安全问题，如何处理？
79. 三数之和如何用排序和双指针写到可面试水平？

## PROMETHEUS（64 题）

1. 可观测性和监控在 Prometheus 体系里应该怎么区分？
2. 设计监控时如何选择输出形式、监控对象和关键指标？
3. 时间序列、标签和聚合维度在 Prometheus 中有什么关系？
4. APM 和基础监控有什么区别，通常采集哪些数据？
5. 四个黄金指标如何用于 Prometheus 服务健康监控？
6. Pod WSS/RSS、kubectl top 和 Linux free 的内存口径为什么会不一致？
7. Prometheus 适合解决什么问题，生产使用有哪些最佳实践？
8. Prometheus 架构中各组件如何分工，数据如何流转？
9. Prometheus 从发现目标到告警通知的工作流程是什么？
10. Prometheus 中 Job、Instance 和 Target 分别表示什么？
11. Prometheus Pull 模型相比 Push 模型有什么优缺点？
12. Pushgateway 解决什么问题，为什么不能滥用？
13. Prometheus 与 InfluxDB、Zabbix 这类方案应该从哪些维度比较？
14. Prometheus 四类核心指标类型如何选择，常见误用有哪些？
15. PromQL 常用函数有哪些，生产查询时怎么分类使用？
16. PromQL 中如何计算窗口请求总量、速率和 CPU 使用率？
17. PromQL 中如何关联两个指标，on/ignoring 和 group_left/right 怎么用？
18. 如何查询 Prometheus 标签值，并把它用于 Grafana 变量和元数据探索？
19. 什么时候使用 relabel_configs，和 metric_relabel_configs 有什么区别？
20. Prometheus 支持哪些服务发现方式，生产中如何接入目标？
21. Exporter 是什么，常见 Exporter 如何选型和使用？
22. 自研 Exporter 时应该如何设计指标、采集器和运行方式？
23. 如何用 Prometheus 接入 Linux 主机和 MySQL 监控？
24. 新增 100 台服务器时，Prometheus 如何实现自动化监控接入？
25. Prometheus 如何实现 Kubernetes 集群全面监控，集群外 Exporter 怎么接入？
26. Prometheus Operator 如何管理 targets 和告警规则？
27. Target down 或 Exporter 停止工作时如何排查和监控？
28. Prometheus Alert 是如何定义、评估和发送的？
29. Prometheus 告警从异常发生到收到通知的延迟来自哪里，如何缩短？
30. Alertmanager 如何通过分组、去重、静默和抑制减少告警噪声？
31. Alertmanager 高可用和告警链路 HA 应该怎么设计？
32. Grafana 中创建告警的流程是什么，和 Prometheus Alert 有什么边界？
33. 如何实现 Prometheus/Alertmanager 告警的自动化响应？
34. 一个成熟的 Prometheus 告警监控体系应该如何设计？
35. Nagios 中邮件告警链路如何配置，和 Alertmanager 通知有什么差异？
36. Prometheus 本地 TSDB 的写入、Block、WAL 和保留机制是什么？
37. Prometheus 数据压缩和持久化大致如何实现？
38. 为什么 Prometheus 本地存储不适合长期保存，通常如何补足？
39. Prometheus 出现 OOM 的常见原因和治理手段有哪些？
40. 大规模 Prometheus 环境如何优化采集、查询和规则性能？
41. Prometheus 查询突然变慢时如何定位？
42. 如何评估 Prometheus 集群的容量和资源需求？
43. Prometheus 有哪些主流高可用方案，各自解决什么问题？
44. Thanos 架构中 Sidecar、Querier、Store、Compactor、Ruler 等组件如何分工？
45. Thanos 实现 Prometheus 高可用和全局查询的核心原理是什么？
46. Thanos Sidecar 模式和 Receive 模式有什么区别，如何选型？
47. Thanos Rule 和 Prometheus 本地规则有什么区别？
48. VictoriaMetrics 如何实现高可用和大规模指标存储？
49. Thanos 和 VictoriaMetrics 在架构、成本和运维上如何比较？
50. Grafana 的定位是什么，OSS、Cloud、Enterprise 有什么差异？
51. Grafana 默认端口是什么，如何配置 HTTPS 和安全访问？
52. Grafana 插件如何安装，生产使用要注意什么？
53. Grafana 数据源是什么，如何用 Prometheus 构建可视化看板？
54. Grafana 默认配置和自定义配置如何生效，容器化部署要注意什么？
55. Grafana 支持哪些外部认证方式，企业接入要注意什么？
56. Grafana 仪表板如何导入，Dashboard JSON 中哪些字段需要关注？
57. Grafana 仪表板如何分享给团队，哪些权限和安全问题要注意？
58. Grafana 中如何组织团队、用户、文件夹和仪表板权限？
59. Grafana 图表不显示数据时如何排查？
60. Nagios 的基本架构和监控机制是什么，和 Prometheus 有什么差异？
61. Nagios 中如何监控一个自定义服务？
62. 如何编写和部署一个 Nagios 自定义插件？
63. Nagios 如何实现分布式或远程监控？
64. Nagios 如何通过 SNMP 监控网络设备或系统指标？

## PYTHON（49 题）

1. Python 的对象模型和引用语义在运维脚本里为什么重要？
2. 可变对象、不可变对象和默认参数陷阱怎么讲清楚？
3. 浅拷贝、深拷贝在配置模板复制时有什么风险？
4. List 和 Tuple 在脚本参数、返回值和配置里应该怎么选？
5. Set 的去重、哈希约束和主机清单场景怎么回答？
6. Dict 的哈希查找、键约束和配置映射怎么说明？
7. `*args`、`**kwargs` 在通用脚本封装里怎么设计？
8. Lambda 的适用边界和排序过滤场景怎么回答？
9. 高阶函数如何用于回调式脚本扩展？
10. 装饰器和闭包如何封装日志、鉴权和重试？
11. LEGB 作用域和变量解析在脚本排障里怎么用？
12. 迭代器、生成器和惰性处理有什么生产价值？
13. GB 级日志文件如何流式读取并控制内存？
14. OOP 建模在运维平台开发中解决什么问题？
15. `__new__` 和 `__init__` 在对象创建生命周期中有什么区别？
16. `@classmethod`、`@staticmethod` 和实例方法如何选择？
17. `hasattr()`、`getattr()` 如何实现反射和动态调度？
18. `super()`、MRO 和多继承协作机制怎么解释？
19. `with` 语句和上下文管理协议如何保证资源释放？
20. 多进程、多线程、协程和 GIL 如何影响并发模型选择？
21. Python 垃圾回收和内存管理如何支撑泄漏排查？
22. 如何递归遍历目录并安全统计文件总大小？
23. 本地 Shell 和 100 台服务器批量执行怎么设计才可靠？
24. Socket 连通性和健康检查脚本怎么写？
25. Python 调用云平台、监控和 CMDB API 的经验怎么表达？
26. Python 程序内存泄漏如何定位和治理？
27. SQLAlchemy 在运维平台中承担什么角色？
28. 运维自动化脚本常用模块如何按能力边界选型？
29. 如何统计 Nginx 日志 Top IP 并兼顾大文件性能？
30. 如何用 Python 采集 CPU、内存、磁盘和网络指标？
31. Python Web 框架如何选型，Django MVT 架构怎么讲？
32. Django ORM 的定位和常用查询方法怎么回答？
33. DRF 在内部 API 平台里承担什么作用？
34. PEP8 和团队工程规范在运维开发中有什么价值？
35. Django 中间件职责和自定义流程怎么说明？
36. DRF 认证、权限和限流如何治理内部 API？
37. Celery 异步任务适合哪些运维平台场景？
38. Django CSRF 防护原理和 API 边界怎么讲？
39. Django 测试用例如何覆盖内部平台接口？
40. WebSocket 和 HTTP 的协议差异在运维控制台里怎么体现？
41. Python 正则表达式和常用元字符如何用于日志解析？
42. 运维开发项目经验应该如何表达才可信？
43. JSON/YAML 配置读取、校验和合并优先级怎么设计？
44. 可靠 API 客户端如何设计超时、重试、Token 和分页？
45. 生产脚本日志应该如何设计才能排障？
46. `argparse` 如何设计运维脚本参数？
47. 定时任务、批处理和幂等自动化如何避免重复执行？
48. 如何用 pytest 测试运维脚本而不是只靠手工跑？
49. Python 数据库操作如何避免连接泄露和事务问题？

## REDIS（27 题）

1. 生产环境 Redis 版本应该怎么选，升级前要评估什么？
2. Redis 适合哪些业务场景，哪些边界不能忽略？
3. Redis 数据类型怎么选，如何避免大 key 和复杂度风险？
4. Redis 到底是单线程还是多线程，Redis 6 I/O 多线程解决什么？
5. Redis 为什么快，什么情况下会从快变慢？
6. Redis 阻塞或卡顿时应该按什么链路排查？
7. Redis SLOWLOG 能定位什么，不能定位什么？
8. 生产环境 Redis 性能优化应该从哪些层面入手？
9. Redis 内存淘汰策略怎么选，如何保护容量边界？
10. Redis RDB 和 AOF 怎么取舍，生产持久化如何设计？
11. Redis 内存持续飙升时如何定位根因？
12. Redis 主从复制的全量同步和部分重同步怎么工作？
13. Redis 主从复制延迟过高怎么排查和治理？
14. Redis 单机、主从、Sentinel 和 Cluster 怎么选？
15. Redis Sentinel 如何判断主库故障并完成切换？
16. Sentinel 模式下应用应该如何连接并感知主从切换？
17. Redis Cluster 的 hash slot、重定向和故障转移怎么理解？
18. Redis Cluster 不可用时如何定位槽位、节点和客户端问题？
19. 缓存雪崩怎么产生，生产上如何做多层防护？
20. 缓存穿透怎么识别，空值缓存和布隆过滤器怎么用？
21. 缓存击穿和热点 key 重建应该如何治理？
22. Redis INFO 和监控系统里最该看哪些指标？
23. Redis 如何做安全加固和访问控制？
24. Redis 和 Memcached 在生产选型上怎么取舍？
25. Memcached 适合什么场景，限制在哪里？
26. Memcached 的多线程、slab 和 LRU 工作机制怎么讲？
27. Memcached 如何做认证和访问控制？

## SHELL（53 题）

1. 脚本第一行如何决定解释器，Bash 与 sh 的边界是什么？
2. 有了 Ansible 等工具后，Shell 仍适合承担哪些自动化任务？
3. 生产级 Shell 脚本应该包含哪些骨架能力？
4. Bash 默认失败行为是什么，严格模式该如何正确使用？
5. Shell 脚本如何调试、静态检查和自动化测试？
6. 变量赋值、命令替换和日期变量在脚本中怎么写才稳？
7. 如何读取用户输入，并正确处理单引号、双引号和反引号？
8. 如何阅读脚本片段并推断输出和命令结果？
9. 位置参数和特殊变量在生产脚本中如何完整使用？
10. `$@` 和 `$*` 在加引号与不加引号时有什么差异？
11. 如何根据参数是否存在实现脚本默认分支？
12. 字符串长度、截取和拼接如何用 Bash 参数展开完成？
13. 如何用模式删除展开提取扩展名、文件名前缀和路径片段？
14. Shell 中如何做算术运算，并用取模判断因子？
15. 如何生成 8 位随机数，并区分普通随机和安全随机？
16. Bash 中有哪些三元表达式写法，为什么要慎用 `&& ||`？
17. Bash 数组如何支撑批量数据遍历？
18. Bash 函数如何封装复用逻辑，并正确表达成功失败？
19. Here Document 如何生成多行输入、配置和远程命令？
20. 条件判断语法、文件测试和否定表达应该如何选择？
21. 如何校验脚本参数是否为数字？
22. for、while、until 循环如何安全处理文件和列表？
23. 如何把条件、循环和退出码组合成可维护脚本？
24. `trap` 如何捕捉信号并清理临时资源？
25. 进程替换、管道子 shell 和变量作用域有哪些陷阱？
26. Shell 管道如何连接数据流，生产中如何发现中间命令失败？
27. 重定向和文件读写如何处理 stdout、stderr 与日志落盘？
28. `awk` 如何做字段切分、过滤、聚合和格式化输出？
29. 正则在 grep、sed、awk 和 `[[ =~ ]]` 中如何使用？
30. grep、sed、awk、cut 如何组合使用才不脆弱？
31. 如何分析 Nginx 访问日志并定位异常流量？
32. 如何统计目录总大小和指定文件总行数？
33. crontab 的工作原理、环境差异和凌晨备份配置怎么回答？
34. 定时备份脚本如何设计目录、压缩、日志、保留周期和告警？
35. 如何自动备份 MySQL 多个库并处理账号、安全和校验？
36. 如何从 FTP 自动下载文件并做失败重试和落盘校验？
37. 临时文件清理脚本如何设置保留策略并避免误删？
38. 批量修改文件名如何处理冲突、回滚和 dry-run？
39. 磁盘使用率巡检和多服务器告警脚本怎么写？
40. 如何监控 CPU 使用率并定位 CPU/内存异常进程？
41. 进程和服务状态监控如何做到自愈但避免重启风暴？
42. 如何批量监控多个网站域名可用性？
43. MySQL 主从同步状态监控应该检查哪些字段？
44. 目录变化监控、日志记录和实时同步如何设计？
45. 关键文件完整性监控如何建立基线和告警？
46. Linux 服务器信息一键采集脚本应该覆盖哪些维度？
47. 如何探测 192.168.1.0/24 网段在线主机并控制扫描风险？
48. 批量创建用户和批量修改服务器账号密码如何控制风险？
49. 如何从访问日志识别异常 IP 并安全封禁？
50. 服务器端口扫描脚本如何实现并避免生产网络影响？
51. Java 项目自动发布到 Tomcat 的脚本流程如何设计？
52. LNMP 网站环境一键部署脚本如何做到幂等和可验证？
53. Windows 环境下如何用 PowerShell 做脚本化故障排查？

## VIBE-CODING（29 题）

1. 什么是 slash command，它和 skill 有什么区别？
2. 什么是 agent，什么情况下使用 agent，什么情况下使用 skill？
3. Sub-agent 是什么，Sub-agent 之间能否直接通信？
4. Agent Team 和 Sub-agent 的核心区别是什么？
5. MCP 是什么，它和普通 API 有什么区别？
6. Sub-agent 是否可以再派生自己的 sub-agent？
7. Plugin 和 Skill 的关系是什么？
8. ToolSearch 和 Deferred Tools 为什么要这样设计？
9. CLAUDE.md 和 AGENTS.md 是什么，加载顺序和优先级如何理解？
10. Hooks 是什么，常见使用场景有哪些？
11. Permission Mode 有哪些，分别适合什么场景？
12. 执行 compact 时，哪些上下文会保留，哪些容易丢失？
13. 如何避免主对话上下文被污染？
14. 设计长期记忆机制时，如何决定记什么和不记什么？
15. 为什么应该保持 context 简单，而不是把所有信息都塞进 prompt？
16. Agent 应该主动还是被动，什么时候该问用户？
17. Vibe Coding 是 hype 还是范式革命？
18. 让 agent 跑很久后看不懂它做了什么，这是 agent 的问题还是用户的问题？
19. 接到中等复杂度新功能时，应该如何拆解 agentic 工作流？
20. 什么时候应该开 sub-agent，什么时候不该？
21. 代码出 bug 时，如何用 agentic 工具调试？
22. 多人协作仓库中，如何让 agentic 工作流团队化？
23. Agent 反复改不对一个 bug 时，应该继续尝试还是停止？
24. 为什么 TDD 在 agentic 工作流里比传统工作流更重要？
25. Agent 写的代码可读性差，应该如何处理？
26. 设计 agentic 低代码平台时，应优先考虑哪些原则？
27. 设计企业内部 MCP 网关时，如何处理权限、审计和限流？
28. 多 agent 协作模型应该选择星型还是网状，为什么？
29. 设计 AI 安全 review agent 时，要避免哪些坑？

## WEBSITE（43 题）

1. Web 服务组件和静态、动态资源的边界怎么划分？
2. 浏览器访问一个域名时，完整链路应该怎么描述和排查？
3. HTTP/1.0、1.1、2、3 的差异对网站运维有什么影响？
4. HTTP 常见状态码如何和网关、应用故障边界对应？
5. HTTP 请求头、响应头和代理链路字段应该重点掌握哪些？
6. HTTP 长连接、短连接和连接生命周期如何影响容量与排障？
7. HTTP 和 HTTPS 的差异，以及 TLS 握手流程应该怎么讲？
8. HTTPS 证书链、CA 边界和 Apache 启用 HTTPS 如何落地？
9. CORS 跨域报错如何定位原因并治理？
10. CGI 和 FastCGI 在 Web 服务器中的作用与性能差异是什么？
11. Apache Worker、Prefork 和 worker 并发容量如何理解？
12. Apache 虚拟主机如何配置和验证？
13. Apache 自定义错误页面如何配置，如何避免二次故障？
14. 如何用 Ansible Playbook 安装并启动 Apache？
15. Tomcat 与 Resin 等 Web 容器如何选型？
16. Tomcat 的 8005、8009、8080 端口分别做什么，如何修改？
17. Tomcat 的工作模式和整体架构如何讲清楚？
18. Tomcat Connector 的作用是什么，NIO、NIO2、APR 有什么差异？
19. 一个 Web 请求在 Tomcat 内部的处理流程是什么？
20. Tomcat 中部署 Java Web 应用有哪些方式和注意点？
21. Cookie 和 Session 的区别与联系是什么？
22. Session 共享和 Tomcat Session 管理机制如何设计？
23. Tomcat 数据源连接池如何配置和排查？
24. Tomcat 内存使用应该监控哪些指标，如何定位内存问题？
25. Tomcat 性能优化应该从哪些层面展开？
26. CDN 的工作原理、缓存命中和回源链路怎么讲？
27. Squid、Varnish 和 Nginx 的定位区别是什么？
28. LVS 的 NAT、DR、TUN 三种模式如何工作？
29. LVS 支持哪些调度算法，生产如何选择？
30. 四层和七层负载均衡有什么区别？
31. 面试中如何介绍自己维护过的网站整体架构？
32. 如何设计高可用的 Web 服务架构？
33. 高并发 Web 服务架构如何设计？
34. 秒杀系统应该如何优化？
35. 高并发下如何保护数据库性能？
36. 网站灰度发布策略如何设计和回滚？
37. 首页白屏、APP 空白和部分用户超时如何排查？
38. 网站或线上服务响应慢时，分层排查流程是什么？
39. 网站中文乱码有哪些原因，如何排查？
40. QPS、TPS、PV、UV 分别是什么，怎么统计才可靠？
41. 网站报 502 Bad Gateway 如何排查？
42. 网站 QPS 突降时如何快速定位？
43. 网站监控指标体系应该覆盖哪些内容？

## ZABBIX（32 题）

1. Zabbix 核心组件怎么分工，生产架构里各自负责什么？
2. 一条监控数据从采集到告警在 Zabbix 中如何流转？
3. Zabbix Server 有哪些关键进程，如何判断采集瓶颈？
4. Host、Item、Trigger、Action、Template 等 Zabbix 术语怎么串起来？
5. Zabbix 中 Host、Host Group 和 Template 的关系怎么设计？
6. Zabbix 模板机制如何支撑批量监控复用？
7. Zabbix 模板宏如何做参数化阈值和差异化配置？
8. Zabbix Agent 主动模式和被动模式怎么选？
9. Zabbix Agent 和 Proxy 的职责边界是什么？
10. 新增一台 Linux 主机接入 Zabbix 的完整流程是什么？
11. Zabbix Agent 如何批量安装和统一下发配置？
12. Windows 主机如何接入 Zabbix 并验证监控数据？
13. Zabbix UserParameter 如何采集自定义指标，风险在哪里？
14. 生产环境 Zabbix 常见监控指标应该如何设计？
15. Zabbix 如何落地 MySQL 监控并设置关键告警？
16. Zabbix 如何通过 SNMP 监控网络设备？
17. Zabbix 如何监控 Web 服务可用性、状态码和响应时间？
18. Zabbix 如何监控 Keepalived 脑裂风险？
19. Zabbix 自动发现、自动注册和 LLD 分别适合什么场景？
20. Zabbix 自定义 LLD 发现规则怎么实现？
21. 上百台服务器如何通过 Zabbix 自动化接入和验证？
22. Zabbix 分布式监控架构如何设计和落地？
23. Zabbix Proxy 适合哪些场景，缓存边界在哪里？
24. Zabbix 7.0 Proxy HA 集群解决什么问题，使用边界是什么？
25. Zabbix 中 Item、Trigger、Action 如何形成告警闭环？
26. Zabbix 告警机制从事件生成到通知发送是怎么实现的？
27. Zabbix 如何配置企业微信或 Webhook 告警通知？
28. Zabbix 如何减少告警风暴和级联误报？
29. Zabbix 监控图表中断时如何逐层排查？
30. Zabbix 数据库膨胀后如何安全清理和治理？
31. Zabbix 监控系统性能优化应该从哪些层面入手？
32. Zabbix 和 Prometheus 在生产监控选型上怎么取舍？

---

**总计：22 个专题，1502 道题目。**
