# Kubernetes 深度专题学习指南（Study Guide）

> 与 [kubernetes-questions.md](kubernetes-questions.md)（50 题快问快答）互补：本文按**知识域**组织，
> 每域给出「概念地图 → 高频面试题（遵循 [../../docs/STANDARD.md](../../docs/STANDARD.md) 模板）→ 排障套路 → 延伸」，
> 用于**系统性复盘**而非零散刷题。
>
> 内容基于官方文档（kubernetes.io）、Jimmy Song《Kubernetes Handbook》、社区排障资料等一手来源综合整理，
> 文末 [附录 A](#附录-a资料来源) 列出对应来源文件。核心对象模型见 [../../basics/04-kubernetes-concepts.md](../../basics/04-kubernetes-concepts.md)。

---

## 目录

1. [集群架构与控制面](#1-集群架构与控制面)
2. [Pod 生命周期与工作负载控制器](#2-pod-生命周期与工作负载控制器)
3. [调度：亲和性、污点、拓扑](#3-调度亲和性污点拓扑)
4. [GPU / 设备管理与拓扑感知](#4-gpu--设备管理与拓扑感知)
5. [网络：CNI、Service、Ingress/Gateway](#5-网络cniserviceingressgateway)
6. [存储：CSI、卷与有状态应用](#6-存储csi卷与有状态应用)
7. [安全：认证、授权、准入、Secret](#7-安全认证授权准入secret)
8. [可观测性与运行时诊断](#8-可观测性与运行时诊断)
9. [排障方法论](#9-排障方法论)
10. [AI 原生 / 大模型推理上 K8s](#10-ai-原生--大模型推理上-k8s)
11. [附录 A：资料来源](#附录-a资料来源)

---

## 1. 集群架构与控制面

**概念地图**：一个集群 = **控制面（control plane）** + 若干 **工作节点（node）**。控制面做全局决策（调度、响应事件），节点跑 Pod。

- 控制面组件：`kube-apiserver`（唯一读写 etcd 的入口，REST 前端）、`etcd`（一致性 KV 存储，集群唯一事实源）、`kube-scheduler`（绑定 Pod→Node）、`kube-controller-manager`（各类 reconcile 循环）、`cloud-controller-manager`（对接云厂商）。
- 节点组件：`kubelet`（管理本节点 Pod，经 CRI 调运行时）、`kube-proxy`（实现 Service 的 L4 转发，部分 CNI 自带代理可省略）、容器运行时（containerd / CRI-O）。
- 核心思想：**声明式 + 控制器 reconcile**——用户声明期望态（spec），控制器持续把实际态（status）拉向期望态。

### Q1. 画出并解释 Kubernetes 的整体架构；etcd 为什么是集群的「单点真相」？
- **难度**：🔴 高级
- **关键词**：control plane, apiserver, etcd, controller, reconcile
- **概念速记**：
  - **apiserver**：所有组件的通信枢纽，唯一直接读写 etcd 者；其余组件通过它 watch/更新。
  - **etcd**：基于 Raft 的强一致 KV，存放全部集群状态；丢了 etcd 约等于丢了集群。
  - **reconcile loop**：控制器「观察实际态→对比期望态→执行差异」的无限循环。
- **问题**：请求 `kubectl apply` 一个 Deployment 后，各控制面组件如何协作把它变成 Running 的 Pod？
- **参考答案**：
  1. `kubectl`→apiserver：认证（authn）→鉴权（authz, RBAC）→准入（admission，含 mutating/validating webhook）→schema 校验→写入 etcd。
  2. Deployment 控制器 watch 到新对象→创建 ReplicaSet→ReplicaSet 控制器创建 Pod（此时 Pod 无节点，Pending）。
  3. scheduler watch 到未绑定 Pod→按过滤（predicates）+ 打分（priorities）选节点→写回 `nodeName`。
  4. 目标节点 kubelet watch 到属于自己的 Pod→经 CRI 拉镜像、建 sandbox/容器→CNI 配网络、CSI 挂卷→探针通过→Running。
  5. 每一步都是**异步、经 apiserver、以 etcd 为真相**；任一控制器崩溃重启后可从 etcd 恢复继续 reconcile。
- **易错点 / 面试官关注**：
  - 以为 scheduler「创建」Pod（它只做绑定，创建来自 controller）。
  - 忽略 admission 阶段（LimitRanger、PodSecurity、webhook 都可能拦截）。
  - 不清楚 etcd 备份/恢复（`etcdctl snapshot save`）是灾备关键。
- **延伸**：Q3（CRI）、[kubernetes-questions.md](kubernetes-questions.md) Q3

### Q2. 控制面高可用怎么做？apiserver 无状态而 etcd 有状态，各自的 HA 策略有何不同？
- **难度**：⚫ 资深
- **关键词**：HA, etcd quorum, leader election, load balancer
- **概念速记**：
  - **apiserver 无状态**：可水平多副本，前面挂 LB（或 kube-vip / haproxy+keepalived）即可。
  - **etcd 有状态**：奇数节点（3/5），靠 Raft 多数派（quorum）；`n` 节点容忍 `(n-1)/2` 故障。
  - **leader election**：controller-manager、scheduler 多副本时只有 leader 干活，避免重复 reconcile。
- **问题**：3 节点 etcd 挂 1 台还能写吗？挂 2 台呢？为什么 controller-manager 要 leader 选举而 apiserver 不用？
- **参考答案**：
  1. 3 节点 quorum=2：挂 1 台仍有 2 台达成多数派，可读写；挂 2 台只剩 1 台无法过半，集群**只读甚至不可用**。故生产用 3 或 5，不用偶数（4 台容错仍是 1，性价比差）。
  2. apiserver 无本地状态，多副本可同时服务、经 LB 分流，天然可并行。
  3. controller/scheduler 若多副本同时 reconcile 会产生竞态（重复建 Pod、重复调度），故用 `leases` 做 leader election，同一时刻只有一个活跃。
- **易错点**：混淆「apiserver 多活」与「controller 主备」；用偶数 etcd 节点。
- **延伸**：Q1；observability 模块（etcd 监控）

---

## 2. Pod 生命周期与工作负载控制器

**概念地图**：Pod 是最小调度单位；上层控制器管理 Pod 集合——**Deployment**（无状态、滚动更新）、**StatefulSet**（有状态、稳定网络/存储、有序）、**DaemonSet**（每节点一个）、**Job/CronJob**（批处理/定时）。

### Q3. Deployment / StatefulSet / DaemonSet 各自解决什么问题？StatefulSet 的三大「稳定性」保证是什么？
- **难度**：🟡 中级
- **关键词**：Deployment, StatefulSet, DaemonSet, 稳定标识, headless service
- **概念速记**：
  - **Deployment**：无状态副本，Pod 可互换、随机名、滚动更新经 ReplicaSet。
  - **StatefulSet**：稳定网络标识（`pod-0/1/2`）+ 稳定存储（每副本独立 PVC）+ 有序创建/删除/滚动。
  - **DaemonSet**：保证每个（或符合选择器的）节点运行一份，如日志/监控/CNI agent。
- **问题**：什么场景必须用 StatefulSet 而非 Deployment？它靠什么给每个副本稳定的网络名？
- **参考答案**：
  1. 需要**稳定标识 + 独占持久卷 + 顺序**时用 StatefulSet：如 etcd/ZooKeeper/MySQL 主从、Kafka——副本间不对等，需知道「我是谁、我的盘是哪块」。
  2. 稳定网络名靠**Headless Service**（`clusterIP: None`）：DNS 为每个 Pod 生成 `pod-0.svc.ns.svc.cluster.local`，Pod 重建后名字/DNS 不变。
  3. 存储稳定靠 `volumeClaimTemplates`：为每个序号生成独立 PVC，Pod 重建后重新绑定同一 PV。
  4. 有序性：默认 `OrderedReady`——`pod-0` Ready 才建 `pod-1`；删除逆序。可用 `podManagementPolicy: Parallel` 放宽。
- **易错点 / 面试官关注**：
  - 用 Deployment 挂共享 PVC 跑数据库（多副本写同盘→数据损坏）。
  - 忘了 StatefulSet 需要配套 Headless Service 才有稳定 DNS。
  - 缩容 StatefulSet 不会自动删 PVC（防误删数据，需手动清）。
- **延伸**：[kubernetes-questions.md](kubernetes-questions.md) 相关；storage 章 Q6

### Q4. 滚动更新（RollingUpdate）的 maxSurge / maxUnavailable 如何影响可用性？回滚怎么做？
- **难度**：🟡 中级
- **关键词**：RollingUpdate, maxSurge, maxUnavailable, revisionHistory, rollback
- **概念速记**：`maxSurge` 允许超出期望副本数多创建几个新 Pod；`maxUnavailable` 允许更新期间不可用几个旧 Pod。
- **问题**：`replicas=10, maxSurge=25%, maxUnavailable=0` 时更新过程最多有多少 Pod？如何回滚到上一个版本？
- **参考答案**：
  1. `maxUnavailable=0` 保证**任何时刻至少 10 个可用**；`maxSurge=25%`→最多额外 3 个（向上取整），即峰值 13 个 Pod。这是「零中断」但更耗资源的配置。
  2. 回滚：`kubectl rollout undo deployment/x`（可 `--to-revision=N`）；`kubectl rollout history` 看历史；Deployment 靠保留旧 ReplicaSet（`revisionHistoryLimit`）实现快速回滚。
  3. 结合 `readinessProbe`：新 Pod 未 Ready 不接流量、不推进更新，避免把坏版本放量。
- **易错点**：`maxUnavailable` 与 `maxSurge` 同时为 0 会导致更新卡死；无 readiness 探针时滚动更新会「假成功」。
- **延伸**：Q3；cicd-iac 模块（渐进式发布/金丝雀）

---

## 3. 调度：亲和性、污点、拓扑

**概念地图**：调度 = **过滤（能不能放）+ 打分（放哪最好）**。约束手段：`nodeSelector`、节点/Pod 亲和与反亲和（affinity/anti-affinity）、污点与容忍（taint/toleration）、拓扑分布约束（topologySpreadConstraints）。

### Q5. nodeAffinity、podAffinity/anti-affinity、taint/toleration、topologySpread 分别解决什么？会不会冲突？
- **难度**：🔴 高级
- **关键词**：nodeAffinity, podAntiAffinity, taint, toleration, topologySpreadConstraints
- **概念速记**：
  - **nodeAffinity**：Pod 倾向/必须落在带某标签的节点（硬 `required` / 软 `preferred`）。
  - **podAffinity / anti-affinity**：按「已有 Pod 的位置」聚拢或打散（如同应用副本互斥到不同节点/机架）。
  - **taint/toleration**：节点「排斥」不容忍它的 Pod（污点在节点，容忍在 Pod）；`NoSchedule/PreferNoSchedule/NoExecute`。
  - **topologySpreadConstraints**：按拓扑域（zone/node）均匀分布，控制 `maxSkew`。
- **问题**：要让一个 3 副本服务「跨可用区打散、且不与某批 Pod 同节点、且只落在 GPU 节点」，怎么组合？
- **参考答案**：
  1. 只落 GPU 节点：`nodeAffinity.required` 匹配 `accelerator=nvidia` 标签（或用 GPU 节点的污点 + 对应 toleration）。
  2. 跨 AZ 打散：`topologySpreadConstraints` 以 `topology.kubernetes.io/zone` 为 key、`maxSkew=1`、`whenUnsatisfiable: DoNotSchedule`。
  3. 与某批 Pod 互斥：`podAntiAffinity.required` 以 `topologyKey: kubernetes.io/hostname` + 匹配那批 Pod 的 label。
  4. 冲突可能：约束太硬（全 required）会导致无节点可选→Pending；生产常「关键约束 required + 优化项 preferred」。
- **易错点 / 面试官关注**：
  - 把污点/容忍当亲和性用（容忍只是「允许」调度到污点节点，不代表「倾向」）。
  - `podAntiAffinity` 用 `required` + 副本数 > 节点数 → 永远 Pending。
  - 忘了 `topologySpread` 的 `whenUnsatisfiable: ScheduleAnyway`（软）与 `DoNotSchedule`（硬）差异。
- **延伸**：Q6（GPU 调度）、[kubernetes-blog-2017-03-advanced-scheduling](#附录-a资料来源)

---

## 4. GPU / 设备管理与拓扑感知

**概念地图**：K8s 自 v1.26 起**稳定**支持 AMD/NVIDIA GPU，经 **Device Plugin** 暴露为可请求资源（如 `nvidia.com/gpu`）。更细粒度/共享/拓扑诉求由 **Dynamic Resource Allocation（DRA）**、**Topology Manager**、以及第三方（HAMi、MPS/MIG）满足。

### Q6. Pod 如何请求 GPU？Device Plugin 与 Dynamic Resource Allocation（DRA）有何区别？
- **难度**：🔴 高级
- **关键词**：device plugin, nvidia.com/gpu, DRA, MIG, 资源共享
- **概念速记**：
  - **Device Plugin**：厂商 DaemonSet 向 kubelet 注册设备，GPU 变成可 `requests/limits` 的整数资源；**不可超卖、不可小数**（一个容器整卡或整数卡）。
  - **DRA（Dynamic Resource Allocation）**：更通用的设备申请模型（ResourceClaim/ResourceClass），支持按参数申请、共享、复杂拓扑，弥补 device plugin「只能整数」的短板。
- **问题**：为什么裸 device plugin 难做「多容器共享一张 GPU」？DRA 或 HAMi 怎么补？
- **参考答案**：
  1. device plugin 模型下 GPU 是不可分割整数资源：`limits: nvidia.com/gpu: 1` 独占整卡，无法原生按显存/算力切分，利用率低。
  2. 共享方案：**MIG**（A100/H100 硬件分区，装置为多个更小的 GPU 实例）、**MPS**（进程级时分复用）、**HAMi** 等（软件层显存/算力配额 + 语义校验）。
  3. **DRA** 从 K8s 层给出标准化的「结构化设备申请」：用 ResourceClaim 描述需要什么样的设备（含共享/拓扑），调度器与驱动协作分配，比 device plugin 表达力强。
  4. 拓扑：跨 NUMA/PCIe 的 GPU-CPU-网卡亲和影响性能，用 **Topology Manager**（`single-numa-node` 等策略）对齐，避免跨 NUMA 拖慢。
- **易错点 / 面试官关注**：
  - 以为 `nvidia.com/gpu: 0.5` 能小数申请（原生不行）。
  - 不装厂商驱动 + device plugin 就想调度 GPU（会一直 Pending，`describe` 见 Insufficient nvidia.com/gpu）。
  - 忽略拓扑：GPU 分到了但跨 NUMA，训练/推理带宽掉。
- **延伸**：第 10 章（AI 推理）、[topology-manager / scheduling-gpus / DRA 文档](#附录-a资料来源)

---

## 5. 网络：CNI、Service、Ingress/Gateway

**概念地图**：K8s 网络三定律——① 每 Pod 一 IP；② Pod 间无 NAT 直连；③ 节点与 Pod 可互通。实现交给 **CNI 插件**（Calico/Cilium/Flannel）。四层暴露用 **Service**（ClusterIP/NodePort/LoadBalancer），七层/路由用 **Ingress** 或新一代 **Gateway API**。

### Q7. Service 的 ClusterIP 是怎么生效的？kube-proxy 的 iptables 与 IPVS 模式差在哪？
- **难度**：🔴 高级
- **关键词**：Service, kube-proxy, iptables, IPVS, Endpoints
- **概念速记**：
  - **Service**：一组 Pod 的稳定虚拟入口；`selector` 关联的就绪 Pod IP 进入 `Endpoints/EndpointSlice`。
  - **kube-proxy**：把访问 ClusterIP 的流量 DNAT 到某个后端 Pod IP；iptables 模式用规则链，IPVS 模式用内核 LVS 哈希表。
- **问题**：一个有 2000 个 Service 的大集群，为什么建议 kube-proxy 用 IPVS 而非 iptables？
- **参考答案**：
  1. ClusterIP 是虚 IP，不在任何网卡；kube-proxy watch Service/Endpoints，编排转发规则实现「访问 VIP→随机/轮询到后端 Pod」。
  2. **iptables 模式**：规则线性匹配，随 Service 数量增长规则数暴涨，更新与匹配 O(n)，大规模下时延与 reload 抖动明显。
  3. **IPVS 模式**：基于内核 LVS 哈希表 O(1) 查找，支持 rr/lc/sh 等算法，大规模转发性能与更新效率显著更好。
  4. 现代趋势：**Cilium** 用 eBPF 直接替代 kube-proxy，进一步降开销、支持更丰富策略。
- **易错点 / 面试官关注**：
  - 以为 ClusterIP 能 ping（多数实现只转发 TCP/UDP，不响应 ICMP）。
  - 只看 Service 不看 Endpoints——`selector` 没匹配到就绪 Pod 时 Service「通但无后端」。
  - readiness 失败的 Pod 会被摘出 EndpointSlice（Service 层的「摘流量」）。
- **延伸**：Q8；service-mesh 模块；[networking / cilium / calico 文档](#附录-a资料来源)

### Q8. Ingress 与 Gateway API 有什么区别？为什么社区在往 Gateway API 迁移？
- **难度**：🟡 中级
- **关键词**：Ingress, Gateway API, 角色分离, 表达力
- **概念速记**：
  - **Ingress**：老的 L7 路由 API，能力有限、厂商靠 annotation 各自扩展，可移植性差。
  - **Gateway API**：新一代，`GatewayClass/Gateway/HTTPRoute` 分层，**角色分离**（平台管 Gateway、应用团队管 Route），原生支持更丰富的流量语义。
- **问题**：Ingress 的痛点是什么？Gateway API 如何解决？
- **参考答案**：
  1. Ingress 痛点：功能靠 annotation 堆砌（不同 controller 不通用）、无标准的流量拆分/头部匹配/多协议、权限粒度粗。
  2. Gateway API：用 CRD 表达路由、跨命名空间引用、按角色拆分资源；标准字段支持 header/method/权重路由；面向多协议（HTTP/TCP/gRPC）。
  3. 迁移：官方有 `ingress2gateway` 工具辅助转换；服务网格（Istio ambient 等）也以 Gateway API 为一等公民。
- **易错点**：以为 Gateway API 只是「新版 Ingress」（它是可扩展的分层模型，不止 HTTP）。
- **延伸**：[ingress2gateway / migrating-from-ingress-to-gateway 文档](#附录-a资料来源)

---

## 6. 存储：CSI、卷与有状态应用

**概念地图**：**CSI（Container Storage Interface）** 解耦 K8s 与存储后端。声明式三件套：**StorageClass**（怎么造盘）→ **PVC**（要多大盘）→ **PV**（真实盘）。`volumeBindingMode: WaitForFirstConsumer` 让盘随 Pod 落到同一拓扑域。

### Q9. PV / PVC / StorageClass 的关系？动态供给（dynamic provisioning）流程是怎样的？
- **难度**：🟡 中级
- **关键词**：PV, PVC, StorageClass, CSI, WaitForFirstConsumer
- **概念速记**：PVC 是「用户对存储的申请」，PV 是「真实存储」，StorageClass 是「按需造 PV 的模板 + 制备器」。
- **问题**：用户建了 PVC 后，一块云盘是怎么被自动创建并挂到 Pod 的？`WaitForFirstConsumer` 解决什么问题？
- **参考答案**：
  1. PVC 引用某 StorageClass→CSI external-provisioner watch 到→调用云厂商创建卷→生成 PV 并与 PVC 绑定。
  2. Pod 调度到节点后，kubelet 经 CSI `NodeStage/NodePublish` 把卷挂进容器。
  3. `WaitForFirstConsumer`：**延迟绑定**到 Pod 被调度时再造盘，确保盘创建在 Pod 实际所在的可用区（否则可能盘在 AZ-a、Pod 在 AZ-b 无法挂载）。
  4. 回收策略 `reclaimPolicy`：`Delete`（删 PVC 连带删盘）/`Retain`（保盘防丢数据）。
- **易错点 / 面试官关注**：
  - 跨 AZ 绑定失败（未用 WaitForFirstConsumer）。
  - `Delete` 回收策略误删生产数据；StatefulSet 缩容不自动删 PVC。
  - `accessModes`（RWO/ROX/RWX）与后端能力不匹配（块存储通常只 RWO）。
- **延伸**：Q3（StatefulSet）、[storage-overview 文档](#附录-a资料来源)

---

## 7. 安全：认证、授权、准入、Secret

**概念地图**：一次 API 请求依次过 **认证（authn：谁）→ 授权（authz：能不能，主力是 RBAC）→ 准入（admission：改写/拦截）**。工作负载身份用 **ServiceAccount**；敏感数据用 **Secret**（默认仅 base64，非加密！）。

### Q10. 描述 K8s 的认证-授权-准入三段式；RBAC 的四个对象是什么？
- **难度**：🔴 高级
- **关键词**：authentication, RBAC, admission, ServiceAccount, PodSecurity
- **概念速记**：
  - **authn**：证书 / token / ServiceAccount / OIDC 确认身份。
  - **authz（RBAC）**：`Role`/`ClusterRole` 定义权限，`RoleBinding`/`ClusterRoleBinding` 把权限绑给主体（user/group/SA）。
  - **admission**：mutating（改写，如注入 sidecar）→ validating（校验/拒绝，如 PodSecurity、OPA/Gatekeeper、Kyverno）。
- **问题**：一个 Pod 里的进程要调用 API server，它的身份从哪来？如何最小权限授权？RBAC 里 Role 与 ClusterRole 何时用哪个？
- **参考答案**：
  1. Pod 挂载 ServiceAccount 的 token（`/var/run/secrets/.../token`），以该 SA 身份访问 apiserver。
  2. 最小权限：为该 SA 建一个只含所需 verbs/resources 的 `Role`，用 `RoleBinding` 绑到该 SA；**避免绑 cluster-admin**。
  3. `Role`（命名空间内权限）配 `RoleBinding`；`ClusterRole`（集群级或跨命名空间、含非命名空间资源如 nodes）配 `ClusterRoleBinding`（全集群）或被 `RoleBinding` 引用（限定到某命名空间）。
  4. 常见越权链：一个可 `create pods` 或 `pods/exec` 的 SA 能借他人 Pod 窃取其 SA token 横向移动——**权限设计要防这种链式升级**（参见 IDOR/越权原理）。
- **易错点 / 面试官关注**：
  - 以为 Secret 是加密的（默认只是 base64；需开 etcd `EncryptionConfiguration` 静态加密）。
  - 滥发 `cluster-admin`；`ClusterRoleBinding` 授权范围远超预期。
  - 忘了 admission webhook 失败策略（`failurePolicy: Fail` 可能把整个集群写操作卡死）。
- **延伸**：cloud-security 模块；[security-overview / RBAC / secrets 文档](#附录-a资料来源)

---

## 8. 可观测性与运行时诊断

**概念地图**：三支柱——**Metrics**（Prometheus，趋势/告警）、**Logs**（采集如 Loggie/Fluent Bit，还原现场）、**Traces**（OpenTelemetry，跨服务链路）。运行时层可用 eBPF/OTel 观测系统调用与容器行为。

### Q11. Metrics / Logs / Traces 各解决什么问题？为什么三者要关联？
- **难度**：🟡 中级
- **关键词**：Prometheus, OpenTelemetry, logs, traces, 关联
- **概念速记**：Metrics 告诉你「有没有问题、何时」，Logs 告诉你「发生了什么」，Traces 告诉你「在链路的哪一跳」。
- **问题**：线上 P99 延迟突增，你会如何用三支柱逐步定位？OpenTelemetry 在其中的角色？
- **参考答案**：
  1. Metrics（告警入口）：看 RED（Rate/Errors/Duration）与资源饱和度，定位「哪个服务、什么时间」。
  2. Traces：对该服务的慢请求下钻 span，找到耗时最长的下游/DB 调用（哪一跳）。
  3. Logs：到那一跳的实例按 trace_id 拉日志看具体错误/堆栈（为什么）。
  4. **OpenTelemetry** 统一采集三类信号并用 `trace_id`/`exemplar` 打通，避免各系统割裂；运行时可观测（eBPF/OTel）还能看系统调用级异常。
- **易错点**：只堆监控不做关联（有海量指标却无法从告警一路下钻到根因）。
- **延伸**：observability 模块；[opentelemetry / runtime-observability 文档](#附录-a资料来源)

---

## 9. 排障方法论

> 面试高频「场景题」。核心：**先分层定界（是调度/网络/存储/应用哪层），再看 Events + Logs + 描述对象，最后动手验证**。

### Q12. Pod 一直 Pending / CrashLoopBackOff / ImagePullBackOff / OOMKilled，各自怎么排？
- **难度**：🟡 中级
- **关键词**：Pending, CrashLoopBackOff, ImagePullBackOff, OOMKilled, Events
- **概念速记**：状态名就是线索——Pending=没调度上；CrashLoop=起来又挂；ImagePull=拉不到镜像；OOMKilled=超内存被杀（exit 137）。
- **问题**：给你一个 CrashLoopBackOff 的 Pod，说出你的排查命令序列。
- **参考答案**：
  1. `kubectl describe pod` 看 **Events**（最重要）：调度失败原因、拉镜像失败、挂载失败、探针失败。
  2. `kubectl logs <pod> --previous`：看**上一次**崩溃的日志（CrashLoop 关键，当前容器可能刚重启无日志）。
  3. 按状态分流：
     - **Pending**：资源不足 / 污点未容忍 / PVC 未绑 / GPU 不足 → `describe node`、查 requests 与 quota。
     - **ImagePullBackOff**：镜像名/tag 错、私有仓库缺 `imagePullSecret`、网络不通 → `crictl pull` 验证。
     - **OOMKilled**：`describe` 见 OOMKilled、exit 137 → 调大 `limits.memory` 或查内存泄漏；区分「cgroup OOM（单容器超限）」与「节点级 OOM」。
     - **CrashLoop**：应用启动即崩（配置错/依赖不通/健康检查过严）→ 看 `--previous` 日志、临时去掉 liveness 观察。
  4. 网络类：进 Pod `nslookup`/`curl` 验证 DNS 与 Service 连通；查 EndpointSlice 是否有后端。
- **易错点 / 面试官关注**：
  - 不看 Events 直接猜；CrashLoop 不加 `--previous` 看不到真正错误。
  - 把 readiness 当 liveness（探针配置引发的 CrashLoop/摘流量）。
  - OOM 混淆节点级与 cgroup 级。
- **延伸**：[kubernetes-questions.md](kubernetes-questions.md) Q5；linux 排障；[feisky troubleshooting / oreilly recipes 文档](#附录-a资料来源)

### Q13. 节点 NotReady 的系统化排查路径？
- **难度**：🟡 中级
- **关键词**：Node NotReady, kubelet, CNI, DiskPressure, 证书
- **概念速记**：节点 Ready 由 kubelet 心跳与 Conditions 决定；NotReady 即心跳丢失或某 Condition 异常。
- **问题**：监控报某节点 NotReady，上面的 Pod 开始被驱逐，你怎么定位？
- **参考答案**：
  1. `kubectl describe node` 看 Conditions：`MemoryPressure`/`DiskPressure`/`PIDPressure`/`NetworkUnavailable`。
  2. 登节点 `journalctl -u kubelet -f`：看 kubelet 是否在跑、报什么错（证书过期、CNI 未就绪、运行时挂了）。
  3. 常见根因：**磁盘打满**（DiskPressure→kubelet 无法写镜像/日志）、**CNI DaemonSet 异常**（NetworkUnavailable）、**kubelet 证书过期**（默认一年）、**容器运行时崩溃**（`crictl ps` 无响应）、**时钟漂移**。
  4. 处置：先止血（cordon + drain 迁移负载），再修根因；`NoExecute` 污点会在容忍期后驱逐 Pod。
- **易错点**：忽略 DiskPressure；忘了 kubelet/证书维度；直接重启节点丢现场。
- **延伸**：[monitor-node-health / kubeadm troubleshooting 文档](#附录-a资料来源)

---

## 10. AI 原生 / 大模型推理上 K8s

**概念地图**：K8s 正从「云原生」走向「AI 原生」——把训练/推理当一等公民。关注点：GPU 利用率（共享/MIG/HAMi）、拓扑感知调度、推理服务弹性（KEDA 按队列/QPS 扩缩）、模型分发与冷启动、Gateway API 的推理扩展（inference routing）。

### Q14. 在 K8s 上跑大模型推理服务，和普通无状态 Web 服务相比要额外考虑什么？
- **难度**：🔴 高级
- **关键词**：GPU 利用率, 冷启动, KEDA, 拓扑感知, 模型分发
- **概念速记**：推理 Pod 又「重」（大镜像 + 大模型权重）又「贵」（GPU），弹性与放置策略比普通 Web 复杂得多。
- **问题**：一个 LLM 推理服务白天高峰、夜间低谷，如何在保证 GPU 利用率的同时控制成本与延迟？
- **参考答案**：
  1. **弹性**：普通 HPA 基于 CPU 不适用，改用 **KEDA** 按队列长度/QPS/GPU 利用率扩缩，甚至可缩到 0（配合冷启动策略）。
  2. **冷启动**：大镜像 + 数十 GB 权重导致启动慢——用镜像预热/懒加载（如 vLLM 的权重加载优化）、模型缓存卷（PVC/本地 NVMe）、预留最小副本避免冷启。
  3. **放置**：拓扑感知（Topology Manager + NUMA 对齐）避免 GPU-CPU-网卡跨 NUMA 掉带宽；多机推理还需高速网络（RDMA/NCCL）亲和。
  4. **共享与隔离**：低 QPS 服务用 MIG/HAMi 切卡提利用率；高 QPS 独占整卡。
  5. **路由**：Gateway API 的推理扩展可按模型/优先级路由请求到不同后端池。
- **易错点 / 面试官关注**：
  - 用 CPU HPA 扩 GPU 服务（指标不相关）。
  - 忽视冷启动，缩到 0 后首个请求超时。
  - 只看「分到 GPU」不看拓扑，训练/推理性能不达标。
- **延伸**：第 4、6 章；[ai-native / KEDA / topology-aware scheduling 文档](#附录-a资料来源)

---

## 附录 A：资料来源

本指南综合以下一手来源整理（均为公开文档/书籍的本地存档）。如需精确原文与更深细节，请回到对应来源：

**官方文档（kubernetes.io）**
- Concepts — Architecture（控制面/节点组件）
- Concepts — Cluster Administration: Networking（网络模型）
- Concepts — Workloads / Controllers: StatefulSet（有状态控制器）
- Concepts — Resource Management: Dynamic Resource Allocation（DRA）
- Tasks — Manage GPUs: Scheduling GPUs（GPU 调度，v1.26 stable）
- Tasks — Administer Cluster: Topology Manager（拓扑管理）
- Tasks — Debug Cluster: Monitor Node Health（节点健康）
- Blog 2017-03: Advanced Scheduling in Kubernetes（亲和/污点）
- Blog 2016-12: Container Runtime Interface (CRI)（CRI 起源）
- Blog 2022-12: Runtime Observability with OpenTelemetry
- zh-cn Setup — kubeadm Troubleshooting（kubeadm 排障）

**Jimmy Song《Kubernetes Handbook》（jimmysong.io，中文）**
- architecture: overview / etcd / perspective（架构与 etcd）
- controllers: overview / deployment / statefulset / daemonset / job / cronjob / replicaset
- cluster: scheduling / taint-and-toleration / namespace
- interfaces: cri / cni（运行时/网络接口）
- networking: overview / calico / cilium / flannel
- storage: overview / configmap-hot-update / configuration-management
- security: overview / authentication / authn-and-authz / network-policy / RBAC / TLS bootstrapping / kubelet & kubectl 认证授权
- service-discovery: service / ingress / gateway / migrating-from-ingress-to-gateway-api
- observability: overview / logging / opentelemetry / kiali
- ai-native: from-cloud-native-to-ai-native / model-deployment / inference-optimization / HAMi / vLLM / security-best-practices
- extend: operator-sdk / kubebuilder / admission-webhook / scheduler-framework / custom-autoscaler

**社区与第三方**
- kubernetes.feisky.xyz — Troubleshooting Index（排障索引）
- O'Reilly — Kubernetes Recipes: Maintenance and Troubleshooting
- OWASP — Kubernetes Security Cheat Sheet
- spacelift — Kubernetes Secrets
- kubernetes-sigs — cri-tools / ingress2gateway / controller-runtime / security-profiles-operator
- 各类实践博客（bare-metal vs VM、KEDA 自动伸缩、Cilium BGP、拓扑感知调度提升 GPU 利用率等）

> 完整来源文件清单见本次提交所引用的 `k8s/slurps/` 存档（461 篇）。本指南为**综合与提炼**，不逐字照搬；命令与结论以你集群实际版本为准（尤其 GPU/DRA/Gateway API 等快速演进特性）。
