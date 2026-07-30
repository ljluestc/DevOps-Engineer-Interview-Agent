# 网络面试题（22 题）

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
