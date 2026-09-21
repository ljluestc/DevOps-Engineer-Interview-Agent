# 运维分模块面试题库（Question Bank）

> 标准化模板：`难度` / `关键词` / `概念速记` / `问题` / `参考要点` / `易错点` / `延伸`。
> 难度图例：🟢 初级 ｜ 🟡 中级 ｜ 🔴 高级 ｜ ⚫ 资深/架构/高管。
> 本文件为「运维面试教练」出题权威来源；完整 200 题见开源仓库 `ops-interview`。

---

## linux（Linux 系统 / 内核 / Shell）

**Q-L1 🟢 平均负载**
- 关键词：load average、R/D 状态、CPU vs IO
- 概念速记：load = 可运行 + 不可中断进程平均数，不等于 CPU 使用率。
- 问题：服务器 load 很高但 CPU 使用率不高，可能是什么原因？怎么定位？
- 参考要点：区分 R（运行/就绪）与 D（不可中断 IO 等待）；用 `vmstat 1` 看 `r`/`b`/`wa`，`top` 看 `D` 状态进程，iostat 看磁盘；可能是 IO 瓶颈、锁竞争、或大量 D 状态进程。
- 易错点：把 load 高直接等同于 CPU 不够。
- 延伸：容器里 load 看的是宿主机还是 cgroup？

**Q-L2 🟡 OOM 排查**
- 关键词：OOM Killer、cgroup memory、dmesg
- 概念速记：OOM 分内核 Killer 与 cgroup 限制两类，容器多是后者。
- 问题：一个容器进程被杀了，怎么判断是 OOM 还是别的？
- 参考要点：`dmesg | grep -i oom`、`/sys/fs/cgroup/.../memory.events` 的 `oom_kill`；看退出码 137（SIGKILL）；区分宿主机内存耗尽 vs limits.memory 触发。
- 易错点：137 不一定是 OOM，也可能是 `docker kill`；需看事件来源。
- 延伸：如何区分 cgroup v1/v2 的 OOM 计数文件？

**Q-L3 🟡 零拷贝**
- 关键词：sendfile、COW、上下文切换
- 概念速记：减少用户态⇄内核态拷贝与切换，提升 IO 吞吐。
- 问题：Nginx 静态文件服务为什么快？零拷贝在其中起什么作用？
- 参考要点：传统 read+write 4 次拷贝；`sendfile` 降到 2 次甚至配合 DMA gather 1 次；减少上下文切换。
- 易错点：零拷贝不是「零次拷贝」，而是减少 CPU 参与拷贝。
- 延伸：kafka/消息队列如何利用零拷贝？

**Q-L4 🔴 epoll ET/LT**
- 关键词：边缘触发、水平触发、EAGAIN
- 问题：epoll 的 ET 和 LT 有什么区别？ET 模式下要注意什么？
- 参考要点：LT 只要就绪就通知（可偷懒）；ET 只在状态变化时通知一次，必须循环 `read` 到 `EAGAIN`，否则丢事件；ET 性能更好但更易写错。
- 易错点：ET 下只 read 一次就返回，导致后续数据不被处理。
- 延伸：为什么 Nginx 用 ET？

**Q-L5 🔴 cgroup v1 vs v2**
- 关键词：统一层级、PSI、memory.max
- 问题：cgroup v1 和 v2 主要区别？为什么新发行版默认 v2？
- 参考要点：v1 各子系统独立层级，v2 单一统一树；v2 提供 PSI（压力阻塞信息）、更清晰接口；K8s 新版本要求/推荐 v2。
- 易错点：以为 v2 只是目录变化，忽略 PSI 对调度/驱逐的价值。
- 延伸：kubelet 如何用 PSI 做节点压力驱逐？

**Q-L6 🟡 systemd 排障**
- 关键词：unit、journalctl、依赖
- 问题：一个 systemd 服务起不来，你的排查步骤？
- 参考要点：`systemctl status <svc>` 看状态/主进程退出码；`journalctl -u <svc> -xe` 看日志；检查 `After=/Requires=` 依赖；`systemd-analyze verify` 校验单元文件。
- 易错点：只看 status 不看 journal，漏掉启动脚本报错。
- 延伸：Type=simple/forking/notify 区别？

**Q-L7 ⚫ 内核参数调优**
- 关键词：sysctl、文件句柄、TCP 栈
- 问题：高并发服务端常见需要调的内核参数有哪些？
- 参考要点：`fs.file-max`/`ulimit -n`、`net.core.somaxconn`、`net.ipv4.tcp_tw_reuse`、`tcp_max_syn_backlog`、`vm.swappiness`、`net.ipv4.ip_local_port_range`。
- 易错点：只调文件句柄忘改 systemd 的 `LimitNOFILE`；调 `tcp_tw_recycle`（已废弃且危险）。
- 延伸：如何验证参数在容器 namespaces 里的可见性？

**Q-L8 🟡 Shell 排障**
- 关键词：set -euxo、管道、信号
- 问题：`set -e` 在脚本里有什么坑？管道中某段失败会被捕获吗？
- 参考要点：`set -e` 在命令失败即退出，但管道整体失败需 `set -o pipefail`；`set -u` 防未定义变量；常见坑：命令在 `if` 条件里失败不触发 `-e`。
- 易错点：以为 `set -e` 能捕获管道中间段失败。
- 延伸：如何安全地在脚本里处理 trap 清理？

---

## network（网络 / TCP-IP / DNS / 负载均衡）

**Q-N1 🟢 TCP 握手挥手**
- 关键词：三次握手、TIME_WAIT、2*MSL
- 问题：为什么 TCP 握手三次、挥手四次？TIME_WAIT 有什么作用？
- 参考要点：全双工需双向各建/关；TIME_WAIT 确保最后 ACK 可达并让旧报文消亡（2*MSL）。
- 易错点：把四次挥手说成必须四次（可捎带变三次）；忽视 TIME_WAIT 大量占用端口。
- 延伸：高并发短连接如何缓解 TIME_WAIT？

**Q-N2 🟡 半连接/全连接队列**
- 关键词：SYN queue、accept queue、backlog
- 问题：大量连接失败，怀疑队列溢出，怎么排查？
- 参考要点：`netstat -s` 看 `SYNs to listened sockets ignored`（半连接）；`ss -lnt` 看 `Recv-Q` 与 `Send-Q`（全连接）；调 `tcp_max_syn_backlog` 与 `somaxconn` 及应用 `listen(backlog)`。
- 易错点：只调内核忘改应用 backlog；二者取最小值。
- 延伸：SYN Flood 与 syncookie。

**Q-N3 🟡 DNS 解析链路**
- 关键词：resolv.conf、nscd、TTL、递归
- 问题：容器内访问域名很慢或偶发失败，怎么排查 DNS？
- 参考要点：`/etc/resolv.conf` 的 nameserver（K8s 里是 CoreDNS）；`dig`/`nslookup` 测；看 TTL 与缓存（nscd/systemd-resolved）；CoreDNS 压力大或 `ndots` 配置导致多余查询。
- 易错点：忽略 `options ndots:5` 导致内部域名每次多查。
- 延伸：CoreDNS 高负载优化？

**Q-N4 🔴 HTTP/2 与队头阻塞**
- 关键词：多路复用、HPACK、QUIC
- 问题：HTTP/2 解决了 HTTP/1.1 的什么？还有什么没解决？
- 参考要点：1.1 队头阻塞（连接级）+ 多连接；2 多路复用单连接、HPACK 头部压缩；但仍受 TCP 层队头阻塞；HTTP/3(QUIC) 用 UDP 解决。
- 易错点：以为 HTTP/2 完全解决队头阻塞（只是应用层）。
- 延伸：gRPC 为什么选 HTTP/2？

**Q-N5 🔴 LVS / 四层负载**
- 关键词：NAT/DR/TUN、VIP、一致性哈希
- 问题：LVS 的 NAT、DR、TUN 三种模式区别？各自适用场景？
- 参考要点：NAT（改目的 IP，回程经 Director，瓶颈）；DR（改 MAC，回程直连 client，需同二层）；TUN（IP 隧道，跨网段）；性能 DR > TUN > NAT。
- 易错点：DR 模式要求 RS 配 VIP 且抑制 ARP。
- 延伸：与 Nginx/HAProxy 七层对比？

**Q-N6 🟡 MTU / 分片**
- 关键词：1500、DF、GRE/VXLAN
- 问题：VPN/容器网络里偶发大包不通，可能和 MTU 有关吗？
- 参考要点：隧道（VXLAN/GRE）封装增加开销，需调小 MTU（常 1450/1400）；DF 位置位时分片被禁会直接丢包；用 `ping -M do -s <size>` 测路径 MTU。
- 易错点：只在宿主机调 MTU 忽略 Pod/隧道接口。
- 延伸：PMTU 发现机制？

**Q-N7 🔴 conntrack / iptables**
- 关键词：nf_conntrack、表链、性能
- 问题：kube-proxy iptables 模式下节点连接数很高，可能有什么问题？
- 参考要点：conntrack 表满会丢包（`dmesg` 见 `nf_conntrack: table full`）；调 `nf_conntrack_max`、缩短 `timeout`；或切 ipvs/Cilium eBPF 绕过。
- 易错点：盲目加大表不解决根因（短连接风暴）。
- 延伸：ipvs 模式优势？

**Q-N8 ⚫ BGP / Anycast**
- 关键词：eBGP、路由通告、就近
- 问题：Anycast 是怎么实现的？在运维场景有什么用？
- 参考要点：同一 IP 在多地通告，路由协议选最近；用于 DNS 根、DDoS 清洗、全球加速；故障切换靠撤回路由。
- 易错点：Anycast 连接可能被中间网络切到不同节点，需会话保持或无状态。
- 延伸：与 DNS 轮询的区别？

---

## kubernetes（K8s / 容器 / 云原生）

**Q-K1 🟢 CRI/CNI/CSI**
- 关键词：运行时、网络、存储接口
- 问题：请说清楚 K8s 的 CRI、CNI、CSI 分别解决什么问题。
- 参考要点：CRI=kubelet↔运行时（containerd/CRI-O）；CNI=Pod 网络 IP/路由（Calico/Cilium）；CSI=外部存储卷（Ceph/EBS）。三者解耦底层实现。
- 易错点：混淆三者对接对象；以为 K8s 不能用 Docker 镜像。
- 延伸：dockershim 为什么被移除？

**Q-K2 🟡 Pod 生命周期**
- 关键词：Pending/Running/CrashLoop、initContainer
- 问题：Pod 一直 Pending 怎么排查？
- 参考要点：资源不足（CPU/mem/GPU）、节点亲和/污点、PVC 未绑定、镜像拉取失败；`kubectl describe pod` 看 Events，`kubectl get events`。
- 易错点：只看状态不看 Events；忽略 ResourceQuota/LimitRange。
- 延伸：CrashLoopBackOff 与 OOMKilled 怎么区分？

**Q-K3 🟡 三种探针**
- 关键词：liveness/readiness/startup
- 问题：liveness 和 readiness 探针的区别？配错会怎样？
- 参考要点：liveness 失败→重启容器；readiness 失败→摘流量（不重启）；startup 保护慢启动。配反了会导致流量打进未就绪 Pod 或频繁重启。
- 易错点：用 liveness 做就绪检查，造成抖动重启。
- 延伸：探针用 exec/http/tcp 怎么选？

**Q-K4 🔴 HPA 原理**
- 关键词：metrics-server、CPU/自定义指标、冷启动
- 问题：HPA 基于什么指标扩缩容？有哪些坑？
- 参考要点：默认 CPU 利用率，依赖 metrics-server；可接自定义/Prometheus 指标；坑：指标延迟、缩容冷却、Pod 启动慢导致抖动、目标值设定。
- 易错点：没装 metrics-server 导致 HPA 不工作；用平均利用率在少副本下抖动大。
- 延伸：KEDA 与 HPA 区别？

**Q-K5 🔴 Service 与 kube-proxy**
- 关键词：ClusterIP、iptables/ipvs、endpoint
- 问题：Service 是如何把请求转发到 Pod 的？
- 参考要点：Service→Endpoints(selector)→Pod IP；kube-proxy 在节点写 iptables(ipvs) 规则做 DNAT；headless 无 ClusterIP 直接返 Pod。
- 易错点：以为 Service 是负载均衡器实体（实际是规则+DNS）。
- 延伸：iptables 模式下大量 Service 的性能问题？

**Q-K6 🔴 亲和性 / 污点**
- 关键词：nodeAffinity、podAntiAffinity、taint/toleration
- 问题：如何让一类 Pod 尽量打散、不挤在同一节点？
- 参考要点：`podAntiAffinity` 软/硬约束打散；`topologyKey` 指定拓扑域；配合 `taint`+`toleration` 隔离专用节点（如 GPU）。
- 易错点：硬反亲和在节点不足时调度失败。
- 延伸：拓扑域与故障域的关系？

**Q-K7 ⚫ etcd 运维**
- 关键词：quorum、快照、defrag、WAL
- 问题：etcd 数据膨胀、性能下降，怎么处理？
- 参考要点：定期 `etcdctl snapshot` 备份；`defrag` 整理碎片；控制单对象大小、避免大 list/watch；磁盘 IO 要低延迟（SSD）；quorum 丢失需谨慎恢复。
- 易错点：只在故障时才备份；defrag 期间影响性能。
- 延伸：etcd 与 K8s 可用性关系？

**Q-K8 🔴 Operator 模式**
- 关键词：CRD、controller、reconcile
- 问题：什么是 Operator？它比普通 Deployment 强在哪？
- 参考要点：用 CRD + 自定义控制器把运维知识（部署/扩缩/备份/故障恢复）编码进集群，声明式自愈；如 etcd-operator、Prometheus-operator。
- 易错点：把 Operator 当 Helm 模板；忽视 reconcile 幂等。
- 延伸：与 GitOps 怎么配合？

**Q-K9 🟡 Ingress / Gateway API**
- 关键词：ingress-controller、7层路由、Gateway API
- 问题：Ingress 和 Service 的区别？Gateway API 解决什么？
- 参考要点：Ingress 是 7 层路由规则，需 ingress-controller 实现；Service 是 4 层；Gateway API 标准化了路由/策略、角色分离（Gateway/HTTPRoute）。
- 易错点：以为创建 Ingress 自动生效（需 controller）。
- 延伸：与 Service Mesh 入口区别？

**Q-K10 ⚫ 大规模 K8s 挑战**
- 关键词：节点数、endpoint 扇出、list-watch 风暴
- 问题：管理数千节点的集群有哪些典型瓶颈？
- 参考要点：API Server 压力（list/watch 风暴、quorum 延迟）、etcd 写入、kube-proxy 规则规模、CNI 规模化、调度吞吐；对策：分片、按需 watch、ipvs/eBPF、多集群联邦。
- 易错点：线性堆资源不解决架构瓶颈。
- 延伸：多集群联邦 vs 单超大集群？

**Q-K11 ⚫ 万节点集群的控制面优化（阿里 2019 实践）**
- 关键词：List & Watch 风暴、Bookmark、watch cache 索引、一致性读、面向终态、OpenKruise
- 问题：单集群万节点、百万容器时 apiserver / etcd / 调度器先在哪里出问题？做了哪些优化？
- 参考要点：先建监控大盘与压测平台。连接层：周期性重建长连接让 kubelet 在 apiserver 副本间重新均衡、webhook 链路 HTTP/2 → 1.1 并设 maxSurge、升级 etcd client。List & Watch：网络抖动后 informer 全量重 List 的风暴用 Bookmark 事件解决（客户端持有更新的 rv，不再 too old）。读路径：`resourceVersion=0` 走 watch cache，支持动态加索引（nodeName / namespace / labels，Describe node 5 s → 0.3 s）并做一致性读（先取 etcd 的 rv@t0，等缓存追上再返回）。面向终态后风险控制要在 admission 层与 kubelet 层各做限流熔断（3000 实例升级设最大不可用 200）。工作负载层沉淀为 OpenKruise：原地升级、保持 IP / 卷、并发与容错暂停、镜像预热、SidecarSet。调度按真实负载与峰值预测排而非只按 request。
- 易错点：只会加 apiserver 副本；分不清缓存读与一致性读；只谈 etcd 不谈 List & Watch。
- 延伸：Q-K10、`references/collections-k8s-local-library.md` 第六组。

**Q-K12 🔴 云原生块存储选型：DRBD / LINSTOR / Piraeus vs Ceph**
- 关键词：内核态复制、超融合、数据本地性、quorum、CSI
- 问题：数据库上 K8s，Ceph RBD、Longhorn、Mayastor、Piraeus + LINSTOR + DRBD 怎么选？
- 参考要点：DRBD 是内核模块级块复制（网络 RAID 1，2.6.33 起主线，DRBD 9 最多 32 副本、双主、两有盘 + 一无盘仲裁）；LINSTOR 用 controller（唯一活跃）+ 每节点 satellite（无状态）+ client 编排 LVM / ZFS 卷；Piraeus 用 CSI 接进 K8s，调度扩展只把 Pod 放到本地有副本的节点、读走本地盘。优势来自内核态 + 超融合 + 只同步变化块；Ceph 用户态多副本强一致同步、CPU 内存随卷数线性增长，统一存储与容量扩展是强项但高 IOPS 数据库常不够。代价：每节点维护内核模块、副本受有盘节点限制、要配 quorum 防脑裂。落地：复制走独立网卡、调大 rmem / wmem、NVMe 用 LVM（无快照）SATA 用 ZFS（快照自愈）、LINSTOR 自身数据库放 local-path。任何方案先 fio 基线。
- 易错点：把 DRBD 当文件系统；多副本不配 quorum；只比 IOPS 不比运维能力。
- 延伸：Q-K1 CSI、`references/collections-k8s-local-library.md` 第七组。

---

## cicd-iac（CI/CD / IaC / 配置管理）

**Q-C1 🟢 CI/CD 流水线**
- 关键词：构建/测试/部署、制品
- 问题：一个标准的 CI/CD 流水线包含哪些阶段？
- 参考要点：代码拉取→依赖缓存→构建→单测→静态扫描→打制品→部署预发→自动化测试→灰度→生产；强调制品不可变、环境一致。
- 易错点：把部署当交付终点，忽略回滚与可观测。
- 延伸：蓝绿与金丝雀区别？

**Q-C2 🟡 Ansible 幂等**
- 关键词：幂等、changed_when、shell 陷阱
- 问题：为什么 Ansible 强调幂等？用 shell 模块怎么保证？
- 参考要点：重复执行结果一致便于安全重跑；`shell` 非幂等需 `creates`/`changed_when: false` 或改用 `lineinfile` 等。
- 易错点：用 `echo >>` 每次追加。
- 延伸：变量优先级？

**Q-C3 🟡 Terraform state/plan**
- 关键词：state、plan/apply、漂移
- 问题：Terraform 的 state 文件有什么用？漂移怎么处理？
- 参考要点：state 记录真实资源映射，支撑增量 plan；漂移=实际与 state 不符，用 `terraform plan`/`refresh` 发现并 `apply` 收敛；state 要远端加密锁（S3+DynamoDB）。
- 易错点：手动改云资源导致漂移且无人发现。
- 延伸：state 泄露风险？

**Q-C4 🔴 蓝绿 / 金丝雀**
- 关键词：零宕切换、渐进放量、指标驱动
- 问题：金丝雀发布怎么做才安全？
- 参考要点：小比例引流（如 5%）→ 看核心指标（错误率/延迟）→ 自动或手动渐进放量；结合服务网格做按权重/按请求路由；失败自动回滚。
- 易错点：只有放量没有健康门禁；回滚慢。
- 延伸：与 Feature Flag 配合？

**Q-C5 🟡 制品仓库 / 供应链**
- 关键词：镜像签名、SBOM、不可变
- 问题：如何保证部署的制品是可信且可追溯的？
- 参考要点：制品仓库（Harbor）存镜像/包；镜像签名（cosign）+ 准入校验（kyverno/gatekeeper）；SBOM 生成与漏洞扫描；不可变 tag、用 digest 拉取。
- 易错点：用 `latest` tag 导致不可追溯。
- 延伸：SLSA 等级？

**Q-C6 🔴 GitOps**
- 关键词：Git 为源、ArgoCD、reconcile
- 问题：GitOps 和传统 CI/CD 推送部署有什么区别？
- 参考要点：Git 是期望状态唯一源，agent（ArgoCD/Flux）在集群内持续 reconcile 拉取并校正漂移；审计靠 Git 历史；回滚=回退 commit。
- 易错点：把 GitOps 当「用 Git 触发脚本」；忽略 secret 管理。
- 延伸：与 Push 模式故障恢复差异？

**Q-C7 🟡 DB 变更管理**
- 关键词：在线 DDL、向后兼容、回滚
- 关键词扩展：可重复执行、灰度
- 问题：线上数据库 schema 变更怎么做才不宕机？
- 参考要点：向后兼容（先加列不加约束）、在线 DDL（gh-ost/pt-osc）、分批、先在从库验证；迁移与代码解耦、可回滚。
- 易错点：大表直接 `ALTER` 锁表；变更与代码不兼容。
- 延伸：expand/contract 模式？

**Q-C8 ⚫ 不可变基础设施**
- 关键词：镜像即环境、替换而非修改
- 问题：什么是不可变基础设施？它对运维意味着什么？
- 参考要点：服务器/镜像一旦创建不再修改，升级=替换新版本；提升一致性与可复现、降低配置漂移；配合镜像构建、编排与蓝绿。
- 易错点：仍 ssh 上去改配置破坏不可变。
- 延伸：与 Pets vs Cattle 隐喻？

---

## observability（监控 / 可观测性）

**Q-O1 🟢 Prometheus 拉模型**
- 关键词：pull、exporter、TSDB
- 问题：Prometheus 为什么用拉（pull）而不是推（push）？
- 参考要点：pull 由 Server 主动抓取，目标健康可见、易查漏；push 适合短任务用 Pushgateway；pull 在网络策略/防火墙下需打通抓取路径。
- 易错点：以为 Prometheus 只能 pull（短任务靠 Pushgateway）。
- 延伸：联邦与远程写？

**Q-O2 🟡 四类指标**
- 关键词：Counter/Gauge/Histogram/Summary
- 问题：Counter 和 Gauge 区别？Histogram 用来算什么？
- 参考要点：Counter 只增（如请求数），Gauge 可升降（如温度）；Histogram 分桶算分位数与 SLO；Summary 客户端算分位但不可聚合。
- 易错点：用 Gauge 记累计量导致 rate 计算错。
- 延伸：Histogram 分桶设计？

**Q-O3 🟡 PromQL 基础**
- 关键词：rate、irate、by、without
- 问题：`rate` 和 `irate` 有什么区别？什么时候用哪个？
- 参考要点：`rate` 取区间平均速率（平滑，适合告警）；`irate` 取最近两个点的瞬时速率（灵敏，适合图表）；`rate` 需区间 ≥  scrape 间隔数倍。
- 易错点：在过小区间用 rate 得 0/不准。
- 延伸：histogram_quantile 坑？

**Q-O4 🔴 可观测性三支柱**
- 关键词：Metrics/Logs/Traces、OpenTelemetry
- 问题：可观测性的三支柱是什么？OpenTelemetry 解决什么？
- 参考要点：指标（聚合态）、日志（离散事件）、追踪（请求链路）；OTel 统一采集标准与协议，避免厂商锁定，采集端解耦后端。
- 易错点：以为装了监控就是可观测（缺 tracing/上下文）。
- 延伸：RED 与 USE 方法？

**Q-O5 🔴 SLO / Error Budget**
- 关键词：SLI、目标、燃尽
- 问题：SLO 和 SLI 区别？Error Budget 怎么用？
- 参考要点：SLI 是实际指标（如成功率），SLO 是目标（99.9%）；Error Budget=1-SLO 的容错额度，耗尽则冻结发布、优先稳定性。
- 易错点：SLI 定义不清导致 SLO 无法度量。
- 延伸：多窗口多燃尽告警？

**Q-O6 🟡 日志体系 ELK vs Loki**
- 关键词：索引成本、标签、全文
- 问题：Loki 和 ELK 设计哲学上的核心区别？
- 参考要点：ELK 对全文建倒排索引（贵、重）；Loki 只索引标签（labels）、日志存对象存储，像「日志界的 Prometheus」，成本低、适合高 cardinal 场景。
- 易错点：用 Loki 做重全文检索性能差。
- 延伸：日志采样策略？

**Q-O7 🔴 告警设计**
- 关键词：告警疲劳、分层、静默
- 问题：如何避免告警疲劳？告警应该怎么设计？
- 参考要点：分层（页/工单）、基于 SLO 而非阈值堆砌、去重/分组/抑制、告警要有 actionable 说明与 runbook 链接；告警数宜少而准。
- 易错点：一切皆电话告警导致疲劳忽略真故障。
- 延伸：Alertmanager 路由树？

**Q-O8 ⚫ 分布式追踪落地**
- 关键词：trace_id、context 传播、采样
- 问题：分布式追踪在微服务里怎么串起一条请求？采样怎么取舍？
- 参考要点：用 trace_id/span_id 跨服务传播（W3C traceparent）；头部注入、跨进程/异步传递；采样（头部/尾部）平衡成本与覆盖。
- 易错点：只在同步调用传、异步/消息队列断链。
- 延伸：尾部采样与头部采样差异？

**Q-O9 🔴 Falco 运行时安全生态**
- 关键词：syscall、eBPF / 内核模块 / modern eBPF、falco_rules、Falcosidekick、响应引擎、k8s audit
- 问题：把 Falco 从「装上」做到「告警能被处理、还能自动响应」，链路上有哪些组件？坑在哪？
- 参考要点：Falco 每节点 DaemonSet，在内核层解析 syscall（也吃 k8s audit 与插件）按规则出告警；驱动三选一——内核模块 / eBPF probe / modern eBPF（CO-RE 免编译，优先）。规则 = 宏 + 列表 + 规则，本地覆盖放 falco_rules.local.yaml，falcoctl 管分发。告警本身只落 stdout/syslog，靠 Falcosidekick 扇出到 Slack/PagerDuty/Kafka/SIEM，Falcosidekick UI 看事件；response engine（如 Falco Talon）联动隔离/加 NetworkPolicy/缩容取证，先审计后处置。事件带 MITRE ATT&CK，与 RBAC 攻击面审计对齐（审计说哪条路径可达、Falco 说有人正在走）。坑：规则太宽告警风暴、驱动与内核不匹配起不来、只装 Falco 不接 sidekick 等于没告警。
- 易错点：以为装了就安全；分不清三种驱动；不接外发通路。
- 延伸：Q-O2 告警抑制、Q-CL9 攻击面审计。

---

## sre-reliability（故障 / 高可用 / 容量 / SRE）

**Q-S1 🟢 故障排查方法论**
- 关键词：分层、止损优先、证据
- 问题：线上出问题，你的通用排查思路？
- 参考要点：先止损（回滚/限流/切流）再定位；自顶向下分层（应用→中间件→系统→网络→硬件）；看指标/日志/链路；用排除法，靠证据不靠猜。
- 易错点：未止损就深挖，扩大影响。
- 延伸：如何建立 runbook？

**Q-S2 🟡 雪崩与防护**
- 关键词：限流、熔断、降级、隔离
- 问题：如何预防服务雪崩？
- 参考要点：限流（令牌桶/漏桶）护入口；熔断（Hystrix/sentinel）断依赖；降级保核心；隔离（线程池/舱壁）防扩散；超时与重试（带抖动）。
- 易错点：重试无退避与上限，反而放大故障。
- 延伸：重试风暴？

**Q-S3 🔴 多活 / 脑裂 / Raft**
- 关键词：quorum、lease、split-brain
- 问题：分布式系统如何防止脑裂？Raft 怎么保证一致性？
- 参考要点：多数派（quorum）+ 租约防双主；Raft 选主+日志复制+任期；脑裂时少数派不可用而非双写。
- 易错点：网络分区时两机房都写导致数据冲突。
- 延伸：异地多活的数据一致性取舍？

**Q-S4 🔴 容量规划**
- 关键词：压测、水位、冗余
- 问题：怎么做容量规划与容量评估？
- 参考要点：基于业务指标（QPS/连接数）做模型；全链路压测定拐点；设安全水位（如 70%）、预留冗余与突发；容量与成本权衡。
- 易错点：只看平均不看长尾与峰值。
- 延伸：弹性扩容与提前扩容？

**Q-S5 🟡 SLO/Error Budget**
- 关键词：已并入 O5，参见 observability
- 问题（复用）：你如何用一个季度的 Error Budget 来决策是否允许新功能发布？
- 参考要点：预算充足→正常发布；消耗过快→冻结非关键变更、优先稳定性；用 multi-window burn 预警。
- 易错点：把 SLO 当纯监控而非决策工具。
- 延伸：SLO 过低/过高分别有什么问题？

**Q-S6 🔴 混沌工程**
- 关键词：故障注入、假设、演练
- 问题：混沌工程是什么？和随便 kill 节点有什么区别？
- 参考要点：在受控实验中对系统注入故障（kill、延迟、丢包），验证「稳态假设」、暴露脆弱点；有范围、有指标、有回滚，而非破坏性乱试。
- 易错点：无假设无度量地乱注入。
- 延伸：GameDay 设计？

**Q-S7 🟡 缓存三崩**
- 关键词：击穿、穿透、雪崩
- 问题：缓存穿透、击穿、雪崩分别是什么？怎么解决？
- 参考要点：穿透=查不存在 key（布隆过滤器/空值缓存）；击穿=热点 key 失效并发回源（互斥锁/逻辑过期）；雪崩=大量 key 同时失效（随机 TTL/多级缓存）。
- 易错点：三者混为一谈。
- 延伸：布隆过滤器误判处理？

**Q-S8 🔴 无责复盘**
- 关键词：Blameless、根因、改进项
- 问题：怎么做一次有效的故障复盘？
- 参考要点：无责、聚焦系统而非个人；还原时间线、找根因（5 Whys）、列可落地的改进项并跟进；沉淀 runbook 与告警。
- 易错点：复盘变成追责会，掩盖真相。
- 延伸：如何避免改进项石沉大海？

**Q-S9 ⚫ RTO / RPO**
- 关键词：恢复时间、数据丢失
- 问题：RTO 和 RPO 的区别？它们如何指导容灾设计？
- 参考要点：RTO=恢复所需时间，RPO=允许丢失的数据时长；RPO 决定备份/复制频率，RTO 决定切换方案与自动化程度。
- 易错点：把二者混为「可用性」。
- 延伸：同城双活 vs 异地灾备取舍？

**Q-S10 🔴 级联故障**
- 关键词：依赖、线程耗尽、背压
- 问题：一个下游变慢，如何演变成全站故障？
- 参考要点：慢调用占满连接/线程池→上游排队超时→重试放大→资源耗尽扩散；防护靠超时、熔断、隔离、背压、限流。
- 易错点：缺乏端到端超时与隔离。
- 延伸：Hystrix 舱壁模式？

---

## middleware（中间件运维）

**Q-M1 🟡 Kafka 不丢不重**
- 关键词：acks、ISR、幂等、事务
- 问题：Kafka 如何做到不丢消息？如何避免重复？
- 参考要点：生产 `acks=all` + ISR 副本；消费手动提交 offset；去重靠幂等 producer（`enable.idempotence`）+ 事务，或消费端幂等。
- 易错点：自动提交 offset 在消费前崩溃导致丢。
- 延伸：消息积压怎么处理？

**Q-M2 🟡 Redis 持久化**
- 关键词：RDB、AOF、混合
- 问题：RDB 和 AOF 区别？怎么选？
- 参考要点：RDB 快照（恢复快、丢间隔数据）；AOF 追加命令（更稳、文件大）；Redis 7 默认混合；取舍看可接受的丢失窗口。
- 易错点：以为 AOF 一定不丢（appendfsync 策略决定）。
- 延伸：缓存与 DB 一致性？

**Q-M3 🟡 Redis 集群/淘汰**
- 关键词：slot、CRC16、maxmemory-policy
- 问题：Redis 内存满了会怎样？淘汰策略怎么选？
- 参考要点：达 `maxmemory` 按策略淘汰（LRU/LFU/随机/TTL）；集群按 16384 slot 分片；大 key/热 key 需拆分。
- 易错点：用 `noeviction` 在满时写失败。
- 延伸：大 key 如何在线删除？

**Q-M4 🔴 MySQL 主从与高可用**
- 关键词：binlog、GTID、MHA/Orchestrator
- 问题：MySQL 主从延迟怎么排查？高可用怎么做？
- 参考要点：看 `Seconds_Behind_Master`/GTID；延迟源=大事务/单线程回放/网络；高可用用 MGR/Orchestrator+MHA，注意脑裂与数据一致。
- 易错点：从库延迟下切主导致数据丢失。
- 延伸：读写分离下的延迟读？

**Q-M5 🔴 MySQL 死锁**
- 关键词：锁等待、事务顺序、索引
- 问题：MySQL 死锁怎么排查和预防？
- 参考要点：`show engine innodb status` 看最近死锁；固定加锁顺序、缩短事务、用好索引减少锁范围；死锁会自动回滚一个事务。
- 易错点：忽视事务粒度导致频繁死锁。
- 延伸：间隙锁与 next-key lock？

**Q-M6 🟡 ES 分片**
- 关键词：shard、routing、heap
- 问题：ES 索引分片数怎么规划？分片过多有什么问题？
- 参考要点：单分片 10–50GB 为宜；分片多→集群元数据与 heap 压力大、查询扇出高；过少→无法并行/扩容受限。
- 易错点：默认大量小分片拖垮集群。
- 延伸：冷热架构？

**Q-M7 ⚫ 中间件边界**
- 关键词：职责、选型、SLA
- 问题：作为运维，你对中间件的职责边界是什么？何时该推动业务改造而非加机器？
- 参考要点：运维负责部署/高可用/容量/监控/备份；业务侧问题（慢 SQL、大 key、滥用消息）应推动改造；建立 SLA 与容量评审。
- 易错点：无限加资源掩盖架构问题。
- 延伸：中间件成本优化？

**Q-M8 🟡 MongoDB 文档模型与索引**
- 关键词：文档模型、BSON、Schema Validation、ESR、TTL
- 问题：什么业务适合 MongoDB 而不是 MySQL？上线前 schema 与索引怎么设计，运维要盯什么？
- 参考要点：字段多变 / 半结构化（日志、事件、画像）且「一个文档装下一次访问」→ 适合；强事务与多表 JOIN → 关系库。集合建好就挂 `$jsonSchema` validator；复合索引按 ESR（等值→排序→范围），时间用 BSON Date 才能范围查与 TTL；用 `explain()` 确认 IXSCAN。盯：COLLSCAN 慢查询、连接 / 游标泄漏、写关注、oplog 窗口、16MB 文档上限。
- 易错点：时间存字符串导致索引失效；不写 `$set` 整文档替换；`deleteMany({})` 清空集合。
- 延伸：`references/collections-mongodb-zero-to-hero.md`（68 题：概念 / 建模 / Atlas / CRUD / 日志实战 / 向量检索）。

**Q-M9 🔴 MongoDB Atlas Vector Search 与向量库选型**
- 关键词：embedding、$vectorSearch、numCandidates、cosine、RAG
- 问题：业务已在 MongoDB，做知识库 RAG 用 Atlas Vector Search 还是引入 Milvus / pgvector？链路与坑？
- 参考要点：链路 = 切块→embedding→存 `{text, embedding, metadata}`→`$vectorSearch`（`numDimensions` 与模型一致、相似度跟模型走、`numCandidates` ≥ 10–20×limit、`filter` 做租户过滤）→拼 prompt→LLM。中小规模默认留在 MongoDB（同库、少一套系统、权限模型简单）；亿级向量 / 精细 HNSW 调参 / 社区版离线环境（无 Vector Search）才上专用库。坑：Search 节点独立计费、换模型要全量重建、维度不一致静默返回空、无黄金集评测。
- 易错点：只说「也能存向量」讲不出参数；多租户 RAG 不做权限过滤。
- 延伸：gpu-ai 推理与 embedding 服务；system-design RAG 主题。

---

## gpu-ai（GPU 与 AI 运维）

**Q-G1 🟢 CUDA / 显存 / SM**
- 关键词：并行、HBM、Tensor Core
- 问题：简单说一下 GPU 的 SM、显存、CUDA 是什么关系？
- 参考要点：SM 是计算单元（含 CUDA/Tensor Core）；显存是高带宽内存放权重/激活；CUDA 是调度计算的编程模型；三者共同决定算力与吞吐。
- 易错点：把显存当内存等同 CPU 内存。
- 延伸：HBM 与带宽瓶颈？

**Q-G2 🟡 驱动与 CUDA 兼容**
- 关键词：driver、toolkit、版本矩阵
- 问题：容器里报 `CUDA driver version is insufficient` 怎么解？
- 参考要点：宿主驱动版本 < 镜像所需 CUDA 版本；升级驱动或换低 CUDA 版本镜像；用 `nvidia-smi` 看驱动支持的最高 CUDA。
- 易错点：只在容器里升级 CUDA 不解决（驱动在宿主机）。
- 延伸：CUDA 向后兼容规则？

**Q-G3 🟡 Device Plugin**
- 关键词：nvidia.com/gpu、调度、资源
- 问题：K8s 里 Pod 怎么申请 GPU？缺了什么就申请不了？
- 参考要点：需 `nvidia-device-plugin`，Pod 声明 `limits["nvidia.com/gpu"]: 1`；缺 plugin 则无该资源；多卡用 `CUDA_VISIBLE_DEVICES` 控制。
- 易错点：以为装了驱动就能调度 GPU。
- 延伸：MIG 切分资源名？

**Q-G4 🔴 MIG / MPS / Time-Slicing**
- 关键词：物理切分、共享、超卖
- 问题：多团队共享一张 A100，有哪些隔离方案？隔离性如何？
- 参考要点：MIG 硬件级强隔离；MPS 共享上下文提利用率、隔离中；Time-Slicing 弱隔离轻量超卖；按 SLA 选。
- 易错点：用 Time-Slicing 当强隔离（会互相影响）。
- 延伸：MIG 实例与 QoS？

**Q-G5 🔴 利用率低排查**
- 关键词：GPU-Util、data pipeline、NCCL
- 问题：GPU 利用率长期很低，可能是什么原因？
- 参考要点：数据加载瓶颈（CPU/磁盘喂不动）、batch 小、通信等待（NCCL 多卡同步）、kernel 未融合；看 `nvidia-smi dmon` 与 profiler。
- 易错点：只看 Util 忽略显存带宽与 SM 占用。
- 延伸：如何做 data loader 优化？

**Q-G6 🔴 显存 OOM**
- 关键词：batch、checkpoint、混合精度
- 问题：训练/推理显存 OOM 怎么救？
- 参考要点：降 batch、开 gradient_checkpointing、fp16/bf16 混合精度、`torch.compile`、清理缓存；推理用 PagedAttention(vLLM)、KV Cache 管理。
- 易错点：只降 batch 不查是否存在显存泄漏。
- 延伸：张量并行 vs 流水并行？

**Q-G7 🔴 vLLM / 推理架构**
- 关键词：PagedAttention、continuous batching、TTFT
- 问题：vLLM 为什么能提升推理吞吐？运维关注哪些指标？
- 参考要点：PagedAttention 分页管理 KV Cache 减少碎片；continuous batching 提升并发；关注 TTFT、TPS、并发、显存、排队。
- 易错点：只比吞吐忽略首 token 延迟与长上下文显存。
- 延伸：与 TGI 区别？

**Q-G8 🔴 DCGM 监控 / XID**
- 关键词：DCGM-exporter、ECC、XID 错误
- 问题：如何监控 GPU 健康？XID 错误说明什么？
- 参考要点：`DCGM-exporter`→Prometheus 暴露温度/显存/功耗/ECC/利用率；XID 错误码是 GPU 硬件故障信号，需隔离节点并走维修。
- 易错点：只监控利用率漏掉 ECC 软错误累积。
- 延伸：ECC 不可纠正错误处置？

**Q-G9 ⚫ NVLink / IB / RDMA**
- 关键词：卡间互联、NCCL、低延迟
- 问题：训练集群里 NVLink 和 InfiniBand 分别解决什么？
- 参考要点：NVLink/NVSwitch 卡间高带宽低延迟；IB/RDMA 节点间低延迟高吞吐；NCCL 负责集合通信拓扑；网络成训练瓶颈时扩环/调拓扑。
- 易错点：忽视 IB 配置（PFC/ECN）导致拥塞。
- 延伸：RoCE vs IB？

**Q-G10 ⚫ 提效降本**
- 关键词：利用率、调度、混部
- 问题：从运维角度，怎么提升 GPU 集群的整体利用率并降本？
- 参考要点：细粒度调度（MIG/分时）、队列优先级与抢占、混部（推理+训练错峰）、闲时回收、显存超卖与弹性、监控驱动容量决策。
- 易错点：只堆卡不提升有效利用率。
- 延伸：GPU 多租户计量？

---

## cloud-security（云 / 安全 / 合规）

**Q-CL1 🟢 IAM 最小权限**
- 关键词：RBAC、least privilege、角色
- 问题：云上如何实践最小权限原则？
- 参考要点：按角色分权、默认拒绝、定期审计闲置权限、用角色而非长期密钥、密钥轮换；避免 `*` 通配。
- 易错点：图省事给管理员权限。
- 延伸：AK/SK 泄露应急？

**Q-CL2 🟡 VPC / 安全组**
- 关键词：子网、ACL、网络隔离
- 问题：安全组和 NACL 区别？怎么设计分层网络？
- 参考要点：安全组有状态、实例级；NACL 无状态、子网级；公/私子网分层、NAT 出网、堡垒机跳板。
- 易错点：把数据库放公网或安全组全放通。
- 延伸：零信任如何落地？

**Q-CL3 🟡 密钥与证书**
- 关键词：KMS、轮换、TLS
- 问题：密钥和证书应该怎么管理才安全？
- 参考要点：用 KMS/Secrets Manager 存、加密静态数据、自动轮换；证书用 ACM/ cert-manager 自动签发续期；禁止明文硬编码。
- 易错点：把密钥提交到代码仓库。
- 延伸：证书过期导致的中断？

**Q-CL4 🔴 等保 / SOC2 / GDPR**
- 关键词：合规框架、数据分类、审计
- 问题：做合规（等保/GDPR）对运维提出了什么要求？
- 参考要点：数据分类分级、访问控制与审计日志、加密、留存与跨境限制（GDPR）、定期评估；运维需提供可追溯日志与变更记录。
- 易错点：把合规当一次性工作而非持续。
- 延伸：审计日志不可篡改？

**Q-CL5 🔴 DDoS / 入侵检测**
- 关键词：清洗、WAF、HIDS
- 问题：遭遇 DDoS 或主机入侵，运维的第一响应是什么？
- 参考要点：DDoS→切高防/Anycast 清洗、限流、封源；入侵→隔离主机、保全证据、排查入口（弱口令/漏洞/密钥）、重置凭据、复盘。
- 易错点：先删文件破坏取证。
- 延伸：如何建立入侵检测基线？

**Q-CL6 ⚫ FinOps**
- 关键词：成本可视、标签、闲置回收
- 问题：云成本失控，从运维角度怎么治理？
- 参考要点：成本分摊标签、识别闲置资源（低 CPU 实例/未挂载盘）、机型选型、预留/竞价、自动启停、预算告警。
- 易错点：只降本不顾业务弹性。
- 延伸：GPU 闲置成本尤其高如何专项治理？

**Q-CL7 🔴 CKS 实操：一个加固任务从头到尾**
- 关键词：NetworkPolicy、审计策略、kube-bench、securityContext / seccomp / AppArmor、RuntimeClass、Falco、ImagePolicyWebhook
- 问题：给你一个 kubeadm 集群：dev 命名空间默认拒绝出站、开审计只记 Deployment 的 RequestResponse、跑 CIS 并修复、给 Pod 只读根文件系统与自定义 seccomp、处置监听 9999 的陌生进程——逐项说操作与验证。
- 参考要点：NetworkPolicy `podSelector: {}` + `policyTypes: [Egress]` 不写规则即拒绝，跨命名空间放行时目标 ns 必须真的有 label；审计在 apiserver 静态 Pod 加 `--audit-policy-file / --audit-log-path / maxsize / maxbackup` 并 hostPath 挂进策略与日志，四级 None / Metadata / Request / RequestResponse 首条匹配生效，Deployment 在 `apps` group；kube-bench 典型 FAIL 是 `--profiling=false`、audit-log 系列、etcd 目录属主、`--kubelet-certificate-authority`，改 manifests 后重跑；`readOnlyRootFilesystem: true` 配 emptyDir 挂可写目录；seccomp JSON 放 `/var/lib/kubelet/seccomp/` 且每个节点都要有；`ss -tunlp` → `ps -f -p` → `systemctl stop/disable`。补齐：RBAC 只有三种合法组合（Role + ClusterRoleBinding 是错的）、`kubectl auth can-i --as`、trivy 扫全集群镜像、RuntimeClass 指到 gVisor / Kata、Falco 规则与输出格式、ImagePolicyWebhook 的 `defaultAllow: false` 会在 webhook 不可达时锁死集群、PSP 已被 PSA 替代。
- 易错点：namespace 没打标签；审计策略改了没挂 hostPath；seccomp 只放控制面节点；把 kube-bench WARN 当 FAIL 全改却不理解含义。
- 延伸：Q-CL2、`references/collections-k8s-local-library.md` 第一组。

**Q-CL8 🔴 Kubernetes 1.24 官方安全审计的核心发现**
- 关键词：NCC Group、nodes/proxy 提权、client CA 与 requestheader CA、RBAC 无 Deny、NetworkPolicy 局限、Bootstrap Token
- 问题：官方审计报告里对生产集群最有指导意义的几条发现是什么？你会据此改什么？
- 参考要点：19 个发现（0 Critical / 0 High / 6 Medium / 9 Low / 4 Info）。`nodes/proxy` = 对任意 kubelet 的 master 级访问（可 exec 任意 Pod；配合 `nodes/status` 写权限可让 apiserver 用 master 证书请求自己）→ 视同 cluster-admin 审计。client CA 与 requestheader CA 共用且未设 `--requestheader-allowed-names` → 任意证书用户可伪造 `X-Remote-Group: system:masters` → 分离 CA。RBAC 只做加法、fail open → 准入层补负向约束。NetworkPolicy 靠标签 opt-in 只能做命名空间级隔离，DNS 可做隐蔽信道 → 默认拒绝 + 准入锁标签 + DNS 策略。PSS Restricted 未限制 `runAsGroup=0`、Localhost seccomp 可选更弱 profile → 准入补齐。其他：命名空间 `..` 穿越放大 etcd 查询、apiserver 代理 InsecureSkipVerify、审计日志不记认证来源、Bootstrap Token 约 83 bit 且失败时明文进日志、emptyDir 不支持 noexec。方法论：先按场景与角色建威胁模型；1.13 审计部分发现仍未修，要纳入自己的基线。
- 易错点：把 0 Critical 理解成不用管；不会把 finding 转成检查项。
- 延伸：Q-CL7、`references/collections-k8s-local-library.md` 第二组。

**Q-CL9 🔴 集群 RBAC 攻击面审计（从 Pod 到 cluster-admin 的路径）**
- 关键词：攻击路径图、多跳提权、bind/escalate/impersonate、workload mutation、nodes/proxy、云 IAM、webhook 注入、GitOps operator
- 问题：一次授权评审列出「从被攻陷 Pod 到 cluster-admin/节点/密钥/云 IAM」的可达路径。分哪几类？根因权限是什么？怎么审计封堵？
- 参考要点：SSRR/SSAR 任何身份都能查，防守不能靠隐蔽。类别与封堵：① 直接 RBAC（bind/escalate、建 CRB、通配符 verb）→ auth can-i --list / who-can 扫、去通配符；② workload mutation（patch Deployment 换 serviceAccountName 继承高权 SA）→ 拆分改工作负载与选 SA；③ 容器逃逸（privileged/hostPID/hostPath/危险 cap）→ PSA restricted + Kyverno 拒绝；④ 横向 + 令牌窃取（pods/exec、读别人 Secret、nodes/proxy 等同任意 kubelet master）→ 收敛 exec、默认关自动挂载令牌；⑤ impersonate 链 → 视同 cluster-admin；⑥ mutating webhook 注入 → 锁写权限；⑦ 云 IAM（IRSA/Workload Identity + metadata 169.254.169.254）→ SA-角色一对一 + 挡 metadata + 收紧 audience；⑧ GitOps/operator（ArgoCD/Flux/Vault）高权 → 最小权限 + 审计谁能写 CR。做成周期性只读审计，每条映射 MITRE ATT&CK 与 Falco 检测对齐。
- 易错点：只看谁是 cluster-admin 忽略多跳；不知道 bind/escalate/impersonate/nodes/proxy/exec 等同提权；把云 IAM 当集群外的事。
- 延伸：Q-CL7 CKS、Q-CL8 官方审计、Q-O9 Falco。

---

## service-mesh（服务网格 / Envoy / Gateway API）

**Q-SM1 🟡 服务网格解决什么、为什么是 Sidecar**
- 关键词：数据面 / 控制面、SDK 痛点、代价
- 问题：已有 Spring Cloud / gRPC SDK，网格还解决什么？为什么做成 Sidecar 而不是库？
- 参考要点：SDK 的根本痛点是升级成本（改策略要全业务发版）与多语言能力对不齐；Sidecar 把治理逻辑放到进程外代理，任何语言走 TCP 就被治理，mTLS / 证书由平台统一管。必须一起讲代价：每 Pod 多一个容器的内存 CPU、多两跳的延迟、控制面成为新单点、排障链路变长；ambient 模式（ztunnel L4 共享 + waypoint L7 按需）正是为摊薄这些成本。
- 易错点：只会背「解耦」；只讲收益不讲代价；把网格等同于 Istio。
- 延伸：Q-SM6、Q-SM9。

**Q-SM2 🔴 Sidecar 注入与 iptables 劫持**
- 关键词：MutatingAdmissionWebhook、istio-init、15001 / 15006、uid 1337、istio-cni
- 问题：istio-init 的 iptables 规则到底做了什么？为什么 Envoy 自己发的包不会被再次劫持？
- 参考要点：入站 PREROUTING → ISTIO_INBOUND → REDIRECT 到 15006（virtualInbound）；出站 OUTPUT → ISTIO_OUTPUT → REDIRECT 到 15001（virtualOutbound）。防循环靠一条规则：来自 istio-proxy 用户（uid/gid 1337）的流量直接 RETURN。用 excludeInboundPorts / excludeOutboundIPRanges 注解放行不该劫持的流量（如 169.254.169.254）。有 PSA 限制的环境用 istio-cni 在节点层配规则，避免给业务 Pod NET_ADMIN。
- 易错点：说不出 15001 与 15006 的方向；不知道 1337 规则的作用。
- 延伸：Q-SM7 排障时对照端口。

**Q-SM3 🟡 mTLS 与 PERMISSIVE → STRICT 迁移**
- 关键词：PeerAuthentication、ALPN、DestinationRule TLS mode、回滚
- 问题：存量集群怎样零停机把东西向流量切到 STRICT mTLS？
- 参考要点：客户端 Envoy 用 istiod 签发的工作负载证书发起 mTLS，双方经 ALPN 协商，服务端校验 SPIFFE ID 后卸载 TLS 明文交给应用。迁移：先全局 PERMISSIVE（同时收明文与 mTLS）→ 用指标确认没有明文调用方 → 按命名空间收紧 STRICT；处理例外：网格外调用方、健康检查、DestinationRule 里显式 DISABLE 的目标。PeerAuthentication 即时生效，出问题 delete 即回到宽松态。
- 易错点：直接上 STRICT 把网格外调用方打挂；忘了 DestinationRule 的 TLS 设置会覆盖默认行为。
- 延伸：Q-SM4 授权依赖 STRICT。

**Q-SM4 🔴 AuthorizationPolicy 的评估顺序与默认拒绝**
- 关键词：CUSTOM / DENY / ALLOW / AUDIT、根命名空间、principals、RequestAuthentication
- 问题：怎样在网格里落地「默认拒绝、按需放行」？为什么说 DENY 优先很关键？
- 参考要点：评估顺序 CUSTOM → DENY → ALLOW（AUDIT 不影响结果）：任一 DENY 命中即拒绝；存在 ALLOW 策略但都不匹配则拒绝；完全没有策略则放行。默认拒绝的标准做法：在 istio-system 放一条 `spec: {}` 的 ALLOW。可匹配 source（principals / namespaces / ipBlocks）、operation（hosts / methods / paths / ports）、condition（headers / JWT claims）。基于 principals 的规则只有 STRICT mTLS 下才有对端身份，PERMISSIVE 下形同虚设；JWT 场景用 RequestAuthentication 校验签名再用 requestPrincipals 强制带 token。
- 易错点：以为「没匹配到 ALLOW」会放行；PERMISSIVE 下写身份规则。
- 延伸：Q-SM3。

**Q-SM5 🔴 Ambient 模式：ztunnel + waypoint 与 HBONE**
- 关键词：分层网格、ztunnel（Rust，DaemonSet）、waypoint（Envoy）、HTTP CONNECT、15008
- 问题：ambient 相比 sidecar 的取舍是什么？为什么需要 HBONE？
- 参考要点：Secure Overlay 层由每节点一个 ztunnel 提供 mTLS、L4 策略与 TCP 指标；L7 由按需拉起的 waypoint 提供路由 / 熔断 / 限流 / 重试 / 丰富授权 / HTTP 遥测。收益：热插入不改 Pod、不重启、摊薄每 Pod 一个 Envoy 的资源；代价：节点级代理是共享故障域、L7 仍需 Envoy。HBONE 把所有流量放进一条 mTLS 的 HTTP CONNECT 隧道（15008）：显式携带原始目的地址（跨节点后 SO_ORIGINAL_DST 已丢失）、多路复用摊薄握手、修复 PERMISSIVE 下 server-speaks-first 协议（MySQL）被嗅探弄坏的问题、网络策略只需放行单端口。2025 年 Trail of Bits 对 ztunnel 审计无漏洞类发现。仍选 sidecar 的场景：专属资源、EnvoyFilter 定制、监管要求。
- 易错点：以为 ambient 完全不需要 Envoy；说不出 HBONE 存在的原因。
- 延伸：Q-SM1、Q-SM9。

**Q-SM6 🟡 网格内调用 503 的排查顺序**
- 关键词：response flags（UF / UH / NR / UO）、istioctl analyze / proxy-status / proxy-config、config_dump
- 问题：A 调 B 返回 503，你按什么顺序查？
- 参考要点：① 看 A 的 sidecar 访问日志拿 response flag 定方向（UH 无健康上游、UF 上游连接失败常是 mTLS 不一致、NR 无路由、UO 熔断）；② `istioctl analyze` 做静态体检；③ `istioctl proxy-status` 看 xDS 是否 SYNCED；④ `istioctl proxy-config listener/route/cluster/endpoint` 逐层对照 Envoy 链路；⑤ 排 mTLS：B 是否 STRICT 而 A 的 DestinationRule 是 DISABLE，`proxy-config secret` 看证书；⑥ 用 `reporter="destination"` 的指标和 B 的应用日志确认是否 B 自己返回的 503；⑦ 兜底 `localhost:15000/config_dump` 与 debug 日志。
- 易错点：一上来重启 Pod；不看 response flag 就猜。
- 延伸：Q-SM2 端口对照。

**Q-SM7 🟡 Gateway API 与 Ingress 的本质区别**
- 关键词：GatewayClass / Gateway / HTTPRoute、角色分离、ReferenceGrant、GAMMA
- 问题：为什么说 Gateway API 不是「Ingress v2」？它定义了哪几类角色？
- 参考要点：Ingress 把监听、TLS、路由塞在一个对象里靠注解扩展（注解地狱、实现不可移植）；Gateway API 拆成 GatewayClass（基础设施提供方）、Gateway（集群运维：监听 / 证书 / 默认策略）、HTTPRoute（应用开发者，可跨命名空间挂到共享 Gateway）。跨命名空间必须 Gateway 侧 allowedRoutes 放行、引用他人 Service 需 ReferenceGrant，从机制上杜绝随便写 host 劫持流量。GAMMA 让同一套 HTTPRoute 描述东西向路由，Istio 已支持用它替代 VirtualService。
- 易错点：把 Gateway API 当成换个名字的 Ingress；不知道 ReferenceGrant。
- 延伸：迁移步骤与风险控制。

**Q-SM8 🔴 非 HTTP 协议（Dubbo / Redis / MySQL / MQ）怎么治理**
- 关键词：端口命名 / appProtocol、TCP 透传、Aeraki MetaProtocol、有状态中间件
- 问题：Dubbo 服务上网格后只能看到 TCP 字节数、没法按方法灰度，怎么办？
- 参考要点：先看 Service 端口名或 appProtocol——命名错就被当 TCP，这是最高频的「配了没生效」。能力分级：HTTP / gRPC 完整 L7；Redis / MySQL / Kafka 有 Envoy 原生 filter 但能力有限且默认不开；Dubbo / Thrift / 私有协议集成度低。三条路：协议迁移到 triple / gRPC（长期最优）、Aeraki + MetaProtocol（写一个 codec 数百行即可获得路由 / 限流 / 指标，控制面零改动）、只做 L4（mTLS + L4 授权 + 连接熔断，对 MySQL / Redis 常常够用，ambient 性价比高）。Redis Cluster / Kafka 这类带重定向元数据的协议要么放行不代理，要么用协议感知代理。
- 易错点：不知道端口命名决定协议处理；把 Redis Cluster 盲目塞进网格。
- 延伸：Q-SM9 迁移实践。

**Q-SM9 ⚫ 异构存量系统平滑迁入统一网格**
- 关键词：第二控制面、ServiceEntry 同步、四步迁移、多控制面三阶段合并、全链路染色、本地限流
- 问题：多协议、两套旧 Istio、四种注册中心、K8s 与 VM 混布，怎么分阶段迁到一套网格？
- 参考要点：以腾讯音乐（IstioCon 2021）为参考：选型标准是通用性 / 兼容性（Aeraki 作第二控制面不改 Istio）/ 易用性 / 可持续性。私有协议用 MetaProtocol 只实现 decode / encode / onError。旧注册中心（Polaris / Consul / Dubbo / Eureka）用 xxx2Istio 组件 watch 后同步成 ServiceEntry，服务按「网格外旧发现 → 网格外经 ServiceEntry 接入 → 进网格旧名指向 K8s Service → 直接用 K8s Service 名」四步推进。多控制面合并三阶段：互指 Gateway + ServiceEntry 打通并迁服务 → 权重切到新网格、旧网格放占位 ServiceEntry 并卸载 → 移除旧 ServiceEntry。迁后收益：按命令字路由做全链路染色；注意本地限流按单 Pod 计，副本扩容阈值随之变大。
- 易错点：给出「全改 gRPC」的理想方案而非迁移方案；不知道 ServiceEntry 是网格内外互通的核心原语。
- 延伸：Q-SM8、Q-K10 多集群。

**Q-SM10 🔴 网格的代价与不该上网格的场景**
- 关键词：延迟、资源、认知负担、eBPF / Cilium Service Mesh
- 问题：老板问要不要上 Istio，你怎么答？eBPF 是替代还是补充？
- 参考要点：代价：每次调用多两跳用户态代理（单跳亚毫秒到数毫秒）、sidecar 内存与配置量正相关、多一层排障与控制面运维、控制面 / ztunnel 成为关键路径。不该上：服务少语言单一已有 SDK、没人能维护控制面、延迟极度敏感、只需要加密（Cilium WireGuard / ambient L4 便宜得多）。该上：多语言、上百服务、零信任合规、统一灰度与故障注入、跨集群治理。eBPF 擅长 L3 / L4（策略、透明加密、替代 kube-proxy、无侵入可观测），做不了完整 L7，需要 L7 时同样拉 Envoy（每节点一个）；行业收敛方向是「L4 下沉、L7 按需」。务实做法：先小范围只开 mTLS + 指标，测出延迟与资源再推广。
- 易错点：只推销不讲代价；认为 eBPF 能完全替代 Envoy。
- 延伸：Q-SM1、Q-SM5。

## system-design（系统设计）

> 系统设计题按「需求澄清 → 估算 → 高层设计 → 深入 2–3 个组件 → 权衡与可运维性」五段推进，一次只推进一段；
> 评分五维：需求与估算 15% · 高层设计 20% · 深入与数据模型 25% · 权衡 20% · 可运维性（失败模式/发布/观测/成本）20%。
> 完整 35 题与 630 个主题语料目录见开源仓库 `modules/system-design/`（`system-design-questions.md` + `system-design-catalog.md`）。

**Q-SD1 🟢 面试流程与估算**
- 关键词：FR/NFR、back-of-envelope、峰值系数
- 问题：面试官说「设计一个图片社交应用」，你前 10 分钟做什么？1 亿 DAU、每人每天看 20 张 / 传 2 张、图 500KB，估算读写 QPS、存储与带宽并指出瓶颈。
- 参考要点：先澄清用户/核心场景/规模/一致性/不做什么；读 ≈ 23K QPS（峰值 ×3–5）、写 ≈ 2.3K；日增 100TB、5 年 ~180PB（未含副本）；出口 ~11GB/s → 瓶颈依次是出口带宽（CDN）→ 元数据读（缓存）→ 存储成本（分层/EC）。
- 易错点：不问规模就画图；算出数字不做结论；忘峰值与副本系数。
- 延伸：CAP/PACELC 在你的设计里体现在哪份数据上？

**Q-SD2 🟡 分布式限流器**
- 关键词：令牌桶、Lua 原子、Redis Cluster、fail-open/closed
- 问题：为 1M QPS 的 API 平台设计限流：算法、位置、原子性、分片、多机房、Redis 挂了怎么办。
- 参考要点：放 API 网关（进程内限流每实例只见 1/N）；令牌桶（O(1) 内存、天然突发）；读-补-扣-写放单个 Lua 原子执行；Redis Cluster 按 client 哈希分片，热 key 本地预扣；多机房默认区域桶；社交/金融 fail-closed（限流故障常与洪峰同时发生），低风险 API 可 fail-open；429 + RateLimit-* 头。
- 易错点：SETNX+EXPIRE 两步；用客户端时钟；没说清 fail 策略。
- 延伸：单个超大客户打爆一个分片怎么办？

**Q-SD3 🟡 分布式 KV / 缓存**
- 关键词：一致性哈希、虚拟节点、quorum、LSM、cache-aside、雪崩/穿透/击穿
- 问题：设计 PB 级 KV 存储的分区/复制/读写路径；再说商品详情缓存怎么保证一致性与防三大故障。
- 参考要点：一致性哈希 + 虚拟节点；N 副本机架感知；W+R>N；hinted handoff / read repair / Merkle 反熵分别修不同时间尺度的不一致；LSM + Bloom；缓存 cache-aside「先写库后删缓存」+ binlog 失效兜底；TTL 抖动、空值缓存 + 布隆、singleflight + 逻辑过期；热 key 本地缓存 + 复制分摊。
- 易错点：哈希取模；quorum 当强一致；「先删缓存再写库」。
- 延伸：缓存整体丢失时 DB 扛得住吗？不能怎么办？

**Q-SD4 🔴 分布式消息队列**
- 关键词：分区、ISR、at-least-once、幂等、outbox、rebalance、lag
- 问题：设计百万 msg/s 的消息队列：存储、复制、顺序、投递语义、积压、消费者组。
- 参考要点：分区顺序追加 segment + page cache + 零拷贝；acks=all + min.insync.replicas；同 key 同分区保证顺序；先处理后提交 = 至少一次 → 消费幂等；「写库 + 发消息」用 outbox + CDC；lag 监控、毒消息进 DLQ；分区数是并行度上限且扩分区破坏 key 有序；cooperative rebalance。
- 易错点：声称 exactly-once 不提业务幂等；以为加消费者就提吞吐。
- 延伸：Kafka vs RabbitMQ 什么时候选谁？

**Q-SD5 🟡 信息流 / IM**
- 关键词：推/拉、大 V、timeline cache、WebSocket 网关、会话序号、写扩散/读扩散
- 问题：设计 3 亿 DAU 的 feed（推拉怎么选、大 V 怎么办）；设计 5 亿 DAU 的 IM（连接、顺序、离线、群聊）。
- 参考要点：普通用户推（写收件箱）、大 V 拉（读时归并）、只推活跃用户；游标分页；删除惰性过滤。IM：WebSocket 网关无状态 + 在线状态 Redis；服务端分配会话 seq，客户端 client_msg_id 幂等、缺口拉取补齐；小群写扩散、大群读扩散；E2EE 用 Signal 协议。
- 易错点：只推或只拉；offset 分页；消息顺序靠客户端时间。
- 延伸：网关发布时百万长连接怎么平滑漂移？

**Q-SD6 🔴 监控 / 日志平台（SRE 重点）**
- 关键词：pull/push、TSDB、高基数、告警去重/抑制、Kafka 缓冲、标签索引 vs 全文索引、冷热分层
- 问题：为 10 万主机设计监控平台（采集、存储、告警、多租户、谁监控监控）；再设计每天 100TB 的日志平台。
- 参考要点：pull 主机/K8s、push 批任务经网关；ingester → 2h 不可变 block → 对象存储 + 降采样（保留 sum/count）；标签倒排索引；relabel + 租户 series 上限防高基数；Alertmanager 集群去重 / 抑制 / 静默 / 分级；独立最小监控 + 多路告警通道盯自己。日志：agent 本地缓冲 → Kafka → 脱敏/采样 → Loki 式标签索引 + 对象存储（比全文索引省 5–10×）或 ES ILM 分层；租户配额与成本展示。
- 易错点：只讲单机 Prometheus；告警无 for/去重；日志全量全文索引无缓冲层。
- 延伸：新 series 创建率（churn）为什么比总 series 数更值得告警？

**Q-SD7 🔴 调度器 / 发布系统 / 容灾**
- 关键词：触发与执行分离、run 唯一键、DAG、分批灰度 + 自动回滚、RPO/RTO、单元化、脑裂
- 问题：设计 100 万任务的分布式 cron/DAG 调度器；设计万台机器的发布系统（含断网边缘）；为支付核心设计 RPO≈0/RTO<1min 的容灾并说明与异地多活的区别。
- 参考要点：按时间桶索引 + 分片 leader 租约，至少一次触发 + (job_id, scheduled_time) 唯一键去重，worker 心跳续租，DAG 事件驱动 + 回填。发布：内容寻址制品 + P2P 分发 + 节点 agent 声明式收敛，分批 + SLI 判定自动回滚，schema 向前兼容；边缘用期望状态 + 差分 + 本地回滚。容灾：同城同步/异地异步、多数派仲裁 + fencing 防脑裂、切换剧本 + 定期演练；多活 = 单元化按用户分片写，代价是跨单元事务与全局查询。
- 易错点：单点调度器；全量重启无健康判定；RPO/RTO 混淆；方案没演练。
- 延伸：配置变更为什么要走和代码一样的灰度？

**Q-SD8 🔴 RAG / LLM 推理平台**
- 关键词：分块、混合检索 + rerank、ACL 预过滤、评测；continuous batching、KV cache、TTFT/TPOT、GPU 估算
- 问题：为 1000 万文档的企业知识库设计 RAG；为百万 DAU 设计 LLM 对话推理平台并估算 GPU 数量。
- 参考要点：RAG：结构化分块带父块引用 → 嵌入 + 关键词双索引 → RRF 融合 → cross-encoder 重排 → 只依证据生成 + 引用校验；ACL 在检索时过滤；金标集回归（召回@k、忠实度）。LLM：网关配额/安全 → 会话裁剪 → 按模型/租户/优先级路由 → vLLM 类引擎（连续批处理、PagedAttention、前缀缓存、量化、prefill/decode 分离）；70B FP16 = 140GB 权重 → TP=2×80GB，KV 每 token ~MB 级决定并发；实例数 = 目标 tokens/s ÷ 单实例吞吐 + 30% 冗余；SLO 用 TTFT 与 TPOT，断连要取消释放 KV。
- 易错点：只有向量检索；权限生成后过滤；把 LLM 当无状态 HTTP 服务、估不出 GPU 数。
- 延伸：GPU 利用率低于 40% 时先查什么？

## fde（前沿部署工程师 / Forward Deployed Engineer）

> FDE（Palantir 的 Delta、OpenAI / Scale / Google 的同类岗位）面试以**案例**为主：给客户场景，按 C.A.S.E.（Clarify 澄清 → Architect 架构 → Solve the Delta 补缺口 → Evaluate 评测与 Day 2）一次推进一段。
> 评分五维：澄清诊断 20% · 架构落地 25% · Delta 胶水 20% · 评测与 Day 2 15% · 干系人沟通 20%。完整 30 题见开源仓库 `modules/fde/`。

**Q-F1 🟢 FDE vs SWE 与 C.A.S.E.**
- 关键词：Delta、嵌入式工程、C.A.S.E.、完成定义
- 问题：FDE 和普通 SWE 有什么区别？拿到「银行想做反洗钱调查助手」的案例，前 5 分钟你问什么？
- 参考要点：用户是少数高风险干系人而非百万匿名用户；环境是遗留/隔离/混合；目标是价值交付速度；代码一半是胶水。前 5 分钟：数据量与形态、分类（PII/PHI）、系统记录源、可测的成功定义、Champion/Blocker、网络与权限。
- 易错点：直接讲框架不问数据与合规。
- 延伸：三个为什么（系统记录源 / 不作为成本 / Day 2）。

**Q-F2 🟡 红旗与敌意干系人**
- 关键词：红旗、信任公式、最小权限、升级
- 问题：客户说「数据两周就绪」「不需要项目经理」「先本地跑」意味着什么？首席工程师拒绝给 VPC 访问怎么办？
- 参考要点：三句话都是红旗（数据永远不就绪 / 无决策人 / 对云的深层不信任），第 1 周就写进 WES 升级。敌意：信任问题非技术问题；1 对 1 听担忧；展示平台接管脏活给对方赢；先申请最小权限并用 Terraform 透明化；只在阻塞里程碑时经 Champion 升级且事先告知。
- 易错点：硬怼或默默扛。
- 延伸：可信顾问公式 = (可信度+可靠性+亲密度)/自我导向。

**Q-F3 🟡 数据工程地基**
- 关键词：Medallion、星型 vs OBT、EXPLAIN、分区/聚簇、数据倾斜
- 问题：在 20 年遗留 SQL Server 上建分析与 AI 层怎么分层？一条 SQL 扫 10TB 怎么优化？Spark 最后一个任务 OOM 怎么办？
- 参考要点：Bronze 不可变原样 → Silver 单一事实来源 → Gold 按消费者（报表星型 / AI 宽表）；看执行计划找未剪枝的分区（分区列上别套函数）、SELECT *、先 join 后过滤；BigQuery 按时间分区 + 高基数过滤列聚簇；倾斜先查 null key，广播小表、加盐热 key、开 AQE。
- 易错点：只会加内存；Bronze 可变。
- 延伸：5PB 48 小时进云 → Transfer Appliance + 缩小范围 + 并行建 schema。

**Q-F4 🟡 GCP 着陆区与安全边界**
- 关键词：共享 VPC、Interconnect/IAP、Workload Identity、私有 GKE、VPC Service Controls、DLP
- 问题：客户零云经验、Okta 身份、数据不出境、HIPAA。请设计着陆区与防泄露。
- 参考要点：项目按环境拆 + 共享 VPC；Interconnect/VPN + Private Google Access；Okta 联合 + IAP 零信任；工作负载用 Workload Identity 不发 JSON 密钥；私有集群 + Cloud NAT；VPC SC 把数据/分析/AI 项目圈进边界（先 dry-run），DLP 在进分析层前脱敏；MVA 用 Cloud Run + BigQuery + Pub/Sub，Terraform 5 分钟拉起。
- 易错点：一上来 GKE 微服务；把 VPC SC 当防火墙。
- 延伸：Autopilot vs Standard 何时选谁？

**Q-F5 🔴 企业 RAG、多 Agent 与评测**
- 关键词：托管检索、混合检索、ADK 层级/工作流 Agent、A2A、内/外循环评测、成对/逐点、Groundedness
- 问题：10 万份合规 PDF 30 天交付带引用的问答；「读报表 → 查仓库 → 审阅」的 Agent 怎么编排；怎么向客户证明它不胡说？
- 参考要点：先托管检索引擎拿基线 + 关键词兜底行业术语 + ACL 检索时过滤；固定顺序用 Sequential/Parallel/Loop 工作流 Agent，只在需判断处用 LLM Agent，工具最小权限；评测：与客户共建金标集，内循环看工具轨迹与响应质量，外循环 CI 跑逐点（Groundedness/Fulfillment/Coherence）+ 与生产版成对评测，放行门槛写进 PRD，上线后漂移监控。
- 易错点：一开始自建全套；凭感觉测。
- 延伸：< 100ms 欺诈检测 → 快模型主路径 + LLM 异步复核。

**Q-F6 🔴 隔离网络与战术边缘**
- 关键词：ATO/IL/FedRAMP/STIG/ITAR/CMMC、safetensors、包镜像、Iron Bank/Harbor/Cosign、数据二极管/CDS、K3s、时钟/PKI/密钥/首次启动
- 问题：国防承包商网络里部署 AI 平台：合规要先确认什么？权重和依赖怎么进去？镜像怎么信？遥测怎么出来？边缘跑什么？第一周必须设计好哪些「云上不会发生」的问题？
- 参考要点：先问 IL 与 ATO 路径，FedRAMP 级别可能排除生成式 AI 服务，ITAR 管权重与人员；权重走加密介质 + SHA-256 + safetensors + 溯源许可记录，内网 PyPI/npm/APT 镜像 + 离线 NVD 扫描；Iron Bank/distroless 基础镜像 + Cosign 签名 + Kyverno 验签；入向二极管、出向 DLP 脱敏 + 清单签核 + 不可变审计，CDS 审批数月要在发现阶段规划；边缘 K3s + vLLM/llama.cpp 量化 + Fluent Bit WAL 存储转发；Day 1 就要本地 Chrony、内部 PKI 自动轮换、Vault HA + HSM、签名 ISO 首次启动。
- 易错点：假设能开 VPN 同步；pickle 权重；证书没轮换。
- 延伸：哪些承诺绝不能随口做？

**Q-F7 🟡 咨询工件与沟通**
- 关键词：BLUF/金字塔、MECE、80/20、SOW、MVA、UAT、Site Survey、PRD、WES
- 问题：15 分钟向 CTO 汇报是否迁云怎么讲？第 6 周客户要「顺便接 CRM」怎么办？三份工件各写什么？
- 参考要点：第一句给结论与要的决策，三个 MECE 理由各带数据，风险与替代方案；范围变更不当场答应，对照 SOW 走变更评估写进 WES，Out of Scope 要白纸黑字；Site Survey 记源系统/体量/质量/身份/连接/缺口/快速胜利，PRD 写成功定义（命中率、延迟、幻觉率）与分阶段与不做项，WES 写价值、风险+动作+责任人、Day 30。
- 易错点：从技术细节讲起；口头答应范围。
- 延伸：技术演示怎么讲成价值叙事？

**Q-F8 🔴 案例：医院再入院预测前 30 天**
- 关键词：30 天计划、数据剖析、指标定义、VPC SC + DLP、Delta 胶水、成对评测、UAT、Day 2
- 问题：大型医院集团、20 年数据在本地 SQL Server、零云经验、HIPAA 极严。走一遍前 30 天并说清每周产出。
- 参考要点：1–7 天数据剖析 + 与首席医疗官定义「再入院」+ 安抚 IT → Site Survey；8–15 天 GCS + BigQuery 着陆区、VPC SC + DLP、Terraform → 过安全评审；16–25 天检索增强流水线 + Cloud Run 胶水拉实时体征 → 端到端可跑；26–30 天成对评测对比历史结局 + 5 位医生 UAT（不改变行为即失败）→ 评测报告与 Day 2 计划；每周 WES，红旗第一周升级。评分：初级只讲脚本，高级讲安全/成本/干系人，顶级讲指标定义与评测门槛。
- 易错点：第一周就建模；没有 UAT。
- 延伸：交接清单——客户独立完成一次发布、回滚、告警处理、评测运行才算完成。

## ai-engineering（AI 工程 / Agentic 工具链）

> 「AI 面试」模块：考 agentic 编码 / 运维工具（以 Claude Code 为例，原理对 Codex / Cursor 通用）的正确与安全用法、团队化、护栏与评测。
> 🟢 会用 → 🟡 会扩展与团队化 → 🔴 会设计护栏 / 平台 / 评测。完整 26 题见开源仓库 `modules/ai-engineering/`。

**Q-AI1 🟢 Agent 循环与记忆文件**
- 关键词：agentic loop、CLAUDE.md/AGENTS.md、记忆层级、精简
- 问题：Agent 和代码补全的区别？CLAUDE.md 该写什么、三层（用户/项目/本地）各放什么？
- 参考要点：Agent 是「探索 → 计划 → 编辑 → 验证 → 汇报」的循环，你委派并审查；记忆写项目结构、构建/测试命令、约定、老犯的错、禁区，不写可推导细节；个人偏好放 `~/.claude/CLAUDE.md`、团队约定放项目 `CLAUDE.md` 提交、本地环境放 `CLAUDE.local.md`；记忆每次前置，十条精确胜过百条模糊；被忽略就更具体或升级成钩子。
- 易错点：把 README 塞进记忆；分不清作用域。
- 延伸：`#` 快速记忆、`/memory`。

**Q-AI2 🟡 上下文管理**
- 关键词：/clear、/compact、/context、@ 引用、extended thinking、压缩损失
- 问题：长会话越来越糊涂怎么办？什么时候 /clear、什么时候 /compact？
- 参考要点：`/context` 看占用；不相关任务 `/clear`，同任务自然边界 `/compact`（可指定保留）；知道文件就 `@path`，大输出先过滤，探索交给子代理；难题才开 extended thinking；压缩会丢数值/路径/被否决方案，关键结论写文件不靠对话。
- 易错点：一个会话干所有事；把上下文当无限。
- 延伸：上下文工程与技能的渐进披露。

**Q-AI3 🟢 权限模式与规则**
- 关键词：默认/accept edits/plan/bypass、allow/deny、deny 优先、三层 settings
- 问题：给新同事配一套安全但不烦的权限。
- 参考要点：allow 测试/lint/git diff 等只读低风险命令；deny `rm -rf`、`.env`、生产凭证、不必要的 WebFetch；改动超过两三个文件先 plan mode；bypass 只在容器；团队规则进 `.claude/settings.json`，个人例外进 `settings.local.json`；deny 永远赢。
- 易错点：本机开 bypass；不知道覆盖顺序。
- 延伸：钩子做内容级阻断。

**Q-AI4 🟡 探索-计划-编码-验证与 TDD**
- 关键词：plan mode、可验证目标、先写失败测试、具体化提示、小步提交、纠偏
- 问题：中等复杂度新功能怎么拆成 agentic 工作流？Agent 三次修不对一个 bug 怎么办？
- 参考要点：探索（只读复述现状）→ plan mode 出计划并批判 → 小步实现每步跑测试提交 → 审 diff；先「写失败测试不实现」再「实现不许改测试」防它改题交卷；提示要具体到用例与参考文件；无新证据的重复尝试两次就停：回退检查点、让它先解释、给复现/失败测试，或双击 Escape 换假设。
- 易错点：不给验证标准；让错误方向跑完。
- 延伸：/rewind 检查点。

**Q-AI5 🟡 扩展点：命令 / 钩子 / MCP / 子代理 / 技能 / 无头**
- 关键词：$ARGUMENTS、allowed-tools、PreToolUse exit 2、MCP 作用域、subagent tools、渐进披露、claude -p --allowedTools
- 问题：分别说明六个扩展点解决什么、放哪里、怎么团队化。
- 参考要点：命令 = 你触发的提示模板（`.claude/commands/`，`!`cmd`` 内联、`allowed-tools` 最小权限）；钩子 = 生命周期上的保证（PostToolUse 格式化、PreToolUse 读 stdin JSON 命中黑名单 `exit 2` 阻断；钩子以你的权限自动跑，要审查、要快）；MCP = 给模型的工具说明书 + 统一传输鉴权（团队 `--scope project` 进 `.mcp.json`，只接用的，来源可信）；子代理 = 独立上下文与人格（`tools` 限权、「use proactively」自动委派，小任务别用）；技能 = 自动触发的 know-how（只预载描述）；插件 = 打包分发；无头 = `claude -p` + JSON 输出 + 显式 `--allowedTools`，CI 里不 bypass、需要全权进容器。
- 易错点：命令给全局权限；审查员有写权限；把 MCP 当 REST。
- 延伸：本仓库 `.mcp.json`、`workbuddy/` 插件、`scripts/e2e/` 就是实例。

**Q-AI6 🔴 Agent 进运维链路的护栏**
- 关键词：只读优先、分阶段、白名单动作、爆炸半径、钩子阻断、审计、SLO 熔断、预算
- 问题：老板要「自动处理告警并修复」的 Agent，怎么分阶段落地？
- 参考要点：阶段 0 只读诊断（K8s MCP 非破坏模式、只读凭证）→ 阶段 1 生成变更由人审批经 GitOps 执行 → 阶段 2 白名单动作 + 单命名空间/非核心/变更窗口 + PreToolUse 黑名单 + 审计通知；贯穿：可回滚、错误率上升自动停、频率预算、演练与 postmortem；不给通用会话生产写凭证、不 bypass、秘密在 deny。
- 易错点：一步到位全自动；只靠提示词约束。
- 延伸：MCP 网关的工具级授权与审计。

**Q-AI7 🔴 提示注入与供应链**
- 关键词：不可信数据 vs 指令、读秘密 + 外发链、能力限制、工具描述注入、插件/钩子/MCP 信任
- 问题：Agent 抓了个网页后突然读 `.env` 并发网络请求，怎么回事、怎么防？
- 参考要点：网页含注入指令 → 模型当任务执行 → 典型「读不可信内容 → 访问敏感数据 → 出向」链；防线是能力：deny 秘密、限制出向、MCP 只读、高风险人工审批、沙箱；检测：钩子对「读秘密 + 外发」模式阻断 + 审计；提示层最弱；供应链只用可信来源、锁版本、内部 marketplace 审核；工具描述本身可注入。
- 易错点：「提示词里说别听网页的」当防护。
- 延伸：长期记忆也可被注入，「请记住…」不能直接写入。

**Q-AI8 🔴 评测与判断题**
- 关键词：金标集、LLM-as-judge 校准、工具轨迹、放行门槛、漂移、vibe coding 边界、度量质量
- 问题：改了提示词有人说「变笨了」怎么办？Vibe coding 是炒作还是范式？
- 参考要点：从历史任务建 50–200 条金标集（含不该做的动作），CI 跑新旧配置比正确率/轨迹/危险拒绝率/成本延迟，评审模型与人工抽样校准，门槛写进变更流程，线上抽检与漂移监控；判断：交互方式真变（定义目标 + 审查），工程本质没变（验收、可维护、责任在人）；从只读低风险起步、仓库化规范、护栏先于自动化、度量返工率与缺陷逃逸而非 PR 数；不该用：无法验证、无回滚、含秘密无脱敏、团队无审查能力。
- 易错点：凭感觉改提示词；全盘否定或全盘拥抱。
- 延伸：本仓库 `scripts/e2e/` 用无头会话做面试智能体的行为回归。

**Q-AI9 🔴 案例：定时 LLM 报告流水线上生产还缺什么**
- 关键词：数据扇入降级、规则兜底、供应商抽象、配置校验、幻觉数字校验、数据源注入、双语一致性、金标集、成本看板
- 问题：看 duanyytop/ai-market-radar（每天 8 点从免费行情 API 拉数据，LLM 出中英双语跨市场报告，发到 GitHub Pages / Issues）——它做对了什么？上生产你补什么？
- 参考要点：做对：每个数据源各自 `catch` 降级、报告模板有无数据分支；LLM 失败回退规则引擎保证每天有产出；只抓一次数据并行出两种语言；Anthropic SDK 可改 baseURL + OpenAI 兼容端点；env 覆盖文件配置并用 zod 校验（GitHub Actions 未设 secret 是空串不是 undefined）；系统提示要求「所有结论基于给定数据、不编造数字」，CI 有 lint / 格式 / 类型 / 测试。要补：输出数字回溯到输入数据的校验；把行情 API 返回内容当不受信任输入（白名单、截断、标注 data-not-instructions）；结构化 JSON 输出再渲染；en / zh 两次生成可能结论相反要做一致性；30 天金标集回归提示词与模型；token / 延迟 / 供应商版本看板；定时任务成功率与「兜底触发率」告警；上游 schema 断言；最小权限 token 与幂等发布。
- 易错点：只看到「用了 LLM」；以为提示词写了不编造就没有幻觉；忘了双语一致性与成本观测。
- 延伸：Q-AI5 护栏、Q-AI8 评测。

## behavior（行为与架构）

**Q-B1 🟡 STAR 项目**
- 关键词：情境、任务、行动、结果
- 问题：讲一个你主导的、最有技术含量的运维项目（用 STAR）。
- 参考要点：S 背景（痛点/规模）、T 目标、A 你的具体动作与权衡、R 量化结果（可用性/成本/效率）；体现 ownership。
- 易错点：只讲团队不讲自己贡献。
- 延伸：如果重来你会改什么？

**Q-B2 🟡 跨团队推动**
- 关键词：沟通、影响力、对齐
- 问题：当你发现问题是业务架构导致的，但业务不配合，怎么办？
- 参考要点：用数据与故障影响说话、给可落地方案而非只提要求、小范围试点证明价值、争取上级与技术委员会支持。
- 易错点：硬怼或放任。
- 延伸：如何建立跨团队 SLA？

**Q-B3 🔴 技术选型权衡**
- 关键词：trade-off、演进、成本
- 问题：让你在自建与托管、开源与商业之间选型，你怎么决策？
- 参考要点：看团队能力、SLA 要求、TCO、锁定风险、演进路径；用决策矩阵，先小规模验证再推广。
- 易错点：盲目追新或一味保守。
- 延伸：如何避免供应商锁定？

**Q-B4 🔴 带人与规划**
- 关键词：梯队、复盘文化、路线图
- 问题：作为资深/leader，你怎么带团队和技术规划？
- 参考要点：建梯队与 oncall 轮值、沉淀 runbook/复盘文化、按业务节奏定技术路线图、平衡稳定性与效率投入。
- 易错点：只盯技术不顾人。
- 延伸：如何衡量运维团队健康度？

**Q-B5 ⚫ 快/稳/省权衡**
- 关键词：SLO、成本、速度
- 问题：业务要快发，稳定性要稳，成本要省，三者冲突时你怎么排？
- 参考要点：以 SLO 为标尺，稳定性是底线；用渐进发布与自动化把「快」与「稳」统一；成本在弹性与闲置治理上优化而非牺牲核心冗余。
- 易错点：为省钱砍掉关键冗余导致大故障。
- 延伸：如何向业务解释稳定性投入？

**Q-B6 🟡 失败复盘**
- 关键词：最大故障、根因、成长
- 问题：讲一次你搞出或参与的最大线上故障，以及你从中学到什么。
- 参考要点：诚实、聚焦系统改进而非甩锅；讲清楚时间线、根因、补救、后续防呆；体现成长。
- 易错点：美化或推卸。
- 延伸：之后是否推动了对类似风险的防护？

**Q-B7 ⚫ 技术趋势**
- 关键词：eBPF、AI Ops、平台工程
- 问题：你认为未来 2–3 年运维领域最重要的技术趋势是什么？
- 参考要点：eBPF 可观测/安全、AIOps/LLM 辅助排障、平台工程（内部开发者平台）、GitOps/多云、GPU/AI 基础设施；结合自己落地判断。
- 易错点：只罗列名词无判断。
- 延伸：你准备如何布局学习？
