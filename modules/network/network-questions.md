# 网络面试题（27 题）

> 模板见 [../../docs/STANDARD.md](../../docs/STANDARD.md)。基础概念详见 [../../basics/02-network-osi.md](../../basics/02-network-osi.md)。

---

### Q1. TCP 拥塞控制算法（Reno/CUBIC/BBR）区别？
- **难度**：🔴 高级
- **关键词**：拥塞控制, CUBIC, BBR, 长肥管道
- **概念速记**：拥塞控制防止网络过载；BBR 基于带宽/RTT 模型，抗丢包。
- **问题**：高延迟高带宽链路为什么用 BBR？
- **参考答案**：
  - Reno（丢包驱动，高 BDP 效率低）；CUBIC（Linux 默认，三次函数）；BBR（Google，基于带宽/RTT，抗丢包、降缓冲膨胀，适合弱网/长肥管道）。`sysctl net.ipv4.tcp_congestion_control=bbr`。
- **易错点**：以为 BBR 在所有场景都优于 CUBIC。
- **延伸**：[basics/02-network-osi.md](../../basics/02-network-osi.md)；linux Q2

### Q2. TCP 粘包/拆包是什么？应用层怎么处理？
- **难度**：🟡 中级
- **关键词**：粘包, 拆包, 消息边界, 长度字段
- **概念速记**：TCP 是字节流无消息边界，发送多次可能合并/拆分。
- **问题**：TCP 为什么需要处理边界？
- **参考答案**：
  - 应用层解决：定长、分隔符、长度字段（header 带 body 长度，最常用）、协议层（HTTP Content-Length、RPC 框架）。UDP 无此问题但需自己保证可靠。
- **易错点**：默认 `recv` 一次拿到完整消息。
- **延伸**：linux Q5（epoll）

### Q3. TCP keepalive 与 HTTP keep-alive 区别？
- **难度**：🟡 中级
- **关键词**：TCP keepalive, HTTP keep-alive, 半开连接
- **概念速记**：TCP keepalive 探测死连接（传输层）；HTTP keep-alive 复用 TCP 连接（应用层）。
- **问题**：两者是一回事吗？
- **参考答案**：
  - 层级与目的不同：TCP keepalive 防半开连接（默认 2h）；HTTP keep-alive 减少握手开销（Connection: keep-alive）。
- **易错点**：混淆，以为开 HTTP keep-alive 就不用管 TCP 探测。
- **延伸**：linux Q2

### Q4. 半连接队列与全连接队列溢出会怎样？怎么排查？
- **难度**：🔴 高级
- **关键词**：SYN queue, accept queue, backlog, 连接超时
- **概念速记**：半连接（SYN 已收未确认）、全连接（已完成握手待 accept）；backlog 限制全连接。
- **问题**：客户端连接超时但服务活着？
- **参考答案**：
  - 半连接满→丢 SYN；全连接满→握手完成但 accept 不及时，客户端以为连上却无响应。`ss -lnt` 看 Recv-Q 接近 Send-Q；`netstat -s | grep overflowed`；调 `somaxconn`/`tcp_max_syn_backlog`、应用 backlog。
- **易错点**：只调应用 backlog 不调内核 somaxconn。
- **延伸**：linux Q22

### Q5. HTTP/1.1、2、3 核心区别？运维关注点？
- **难度**：🔴 高级
- **关键词**：HTTP2, HTTP3, QUIC, 队头阻塞
- **概念速记**：H2 多路复用单连接（仍受 TCP 队头阻塞）；H3 基于 QUIC/UDP 解决之。
- **问题**：升级到 HTTP/3 要做什么？
- **参考答案**：
  - H1.1（队头阻塞、多连接）；H2（多路复用、HPACK，需 TLS）；H3（QUIC/UDP，0-RTT、抗丢包）。运维：H2 需 TLS、注意头阻塞；H3 需放行 UDP 443、nginx/envoy 支持；观察 ALPN。
- **易错点**：以为 H2 彻底解决队头阻塞（仍受 TCP HOL）。
- **延伸**：linux Q（TLS）；Q47（QUIC）

### Q6. HTTPS/TLS 握手过程？TLS1.2 与 1.3 区别？证书链怎么验证？
- **难度**：🔴 高级
- **关键词**：TLS, 握手, 证书链, OCSP
- **概念速记**：TLS 在 TCP 之上提供加密与认证；1.3 简化握手、去弱套件。
- **问题**：TLS 握手要几个 RTT？
- **参考答案**：
  - 1.2：ClientHello→ServerHello+证书→密钥交换（ECDHE）→对称密钥（2 RTT）。1.3：1-RTT，可选 0-RTT，移除 RSA 密钥交换。验证：证书链（叶子→中间→根）、域名、有效期、吊销（OCSP/CRL）。
- **易错点**：忽略证书过期/链不全导致握手失败。
- **延伸**：cloud-security Q（证书管理）

### Q7. DNS 完整解析流程？递归与迭代区别？排查慢/失败？
- **难度**：🟡 中级
- **关键词**：DNS, 递归, 迭代, dig +trace
- **概念速记**：递归=客户端一次拿到结果（Local DNS 代为递归）；迭代=每级返回下一跳。
- **问题**：DNS 解析慢怎么定位？
- **参考答案**：
  - 顺序：hosts→本地 resolver→递归解析器→根→TLD→权威。`dig +trace`；`tcpdump port 53`；注意 TTL、NAT 下 DNS、DoH/DoT 兜底。
- **易错点**：只查权威 DNS 忽略 Local DNS 缓存。
- **延伸**：[basics/02-network-osi.md](../../basics/02-network-osi.md)；Q10（服务发现）

### Q8. Anycast DNS / Anycast IP 是什么？用在哪？
- **难度**：🔴 高级
- **关键词**：Anycast, BGP, 就近接入
- **概念速记**：同一 IP 多地点通告（BGP），路由送最近节点。
- **问题**：8.8.8.8 全球都能用是怎么做到的？
- **参考答案**：
  - Anycast + BGP，用于公共 DNS、CDN、DDoS 缓解。依赖 BGP，需防路由劫持（RPKI）；就近调度、抗攻击。
- **易错点**：误以为单台服务器承载全球流量。
- **延伸**：Q13（CDN）、cloud-security Q（BGP 劫持）

### Q9. LVS 的 NAT/DR/TUN 模式区别与适用？
- **难度**：🔴 高级
- **关键词**：LVS, NAT, DR, TUN, 四层负载
- **概念速记**：LVS 是 L4 负载均衡（IPVS），性能极高。
- **问题**：为什么 DR 模式性能最好？
- **参考答案**：
  - NAT（改目的 IP，回包经 Director，瓶颈）；DR（改 MAC，RS 配 lo 上 VIP，回包直连，需同二层，性能最好）；TUN（IP 隧道，跨网段）。七层用 Nginx/HAProxy/Envoy。
- **易错点**：DR 模式 RS 必须绑 VIP 到 lo 且抑制 ARP。
- **延伸**：Q11（L4 vs L7）

### Q10. 内网服务发现（Consul / CoreDNS）怎么工作？
- **难度**：🔴 高级
- **关键词**：服务发现, Consul, CoreDNS, TTL
- **概念速记**：服务发现让调用方动态找到实例，避免硬编码 IP。
- **问题**：K8s 里服务名怎么解析到 Pod？
- **参考答案**：
  - Consul：agent 注册健康，DNS 接口返回健康实例；CoreDNS：K8s 集群 DNS，watch Service/Endpoint 动态解析。对比：客户端 SDK vs DNS 侧（无侵入）。关注 TTL、缓存致摘除延迟。
- **易错点**：DNS TTL 过长导致摘除慢。
- **延伸**：kubernetes Q（Service/Ingress）；Q7

### Q11. 四层（L4）与七层（L7）负载均衡本质区别？
- **难度**：🟡 中级
- **关键词**：L4, L7, 反向代理, 路由
- **概念速记**：L4 基于 IP+端口（快、通用）；L7 基于应用层（智能路由）。
- **问题**：什么时候用 L7 而非 L4？
- **参考答案**：
  - L4 仅转发（快）；L7 按域名/路径/Header 路由、改写、认证（慢一点但智能）。仅需转发用 L4；需灰度/按域名用 L7。
- **易错点**：所有流量都上 L7 浪费性能。
- **延伸**：Q9

### Q12. HAProxy 与 Nginx 做七层负载怎么选？
- **难度**：🟡 中级
- **关键词**：HAProxy, Nginx, 反向代理, 健康检查
- **概念速记**：HAProxy 专业 LB，连接级控制强；Nginx Web+反向代理一体。
- **问题**：高并发长连接选哪个？
- **参考答案**：
  - HAProxy：专业 LB，健康检查强、长连接/高并发稳、stats 丰富。Nginx：生态大、易上手、静态强。极高并发/L4 也可 LVS/DPDK。云上用 ALB/NLB。
- **易错点**：用 Nginx 扛超长连接导致 worker 耗尽。
- **延伸**：Q9、Q11

### Q13. CDN 工作原理？回源、缓存命中、刷新？
- **难度**：🟡 中级
- **关键词**：CDN, 回源, 缓存命中, Cache-Control
- **概念速记**：CDN 边缘节点缓存内容，就近返回；未命中/过期则回源。
- **问题**：源站被打挂可能是什么原因？
- **参考答案**：
  - 缓存击穿（大量 key 同时失效/未命中）→ 回源风暴。治理：Cache-Control/Expires、刷新（URL/目录/全量）、源站保护、预热、HTTPS 回源、鉴权。
- **易错点**：缓存策略不当导致回源风暴。
- **延伸**：Q8、Q14

### Q14. 网络命名空间（netns）与 veth/bridge/overlay 关系？
- **难度**：🔴 高级
- **关键词**：netns, veth, bridge, overlay, 容器网络
- **概念速记**：netns 隔离网络栈；veth 成对跨 netns；bridge 像交换机；overlay 跨主机二层。
- **问题**：容器怎么和宿主通信？
- **参考答案**：
  - Pod netns ↔ veth ↔ 主机 bridge/CNI（Calico 路由、Flannel vxlan、Cilium eBPF）。overlay（VXLAN）封包走 UDP 跨主机。
- **易错点**：混淆 bridge（二层）与路由（三层）。
- **延伸**：[basics/04-kubernetes-concepts.md](../../basics/04-kubernetes-concepts.md)；kubernetes Q（CNI）

### Q15. 如何排查「能 ping 通但端口连不上」？
- **难度**：🟡 中级
- **关键词**：防火墙, 安全组, 监听地址, conntrack
- **概念速记**：ping（ICMP）通≠TCP 端口通，可能中间 ACL 或监听地址错。
- **问题**：ICMP 通但 8080 连不上？
- **参考答案**：
  - 分层：iptables/nftables 是否 DROP；安全组；`ss -lntp` 看监听 0.0.0.0 vs 127.0.0.1；conntrack 满；K8s NetworkPolicy。逐跳 `telnet`/`nc`/`tcpdump`。
- **易错点**：服务只监听 127.0.0.1 却从外部连。
- **延伸**：linux Q20；kubernetes Q（NetworkPolicy）

### Q16. iptables 与 nftables 区别？容器网络常用哪套？
- **难度**：🔴 高级
- **关键词**：iptables, nftables, conntrack, eBPF
- **概念速记**：iptables 规则链式，规则多性能差；nftables 统一框架更优；Cilium 用 eBPF 绕过。
- **问题**：kube-proxy 为什么慢？
- **参考答案**：
  - 规则多时 iptables 刷新慢（O(n) 匹配）；nftables 单表多族、性能更好。K8s 早期 iptables，后 ipvs；Cilium 用 eBPF 绕过 iptables。排障：`iptables -t nat -L -n -v`、`nft list ruleset`、`conntrack -L`。
- **易错点**：规则膨胀导致转发延迟上升。
- **延伸**：Q17（conntrack）、kubernetes Q（kube-proxy）

### Q17. conntrack 表满了会怎样？怎么优化？
- **难度**：🔴 高级
- **关键词**：conntrack, 表满, nf_conntrack_max
- **概念速记**：conntrack 跟踪连接状态，表满后新建连接被丢。
- **问题**：随机连接失败但 CPU/内存正常？
- **参考答案**：
  - 日志 `nf_conntrack: table full`；调大 `net.netfilter.nf_conntrack_max`、缩短 `nf_conntrack_tcp_timeout_*`；高并发 L4 可 notrack 或用 DSR；K8s 节点易踩。
- **易错点**：只加内存不调 conntrack_max。
- **延伸**：Q16

### Q18. MTU / MSS 是什么？隧道下分片问题？
- **难度**：🔴 高级
- **关键词**：MTU, MSS, PMTU 黑洞, VXLAN
- **概念速记**：MTU 链路最大帧（1500）；MSS = MTU - IP/TCP 头（约 1460）；隧道加头易超 MTU。
- **问题**：为什么大包不通小包通？
- **参考答案**：
  - 隧道（VXLAN+50、GRE）使内层包超 MTU→分片或丢包（DF 位设了直接丢，PMTU 黑洞）。解决：调小 VM 内 MSS（`iptables TCPMSS`）、或调大底层 MTU（巨帧 9000，需全链路支持）。
- **易错点**：只调 MTU 不调 MSS，TCP 仍按大 MSS 发。
- **延伸**：[basics/02-network-osi.md](../../basics/02-network-osi.md)；Q14

### Q19. 网络延迟（RTT）高，如何分层定位哪段慢？
- **难度**：🟡 中级
- **关键词**：RTT, mtr, tcpdump, 链路追踪
- **概念速记**：RTT 是往返时延；需区分网络延迟 vs 应用延迟 vs 排队延迟。
- **问题**：接口慢是网络还是应用？
- **参考答案**：
  - `ping`/`mtr` 看链路 RTT；`ss -ti` 看重传/RTT；`tcpdump` 看 SYN→SYN-ACK 间隔（服务端处理慢）；应用层看处理耗时（链路追踪）。CDN/就近接入降 RTT。
- **易错点**：把应用慢当成网络慢。
- **延伸**：Q5、observability Q（tracing）

### Q20. BGP / AS 是什么？运维为什么要知道？
- **难度**：⚫ 资深
- **关键词**：BGP, AS, 路由劫持, RPKI
- **概念速记**：BGP 是互联网骨干路由协议；AS 是自治域。
- **问题**：多线接入怎么选路？
- **参考答案**：
  - 多线/多出口选路、Anycast、云上 BGP 宣告、防路由泄露/劫持（RPKI/ROV）。跨运营商故障排查必备。
- **易错点**：忽略 RPKI 导致前缀被劫持。
- **延伸**：Q8、Q13

### Q21. 如何用 tcpdump / Wireshark 定位丢包或重传？
- **难度**：🟡 中级
- **关键词**：tcpdump, Wireshark, 重传, RST
- **概念速记**：抓包看实际报文，定位重传/乱序/连接重置。
- **问题**：怎么确认是网络丢包还是应用？
- **参考答案**：
  - `tcpdump -i eth0 -nn 'tcp[tcpflags] & (tcp-rst|tcp-syn) != 0'`；Wireshark 过滤 `tcp.analysis.retransmission` 看 Dup ACK/Zero Window。`ss -ti` 看重传率；`netstat -s | grep retransmit`；`mtr` 定位链路。
- **易错点**：只在客户端抓，看不到中间链路。
- **延伸**：Q15、Q19

### Q22. QUIC 解决了 TCP 的哪些问题？运维要注意什么？
- **难度**：🔴 高级
- **关键词**：QUIC, HTTP3, UDP, 0-RTT
- **概念速记**：QUIC 基于 UDP，解决 TCP 队头阻塞、连接建立慢、连接迁移。
- **问题**：上 QUIC 为什么要放行 UDP？
- **参考答案**：
  - QUIC 基于 UDP：0/1-RTT 建连、无 TCP HOL、连接迁移（IP 变不断流）。运维：放行 UDP 443；中间设备（老防火墙/NAT）可能不友好；监控需支持 QUIC；nginx/Envoy/Caddy 开启。
- **易错点**：防火墙只开 TCP 443，QUIC 握手失败回退 H2（仍可用但不优）。
- **延伸**：Q5、Q16

### Q23. 经过 LB / 代理后服务端拿不到真实客户端 IP，有哪些解法？PROXY 协议是什么？
- **难度**：🔴 高级
- **关键词**：PROXY protocol, X-Forwarded-For, 源 IP 保持, 四层代理, TLV
- **概念速记**：TCP 连接经过代理中继后，服务端 `getpeername()` 拿到的是**代理的地址**，原始的源地址/端口就丢了。L7 协议可以靠 header 补救（HTTP 用 `X-Forwarded-For` / `Forwarded`），但**四层「哑代理」**（stunnel、HAProxy 的 TCP 模式、云厂商 NLB）不解析上层协议，没法插 header。
- **参考答案**：
  1. **PROXY 协议的思路**：不在每个请求里加东西，而是在**连接建立后、业务数据之前**发送一个一次性的头部，携带 `getsockname()/getpeername()` 级别的信息——地址族（IPv4/IPv6/UNIX）、套接字协议（TCP/UDP）、L3 源/目的地址与 L4 端口。发送方只需在连接后多发一段，接收方只需在连接后多 read 一次，**两侧都不需要理解上层协议**。
  2. **v1 与 v2**：v1 是人类可读的文本（`PROXY TCP4 1.2.3.4 5.6.7.8 1234 80\r\n`，便于调试）；v2 是二进制，效率更高，并支持 **TLV 扩展**（可携带 SSL 信息、ALPN、唯一 ID 等）。
  3. **几种解法对比**：
     | 方案 | 层级 | 代价 |
     |---|---|---|
     | `X-Forwarded-For` / `Forwarded` | L7 | 仅 HTTP；可被伪造，需在可信边界剥离重写 |
     | **PROXY 协议** | L4 | 协议无关、可靠；**两端必须都开启**，否则解析失败 |
     | `externalTrafficPolicy: Local` | L4 | 不需要改协议，但有流量分布不均问题（见 Q24） |
     | IPVS DR / 直接路由 | L2/L3 | 源 IP 天然保留，但组网受限 |
  4. **最大的坑——必须两端同时开**：只在 LB 侧开而后端不认，后端会把 `PROXY TCP4 ...` 当作业务数据，导致协议错乱、连接被重置；反过来只在后端开而 LB 不发，后端会一直等头部直到超时。**切换时必须先加一个新端口/新监听器双跑，验证后再切流**，不能原地改。
  5. **典型落地**：AWS NLB 开启 `proxy_protocol_v2` target group 属性 + Istio Ingress Gateway 上配 `proxy_protocol` listener filter，Envoy 解析后把真实源 IP 填进 `x-forwarded-for` 继续往后传；Nginx 用 `listen 80 proxy_protocol;` + `set_real_ip_from`。
  6. **安全**：接收端必须**只信任来自已知代理 IP 的 PROXY 头部**，否则任何人都能伪造源 IP 绕过基于 IP 的访问控制。
- **易错点**：只改一端导致全站连接失败；健康检查端口没同步开启 PROXY 协议（LB 探测失败，整组下线）；不限制可信来源导致 IP 白名单被绕过。
- **延伸**：Q11、Q24、service-mesh Q18、来源：[Proxy 协议规范（HAProxy）](https://cloudnative.jimmysong.io/blog/proxy-protocol/)

### Q24. Service 的 externalTrafficPolicy: Local 和 Cluster 有什么区别？各自代价是什么？
- **难度**：🔴 高级
- **关键词**：externalTrafficPolicy, SNAT, 源 IP, 负载不均, 健康检查
- **概念速记**：`Cluster`（默认）允许任意节点接收流量后**再转发**到其他节点的 Pod，转发时做 SNAT，源 IP 被改写；`Local` 只把流量交给**本节点上的 Pod**，不转发、不 SNAT，源 IP 得以保留。
- **参考答案**：
  1. **对比**：
     | | `Cluster`（默认） | `Local` |
     |---|---|---|
     | 源 IP | **丢失**（SNAT 成节点 IP） | **保留** |
     | 额外网络跳数 | 可能多一跳 | 无 |
     | 负载均衡 | 均匀（全集群 endpoint） | **按节点**，取决于 Pod 在节点上的分布 |
     | 节点无 Pod 时 | 仍可接收并转发 | **丢弃**（靠健康检查摘除该节点） |
  2. **`Local` 的负载不均问题（最常被忽略）**：云 LB 通常把流量**平均分给各节点**，而不是按 Pod 数量加权。若 A 节点有 1 个 Pod、B 节点有 3 个 Pod，两节点各拿 50% 流量 → A 上那个 Pod 承受的压力是 B 上每个 Pod 的 3 倍。
     - 缓解：用 `topologySpreadConstraints` 让 Pod 在节点间均匀分布；或让 Ingress/Gateway 以 DaemonSet 方式每节点一个。
  3. **`Local` 的健康检查机制**：kube-proxy 在每个节点开一个 `healthCheckNodePort`，没有本地 endpoint 时返回失败，云 LB 据此把该节点摘掉。**如果 LB 没配这个健康检查（或用了 TCP 探活而非 HTTP 探 healthCheckNodePort），流量会被打到没有 Pod 的节点然后黑洞掉。**
  4. **`internalTrafficPolicy`**：K8s 1.26+ GA，是集群**内部**流量的对应开关，设 `Local` 可以让 Pod 只访问本节点的服务实例——适合 DaemonSet 型的日志/指标采集，能省跨节点带宽。
  5. **和源 IP 保持方案的选择**：如果已经用 PROXY 协议（Q23）或 L7 的 XFF 拿到真实 IP，就不必为了源 IP 而用 `Local`，从而避开负载不均。**先想清楚要源 IP 干什么**（限流？审计？地域路由？），不同用途有不同的更优解。
- **易错点**：为了拿源 IP 全局改成 `Local` 却没做 Pod 分布约束，造成热点；LB 健康检查配错导致流量黑洞；以为 `Local` 一定更快（少一跳）而忽视不均衡的代价。
- **延伸**：Q11、Q23、kubernetes Q8、Q9

### Q25. Calico 的数据平面和 BGP 部署模式有哪几种？大规模集群怎么选？
- **难度**：🔴 高级
- **关键词**：Calico, BGP, Full Mesh, Route Reflector, IPIP/VXLAN, eBPF 数据平面
- **概念速记**：Calico 的核心是**纯三层路由**——不做 overlay 时，Pod IP 直接在底层网络上可路由，靠 **BGP** 把「哪个 Pod 网段在哪个节点」这件事通告出去。
- **参考答案**：
  1. **两种数据平面**：
     - **iptables 模式**：成熟稳定、兼容性好、易调试；但规则数随 Service/Pod 增长，大规模下匹配开销和更新延迟明显。
     - **eBPF 模式**：内核态处理，绕开 iptables/conntrack 链，延迟更低吞吐更高，并且**原生保留源 IP**（不需要 `externalTrafficPolicy: Local` 那套权衡，见 Q24），还能替代 kube-proxy。代价是对内核版本有要求、排障工具链不同。
  2. **三种 BGP 拓扑**：
     - **Full Mesh**：所有节点两两建立 BGP 邻居。简单，但会话数是 O(N²)，**一般只适合 ~100 节点以内**。
     - **Route Reflector（RR）**：选少数节点作反射器，其他节点只与 RR 建邻居，会话数降到 O(N)。**中大规模的标准解法**，RR 要做冗余（至少 2 个）。
     - **AS Per Rack**：每个机架一个自治域，与 ToR 交换机做 eBGP。最贴近数据中心网络架构，适合和网络团队协同的自建 IDC。
  3. **要不要 overlay**：底层网络不允许 Pod 网段路由（典型是公有云 VPC 不认你的 Pod CIDR）时，用 **IPIP 或 VXLAN 封装**；同子网内可开 `CrossSubnet` 模式——同子网直接路由、跨子网才封装，兼顾性能与可达性。封装会带来 MTU 开销（见 Q18）和一定 CPU 成本。
  4. **策略能力**（相比原生 NetworkPolicy 的扩展）：GlobalNetworkPolicy（跨 namespace）、HostEndpoint（保护宿主机网卡本身，这点很多方案没有）、基于 Service 的策略、有限的 L7 策略。
  5. **选型口径**：已有 BGP 能力的自建 IDC + 要求扁平网络 → Calico BGP；公有云托管集群 → 通常直接用云厂商 CNI（VPC 原生 IP）；要强 L7 可观测与 eBPF 能力 → Cilium（见 Q26）。
- **易错点**：几百节点还用 Full Mesh；RR 只部署一个成为单点；开了 IPIP 却没调 MTU 导致大包丢失；以为 Calico 一定不用 overlay。
- **延伸**：Q18、Q20、Q26、kubernetes Q14、来源：[Kubernetes Handbook - Calico](https://jimmysong.io/book/kubernetes-handbook/networking-calico/)

### Q26. Cilium 凭什么能替代 kube-proxy？「身份驱动的安全模型」是什么意思？
- **难度**：🔴 高级
- **关键词**：eBPF, kube-proxy replacement, identity, Hubble, Native Routing
- **概念速记**：Cilium 用 **eBPF** 把网络逻辑挂在内核的 socket/网卡钩子上，绕开 iptables 那条越来越长的规则链；同时不按 IP 做策略，而是给每组标签相同的工作负载分配一个**数字身份（identity）**，策略在身份之间表达。
- **参考答案**：
  1. **替代 kube-proxy 的原理**：kube-proxy 的 iptables 模式为每个 Service 生成一串规则，匹配是**线性**的，几千个 Service 时规则数上万，更新一次要重写整张表 → 延迟高、CPU 抖动。Cilium 把 Service→Endpoint 的映射放进 **eBPF map（哈希查找，O(1)）**，并在 **socket 层**就完成地址转换（`connect()` 时直接改写目的地址），**连接根本不经过 conntrack 和 NAT**。
  2. **身份驱动为什么重要**：K8s 里 Pod IP 是易变的，基于 IP 的规则必须随 Pod 重建不断更新。Cilium 把「带 `app=frontend` 标签的一组 Pod」映射成一个 identity，策略写成「identity A 可以访问 identity B 的 80 端口」——**Pod 重建、扩缩容都不需要改数据面规则**，只在身份变化时更新。这也让策略在**跨集群**时仍然成立（identity 可以跨集群同步）。
  3. **网络模式**：
     - **Overlay（VXLAN/Geneve）**：对底层网络零要求，开箱即用，有封装开销。
     - **Native Routing**：Pod IP 直接由底层网络路由（配合 BGP 或云厂商 ENI），性能最好。
  4. **Hubble 的价值**：eBPF 天然在数据路径上，所以能**零侵入**地导出每一条流的元数据——`hubble observe --verdict DROPPED` 直接告诉你「哪条策略挡了谁」，这是 iptables 方案很难做到的（见 observability Q21）。
  5. **代价与前提**：对内核版本有要求（建议 5.10+，部分特性更高）；排障需要新的工具链（`cilium monitor`、`bpftool`），团队学习成本不低；L7 策略仍需拉起 Envoy（见 service-mesh Q24）。
- **易错点**：以为 eBPF 能做所有事（L7 复杂处理仍需代理）；内核版本不满足就开高级特性；迁移掉 kube-proxy 时没清理残留的 iptables 规则。
- **延伸**：Q25、kubernetes Q14、Q34、service-mesh Q24、observability Q21、来源：[Kubernetes Handbook - Cilium](https://jimmysong.io/book/kubernetes-handbook/networking-cilium/)

### Q27. 怎么把 K8s 的 LoadBalancer Service 暴露到自建机房内网？BGP 方案是怎么工作的？
- **难度**：🔴 高级
- **关键词**：MetalLB, Cilium BGP, L2 模式, ECMP, VIP 通告
- **概念速记**：`type: LoadBalancer` 在公有云由云厂商 controller 创建真实 LB；自建机房没有这个东西，Service 会永远停在 `<pending>`。解法是让集群**自己把 VIP 通告给网络设备**。
- **参考答案**：
  1. **两种模式**：
     - **L2 / ARP 模式**（MetalLB Layer2）：由集群中的**一个**节点应答该 VIP 的 ARP，流量全部先到这个节点再转发。实现简单、不需要网络设备配合，但**该节点是带宽瓶颈和故障点**，切换靠重新发 ARP（有秒级中断）。
     - **BGP 模式**（MetalLB BGP / Cilium BGP Control Plane）：多个节点用 BGP 向 ToR 交换机通告同一个 VIP，交换机用 **ECMP** 把流量哈希到多个节点 → **真正的多活 + 水平扩展带宽**。
  2. **BGP 模式的细节**：
     - 需要网络团队配合分配 AS 号、开放 BGP 邻居、确认交换机支持 ECMP。
     - **ECMP 重哈希问题**：节点增删会导致哈希桶变化，部分已建立的连接被打到新节点而被 reset。缓解：交换机用 **resilient hashing / consistent hashing**；应用侧做好重连。
     - 通常配合 `externalTrafficPolicy: Local`（见 Q24）——只有真正有 Pod 的节点才通告该 VIP，天然把没有后端的节点排除。
  3. **Cilium BGP 的额外能力**：不仅能通告 LoadBalancer 的 VIP，还能直接通告 **Pod CIDR**，实现 Native Routing（见 Q26），一套 BGP 同时解决「Pod 可达」和「服务暴露」两件事，少一层封装。
  4. **VIP 池管理**：用 `IPAddressPool`/`CiliumLoadBalancerIPPool` 声明可分配的地址段，按 namespace/标签做分配策略，避免团队之间抢地址。
  5. **验证**：交换机上 `show ip bgp` 看是否收到路由且下一跳是多个节点；节点上 `cilium bgp routes` / `metallb` 的 speaker 日志。
- **易错点**：用 L2 模式却期待带宽线性扩展；BGP 邻居没做冗余；VIP 段和现网地址冲突；忘了配 `externalTrafficPolicy` 导致没有后端的节点也通告 VIP。
- **延伸**：Q20、Q24、Q26、kubernetes Q10
