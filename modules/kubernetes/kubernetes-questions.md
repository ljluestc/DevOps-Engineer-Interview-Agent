# Kubernetes 面试题（40 题）

> 模板见 [../../docs/STANDARD.md](../../docs/STANDARD.md)。核心概念（CRI/CNI/CSI/对象模型）见 [../../basics/04-kubernetes-concepts.md](../../basics/04-kubernetes-concepts.md)。

---

### Q1. 容器底层原理？namespace 与 cgroup 各自解决什么？
- **难度**：🟡 中级
- **关键词**：namespace, cgroup, 容器隔离
- **概念速记**：容器 = 受限进程；namespace 隔离视图，cgroup 限制资源。
- **参考答案**：namespace 做视图隔离（pid/net/mnt…）；cgroup 做 cpu/mem/io/device 限制与统计。镜像分层（overlay2）只读层+可写层共享 base。容器不带独立内核。
- **易错点**：认为容器有独立内核（实际共享宿主）。
- **延伸**：[basics/04-kubernetes-concepts.md](../../basics/04-kubernetes-concepts.md)；linux Q7

### Q2. 镜像分层与存储驱动（overlay2）原理？
- **难度**：🟡 中级
- **关键词**：镜像分层, overlay2, CoW, 存储驱动
- **概念速记**：镜像多层只读，容器加可写层，CoW 写时复制。
- **参考答案**：lowerdir（镜像层）+ upperdir（容器层）+ merged（视图）。overlay2 主流默认；`docker system df` 看空间；层过多致镜像臃肿、inode 消耗。
- **易错点**：把数据写进容器层不挂卷，容器删数据丢。
- **延伸**：[basics/03-docker-basics.md](../../basics/03-docker-basics.md)；Q1

### Q3. Pod 从 kubectl apply 到 Running 的完整生命周期？
- **难度**：🔴 高级
- **关键词**：声明式, 调度, CRI, CNI, CSI
- **概念速记**：kubectl→apiserver→etcd→scheduler→kubelet→CRI/CNI/CSI 协同。
- **参考答案**：apiserver 鉴权/准入/校验→etcd 持久化→scheduler 绑定节点→kubelet watch→CRI 拉镜像→建 sandbox/容器→CNI 配网络、CSI 挂盘→探针→Running。失败点：Scheduler（Pending）、kubelet（镜像/挂载）、CNI（网络）。
- **易错点**：忽略准入控制（admission）阶段可能拒绝。
- **延伸**：[basics/04-kubernetes-concepts.md](../../basics/04-kubernetes-concepts.md)；Q6

### Q4. liveness / readiness / startup 探针区别与陷阱？
- **难度**：🟡 中级
- **关键词**：探针, liveness, readiness, startup
- **概念速记**：liveness 失败杀容器；readiness 失败摘流量不重启；startup 用于慢启动。
- **参考答案**：readiness 失败从 Endpoints 摘除（不重启）；liveness 失败重启；startup 期间禁用前两者。陷阱：把 ready 当 live 用掐流量；阈值不当引发重启雪崩；探针依赖下游误杀。
- **易错点**：readiness 探针当成 liveness 用。
- **延伸**：linux Q21（优雅停机）；Q3

### Q5. 排查 Pod 处于 Pending / CrashLoopBackOff / OOMKilled？
- **难度**：🟡 中级
- **关键词**：Pending, CrashLoopBackOff, OOMKilled, 排障
- **概念速记**：exit 137 通常是 cgroup OOM。
- **参考答案**：Pending：`describe` 看 Events（资源不足、PVC 未绑、污点、GPU 不可用）。CrashLoop：`logs --previous` 看上次崩溃。OOMKilled：exit 137、`describe` 看 OOMKilled，调大 limit 或查泄漏。
- **易错点**：混淆宿主机 OOM 与 cgroup OOM。
- **延伸**：linux Q3；Q7（资源 QoS）

### Q6. HPA 原理、指标与坑？和 VPA 怎么配合？
- **难度**：🔴 高级
- **关键词**：HPA, Metrics Server, 副本计算, VPA
- **概念速记**：HPA 按指标周期性调整副本数。
- **参考答案**：HPA 控制器周期性从 Metrics Server 拉使用率，按 `desired=current*(current/target)` 算副本调 RS。坑：指标延迟致震荡（配 downscale stabilization）、冷启动慢、自定义指标需 Prometheus Adapter、扩容受节点配额限。VPA 改 requests 需重建 Pod，通常与 HPA 不混用同资源。
- **易错点**：HPA 与 VPA 同时改同资源导致冲突。
- **延伸**：Q7、Q19（cluster-autoscaler）

### Q7. 节点 NotReady 怎么排查？
- **难度**：🟡 中级
- **关键词**：Node NotReady, kubelet, CNI, 证书
- **概念速记**：节点状态由 kubelet 上报，NotReady 即心跳/条件异常。
- **参考答案**：`describe node` 看 Conditions（MemoryPressure/DiskPressure/NetworkUnavailable）；`journalctl -u kubelet`；CNI DaemonSet 异常；etcd 健康；磁盘打满；时钟漂移/证书过期（kubelet cert 一年）。
- **易错点**：忽略 DiskPressure 导致 kubelet 无法写镜像/日志。
- **延伸**：Q5、Q21（证书）

### Q8. Service 的四种类型区别？kube-proxy 的 iptables 与 ipvs？
- **难度**：🟡 中级
- **关键词**：Service, ClusterIP, NodePort, LoadBalancer, ipvs
- **概念速记**：Service 是稳定访问入口（VIP）；kube-proxy 实现转发。
- **参考答案**：ClusterIP（集群内）、NodePort（每节点端口）、LoadBalancer（云 LB）、Headless（直返 Pod IP）。iptables 规则多刷新慢（O(n)）；ipvs 哈希表、连接级负载、性能更好（需 ip_vs 模块）。
- **易错点**：Headless 仍走 kube-proxy/ipvs 解析到 Pod IP。
- **延伸**：network Q16；Q10（Ingress）

### Q9. 亲和性/反亲和性、污点/容忍如何配合？topologySpreadConstraints？
- **难度**：🔴 高级
- **关键词**：affinity, taint, toleration, topologySpread
- **概念速记**：nodeSelector 硬约束；taint+toleration 专用节点；topologySpread 平滑分布。
- **参考答案**：nodeAffinity 软/硬选节点；podAntiAffinity 打散防单点；Taint+Toleration 用于 GPU/机房专用。`topologySpreadConstraints` 比反亲和更平滑按拓扑域均匀分布。
- **易错点**：反亲和性表达式写错导致 Pod 无法调度。
- **延伸**：Q6、Q19

### Q10. Ingress 与 Service 区别？Nginx/Traefik/Envoy 选型？
- **难度**：🟡 中级
- **关键词**：Ingress, 七层路由, Service Mesh
- **概念速记**：Service 四层内部负载；Ingress 七层 HTTP 路由。
- **参考答案**：Ingress 按域名/路径路由到 Service。Nginx Ingress（成熟、注解多）；Traefik（服务发现原生、简单）；Envoy/Istio（流量治理、灰度、mTLS，复杂）。
- **易错点**：以为 Ingress 替代 Service（两者层级不同）。
- **延伸**：Q8、network Q11

### Q11. Operator 与 CRD 解决什么问题？Reconcile 原理？
- **难度**：🔴 高级
- **关键词**：Operator, CRD, Reconcile, 声明式
- **概念速记**：CRD 扩展 API；Operator = CRD + 控制器，调谐让实际趋近期望。
- **参考答案**：watch 资源变更→入队→Reconcile（对比期望/实际→执行）→更新状态。用于有状态/复杂应用（etcd/Prometheus/DB）。
- **易错点**：Operator 不是「脚本」，核心是调谐循环与最终一致。
- **延伸**：Q3

### Q12. Service Mesh（Istio）架构与代价？eBPF 替代趋势？
- **难度**：⚫ 资深
- **关键词**：Istio, Envoy, sidecar, eBPF, mTLS
- **概念速记**：数据面 Envoy sidecar + 控制面 Istiod。
- **参考答案**：能力：流量治理、mTLS、自动埋点。代价：延迟（两跳）、资源、运维复杂。演进：Cilium/Hubble 用 eBPF 替代 sidecar 降开销。
- **易错点**：忽略 sidecar 两跳延迟对延迟敏感服务的影响。
- **延伸**：network Q16；Q14（Cilium）

### Q13. GitOps（ArgoCD / Flux）与传统推送式 CI/CD 区别？
- **难度**：🔴 高级
- **关键词**：GitOps, ArgoCD, 拉模型, drift
- **概念速记**：Git 为唯一事实源，集群向 Git 收敛（pull）。
- **参考答案**：ArgoCD 持续对比并自动同步/告警 drift。优势：审计、回滚（git revert）、一致性、防漂移。适合多集群。
- **易错点**：GitOps 不等于「用 Git 存 YAML」，关键是持续 reconcile。
- **延伸**：cicd-iac Q（CI/CD 流水线）

### Q14. CNI 插件 Calico / Flannel / Cilium 区别与选型？
- **难度**：🔴 高级
- **关键词**：CNI, Calico, Flannel, Cilium, eBPF
- **概念速记**：CNI 管容器网络；三者在性能/策略/可观测上差异大。
- **参考答案**：Flannel（vxlan，简单）；Calico（BGP/IPIP，网络策略强）；Cilium（eBPF，性能+可观测+替代 kube-proxy）。选型看规模、网络策略、可观测演进。
- **易错点**：小规模默认 Flannel 但后续要网络策略时迁移成本高。
- **延伸**：[basics/04-kubernetes-concepts.md](../../basics/04-kubernetes-concepts.md)；network Q14

### Q15. NetworkPolicy 怎么工作？默认放行还是拒绝？
- **难度**：🔴 高级
- **关键词**：NetworkPolicy, 零信任, 默认拒绝
- **概念速记**：Namespace 级防火墙（L3/L4，部分 L7）。
- **参考答案**：无策略全放行；有策略匹配 Pod 后，未被允许的被拒（对该 Pod deny by default）。依赖 CNI 支持（Calico/Cilium）。用于微服务零信任、租户隔离。
- **易错点**：以为 NetworkPolicy 默认拒绝所有（实际是默认放行）。
- **延伸**：Q14、cloud-security Q

### Q16. CSI / CRI / CNI 分别是什么？（高频）
- **难度**：🟡 中级
- **关键词**：CRI, CNI, CSI, 插件接口
- **概念速记**：三者都是 K8s 插件接口：R=Runtime、N=Network、S=Storage，解耦实现。
- **参考答案**：CRI 管容器运行时（containerd/CRI-O）；CNI 管网络（Calico/Cilium）；CSI 管存储（Ceph/EBS CSI）。K8s 只定义接口，具体实现由插件。
- **易错点**：混淆 CRI（接口）/ OCI（规范）/ 运行时（runc）。
- **延伸**：[basics/04-kubernetes-concepts.md](../../basics/04-kubernetes-concepts.md)；Q1、Q3

### Q17. PV / PVC / StorageClass / 动态供给原理？
- **难度**：🟡 中级
- **关键词**：PV, PVC, StorageClass, 动态供给
- **概念速记**：PVC 申请，SC 定义供给模板，动态供给自动建 PV。
- **参考答案**：PVC 引用 SC→Provisioner 自动建 PV（云盘/Ceph CSI）。关注 reclaimPolicy（Delete/Retain）、扩容、快照、跨区限制。
- **易错点**：Retain 的 PV 删 PVC 后需手动清理，否则泄漏。
- **延伸**：Q16

### Q18. 资源 requests / limits / QoS 三等级？
- **难度**：🔴 高级
- **关键词**：requests, limits, QoS, OOM 优先级
- **概念速记**：requests 调度依据，limits 上限；QoS 决定 OOM 时谁先死。
- **参考答案**：Guaranteed（req=lim，最不易杀）> Burstable > BestEffort（最先杀）。OOM 按 QoS 逆序。limits 过高致超卖，过低致频繁 OOM。
- **易错点**：limits 设得高以为安全，实则节点超卖风险。
- **延伸**：linux Q3；Q5

### Q19. 节点资源超卖怎么评估与防控？
- **难度**：🔴 高级
- **关键词**：超卖, LimitRange, ResourceQuota, 驱逐
- **概念速记**：调度按 requests 求和，limits 可超卖。
- **参考答案**：防控：LimitRange 设默认、ResourceQuota 限命名空间、监控实际利用率、保证系统预留（`systemReserved`/`kubeReserved`）、设 eviction 阈值（memory.available/nodefs.available）。
- **易错点**：不设系统预留导致 kubelet 自身被驱逐。
- **延伸**：Q6、Q18、Q20（驱逐）

### Q20. kubelet 的驱逐（eviction）机制？哪些信号触发？
- **难度**：🔴 高级
- **关键词**：eviction, 资源压力, 系统预留
- **概念速记**：kubelet 监控资源信号，超阈值按 QoS 驱逐 Pod。
- **参考答案**：信号：memory.available、nodefs.available、imagefs、pid。hard 立即、soft 有宽限期。关注磁盘满导致镜像无法清理→雪崩；合理设阈值与系统预留。
- **易错点**：磁盘满时驱逐依赖删镜像，恶性循环。
- **延伸**：Q18、Q19

### Q21. 集群证书过期怎么处理？
- **难度**：🔴 高级
- **关键词**：证书, kubeadm certs renew, 证书过期
- **参考答案**：K8s 证书默认 1 年。`kubeadm certs renew`（kubeadm 集群）/ 手动续签 / 轮换 kubeconfig；监控剩余（`kube-cert-exporter`）。纳入例行巡检防 apiserver 不可用。
- **易错点**：证书过期导致整个集群不可用，却未监控。
- **延伸**：Q7；cloud-security Q（证书管理）

### Q22. CSI / CRI / CNI 在节点上的组件分别跑在哪？
- **难度**：🔴 高级
- **关键词**：device plugin, CNI 二进制, CSI sidecar
- **概念速记**：CRI 在容器运行时；CNI 二进制在 /opt/cni/bin；CSI 以 sidecar 形式。
- **参考答案**：containerd/CRI-O 实现 CRI；CNI 插件二进制 + 配置在节点；CSI 以 DaemonSet/sidecar（external-provisioner/attacher/node-plugin）运行。
- **易错点**：不清楚 CNI 插件是节点上的二进制而非 apiserver 组件。
- **延伸**：Q16

### Q23. 如何用 kubectl 高效调试？
- **难度**：🟡 中级
- **关键词**：kubectl debug, exec, port-forward, 临时容器
- **概念速记**：ephemeral container 用于排障不重启 Pod。
- **参考答案**：`kubectl debug`（临时排障容器/拷节点）、`exec -it`、`port-forward`、`cp`、`logs -p`、`describe`/`get events`。`kubectl neat` 化简、`kubectl-tree` 看归属。
- **易错点**：直接改生产 Pod 镜像调试（应 ephemeral container）。
- **延伸**：Q5

### Q24. 镜像仓库（Harbor）的权限、签名与漏洞扫描？
- **难度**：🟡 中级
- **关键词**：Harbor, 镜像签名, 漏洞扫描, 垃圾回收
- **概念速记**：Harbor 是企业级镜像仓库，增强权限/安全/复制。
- **参考答案**：项目级 RBAC、镜像复制（异地）、Notary 内容信任（签名）、Trivy/Clair 扫描、垃圾回收。清理策略（保留最近 N）、配额、私有 CA。
- **易错点**：扫描不通过仍允许发布（应阻断流水线）。
- **延伸**：cicd-iac Q（供应链安全）；[basics/03-docker-basics.md](../../basics/03-docker-basics.md)

### Q25. RBAC 工作原理？如何最小权限授权？
- **难度**：🔴 高级
- **关键词**：RBAC, Role, RoleBinding, 最小权限
- **概念速记**：Role/ClusterRole（权限集）+ Binding（绑 SA/User）。
- **参考答案**：按命名空间/操作细分、用 SA 而非共享账号、定期审计（`kubectl auth can-i`）。结合 OPA/Gatekeeper 策略准入。
- **易错点**：图省事给 cluster-admin 通配。
- **延伸**：Q26（准入控制）；cloud-security Q（IAM）

### Q26. 准入控制（Admission Control）有哪些？OPA/Gatekeeper 做什么？
- **难度**：⚫ 资深
- **关键词**：准入控制, OPA, Gatekeeper, 策略即代码
- **概念速记**：对象持久化前拦截校验/修改。
- **参考答案**：内置（NamespaceLifecycle、LimitRanger、ResourceQuota、PodSecurity）。OPA/Gatekeeper 用 Rego 写自定义策略（禁 :latest、强制资源限制、镜像白名单），策略即代码、多集群一致。
- **易错点**：只靠 RBAC 不靠准入，无法防配置错误。
- **延伸**：Q25、cloud-security Q

### Q27. Pod 安全上下文（securityContext）与 PodSecurity 标准？
- **难度**：🔴 高级
- **关键词**：securityContext, PodSecurity, 非root, 特权容器
- **概念速记**：securityContext 配 runAsNonRoot、只读根、capabilities 丢弃。
- **参考答案**：配 runAsNonRoot、readOnlyRootFilesystem、drop capabilities、seccompProfile。PodSecurity 三级（privileged/baseline/restricted）。关注 root 容器、hostPath 风险。
- **易错点**：特权容器 + hostPath 等于近乎逃逸。
- **延伸**：Q25、cloud-security Q

### Q28. ConfigMap 与 Secret 管理与风险？
- **难度**：🟡 中级
- **关键词**：ConfigMap, Secret, 加密, External Secrets
- **概念速记**：ConfigMap 存配置；Secret 存密钥（默认 base64 非加密）。
- **参考答案**：风险：Secret 明文存 etcd（开 encryptionConfiguration）、体积上限 1MB、热更新需应用支持、误提交 Git。方案：External Secrets（Vault/AWS SM）、Sealed Secrets、CSI 挂载。
- **易错点**：以为 base64 等于加密。
- **延伸**：cloud-security Q（密钥管理）

### Q29. Deployment / StatefulSet / DaemonSet / Job / CronJob 区别？
- **难度**：🟡 中级
- **关键词**：工作负载, StatefulSet, 有状态
- **概念速记**：无状态用 Deployment；有状态用 StatefulSet（稳定标识/卷）。
- **参考答案**：Deployment（滚动更新）、StatefulSet（稳定网络标识/持久卷/有序启停）、DaemonSet（每节点 agent）、Job（一次性）、CronJob（定时）。StatefulSet 的 PVC 与升级策略（OnDelete/RollingUpdate）。
- **易错点**：用 Deployment 跑有状态 DB（Pod 重建丢标识）。
- **延伸**：Q17

### Q30. 滚动更新与蓝绿/金丝雀在 K8s 怎么实现？
- **难度**：🔴 高级
- **关键词**：滚动更新, 金丝雀, Argo Rollouts, 回滚
- **概念速记**：RollingUpdate 逐步替换；金丝雀按流量比例放量。
- **参考答案**：RollingUpdate 用 maxSurge/maxUnavailable 控节奏。金丝雀用 Argo Rollouts/Flagger/Istio 按流量比例+指标分析自动推进/回滚。蓝绿：两套 Deployment + Service 切换。强调自动分析与一键回滚。
- **易错点**：金丝雀只看部署成功不看错误率。
- **延伸**：cicd-iac Q（发布策略）；Q12

### Q31. Helm 与 Kustomize 区别？
- **难度**：🟡 中级
- **关键词**：Helm, Kustomize, 模板, overlay
- **概念速记**：Helm 模板化（values + 模板）；Kustomize 无模板 overlay 叠加。
- **参考答案**：Helm 有版本/chart 仓库，适合标准化分发；Kustomize 声明式 overlay（base+env），K8s 原生内置。多环境差异化用 Kustomize；复用 chart 用 Helm。
- **易错点**：用 Helm 硬写多环境导致 values 爆炸。
- **延伸**：cicd-iac Q（Git 工作流）

### Q32. 集群升级策略？如何不停机升级控制面与节点？
- **难度**：⚫ 资深
- **关键词**：集群升级, kubeadm, 节点排水, PDB
- **概念速记**：先备 etcd 快照，按版本 skew 顺序升级。
- **参考答案**：控制面：先备 etcd 快照，按 skew（≤1 minor）升 apiserver→controller→scheduler→kubelet。节点：drain --ignore-daemonsets + 滚动替换（托管节点池）。保证 PDB 满足、工作负载多副本。灰度小批量验证。
- **易错点**：跨多个 minor 直接升级导致不兼容。
- **延伸**：Q21（证书）、observability Q

### Q33. 多集群管理方案（Karmada / 跨云）？
- **难度**：⚫ 资深
- **关键词**：多集群, Karmada, 多活, 联邦
- **概念速记**：多集群分发与调度，用于多活/容灾/混合云。
- **参考答案**：Karmada/Cluster API/federation v2 做分发调度。关注集群间网络（专线/Submariner）、统一身份（OIDC）、配置分发、故障切换、GSLB。
- **易错点**：只做部署分发不做流量与故障切换。
- **延伸**：Q30、sre Q（多活）

### Q34. 如何用 eBPF 提升 K8s 可观测与安全（Cilium/Hubble）？
- **难度**：⚫ 资深
- **关键词**：eBPF, Cilium, Hubble, Tetragon
- **概念速记**：eBPF 内核挂点无侵入采集/拦截。
- **参考答案**：Cilium 用 eBPF 实现 CNI、替代 kube-proxy、L3-L7 策略；Hubble 服务地图/flow；Tetragon 运行时安全（提权/篡改检测）。
- **易错点**：eBPF 需较新内核，老集群不可用。
- **延伸**：Q14、network Q16

### Q35. K8s 多租户隔离方案？
- **难度**：⚫ 资深
- **关键词**：多租户, Namespace, vcluster, 软硬隔离
- **概念速记**：软隔离用 Namespace 策略；强隔离用 vcluster/独立集群。
- **参考答案**：软：Namespace + ResourceQuota + NetworkPolicy + RBAC + PodSecurity。强：vcluster（独立 apiserver）、独立集群、节点池物理隔离（污点+拓扑）。按安全等级权衡成本。
- **易错点**：仅靠 Namespace 名做隔离（无策略则互通）。
- **延伸**：Q15、Q25

### Q36. Serverless / Knative 在 K8s 上是什么？
- **难度**：🔴 高级
- **关键词**：Knative, Serverless, 缩到0, 事件驱动
- **概念速记**：基于 K8s 的 Serverless，自动扩缩（含缩到 0）。
- **参考答案**：自动扩缩、事件驱动、按请求计费。适用流量波动大/事件处理。运维关注冷启动、并发、资源、与网关集成。
- **易错点**：缩到 0 后首次请求冷启动延迟。
- **延伸**：Q6（HPA）

### Q37. 如何做 K8s 成本控制（FinOps）？
- **难度**：⚫ 资深
- **关键词**：FinOps, 右配, Spot, 闲置回收
- **概念速记**：降浪费=右配 + 弹性 + 回收。
- **参考答案**：右配 requests/limits（Goldilocks 建议）；HPA/VPA；缩到 0（Knative）；命名空间配额；Spot/抢占跑非核心；cluster-autoscaler/Karpenter；闲置检测回收；分账报表。
- **易错点**：只降单价不降闲置率。
- **延伸**：Q18、Q19、cloud-security Q（FinOps）

### Q38. 大规模集群（千节点）的运维挑战？
- **难度**：⚫ 资深
- **关键词**：大规模, etcd, 控制面, 监控数据量
- **概念速记**：规模上来后控制面/网络/监控都成瓶颈。
- **参考答案**：挑战：etcd 磁盘/quorum、apiserver 缓存、调度延迟、iptables 规则爆炸、监控数据量。应对：分片、多集群联邦、Karpenter、Cilium、Vertical Pod Autoscaler、独立 etcd 专盘。
- **易错点**：用 iptables 模式上大规模集群。
- **延伸**：Q14、Q20、Q21

### Q39. K8s 事件（Event）机制与告警怎么用？
- **难度**：🟡 中级
- **关键词**：Event, kube-eventer, 告警
- **概念速记**：Event 记录对象状态变更，存 etcd（默认 1h）。
- **参考答案**：关键 Event（FailedScheduling、Unhealthy、BackOff）告警。用 kube-eventer/EventRouter 转发 ES/Slack；避免 Event 风暴淹没。
- **易错点**：Event 默认只保留 1h，排旧故障查不到。
- **延伸**：observability Q（告警）

### Q40. etcd 原理、调优与脑裂预防？（进阶）
- **难度**：⚫ 资深
- **关键词**：etcd, Raft, MVCC, 快照, 脑裂
- **概念速记**：etcd 是 K8s 的「数据库」，基于 Raft 分布式 KV。
- **参考答案**：Raft 多数派（>N/2）防脑裂；SSD 专盘（磁盘 IO 决定稳定）；`--quota-backend-bytes` 控大小；`etcdctl defrag`/`snapshot save` 备份恢复。单集群建议 ≤5000 节点。监控 leader 切换、wal 延迟。
- **易错点**：etcd 跑在机械盘/网络盘上导致集群抖动。
- **延伸**：Q32、sre Q（多活/Raft）
