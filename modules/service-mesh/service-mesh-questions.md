# 服务网格 / Envoy / Gateway API 面试题（25 题）

> 遵循 [../../docs/STANDARD.md](../../docs/STANDARD.md) 模板。
> 本模块聚焦「东西向流量治理」与「南北向新一代网关」，与 `kubernetes/` 模块的 Q12（网格概览）互补：
> 那里回答「要不要上网格」，这里回答「上了之后怎么讲原理、怎么排障、怎么调优」。
>
> 素材来源见文末「参考来源」。难度：🟢 初级 · 🟡 中级 · 🔴 高级。

---

### Q1. 服务网格（Service Mesh）到底解决了什么问题？为什么形态是 Sidecar？

- **难度**：🟡 中级
- **关键词**：service mesh, sidecar, 数据面 data plane, 控制面 control plane, 关注点分离
- **概念速记**：
  - **服务网格**：把「服务间通信」本身抽象成一层独立的基础设施——重试、超时、熔断、mTLS、可观测性不再写在业务代码里，而是由与应用同生命周期的代理接管。
  - **Sidecar**：与应用容器共享同一个 Pod（同 network namespace）的代理容器，通过流量劫持接管进出流量，应用零改造。
  - **数据面 / 控制面**：数据面（Envoy/ztunnel）真正转发流量；控制面（istiod）把用户写的 CRD 翻译成代理配置并下发。
- **问题**：在已经有 Spring Cloud / gRPC 这类 SDK 方案的情况下，服务网格解决了什么 SDK 解决不了的问题？为什么要做成 Sidecar 而不是一个库？
- **参考答案**：
  1. **SDK 方案的根本痛点是「升级成本」与「多语言」**：治理逻辑编译进业务二进制，改一次重试策略要所有业务重新发版；Java 生态完善但 Go/Python/Node 要各写一套，能力还对不齐。
  2. **Sidecar 把治理逻辑从「进程内库」变成「进程外代理」**：升级代理不需要业务改代码；任何语言只要走 TCP 就自动被治理；安全能力（mTLS、证书轮转）由平台统一负责，业务不碰私钥。
  3. **代价必须一起讲**（面试加分点）：每个 Pod 多一个容器 → 内存与 CPU 开销；多两跳网络 → 增加延迟（典型 sidecar 单跳 亚毫秒~数毫秒）；控制面成为新的单点与复杂度来源；排障链路变长。
  4. **所以形态在演进**：Istio ambient 模式把 L4 下沉到每节点一个 ztunnel（共享），L7 才按需拉起 waypoint，正是为了摊薄「每 Pod 一个 Envoy」的成本，见 Q14。
- **易错点 / 面试官关注**：
  - 只会背「解耦」，说不出 SDK 方案具体卡在哪（升级 + 多语言）。
  - 只讲收益不讲代价——网格是有明确适用边界的技术，见 Q24。
  - 把「服务网格」等同于「Istio」，忽略 Linkerd、Cilium Service Mesh、Consul 等不同取舍。
- **延伸**：Q14、Q24、[kubernetes/kubernetes-questions.md](../kubernetes/kubernetes-questions.md) Q12

---

### Q2. Istio 的控制面与数据面各自做什么？istiod 合并了哪些组件？

- **难度**：🟡 中级
- **关键词**：istiod, Pilot, Citadel, Galley, xDS, CA
- **概念速记**：
  - **istiod**：Istio 1.5 之后的单体控制面进程，合并了原来的 **Pilot**（配置下发）、**Citadel**（证书签发 CA）、**Galley**（配置校验与聚合）、Sidecar Injector（注入 webhook）。
  - **数据面**：Envoy（sidecar / gateway / waypoint）或 ztunnel（ambient L4）。
- **问题**：描述一条 Istio 配置（比如一个 VirtualService）从 `kubectl apply` 到真正在 Envoy 上生效的完整链路。
- **参考答案**：
  1. **配置入口**：CRD 写入 etcd → istiod 通过 informer watch 到变更（配置源还可以是 MCP / 文件，多集群下还会 watch 远端集群的 Service/Endpoint）。
  2. **服务发现聚合**：istiod 把 K8s 的 Service/EndpointSlice、ServiceEntry、WorkloadEntry 聚合成内部的服务模型。
  3. **翻译**：把「用户意图」（VirtualService 的路由规则、DestinationRule 的负载均衡与熔断）翻译成 Envoy 的 **LDS/RDS/CDS/EDS** 资源。
  4. **按需裁剪**：根据每个 proxy 的 `node id`（`sidecar~<ip>~<pod>.<ns>~<ns>.svc.cluster.local`）和 Sidecar/discoverySelectors 配置，只推送该实例需要的那部分配置（见 Q16）。
  5. **下发**：通过 **ADS**（单条 gRPC 双向流）推给 Envoy，Envoy ACK/NACK；`istioctl proxy-status` 看到的 `SYNCED / STALE / NOT SENT` 就是这一步的状态。
  6. **证书**：istiod 同时作为 CA，通过 SDS 给每个 proxy 签发并轮转工作负载证书（见 Q8）。
- **易错点 / 面试官关注**：
  - 说不出 istiod 合并前的三个组件名，或以为现在还要单独部署 Citadel/Galley。
  - 不知道配置是「按需裁剪」的，以为全量推给所有 sidecar——这正是大规模网格性能问题的根源。
  - 分不清 NACK（Envoy 拒绝了配置，通常是配置非法）与 STALE（推送超时/连接问题）。
- **延伸**：Q4、Q16、Q17

---

### Q3. Envoy 的核心概念：Listener / Filter Chain / Route / Cluster / Endpoint 分别是什么？

- **难度**：🟡 中级
- **关键词**：Envoy, Listener, FilterChain, RouteConfiguration, Cluster, ClusterLoadAssignment
- **概念速记**：
  - **Listener**：监听地址+端口，是配置树的根。一条请求先命中 Listener。
  - **Filter Chain**：Listener 上的过滤器链。L4 是 network filter（如 `tcp_proxy`、`http_connection_manager`），L7 是 HCM 里面的 http filter（如 `router`、`jwt_authn`、Istio 的 `stats`）。
  - **RouteConfiguration（RDS）**：HCM 用它做 L7 路由匹配（host/path/header），匹配结果指向一个 Cluster。
  - **Cluster（CDS）**：一个上游服务集群，定义负载均衡策略、连接池、熔断、TLS 上下文。
  - **ClusterLoadAssignment（EDS）**：Cluster 里具体的 endpoint 列表（IP:Port + 健康状态 + locality）。
- **问题**：画出 Envoy 处理一次 HTTP 请求的配置链路，并说明 Istio 的 VirtualService 和 DestinationRule 分别落到哪一层。
- **参考答案**：
  1. **链路**：`Listener` →（filter chain 匹配：SNI/目的地址/传输协议）→ `HttpConnectionManager` → `RouteConfiguration` → 匹配到 `route` → `Cluster` → `ClusterLoadAssignment` 里的 `Endpoint`。
  2. **对应关系**：
     - `VirtualService`（路由：按 header/path 分流、流量权重、超时重试、故障注入）→ 主要落到 **RouteConfiguration（RDS）**。
     - `DestinationRule`（subset 定义、负载均衡算法、连接池、异常点检测/熔断、TLS 模式）→ 主要落到 **Cluster（CDS）**，subset 会生成形如 `outbound|9080|v1|reviews.default.svc.cluster.local` 的独立 cluster。
     - `Gateway` → 生成入口 **Listener**。
     - `ServiceEntry` → 往服务发现里加一个网格外的服务，生成对应 Cluster/Endpoint。
  3. **实操验证**：
     ```bash
     istioctl proxy-config listener <pod> -n <ns>
     istioctl proxy-config route    <pod> -n <ns> --name 9080 -o json
     istioctl proxy-config cluster  <pod> -n <ns> --fqdn reviews.default.svc.cluster.local
     istioctl proxy-config endpoint <pod> -n <ns>
     ```
- **易错点 / 面试官关注**：
  - 把 Cluster 理解成「K8s 集群」——在 Envoy 里 Cluster 是「上游服务」。
  - 不知道 DestinationRule 的 subset 会生成独立 Cluster，导致「VirtualService 里写了 subset 但没定义 DestinationRule」时报 `no healthy upstream` 却找不到原因。
  - 说不清 filter chain 是怎么匹配的（SNI、destination port、source IP 等），在 TLS passthrough 场景排障会卡住。
- **延伸**：Q4、Q10、Q17

---

### Q4. xDS 协议有哪四种变体？为什么需要 ADS？Incremental（Delta）xDS 解决什么？

- **难度**：🔴 高级
- **关键词**：xDS, SotW, Delta xDS, ADS, 最终一致性, nonce, ACK/NACK
- **概念速记**：
  - **xDS**：Envoy 的动态配置发现协议族（LDS/RDS/CDS/EDS/SDS…），基于 gRPC 双向流。
  - **SotW（State of the World）**：每次请求都要带上全部关心的资源名，服务端对 LDS/CDS 也要返回全量资源。
  - **Incremental / Delta**：只传增量（新增/删除的资源名、变化的资源），并支持按需（lazy）订阅。
  - **ADS（Aggregated Discovery Service）**：把所有资源类型复用到**一条** gRPC 流上，用 type URL 区分，从而能严格控制下发顺序。
- **问题**：xDS 有哪几种变体？为什么 Istio 默认用 ADS？如果不用 ADS 会出什么问题？
- **参考答案**：
  1. **两个维度组合出四种变体**（Envoy 官方口径）：
     | | 独立 gRPC 流（每种资源一条） | 聚合到一条流 |
     |---|---|---|
     | **SotW** | Basic xDS | **ADS** |
     | **Incremental** | Incremental xDS | Incremental ADS |
  2. **为什么要 ADS——顺序问题**：LDS/CDS 是配置树的根，RDS/EDS 是叶子。如果 Listener 已经引用了某个 RouteConfiguration，而 RDS 还没到，或者 Cluster 到了但 Endpoint 还没到，就会出现**短暂流量黑洞**（`no healthy upstream` / 404）。分开多条流时无法保证跨类型顺序；ADS 用单条流让管理服务器能「先 CDS→EDS→LDS→RDS」地有序推送。**每个 Envoy 实例只有一条 ADS 流。**
  3. **为什么要 Delta——规模问题**：SotW 下改 1 个 cluster 要重推 10 万个 cluster，控制面 CPU/内存和网络都扛不住；Delta 只推变化的那一个，还支持「请求到来时才按需加载该 cluster」。
  4. **ACK/NACK 机制**：响应带 `nonce`，Envoy 回一个带 `response_nonce` 的请求；**没有 `error_detail` 是 ACK，有则是 NACK**。排障时 istiod 的 `pilot_xds_push_errors`、Envoy 的 `update_rejected` 指标就是看这个。
  5. **资源预热（warming）**：Cluster 在拿到对应 EDS 之前处于 warming 状态，不会被路由使用——这是避免流量打到空集群的保护机制。
- **易错点 / 面试官关注**：
  - 只知道「xDS 就是下发配置」，说不出 SotW 与 Delta 的区别，更说不出 ADS 的顺序保证价值。
  - 把 ADS 理解成「性能优化」——它的首要目的是**顺序/一致性**，性能优化是 Delta 的事。
  - 不知道 NACK 是靠 `error_detail` 有无来判定的。
- **延伸**：Q2、Q16、来源：[Envoy xDS 协议文档](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol)

---

### Q5. Sidecar 是怎么注入的？istio-init 的 iptables 规则到底做了什么？

- **难度**：🔴 高级
- **关键词**：MutatingAdmissionWebhook, istio-init, iptables NAT, 流量劫持, istio-cni
- **概念速记**：
  - **注入**：由 `MutatingAdmissionWebhook` 在 Pod 创建时改写 Pod spec，加入 `istio-init`（initContainer）与 `istio-proxy`（sidecar 容器）。开关是 namespace 标签 `istio-injection=enabled` 或 `istio.io/rev=<revision>`。
  - **流量劫持**：`istio-init` 以 `NET_ADMIN`/`NET_RAW` 权限在 Pod 的 network namespace 里写 iptables NAT 规则，把进出流量强制重定向到 Envoy。
- **问题**：一个 Pod 被注入后，它的 iptables NAT 表里大概有哪几条链？入站和出站流量分别怎么走？怎么避免无限循环？
- **参考答案**：
  1. **入站**：`PREROUTING` → 全部 TCP 跳到 `ISTIO_INBOUND` → 目标端口在劫持范围内的跳到 `ISTIO_IN_REDIRECT` → REDIRECT 到本地 **15006**（Envoy 的 virtualInbound listener）。
  2. **出站**：`OUTPUT` → 跳到 `ISTIO_OUTPUT` → 非 localhost 的流量跳到 `ISTIO_REDIRECT` → REDIRECT 到本地 **15001**（virtualOutbound listener）。
  3. **防循环的关键**：`ISTIO_OUTPUT` 链里有一条规则——**来自 istio-proxy 用户空间（即 uid/gid 1337）的流量直接 RETURN**，跳出该链，不再重定向。否则 Envoy 自己发出的包会被再次劫持回 Envoy，形成死循环。
  4. **排除清单**：`traffic.sidecar.istio.io/excludeInboundPorts`、`excludeOutboundIPRanges` 等注解用来放行不该被劫持的流量（典型如访问云厂商 metadata 服务 169.254.169.254、或某些 UDP/非 TCP 协议）。
  5. **实操查看**：
     ```bash
     kubectl exec <pod> -c istio-proxy -- iptables -t nat -S
     # 或用 nsenter 进入 Pod netns 查看
     ```
  6. **istio-cni 方案**：用 CNI 插件在节点上配置规则，替代需要特权的 `istio-init`，避免给业务 Pod 授予 `NET_ADMIN`——在有 PSA/PSP 限制的环境是必选项。
- **易错点 / 面试官关注**：
  - 说不出 15001（outbound）与 15006（inbound）的区别。
  - 不知道 1337 这个 uid 的防循环作用——这是最能体现「真看过规则」的细节。
  - 忽略 `istio-init` 需要特权，在受限集群里会被 admission 拒绝。
  - 忘记 iptables 只劫持 TCP；UDP（如 DNS，除非开 DNS 代理）和非 IP 协议不走 Envoy。
- **延伸**：Q6、Q14、来源：[宋净超《理解 Istio 中 Envoy Sidecar 注入与流量劫持》](https://jimmysong.io/blog/envoy-sidecar-injection-in-istio-service-mesh-deep-dive/)

---

### Q6. Istio 用到的 15000/15001/15006/15020/15021/15090 端口分别是什么？

- **难度**：🟡 中级
- **关键词**：Envoy admin, virtualOutbound, virtualInbound, 健康检查, prometheus merge
- **概念速记**：Istio 在 Pod 内占用一批 15xxx 端口，分别承担管理、劫持、探针与指标职责；面试常作为「你是否真的在线上跑过」的试金石。
- **问题**：列举 Istio sidecar 占用的关键端口及用途。为什么 Pod 的 readinessProbe 要走 15021 而不是应用端口？
- **参考答案**：
  | 端口 | 用途 |
  |---|---|
  | **15000** | Envoy admin 接口（`/config_dump`、`/stats`、`/clusters`、`/logging`），只监听 localhost，排障主力 |
  | **15001** | virtualOutbound——出站流量劫持目标 |
  | **15006** | virtualInbound——入站流量劫持目标 |
  | **15020** | pilot-agent 的管理端口：**合并**应用与 Envoy 的 Prometheus 指标、健康检查转发、调试 |
  | **15021** | 健康检查端口（`/healthz/ready`），Gateway/Sidecar 的 readiness 走这里 |
  | **15090** | Envoy 原始 Prometheus 指标端口 |
  | **15008** | ambient 模式下 ztunnel 的 HBONE 端口（见 Q15） |
  | **15012** | istiod 的 XDS+CA gRPC 端口（双向 TLS） |
- **参考答案（要点补充）**：
  1. **为什么探针要改道**：开启 STRICT mTLS 后，kubelet 直接访问应用端口的明文探针会被 Envoy 拒绝。Istio 通过 **probe rewrite**（`sidecar.istio.io/rewriteAppHTTPProbers`）把 httpGet 探针改写成访问 15020，由 pilot-agent 在 Pod 内部转发到应用，从而绕过 mTLS。
  2. **常用排障命令**：
     ```bash
     kubectl exec <pod> -c istio-proxy -- curl -s localhost:15000/config_dump | less
     kubectl exec <pod> -c istio-proxy -- curl -s localhost:15000/clusters | grep reviews
     kubectl exec <pod> -c istio-proxy -- curl -s -XPOST localhost:15000/logging?level=debug
     ```
- **易错点 / 面试官关注**：
  - 混淆 15001/15006 的方向。
  - 不知道 15020 做了「指标合并」，导致以为要单独抓 15090。
  - 不知道探针改写机制，遇到「开了 mTLS 后 Pod 一直 NotReady」定位不出来。
- **延伸**：Q5、Q13、Q17

---

### Q7. Istio 的 mTLS 是怎么建立的？PeerAuthentication 的 STRICT / PERMISSIVE 有什么区别？

- **难度**：🟡 中级
- **关键词**：mTLS, PeerAuthentication, PERMISSIVE, DestinationRule TLS mode, ALPN
- **概念速记**：
  - **PeerAuthentication**：定义**服务端**接受什么样的连接（STRICT 只收 mTLS / PERMISSIVE 明文与 mTLS 都收 / DISABLE 只收明文）。
  - **DestinationRule 的 `trafficPolicy.tls.mode`**：定义**客户端**发出什么（`ISTIO_MUTUAL` / `SIMPLE` / `MUTUAL` / `DISABLE`）。
  - 两者是**一对**：一边管收，一边管发，配错了就单向不通。
- **问题**：如何在一个正在运行的生产网格里，把全网格从明文安全地切换到 STRICT mTLS？
- **参考答案**：
  1. **先理解握手**：客户端 Envoy 用 istiod 签发的工作负载证书发起 mTLS；双方通过 **ALPN**（`istio`）协商；服务端 Envoy 校验对端证书中的 SPIFFE ID 后卸载 TLS，明文交给应用。整个过程应用无感知。
  2. **迁移步骤（关键就是 PERMISSIVE 这个过渡态）**：
     - ① 全网格保持默认 **PERMISSIVE**（Istio 默认值），先把所有工作负载都注入 sidecar。
     - ② 用指标验证：`istio_requests_total{connection_security_policy="mutual_tls"}` 占比是否接近 100%，或 Kiali 的安全视图看哪些边还是明文。
     - ③ 按 namespace 逐个收紧为 STRICT，观察一段时间。
     - ④ 最后把 mesh-wide 的 PeerAuthentication 设为 STRICT。
  3. **必须一并处理的例外**：
     - 没注入 sidecar 的工作负载（如 DaemonSet 日志采集、旧的中间件）→ 单独留 PERMISSIVE 或 `portLevelMtls`。
     - kubelet 探针 → 靠 probe rewrite（见 Q6）。
     - 从网格外进来的流量（Ingress 之前、跨集群）→ 走 Gateway 或 ServiceEntry。
  4. **回滚要快**：PeerAuthentication 是即时生效的 CRD，出问题 `kubectl delete` 即可回到宽松态。
- **易错点 / 面试官关注**：
  - 只改了 PeerAuthentication（服务端收），忘了客户端侧的 DestinationRule 还写着 `DISABLE`，导致 503。
  - 直接全网格 STRICT，把探针、无 sidecar 的组件、Prometheus 抓取全打挂。
  - 不知道 PERMISSIVE 的存在价值就是「灰度迁移」。
- **延伸**：Q8、Q9

---

### Q8. Istio 里工作负载的身份从哪来？SPIFFE / SVID / 证书轮转是怎么回事？

- **难度**：🔴 高级
- **关键词**：SPIFFE ID, SVID, SDS, 节点证明 node attestation, 工作负载证明, 信任域 trust domain
- **概念速记**：
  - **SPIFFE**：通用的工作负载身份标准。**SPIFFE ID** 形如 `spiffe://<trust-domain>/ns/<ns>/sa/<serviceaccount>`，Istio 里身份的粒度是 **ServiceAccount**，不是 Pod。
  - **SVID**：SPIFFE Verifiable Identity Document，即承载 SPIFFE ID 的 X.509 证书（放在 SAN 的 URI 字段）或 JWT。
  - **SDS（Secret Discovery Service）**：xDS 家族中负责把证书/密钥推给 Envoy 的协议。Istio 里私钥**不落盘**，由 pilot-agent 在内存中生成 CSR、向 istiod 换证，经 SDS 交给 Envoy。
  - **SPIRE**：SPIFFE 的参考实现，分两阶段证明——**节点证明**（验证 agent 所在节点，凭据可以是云厂商实例身份文档、TPM、K8s ServiceAccount token 等）和**工作负载证明**（agent 通过内核/kubelet 信息确认调用方是哪个进程）。
- **问题**：Istio 的证书是怎么签发和轮转的？为什么说这比「给每个服务发一个长期证书」更安全？如果要跨 K8s 和虚拟机统一身份，怎么做？
- **参考答案**：
  1. **签发链路**：pilot-agent 启动 → 用 Pod 的 ServiceAccount token 向 istiod（CA）证明身份 → istiod 校验 token（TokenReview）后签发短期证书（默认 24h，可调到更短）→ 通过 SDS 下发给 Envoy → **到期前自动轮转**，无需重启 Pod。
  2. **为什么更安全**：
     - 私钥不落盘、不进镜像、不进 Secret，泄露面小。
     - 证书生命周期短，泄露后的窗口期小，等于内置了「自动吊销」。
     - 身份绑定到 ServiceAccount，天然可以和 RBAC、AuthorizationPolicy 联动（见 Q9）。
  3. **跨 K8s / VM 统一身份**：这正是 SPIFFE/SPIRE 的价值——K8s 里用 ServiceAccount token 做节点证明，VM 上用云实例身份文档或 TPM 做节点证明，最终都发同一信任域下的 SVID，网格两侧可以互认。Istio 支持接入外部 SPIRE 作为 CA。
  4. **多集群/多信任域**：跨集群 mTLS 要么共享同一个根 CA（common root），要么配置信任域联邦（trust domain federation），否则证书校验必然失败。
  5. **排障**：
     ```bash
     istioctl proxy-config secret <pod> -n <ns>        # 看 Envoy 手里的证书
     openssl x509 -in cert.pem -noout -text | grep URI  # SAN 里的 SPIFFE ID
     ```
- **易错点 / 面试官关注**：
  - 以为身份粒度是 Pod——实际是 ServiceAccount，所以「同一个 SA 下的两个 Deployment 在授权上无法区分」是真实的设计约束。
  - 不知道私钥不落盘（SDS 的核心价值）。
  - 多集群场景忘记统一根 CA，排查 `TLS error: certificate verify failed` 半天。
- **延伸**：Q7、Q9、Q22、来源：[Kubernetes Handbook - SPIRE](https://jimmysong.io/book/kubernetes-handbook/auth-spire/)

---

### Q9. AuthorizationPolicy 的匹配规则与生效顺序是什么？为什么说「DENY 优先」很关键？

- **难度**：🔴 高级
- **关键词**：AuthorizationPolicy, ALLOW/DENY/AUDIT/CUSTOM, 默认拒绝, RequestAuthentication
- **概念速记**：
  - **AuthorizationPolicy**：Istio 的 L4/L7 授权 CRD，`action` 可为 `ALLOW`（默认）/`DENY`/`AUDIT`/`CUSTOM`（外部授权器）。
  - **RequestAuthentication**：只负责**验证** JWT 是否合法，**不做**放行/拒绝决策；要拒绝无 token 的请求必须再配一条 AuthorizationPolicy。
- **问题**：一个工作负载上同时存在 ALLOW 和 DENY 策略，Istio 如何决策？如何实现「默认拒绝、白名单放行」？
- **参考答案**：
  1. **评估顺序（务必背准）**：
     - ① 先评估所有 **CUSTOM** 策略；
     - ② 再评估所有 **DENY**，**命中任一 DENY 立即拒绝**；
     - ③ 若该工作负载上**存在** ALLOW 策略，则必须命中其中之一才放行，否则拒绝；
     - ④ 若**不存在**任何 ALLOW 策略，则默认放行。
     → 结论：**DENY 优先于 ALLOW**；而「有 ALLOW 就默认拒绝其余」是最容易被忽视的隐式行为。
  2. **默认拒绝的标准做法**：在 `istio-system`（根命名空间）下一条空 `spec: {}` 的 ALLOW 策略即为「拒绝全部」：
     ```yaml
     apiVersion: security.istio.io/v1
     kind: AuthorizationPolicy
     metadata: {name: deny-all, namespace: istio-system}
     spec: {}          # 没有 rules 的 ALLOW = 谁都不匹配 = 全拒
     ```
     然后逐个 namespace/工作负载加白名单 ALLOW。
  3. **可匹配的维度**：`source`（principals=SPIFFE ID、namespaces、ipBlocks）、`operation`（hosts、methods、paths、ports）、`condition`（`request.headers[...]`、`request.auth.claims[...]`）。
  4. **依赖 mTLS 的点**：基于 `principals`（对端身份）的策略只有在 mTLS 生效时才有意义；PERMISSIVE 下明文请求没有对端身份，规则会不匹配 → 授权形同虚设。**先 STRICT，再谈授权。**
  5. **JWT 场景**：`RequestAuthentication` 校验签名与 issuer，然后 AuthorizationPolicy 用 `requestPrincipals: ["*"]` 要求必须带合法 token。
- **易错点 / 面试官关注**：
  - 以为「加了一条 ALLOW 只影响这一条路径」，结果同工作负载上其他路径全被拒。
  - 只配 RequestAuthentication 就以为鉴权做完了——无 token 的请求依然放行。
  - 在 PERMISSIVE 下写基于 principal 的策略，安全形同虚设。
  - 忘记根命名空间（默认 `istio-system`）的策略是全局生效的。
- **延伸**：Q7、Q8

---

### Q10. VirtualService / DestinationRule / Gateway / ServiceEntry / Sidecar 各自职责是什么？

- **难度**：🟡 中级
- **关键词**：VirtualService, DestinationRule, Gateway, ServiceEntry, Sidecar CRD
- **概念速记**：
  - **Gateway**：定义入口的「门」——监听哪个端口、什么协议、什么 host、用什么证书。只管门，不管门后怎么走。
  - **VirtualService**：定义「怎么路由」——匹配条件 → 目标服务/subset/权重，以及超时、重试、重写、故障注入。
  - **DestinationRule**：定义「到达目标之后的策略」——subset 划分、负载均衡算法、连接池、异常点检测（熔断）、上游 TLS 模式。
  - **ServiceEntry**：把网格外的服务（外部 API、自建 DB、VM 上的服务）纳入服务发现，之后就能用 VS/DR 治理它。
  - **Sidecar**：限制某个/某些工作负载的 sidecar **能看见哪些服务**，是控制面与数据面双重减负的关键（见 Q16）。
- **问题**：只写 VirtualService 把流量按 90/10 分到 v1/v2，为什么报 `no healthy upstream`？
- **参考答案**：
  1. **原因**：VirtualService 里的 `subset: v1` 只是一个**名字引用**，真正定义「v1 = 带 `version: v1` 标签的 endpoint」的是 **DestinationRule**。没有 DR，subset 对应的 Cluster 不存在，Envoy 就返回 503 `no healthy upstream` / `NR`（No Route）。
  2. **正确写法**：
     ```yaml
     # DestinationRule：先定义 subset
     spec:
       host: reviews
       subsets:
       - name: v1
         labels: {version: v1}
       - name: v2
         labels: {version: v2}
     ---
     # VirtualService：再按权重分流
     spec:
       hosts: [reviews]
       http:
       - route:
         - {destination: {host: reviews, subset: v1}, weight: 90}
         - {destination: {host: reviews, subset: v2}, weight: 10}
     ```
  3. **验证**：`istioctl proxy-config cluster <pod> --fqdn reviews... ` 看是否有 `outbound|9080|v1|reviews...`；`istioctl analyze` 能直接报出「引用了未定义的 subset」。
  4. **常见配套坑**：Pod 的标签里必须真有 `version: v1`；Service 的 port 必须命名为 `http`/`http-xxx`（或设 `appProtocol`），否则 Istio 按 TCP 处理，L7 路由规则整体不生效。
- **易错点 / 面试官关注**：
  - 说不清 VS 与 DR 的分工（一个管「怎么去」，一个管「到了之后怎么对待」）。
  - 不知道 **Service 端口命名协议前缀**这个经典坑。
  - 以为 ServiceEntry 是「出口白名单」——它首先是「服务发现补全」，出口管控靠 `outboundTrafficPolicy: REGISTRY_ONLY` + Egress Gateway。
- **延伸**：Q3、Q11、Q17

---

### Q11. 用 Istio 做金丝雀发布，与 K8s 原生滚动更新有什么本质区别？

- **难度**：🟡 中级
- **关键词**：金丝雀 canary, 流量权重, 副本比例, Argo Rollouts, Flagger
- **概念速记**：K8s 原生的「灰度」是靠**副本数比例**间接控制流量；Istio 是直接控制**流量权重**，两者解耦。
- **问题**：K8s Deployment 滚动更新能不能做金丝雀？和 Istio 的做法差在哪？生产里怎么做自动化渐进式发布？
- **参考答案**：
  1. **原生方案的局限**：想让 1% 流量进新版本，就得让新版本副本占总副本的 1% —— 100 个副本才能做到 1%，小规模服务根本做不到细粒度；而且**无法按 header/用户/地域**定向灰度。
  2. **Istio 方案**：新旧版本副本数各自独立（新版本可以只有 1 个副本），流量比例由 VirtualService 的 `weight` 决定；还能先做**定向灰度**（只有带 `x-canary: true` header 或特定用户走 v2），再逐步放开权重。
  3. **典型渐进式流程**：镜像流量（`mirror` + `mirrorPercentage`，只复制不影响响应）→ 内部用户定向 → 1% → 5% → 25% → 100%，每一步看 SLI。
  4. **自动化**：**Flagger** 或 **Argo Rollouts** 接管这个过程——按 Prometheus 指标（成功率、P99）自动推进或自动回滚，避免人肉盯盘。
  5. **必须注意的陷阱**：
     - **会话一致性**：无状态服务才能随意分流；有状态/有本地缓存的要配 `consistentHash` 做会话亲和。
     - **数据库 schema**：流量可以秒回滚，数据库变更不能。schema 必须向前兼容（先加列不删列）。
     - **指标要能区分版本**：`istio_requests_total` 带 `destination_version` label，这是自动化判断的基础（见 Q13）。
- **易错点 / 面试官关注**：
  - 说不出「副本比例 vs 流量权重」这个本质差异。
  - 只讲流量切换，不讲回滚判据和数据库兼容性。
  - 忘了金丝雀的前提是新旧版本共存期的兼容性（API、消息格式）。
- **延伸**：Q10、Q13、[cicd-iac/cicd-iac-questions.md](../cicd-iac/cicd-iac-questions.md) Q3

---

### Q12. Istio 的超时、重试、熔断（outlier detection）怎么配？有哪些坑？

- **难度**：🔴 高级
- **关键词**：timeout, retries, connectionPool, outlierDetection, 重试风暴, 熔断
- **概念速记**：
  - **timeout / retries**：写在 VirtualService（落到 RDS 的 route 上）。
  - **connectionPool**：写在 DestinationRule，限制并发连接数/待处理请求数——达到上限直接快速失败，这是**真正意义上的限流式熔断**。
  - **outlierDetection**：被动健康检查——连续 N 个 5xx 就把该 endpoint 从负载均衡池里**临时弹出**（ejection），一段时间后再放回。
- **问题**：给一个下游不稳定的服务配重试，结果故障时集群雪崩得更快，为什么？怎么正确配置？
- **参考答案**：
  1. **重试风暴（retry storm）**：调用链 A→B→C，每层各重试 3 次，C 故障时 C 实际承受的请求是 3×3=9 倍。**下游已经过载时，重试是在火上浇油。**
  2. **正确做法**：
     - 只在**最靠近用户的一层**或明确幂等的调用上重试；深层链路关掉重试。
     - 必须配 `perTryTimeout`，且满足 `perTryTimeout × attempts < timeout`，否则重试还没做完整体超时就到了，配置形同虚设。
     - `retryOn` 精确指定条件（`5xx,reset,connect-failure,retriable-status-codes`），**不要重试非幂等的 POST**。
     - Envoy 默认带 **retry budget / 指数退避 + 抖动**，但跨层叠加仍需人为收敛。
  3. **熔断分两种，别混**：
     ```yaml
     trafficPolicy:
       connectionPool:                     # 主动限流：超过就快速失败
         tcp:  {maxConnections: 100}
         http: {http2MaxRequests: 1000, maxRequestsPerConnection: 10,
                http1MaxPendingRequests: 100}
       outlierDetection:                   # 被动剔除：连续 5xx 就弹出
         consecutive5xxErrors: 5
         interval: 10s
         baseEjectionTime: 30s
         maxEjectionPercent: 50            # ← 关键：别把整个池子弹空
     ```
  4. **`maxEjectionPercent` 是救命参数**：默认 10%。如果故障是全局性的（比如下游 DB 挂了，所有 endpoint 都返回 5xx），不设上限会把所有实例都弹出，服务直接 100% 不可用——从「部分降级」变成「完全宕机」。
  5. **验证**：`istioctl proxy-config cluster <pod> -o json` 看 `outlierDetection`/`circuitBreakers` 是否真的下发了；Envoy 指标 `upstream_rq_pending_overflow`、`upstream_cx_overflow`、`outlier_detection.ejections_active` 是观测点。
- **易错点 / 面试官关注**：
  - 只知道「配了 retries 更可靠」，没有雪崩意识。
  - 分不清 connectionPool（主动）与 outlierDetection（被动）。
  - 不知道 `perTryTimeout` 与 `timeout` 的数学关系。
  - 不设 `maxEjectionPercent`。
- **延伸**：[sre-reliability/sre-questions.md](../sre-reliability/sre-questions.md) Q3、Q13

---

### Q13. Istio 的服务级指标是怎么产生的？Metadata Exchange 机制是什么？为什么它会引发 Envoy OOM？

- **难度**：🔴 高级
- **关键词**：istio_requests_total, Metadata Exchange, Stats Filter, ALPN 协商, 指标基数
- **概念速记**：
  - **Envoy 原生 stats** 只有代理自身维度；Istio 额外加了 **Stats Filter**（L7/L4 各一个）生成**服务维度**指标：`istio_requests_total`、`istio_request_duration_milliseconds`、`istio_tcp_sent_bytes_total` 等。
  - **Metadata Exchange**：让通信双方互相知道对方是谁，从而把「对端服务名/版本/命名空间」作为 label 打进指标。
- **问题**：`istio_requests_total` 上的 `source_workload`、`destination_version` 这些 label 是怎么来的？给指标加一个自定义 label 有什么风险？
- **参考答案**：
  1. **L7（HTTP/gRPC）**：Istio 在 Envoy 里加了 metadata exchange 的 **http filter**，客户端在请求里塞两个 header——`x-envoy-peer-metadata-id`（形如 `sidecar~<ip>~<pod>.<ns>~<ns>.svc.cluster.local`）和 `x-envoy-peer-metadata`（base64 编码的节点元数据：workload 名、namespace、version、labels、Istio 版本等）；服务端在响应里回同样两个 header。双方各自拿到对端信息，存入 Envoy 的 **filter state**。
  2. **L4（TCP）**：HTTP header 用不了，Istio 定义了一个简易的 **tcp metadata exchange 协议**——在应用数据前加一个 header（魔数 `0x3D230467` + body 长度）再跟元数据。
  3. **能力协商靠 ALPN**：对端可能版本低或压根没 sidecar。支持该协议的 Envoy 在 TLS ClientHello 的 ALPN 里带上 `istio-peer-exchange`，双方都支持才启用。**所以未启用 TLS 时，L4 的 metadata exchange 不会生效**，指标里对端信息会缺失（显示 `unknown`）。
  4. **Stats Filter** 最后读取 filter state，把对端元数据作为 label 生成上述服务级指标。
  5. **为什么会 OOM——指标基数爆炸**：Envoy 把所有 stats 常驻内存，**指标数 = 各 label 取值的笛卡尔积**。加一个取值范围 10 的 label，指标数就 ×10。典型事故是把 **request path** 加进 label，而 path 里含 ID 等变量（`/order/12345`），瞬间生成上百万时间序列，Envoy 内存直接打爆。
  6. **防范**：自定义 label 只用**有限枚举值**；需要 path 维度就先做模板化归一（`/order/{id}`）；用 `Telemetry` API 裁剪不需要的指标与 label；监控 `envoy_server_memory_allocated` 与 Pod 内存水位。
- **易错点 / 面试官关注**：
  - 不知道对端信息是靠 header/TCP 协议交换来的，以为控制面直接给。
  - 不知道 L4 场景依赖 TLS+ALPN，遇到「TCP 服务指标里对端全是 unknown」查不出原因。
  - 随手给指标加高基数 label——这是网格里最常见的自伤型故障。
- **延伸**：Q6、[observability/observability-questions.md](../observability/observability-questions.md) Q2、来源：[赵化冰《Istio Metrics 实现机制深度解析》](https://zhaohuabing.com/post/2023-02-14-istio-metrics-deep-dive/)

---

### Q14. Istio Ambient 模式的架构是什么？ztunnel + waypoint 相比 sidecar 的取舍？

- **难度**：🔴 高级
- **关键词**：ambient mesh, ztunnel, waypoint proxy, 分层网格, Rust
- **概念速记**：
  - **Ambient**：Istio 的「无 sidecar」模式，把网格拆成两层。
  - **ztunnel（zero-trust tunnel）**：每节点一个的 DaemonSet，用 **Rust** 重写，只做 **L4**——mTLS、L4 授权、TCP 层指标。
  - **waypoint proxy**：**按需**部署（按 namespace 或按 service account）的 Envoy，只有需要 L7 能力（HTTP 路由、重试、L7 授权）时才拉起。
- **问题**：ambient 模式相比 sidecar 模式解决了什么？代价是什么？什么场景仍然该用 sidecar？
- **参考答案**：
  1. **解决的核心痛点**：
     - **资源开销**：不再是「每 Pod 一个 Envoy」，L4 能力由节点级 ztunnel 共享承担。
     - **运维侵入**：不需要注入容器、不需要改 Pod spec、**升级网格不需要重启业务 Pod**——这是最实在的收益。
     - **渐进采用**：可以只开 L4（零信任加密 + L4 授权）而完全不引入 L7 代理的延迟与复杂度。
  2. **代价与风险**：
     - **故障域变大**：ztunnel 是节点级组件，它挂了影响整个节点的网格流量（sidecar 的故障域只是单个 Pod）。
     - **多跳**：需要 L7 时路径变成 `client → ztunnel → waypoint → ztunnel → server`，跳数不一定比 sidecar 少。
     - **成熟度与生态**：部分 EnvoyFilter/WASM 扩展、某些 L7 策略在 ambient 下语义不同或尚未覆盖。
  3. **安全性有第三方背书**：2025 年 Trail of Bits 对 ztunnel 做了安全审计（CNCF 资助、OSTIF 协调），结论是代码本身**无漏洞类发现**，三条建议集中在依赖管理与测试覆盖（已用 Dependabot、自研 Forwarded header 解析器 + fuzz 解决）。性能上 ztunnel 的 TCP 吞吐甚至高于内核态的 IPsec / WireGuard。
  4. **选型建议**：
     - 只要**零信任加密 + L4 策略 + 基础指标** → ambient，成本最低。
     - 需要**精细 L7 治理**（按 header 灰度、复杂重试、WASM 扩展）→ 该 namespace 加 waypoint，或继续用 sidecar。
     - 两种模式**可以在同一网格共存**，逐 namespace 迁移。
- **易错点 / 面试官关注**：
  - 以为 ambient 就是「把 Envoy 挪到节点上」——关键是 **L4/L7 分层 + L7 按需**。
  - 只说省资源，说不出故障域变大这个真实代价。
  - 不知道 ztunnel 是 Rust 写的独立代码库（不是 Envoy）。
- **延伸**：Q15、Q24、来源：[Istio ztunnel 安全评估](https://istio.io/latest/blog/2025/ztunnel-security-assessment/)

---

### Q15. HBONE 是什么？为什么 ambient 要用 HTTP CONNECT 隧道？

- **难度**：🔴 高级
- **关键词**：HBONE, HTTP CONNECT, HTTP/2 隧道, Internal Listener, mTLS
- **概念速记**：
  - **HBONE（HTTP-Based Overlay Network Environment）**：ambient 模式下 ztunnel 之间、ztunnel 与 waypoint 之间的传输协议——用 **HTTP/2 的 CONNECT** 建立隧道，隧道内承载原始 TCP 流，隧道本身用 **mTLS** 加密。默认端口 **15008**。
- **问题**：为什么不直接用 mTLS 裸 TCP，而要套一层 HTTP CONNECT？
- **参考答案**：
  1. **HTTP CONNECT 的本质**：客户端发 `CONNECT host:port HTTP/2`，代理建立到目标的 TCP 连接后回 200，之后连接退化成一根双向字节管道。Envoy 原生支持既做隧道客户端也做隧道服务端（配合 **Internal Listener** 可以在同一进程内把隧道内流量再交给另一个 filter chain 做 L7 处理）。
  2. **为什么需要它——原始目的地址丢失问题**：ztunnel 是节点级共享代理，一个连接到达 ztunnel 时，必须知道「这个包本来要发给谁」。裸 TCP + mTLS 做不到带外传递元数据，而 CONNECT 请求行天然就携带目标地址。
  3. **可以顺便携带上下文**（这是相比裸 TCP 的关键增益）：
     - `authority`：请求的**原始目的地址**（如 `1.2.3.4:80`）。
     - `X-Forwarded-For`（可选）：原始源地址，多跳之间保留真实客户端 IP。
     - `baggage`（可选）：client/server 的元数据，供 telemetry 使用——相当于 ambient 版的 metadata exchange（对比 Q13 的 sidecar 做法）。
  4. **HTTP/2 多路复用的好处**：多个逻辑连接复用一条 ztunnel 之间的 TCP+TLS 连接，减少握手开销——对节点级共享代理这个场景收益很大。
  5. **与 sidecar 的对比**：sidecar 模式靠 iptables REDIRECT + `SO_ORIGINAL_DST` 拿原始目的地址；ambient 里跨节点后这个信息就没了，所以必须靠 HBONE 显式携带。
- **易错点 / 面试官关注**：
  - 只会说「HBONE 是 ambient 的隧道协议」，说不出「为什么需要隧道」（原始目的地址 + 上下文传递）。
  - 不知道 15008 端口。
  - 混淆 HBONE 与 mTLS——HBONE 是隧道封装，mTLS 是隧道的加密方式，两者叠加。
- **延伸**：Q14、来源：[赵化冰《Istio Ambient 模式深度解析（一）HBONE》](https://zhaohuabing.com/post/2022-09-11-ambient-deep-dive-1/)

---

### Q16. 大规模网格（数千服务）下控制面 CPU/内存飙高，怎么优化？

- **难度**：🔴 高级
- **关键词**：Sidecar CRD, discoverySelectors, 配置裁剪, 全量推送, istiod 扩缩容
- **概念速记**：
  - **默认行为的致命之处**：如果不做任何限制，istiod 会把**网格内所有服务**的 Listener/Cluster/Endpoint 推给**每一个** sidecar。N 个服务 × M 个 Pod 的配置量是 O(N×M)，控制面 CPU、网络和每个 Envoy 的内存都会随规模平方级恶化。
- **问题**：网格里有 3000 个 Service、上万个 Pod，istiod 频繁 OOM、推送延迟很高，sidecar 内存也都几百 MB。怎么系统性优化？
- **参考答案**：
  1. **Sidecar CRD 做配置裁剪（收益最大的一招）**：显式声明每个 namespace 的工作负载只需要访问哪些服务：
     ```yaml
     apiVersion: networking.istio.io/v1
     kind: Sidecar
     metadata: {name: default, namespace: team-a}
     spec:
       egress:
       - hosts:
         - "./*"                    # 本 namespace
         - "istio-system/*"
         - "common/*"               # 只依赖的公共服务
     ```
     效果：该 namespace 的 Envoy 配置量从「全网格」降到「实际依赖」，内存与推送量常见能降一个数量级。
  2. **discoverySelectors**：在 MeshConfig 里让 istiod 干脆**只 watch 带特定标签的 namespace**，把非网格 namespace 的 Service 变更彻底挡在控制面之外，减少无谓的 push。
  3. **减少 push 触发源**：
     - 大量 Pod 频繁重建 → EDS 高频变更。稳定副本、避免抖动。
     - 尽量少用 `EnvoyFilter`（它会触发全量重算）。
     - 合理的 `PILOT_DEBOUNCE_AFTER` / `PILOT_DEBOUNCE_MAX` 做变更合并。
  4. **控制面本身**：istiod 水平扩容（多副本，Envoy 会分散连接）+ 提高 CPU limit；`PILOT_ENABLE_EDS_DEBOUNCE`、`PILOT_MAX_REQUESTS_PER_SECOND` 等限流参数。
  5. **观测指标**：`pilot_xds`（连接数）、`pilot_xds_pushes`、`pilot_proxy_convergence_time`（收敛时间，最关键的 SLI）、`pilot_xds_push_time`、`envoy_server_memory_allocated`。
  6. **架构级方案**：考虑 ambient 模式（L7 代理按需才有，见 Q14）或多控制面拆分（按业务域划分网格，见 Q22）。
- **易错点 / 面试官关注**：
  - 不知道默认是「全量推送」，这是网格规模化第一课。
  - 只想到「给 istiod 加内存」，没有从配置裁剪入手。
  - 不知道 `pilot_proxy_convergence_time` 是衡量控制面健康的核心指标。
- **延伸**：Q2、Q4、Q14

---

### Q17. 网格里「服务间调用 503」，你的排查顺序是什么？istioctl 怎么用？

- **难度**：🟡 中级
- **关键词**：istioctl analyze, proxy-status, proxy-config, 响应标志 response flags, UF/UH/NR
- **概念速记**：
  - **Envoy 响应标志（response flags）** 是网格排障的第一手线索，出现在 Envoy access log 里：
    | 标志 | 含义 | 常见原因 |
    |---|---|---|
    | `NR` | No Route | 没匹配到路由（VS 配错、端口未命名 http） |
    | `UH` | No healthy Upstream | 目标 cluster 里没有健康 endpoint（subset 未定义、标签不匹配） |
    | `UF` | Upstream Failure | 连不上上游（mTLS 不匹配、网络不通） |
    | `UO` | Upstream Overflow | 触发了 connectionPool 熔断 |
    | `URX` | 重试次数或超时耗尽 | 见 Q12 |
    | `DC` | Downstream Connection termination | 客户端提前断开 |
- **问题**：A 调 B 报 503，给出你的分步排查路径。
- **参考答案**：
  1. **看日志拿 response flag**（最快定位方向）：
     ```bash
     kubectl logs <pod-a> -c istio-proxy --tail=50 | grep -v ' 200 '
     ```
     根据 `NR/UH/UF/UO` 直接分流到下面对应分支。
  2. **静态配置体检**：
     ```bash
     istioctl analyze -n <ns>         # 能查出未定义 subset、冲突 VS、端口命名等大部分低级错误
     ```
  3. **控制面是否同步**：
     ```bash
     istioctl proxy-status            # 全是 SYNCED 才说明配置真下发了
     ```
     出现 `STALE` → 控制面推送有问题；`NOT SENT` → 该 proxy 压根没订阅到。
  4. **数据面实际配置**（逐层对照 Q3 的链路）：
     ```bash
     istioctl proxy-config route    <pod-a> --name 9080   # 路由有没有？→ 排 NR
     istioctl proxy-config cluster  <pod-a> --fqdn b.ns.svc.cluster.local
     istioctl proxy-config endpoint <pod-a> --cluster "outbound|9080|v1|b.ns..."  # 有没有健康端点？→ 排 UH
     ```
  5. **mTLS 方向**（排 UF）：检查 B 的 PeerAuthentication 是否 STRICT 而 A 的 DestinationRule 是 `DISABLE`；`istioctl proxy-config secret` 看证书是否正常。
  6. **应用层**：确认不是 B 自己返回的 503——`reporter="destination"` 的 `istio_requests_total` 和 B 的应用日志。
  7. **兜底大招**：`kubectl exec <pod> -c istio-proxy -- curl -s localhost:15000/config_dump` 看完整配置；开 debug 日志：`curl -XPOST localhost:15000/logging?level=debug`。
- **易错点 / 面试官关注**：
  - 直接上 tcpdump，不看 response flag——网格里 flag 能省 80% 时间。
  - 不知道 `istioctl analyze` 这个静态检查工具。
  - 分不清 503 是 Envoy 生成的还是应用返回的（看 `reporter` label 和 `upstream_service_time` 是否存在）。
- **延伸**：Q3、Q6、Q10、Q12

---

### Q18. Gateway API 与 Ingress 的本质区别是什么？它定义了哪几类角色？

- **难度**：🟡 中级
- **关键词**：Gateway API, GatewayClass, Gateway, HTTPRoute, 角色分离, 注解地狱
- **概念速记**：
  - **Ingress 的困境**：只有一个资源、只支持 HTTP/HTTPS、路由能力只有 host+path，其他一切（重写、限流、超时、灰度）全靠 **annotation**——而 annotation 各家实现互不兼容，形成「注解地狱」，且权限模型粗糙，一个 Ingress 对象里混了基础设施配置和业务路由。
  - **Gateway API**：用多个强类型资源替代单一 Ingress，并显式做**角色分离**。
- **问题**：Gateway API 相比 Ingress 改进了什么？它的资源模型和角色模型是怎样的？
- **参考答案**：
  1. **核心差异对比**：
     | 维度 | Ingress API | Gateway API |
     |---|---|---|
     | 资源模型 | 单一 Ingress | GatewayClass / Gateway / HTTPRoute 等多资源 |
     | 用户角色 | 单一角色 | 明确四类角色，权限可分离 |
     | 协议支持 | 仅 HTTP/HTTPS | HTTP/HTTPS/TCP/UDP/gRPC/TLS |
     | 路由能力 | 主机名 + 路径 | 还支持 header、method、query param 等多维匹配 |
     | 扩展方式 | annotation（非标准） | Policy 附着、外部引用等标准化机制 |
     | 权限控制 | 粗粒度 | 细粒度，支持跨 namespace 授权引用 |
  2. **四类角色与对应资源**：
     - **基础设施提供方（Infrastructure Provider）** → `GatewayClass`：定义由哪个控制器实现（类似 StorageClass 之于 PV）。
     - **集群运维（Cluster Operator）** → `Gateway`：定义监听器（端口、协议、证书），并通过 `allowedRoutes` 声明哪些 namespace 的 Route 可以绑上来。
     - **应用开发者（Application Developer）** → `HTTPRoute`/`GRPCRoute`/`TCPRoute`：在自己的 namespace 里写业务路由，通过 `parentRefs` 挂到 Gateway。
     - **应用运维**：调整具体路由策略。
     → 价值：运维管「门和证书」，开发管「自己的路由」，**互不越权**，这在多团队共享入口的场景是刚需。
  3. **跨 namespace 的安全性**：Route 要挂到别的 namespace 的 Gateway，必须 Gateway 侧 `allowedRoutes` 放行；要引用别的 namespace 的 Service，必须有 `ReferenceGrant`——从机制上杜绝了 Ingress 时代「随便写个 host 就能劫持别人流量」。
  4. **和网格的统一（GAMMA）**：Gateway API 不止管南北向，GAMMA 倡议让同一套 HTTPRoute 也能描述东西向（网格内）路由——Istio 已支持用 HTTPRoute 替代 VirtualService，长期看是 Istio 自有 API 的继任者。
- **易错点 / 面试官关注**：
  - 只会说「Gateway API 更强大」，说不出**角色分离**这个设计核心。
  - 不知道 `ReferenceGrant` / `allowedRoutes` 的安全意义。
  - 不知道 Gateway API 也覆盖网格内流量（GAMMA）。
- **延伸**：Q19、Q20、来源：[Gateway API 官方文档](https://gateway-api.sigs.k8s.io/)

---

### Q19. 生产环境从 Ingress 迁移到 Gateway API，你的步骤和风险控制是什么？

- **难度**：🔴 高级
- **关键词**：ingress2gateway, 双跑, 灰度切流, DNS 切换, 回滚
- **概念速记**：迁移的本质是「入口 IP 和路由语义都要换」，必须做到**可灰度、可回滚**，不能一把梭。
- **问题**：给出一个可回滚的迁移方案。注解功能怎么办？
- **参考答案**：
  1. **盘点**：列出现有全部 Ingress，重点标注**依赖 annotation 的功能**（重写、重定向、限流、超时、CORS、认证、canary），这些是迁移的真正难点。
  2. **字段映射**（标准能力直接翻译）：
     | Ingress | Gateway API |
     |---|---|
     | `spec.rules[].host` | `HTTPRoute.spec.hostnames` |
     | `spec.rules[].http.paths[]` | `HTTPRoute.spec.rules[].matches[]` |
     | `backend.service` | `HTTPRoute.spec.rules[].backendRefs[]` |
     | 注解式重定向 | `filters[].requestRedirect` |
     | 注解式重写 | `filters[].urlRewrite` |
     | 注解式 canary | `backendRefs[].weight`（原生支持，不再需要注解） |
     | 入口端口（隐式 80/443） | `Gateway.spec.listeners` **显式声明** |
     剩下没有标准对应的（限流、WAF、自定义认证）→ 用实现方的 **Policy 资源**（如 Envoy Gateway 的 `BackendTrafficPolicy`、`SecurityPolicy`）。
  3. **自动化起步**：用 `ingress2gateway` 工具批量把 Ingress 转成 Gateway/HTTPRoute 草稿，**但必须人工复核**——注解类功能它转不了。
  4. **双跑 + 灰度切流（风险控制的核心）**：
     - 新建 Gateway（会拿到**新的 LB IP**），与旧 Ingress **并行运行**，两边指向同一批后端 Service。
     - 内部先用 `curl -H "Host: xxx" http://<新IP>` 逐条验证路由、证书、header 行为。
     - 通过 **DNS 权重**（或上游 LB 权重）把真实流量 1% → 10% → 50% → 100% 逐步切到新 IP。
     - 观察期至少覆盖一个业务高峰。
     - 全量后再观察数天才删除旧 Ingress。
  5. **回滚**：DNS 权重调回 0 即可，秒级生效（这就是为什么要双跑而不是原地改）。注意提前把 DNS TTL 调小（如 60s）。
  6. **常见坑**：
     - 忘了 Gateway 必须**显式**声明 443 监听器和 `certificateRefs`，导致 HTTPS 不通。
     - `HTTPRoute` 和 `Gateway` 不在同一 namespace，忘配 `allowedRoutes` / `ReferenceGrant`，Route 状态是 `NotAllowedByListeners`。
     - path 匹配语义差异：Ingress 的 `Prefix` 与 Gateway API 的 `PathPrefix` 在尾斜杠、最长匹配上的细节不完全一致，要逐条验证。
     - 排障先看状态：`kubectl get gateway/httproute -o yaml` 里的 `status.conditions` 会明确写出为什么没生效。
- **易错点 / 面试官关注**：
  - 只讲字段映射，不讲双跑和 DNS 灰度——这是「有没有真做过生产迁移」的分水岭。
  - 忽略注解类功能的迁移难度（这往往占工作量的 70%）。
  - 不知道新 Gateway 会分配新 LB IP。
- **延伸**：Q18、Q20、来源：[Kubernetes Handbook - 从 Ingress 迁移到 Gateway API](https://jimmysong.io/book/kubernetes-handbook/service-discovery-migrating-from-ingress-to-gateway-api/)

---

### Q20. Nginx Ingress / Istio Gateway / Envoy Gateway 怎么选？

- **难度**：🔴 高级
- **关键词**：Envoy Gateway, Nginx Ingress, 动态配置, reload, 选型
- **概念速记**：
  - **Nginx 的时代局限**：配置是**静态文件**，变更要 reload。在 K8s 里 endpoint 秒级变化，reload 频繁会导致长连接被断、内存抖动、配置生效有延迟。
  - **Envoy 的云原生设计**：配置**全动态**（xDS），支持热更新不断连接；原生 gRPC/HTTP2/HTTP3 支持；可观测性（stats/tracing/access log）是一等公民；可用 WASM/Lua 扩展。
  - **Envoy Gateway**：CNCF 项目，以 Gateway API 为唯一用户接口，底下驱动 Envoy，把「Envoy 难配」这个门槛抹平。
- **问题**：给三种入口方案做选型对比，说明各自适用场景。
- **参考答案**：
  | | Nginx Ingress | Istio Ingress Gateway | Envoy Gateway |
  |---|---|---|---|
  | 用户 API | Ingress + 大量注解 | Gateway CRD（也支持 Gateway API） | **Gateway API 原生** |
  | 配置模型 | 静态 + reload | 动态 xDS | 动态 xDS |
  | 是否需要网格 | 否 | **通常与 Istio 网格绑定** | 否，独立可用 |
  | 协议 | HTTP/HTTPS/TCP(有限) | 全面 | 全面（含 gRPC/UDP/HTTP3） |
  | 运维成本 | 低，生态最熟 | 高（要维护整个控制面） | 中 |
  | 适合 | 存量系统、简单入口、团队只熟 Nginx | 已经上了 Istio，希望南北向+东西向统一治理 | 只要现代化网关、不想引入整个网格 |
  1. **选型主线**：
     - **已有 Istio 网格** → 直接用 Istio Ingress Gateway，南北向与东西向共用一套证书、策略与遥测，没必要再引入一套网关。
     - **不想上网格、但要 Gateway API 的能力**（多团队权限分离、gRPC、动态配置） → **Envoy Gateway**，这是当下最主流的新建选择。
     - **存量 Nginx Ingress 跑得好、需求简单** → 不要为了换而换；迁移成本主要在注解（见 Q19）。
  2. **新趋势——统一南北向与东西向**：Envoy Gateway 可以同时作为 ambient 网格的 **ingress gateway 和 waypoint proxy**，一套数据面覆盖两个方向，减少组件种类。
  3. **其他候选**：Cilium 的 Gateway API 实现（eBPF 数据面，与 CNI 同栈）、Traefik、APISIX——选型时统一看：Gateway API 一致性测试（conformance）通过程度、社区活跃度、团队运维能力。
- **易错点 / 面试官关注**：
  - 说不出 Nginx 的 reload 问题为什么在 K8s 里更严重。
  - 「因为 Istio 功能多所以选 Istio」——忽略为了一个入口网关而背上整个控制面的代价。
  - 不知道 Gateway API conformance 是重要的选型依据。
- **延伸**：Q18、Q24、来源：[赵化冰《为什么说 Envoy Gateway 是云原生时代的七层网关》](https://zhaohuabing.com/post/2023-04-11-why-eg-is-the-gateway-in-cloud-native-era/)

---

### Q21. 网格里的非 HTTP 协议（Dubbo / Redis / MySQL / MQ）怎么治理？

- **难度**：🔴 高级
- **关键词**：TCP 代理, MetaProtocol, Aeraki, 协议嗅探, appProtocol
- **概念速记**：
  - Istio 原生只对 **HTTP/HTTP2/gRPC** 有完整 L7 能力；其他协议默认退化成 **TCP 透传**——只有连接级指标，没有请求级路由、重试、限流。
  - **Aeraki Mesh / MetaProtocol**：在 Envoy 上提供一个通用的七层协议框架，只需描述协议的编解码即可获得路由/限流/指标能力，避免为每个协议重写一个 Envoy filter。
- **问题**：团队的 Dubbo 服务上网格后，发现只能看到 TCP 字节数，没法按方法灰度。怎么解决？
- **参考答案**：
  1. **先确认协议识别**：Istio 靠 Service 的**端口命名**（`http-`、`grpc-`、`tcp-`、`mysql-`…）或 `appProtocol` 字段判断协议。命名错了会直接按 TCP 处理——**排查第一步永远是看端口名**。
  2. **能力分级**：
     - **HTTP/gRPC**：完整 L7（路由、重试、超时、熔断、请求级指标）。
     - **Redis / MySQL / MongoDB / Kafka**：Envoy 有对应的原生 filter，能力有限（Redis 有代理与分片、MySQL 有基础指标），Istio 默认不启用，需要 EnvoyFilter 手动开。
     - **Dubbo / Thrift / 私有二进制协议**：Envoy 有 dubbo_proxy/thrift_proxy，但与 Istio API 的集成度低。
  3. **三条实际路线**：
     - **协议迁移**（最推荐）：Dubbo 支持 triple/gRPC 协议，切过去后直接享受完整 L7 能力，长期收益最大。
     - **Aeraki + MetaProtocol**：写一个协议的 codec（描述如何从字节流里解出 method、目标服务等元数据），即可用 Istio 风格的 CRD 做路由与限流，避免改业务。
     - **只做 L4**：接受只有连接级治理（mTLS + L4 授权 + 连接数熔断），这对 MySQL/Redis 这类「不需要 L7 路由，但需要加密和访问控制」的场景其实完全够用——ambient 模式（Q14）在这里性价比很高。
  4. **有状态中间件的特别注意**：Redis Cluster、Kafka 这类协议里带**重定向/元数据**（MOVED、broker 列表），代理介入可能破坏客户端的拓扑感知。要么放行不代理（`excludeOutboundPorts`），要么用专门支持该协议的代理方案。
- **易错点 / 面试官关注**：
  - 不知道端口命名/`appProtocol` 决定了协议处理方式——这是最高频的「配了没生效」原因。
  - 把有状态中间件（Redis Cluster）盲目塞进网格，导致客户端拿到的是代理 IP 而非真实节点，集群重定向失效。
  - 不知道「只做 L4」也是一种合理答案。
- **延伸**：Q10、Q14、来源：[赵化冰《Aeraki：如何在 Istio 中支持自定义协议》](https://zhaohuabing.com/post/2022-01-23-aeraki-how-to-implement-a-custom-protocol/)

---

### Q22. 多集群网格有哪几种部署模型？东西向网关和信任域怎么处理？

- **难度**：🔴 高级
- **关键词**：primary-remote, multi-primary, 东西向网关 east-west gateway, 信任域, locality 负载均衡
- **概念速记**：
  - **网络维度**：单网络（集群间 Pod IP 直通）vs 多网络（跨集群需经网关）。
  - **控制面维度**：**multi-primary**（每个集群一套 istiod，互相 watch 对方 API Server）vs **primary-remote**（一个主控制面管多个远端集群）。
  - **东西向网关（east-west gateway）**：多网络模型下，跨集群流量的出入口，用 **SNI 路由**（AUTO_PASSTHROUGH）把 mTLS 流量直接透传到目标集群，不解密。
- **问题**：两个跨云的 K8s 集群要组成一个网格，你怎么设计？有哪些前置条件？
- **参考答案**：
  1. **先确定网络模型**：Pod CIDR 是否可路由互通？跨云通常**不通** → 走**多网络 + 东西向网关**模型。
  2. **控制面模型选择**：
     - **multi-primary**：每集群独立 istiod，任一控制面挂了另一集群仍可用 → **可用性高**，推荐生产。代价是每个 istiod 都要有对方 API Server 的凭据（`istioctl create-remote-secret`）。
     - **primary-remote**：远端集群无控制面，运维简单、成本低，但主控制面是单点，且跨地域的 xDS 连接稳定性要求高。
  3. **前置条件（缺一不可）**：
     - **共享信任根**：所有集群的 istiod 必须用**同一个根 CA** 签发的中间 CA，否则跨集群 mTLS 证书校验必然失败。这是多集群网格最常见的第一个坑。
     - **统一信任域**（`trustDomain`）或配置信任域联邦。
     - **集群唯一标识**：每个集群有唯一 `clusterName` 和 `network` 标签，istiod 靠它决定「同网络直连」还是「走东西向网关」。
     - 东西向网关之间网络可达（公网需加固，最好走专线/VPN）。
  4. **流量行为**：
     - 同名 Service 在多集群都存在时，endpoint 会被聚合，默认按 **locality** 优先本地（`localityLbSetting`），本地不健康才溢出到远端——这正是多集群做容灾的价值。
     - 跨集群调用路径：`client sidecar → 本集群 east-west gw → 对端 east-west gw → 目标 sidecar`，全程 mTLS，网关只按 SNI 转发不解密。
  5. **运维复杂度警告**（面试要主动提）：多集群网格把「网络 + 证书 + 控制面 + DNS」四个复杂度叠加。除非确有跨地域容灾/合规需求，否则先考虑**多个独立网格 + 集群间走普通 Gateway** 这种更简单的方案。
- **易错点 / 面试官关注**：
  - 忘记共享根 CA。
  - 说不清东西向网关为什么用 SNI passthrough（保持端到端 mTLS，网关不需要也不应该持有工作负载私钥）。
  - 不知道 locality 优先才是多集群的主要收益。
- **延伸**：Q8、Q16

---

### Q23. Sidecar 与应用容器的启动/停止顺序问题怎么解决？

- **难度**：🟡 中级
- **关键词**：启动竞态, holdApplicationUntilProxyStarts, preStop, sidecar containers, Job 卡住
- **概念速记**：K8s 1.29 之前，Pod 内容器**没有启动顺序保证**，这给 sidecar 模式带来两个经典问题：应用比 Envoy 先启动（出站请求失败）、Envoy 比应用先退出（优雅停机期间请求失败）。
- **问题**：应用启动时立刻访问下游就报连接被拒；另外 Job 跑完了 Pod 却一直不结束。分别怎么解决？
- **参考答案**：
  1. **启动竞态**：应用先起来发请求，此时 iptables 规则已经生效但 Envoy 还没 ready → 流量被劫持到一个没准备好的代理 → 连接被拒。
     - **方案 A（推荐）**：`holdApplicationUntilProxyStarts: true`（全局 MeshConfig 或 Pod 注解 `proxy.istio.io/config`）。它给 istio-proxy 加了一个 postStart hook，**阻塞到 Envoy ready 才启动业务容器**。
     - **方案 B（根治）**：K8s **1.29+ 的原生 sidecar containers**（`initContainers` 里设 `restartPolicy: Always`）——sidecar 保证先于业务容器启动、后于业务容器终止，这是社区的最终解法。Istio 已支持。
     - **方案 C（兜底）**：应用侧自带启动重试，这本来也是健壮性应有的行为。
  2. **停止顺序**：Envoy 先退出 → 应用还在处理的请求发不出去。
     - Istio 默认给 istio-proxy 配了 `preStop` 睡眠 + `EXIT_ON_ZERO_ACTIVE_CONNECTIONS`，等活跃连接归零再退。
     - 保证 `terminationGracePeriodSeconds` 足够长，覆盖应用的优雅停机时间。
  3. **Job / CronJob 不结束**：业务容器退出了，但 istio-proxy 是常驻进程，Pod 永远不是 `Completed`。
     - K8s 1.29+ 原生 sidecar 直接解决（业务容器退出后 sidecar 自动终止）。
     - 老版本变通：任务结束时 `curl -XPOST http://localhost:15020/quitquitquit` 让 pilot-agent 退出；或给该 Job 关闭注入（`sidecar.istio.io/inject: "false"`）。
- **易错点 / 面试官关注**：
  - 只知道有这个问题，不知道 `holdApplicationUntilProxyStarts` 这个开关。
  - 不知道 K8s 1.29 的原生 sidecar 容器已经从机制上解决了它。
  - Job 场景没意识到会卡住，上线后才发现 CronJob 堆积。
- **延伸**：Q5、[kubernetes/kubernetes-questions.md](../kubernetes/kubernetes-questions.md) Q29

---

### Q24. 服务网格的代价是什么？什么情况下不该上网格？eBPF 方案是替代还是补充？

- **难度**：🔴 高级
- **关键词**：延迟开销, 资源开销, 认知负担, Cilium Service Mesh, eBPF, 无 sidecar
- **概念速记**：网格不是免费的。面试里能主动、准确地说出代价，比能背出多少 CRD 更能体现资深度。
- **问题**：老板问「我们要不要上 Istio」，你怎么回答？
- **参考答案**：
  1. **先算代价**：
     - **延迟**：每次调用多两跳用户态代理，典型增加 **单跳亚毫秒到数毫秒**（取决于 L7 处理复杂度）。对 P99 敏感的交易链路必须实测。
     - **资源**：sidecar 模式下每 Pod 一个 Envoy，内存与配置量正相关（不做裁剪时几百 MB 很常见，见 Q16）；千 Pod 规模下这是一笔实打实的成本。
     - **认知与运维**：多一层排障（Q17 那一整套）、控制面要升级要监控、团队需要专门的人懂 Envoy。
     - **故障域**：控制面/ztunnel 成为新的关键路径组件。
  2. **什么时候「不该」上**：
     - 服务数量少（十几个）、语言单一、已有成熟 SDK 治理 → 收益覆盖不了复杂度。
     - 团队没有专人能维护控制面 → 网格会成为新的故障源而非可靠性来源。
     - 对延迟极度敏感的场景（高频交易、实时音视频转发）。
     - **只需要加密**：如果诉求仅是「东西向流量加密」，Cilium 的 WireGuard/IPsec 透明加密或 ambient 的 L4 模式（Q14）都比全量 sidecar 网格便宜得多。
  3. **什么时候「该」上**：多语言、服务数量上百、强合规要求（零信任、全链路加密与审计）、需要统一的灰度发布与故障注入能力、跨集群/跨云统一治理。
  4. **eBPF 方案是补充而非完全替代**：
     - **eBPF 擅长的**：L3/L4——连接级策略、透明加密、负载均衡（替代 kube-proxy）、无侵入可观测（Hubble/Pixie）。在内核态做，**没有用户态代理的跳数开销**。
     - **eBPF 不擅长的**：复杂 L7 处理（HTTP 路由、JWT 校验、重试、WASM 扩展）。eBPF 程序有指令数/循环/验证器限制，做完整 HTTP 协议栈既不现实也不安全。所以 Cilium Service Mesh 在需要 L7 时同样要拉起 Envoy（只是**每节点一个**而非每 Pod 一个）。
     - **结论**：行业的收敛方向正是「**L4 下沉（eBPF 或 Rust 写的节点级代理），L7 按需（Envoy）**」——Istio ambient 和 Cilium Service Mesh 在架构上殊途同归。
  5. **务实建议**：先用最小可行范围验证（一个业务域、只开 mTLS + 指标），把延迟和资源数据测出来，再决定是否推广。
- **易错点 / 面试官关注**：
  - 一味推销网格，说不出代价 → 面试官会认为没有真实生产经验。
  - 认为 eBPF 能完全替代 Envoy（L7 做不了）。
  - 不知道「只要加密」有远比网格便宜的方案。
- **延伸**：Q1、Q14、Q20、[kubernetes/kubernetes-questions.md](../kubernetes/kubernetes-questions.md) Q34

### Q25. 一个「多协议、多套旧网格、多种注册中心、K8s 与 VM 混布」的存量系统，怎么平滑迁到统一的 Istio 网格？

- **难度**：⚫ 资深
- **关键词**：异构迁移, 第二控制面, Aeraki, MetaProtocol, 外部服务发现 ServiceEntry, 多控制面合并, 全链路染色, 本地限流
- **概念速记**：
  - **第二控制面（second control plane）**：不改 Istio 本体，用一个旁路控制器（如 Aeraki）监听自己的 CRD 并生成 EnvoyFilter / 路由配置下发，从而给 Istio 补上它原生没有的协议与治理能力。
  - **外部服务发现同步**：把 L5 / Polaris（北极星）/ Consul / Eureka / Dubbo 注册中心里的实例 **watch 后同步成 Istio 的 `ServiceEntry`**，再由 istiod 通过 xDS 下发；网格内外的服务因此能互相看见。
  - **多控制面合并**：两套 Istio（例如 1.3.6 与 1.10）之间先用 **Gateway + ServiceEntry 互指**打通，再按权重把流量切到新网格，最后拆旧网格。
- **问题**：腾讯音乐 2021 年在 IstioCon 分享过这类迁移：业务有 HTTP / gRPC / 私有 RPC 协议并存，Istio 1.3.6 与 1.10 两套旧网格，L5 / Polaris / Consul / DNS 四种服务发现，C++ / Go / Node 多语言，K8s 与 VM 混布。若你来主导，迁移方案怎么分阶段？私有协议怎么获得七层治理？怎样保证业务无感？
- **参考答案**：
  1. **先定业务约束再选型**：业务的硬要求是「平滑迁移、无感知、代码改动少、流量透明可控、支持私有协议与多种服务发现」。据此选型标准是：**通用性**（sidecar 方案对任何框架都适用）、**兼容性**（Aeraki 作为第二控制面，不改 Istio 控制面）、**易用性**（MetaProtocol 让私有协议只需写编解码）、**可持续**（跟社区版本走，不魔改）。
  2. **私有协议：用 MetaProtocol 而不是手写 Envoy filter**：Istio 原生只对 HTTP/gRPC 有完整 L7 能力，其余协议按 TCP 处理（只有连接级指标与四层路由）。自己写 EnvoyFilter 的两大痛点是**实现复杂**和**要专门做控制面**。MetaProtocol 已把负载均衡、熔断、RDS 动态路由、消息头修改、本地 / 全局限流、请求指标、调用跟踪做成通用逻辑，接入方只需实现 **decode / encode / onError 三个接口（约数百行）**并声明一个 `ApplicationProtocol`；控制面工作量为零，因为 Aeraki 天然是所有 MetaProtocol 协议的控制面。请求路径：Decoder 填 Metadata → L7 filter 处理并写 Mutation → Router 按 RDS 选 upstream cluster → Encoder 按 Mutation 封包。
  3. **外部服务发现：先同步再分步迁移**：以 Polaris 为例，Polaris-Controller 把 K8s 服务注册进北极星，`Polaris2Istio` 反向 watch 变更并同步成 `ServiceEntry`，Pilot 再通过 xDS 下发；Consul2Istio / Dubbo2Istio / Eureka2Istio 同理。迁移分四步：**方式 4** 服务在网格外、用旧服务发现 → **方式 3** 服务仍在网格外、旧服务名但通过网格内 ServiceEntry 接入 → **方式 2** 服务进网格、旧服务名指向 K8s Service → **方式 1** 直接用 K8s Service 名、旧名只作别名。每一步对调用方都是透明的，可随时回退。
  4. **多控制面合并分三阶段**：一阶段在新网格创建指回旧网格的 Gateway、对应 VirtualService、以及指向旧网格网关的 ServiceEntry（可编程自动生成），验证网络后把服务逐个迁到新网格；二阶段把流量权重切到新网格，在旧网格创建指向新网格网关的 **占位 ServiceEntry**，再卸载旧网格里的服务；三阶段移除指向旧网格的 ServiceEntry。全程要盯**资源水位与网络互通**两件事。
  5. **迁完之后网格能带来什么（证明投入值得）**：私有协议也能按「命令字」路由到不同版本 → 可做**全链路染色**：开发环境按分支隔离、生产按业务需求分版本；**本地限流是按单 Pod 计**（配额随副本数线性增长，例如 2 个 Pod 时「每分钟前 4 次成功」意味着单 Pod 2 次），可按子命令等条件限流；还有自定义协议的指标、全局限流、负载均衡、熔断、改消息头。他们的后续规划是 tracing 全面打通与治理平台化。
  6. **面试官想听到的风险意识**：Aeraki 第一版基于 Envoy 原生 dubbo / thrift filter，受限于这些 filter 功能不齐（无 RDS、限流、一致性哈希、镜像、跟踪）才演进到 MetaProtocol；两套网格共存时证书信任链与 `trustDomain` 要提前对齐（见 Q22）；VM 工作负载要用 WorkloadEntry / WorkloadGroup 纳管；每一步都要有回滚开关（权重切回、别名保留）。
- **易错点 / 面试官关注**：
  - 上来就说「升级 Istio、所有业务改成 gRPC」——这是理想方案不是迁移方案，忽略了私有协议与旧注册中心的存量。
  - 不知道 ServiceEntry 是网格内外互通与多网格互指的核心原语。
  - 把本地限流当全局限流，副本扩容后限流阈值悄悄变大。
  - 说不出为什么需要「第二控制面」而不是魔改 Istio（可持续性、跟社区升级）。
- **延伸**：Q10、Q14、Q21、Q22、kubernetes Q33、来源：赵化冰 / 王诚强《Tencent Music's service mesh practice with Istio and Aeraki》（IstioCon 2021 演讲，本地 PDF 存档）、[Aeraki Mesh](https://www.aeraki.net)、[meta-protocol-awesomerpc 模板](https://github.com/aeraki-mesh/meta-protocol-awesomerpc)

---

## 参考来源

本模块的事实性内容基于以下公开资料整理（均为技术博客 / 官方文档，观点与结论已结合面试场景重新组织）：

| 主题 | 来源 |
|---|---|
| xDS 四种变体、ADS、Delta、warming | [Envoy 官方文档 - xDS protocol](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol) |
| Sidecar 注入与 iptables 劫持逐条解析 | [宋净超 - 理解 Istio 中 Envoy Sidecar 注入与流量劫持](https://jimmysong.io/blog/envoy-sidecar-injection-in-istio-service-mesh-deep-dive/) |
| Istio Metrics / Metadata Exchange / 内存问题 | [赵化冰 - Istio Metrics 实现机制深度解析](https://zhaohuabing.com/post/2023-02-14-istio-metrics-deep-dive/) |
| HBONE / HTTP CONNECT 隧道 | [赵化冰 - Istio Ambient 模式深度解析（一）HBONE](https://zhaohuabing.com/post/2022-09-11-ambient-deep-dive-1/) |
| ztunnel 安全审计与性能 | [Istio Blog - ztunnel security assessment (2025)](https://istio.io/latest/blog/2025/ztunnel-security-assessment/) |
| Gateway API 资源模型与角色 | [Gateway API 官方文档](https://gateway-api.sigs.k8s.io/) |
| Ingress → Gateway API 迁移 | [Kubernetes Handbook - 从 Ingress 迁移到 Gateway API](https://jimmysong.io/book/kubernetes-handbook/service-discovery-migrating-from-ingress-to-gateway-api/) |
| Envoy Gateway 选型 | [赵化冰 - 为什么说 Envoy Gateway 是云原生时代的七层网关](https://zhaohuabing.com/post/2023-04-11-why-eg-is-the-gateway-in-cloud-native-era/) |
| 自定义协议 / Aeraki MetaProtocol | [赵化冰 - Aeraki：如何在 Istio 中支持自定义协议](https://zhaohuabing.com/post/2022-01-23-aeraki-how-to-implement-a-custom-protocol/) |
| 异构系统迁移 / 多控制面合并 / 外部服务发现（Q25） | 赵化冰、王诚强 - Tencent Music's service mesh practice with Istio and Aeraki（IstioCon 2021，本地 PDF 存档）|
| Ambient 分层架构与 sidecar 取舍（Q14 补充） | Abdel Sghiouar - Introduction to Istio Ambient Mesh（Conf42 Kube Native 2023，本地 PDF 存档）|
| SPIFFE / SPIRE 身份体系 | [Kubernetes Handbook - SPIRE](https://jimmysong.io/book/kubernetes-handbook/auth-spire/) |
