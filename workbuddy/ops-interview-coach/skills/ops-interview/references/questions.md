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

---

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
