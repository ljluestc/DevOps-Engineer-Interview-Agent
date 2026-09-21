# Kubernetes 面试题（52 题）

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

### Q41. client-go 的 Informer 机制：Reflector / DeltaFIFO / Indexer 怎么协作？
- **难度**：🔴 高级
- **关键词**：Informer, Reflector, DeltaFIFO, Indexer, resync, List-Watch
- **概念速记**：Informer 是「本地缓存 + 事件通知」的组合，让控制器不必每次都打 API Server。六个核心组件：**SharedInformerFactory**（统一管理多资源）、**SharedIndexInformer**（单资源实现）、**Reflector**（执行 List & Watch）、**DeltaFIFO**（增量事件队列）、**Indexer**（带索引的本地缓存）、**SharedProcessor**（事件分发）。
- **参考答案**：
  1. 数据流：`Reflector` 先 **List** 全量（拿到 resourceVersion）写入 `DeltaFIFO`，再从该 version 起 **Watch** 增量；`DeltaFIFO` 弹出 Delta → `HandleDeltas` 同时做两件事：更新 `Indexer` 本地缓存、经 `SharedProcessor` 分发给注册的 EventHandler（Add/Update/Delete）。
  2. **Shared 的含义**：同一资源类型只维持一条 watch 连接和一份缓存，多个 controller 共享 → 避免每个 controller 各开一条 watch 把 API Server 打爆。
  3. **resync 不是重新 List**：定时把 Indexer 里的**存量对象**重新投递一次 Update 事件，用于兜底「事件丢了但缓存是对的」的场景。周期设太短会造成无谓的 reconcile 风暴；可用 `NewSharedInformerFactoryWithOptions` + `WithCustomResyncConfig` 给不同资源设不同周期。
  4. **Indexer 的价值**：除了 key（ns/name）查询，还能按自定义索引（如按 nodeName、按 label）O(1) 反查，避免全量遍历。
  5. **实战注意**：从 Lister/Indexer 拿到的对象是**共享指针**，直接改会污染缓存，必须 `DeepCopy()` 后再改；缓存有延迟，写操作要靠 API Server 的乐观锁（resourceVersion 冲突重试）而不是信任缓存。
- **易错点**：修改 Lister 返回的对象不 DeepCopy；把 resync 当成「重新拉全量」；每个 controller 各建一套 Informer 导致 API Server 压力暴涨。
- **延伸**：Q50、Q11、来源：[Kubernetes Handbook - client-go Informer 源码解析](https://jimmysong.io/book/kubernetes-handbook/develop-client-go-informer-sourcecode-analyse/)

### Q42. 自定义调度：Scheduler Framework 有哪些扩展点？怎么落地一个 GPU 优先调度插件？
- **难度**：🔴 高级
- **关键词**：Scheduler Framework, Filter, Score, Reserve, Permit, CycleState
- **概念速记**：Scheduler Framework 把调度流程切成一串有明确语义的扩展点，用**插件**编译进调度器，取代了已废弃的 scheduler-extender（HTTP 回调，延迟高）。
- **参考答案**：
  1. 主要扩展点与用途：
     | 插件类型 | 关键方法 | 阶段 |
     |---|---|---|
     | QueueSort | `Less()` | 决定 Pod 出队顺序（优先级） |
     | PreFilter | `PreFilter()` | Filter 前预计算，结果放 CycleState |
     | Filter | `Filter()` | 过滤不满足条件的节点（硬约束） |
     | PostFilter | `PostFilter()` | 无可用节点时的回退（如抢占） |
     | Score / NormalizeScore | `Score()` | 给节点打分并归一化（软约束） |
     | Reserve | `Reserve()` | 预留资源，防并发争抢 |
     | **Permit** | `Permit()` | **等待外部条件**——AI 作业 gang scheduling 的关键 |
     | Bind / PostBind | `Bind()` | 执行与后置处理 |
  2. **Permit 为什么重要**：分布式训练要求 N 个 Pod **要么全调度、要么都不调度**（gang scheduling），否则占着 GPU 互相等待造成死锁。Permit 可以让 Pod 停在「已预留但未绑定」状态，等同组凑齐再统一放行——Volcano / Kueue / KubeRay 都靠这个语义。
  3. **落地一个 GPU 优先插件**：实现 Filter（排除 GPU 型号/显存不满足的节点）+ Score（GPU 空闲多、拓扑亲和好的节点得分高），用 `KubeSchedulerConfiguration` 的 profile 启用，与默认插件共存。
  4. **最佳实践**：Filter/Score 里**禁止做耗时操作**（会拖慢整个调度吞吐）；插件方法必须幂等；跨阶段传数据用 `CycleState` 而不是全局变量；用 `framework.Handle` 复用调度器已有的 SharedInformer 缓存，不要自己再 List。
  5. **什么时候不自己写**：大多数 AI/批处理场景直接用 **Volcano / Kueue** 即可，自研插件的维护成本（要跟随 K8s 版本升级重编译）常被低估。
- **易错点**：用已废弃的 extender；在 Filter 里做远程调用；插件不幂等导致重复预留；忘了自定义调度器要靠 `spec.schedulerName` 才会生效。
- **延伸**：Q9、Q45、gpu-ai Q19、来源：[Kubernetes Handbook - Scheduler Framework](https://jimmysong.io/book/kubernetes-handbook/extend-scheduler-framework/)

### Q43. Mutating 与 Validating Webhook 的区别？生产上有哪些风险？
- **难度**：🔴 高级
- **关键词**：准入控制, MutatingWebhook, ValidatingWebhook, failurePolicy, 集群雪崩
- **概念速记**：准入链顺序是 **认证/鉴权 → Mutating → 对象 schema 校验 → Validating → 持久化到 etcd**。Mutating 可以**改写**对象（如 Istio 注入 sidecar），Validating 只能**放行或拒绝**，不能改。
- **参考答案**：
  1. 为什么 Mutating 在前：先让所有改写发生，再统一校验最终形态；否则校验过的对象又被改写，校验就失去意义。
  2. **最大的生产风险——webhook 挂了拖垮集群**：`failurePolicy: Fail` 时，webhook 服务不可用会导致**匹配范围内的所有写请求全部失败**。如果 webhook 自己就跑在集群里，一旦它所在节点故障，可能出现「Pod 起不来 → webhook 起不来」的死锁。
     - 缓解：`namespaceSelector` / `objectSelector` **精确限定作用范围**，尤其要**排除 `kube-system`**；webhook 多副本 + PDB + 反亲和；设合理 `timeoutSeconds`（默认 10s，建议 ≤5s）；核心链路评估用 `Ignore`（但要清楚这意味着策略可被绕过）。
  3. **Mutating 必须幂等**：同一对象可能被多次调用（reinvocation policy），注入逻辑要先判断是否已注入。
  4. **顺序不可控**：多个 Mutating webhook 之间没有稳定顺序保证，互相改同一字段会打架。
  5. **替代方案**：纯校验类策略优先用 **OPA/Gatekeeper 或 Kyverno**（声明式策略、自带审计与 dry-run），不要为每条规则手写一个 webhook；K8s 1.30+ 的 **ValidatingAdmissionPolicy**（CEL 表达式，跑在 apiserver 进程内）连 webhook 服务都不需要，没有可用性风险。
- **易错点**：不设 selector 导致 webhook 拦截 kube-system 把集群锁死；`failurePolicy: Fail` + 单副本；Mutating 不幂等造成重复注入。
- **延伸**：Q26、Q27、service-mesh Q5

### Q44. kubelet TLS Bootstrapping 是怎么工作的？证书怎么轮转？
- **难度**：🔴 高级
- **关键词**：TLS Bootstrapping, CSR, bootstrap token, 证书轮转, 自动审批
- **概念速记**：新节点加入集群时需要一份 kubelet 客户端证书，但不可能人工给每台机器签发。TLS Bootstrapping 让 kubelet 用一个**低权限的 bootstrap token** 换取**正式的客户端证书**。
- **参考答案**：
  1. 流程：kubelet 用 `bootstrap-kubeconfig`（内含 bootstrap token）连 apiserver → 自动创建一个 **CSR** 对象 → controller-manager 的 CSR 签发控制器（需配 `--cluster-signing-cert-file/--cluster-signing-key-file`）签发 → kubelet 取回证书写入 `--cert-dir`，后续用正式证书通信。
  2. **RBAC 是关键**：bootstrap token 所属的组要绑定
     - `system:node-bootstrapper`（允许创建 CSR）
     - `system:certificates.k8s.io:certificatesigningrequests:nodeclient`（允许**自动审批**首次申请）
     - `...:selfnodeclient`（允许**自动审批续期**）
     没配自动审批就要人工 `kubectl certificate approve`。
  3. **轮转**：kubelet 开 `--rotate-certificates`（客户端证书）与 `--rotate-server-certificates`（服务端证书），到期前自动发起新 CSR 续期，无需重装节点。服务端证书的自动审批**默认没有内置 approver**，需要额外部署或人工批。
  4. **排障**：
     ```bash
     kubectl get csr                      # Pending 说明没被审批
     kubectl certificate approve <csr>
     openssl x509 -in /var/lib/kubelet/pki/kubelet-client-current.pem -noout -dates
     ```
  5. **和集群证书过期的关系**：这解决的是 **kubelet 证书**；控制面组件证书（apiserver/etcd）由 kubeadm 管理，`kubeadm certs check-expiration` / `kubeadm certs renew all` 是另一套（见 Q21）。
- **易错点**：忘记绑定自动审批的 ClusterRole，节点加入后卡在 CSR Pending；只轮转了客户端证书，服务端证书过期导致 `kubectl logs/exec` 失败；bootstrap token 过期（默认 24h）后新节点加不进来。
- **延伸**：Q21、Q25、来源：[Kubernetes Handbook - TLS Bootstrapping](https://jimmysong.io/book/kubernetes-handbook/security-tls-bootstrapping/)

### Q45. DRA（动态资源分配）是什么？和 Device Plugin 有什么区别？
- **难度**：🔴 高级
- **关键词**：DRA, ResourceClaim, ResourceSlice, DeviceClass, Device Plugin
- **概念速记**：Device Plugin 把设备抽象成一个**可数的整数资源**（`nvidia.com/gpu: 1`）——只能表达「要几个」，无法表达「要什么样的」。**DRA（Dynamic Resource Allocation，`resource.k8s.io` API 组）** 用一套声明式对象让工作负载能按**属性**申请设备。
- **参考答案**：
  1. 四个核心对象：
     - **DeviceClass**：管理员/驱动定义的设备类别，可用 **CEL 表达式**按属性筛选。
     - **ResourceClaim**：一次具体的设备申请（「我要一块显存 ≥40GB、和 NIC 同 NUMA 的卡」）。
     - **ResourceClaimTemplate**：为每个 Pod 自动生成独立 ResourceClaim；Pod 删除时 Claim 一起回收。
     - **ResourceSlice**：**驱动**上报的、节点上实际可用的设备池。
  2. 分配流程：驱动创建 ResourceSlice → 用户创建 ResourceClaim(Template) 并在 Pod 里引用 → 调度器过滤 ResourceSlice 找到满足属性且节点可运行该 Pod 的设备 → 更新 ResourceClaim 记录分配结果（**first-fit**，按名字字典序遍历）→ Pod 绑定到该节点 → 驱动与 kubelet 通过 gRPC 完成设备准备。
  3. **相比 Device Plugin 的关键改进**：
     | | Device Plugin | DRA |
     |---|---|---|
     | 表达能力 | 只有数量 | 属性 + CEL 选择器 |
     | 共享 | 难（靠厂商自己实现 MIG/MPS） | 一个 Claim 可被多容器/多 Pod 共享 |
     | 拓扑 | 靠 Topology Manager 间接对齐 | 驱动可直接表达拓扑约束 |
     | 参数化 | 无（只能靠环境变量/注解） | Claim 里带配置参数 |
  4. **注意点**：`spec.nodeName` 直接指定节点的 Pod **绕过调度器**，其 ResourceClaim 不会被分配，kubelet 会一直失败重试；DRA 从 1.34 起 `resource.k8s.io/v1` GA，但**真正可用取决于厂商驱动的成熟度**，生产上目前多数仍是 Device Plugin + HAMi 这类方案。
- **易错点**：以为 DRA 能立刻替代 Device Plugin（依赖驱动支持）；用 nodeName 静态调度带 Claim 的 Pod；ResourceClaim（共享、需手动清理）与 ResourceClaimTemplate（每 Pod 独立、自动回收）混用。
- **延伸**：Q46、gpu-ai Q3、Q21、来源：[Kubernetes 官方文档 - Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)

### Q46. Topology Manager 的 scope 与 policy 分别有哪些？选错会怎样？
- **难度**：🔴 高级
- **关键词**：Topology Manager, NUMA, Hint Provider, single-numa-node, 拓扑对齐
- **概念速记**：在 Topology Manager 出现之前，**CPU Manager 和 Device Manager 各自独立分配**，结果可能把 CPU 分在 NUMA 0、GPU/网卡分在 NUMA 1，跨 socket 访问带来额外延迟。Topology Manager 是 **kubelet 内的协调者**，从各 **Hint Provider**（CPU Manager、Device Manager、Memory Manager）收集 NUMA 位掩码建议，收敛出一个统一的分配决策。
- **参考答案**：
  1. **两种 scope**（`topologyManagerScope`）：
     - `container`（默认）：逐容器独立对齐，同 Pod 的容器可能落在不同 NUMA。
     - `pod`：整个 Pod 作为一个整体对齐，Pod 内所有容器得到**相同**的 NUMA 决策——多容器协同的 AI 任务应选这个。
  2. **四种 policy**（`--topology-manager-policy`）：
     - `none`（默认）：不做对齐。
     - `best-effort`：记录首选 NUMA，**即使不满足也接纳** Pod。
     - `restricted`：不满足首选亲和性就**拒绝** Pod。
     - `single-numa-node`：必须能在**单个 NUMA 节点**上满足，否则拒绝——延迟最敏感的场景用它。
  3. **最大的坑——被拒绝的 Pod 不会被重新调度**：`restricted`/`single-numa-node` 拒绝 Pod 时，Pod 进入 `Terminated` 并报 `Topology Affinity` 错误，**调度器不会自动换个节点重试**。必须用 Deployment/ReplicaSet（或外部控制循环）来触发重建，否则裸 Pod 直接死在那里。
  4. **生效前提**：只对 **Guaranteed QoS**（CPU 是整数、requests==limits）的 Pod 有意义；还需要 CPU Manager policy 设为 `static`。Burstable/BestEffort Pod 拿不到独占 CPU，谈不上对齐。
  5. **策略选项**：`prefer-closest-numa-nodes`（无法单 NUMA 时优先选距离近的组合）、`max-allowable-numa-nodes`（限制参与计算的 NUMA 数，防止大机器上组合爆炸）。
- **易错点**：用裸 Pod + `single-numa-node`，被拒后永久卡死；忘了必须是 Guaranteed QoS；在 8 卡机上设过严策略导致大量 Pod 无法调度。
- **延伸**：Q45、Q18、gpu-ai Q22、linux Q10、来源：[Kubernetes 官方文档 - Topology Manager](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/)

### Q47. pause 容器（infra container）到底做什么？
- **难度**：🟡 中级
- **关键词**：pause, infra container, namespace 共享, 僵尸进程回收
- **概念速记**：每个 Pod 都有一个几乎不占资源的 `pause` 容器，它是 Pod 内所有 namespace（net/ipc/uts，可选 pid）的**持有者**和**生命周期锚点**。
- **参考答案**：
  1. **namespace 的锚**：pause 最先启动并创建 network namespace，业务容器都 join 进来 —— 这就是同 Pod 容器能用 `localhost` 互访、共享同一个 Pod IP 的原因。**业务容器崩溃重启时 namespace 不变，Pod IP 也就不变**；如果没有 pause，第一个容器挂掉会把 namespace 带走。
  2. **回收僵尸进程**：共享 PID namespace（`shareProcessNamespace: true`）时，pause 作为 PID 1 负责 reap 孤儿进程，防止僵尸进程堆积。
  3. **极简实现**：源码就是「设置信号处理 → `pause()` 系统调用挂起」，镜像只有几百 KB，几乎不占 CPU/内存。
  4. **运维相关**：`crictl ps` 默认不显示它，`crictl pods` 才看得到沙箱；pause 镜像拉不下来（国内网络/私有仓库未同步）会导致**所有 Pod 卡在 ContainerCreating**，报 `sandbox` 创建失败——这是离线环境最常见的坑，要在 kubelet 的 `--pod-infra-container-image` 或 containerd 配置里指向内网地址。
- **易错点**：不知道它的存在，排查「Pod 卡在 ContainerCreating」时忽略 sandbox 镜像；以为它会消耗可观资源。
- **延伸**：Q1、Q3、Q22

### Q48. ConfigMap / Secret 挂载后能热更新吗？延迟多久？Secret 有哪些真实风险？
- **难度**：🟡 中级
- **关键词**：ConfigMap 热更新, subPath, kubelet sync, envFrom, etcd 明文
- **概念速记**：**以 volume 方式挂载**的 ConfigMap/Secret 会被 kubelet 周期性同步，内容能自动更新；**以环境变量注入**的则在容器启动时固化，**永远不会更新**。
- **参考答案**：
  1. **更新延迟**：kubelet 的同步周期（`--sync-frequency`，默认 1min）+ 缓存 TTL，实际生效通常在 **1～2 分钟**量级，不是实时。要立刻生效只能重启 Pod。
  2. **subPath 挂载不会更新**（高频坑）：用 `subPath` 挂单个文件时，kubelet 是把文件直接 bind mount 进去，后续更新不会反映到容器内。要热更新必须挂目录。
  3. **应用还得自己 reload**：文件变了不等于进程重新读了。要么应用自己 watch 文件（inotify），要么用 sidecar（如 `reloader`）检测变更后触发滚动更新。
  4. **推荐做法——不可变 + 滚动**：给 ConfigMap 加内容哈希后缀（`app-config-a1b2c3`），改配置就是发一个新 ConfigMap 并更新 Deployment 引用 → 触发滚动更新。好处是**变更有版本、可回滚、生效确定**。`immutable: true` 还能显著降低 kubelet 的 watch 开销。
  5. **Secret 的真实风险**：
     - etcd 里默认是 **base64 编码而非加密** → 必须开 `EncryptionConfiguration`（静态加密），并保护 etcd 备份文件。
     - 能读某 namespace Secret 的 RBAC 权限 ≈ 拿到该 namespace 所有凭据，授权要精细。
     - 不要 `envFrom` 整个 Secret（会进 `/proc/<pid>/environ`、崩溃转储和日志）。
     - 生产建议用外部密钥管理（Vault / 云 KMS + External Secrets Operator / Secrets Store CSI Driver），K8s 里只留短期凭据。
- **易错点**：用 subPath 后以为能热更新；用环境变量注入后期待自动更新；以为 Secret 在 etcd 里是加密的。
- **延伸**：Q28、cloud-security Q7

### Q49. ServiceAccount 的投影令牌（projected token）与旧版 Secret token 有什么区别？
- **难度**：🔴 高级
- **关键词**：BoundServiceAccountToken, projected volume, audience, TokenRequest API, exp
- **概念速记**：老版本里每个 ServiceAccount 会自动生成一个 Secret，里面是**永不过期、无受众限制**的 JWT；1.24 起默认改用 **TokenRequest API 签发的投影令牌**——有过期时间、绑定受众（audience）、绑定 Pod 对象。
- **参考答案**：
  1. **旧 token 的问题**：永久有效（泄露即永久失效风险）、任何服务都能拿去用（无 audience 校验）、Pod 删了 token 还在、每个 SA 都产生一个 Secret 造成 etcd 膨胀。
  2. **投影令牌的改进**：
     - `expirationSeconds`：短期有效，kubelet 在到期前自动刷新并重写文件（默认 1h，通常在 80% 生命周期时轮转）。
     - `audience`：令牌只对指定受众有效，交给第三方（如 Vault、SPIRE、云厂商 OIDC）时对方必须校验 audience，防止令牌被跨服务重放。
     - **绑定 Pod**：Pod 删除后令牌立即失效。
  3. **对应用的要求**：**必须每次使用前重新读文件**，不能启动时读一次缓存到内存——否则 1 小时后 401。很多 SDK 已内置（client-go 的 `BoundServiceAccountTokenVolume` 处理），自己写 HTTP 调用的要注意。
  4. **典型用途**：
     - **云上 IRSA / Workload Identity**：Pod 用投影令牌（audience 设为云厂商 STS）换取临时云凭据，从而不需要在集群里存长期 AK/SK。
     - **SPIRE 节点/工作负载证明**（见 service-mesh Q8）。
  5. **仍需旧 token 时**：手动创建 `kubernetes.io/service-account-token` 类型的 Secret，或用 `kubectl create token <sa> --duration=...` 临时签发。
- **易错点**：应用把 token 读一次就缓存，1 小时后全线 401；给第三方用时不设/不校验 audience；升级到 1.24+ 后依赖「SA 自动生成 Secret」的老脚本失效。
- **延伸**：Q25、Q28、cloud-security Q2、service-mesh Q8

### Q50. 写一个生产级 Controller：幂等、限速、Finalizer、status 冲突怎么处理？
- **难度**：⚫ 资深
- **关键词**：Reconcile, 幂等, workqueue 限速, Finalizer, 乐观锁冲突, observedGeneration
- **概念速记**：Controller 的核心是**水平触发（level-triggered）**的调谐循环——每次 Reconcile 都应该「读当前实际状态 → 与期望状态比对 → 补差」，而不是「响应这个事件做什么动作」。
- **参考答案**：
  1. **幂等是底线**：同一个对象会被反复 Reconcile（resync、重启、事件重复、status 更新又触发一次）。永远不要写「收到 Add 就创建」，要写「不存在则创建，存在且不一致则更新」。创建子资源用**确定性名字** + `CreateOrUpdate`，避免重复创建。
  2. **限速队列**：用 `workqueue.RateLimitingInterface`。失败返回 error → 指数退避重试（默认 5ms 起，上限 1000s）；需要定时复查返回 `RequeueAfter`。**不要在 Reconcile 里写 sleep 循环**，那会占死 worker。
  3. **Finalizer 做清理**：需要在对象删除前清理外部资源（云上 LB、DNS 记录、外部数据库）时加 Finalizer。要点：
     - 对象被删时 `DeletionTimestamp` 非空，此时执行清理，**清理成功后一定要移除 Finalizer**，否则对象永久卡在 Terminating。
     - 清理逻辑本身必须幂等且能容忍外部资源已不存在。
     - 运维兜底：`kubectl patch <obj> -p '{"metadata":{"finalizers":null}}' --type=merge`（但这会泄漏外部资源，是最后手段）。
  4. **status 更新冲突**：status 要用 `Status().Update()` 或 `Status().Patch()`（走 status 子资源，不会和 spec 互相覆盖）。遇到 `Conflict`（resourceVersion 过期）**不要盲目重试写**，而是重新 Get 最新对象再改——或直接返回 error 让队列重新调谐。
  5. **`observedGeneration` 模式**：在 status 里记录已处理的 `metadata.generation`，使用者据此判断「controller 是否已经看到我最新的 spec」，避免读到陈旧状态。
  6. **其他生产要点**：多副本要用 **leader election**；Watch 的资源要设 `Owns()` 建立 ownerReference（既能级联删除，也能让子资源变更触发父对象 Reconcile）；对象数量大时用 label selector 缩小 informer 范围；所有外部调用要有超时。
- **易错点**：把 Reconcile 写成「边缘触发」的事件处理器；Finalizer 加了但异常路径不移除，导致 namespace 永远删不掉；直接 `Update()` 整个对象把别人的 spec 改动覆盖掉；不做 leader election 导致多副本互相打架。
- **延伸**：Q11、Q41、Q43

### Q51. 单集群上万节点、百万容器的控制面怎么撑住？阿里巴巴 2019 双 11 的做法给了哪些可复用的套路？
- **难度**：⚫ 资深
- **关键词**：List & Watch, Bookmark, watch cache, 一致性读, 索引, 面向终态, 原地升级, OpenKruise, 负载感知调度
- **概念速记**：
  - **List & Watch 风暴**：informer 首次或断线后要 `List` 全量再 `Watch` 增量；网络抖动让成千上万 kubelet 同时重 List，apiserver 与 etcd 被瞬间打爆。
  - **Watch Bookmark**：apiserver 周期性推送「当前 resourceVersion」的空事件，让客户端的 rv 不至于太旧；重连时 rv 仍在 watch cache 窗口内，就不会触发 `too old resource version` 从而全量重 List。
  - **面向终态（declarative / desired state）**：运维平台不再「按流程逐台操作」，而是提交期望状态，由 controller 持续调谐；风险控制随之要从「流程卡点」变成「controller 级限流与熔断」。
- **问题**：阿里 2019 年 k8s 体系已达「数十个集群、数十万节点、单集群 10,000 节点、超百万容器」。这种规模下 apiserver / etcd / 调度器分别会先在哪里出问题？他们做了哪些优化？其中哪些是普通团队在千节点规模也该做的？
- **参考答案**：
  1. **先讲瓶颈在哪**：单集群万节点时，压力顺序通常是 **apiserver 的 List 与 watch 扇出 → etcd 的读写与网络 → webhook 长尾 → 调度吞吐**。阿里的做法是先把**监控大盘 + 压测平台**建起来（RT/QPS、资源使用率、gRPC、长连接分布、队列长度），先度量再优化。
  2. **接入层与连接均衡**：apiserver 多副本前面挂 SLB，但 HTTP/2 长连接会「粘」在某个副本上，他们做了**周期性重建连接**让 kubelet 的连接重新均衡；webhook 链路上把 HTTP/2 改回 HTTP/1.1 并给 webhook 设 `maxSurge`，避免升级期间 webhook 成为 apiserver 的长尾；同时升级了 etcd client（v3.3.15）修正连接层问题。
  3. **List & Watch 优化**：核心手段是 **Bookmark**——apiserver 把 watch cache 中较新的 rv 通过 bookmark 事件推给 informer，网络抖动后 informer 用较新的 rv 重连即可，不必全量 List；这也是社区 `WatchBookmark` 特性的由来。
  4. **读路径走缓存 + 索引**：`List`/`Get` 带 `resourceVersion=0` 走 apiserver watch cache 而不是穿透 etcd；阿里在 watch cache 上支持**动态新增索引**（nodeName、namespace、labels 等），让「按节点列 Pod」从遍历过滤变成索引命中（他们给的数字是 5 s → 0.3 s）；同时实现**缓存一致性读**：先从 etcd 拿一个 rv@t0，等 cache 追上（rv > rv@t0）再返回，保证读到的不是陈旧数据。
  5. **面向终态的风险控制**：决策分散到 controller / operator / rescheduler 之后，要在 **apiserver admission 层和 kubelet 层各加一道限流与熔断**（例如 3000 实例升级设最大不可用数 200），否则一个 controller 的 bug 会瞬间把集群推向错误的终态。
  6. **工作负载层的规模化能力**：阿里把「容器原地升级（保持 IP / 卷）、并发更新与容错暂停、镜像预热与按需下载、Sidecar 与业务容器分离升级」沉淀为 **OpenKruise**（CloneSet / AdvancedStatefulSet / SidecarSet / BroadcastJob），原生 Deployment 的「重建 Pod」在万级实例场景成本过高。
  7. **调度**：CPU 精细化分配、应用按 AZ / 节点打散、CPU 敏感 Pod 打散、**节点负载感知**与**应用峰值 CPU 预测**（离线统计写成 CR，调度器读取）——即从「按 request 排」转为「按真实负载与预测排」。
  8. **千节点规模也该做的子集**：开 watch bookmark；informer 用 `resourceVersion=0` 与字段/标签选择器；webhook 加超时与失败策略并监控 P99；apiserver 与 etcd 分开监控并做压测；升级类操作一律带 `maxUnavailable` 类熔断；用标准的原地升级 / 分批发布工具而不是自研脚本。
- **易错点**：把「加 apiserver 副本」当万能药（长连接不均衡时副本越多越浪费）；不知道 `resourceVersion=0` 与精确 rv 的语义差别（缓存读 vs 一致性读）；只谈 etcd 调优不谈 List & Watch；把 OpenKruise 说成「另一个 Helm」。
- **延伸**：Q38、Q40、Q41、Q50、来源：阿里巴巴云原生应用平台《阿里巴巴 k8s 超大规模实践》（曾凡松 / 汪萌海，2019 KubeCon China 演讲，本地 PDF 存档）、[OpenKruise](https://openkruise.io)、[OAM](https://openappmodel.io)

### Q52. 云原生块存储怎么选？DRBD / LINSTOR / Piraeus 的超融合方案与 Ceph、Longhorn、OpenEBS 有什么本质区别？
- **难度**：🔴 高级
- **关键词**：DRBD, LINSTOR, Piraeus, 超融合 hyper-converged, 数据本地性 data locality, 同步 / 异步复制, 仲裁 quorum, CSI
- **概念速记**：
  - **DRBD（Distributed Replicated Block Device）**：Linux 内核模块（2.6.33 起进入主线），把块设备按块级别实时复制到其他节点，即「网络 RAID 1」；支持同步 / 异步复制，DRBD 9 最多 32 副本、支持双主与「两有盘 + 一无盘仲裁」拓扑。
  - **LINSTOR**：管理集群里 LVM / ZFS 卷与 DRBD 资源的编排服务：`linstor-controller`（集群配置数据库，只能一个活跃）+ 每节点 `linstor-satellite`（无状态代理，调 `drbdadm`/`lvcreate`/`zpool`）+ `linstor-client`（REST）。
  - **Piraeus**：CNCF 项目，用 CSI 把 LINSTOR/DRBD 接进 K8s：CSI 驱动、Operator、HA Controller、调度器扩展（`linstor-scheduler-extender`）、`drbd-shutdown-guard`、`kubectl-linstor` 插件。
- **问题**：数据库要上 K8s，团队在 Ceph RBD、Longhorn、OpenEBS Mayastor 和 Piraeus + LINSTOR + DRBD 之间纠结。你怎么给出选型建议？DRBD 方案的性能优势从哪来，代价又是什么？
- **参考答案**：
  1. **先按存储类型分层**：本地卷（OpenEBS LocalPath / LVM / ZFS、Carina）适合可重建的有副本数据（Kafka、ES）；分布式文件（CephFS、JuiceFS、NFS）适合共享读写；**分布式块**（Ceph RBD、Longhorn、OpenEBS Mayastor / cStor、Piraeus + LINSTOR + DRBD）适合数据库；对象（Ceph RGW、MinIO）走 S3。数据库的问题域是「块存储 + 高 IOPS + 低尾延迟」。
  2. **DRBD 方案的性能优势来自三点**：① **内核态复制**——DRBD 是内核驱动，位于 I/O 栈底部，通过 TCP/IP 或 RDMA 做块级同步，没有用户态多副本协议的开销；② **超融合 + 数据本地性**——Piraeus 的调度器扩展只把 Pod 调度到**本地有副本**的节点，读走本地盘、写只多一跳复制；③ 同步算法只同步变化块、按磁盘自然布局顺序同步、可变速率与校验和。厂商在 3 节点 Ampere 集群上给出的数字是随机 4K 读 2,550 万 IOPS、顺序读 103 GiB/s（供参考量级，不是承诺）。
  3. **Ceph 的取舍**：用户态、多副本强一致同步、CRUSH 无中心，扩展性和统一（块 / 文件 / 对象）是强项；代价是 CPU / 内存随卷数线性增长、跨主机同步带来网络延迟，**对高性能数据库与虚拟化负载常常不够用**。Longhorn 与 OpenEBS 同样是用户态复制引擎（Mayastor 用 SPDK/NVMe-oF 例外），运维更简单但单卷性能上限低于内核态方案。
  4. **DRBD 方案的代价必须讲**：需要在**每个节点编译 / 安装内核模块**（内核升级要同步跟进，通常用 DKMS 或供应商工具）；副本数受限于「有盘节点」数量，数据不会像 Ceph 那样自动散布到全集群；脑裂防护靠 quorum（推荐两有盘 + 一无盘仲裁节点）；跨站点要靠 DRBD Proxy 做压缩缓存的异步复制。
  5. **落地要点**：复制走**独立网卡**（示例把管理网与 DRBD 复制网分开）；调大 `net.core.rmem_max` / `wmem_max`（示例 16 MB）；NVMe 用 LVM 管理（性能最好但没有快照），SATA / SAS 用 ZFS（在线换盘、校验自愈、快照）；LINSTOR controller 自己的数据库放在独立 StorageClass（例如 local-path）上，别形成「存储依赖存储」的环；控制面用 Rancher / Sealos 之类工具装集群时，记得删除 `--port=0` 类阻断健康检查的旧参数。
  6. **给出的推荐**：单机房、数据库为主、追求 IOPS 与尾延迟 → Piraeus + LINSTOR + DRBD；多类型存储统一供给、容量优先、团队有 Ceph 经验 → Rook-Ceph；小集群求简单 → Longhorn；已经在用 NVMe-oF、追求极致 → Mayastor。任何一个都要先用 `fio` 在目标节点跑基线再做决定。
- **易错点**：把 DRBD 说成「文件系统」（它是块设备）；认为多副本就一定安全却不配 quorum；忽视内核模块与内核升级的耦合；只比 IOPS 不比运维能力（备份、快照、扩容、监控）。
- **延伸**：Q16、Q17、middleware（数据库高可用）、来源：全速云《云原生存储实战课程：Linstor + DRBD + Piraeus + KubeStorage 入门篇》（2023，本地 PDF 存档）、[LINSTOR 用户指南](https://linbit.com/drbd-user-guide/linstor-guide-1_0-cn/)、[DRBD 9 用户指南](https://linbit.com/drbd-user-guide/drbd-guide-9_0-cn/)、[Piraeus](https://piraeus.io)
