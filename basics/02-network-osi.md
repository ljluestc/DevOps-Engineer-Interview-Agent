# 02 · 网络与 OSI 七层深度篇

> 关键词：OSI 七层、TCP/IP、封装、MAC/IP、TCP 三次握手、DNS、HTTP、负载均衡

---

## 1. 为什么要有 OSI 模型

OSI（Open Systems Interconnection）是 **ISO 制定的网络通信概念模型**，把复杂的网络通信拆成 7 层，每层只管自己的事、只与相邻层交互。价值：**解耦**、**标准化**、**便于排障**（哪层出问题就查哪层）。

> 注意：OSI 是「理论模型」，现实中互联网实际用的是 **TCP/IP 四层/五层模型**。面试常考「OSI vs TCP/IP 区别」。

---

## 2. OSI 七层逐层拆解

| 层 | 名称 | 数据单位 | 核心职责 | 典型协议/设备 | 运维关注点 |
|---|---|---|---|---|---|
| 7 | 应用层（Application） | 报文 | 为用户程序提供网络服务 | HTTP/HTTPS、DNS、FTP、SSH、SMTP | 证书、域名、状态码、TLS 版本 |
| 6 | 表示层（Presentation） | 数据 | 数据格式/加密/压缩 | TLS、JPEG、gzip | 加密套件、压缩 |
| 5 | 会话层（Session） | 数据 | 会话建立/维持/断开 | RPC、NetBIOS | 长连接、会话保持 |
| 4 | 传输层（Transport） | 段（Segment） | 端到端可靠/不可靠传输、端口 | TCP、UDP | 握手、重传、拥塞、端口、连接数 |
| 3 | 网络层（Network） | 包（Packet） | 路由、寻址、跨网段转发 | IP、ICMP、BGP、OSPF | 路由、MTU、ICMP、丢包 |
| 2 | 数据链路层（Data Link） | 帧（Frame） | 相邻节点可靠传输、MAC 寻址 | Ethernet、VLAN、ARP、PPP | MAC、ARP、交换机、MTU |
| 1 | 物理层（Physical） | 比特（Bit） | 电信号/光信号传输 | 双绞线、光纤、RJ45 | 网线、速率、双工、光衰 |

> 记忆口诀：**应表会传网数物**（应用、表示、会话、传输、网络、数据链路、物理）。

---

## 3. TCP/IP 模型与 OSI 的映射

| TCP/IP 五层 | 对应 OSI |
|---|---|
| 应用层 | 应用 + 表示 + 会话（5–7） |
| 传输层 | 传输层（4） |
| 网络层 | 网络层（3） |
| 网络接口层 | 数据链路 + 物理（1–2） |

差异：OSI 先有模型后实现；TCP/IP 先有协议后抽象；OSI 严格分层，TCP/IP 更实用（把上三层合并）。

---

## 4. 封装（Encapsulation）流程

数据从应用层往下，每层加自己的头：

```
应用数据
→ [TCP头 | 数据]            (传输层)
→ [IP头 | TCP头 | 数据]      (网络层)
→ [MAC头 | IP头 | ... | FCS] (链路层)
```

接收方逆向解封装。每层只认自己的头——这就是为什么「TCP 端口」在传输层、「IP」在网络层、「MAC」在链路层。

---

## 5. 传输层重点：TCP vs UDP

| 维度 | TCP | UDP |
|---|---|---|
| 连接 | 面向连接（三次握手） | 无连接 |
| 可靠 | 确认/重传/排序 | 不保证 |
| 速度 | 慢（开销大） | 快 |
| 场景 | HTTP、DB、SSH | DNS、视频、游戏、QUIC |

**TCP 三次握手**：SYN → SYN+ACK → ACK（确认双方收发能力）。
**四次挥手**：FIN → ACK → FIN → ACK（全双工，各自关闭）。

**TIME_WAIT（2MSL）**：确保最后 ACK 到达 + 让旧报文消亡。过多治理见 `modules/network`。

---

## 6. 网络层重点：IP / ARP / ICMP / MTU

- **IP**：无连接、尽力交付，负责寻址与路由。IPv4/IPv6。
- **ARP**：IP → MAC 的解析（同网段）。`arp -n` 查看缓存。
- **ICMP**：诊断（ping、traceroute、`type/code`）。常被防火墙禁，导致 ping 不通但服务可达。
- **MTU**：链路最大帧（以太网 1500）。**PMTU 黑洞**是经典坑：隧道（VXLAN/GRE）加头后超 MTU，DF 位设了直接丢包 → 大包不通、小包通。解决：调小 MSS 或开巨帧（9000，需全链路支持）。

---

## 7. 应用层重点：DNS / HTTP

- **DNS**：域名 → IP。递归（Local DNS 替你问）vs 迭代（每级返回下一跳）。记录：A/AAAA、CNAME、MX、TXT、PTR、NS、SOA。排查 `dig +trace`。
- **HTTP**：1.1（管线化、队头阻塞）、2（多路复用、HPACK）、3（QUIC/UDP，0-RTT）。HTTPS = HTTP + TLS（握手、证书链、1.2 vs 1.3）。
- **负载均衡**：L4（IP+端口，快）vs L7（HTTP 头/路径，智能）。LVS（NAT/DR/TUN）、Nginx/HAProxy、云 ALB/NLB。

---

## 8. 排障分层法（面试必考）

```
应用层：服务是否健康？证书/域名对？
传输层：端口通？连接数满？重传率？
网络层：路由/ICMP 通？MTU？丢包？
链路层：MAC/ARP？交换机？网线/光衰？
物理层：网卡/速率/双工？
```
工具链：`ping`/`mtr`（网络层）、`telnet`/`nc`（传输层）、`tcpdump`/`ss`（全栈）、`traceroute`。

---

## 9. 常见误区

- ❌ 「OSI 是互联网实际使用的模型」 → 实际是 TCP/IP。
- ❌ 「MAC 地址全球路由」 → MAC 只在二层（同广播域）有效，跨网段靠 IP。
- ❌ 「ping 不通 = 服务挂了」 → 可能只是 ICMP 被禁。
- ❌ 「TCP 保证不丢包」 → TCP 只在**传输过程**内重传保证可靠，应用层仍可能丢（如未 commit）。

---

## 延伸

- 面试题：见 `modules/network/network-questions.md`
- 推荐：TCP/IP 详解 卷1；Cloudflare 的 TCP/HTTP 科普博客
