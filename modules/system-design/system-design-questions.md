# 系统设计面试题（35 题）

> 遵循 [../../docs/STANDARD.md](../../docs/STANDARD.md) 模板。难度：🟢 初级 · 🟡 中级 · 🔴 高级。
> **主题解析**：候选人说的名字（品牌名 / 中文 / 错别字 / 同题多拼法）先查 [system-design-resolver.md](system-design-resolver.md)（181 条别名 · 82 组重复主题 · 2 个真薄主题 + 21 个非标准编号主题），再查 [system-design-catalog.md](system-design-catalog.md)；都不中时用本文件 Q1–Q4 的方法论开面，并明确说明语料里没有该主题。
> **AWS-only 渲染补充**：[collections/aws-managed-services-only.md](../../collections/aws-managed-services-only.md) 第 131–195 题——把 11 个经典题（短链 / IM / 票务 / 定时任务 / 通知 / 爬虫 / 信息流 / 直播 / 文件存储 / 分布式缓存 / Web 分析）逐行翻成 AWS 托管服务，考「通用设计里哪些组件消失了、剩下的那部分才是要设计的东西」。适合在候选人画完通用架构后追问。
> 本模块是 `switch system-design` 的**主题库与评分口径**；具体主题的深度素材来自
> [`system-design/`](../../system-design/) 子模块（<https://github.com/ljluestc/system-design>，600+ 主题），
> 全量主题目录见 [system-design-catalog.md](system-design-catalog.md)（自动生成）。
>
> 面向运维 / SRE / DevOps 候选人的系统设计面试，与纯后端面试的区别在于**更看重可运维性**：
> 容量与 SLO、失败模式与降级、发布与回滚、观测与告警、成本。每题的参考答案都按这个口径展开。

---

## 系统设计面试怎么进行（面试官执行手册）

1. **选题**：按候选人级别与岗位从本文件抽题；候选人点名主题（如「设计一个监控系统」）时，
   到 [system-design-catalog.md](system-design-catalog.md) 按目录名 / 标题定位到 `system-design/<topic>/`。
2. **备课**：出题前读该主题的 `00-index.md`（题面）、`01-requirements.md`（FR/NFR/规模）、
   `05-trade-offs.md`；追问从 `06-quiz.md`（有折叠答案）与 `20-interview-drills.md`（速答表 + 常见陷阱）取。
3. **推进节奏（45–60 分钟）**：
   - 0–5 min 需求澄清：功能 / 非功能 / 规模 / 明确不做什么；
   - 5–10 min 估算：QPS、存储、带宽、峰值系数；
   - 10–25 min 高层设计：5–7 个组件 + 数据流；
   - 25–45 min 深入 2–3 个关键组件：数据模型、扩展、失败处理；
   - 45–55 min 权衡与运维：一致性 vs 可用性、成本、SLO、发布、观测；
   - 最后 5 min 候选人补充 + 反馈。
4. **一次只推进一个环节**，候选人卡壳时给 `hint`（提示方向，不给答案）。
5. **不要让候选人「背架构」**：每个组件都追问「为什么是它」「它挂了怎么办」「怎么知道它挂了」。

## 系统设计评分维度（每题 1–10 分按此打）

| 维度 | 权重 | 看什么 |
|---|---|---|
| 需求澄清与估算 | 15% | 主动问规模 / 一致性 / 延迟目标；估算数量级正确、能推导瓶颈 |
| 高层设计 | 20% | 组件职责清晰、数据流完整、没有明显单点 |
| 深入与数据模型 | 25% | 关键组件讲得出内部机制（分区、复制、索引、协议） |
| 权衡与替代方案 | 20% | 每个决策都能说「代价是什么、什么时候选另一种」 |
| 可运维性（SRE 视角） | 20% | 失败模式与降级、发布回滚、SLI/SLO 与告警、容量与成本 |

9–10：五个维度全部到位且有实战细节 · 7–8：主干正确、一两个维度浅 · 5–6：能画出架构但说不清为什么 · 3–4：组件堆砌、无估算无权衡 · 1–2：无法给出可用设计。

---

## 一、方法论与基础

### Q1. 系统设计面试的标准流程是什么？45 分钟你怎么分配？

- **难度**：🟢 初级
- **关键词**：需求澄清 requirements, 估算 back-of-envelope, 高层设计 HLD, 深入 deep dive, 权衡 trade-off
- **概念速记**：
  - **FR / NFR**：功能需求（系统做什么）与非功能需求（延迟、可用性、一致性、规模、成本）。面试里 NFR 决定架构，FR 只决定 API。
  - **HLD（High-Level Design）**：5–7 个组件的框图 + 主要数据流；不是画得越多越好，而是每个框都能解释「为什么需要」。
  - **深入（Deep dive）**：挑 2–3 个最关键 / 最有风险的组件展开到数据模型、分区、复制、失败处理。
- **问题**：面试官说「设计一个 X」，你第一句话说什么？45 分钟怎么分配？什么情况下算「跑偏」？
- **参考答案**：
  1. **第一句永远是澄清而不是画图**：用户是谁、核心场景是哪 2–3 个、规模（DAU / QPS / 数据量）、延迟与一致性要求、明确「不做什么」。把假设写在白板角落，后面所有决策都能追溯到它。
  2. **时间分配**：澄清 5 min → 估算 5 min → 高层设计 10–15 min → 深入 2–3 个组件 15–20 min → 权衡 / 失败模式 / 运维 5–10 min → 留 3 min 总结。
  3. **估算要「推导出瓶颈」而不是背数字**：例如 1 亿 DAU × 10 请求 / 天 ≈ 12K QPS 平均、峰值 ×3–5；由此判断单机能扛还是必须分片。
  4. **高层设计只放会被追问的组件**：客户端 → 网关 / LB → 服务 → 存储 / 缓存 / 队列；每个框说一句「职责」和一句「为什么不放在别处」。
  5. **深入时主动选**：说「我建议深入 A 和 B，因为 A 是写热点、B 是一致性难点」，把主动权拿回来。
  6. **收尾讲运维**：单点在哪、挂了怎么降级、怎么发布、看什么指标、成本大头是什么——这是 SRE 岗位的加分区。
  7. **跑偏信号**：10 分钟还在纠结 API 字段；上来就选具体产品（「用 Kafka」）而说不出为什么；画了 15 个框但没有一条完整数据流。
- **易错点 / 面试官关注**：
  - 不问规模就开始设计，导致方案与规模不匹配（给 1K QPS 上分片）。
  - 把「组件名」当「设计」：说「加个缓存」但说不出缓存什么、失效策略、命中率目标。
  - 全程没有数字：没有估算、没有 SLO、没有容量。
- **延伸**：Q2、Q4、[system-design/interview-quick-reference.md](../../system-design/interview-quick-reference.md)、[system-design/end-to-end/](../../system-design/end-to-end/)、[system-design/system-design-interview/07-walkthrough.md](../../system-design/system-design-interview/07-walkthrough.md)

---

### Q2. 做一次 back-of-envelope 估算：1 亿 DAU 的图片社交应用需要多少 QPS、存储和带宽？

- **难度**：🟡 中级
- **关键词**：估算 estimation, QPS, 峰值系数 peak factor, 存储增长, 延迟数字 latency numbers
- **概念速记**：
  - **Back-of-envelope**：用 2–3 个假设 + 乘法得到数量级（不是精确值），目的是判断「单机 / 单库能不能扛」「瓶颈在读还是写」。
  - **经典延迟数字**：内存访问 ~100ns、SSD 随机读 ~100µs、同机房 RTT ~0.5ms、跨洲 RTT ~100ms+、机械盘寻道 ~10ms。估算时用这些判断「能不能放内存」「要不要就近部署」。
- **问题**：1 亿 DAU，每人每天浏览 20 张图、上传 2 张，图片平均 500KB，保存 5 年。请估算读写 QPS、峰值、每日新增存储、5 年总存储、出入带宽，并指出瓶颈在哪。
- **参考答案**：
  1. **写 QPS**：1e8 × 2 / 86400 ≈ 2.3K/s 平均；峰值按 ×5 ≈ 12K/s。元数据写入量小，图片本体走对象存储。
  2. **读 QPS**：1e8 × 20 / 86400 ≈ 23K/s 平均，峰值 ≈ 100K+/s；读写比 10:1，**读多写少 → 缓存 + CDN 是主战场**。
  3. **存储**：每日 2e8 张 × 500KB = 100TB/天；5 年 ≈ 100TB × 365 × 5 ≈ **180PB**（未含副本与缩略图）。三副本或 EC 后 ×1.5–3。结论：必须是对象存储 + 分层（热 / 冷）+ 生命周期策略。
  4. **带宽**：入口 2.3K × 500KB ≈ 1.2GB/s；出口 23K × 500KB ≈ 11.5GB/s，峰值 50GB/s+ → **必须 CDN**，源站只承受 miss 流量（命中率 90% 时源站出口 ≈ 1–5GB/s）。
  5. **元数据规模**：2e8 行 / 天，5 年 3.6e11 行，单表不可能 → 按用户或时间分片；索引热点在「最近」。
  6. **结论性判断**（面试官真正要的）：瓶颈依次是出口带宽（CDN 解决）→ 元数据读（缓存 + 读副本）→ 存储成本（分层 + EC + 压缩）；写路径不是瓶颈但要保证上传可靠（分片 / 断点续传）。
- **易错点 / 面试官关注**：
  - 算出数字不做结论：估算的价值是「因此要 X」。
  - 忘记峰值系数与副本系数。
  - 单位混乱（bit / byte、GB / GiB）——面试中说清取整口径即可。
- **延伸**：Q1、Q11、[system-design/back-of-envelope/](../../system-design/back-of-envelope/)、[system-design/interview-quick-reference.md](../../system-design/interview-quick-reference.md)

---

### Q3. CAP 在真实系统里到底怎么用？请讲清一致性模型的谱系与 PACELC。

- **难度**：🟡 中级
- **关键词**：CAP, PACELC, 线性一致 linearizability, 顺序一致, 因果一致, 最终一致 eventual consistency, 读己之写
- **概念速记**：
  - **CAP**：网络分区（P）发生时，只能在一致性（C，线性一致）和可用性（A，每个请求都得到非错误响应）二选一。**分区是常态不是选项**，所以 CAP 实际是「分区时选 C 还是 A」。
  - **PACELC**：补充「没有分区（E）时，选延迟（L）还是一致性（C）」——多数系统即使正常运行也在用一致性换延迟。
  - **一致性谱系**（强 → 弱）：线性一致（单副本错觉）> 顺序一致 > 因果一致 > 读己之写 / 单调读 > 最终一致。
- **问题**：「Kafka / ZooKeeper / Cassandra / DynamoDB 分别是 CP 还是 AP？」这个问题为什么不准确？你怎么向面试官解释自己在设计中选了哪种一致性？
- **参考答案**：
  1. **CAP 是每个操作 / 每份数据的属性，不是系统标签**：Cassandra 用 `QUORUM` 读写可接近强一致、`ONE` 则是 AP；DynamoDB 有强一致读与最终一致读两种 API；ZooKeeper 写是 CP、读默认可能读到旧值（除非 `sync`）。
  2. **正确的表述方式**：「订单状态这类数据我用 CP（多数派写、leader 读），代价是分区时少数派不可写；用户的 feed 缓存用 AP + 最终一致，代价是几秒内可能看不到自己刚发的帖子——我用读己之写（session 粘性或写后读主）掩盖这个体验问题。」
  3. **PACELC 才是日常**：跨地域部署时，同步复制换来强一致但每次写多 100ms+ RTT；异步复制延迟低但会丢最近的写——这就是 E 情况下的 L vs C。
  4. **落地手段**：quorum（W + R > N）、leader 租约、fencing token、版本向量 / 逻辑时钟解决冲突；业务层用幂等 + 补偿代替分布式事务。
  5. **面试加分**：指出「线性一致 ≠ 事务隔离级别」（前者是单对象多副本的，后者是多对象单副本的），以及「最终一致要说清『最终』多久、冲突怎么解」。
- **易错点 / 面试官关注**：
  - 把 CAP 当三选二，或说「我们选 CA」。
  - 说不清自己系统里哪份数据用什么一致性、代价是什么。
  - 不知道 quorum 只保证「读到最新写」不保证「多客户端的顺序一致」。
- **延伸**：Q6、Q9、Q21、[system-design/consistency-models-guide/](../../system-design/consistency-models-guide/)、[system-design/consistency-models-spectrum/](../../system-design/consistency-models-spectrum/)、[system-design/distributed-systems-tradeoffs/](../../system-design/distributed-systems-tradeoffs/)

---

### Q4. 一个单体 Web 应用从 0 到百万用户，架构会经历哪些演进？每一步的触发条件是什么？

- **难度**：🔴 高级
- **关键词**：单体 monolith, 读写分离, 缓存, 无状态 stateless, 分片 sharding, 消息队列, 多活 multi-region
- **概念速记**：
  - **无状态化**：会话状态移出应用进程（放 Redis / 签名 Cookie），应用实例才能随意加减与滚动发布。
  - **分片（Sharding）**：按 key 把数据水平切到多个库；代价是跨分片事务 / join 变难、需要路由层与再平衡。
  - **触发条件**：每一步演进都应由**可观测到的瓶颈**触发（CPU / 连接数 / 慢查询 / p99），而不是「大厂都这么做」。
- **问题**：请按阶段描述演进路径，每一步说清「看到什么指标才做」「做完解决了什么、引入了什么新问题」。
- **参考答案**：
  1. **单机 → 应用与数据库分离**：触发：CPU / 内存互相争抢、无法独立扩容。得到：各自扩容；引入：网络一跳、连接池管理。
  2. **多实例 + 负载均衡 + 无状态**：触发：单实例 CPU 饱和、发布要停机。前置：会话外置。引入：LB 成为入口单点（用双活 / 云 LB）、需要健康检查与优雅下线。
  3. **数据库读写分离 + 缓存**：触发：慢查询、读 QPS 占 90%。得到：读扩展；引入：复制延迟（读己之写问题）、缓存一致性（更新策略、雪崩 / 穿透，见 Q7）。
  4. **CDN + 对象存储**：触发：出口带宽与静态资源占比高。引入：缓存失效策略、回源保护。
  5. **异步化 / 消息队列**：触发：写路径里有慢的第三方调用（邮件、通知、风控）拖长 p99。得到：削峰、解耦；引入：至少一次投递 → 消费者必须幂等；积压监控。
  6. **服务拆分（按业务边界，不是按技术层）**：触发：团队规模与发布冲突、不同模块扩容比例差异大。引入：分布式调用链、服务发现、超时 / 重试 / 熔断、跨服务一致性（Saga / outbox）。
  7. **数据库分片**：触发：单库写入或存储到顶（垂直扩容到头）。选分片键（用户 ID / 时间）、路由层、再平衡方案（一致性哈希 / 目录服务）；跨片查询走异步物化视图或搜索引擎。
  8. **多机房 / 多活**：触发：可用性目标 ≥ 99.99% 或合规就近。引入：数据主权、冲突解决、流量调度、全局唯一 ID（Q8）。
  9. **贯穿全程的运维面**：每一步都要同步补齐：指标 / 日志 / 链路、SLO 与告警、容量规划、发布回滚、故障演练；否则「演进」只是把故障面做大。
- **易错点 / 面试官关注**：
  - 跳步（1K QPS 就上微服务 + 分片）；说不出每一步的触发指标。
  - 只讲收益不讲新引入的问题（复制延迟、幂等、分布式事务）。
  - 认为「微服务 = 可扩展」；扩展性来自无状态 + 数据分片，不来自拆服务。
- **延伸**：Q7、Q10、Q28、[system-design/scale-from-zero-to-millions/](../../system-design/scale-from-zero-to-millions/)、[system-design/three-tier-architecture/](../../system-design/three-tier-architecture/)、[sre-reliability/sre-questions.md](../sre-reliability/sre-questions.md)

---

## 二、基础构件（Building Blocks）

### Q5. 设计一个分布式限流器（Rate Limiter）：算法怎么选、放在哪一层、Redis 挂了怎么办？

- **难度**：🟡 中级
- **关键词**：令牌桶 token bucket, 滑动窗口 sliding window, 固定窗口, Lua 原子性, fail-open / fail-closed, 429
- **概念速记**：
  - **固定窗口**：每个时间窗一个计数器，简单但窗口边界可放过 2× 流量。
  - **滑动窗口日志**：记录每个请求时间戳，精确但内存 O(请求数)。
  - **滑动窗口计数**：用当前窗与上一窗加权近似，内存 O(1)，精度够用。
  - **令牌桶**：以固定速率补充令牌、桶容量即允许的突发；只需存「令牌数 + 上次补充时间」两个值，Stripe 等生产系统的常见选择。
- **问题**：为一个 1M QPS 的 API 平台设计限流：算法、部署位置、数据结构、原子性、分片、多机房、故障策略。
- **参考答案**：
  1. **位置**：放在 API 网关（集中、被拒请求不进后端、一个地方管规则）而不是每个服务进程内——进程内限流每实例只看到 1/N 流量，总放行量是 N 倍。业务相关的分级（付费用户 10× 配额）把 tier 编进 JWT 让网关能读。
  2. **算法**：令牌桶。理由：内存 O(1)、天然支持突发、补充速率即稳态限制；固定窗口边界问题、滑动日志内存太大。
  3. **状态存储**：Redis，key = `hash(rule, client_id)`，值是 `{tokens, last_refill_ts}`；**整个「读 → 按时间补令牌 → 扣减 → 写回」放在一个 Lua 脚本里原子执行**，比 MULTI/EXEC 强（后者读在事务外，有 TOCTOU 竞争）。
  4. **规模**：单 Redis ~100K ops/s，1M QPS 用 Redis Cluster 10+ 分片；按 client 哈希到槽位，同一 client 的请求落同一分片；每分片主从。热 key（某个超大客户）用本地令牌桶预扣 + 周期性同步兜底。
  5. **多机房**：默认「每区域独立桶」（各自 1/N 配额或全量配额），接受跨区域的短时超限；真正要全局精确的场景才用中心化 Redis 承担跨区 RTT。
  6. **故障策略**：Redis 不可用时——社交 / 金融类默认 **fail-closed**（返回 429），因为限流器故障往往与流量洪峰同时发生，fail-open 会把洪峰全放进后端引发级联；低风险 API 可 fail-open。同时网关本地兜底一个粗粒度令牌桶。
  7. **响应契约**：429 + `RateLimit-Limit / Remaining / Reset` + `Retry-After` 头；规则存 DB，通过配置推送到网关本地缓存，热更新不重启。
  8. **可观测**：p99 延迟（Lua 应在亚毫秒）、拒绝率按规则 / 客户分布、Redis 分片健康、规则命中 top-N。
- **易错点 / 面试官关注**：
  - 用客户端时钟做补充计算（时钟漂移）；应用 Redis `TIME` 或服务端时间。
  - 忽略多实例协调问题；忽略热 key。
  - 没有明确说 fail-open 还是 fail-closed，以及为什么。
- **延伸**：Q12、[system-design/rate-limiter/06-quiz.md](../../system-design/rate-limiter/06-quiz.md)、[system-design/rate-limiter/20-interview-drills.md](../../system-design/rate-limiter/20-interview-drills.md)、[system-design/rate-limiter-production/](../../system-design/rate-limiter-production/)

---

### Q6. 设计一个分布式键值存储（Dynamo / Cassandra 风格）：分区、复制、一致性与存储引擎

- **难度**：🟡 中级
- **关键词**：一致性哈希 consistent hashing, 虚拟节点, 复制因子 N, quorum W/R, 提示移交 hinted handoff, 读修复, LSM-tree, 反熵 Merkle tree
- **概念速记**：
  - **一致性哈希**：把节点与 key 都哈希到同一个环上，key 归顺时针第一个节点；加减节点只影响相邻一段数据。**虚拟节点**让每台物理机在环上占多个位置，解决负载不均与异构机器问题。
  - **Quorum**：N 副本中写成功 W 个、读 R 个；W + R > N 时读一定能碰到最新写（不保证顺序一致）。
  - **LSM-tree**：写先进内存 MemTable + WAL，刷成不可变 SSTable，后台 compaction 合并；写快、读需查多层（用 Bloom filter 加速）。
- **问题**：设计一个支持 PB 级、可水平扩展、高可用的 KV 存储：数据怎么分布、怎么复制、读写路径、节点故障 / 加入怎么处理、存储引擎选什么。
- **参考答案**：
  1. **分区**：一致性哈希 + 虚拟节点（每物理节点 100–256 个）；元数据（环状态）用 gossip 传播或放协调服务（etcd / ZK）。
  2. **复制**：key 的 N 个副本放环上顺时针 N 个**不同物理节点 / 机架 / 可用区**（rack-aware）。
  3. **写路径**：协调节点把写发给 N 个副本，W 个 ACK 即返回；副本本地写 WAL → MemTable。故障副本用 **hinted handoff**：暂存到其他节点，恢复后回放。
  4. **读路径**：向 R 个副本读，用版本（向量时钟 / 时间戳）挑最新，发现旧副本做 **read repair**；后台用 **Merkle tree** 做反熵对账修复长期不一致。
  5. **一致性档位**：W=R=QUORUM 接近强一致；W=1,R=1 高可用低延迟；由调用方按 key 级别选（订单 quorum、计数器 ONE）。
  6. **冲突**：多主写用向量时钟 + 应用层合并（或 LWW，承认可能丢写）；要真正的单对象线性一致就用 leader-based（Raft）分片。
  7. **存储引擎**：LSM（写多）；范围查询多、读放大敏感则 B-tree。SSTable 配 Bloom filter + 块索引；compaction 策略（size-tiered vs leveled）影响写放大 / 空间放大。
  8. **扩缩容**：新节点接管一段环，从原持有者流式复制数据；限速避免影响线上；再平衡期间读写路由到新旧两处。
  9. **运维面**：监控 p99 读写、compaction 积压、每节点 token 数均衡、hinted handoff 队列、修复进度；容量上按 `数据量 × N / 单节点安全水位（≤ 60–70%）` 算节点数。
- **易错点 / 面试官关注**：
  - 只说「哈希取模」——扩容时几乎全部数据要迁移。
  - 认为 quorum = 强一致 / 事务。
  - 说不出 hinted handoff、read repair、反熵三者分别解决什么时间尺度的不一致。
- **延伸**：Q3、Q7、Q14、[system-design/key-value-store/](../../system-design/key-value-store/)、[system-design/cassandra/](../../system-design/cassandra/)、[system-design/dynamodb/](../../system-design/dynamodb/)、[middleware/middleware-questions.md](../middleware/middleware-questions.md)

---

### Q7. 设计一个分布式缓存：缓存策略、一致性、雪崩 / 穿透 / 击穿、热 key

- **难度**：🟡 中级
- **关键词**：cache-aside, write-through / write-back, TTL, 雪崩 avalanche, 穿透 penetration, 击穿 breakdown, 热 key, LRU/LFU
- **概念速记**：
  - **Cache-aside**：应用先读缓存、miss 读库再回填；写时**先更新库再删缓存**（不是更新缓存），避免并发写导致脏数据。
  - **Write-through / write-back**：写经过缓存同步 / 异步落库；write-back 快但缓存挂了会丢数据。
  - **雪崩 / 穿透 / 击穿**：大量 key 同时过期或缓存整体宕机 / 查询不存在的 key 每次都打库 / 单个热 key 过期瞬间大量并发打库。
- **问题**：为一个读多写少的商品详情页设计缓存层：拓扑、读写策略、一致性保证、三大经典故障怎么防、热 key 怎么处理、容量与淘汰怎么定。
- **参考答案**：
  1. **拓扑**：客户端一致性哈希（或代理 / Redis Cluster）分片，每片主从；多级缓存：进程内（Caffeine / guava，毫秒级 TTL 抗热 key）→ 分布式 Redis → DB。
  2. **策略**：cache-aside + **先写库后删缓存** + 延迟双删 / 订阅 binlog（Canal / Debezium）异步失效兜底极端并发；强一致场景不该用缓存或用 lease（读时先拿 lease token，写时使其失效）。
  3. **雪崩**：TTL 加随机抖动；缓存集群多副本 + 分片隔离；DB 前置限流 / 熔断；预热。
  4. **穿透**：不存在的 key 缓存空值（短 TTL）；布隆过滤器前置拦截。
  5. **击穿**：单飞（singleflight / 互斥锁）只放一个请求回源；热 key 永不过期 + 后台异步刷新（逻辑过期）。
  6. **热 key**：探测（采样统计 / 代理层 top-k）→ 本地缓存 + 复制到多个分片（key 加后缀）分摊；写热 key 用本地聚合再批量写。
  7. **容量与淘汰**：按「热数据集 × 1.2」定内存；淘汰 LRU 常用，访问模式有周期性用 LFU / W-TinyLFU；关注命中率（目标 > 95%）而不是内存占用。
  8. **大 key**：拆分（hash 分桶）、压缩、禁止 `KEYS` / 大范围 `HGETALL`。
  9. **运维面**：命中率、p99、连接数、驱逐速率、主从复制延迟、内存碎片率；故障演练「缓存整体丢失时 DB 扛不扛得住」——答案通常是不能，所以要限流。
- **易错点 / 面试官关注**：
  - 「先删缓存再写库」或「写库后更新缓存」——并发下都会脏。
  - 把 Redis 当成强一致存储；不知道 Redis 主从异步复制会丢写。
  - 说不出命中率目标与「缓存丢了 DB 能不能扛」。
- **延伸**：Q5、Q6、[collections/k8s-web-archive.md 第 686–697 题](../../collections/k8s-web-archive.md)（HelloInterview 分布式缓存拆解速答）、[system-design/distributed-cache/answer-suites/](../../system-design/distributed-cache/answer-suites/README.md)（逐阶段 60 秒口述答案 + 数字推导 + 计时演练，来自一场 7.6/10 的模拟面试复盘；面试中不要直接给候选人看）、[system-design/distributed-cache/](../../system-design/distributed-cache/)、[system-design/distributed-cache-design/](../../system-design/distributed-cache-design/)、[system-design/caching/](../../system-design/caching/)、[middleware/middleware-questions.md](../middleware/middleware-questions.md)

---

### Q8. 设计一个分布式唯一 ID 生成器：UUID、Snowflake、号段模式怎么选？

- **难度**：🟢 初级
- **关键词**：UUID, Snowflake, 号段 segment, 时钟回拨 clock drift, 趋势递增, 索引局部性
- **概念速记**：
  - **UUID v4**：128 位随机，无协调、全局唯一；但无序，作为 B-tree 主键会随机写导致页分裂与缓存命中差。
  - **Snowflake**：64 位 = 时间戳(41) + 机器 ID(10) + 序列号(12)，趋势递增、每毫秒每机 4096 个；依赖机器 ID 分配与时钟。
  - **号段模式**：DB 里一行 `max_id`，每次批量取一段（如 1000 个）放内存分配；DB 压力低，双 buffer 预取避免抖动。
- **问题**：一个多机房部署的订单系统需要全局唯一、趋势递增、每秒 10 万级的 ID，你怎么设计？时钟回拨怎么办？
- **参考答案**：
  1. **需求拆解**：唯一（硬）、趋势递增（利于索引与分页）、高可用（不能依赖单点）、不可预测（订单号防遍历，可用混淆层）、长度 64 位放 BIGINT。
  2. **选 Snowflake 变体**：机器 ID 由协调服务（ZK / etcd / 配置中心）分配并租约续期，避免重复；机房 ID 占几位保证多机房不撞。
  3. **时钟回拨**：小回拨（< 几十 ms）等待追平；大回拨拒绝服务并告警；或维护「上次时间戳」，回拨时改用序列号扩展位 / 备用机器 ID。NTP 用 slew 模式而非 step。
  4. **号段模式适用场景**：只有单机房 / 允许依赖 DB 时更简单；双 buffer 预取；配合 DB 高可用。
  5. **UUID 适用场景**：无中心协调、不需要排序（对象存储 key、trace id）；写 MySQL 主键要用 UUID v7（时间有序）或改为 BINARY(16)。
  6. **运维面**：ID 服务是全站依赖，要多实例无状态 + 本地缓存一段 ID 允许短暂脱离协调服务；监控回拨事件、分配 QPS、序列号溢出等待次数。
- **易错点 / 面试官关注**：
  - 用 DB 自增做全局 ID（单点 + 跨机房冲突）却不知道双主步长方案的局限。
  - 不知道 UUID 做主键为什么慢。
  - 没考虑时钟回拨。
- **延伸**：Q6、Q15、[system-design/unique-id-generator/](../../system-design/unique-id-generator/)、[system-design/unique-id/](../../system-design/unique-id/)

---

### Q9. 设计一个分布式锁：Redis RedLock 与 ZooKeeper / etcd 方案的取舍，fencing token 是什么？

- **难度**：🟡 中级
- **关键词**:分布式锁, RedLock, 租约 lease, fencing token, ZooKeeper 临时顺序节点, etcd lease, 羊群效应 herd effect
- **概念速记**：
  - **租约（Lease）**：锁带过期时间，持有者崩溃后自动释放；代价是持有者 GC 停顿 / 网络延迟后可能「以为自己还持锁」。
  - **Fencing token**：锁服务每次授予锁递增一个 token，被保护的资源拒绝旧 token 的写——这是解决「过期后仍写入」的唯一可靠手段。
  - **临时顺序节点**：ZK 客户端会话断开节点即消失；顺序号最小者持锁，其他人只 watch 前一个节点（避免羊群效应）。
- **问题**：定时任务要保证「同一时刻只有一个实例执行」，用什么锁？Redis `SET NX PX` 够不够？RedLock 争议是什么？什么时候必须用 ZK / etcd？
- **参考答案**：
  1. **先问业务容忍度**：锁是「效率」目的（避免重复劳动，偶尔重复无害）还是「正确性」目的（重复执行会损坏数据）。前者 Redis 单节点 `SET key val NX PX ttl` + Lua 校验 val 再删即可；后者需要 fencing。
  2. **Redis 单节点锁的坑**：主从异步复制，主挂了从没同步到锁 → 两个持有者；TTL 到期但任务未完成 → 需要 watchdog 续期（Redisson）；解锁必须校验持有者。
  3. **RedLock**：向 N（5）个独立 Redis 写锁，多数成功且总耗时 < TTL 则持有。争议（Kleppmann）：依赖时钟假设，GC 停顿 / 时钟跳变仍可导致两个持有者，且没有 fencing token。结论：不要把 RedLock 当正确性锁。
  4. **ZK / etcd 方案**：基于共识（ZAB / Raft），会话 / lease 绑定；etcd 用 `lease + txn(compare revision)` 实现，锁的 revision 天然是 fencing token；ZK 用临时顺序节点。代价是延迟高（共识写）与吞吐低，适合低频、强正确性场景。
  5. **正确性的最终防线在资源侧**：DB 写带 `WHERE token >= ?` 或乐观锁版本号；存储不支持时把操作做成幂等。
  6. **运维面**：锁服务高可用（奇数节点、跨 AZ）、锁等待 / 持有时长监控、锁泄漏（未释放）告警、避免长事务持锁。
- **易错点 / 面试官关注**：
  - 用 `SETNX` + `EXPIRE` 两步（非原子）。
  - 不知道 fencing token；以为 RedLock 完美。
  - 用分布式锁替代本该用的幂等设计。
- **延伸**：Q3、Q26、[system-design/distributed-locking/](../../system-design/distributed-locking/)、[system-design/zookeeper/](../../system-design/zookeeper/)、[system-design/filelock/](../../system-design/filelock/)

---

### Q10. 设计一个分布式消息队列（Kafka 风格）：分区、顺序、投递语义、积压与消费者组

- **难度**：🔴 高级
- **关键词**：分区 partition, 副本 ISR, 顺序保证, at-least-once / exactly-once, 幂等消费, 消费者组 rebalance, 死信队列 DLQ, 积压 lag
- **概念速记**：
  - **分区**：topic 切成多个有序日志；分区内有序、分区间无序；分区数 = 并行度上限。
  - **ISR（In-Sync Replicas）**：与 leader 保持同步的副本集合；`acks=all` + `min.insync.replicas=2` 才能保证不丢。
  - **投递语义**：at-most-once（可能丢）/ at-least-once（可能重）/ exactly-once（生产者幂等 + 事务 + 消费端幂等共同实现，端到端仍需业务幂等）。
- **问题**：设计一个支撑百万级 msg/s 的消息队列：存储结构、复制、顺序、消费模型、不丢不重怎么做、积压与 rebalance 怎么处理。
- **参考答案**：
  1. **存储**：每分区是顺序追加的 segment 文件 + 稀疏索引；顺序写 + page cache + `sendfile` 零拷贝是高吞吐来源；按时间 / 大小做 retention，compacted topic 保留每 key 最新值。
  2. **复制与可靠性**：每分区 leader + follower，ISR 机制；生产者 `acks=all`；leader 选举由控制器（ZK 或 KRaft）；`unclean.leader.election=false` 防止丢数据换可用性。
  3. **顺序**：按业务 key（订单 ID）分区保证同 key 有序；全局有序只能单分区（牺牲并行）；消费者单线程或按 key 分线程。
  4. **消费模型**：消费者组内每分区只给一个消费者；位点（offset）由消费者提交——**先处理后提交 = at-least-once**；处理必须幂等（唯一键去重表 / 幂等 token）。
  5. **不丢**：生产端重试 + 幂等生产者（PID + seq）；服务端 ISR ≥ 2；消费端手动提交。**不重**：消费端幂等；跨 topic 原子用事务。业务上「outbox 模式」解决「写库 + 发消息」原子性。
  6. **积压（lag）**：监控 consumer lag；处理慢 → 加分区 + 加消费者（分区数是上限）、批量消费、异步化处理；毒消息 → 重试 N 次后进 DLQ 并告警。
  7. **Rebalance**：消费者加入 / 退出触发再分配，期间停止消费（stop-the-world）；用 cooperative / sticky 策略、`static membership` 减少抖动；避免长处理导致心跳超时被踢。
  8. **Kafka vs RabbitMQ 取舍**：日志型（重放、高吞吐、流处理）选 Kafka；复杂路由、低延迟单条确认、优先级 / 延迟队列选 RabbitMQ；两者都需要消费者幂等。
  9. **运维面**：lag、ISR 收缩、under-replicated partitions、请求队列时间、磁盘水位；扩分区不可逆且会破坏 key 有序性，要提前规划。
- **易错点 / 面试官关注**：
  - 声称「exactly-once」而不说端到端需要业务幂等。
  - 以为加消费者就能提吞吐（超过分区数无效）。
  - 不知道 outbox 模式与「双写」问题。
- **延伸**：Q4、Q18、Q25、[system-design/distributed-message-queue/](../../system-design/distributed-message-queue/)、[system-design/kafka-vs-rabbitmq.md](../../system-design/kafka-vs-rabbitmq.md)、[system-design/pubsub/](../../system-design/pubsub/)、[middleware/middleware-questions.md](../middleware/middleware-questions.md)

---
### Q11. 设计 CDN 与对象存储（S3 风格）：边缘缓存、回源、分片上传、纠删码

- **难度**：🟡 中级
- **关键词**：CDN, 边缘节点 PoP, 回源 origin, 缓存失效 purge, 对象存储, 分片上传 multipart, 纠删码 erasure coding, 分层存储
- **概念速记**：
  - **CDN**：把静态 / 可缓存内容放到离用户近的边缘节点，命中时不回源；关键指标是命中率与回源带宽。
  - **对象存储**：扁平命名空间 + HTTP API（PUT/GET/DELETE），元数据与数据分离；不支持随机改写，适合一次写多次读。
  - **纠删码（EC）**：把对象切成 k 个数据块 + m 个校验块，任意 k 块可恢复；存储开销 (k+m)/k（如 1.5×）远低于三副本（3×），代价是重建时计算与网络开销大。
- **问题**：设计一个图片 / 视频分发平台的存储与分发层：对象存储内部怎么组织元数据与数据、大文件怎么上传、副本 vs EC、CDN 怎么接、缓存怎么失效、成本怎么控。
- **参考答案**：
  1. **对象存储架构**：API 网关 → 元数据服务（对象名 → 存储位置、版本、ACL；用分片 KV / DB）→ 数据节点（按 chunk 存放）；放置服务负责选择节点（机架 / AZ 感知）与再均衡。
  2. **写路径**：小对象直接写；大对象 **multipart upload**（分片并行、断点续传、最后 complete 合并元数据）；内容寻址（SHA-256）去重；先写数据再提交元数据，保证元数据可见即数据可读。
  3. **持久性**：热数据三副本（读快、重建快），温冷数据 EC（如 8+4）；后台巡检（scrub）校验和，坏块修复；跨 AZ 放置，可选跨区域异步复制。
  4. **读路径与 CDN**：客户端 → CDN 边缘 → （miss）区域缓存 → 源站对象存储；用签名 URL 控制访问；`Cache-Control` / ETag 决定边缘缓存时长；大文件按 Range 缓存。
  5. **失效**：内容用**版本化 URL**（`/img/abc.v2.jpg`）让失效变成「换 URL」，避免 purge；必须 purge 时按 tag / 前缀批量，接受传播延迟秒到分钟级。
  6. **回源保护**：请求合并（collapsed forwarding）防击穿；源站限流；预热热门内容到边缘。
  7. **成本**：出口带宽是大头 → 提高命中率（更长 TTL、分层缓存）、压缩 / 转码（WebP / AVIF、多码率）；存储用生命周期策略（30 天后 EC、90 天冷存、按需删除）。
  8. **运维面**：命中率、回源 QPS 与带宽、边缘 5xx、p99 首字节时间；存储侧 durability 巡检、修复队列、磁盘 / 节点均衡；容量按增长率提前 N 个月采购。
- **易错点 / 面试官关注**：
  - 元数据放单库不分片；不知道对象存储不支持原地修改。
  - 只说「三副本」不知道 EC 的存储开销与重建代价。
  - 缓存失效只会「清缓存」，不知道版本化 URL。
- **延伸**：Q2、Q19、[system-design/cdn/](../../system-design/cdn/)、[system-design/blob-store/](../../system-design/blob-store/)、[system-design/s3-like-storage/](../../system-design/s3-like-storage/)、[system-design/object-storage/](../../system-design/object-storage/)

---

### Q12. 设计负载均衡器与 API 网关：L4 vs L7、健康检查、会话保持、网关职责边界

- **难度**：🟡 中级
- **关键词**：L4 / L7, 健康检查 health check, 一致性哈希, DSR, 连接保持 keep-alive, 网关 gateway, 认证 / 限流 / 路由, 优雅下线
- **概念速记**：
  - **L4 LB**：按 IP/端口转发 TCP/UDP，不解析应用层，吞吐高（LVS / IPVS、云 NLB）；**L7 LB**：解析 HTTP，可按路径 / 头 / Cookie 路由，做 TLS 终止、重试（Nginx / Envoy / ALB）。
  - **DSR（Direct Server Return）**：回包不经过 LB 直接回客户端，适合响应远大于请求的场景。
  - **API 网关**：L7 入口 + 跨切面能力（认证、限流、路由、协议转换、灰度、可观测）；不该放业务逻辑。
- **问题**：设计一个 100K QPS 的入口层：几层 LB、各层做什么、健康检查与摘流怎么做、会话保持怎么解决、网关放哪些能力、自身怎么高可用。
- **参考答案**：
  1. **分层**：DNS（GSLB，就近 / 权重）→ 四层 LB（LVS/IPVS 或云 NLB，anycast / ECMP 多活）→ 七层网关（Envoy / Nginx / Kong）→ 服务。四层只做转发保证吞吐，七层做智能。
  2. **算法**：轮询 / 最少连接（长连接场景）/ 加权（异构机器）/ 一致性哈希（缓存亲和、WebSocket）/ P2C（两次随机选负载低者，避免羊群）。
  3. **健康检查**：主动（周期探测 `/healthz`，区分 liveness 与 readiness）+ 被动（连续 5xx / 超时自动摘除 outlier detection）；**优雅下线**：先从 LB 摘除、等待在途请求（drain）、再停进程；K8s 里对应 readinessProbe + preStop。
  4. **会话保持**：优先无状态（会话外置 Redis / JWT）；确需粘性用 Cookie 哈希，且要能在实例下线时迁移。
  5. **网关职责**：TLS 终止与 mTLS、认证鉴权（JWT / OAuth）、限流（Q5）、路由与灰度（按 header / 权重）、重试与超时（带预算，避免重试风暴）、协议转换（gRPC-web）、请求日志与指标。**不放**：业务编排、数据聚合（那是 BFF 的事）。
  6. **自身高可用**：LB 无状态多实例；四层用 VRRP / anycast；七层网关水平扩展；配置由控制面下发（热更新），配置错误要能秒级回滚。
  7. **超时与重试策略**：入口超时 < 上游超时之和；只对幂等请求重试；用 retry budget（如 ≤ 20% 请求可重试）与 backoff + jitter。
  8. **运维面**：每路由 QPS / p99 / 5xx、上游健康实例数、连接数与 TLS 握手、配置推送成功率；容量按峰值 × 2 冗余、N+1 跨 AZ。
- **易错点 / 面试官关注**：
  - 分不清四层与七层能做什么；不知道 readiness 与 liveness 的区别。
  - 重试无预算导致级联；网关里塞业务逻辑。
  - 不会讲优雅下线导致发布时 5xx。
- **延伸**：Q5、[network/network-questions.md](../network/network-questions.md)、[service-mesh/service-mesh-questions.md](../service-mesh/service-mesh-questions.md)、[system-design/load-balancer/](../../system-design/load-balancer/)、[system-design/api-gateway/](../../system-design/api-gateway/)

---

### Q13. 设计搜索与 Typeahead（自动补全）：倒排索引、Trie、Top-K 与热点更新

- **难度**：🟡 中级
- **关键词**：倒排索引 inverted index, 分片 / 副本, Trie / 前缀树, Top-K, 离线聚合, 布隆过滤器, 拼写纠错
- **概念速记**：
  - **倒排索引**：词 → 文档列表（posting list），支持关键词检索与打分（BM25）；构建成本高，通常按段（segment）不可变 + 合并。
  - **Trie**：按前缀组织的树，每个节点缓存该前缀的 Top-K 热门词，前缀查询 O(前缀长度)。
  - **Top-K**：用堆 / count-min sketch 在流上近似统计热门项；精确 Top-K 需要离线 MapReduce。
- **问题**：设计一个搜索框：输入时 p99 < 100ms 返回 5 条补全，每天 10 亿次查询；如何构建与更新 Trie、如何分片、如何处理热点词与个性化，全文检索层怎么设计。
- **参考答案**：
  1. **数据流**：查询日志 → 流式聚合（Flink / Kafka Streams，按小时统计词频）+ 离线全量（每天）→ 构建 Trie（每节点存 Top-K）→ 快照发布到补全服务（内存加载，蓝绿切换）。
  2. **Trie 分片**：按首字母 / 前缀哈希分片（注意热点前缀如 "a"、"the" 需二次切分或专门副本）；每片多副本，前端用一致性哈希路由。
  3. **查询路径**：浏览器防抖（100–200ms）+ 客户端缓存 → CDN / 边缘缓存热门前缀 → 补全服务内存 Trie。返回 Top-5 + 高亮。
  4. **更新策略**：Trie 不适合高频原地更新；用「周期性重建 + 增量热更新（只更新热门节点的计数）」；突发热点（新闻）用短周期流式层覆盖。
  5. **过滤与安全**：敏感词黑名单、个性化（用户历史前缀 + 全局 Top-K 合并打分）、拼写纠错（编辑距离 + 语言模型）。
  6. **全文检索层**：Elasticsearch / Lucene 倒排索引，按时间或业务分片；写入走近实时 refresh（1s）；相关性 BM25 + 业务加权；深分页用 search_after；高基数聚合限制。
  7. **运维面**：p99、缓存命中率、Trie 构建时长与内存、快照切换失败回滚；ES 侧 segment 合并压力、JVM 堆、分片均衡、慢查询日志。
- **易错点 / 面试官关注**：
  - 每次请求查数据库 `LIKE 'abc%'`。
  - Trie 不做 Top-K 缓存导致每次遍历子树。
  - 不知道热点前缀分片不均。
- **延伸**：Q14、Q16、[system-design/typeahead/](../../system-design/typeahead/)、[system-design/typeahead-suggestion-system/](../../system-design/typeahead-suggestion-system/)、[system-design/distributed-search/](../../system-design/distributed-search/)、[system-design/topk/](../../system-design/topk/)、[system-design/elastic/](../../system-design/elastic/)

---

### Q14. 设计时序数据库 / 指标存储：写入路径、压缩、降采样、高基数与查询引擎

- **难度**：🔴 高级
- **关键词**：TSDB, 时间分区, LSM / 列存, Gorilla 压缩, 降采样 downsampling, 高基数 cardinality, 倒排标签索引, 保留策略 retention
- **概念速记**：
  - **时序数据**：`(metric, labels) → [(ts, value), ...]`，写多读少、按时间追加、按时间范围 + 标签过滤查询。
  - **Gorilla 压缩**：时间戳 delta-of-delta、值 XOR 编码，单点从 16 字节压到 ~1.4 字节。
  - **高基数**：标签组合数爆炸（如 label 里放 user_id）导致索引与内存暴涨，是 Prometheus 类系统最常见的故障根因。
- **问题**：为 10 万台主机、每台 1000 个指标、15s 采集一次的平台设计指标存储：写入吞吐、存储格式、索引、降采样、查询、长期存储、如何防高基数。
- **参考答案**：
  1. **规模**：1e5 × 1e3 / 15 ≈ 6.7M 样本/s；原始 16B/样本 ≈ 100MB/s，压缩后 ~10MB/s ≈ 0.9TB/天；1 年 ~300TB（未降采样）。
  2. **写入路径**：采集 → 写入网关（按 series 哈希分片到 ingester）→ 内存 head block（按 series 追加，WAL 保证崩溃恢复）→ 每 2h 刷成不可变 block（列式、按时间分区）→ 后台 compaction 合并。
  3. **索引**：标签倒排索引（label=value → series ID 集合），查询时对 posting list 求交；series ID → chunk 位置。索引也按 block 分。
  4. **降采样与保留**：原始 15d → 5m 聚合 90d → 1h 聚合 2y；每层保留 min/max/sum/count 以便正确聚合；对象存储做长期层（Thanos / Cortex / Mimir 模式）。
  5. **查询引擎**：解析 → 选择 block（按时间范围剪枝）→ 并行拉取 chunk → 聚合；查询前端做拆分（按天）、缓存结果、限制最大 series 数与时间跨度。
  6. **高基数防线**：写入侧 relabel 丢弃高基数标签、每租户 series 上限、每 scrape 样本上限；观测 `series 数 / 增长率` 与「新 series 创建率」（churn）；教育用户「ID 类字段进日志 / trace，不进指标」。
  7. **高可用**：ingester 复制因子 3（同一 series 写 3 个 ingester，查询去重）；多副本 Prometheus + 去重；对象存储保证长期数据持久。
  8. **运维面**：ingest 速率、series 数与 churn、head 内存、compaction 延迟、查询 p99 与被拒查询、对象存储成本；容量按 series 数而非主机数规划。
- **易错点 / 面试官关注**：
  - 用关系库或通用 KV 存指标；不知道时间分区与不可变 block 的价值。
  - 说不出高基数为什么会炸、怎么防。
  - 降采样不保留 count/sum 导致平均值算错。
- **延伸**：Q24、[observability/observability-questions.md](../observability/observability-questions.md)、[system-design/time-series-database/](../../system-design/time-series-database/)、[system-design/metrics-monitoring-hello-interview/](../../system-design/metrics-monitoring-hello-interview/)

---

## 三、经典产品设计

### Q15. 设计短链服务（TinyURL / Bitly）：编码、存储、重定向与热点

- **难度**：🟢 初级
- **关键词**：base62, 哈希 vs 号段, 301 vs 302, 读多写少, 缓存, 布隆过滤器, 过期清理
- **概念速记**：
  - **Base62**：用 `[0-9a-zA-Z]` 62 个字符表示整数，7 位可表示 62^7 ≈ 3.5 万亿个短码。
  - **301 vs 302**：301 永久重定向会被浏览器缓存（省服务端流量但统计不到点击）；302 每次回源（可统计，多一次请求）。
- **问题**：设计一个 100:1 读写比、每天 1 亿次跳转的短链服务：短码怎么生成、怎么存、怎么扩展读、怎么防碰撞与恶意、过期怎么处理。
- **参考答案**：
  1. **估算**：写 ~12/s（峰值几百）、读 ~1.2K/s（峰值 ~10K）；5 年 ~20 亿条 × ~500B ≈ 1TB——单表分片不急，但读要缓存。
  2. **短码生成**：(a) 全局唯一 ID（Q8）→ base62，无碰撞、可预测（可加混淆位）；(b) 对长 URL 哈希（MD5/SHA）取前 7 位 + 碰撞检测重试，同 URL 同短码但需查重；(c) **计数器 + base62**：Redis `INCR` 做单一事实来源，写服务**批量领号**（一次拿 1000 个本地分配）减少网络往返；多机房给每个区域分配**不相交的计数区间**（A 区 0–10 亿、B 区 10–20 亿）避免跨区协调；Redis 故障丢几个号无所谓（只要唯一不要连续），DB 上 `short_code` 的 UNIQUE 约束是最终兜底。推荐 (c) 或 (a)，自定义别名放独立命名空间（如禁止生成码使用某个前缀字符），防止与未来生成码冲突。
  3. **存储**：KV 或 MySQL（`short → long, owner, created, expire, clicks`），主键 short；按 short 哈希分片；写走主库，读走缓存。
  4. **读路径**：LB → 服务 → Redis（命中率目标 > 99%，热门短链常驻）→ miss 查 DB 回填；不存在的短码用布隆过滤器挡住穿透。返回 302（要统计）或 301（纯省流量）。
  5. **点击统计**：异步（写 Kafka → 流式聚合），不在跳转路径同步写 DB。
  6. **安全与治理**：恶意 URL 扫描（安全 API / 黑名单）、限流（Q5）、短码不可枚举（随机化）、私有 / 需登录短链。
  7. **过期**：`expiration_date` 字段 + 惰性删除（读到过期返回 **410 Gone**）+ 后台批量清理；**缓存 TTL 必须 ≤ 剩余过期时间**，否则缓存里会残留已过期短链。
  8. **读写分离扩展**：读服务（跳转）与写服务（创建）拆成独立可扩展的服务，读服务无状态水平扩容，热点全部由缓存 + CDN 边缘承接；DB 1B 行 × ~500B ≈ 500GB，单实例 Postgres/MySQL + 副本即可，先别急着分片。
  9. **运维面**：跳转 p99（目标 < 100ms，缓存命中路径 < 20ms）、缓存命中率、DB 慢查询、错误率；多机房只读副本就近服务。
- **按级别的期望**（面试官口径）：
  - 🟡 中级：能给出可工作的高层设计（提交 → 生成短码 → 存映射 → 跳转），知道短码必须唯一并至少提出一种生成方案，能说清 301 与 302 的区别。
  - 🔴 高级：主动识别三大挑战（唯一生成、快速跳转、水平扩展），不需提示就能对比哈希（碰撞处理）与计数器（协调开销）的取舍，详细讲缓存策略与失效。
  - 🔴 Staff+：一开始就按「读极多写极少」组织设计；主动讲多机房计数区间分配、Redis 故障切换时会发生什么、CDN/边缘做跳转的成本收益。
- **易错点 / 面试官关注**：
  - 用自增 ID 直接 base62（可枚举全部短链）；或多写实例各自计数导致重号。
  - 分不清 301/302 对统计与可更新性的影响；过期不返回 410。
  - 同步写点击计数拖慢跳转；缓存 TTL 长于过期时间。
- **延伸**：Q7、Q8、[system-design/url-shortener/](../../system-design/url-shortener/)、[system-design/url-shortener/22-bitly-full-design.md](../../system-design/url-shortener/22-bitly-full-design.md)（逐阶段口述答案 + 推导 + 速答卡，基于 HelloInterview Bitly 拆解并补 SRE 视角；面试中不要直接给候选人看）、[system-design/tinyurl-system/](../../system-design/tinyurl-system/)、[system-design/pastebin/](../../system-design/pastebin/)、[system-design/14-bitly.md](../../system-design/14-bitly.md)、来源：[Hello Interview — Bitly problem breakdown](https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly)（Evan King，2026-02）

---

### Q16. 设计信息流（News Feed / Twitter 时间线）：推 vs 拉、大 V 问题、排序与缓存

- **难度**：🟡 中级
- **关键词**：fan-out on write（推）, fan-out on read（拉）, 混合模式, 大 V / 热点用户, 时间线缓存, 排序 ranking, 分页游标
- **概念速记**：
  - **推模式**：发帖时把帖子 ID 写进每个粉丝的收件箱（timeline cache）；读快、写放大（粉丝数倍）。
  - **拉模式**：读时实时聚合所关注用户的最新帖；写便宜、读慢且关注多时聚合成本高。
  - **混合**：普通用户推、大 V 拉（读时合并），兼顾两者。
- **问题**：设计支持 3 亿 DAU 的 feed：发帖与读 feed 的路径、推拉怎么选、千万粉丝的大 V 怎么处理、feed 排序放哪、分页怎么做、缓存怎么组织。
- **参考答案**：
  1. **发帖路径**：写帖子服务（帖子表分片，内容 + 媒体走对象存储）→ 发 fan-out 事件到队列 → fan-out worker 查关注关系（图服务 / 缓存）→ 把 `post_id` 写入每个活跃粉丝的 timeline cache（Redis list / sorted set，只保留最近 N 条）。
  2. **读路径**：读 timeline cache 拿 ID 列表 → 批量 hydrate（帖子内容、作者、计数，各自缓存）→ 排序 / 过滤 → 返回。冷用户 cache 缺失时回退到拉模式重建。
  3. **大 V**：粉丝 > 阈值（如 10 万）不推；读时把关注的大 V 最新帖与自己的收件箱合并（k 路归并）。同时只给「最近活跃」用户推，减少写放大。
  4. **排序**：时间序简单可预期；算法排序（互动概率）放在读路径的 ranking 服务，输入候选集（收件箱 + 推荐召回），输出打分——与 Q33 衔接。
  5. **分页**：游标（`(score, post_id)`）而不是 offset；保证新帖插入不会重复 / 漏掉。
  6. **一致性**：删除帖子 → 从各收件箱惰性过滤（hydrate 时发现已删则跳过）而非同步清理；关注 / 取关的收件箱补齐 / 剔除异步做。
  7. **存储**：帖子按 `post_id`（时间有序）分片；关注关系用图存储或双向邻接表（分别按 follower / followee 分片）；timeline cache 按 user_id 分片，可丢（可重建）。
  8. **运维面**：fan-out 延迟（发帖到粉丝可见 p99）、队列积压、hydrate 缓存命中率、feed p99；大 V 发帖引发的突发写要限速。
- **易错点 / 面试官关注**：
  - 只说推或只说拉；不知道大 V 问题。
  - 用 offset 分页；同步 fan-out。
  - 没说 timeline cache 可丢、怎么重建。
- **延伸**：Q7、Q10、Q33、[system-design/newsfeed/](../../system-design/newsfeed/)、[system-design/fb-news-feed/](../../system-design/fb-news-feed/)、[system-design/twitter/](../../system-design/twitter/)、[system-design/instagram/](../../system-design/instagram/)

---

### Q17. 设计即时通讯系统（WhatsApp / Messenger）：长连接、消息顺序、送达状态、群聊与离线

- **难度**：🟡 中级
- **关键词**：WebSocket, 连接网关, 会话路由, 消息 ID 与顺序, 送达回执 ack, 离线消息, 群聊扇出, 端到端加密 E2EE
- **概念速记**：
  - **连接网关（chat server）**：维持与客户端的长连接，无业务状态；「用户在哪台网关」由在线状态服务（Redis）记录。
  - **消息顺序**：单聊内用会话级单调递增序号（服务端分配），客户端按序号排序与去重。
  - **送达状态**：发送中 → 服务端已收（ack）→ 对端已送达 → 已读；每一步是一条回执消息。
- **问题**：设计支持 5 亿 DAU 的 IM：连接层怎么扩展、消息怎么路由、怎么保证不丢不乱序、离线怎么补、群聊 1000 人怎么发、在线状态怎么做、加密怎么做。
- **参考答案**：
  1. **连接层**：WebSocket 网关集群（每台维持百万级连接，长连接消耗内存与 fd），客户端通过接入服务发现「分配到哪台」；心跳 + 断线重连指数退避；网关只转发不存业务状态。
  2. **消息路径**：发送方 → 网关 A → 消息服务（分配会话序号、持久化到消息存储、写发件人副本）→ 查在线状态得到接收方所在网关 B → 推送；B 不在线则写离线队列 / 推送通知（APNs/FCM）。
  3. **存储**：消息表按 `conversation_id` 分片（同会话同片，范围读取高效），主键 `(conversation_id, seq)`；用宽列 / KV（Cassandra / HBase）承接高写入；媒体走对象存储 + CDN。
  4. **不丢不乱序**：客户端本地生成 `client_msg_id` 做幂等；服务端持久化后才 ack；接收端用 seq 检测缺口并向服务端拉取补齐（拉 + 推结合）；离线上线后按「上次 seq」增量同步。
  5. **群聊**：小群（≤ 几百）写扩散（每成员收件箱一份索引）；大群 / 超级群读扩散（消息只存一份，成员按 seq 拉）+ 推送通知；@ 与已读回执在大群里降级（只统计不逐条推）。
  6. **在线状态**：心跳写 Redis（TTL），好友订阅变更；大量好友时用「上线时批量拉 + 变更推送节流」，避免状态风暴。
  7. **E2EE**：Signal 协议（X3DH + Double Ratchet），服务端只见密文，元数据（谁给谁）仍可见；多设备各有会话密钥；服务端无法做内容检索 / 审核是业务代价。
  8. **运维面**：连接数 / 每网关、消息端到端延迟 p99、送达率、离线队列长度、推送成功率；网关发布要「连接漂移」（逐台摘流、客户端重连打散）。
- **易错点 / 面试官关注**：
  - 用 HTTP 轮询；把用户状态存在网关内存导致不能扩缩。
  - 消息顺序靠客户端时间戳。
  - 群聊不区分小群写扩散 / 大群读扩散。
- **延伸**：Q10、Q18、[system-design/whatsapp/](../../system-design/whatsapp/)、[system-design/messenger/](../../system-design/messenger/)、[system-design/facebook-messenger-system/](../../system-design/facebook-messenger-system/)、[system-design/live-comments-system/](../../system-design/live-comments-system/)

---

### Q18. 设计通知系统：多渠道、模板、限频、去重与可靠投递

- **难度**：🟡 中级
- **关键词**：多渠道 push / SMS / email, 优先级队列, 模板与本地化, 用户偏好, 去重与限频, 重试与 DLQ, 第三方网关
- **概念速记**：
  - **通知系统**：接收事件 → 决定给谁、通过什么渠道、什么内容 → 可靠投递到第三方（APNs / FCM / 短信网关 / SMTP）→ 记录状态与回执。
  - **限频（rate control）**：用户级（每天最多 N 条）+ 渠道级（短信网关吞吐）+ 全局（避免营销洪峰打垮推送）。
- **问题**：设计一个每天 100 亿条、覆盖推送 / 短信 / 邮件 / 站内信的通知平台：接口、优先级、模板、偏好与合规、去重限频、第三方故障、可观测。
- **参考答案**：
  1. **入口**：通知 API（同步校验 + 幂等 key）→ 按优先级写入队列（交易类高优独立队列，营销类低优可延迟）；批量 API 供营销系统。
  2. **编排服务**：查用户偏好（渠道开关、勿扰时段、退订）→ 渲染模板（多语言、变量）→ 去重（幂等 key + 内容哈希，窗口内相同不重发）→ 限频（令牌桶按用户 / 渠道）→ 投递任务入渠道队列。
  3. **渠道 worker**：每渠道独立消费者与并发上限；对第三方调用带超时 / 重试 / 熔断；多供应商 failover（短信 A 挂切 B）；回执（送达 / 失败 / 点击）异步回写状态。
  4. **可靠性**：至少一次 + 幂等（第三方多数不幂等，靠去重表）；失败进重试队列指数退避，超过次数进 DLQ 人工 / 告警；持久化每条通知状态机（created → queued → sent → delivered/failed）。
  5. **优先级隔离**：物理隔离队列与 worker 池，防止营销洪峰阻塞验证码；验证码类 SLO p99 < 5s。
  6. **合规**：退订链接与偏好中心、地区法规（GDPR/TCPA）、敏感内容审核、发送时段限制。
  7. **运维面**：各渠道发送成功率 / 延迟 / 积压、第三方错误率、退订率与投诉率（影响供应商信誉）；容量按峰值（如秒杀提醒）预留并可降级低优通知。
- **易错点 / 面试官关注**：
  - 同步调用第三方；不区分优先级导致验证码被营销拖慢。
  - 没有去重与幂等（用户收到重复短信）。
  - 忽略用户偏好与合规。
- **延伸**：Q10、Q17、[system-design/notification-system/](../../system-design/notification-system/)、[system-design/notification-service/](../../system-design/notification-service/)、[system-design/email-service/](../../system-design/email-service/)

---

### Q19. 设计视频平台（YouTube）与直播系统：上传转码、自适应码率、分发与直播延迟

- **难度**：🔴 高级
- **关键词**：分片上传, 转码 DAG, ABR（HLS / DASH）, CDN, 预签名 URL, 直播 RTMP / SRT / WebRTC, 延迟与卡顿, 弹幕
- **概念速记**：
  - **ABR（自适应码率）**：把视频切成小段（2–6s）并转出多档码率，播放器按带宽切换档位；HLS（m3u8 + ts/fmp4）与 DASH（mpd）是两大协议。
  - **转码 DAG**：上传原片后按「抽帧 → 多码率转码 → 切片 → 打包 → 缩略图 / 字幕 / 审核」拆成有依赖的任务图并行执行。
  - **直播延迟**：RTMP 推流 → 转码 → HLS 分发通常 10–30s；LL-HLS / DASH 可到 3–5s；WebRTC 亚秒级但成本高、规模难。
- **问题**：设计 YouTube 级的点播平台，再扩展到直播：上传、转码、存储、分发、播放；直播的推流、转码、分发、延迟与互动（弹幕 / 评论）怎么做；成本与可观测。
- **参考答案**：
  1. **上传**：客户端向 API 拿预签名 URL 直传对象存储（不过应用服务器），分片 + 断点续传；上传完成事件触发转码流水线；原片保留（冷存）。
  2. **转码**：DAG 调度（Q26 的调度器）把任务分发到转码集群（CPU/GPU 混合、抢占式实例降本）；并行按分段切分（把 1 小时视频切成 N 段并行转）；输出多码率 + 缩略图 + 字幕 + 审核（内容安全模型）；状态机可重试、幂等（同段重复转码覆盖）。
  3. **存储与分发**：切片放对象存储，CDN 前置（Q11）；热门视频预热到边缘，长尾按需回源；按地域多源站。
  4. **播放**：播放器拿 manifest → 按带宽选档 → 预取；观测卡顿率、起播时间、码率切换次数（QoE）。
  5. **元数据与互动**：视频元数据 DB（分片）、观看计数异步聚合、推荐（Q33）；评论 / 点赞独立服务。
  6. **直播**：主播 RTMP/SRT 推流到就近接入节点 → 实时转码成多档 → 切片推 CDN（HLS/DASH）；互动弹幕走 Q17 的长连接网关 + 按房间扇出（热门房间读扩散 + 合并 / 抽样）；录制回放异步生成。延迟要求高时上 WebRTC + SFU，代价是每观众一路流、CDN 不可用。
  7. **失败处理**：转码失败重试与降级（先出低码率可播）；接入节点故障主播自动重推到备用；CDN 故障切换多 CDN。
  8. **运维面**：转码队列积压与时长、单位分钟转码成本、CDN 命中率与出口带宽（最大成本）、播放 QoE 指标、直播端到端延迟；容量按热门事件（发布会 / 赛事）预扩。
- **易错点 / 面试官关注**：
  - 视频经应用服务器中转上传；不切分并行转码。
  - 不知道 ABR 与 HLS/DASH；直播和点播用同一套。
  - 忽略成本（CDN 带宽、转码）与 QoE 指标。
- **延伸**：Q11、Q17、Q26、[system-design/youtube/](../../system-design/youtube/)、[system-design/live-streaming-platform/](../../system-design/live-streaming-platform/)、[system-design/twitch/](../../system-design/twitch/)、[system-design/video-streaming/](../../system-design/video-streaming/)

---

### Q20. 设计打车 / 外卖的地理服务：位置更新、附近搜索、匹配调度与 ETA

- **难度**：🔴 高级
- **关键词**：Geohash, QuadTree, S2/H3, 位置更新 QPS, 附近查询, 匹配 dispatch, ETA, 地图路由, 状态机
- **概念速记**：
  - **Geohash**：把经纬度编码成字符串，前缀相同表示相近；用「同前缀 + 8 个邻居格」查附近，边界问题靠邻居格解决。
  - **QuadTree**：动态四叉树，密集区自动细分；适合内存索引静态 / 慢变对象（商家）。
  - **S2 / H3**：球面 / 六边形网格系统，格子面积均匀、层级可变，适合按格子聚合供需与做匹配。
- **问题**：设计 Uber 级平台：司机每 4s 上报位置（百万在线）、乘客查附近司机、下单后匹配、ETA 与路线、行程状态机，以及外卖场景的差异。
- **参考答案**：
  1. **位置上报**：1e6 / 4s = 250K 写/s；不进 DB，写内存网格索引（按 geohash / H3 格分片的 Redis GEO 或自研内存服务），保留最新一条 + TTL；历史轨迹异步写 Kafka → 冷存（计费 / 分析）。
  2. **附近查询**：乘客位置 → 目标格 + 邻居格 → 各格取候选司机 → 直线距离粗排 → 路网 ETA 精排 top-N；结果缓存几秒。
  3. **匹配（dispatch）**：按城市 / 区域分片的匹配服务，聚合一个短窗口（如 2–5s）的订单与空闲司机做批量匹配（二分图 / 贪心 + 权重：ETA、接单率、供需平衡），比逐单贪心更优；派单后司机接受 / 拒绝超时重派；锁司机状态防止双派（Q9 的锁或状态机 CAS）。
  4. **行程状态机**：requested → matched → arriving → in_trip → completed/cancelled；状态变更事件化（Kafka），下游计费 / 通知 / 分析消费；状态存强一致 DB（按 trip_id 分片）。
  5. **ETA 与路线**：路网图（分层 / 收缩层次 CH）+ 实时路况权重；ETA 用 ML 修正；结果缓存按 (起点格, 终点格, 时间段)。
  6. **供需与定价**：按 H3 格聚合供需比 → 动态定价；预测热区引导司机。
  7. **外卖差异**：三方（用户 / 商家 / 骑手）、出餐时间不确定 → 匹配要考虑取餐时间窗与顺路合并（多单并单）；商家菜单缓存与库存一致性。
  8. **运维面**：位置写入延迟与丢失率、附近查询 p99、匹配成功率与平均接驾时间、状态机卡单（stuck）监控与补偿任务；按城市隔离故障域，热点城市单独扩容。
- **易错点 / 面试官关注**：
  - 位置直接写关系库；附近查询用 `WHERE lat BETWEEN ...` 全表扫。
  - 不知道 geohash 边界问题与邻居格。
  - 匹配逐单贪心、没有防双派；状态机没有卡单补偿。
- **延伸**：Q9、Q13、[system-design/uber/](../../system-design/uber/)、[system-design/yelp/23-yelp-full-design.md](../../system-design/yelp/23-yelp-full-design.md)（附近搜索的静态版：地理索引 + 倒排索引 + 评分聚合 + 社区多边形，逐阶段口述答案与速答卡；面试中不要直接给候选人看）、[system-design/google-maps/](../../system-design/google-maps/)、[system-design/doordash/](../../system-design/doordash/)、[system-design/food-delivery/](../../system-design/food-delivery/)、[system-design/yelp/](../../system-design/yelp/)

---

### Q21. 设计票务 / 支付 / 秒杀系统：超卖、幂等、分布式事务与对账

- **难度**：🔴 高级
- **关键词**：库存扣减, 超卖, 幂等 idempotency key, 预留 / 释放, Saga / TCC, 出站箱 outbox, 对账 reconciliation, 排队 / 令牌
- **概念速记**：
  - **幂等键**：客户端为每次支付生成唯一 key，服务端用它去重，重试不会重复扣款。
  - **Saga**：把跨服务事务拆成本地事务序列 + 补偿操作；TCC 是 Try（预留）/ Confirm / Cancel 三段式。
  - **对账**：定期与第三方（支付渠道 / 银行）核对流水，发现单边账并修复——分布式支付系统的最终防线。
- **问题**：设计 Ticketmaster 级售票 + 支付：热门演出开售瞬间百万请求怎么扛、座位 / 库存怎么不超卖、下单支付跨服务怎么一致、支付渠道超时怎么办、怎么保证账目正确。
- **参考答案**：
  1. **削峰与公平**：开售前候车室（虚拟排队，令牌按序放行）+ 网关限流 + 静态页面 CDN；把「百万并发」变成「稳定的几千 QPS」进核心。
  2. **库存 / 座位**：座位状态机（available → held(TTL) → sold）；hold 用 Redis 原子操作（Lua）或 DB 行锁 / 乐观锁（`UPDATE ... WHERE status='available'` 影响行数 = 1）；hold 超时自动释放。热门场次按场次分片、避免单行热点（分桶库存）。
  3. **下单 → 支付流程**：订单服务创建订单（pending）→ 支付服务向渠道发起（带幂等键）→ 渠道回调 / 轮询 → 订单确认 → 库存 confirm。跨服务用 Saga：支付失败 / 超时 → 释放 hold、订单取消（补偿）。
  4. **事件一致性**：「写订单 + 发事件」用 outbox 表 + CDC，避免双写不一致；消费者幂等。
  5. **支付渠道**：超时不代表失败——必须查询渠道状态或等回调，不能直接重试发起；每笔用幂等键；回调验签、幂等处理、乱序处理（先到「成功」后到「处理中」要忽略）。
  6. **账务**：复式记账（每笔交易借贷平衡），账本只追加不改；日终 / 小时级对账（内部订单 vs 渠道流水 vs 账本），差异进人工队列。
  7. **安全**：不存卡号（PCI，用 token 化）、风控（限购、设备指纹）、防黄牛（验证码、实名）。
  8. **运维面**：下单成功率、支付成功率与渠道延迟、hold 释放积压、卡单（pending 超时）补偿任务、对账差异数；演练渠道全挂时的降级（改期支付 / 排队）。
- **易错点 / 面试官关注**：
  - `SELECT 再 UPDATE` 检查库存（竞态超卖）。
  - 支付超时直接重试或直接判失败。
  - 没有对账；不知道 outbox。
- **延伸**：Q3、Q9、Q10、[system-design/ticketmaster/](../../system-design/ticketmaster/)、[system-design/payment-system-hello-interview/](../../system-design/payment-system-hello-interview/)、[system-design/stock-exchange/](../../system-design/stock-exchange/)、[system-design/hotel-booking-system/](../../system-design/hotel-booking-system/)

---

### Q22. 设计协同文档（Google Docs）：OT 与 CRDT、实时同步、版本与权限

- **难度**：🔴 高级
- **关键词**：OT（操作变换）, CRDT, 实时协同, WebSocket, 版本历史, 快照 + 操作日志, 权限 ACL, 离线编辑
- **概念速记**：
  - **OT（Operational Transformation）**：所有操作经中心服务器排序，客户端收到并发操作时按变换函数调整自己的操作位置；实现简单但依赖中心。
  - **CRDT**：数据结构本身保证任意顺序合并后收敛（如序列 CRDT 给每个字符唯一位置 ID）；去中心、离线友好，但元数据开销与删除（墓碑）管理复杂。
- **问题**：设计支持百人同时编辑一篇文档、毫秒级同步、可离线、有版本历史与细粒度权限的协同文档系统。
- **参考答案**：
  1. **协同算法选择**：中心服务器架构 + OT（Google Docs 路线）：每篇文档一个「文档会话」进程做单点排序，操作 log 递增版本号；或 CRDT（Yjs / Automerge）适合离线优先与 P2P。面试说清取舍：OT 简单可控但会话是有状态单点，CRDT 无中心但内存与合并成本高。
  2. **实时通道**：WebSocket 网关（Q17）→ 按 `doc_id` 一致性哈希路由到持有该文档会话的节点（保证同文档同节点）；节点挂了从持久化的操作日志恢复会话。
  3. **存储**：操作日志（追加、按 doc 分片）+ 周期快照（每 N 个操作 / 分钟）；加载 = 最近快照 + 之后的操作重放；历史版本 = 任意快照 + 重放；冷文档快照放对象存储。
  4. **一致性与冲突**：客户端乐观应用本地操作、发送 `(baseVersion, op)`；服务端变换、广播 `(newVersion, op')`；客户端确认后清除待确认队列。光标 / 选区作为「感知」信息（presence）走独立低优通道，不持久化。
  5. **离线**：本地操作队列，重连后按服务端最新版本变换重放；冲突极端情况提示用户。
  6. **权限**：文档 / 文件夹 ACL（owner / editor / commenter / viewer），继承 + 显式；链接分享 token；操作级鉴权在会话节点检查；评论、建议模式是操作类型的扩展。
  7. **规模**：热文档（百人）会话节点 CPU 是瓶颈 → 合并广播（批量 / 节流 50ms）；冷文档会话空闲卸载。
  8. **运维面**：操作到广播延迟 p99、会话节点内存 / 文档数、快照落后量、恢复时间；发布时会话迁移（先冻结 → 快照 → 新节点接管）。
- **易错点 / 面试官关注**：
  - 用「最后写入覆盖」或整篇文档 diff 同步。
  - 说不出 OT 与 CRDT 各自的代价。
  - 不做快照，恢复要重放全部历史。
- **延伸**：Q17、[system-design/google-docs/](../../system-design/google-docs/)、[system-design/google-docs-system/](../../system-design/google-docs-system/)、[system-design/dropbox/](../../system-design/dropbox/)

---

### Q23. 设计分布式网络爬虫：URL 前沿、去重、礼貌性、内容存储与增量抓取

- **难度**：🟡 中级
- **关键词**：URL frontier, 优先级与礼貌 politeness, robots.txt, 去重 布隆过滤器, DNS 缓存, 内容指纹 SimHash, 增量抓取, 陷阱 spider trap
- **概念速记**：
  - **URL frontier**：待抓取队列，同时实现优先级（重要 / 更新快的先抓）与礼貌性（同一域名限速、串行）。
  - **SimHash**：近似重复内容检测，海明距离小即相似页，避免存重复内容。
- **问题**：设计一个每月抓 10 亿页的爬虫：架构、frontier 怎么做到优先级 + 礼貌、URL 与内容怎么去重、怎么处理陷阱与动态页、怎么增量更新、怎么扩展与监控。
- **参考答案**：
  1. **估算**：1e9 / 30 天 ≈ 400 页/s；每页 ~500KB（HTML + 资源）→ 200MB/s 入口带宽、每月 500TB 存储（压缩后 ~100TB）。
  2. **架构**：种子 → frontier → 抓取 worker（DNS 缓存、HTTP 客户端、超时）→ 内容处理（解析、去重、提取链接）→ 存储（对象存储 + 元数据索引）→ 新 URL 过滤（规范化、去重、robots）→ 回 frontier。
  3. **Frontier**：两级队列：前队列按优先级（PageRank / 更新频率 / 业务权重），后队列按域名（每域名一个 FIFO，worker 按域名的「下次可抓时间」取），保证同域名串行且间隔 ≥ 礼貌间隔；持久化在磁盘 / Kafka，避免全放内存。
  4. **去重**：URL 规范化（大小写、参数排序、去 fragment）→ 布隆过滤器（内存）+ 持久化 KV 兜底假阳性；内容用 SimHash 检测近重复。
  5. **礼貌与合规**：遵守 robots.txt（缓存）、`Crawl-delay`、限制每域名并发；UA 标识；避免抓登录后内容。
  6. **陷阱与质量**：URL 长度 / 深度上限、同域名页数上限、日历 / 无限分页识别；动态页用无头浏览器池（成本高，按需）。
  7. **增量抓取**：按历史变更频率估计重抓周期（自适应），用 `ETag / Last-Modified` 条件请求节省带宽。
  8. **扩展与运维**：worker 无状态水平扩展，frontier 按域名哈希分片；监控抓取速率、成功率、每域名错误率（被封）、frontier 深度、存储增长；IP 池与代理健康。
- **易错点 / 面试官关注**：
  - Frontier 只有一个全局队列（无礼貌性，会被封）。
  - 去重只用内存 set；不做 URL 规范化。
  - 不遵守 robots / 无陷阱防护。
- **延伸**：Q13、Q26、[system-design/web-crawler-system/](../../system-design/web-crawler-system/)、[system-design/webcrawler/](../../system-design/webcrawler/)、[system-design/crawler/](../../system-design/crawler/)

---
## 四、运维与基础设施系统（SRE 岗位重点）

### Q24. 设计一个分布式监控系统（Datadog / Prometheus 级）：采集、存储、告警与高基数治理

- **难度**：🔴 高级
- **关键词**：pull vs push, 服务发现, 采集网关, 指标存储（Q14）, 告警规则评估, 去重 / 抑制 / 静默, 高基数, 多租户
- **概念速记**：
  - **Pull（Prometheus）**：服务端按服务发现列表定期抓取 `/metrics`；天然知道「目标不可达」，但跨网络 / 短生命周期任务不便。**Push（StatsD / OTLP）**：客户端主动上报，适合 serverless / 批任务，需要网关承接与背压。
  - **告警去重 / 抑制 / 静默**：同一告警多副本评估只发一次；上游故障时抑制下游派生告警；维护期静默。
- **问题**：为一家 10 万主机 + 5 万服务实例的公司设计监控平台：采集模型、存储（引用 Q14）、告警评估与通知、仪表盘查询、多租户隔离、自身高可用与「监控监控」。
- **参考答案**：
  1. **采集**：主机与 K8s 用 pull（agent 暴露 + 服务发现），批任务 / 边缘用 push 到采集网关（带鉴权、限流、背压）；统一 OpenTelemetry 协议；采集器分片（按目标哈希）+ 每分片双副本（HA pair）。
  2. **存储**：Q14 的 TSDB 架构（ingester → block → 对象存储 + 降采样）；多租户按租户隔离 series 上限与查询配额。
  3. **告警评估**：规则按租户 / 分组分片到评估器，周期性执行 PromQL；`for` 持续时间避免抖动；评估器多副本 + Alertmanager 集群（gossip）去重；路由树按 label 分发（团队 / 严重级），分级通知（IM → 电话升级），抑制与静默。
  4. **查询与仪表盘**：查询前端做拆分 / 缓存 / 限流；仪表盘用录制规则（recording rules）预聚合重查询；慢查询保护（超时、series 上限）。
  5. **高基数治理**：写入侧 relabel、租户配额、cardinality 分析工具、按 metric 名 top-N 报表；教育与审批。
  6. **日志 / 链路衔接**：指标异常 → exemplar 跳到 trace → 关联日志（同一 trace_id）；三者共享资源标签（service / env / version）。
  7. **自身高可用与「谁监控监控」**：采集器 / 评估器 / 存储跨 AZ 多副本；用一套独立的最小监控（外部探活 + 死信通道）盯监控系统本身；告警通道多路（IM 挂了走短信 / 电话）。
  8. **运维面 / SLO**：采集成功率、数据新鲜度（scrape 到可查延迟 < 1 min）、告警投递延迟、查询 p99；容量按 series 与 QPS 规划；变更（规则 / 采集配置）走 GitOps + 校验 + 灰度。
- **易错点 / 面试官关注**：
  - 只讲 Prometheus 单机；说不出 pull/push 各自适用场景。
  - 告警没有去重 / 抑制 / 分级；不知道 `for`。
  - 没回答「监控系统自己挂了怎么知道」。
- **延伸**：Q14、Q25、[observability/observability-questions.md](../observability/observability-questions.md)、[system-design/monitoring-system/](../../system-design/monitoring-system/)、[system-design/distributed-monitoring/](../../system-design/distributed-monitoring/)、[system-design/metrics-monitoring-hello-interview/](../../system-design/metrics-monitoring-hello-interview/)、[system-design/distributed-monitoring-system-design-guide.md](../../system-design/distributed-monitoring-system-design-guide.md)

---

### Q25. 设计分布式日志系统（ELK / Loki 级）：采集、传输、索引策略、保留与成本

- **难度**：🔴 高级
- **关键词**：日志采集 agent, 缓冲与背压, Kafka 缓冲层, 全文索引 vs 标签索引, 冷热分层, 保留策略, 采样, PII 脱敏
- **概念速记**：
  - **全文索引（Elasticsearch）**：每条日志所有字段建倒排索引，查询灵活但写入与存储成本高。**标签索引（Loki）**：只索引少量标签，内容压缩存对象存储，查询时暴力扫描相关块——便宜、写快、复杂查询慢。
  - **背压**：下游慢时向上游传递压力（缓冲 → 限速 → 丢弃低优），避免采集 agent 把应用磁盘写满或 OOM。
- **问题**：设计每天 100TB 日志、保留 30 天热 + 1 年冷、支持秒级检索与告警的日志平台：采集、缓冲、处理、索引、存储、查询、多租户与成本。
- **参考答案**：
  1. **采集**：节点级 agent（Fluent Bit / Vector / Filebeat）读文件 / stdout，附加元数据（pod、service、env），本地磁盘缓冲，批量压缩发送；应用侧结构化 JSON 输出，禁止同步远程写日志。
  2. **缓冲层**：Kafka 按租户 / 来源分 topic，吸收峰值（部署风暴、故障刷日志）、解耦下游维护；保留几小时到一天。
  3. **处理**：流式解析 / 富化 / 脱敏（PII、密钥）/ 采样（debug 级按比例、错误全量）/ 路由（安全日志单独走）；处理器无状态可扩。
  4. **索引与存储**：两条路线择一或混合——(a) ES：按天 / 租户建索引，ILM 热（SSD）→ 温 → 冷（对象存储 searchable snapshot），控制 shard 大小（20–50GB）与数量；(b) Loki 模式：标签索引 + 压缩块进对象存储，成本低 5–10×，适合「按 service / pod 拉日志再 grep」的运维场景。100TB/天规模下多用 (b) 或 (a) 只索引关键字段。
  5. **查询**：查询网关限时限量、按时间分片并行、结果缓存；常用查询固化成告警规则（如错误率）与仪表盘；关联 trace_id 跳转。
  6. **告警**：流式规则（如 5 分钟内 ERROR > N）在处理层评估，或定时查询；输出到 Q24 的告警路由。
  7. **多租户与治理**：配额（写入速率、保留天数、查询并发）、按租户计费 / 展示成本、日志量 top-N 推动业务降噪。
  8. **运维面**：端到端延迟（产生到可查 < 30s）、丢失率、Kafka lag、索引 / 压缩积压、存储成本 / GB；容量按日志量增长率与保留期规划；agent 发布要灰度（它跑在所有节点上）。
- **易错点 / 面试官关注**：
  - 全量全文索引且不分层，不知道成本量级。
  - 没有缓冲层，故障刷日志时把整条链打挂。
  - 忽略脱敏与多租户配额。
- **延伸**：Q10、Q24、[observability/observability-questions.md](../observability/observability-questions.md)、[system-design/distributed-logging/](../../system-design/distributed-logging/)、[system-design/distribute-logs/](../../system-design/distribute-logs/)、[system-design/README-Distributed-Logging-Docs.md](../../system-design/README-Distributed-Logging-Docs.md)

---

### Q26. 设计分布式任务调度器（cron / DAG 工作流）：触发精度、去重、失败重试与工作流依赖

- **难度**：🔴 高级
- **关键词**：分布式 cron, 时间轮 / 延迟队列, 领导选举, 至少一次触发, 幂等执行, DAG 依赖, 重试与退避, 优先级与资源配额
- **概念速记**：
  - **触发 vs 执行分离**：调度器只负责「到点把任务放进队列」，worker 负责执行；两者独立扩展与故障域隔离。
  - **至少一次触发 + 幂等执行**：调度器故障切换可能重复触发同一次运行，用 `(job_id, scheduled_time)` 作为运行的唯一键去重。
  - **DAG**：任务间依赖构成有向无环图；调度器按拓扑顺序在上游成功后触发下游。
- **问题**：设计一个支持 100 万个定时任务、每秒万级触发、支持工作流依赖、失败重试、优先级与多租户配额的调度平台；说清调度器怎么高可用、怎么保证不漏触发不重复执行。
- **参考答案**：
  1. **数据模型**：`job`（cron 表达式 / 一次性时间、owner、重试策略、超时、优先级、资源需求）、`run`（每次触发实例，状态机 scheduled → queued → running → succeeded/failed/timeout）、`dag`（边）。
  2. **触发**：把「下次触发时间」写进按时间分片的索引（DB 索引或 Redis ZSET 按分钟桶）；调度器每秒扫描到期桶（或时间轮）→ 创建 run（唯一键去重）→ 投入优先级队列。分片：按 job_id 哈希把任务分到多个调度器分片，每分片 leader（etcd / ZK 租约选举）+ standby；leader 切换后按「上次扫描水位」补扫，保证不漏（可能重）。
  3. **执行**：worker 池按队列拉取（长轮询），执行前写 `running` + 心跳续租；超时 / 心跳丢失则 run 判失败并按策略重试（指数退避、最大次数）；worker 无状态可扩，按资源标签（GPU / 内存）路由。
  4. **幂等**：run 唯一键；任务体本身幂等（写结果带 run_id、外部副作用去重）；重复触发的第二次 run 创建失败即丢弃。
  5. **DAG**：上游 run 成功事件 → 检查下游所有入边完成 → 触发下游；失败策略（跳过 / 阻塞 / 部分重跑）；回填（backfill）按时间区间批量生成 run；避免长链在一个事务里更新，用事件驱动。
  6. **优先级与配额**：多级队列 + 租户配额（并发上限、每日 run 数）；防饥饿（低优等待时间加权提升）。
  7. **规模**：100 万 job 的「下次触发」索引很小（几百 MB），瓶颈在触发峰值（整点 / 每分钟 0 秒）→ 抖动（jitter）打散、桶内并行扫描。
  8. **运维面**：触发延迟（计划时间到实际入队）、队列积压、失败率与重试率、卡在 running 的 run、调度器 leader 切换次数；变更 cron 表达式要校验；提供 run 日志与可观测链接。
- **易错点 / 面试官关注**：
  - 单点调度器；用 sleep 轮询全表。
  - 不区分触发与执行；没有 run 唯一键。
  - DAG 的失败语义与回填没考虑。
- **延伸**：Q9、Q10、Q19、[system-design/distributed-job-scheduler/](../../system-design/distributed-job-scheduler/)、[system-design/task-scheduler/](../../system-design/task-scheduler/)、[system-design/distributed-task-scheduler-zookeeper/](../../system-design/distributed-task-scheduler-zookeeper/)、[system-design/job-scheduler-system/](../../system-design/job-scheduler-system/)

---

### Q27. 设计大规模代码发布 / 部署系统：制品分发、分批灰度、健康判定与回滚

- **难度**：🔴 高级
- **关键词**：制品仓库, P2P 分发, 分批发布 canary, 健康判定 / 自动回滚, 配置与代码分离, 审批与变更窗口, 万台机器 / 断网边缘
- **概念速记**：
  - **制品（artifact）**：构建产物（镜像 / 二进制 / 包）以内容哈希唯一标识，不可变；「发布」= 把某哈希推到某环境的某批机器。
  - **分批 + 健康判定**：1% → 10% → 50% → 100%，每批后按 SLI（错误率 / 延迟 / 崩溃）自动判定，不达标自动回滚到上一个哈希。
- **问题**：设计支撑上千个服务、每天万次发布、单服务上万实例的发布系统；再扩展到「几十万台断续联网的边缘机器（如月球基地 / 门店）」场景。
- **参考答案**：
  1. **架构**：CI 产出制品 → 制品仓库（内容寻址、签名、漏洞扫描）→ 发布控制面（发布单、策略、审批、状态机）→ 分发层（区域镜像仓库 + P2P / CDN 把大制品推到万台机器，避免中心带宽瓶颈）→ 节点 agent（拉取、校验签名、切换、上报健康）。
  2. **发布策略**：蓝绿 / 金丝雀 / 滚动；按 AZ / 分片 / 权重分批；每批之间「烘焙时间」+ 自动分析（对比基线的错误率、p99、资源）；不通过自动回滚；配置变更走同一套流程与灰度（配置是最常见的故障源）。
  3. **切换与回滚**：节点保留上一个版本目录（原子 symlink 切换 / 镜像标签），回滚 = 切回上一哈希，秒级；数据库迁移向前兼容（先加不删，expand/contract），让回滚不受 schema 阻塞。
  4. **一致性与可靠性**：发布状态机持久化，控制面无状态多副本；agent 幂等（目标版本声明式，agent 收敛到目标）；控制面挂了不影响运行中服务、agent 缓存最后目标。
  5. **治理**：变更窗口与冻结期、审批（高风险自动升级审批）、发布与告警 / 事故关联（「最近谁发布了什么」是排障第一问）、审计。
  6. **边缘 / 断网扩展**：目标版本作为「期望状态」下发到区域网关，边缘节点上线时拉取；制品预置 + 差分更新（delta）省带宽；本地健康判定 + 本地自动回滚（不依赖中心）；分区域波次（先内测门店 → 区域 → 全量）；上报汇聚到中心做全局进度与异常检测；容忍长时间失联（幂等 + 版本向量）。
  7. **运维面 / SLO**：发布成功率、平均发布时长、回滚率与回滚耗时、分发带宽与命中率、agent 在线率；发布系统自身的发布要最保守。
- **易错点 / 面试官关注**：
  - 「全量重启」；没有自动健康判定与回滚。
  - 配置改动绕过发布系统。
  - 数据库迁移不向前兼容导致无法回滚。
- **延伸**：Q12、Q28、[cicd-iac/cicd-iac-questions.md](../cicd-iac/cicd-iac-questions.md)、[system-design/code-deployment/](../../system-design/code-deployment/)、[system-design/moon-machine-upgrade/](../../system-design/moon-machine-upgrade/)、[system-design/upgrade/](../../system-design/upgrade/)

---

### Q28. 设计容灾与多活架构：RPO/RTO、数据复制、流量切换与演练

- **难度**：🔴 高级
- **关键词**：RPO / RTO, 冷备 / 温备 / 热备, 同城双活 / 异地多活, 单元化 cell, 数据复制（同步 / 异步）, 流量调度 GSLB, 脑裂, 故障演练
- **概念速记**：
  - **RPO**（最多丢多少数据）由复制方式决定：同步复制 RPO≈0，异步复制 RPO = 复制延迟。**RTO**（多久恢复）由切换自动化程度决定。
  - **单元化（cell / set 架构）**：按用户维度把整套服务 + 数据切成自包含单元，单元内闭环、单元间不依赖；故障与容量按单元隔离。
- **问题**：为一个支付级核心系统设计 RPO≈0、RTO < 1 min 的容灾方案，并说明与「异地多活」的区别与代价；怎么避免脑裂；怎么验证方案真的有效。
- **参考答案**：
  1. **先定目标再选架构**：RPO≈0 + RTO<1min → 至少同城双活（同步复制可接受的 RTT < 2ms）+ 异地热备（异步，RPO 秒级）；「两地三中心」是这个目标的经典解。
  2. **数据层**：核心库跨机房同步 / 半同步复制（多数派，如 3 AZ 的 Raft / Paxos 型数据库）；异地异步复制；缓存与队列按机房独立 + 双写或重建；对象存储跨区域复制。
  3. **应用层**：无状态多机房部署；依赖（配置中心、注册中心、ID 服务）每机房自治或多数派跨机房。
  4. **流量切换**：GSLB / DNS + 网关权重；切换步骤自动化（剧本化）：冻结写 → 确认复制追平 → 提升新主 → 切流 → 验证；DNS TTL 要短且客户端要能重解析。
  5. **异地多活的区别**：多活 = 各地都承接写流量 → 必须解决跨地域写冲突，通常靠**单元化按用户分片写**（每个用户的写只在归属单元），跨单元数据异步同步 + 冲突规避（而非冲突解决）；代价：跨单元事务 / 全局唯一约束 / 全局查询变难，改造成本极高，只有可用性 ≥ 99.99% 且规模足够大才值得。
  6. **脑裂**：多数派仲裁（第三机房 / 见证节点）、租约 + fencing（Q9）、切换必须由单一控制面执行且带全局锁；「双主同时写」是最坏结果，宁可短暂不可写。
  7. **验证**：定期演练（计划内切换、断网注入、机房断电）并测量真实 RPO/RTO；混沌工程持续验证依赖闭环；演练结果作为 SLO 报告的一部分；备份 + 恢复演练单独做（容灾不等于备份，逻辑损坏要靠备份）。
  8. **成本**：冗余容量（每机房要能扛全量或 N-1）、跨地域带宽、复杂度；按业务分级（核心链路多活、非核心冷备）。
- **易错点 / 面试官关注**：
  - 把 RPO/RTO 说成同一个东西；不知道同步复制的 RTT 约束。
  - 「多活」= 多机房都部署（其实是双活读 + 单写）。
  - 没有演练与切换剧本，方案只存在于 PPT。
- **延伸**：Q3、Q4、Q27、[sre-reliability/sre-questions.md](../sre-reliability/sre-questions.md)、[system-design/disaster-recovery-system-design/](../../system-design/disaster-recovery-system-design/)、[system-design/kubernetes-disaster-recovery.md](../../system-design/kubernetes-disaster-recovery.md)、[system-design/replicated-sites/](../../system-design/replicated-sites/)

---

### Q29. 设计一个容器编排系统（自己造一个 Kubernetes）：状态存储、调度器、控制循环与节点代理

- **难度**：🔴 高级
- **关键词**：声明式 API, 期望状态 vs 实际状态, 控制循环 reconcile, 调度器 filter/score, 节点代理 kubelet, 服务发现, 水平扩缩, 多租户隔离
- **概念速记**：
  - **声明式 + 控制循环**：用户提交期望状态（3 个副本），控制器持续比较实际状态并采取动作收敛；所有组件通过状态存储通信，而非互相调用。
  - **两阶段调度**：过滤（资源、亲和、污点）得可行节点集 → 打分（打散 / 装箱 / 亲和）选最优；调度器只写「绑定」，不直接启动容器。
- **问题**：请从零设计一个跨 5000 节点的容器编排系统：API 与存储、调度、控制器、节点代理、网络与服务发现、扩缩容、故障处理；并说明哪些设计决定了它能扩到 5000 节点。
- **参考答案**：
  1. **API 与状态存储**：REST/gRPC API 服务器做认证 / 鉴权 / 校验 / 准入；对象存到强一致 KV（Raft，如 etcd），支持 watch（增量事件流）与乐观并发（resourceVersion）；对象带 spec（期望）/ status（实际）。
  2. **控制器**：每类对象一个控制循环（ReplicaSet 控制副本数、Deployment 控制滚动、Node 控制器处理节点失联、Endpoint 控制器维护服务后端）；通过 informer（本地缓存 + watch）减少 API 压力；幂等、可重入、level-triggered（不依赖不丢事件）。
  3. **调度器**：watch 未绑定 Pod → 过滤（资源、端口、亲和 / 反亲和、污点容忍、拓扑）→ 打分 → 绑定；用抢占处理高优先级；批量 / 并行调度提升吞吐；GPU 等扩展资源用插件（对应 DRA）。
  4. **节点代理**：watch 分配给本节点的 Pod → 调运行时（CRI）拉镜像、建 sandbox、启容器 → 探针 → 上报状态与心跳；节点资源预留、驱逐策略（内存压力）。
  5. **网络与服务发现**：每 Pod 一 IP（CNI），服务 = 虚拟 IP + 后端列表（每节点代理维护 iptables/IPVS/eBPF 规则），DNS 名到服务 IP；入口层（Ingress / Gateway）。
  6. **扩缩容**：HPA 按指标调副本、集群自动扩缩按待调度 Pod 增减节点；PDB 保护滚动时的最小可用。
  7. **故障处理**：节点失联 → 超时后标记不可达 → 驱逐 / 重建（有状态工作负载需要 fencing 防止双写）；控制面多副本（API 无状态、etcd 3/5 节点、控制器 / 调度器 leader 选举）。
  8. **可扩展性来源**：状态存储只存元数据不走数据面、watch 增量而非轮询、informer 缓存、控制器分片、API 限流与优先级（APF）、节点心跳降频（lease 对象）、etcd 单集群规模上限决定单集群 ~5000 节点——再大就多集群联邦。
  9. **多租户**：命名空间 + 配额 + 网络策略 + RBAC + 准入策略；强隔离用 gVisor / Kata 或独立集群。
  10. **运维面**：API 延迟、etcd 提交延迟 / 大小、调度延迟与待调度队列、控制器 workqueue 深度、节点 NotReady 数；升级要先控制面后节点、版本偏差规则。
- **易错点 / 面试官关注**：
  - 设计成「中心直接命令节点」而非声明式 + 控制循环。
  - 调度器直接启动容器；不知道 watch / informer 为什么重要。
  - 说不出规模瓶颈在 etcd 与 watch 扇出。
- **延伸**：[kubernetes/kubernetes-questions.md](../kubernetes/kubernetes-questions.md)、[system-design/container-orchestration-system-design/](../../system-design/container-orchestration-system-design/)、[system-design/kubernetes-operator-system/](../../system-design/kubernetes-operator-system/)、[system-design/dynamic-kubernetes-scaling/](../../system-design/dynamic-kubernetes-scaling/)

---

### Q30. 设计会话管理与认证授权系统：Session vs JWT、SSO、令牌撤销与 RBAC

- **难度**：🟡 中级
- **关键词**：Session 存储, JWT, 刷新令牌 refresh token, 撤销 / 黑名单, OAuth2 / OIDC, SSO, RBAC / ABAC, 多设备
- **概念速记**：
  - **服务端 Session**：状态存服务端（Redis），Cookie 只放 session id；可随时撤销，但每请求查一次存储。**JWT**：状态自包含 + 签名，无需查存储；撤销困难（只能等过期或维护黑名单）。
  - **OIDC**：在 OAuth2 之上的身份层，返回 ID Token；SSO 靠身份提供方（IdP）统一登录并向各应用签发令牌。
- **问题**：设计一个支撑 1 亿用户、多端登录、支持 SSO、能秒级踢下线、有细粒度权限的认证与会话系统。
- **参考答案**：
  1. **令牌模型**：短期访问令牌（JWT，5–15 min，无状态校验）+ 长期刷新令牌（不透明、存服务端、可撤销、绑定设备）；刷新令牌轮换（每次刷新换新，旧的重用即视为泄露、撤销整个会话族）。
  2. **会话存储**：Redis 集群按 user_id 分片，`session_id → {user, device, issued, scopes}`；用户 → 会话列表用于「查看 / 踢出设备」；TTL 与滑动过期。
  3. **秒级撤销**：访问令牌短期 + 网关维护撤销列表（用户级 `not_before` 时间戳广播到网关缓存 / 发布订阅），比逐 token 黑名单便宜；高敏操作（改密、支付）强制回源校验。
  4. **认证与 SSO**：IdP（OIDC）+ 授权码 + PKCE；应用只信任 IdP 签发的令牌；密钥轮换用 JWKS + kid；社交登录作为外部 IdP 联合。
  5. **授权**：RBAC（角色 → 权限）满足多数场景；资源级 / 属性级用 ABAC 或策略引擎（OPA / Zanzibar 风格关系元组，适合共享文档类）；授权决策缓存 + 变更推送。
  6. **安全**：Cookie `HttpOnly/Secure/SameSite`、CSRF token、登录限速与风控（设备指纹、异地）、MFA、密码哈希（Argon2/bcrypt）、令牌不落日志。
  7. **规模**：认证 QPS 高但可缓存（JWKS、撤销位）；Redis 会话按活跃用户估算（1e8 × 平均 3 设备 × 300B ≈ 90GB）；多机房会话就近读、写主复制或按用户归属单元。
  8. **运维面**：登录成功率 / 延迟、令牌校验失败率、Redis 命中与延迟、密钥轮换成功、异常登录告警；IdP 是全站单点，需多副本 + 降级（短时允许仅本地校验）。
- **易错点 / 面试官关注**：
  - JWT 放长期不可撤销；刷新令牌不轮换。
  - 把权限塞进 JWT 后无法即时变更。
  - 忽略 CSRF / Cookie 属性 / 密钥轮换。
- **延伸**：Q12、[cloud-security/cloud-security-questions.md](../cloud-security/cloud-security-questions.md)、[system-design/session-management-system/](../../system-design/session-management-system/)、[system-design/scalable-session-management/](../../system-design/scalable-session-management/)、[system-design/rbac/](../../system-design/rbac/)

---

## 五、AI / ML 系统设计

### Q31. 设计 RAG（检索增强生成）系统：切分、向量检索、混合检索、评测与成本

- **难度**：🔴 高级
- **关键词**：分块 chunking, 嵌入 embedding, 向量索引 HNSW / IVF, 混合检索 BM25 + 向量, 重排 rerank, 引用溯源, 评测 RAGAS, 缓存与成本
- **概念速记**：
  - **RAG**：用检索把外部知识注入提示词，让 LLM 基于证据回答；质量 = 检索质量 × 生成质量，检索先于模型。
  - **HNSW**：分层近邻图索引，查询 O(log n)，内存驻留；**IVF-PQ**：聚类 + 乘积量化压缩，内存小、精度略降。
  - **混合检索**：关键词（BM25）抓精确术语，向量抓语义，RRF 融合后 rerank。
- **问题**：为企业知识库（1000 万文档、日更、多租户、需引用来源）设计 RAG 平台：摄取流水线、索引、检索、生成、评测、权限与成本。
- **参考答案**：
  1. **摄取**：文档源 → 解析（PDF / HTML / 表格）→ 清洗 → 分块（按结构 / 语义，200–800 token，带重叠与父块引用）→ 嵌入（批量、GPU）→ 写向量库 + 关键词索引 + 元数据（租户、ACL、版本）；增量更新用文档版本与删除墓碑；流水线用 Q26 的调度 + 幂等。
  2. **索引**：向量库按租户 / 集合分片，HNSW 内存驻留（1e7 × 1536 维 × 4B ≈ 60GB → 量化或分片）；元数据过滤（租户 / ACL）要在索引内做 pre-filter，否则召回被过滤后不足。
  3. **检索**：查询改写（多查询、HyDE）→ 混合召回（各 top-50）→ RRF 融合 → cross-encoder 重排 top-5–10 → 组装上下文（去重、按父块扩展、引用编号）。
  4. **生成**：提示模板要求「只依据证据、无证据则说不知道、逐句引用」；流式输出；输出后置校验（引用是否存在、PII）。
  5. **权限**：检索时按用户 ACL 过滤（不是生成后过滤），文档 ACL 变更要同步到索引元数据。
  6. **评测**：离线金标集（问题 / 证据 / 答案）测召回率@k、忠实度、答案相关性（RAGAS 类指标）；线上用户反馈 + LLM-judge 抽样；每次改分块 / 模型 / 提示都跑回归。
  7. **成本与延迟**：嵌入与 rerank 走小模型 / 自托管；查询与答案缓存（语义缓存）；上下文长度控制 token 成本；p95 延迟目标（检索 < 200ms，首 token < 1s）。
  8. **运维面**：索引新鲜度（文档更新到可检索延迟）、召回率漂移、幻觉率、每问成本、向量库内存与 QPS；模型 / 嵌入版本升级需全量重嵌入（灰度双索引）。
- **易错点 / 面试官关注**：
  - 只有向量检索没有关键词与 rerank；分块无策略。
  - 权限在生成后过滤（泄露）。
  - 没有评测体系，改动靠感觉。
- **延伸**：Q13、Q32、[gpu-ai/gpu-ai-questions.md](../gpu-ai/gpu-ai-questions.md)、[system-design/rag-system/](../../system-design/rag-system/)、[system-design/rag-retrieval-platform/](../../system-design/rag-retrieval-platform/)、[system-design/vectordb/](../../system-design/vectordb/)、[system-design/embedding-retrieval/](../../system-design/embedding-retrieval/)

---

### Q32. 设计 LLM 推理服务平台（ChatGPT 级）：批处理、KV Cache、路由、多租户与成本

- **难度**：🔴 高级
- **关键词**：连续批处理 continuous batching, KV cache, PagedAttention, 预填充 / 解码分离, 模型路由, 流式 SSE, 配额与优先级, GPU 利用率, 资源估算
- **概念速记**：
  - **Prefill / Decode**：prefill 处理整个提示词（计算密集、并行），decode 逐 token 生成（内存带宽密集、串行）；两阶段特性不同，可分离部署。
  - **KV cache**：每个 token 的注意力键值缓存，显存占用 = 层数 × 2 × 隐维 × 序列长 × 精度；PagedAttention 把它分页管理消除碎片。
  - **连续批处理**：新请求随时插入正在解码的 batch，替代「等整批完成」，吞吐提升数倍。
- **问题**：设计一个服务百万 DAU 的对话 LLM 平台：请求路径、推理引擎关键优化、如何估算 GPU 数量、多模型 / 多租户路由、流式与超时、成本与可观测。
- **参考答案**：
  1. **请求路径**：网关（鉴权、配额、内容安全）→ 会话服务（历史、摘要、上下文裁剪）→ 路由（按模型 / 租户 / 优先级 / 负载选择推理池）→ 推理引擎（vLLM / TensorRT-LLM 类）→ 流式 SSE 返回；异步安全审核并行。
  2. **推理引擎优化**：连续批处理、PagedAttention、前缀缓存（系统提示词共享 KV）、量化（INT8/FP8）、投机解码；prefill 与 decode 分离到不同实例减少互相干扰；张量并行跨 GPU 放大模型。
  3. **资源估算**（面试必答）：70B 模型 FP16 权重 140GB → 至少 2×80GB 卡（TP=2），KV cache 每 token ~ 2×80 层×8192 维×2B ≈ 2.6MB（分组查询注意力可降）；每卡剩余显存决定并发序列数；按「峰值并发会话 × 平均序列长」推显存，按「目标 tokens/s ÷ 单实例吞吐」推实例数，再加 30% 冗余。
  4. **路由与多租户**：按 SLA 分池（付费 / 免费）、队列优先级与配额（tokens/min）、超载时排队或降级到小模型；长上下文请求单独池以免拖慢 batch。
  5. **流式与超时**：首 token 延迟（TTFT）与每 token 延迟（TPOT）双 SLO；客户端断开要取消生成释放 KV；最大输出 token 限制。
  6. **成本**：GPU 利用率是核心指标（目标 > 60%）；缓存（前缀 / 语义）、小模型路由、批大小调优、抢占式实例做离线任务；按 token 计量计费。
  7. **发布与安全**：模型版本灰度（影子流量、A/B 评测）、回滚；提示注入与输出过滤；PII 处理。
  8. **运维面**：TTFT / TPOT p99、吞吐 tokens/s、GPU 利用率与显存、队列等待、拒绝率、每千 token 成本；GPU 故障（XID）自动摘除；容量按峰值与模型升级提前采购（交付周期长）。
- **易错点 / 面试官关注**：
  - 把 LLM 当普通无状态 HTTP 服务，不知道 KV cache 与批处理。
  - 估算不出 GPU 数量。
  - 没有 TTFT/TPOT 两类延迟指标与取消机制。
- **延伸**：Q31、[gpu-ai/gpu-ai-questions.md](../gpu-ai/gpu-ai-questions.md)、[system-design/chatgpt-system-design/](../../system-design/chatgpt-system-design/)、[system-design/inference-optimization/](../../system-design/inference-optimization/)、[system-design/genai-resource-estimation/](../../system-design/genai-resource-estimation/)、[system-design/llm-customer-support-bot/](../../system-design/llm-customer-support-bot/)

---

### Q33. 设计推荐系统（视频 / 广告 / 信息流）：召回 → 粗排 → 精排 → 重排，特征与在线离线一致性

- **难度**：🔴 高级
- **关键词**：召回 recall, 排序 ranking, 特征存储 feature store, 在线 / 离线一致性, 实时特征, 模型服务, A/B 实验, 冷启动
- **概念速记**：
  - **漏斗**：从亿级候选 → 召回几千（多路：协同过滤、向量、热门、关注）→ 粗排几百（轻模型）→ 精排几十（重模型、多目标）→ 重排（多样性、业务规则）。
  - **特征存储**：离线（批计算、训练）与在线（低延迟 KV，推理）两套存储共享同一特征定义，避免训练 / 服务偏差。
- **问题**：设计一个短视频推荐系统：请求路径与延迟预算（< 200ms）、多路召回、模型服务、特征怎么保证在线离线一致、实时反馈怎么进模型、A/B 与冷启动、以及平台的运维与成本。
- **参考答案**：
  1. **请求路径**：客户端 → 推荐网关（用户画像与上下文）→ 并行多路召回（向量 ANN、协同过滤、热门 / 地域、关注、探索）→ 合并去重 → 粗排（双塔 / 轻 GBDT）→ 精排（多任务 DNN：完播、点赞、分享）→ 重排（多样性、去重、广告插入、新内容配额）→ 返回 + 埋点。延迟预算：召回 50ms、粗排 30ms、精排 80ms、其余 40ms。
  2. **特征**：用户特征（画像、近期行为序列）、物品特征（内容嵌入、统计量）、上下文（时间、设备）；离线由批作业生成到仓库，在线由流式作业（Flink）实时更新到 KV（Redis / 自研）；**同一份特征定义代码离线 / 在线共用**（feature store），并记录服务时的特征快照用于训练（避免时间穿越）。
  3. **模型服务**：模型注册 / 版本、GPU/CPU 推理集群、批量打分、模型热更新；嵌入索引（ANN，HNSW）周期重建 + 增量。
  4. **实时反馈**：曝光 / 点击 / 完播事件 → Kafka → 流式更新用户短期兴趣特征（分钟级）→ 在线学习或小时级增量训练。
  5. **冷启动**：新用户用上下文 + 热门 + 探索（bandit）；新内容强制曝光配额 + 内容理解嵌入。
  6. **实验**：分层正交的 A/B 平台，流量按用户哈希分桶，指标（留存、时长、多样性）+ 护栏（负反馈、延迟）；灰度上线模型。
  7. **运维面**：各阶段 p99 与超时降级（精排超时用粗排结果）、召回空结果率、特征缺失率、模型新鲜度、GPU 利用率、A/B 指标异常；成本大头在精排推理与特征存储，靠缓存与蒸馏控制。
- **易错点 / 面试官关注**：
  - 只有一个模型直接对全量打分；没有漏斗与延迟预算。
  - 不知道训练 / 服务偏差与时间穿越。
  - 没有降级路径（模型挂了给热门）。
- **延伸**：Q16、Q31、[system-design/recommendation/](../../system-design/recommendation/)、[system-design/video-recommendation/](../../system-design/video-recommendation/)、[system-design/ads-recommendation-system/](../../system-design/ads-recommendation-system/)、[system-design/ad-click-aggregator/](../../system-design/ad-click-aggregator/)

---

### Q34. 设计 AI Agent 编排平台：工具调用、状态与记忆、并发控制、可观测与安全护栏

- **难度**：🟡 中级
- **关键词**：Agent 循环, 工具调用 tool use, 状态持久化 / 检查点, 长任务与重试, 并发与预算, 沙箱, 可观测 trace, 护栏 guardrails, 人工介入 HITL
- **概念速记**：
  - **Agent 循环**：模型看上下文 → 决定调用工具或回答 → 执行工具 → 结果回填 → 循环直到完成；每一步都可能失败、超时、花钱。
  - **检查点**：把每步状态（消息、工具结果、计划）持久化，使长任务可恢复、可回放、可审计。
- **问题**：设计一个企业级 Agent 平台：支持多 Agent 协作、长时间任务、工具（API / 代码执行 / 浏览器）、成本与并发控制、可观测与审计、安全护栏和人工审批。
- **参考答案**：
  1. **运行时**：Agent 作为工作流实例运行在编排器（有向图 / 状态机，每节点是模型调用或工具）；每步写检查点（Q26 的 run 模型），失败按策略重试或回退；长任务用工作队列 + worker（无状态，可迁移）。
  2. **工具层**：统一工具注册（schema、权限、超时、幂等性标记、成本）；执行在沙箱（容器 / gVisor，网络白名单，资源限额）；结果截断与结构化；副作用工具（发邮件、改配置）默认需要审批。
  3. **记忆与状态**：短期 = 上下文窗口（裁剪 / 摘要）；长期 = 向量 + 结构化存储（按用户 / 租户隔离，Q31）；共享状态用版本化文档避免多 Agent 写冲突。
  4. **多 Agent**：编排者 / 工作者模式，消息通过队列传递，任务分解带明确输入输出契约；限制递归深度与总步数。
  5. **成本与并发**：每任务 token / 工具调用 / 时间预算，超预算中止；租户级并发配额；模型路由（简单步用小模型）；缓存重复工具调用结果。
  6. **可观测**：每任务一条 trace，span = 模型调用 / 工具调用（输入输出、token、延迟、成本）；离线回放评测；仪表盘按任务成功率、平均步数、成本。
  7. **护栏**：输入输出内容安全、提示注入防护（工具返回内容视为不可信数据）、敏感操作人工审批（HITL）、最小权限凭证（短期、按任务签发）、审计日志不可篡改。
  8. **运维面**：任务成功率、步数分布、超时 / 预算中止率、工具错误率、队列积压、每任务成本；模型升级要回放评测集。
- **易错点 / 面试官关注**：
  - Agent 无限循环、无预算与步数上限。
  - 工具直接在平台进程执行（无沙箱、无最小权限）。
  - 没有 trace，出问题无法回放。
- **延伸**：Q26、Q31、Q32、[behavior/behavior-questions.md](../behavior/behavior-questions.md)、[system-design/agentic-orchestration/](../../system-design/agentic-orchestration/)、[system-design/agent-orchestration/](../../system-design/agent-orchestration/)、[system-design/agentic-system-design/](../../system-design/agentic-system-design/)

---

### Q35. 设计 Dropbox 文件存储与同步：大文件直传、分片断点续传、去重与多端同步

- **难度**：🔴 高级
- **关键词**：预签名 URL presigned URL, 分片 chunking, 指纹 fingerprint / SHA-256, 断点续传 resumable, Multipart Upload, CDN 签名 URL, 同步代理 sync agent, 变更事件 change event, 最后写入胜 LWW, 内容定义分块 CDC
- **概念速记**：
  - **预签名 URL**：应用服务用自己的凭证对「某个对象 + 有效期 + 允许的操作」签名，客户端拿着它**直接**向对象存储上传 / 下载，字节流不经过应用服务器；生成签名是纯本地计算。
  - **分片 + 指纹**：客户端把文件切成 5–10MB 的块，对每块与整个文件分别算 SHA-256；整文件指纹用于去重与「是否传过」，块指纹用于断点续传时判断哪些块已到。
  - **同步代理**：常驻客户端进程，监听本地文件变化并上传；同时通过轮询或 WebSocket 拿远端变更事件（`since` 时间戳增量拉取）把别的设备的改动落到本地。
- **问题**：设计一个支持 50GB 单文件、高可用优先、多设备自动同步、可分享的云盘：上传 / 下载 / 分享 / 同步四条路径怎么走，大文件怎么可靠上传并可续传，怎么去重，同步怎么发现变更与解决冲突，安全怎么做。
- **参考答案**：
  1. **实体与 API**：`File`（内容）、`FileMetadata`（id、name、size、mime、owner、fingerprint、status、chunks[]）、`User`、`SharedFiles`（file → 有权限的用户，独立表而不是塞进元数据里的 sharelist，便于按用户查「分享给我的」）；API：`POST /files`（初始化上传，返回预签名 URL）、`GET /files/{id}`（元数据 + 下载 URL）、`POST /files/{id}/share`、`GET /changes?since=ts`（变更事件）。元数据放按 owner 分区的 KV / 文档库（查询模式是「按用户列文件」），文件本体放对象存储。
  2. **上传（核心深挖）**：❌ 传到应用服务器再转存（带宽 / 内存 / 单点）→ ✅ **客户端用预签名 URL 直传对象存储**；50GB 必须分片：客户端切块 + 算指纹 → 先问服务端「这个整文件指纹存在吗、状态是否 uploading」（去重 / 续传）→ 不存在则服务端调 `CreateMultipartUpload` 拿 uploadId、为每个分片签一个 URL、把 chunks 状态写入元数据 → 客户端并行上传分片 → 分片完成状态**由服务端校验**（对象存储事件通知 / `ListParts`）而不是只信客户端 PATCH → 全部到齐后服务端调 `CompleteMultipartUpload` 合并，再把文件标记为 uploaded。断点续传 = 重读 chunks 状态只传缺失块；进度条 = 已完成块比例。
  3. **下载**：❌ 经文件服务转发 → ✅ 对象存储直连 → ✅✅ **CDN 签名 URL**（边缘缓存热文件，签名带过期与权限，CDN 用注册的公钥验签）；合并后的对象是单个文件，下载不需要按分片，但客户端可用 Range 并行拉。
  4. **同步**：远端是事实来源；本地代理监听文件系统变化 → 切块 → 只上传变化的块 + 更新元数据；远端变更用**轮询（简单、延迟 = 周期）与 WebSocket 推送（即时）混合**：活跃客户端走长连接，空闲降级为轮询。冲突默认 **LWW**（最后写入胜）并说明代价；生产上不覆盖唯一副本而是写新版本 + 更新指针（版本化虽出题范围外也要点到）。
  5. **速度**：**固定大小分块的坑**——在文件开头插入一个字节会移动后面所有块边界，所有块指纹都变、全部重传；用**内容定义分块（rolling hash / CDC）**让块边界随内容走，只重传真正变化的块；客户端压缩（文本类收益大、媒体类不压）；CDN 就近；并行分片。
  6. **安全**：传输 TLS；静态加密（对象存储 SSE 或客户端密钥）；预签名 / CDN 签名 URL 短有效期 + 绑定文件；分享权限在 `SharedFiles` 表校验后才签 URL；审计。
  7. **可用性与一致性**：CAP 上选可用性（用户能继续读写本地副本，稍后收敛），只有「每次读必须看到最新写否则系统出错」的场景（交易）才选一致性；元数据库多副本、对象存储自带 11 个 9 持久性；备份 / 版本用于误删恢复。
  8. **运维面**：上传成功率与 p95 时长（按文件大小分桶）、分片重传率、断点续传命中率、CDN 命中率与出口带宽（最大成本）、同步延迟（一端改动到另一端可见）、变更事件积压、去重节省的存储比例；容量按「用户数 × 平均存储 × 副本」加去重折扣估算。
- **速答练习**（15 题，提炼自 Hello Interview 的 Dropbox 测验；面试官可用 `quiz dropbox` 逐题快问）：
  1. 把内容分发到离用户近的地方以降低延迟的是什么？→ CDN（边缘缓存），不是地理路由的 LB。
  2. 为什么对象存储的事件通知比客户端回调更可靠？→ 客户端上传后可能崩溃 / 断网发不出回调；存储侧事件在确认写入后触发（轮询是替代方案）。
  3. 组件职责：CDN 边缘缓存 / 文件服务签预签名 URL 与写元数据 / 对象存储存字节 / 元数据库存名称、大小、归属。
  4. 50GB 文件怎么可靠上传？→ 分片 multipart（进度、续传、避开超时）。
  5. 并行分片上传能吃满带宽吗？→ 能，多连接同时传，高延迟链路收益更大。
  6. 离线几小时后怎么同步不多下？→ `GET /files/changes?since=` 只拉变更事件，不是全量比对。
  7. LWW 提供强一致吗？→ 否，是最终一致，只是冲突裁决规则。
  8. 断网后续传需要什么？→ 文件指纹（或 uploadId）+ 服务端已存分片状态，只补缺失块。
  9. 分区时优先什么？→ 可用性（允许读到旧数据），文件晚几秒出现可接受。
  10. 为什么元数据可用 DynamoDB 类 NoSQL？→ 结构松散、关系少、主要按用户查询（Postgres 也行）。
  11. 单个 HTTP 请求传大文件为什么不行？→ 服务器 / 网关 / 浏览器有请求体上限（NGINX ~2GB、API 网关常 10MB），分片是硬约束不是优化。
  12. `since` 用客户端本地时钟有什么问题？→ 时钟偏差会漏事件；生产用服务端下发的游标 / 高水位。
  13. 字节写成功、元数据写超时后重试怎么处理？→ 把两步当一个逻辑事务 / 工作流，或有补偿清理，避免「有文件无元数据」的分裂状态。
  14. 请求体里自称 owner 的 `uploadedBy` 怎么处理？→ 忽略请求体身份字段，从会话 / JWT 取调用者，再对照服务端元数据鉴权。
  15. 上传方式从差到优：存应用服务器本地盘 < 经后端转存对象存储（双倍上传）< 预签名 URL 直传。
- **按级别的期望**（面试官口径）：
  - 🟡 中级（约 80% 广度 / 20% 深度）：API 与数据模型清楚，上传 / 下载 / 分享的高层设计都能工作；不要求知道预签名 URL 或分片细节，但被引导后能跟上。
  - 🔴 高级（60/40）：快速过完高层设计，把时间花在**大文件上传**的细节上：直传、分片、指纹、续传、服务端校验；主动提出而不是等追问；能讲对象存储与 CDN 的取舍。
  - 🔴 Staff+（40/60）：在上述基础上深入固定分块 vs 内容定义分块、同步冲突与版本化、跨端一致性与安全边界，并能说出「我会用 S3 Multipart Upload，但它内部是这样工作的」。
- **易错点 / 面试官关注**：
  - 文件经应用服务器中转；不分片，或分片了但续传状态只信客户端。
  - 只有整文件指纹没有块指纹；不知道固定分块在插入场景下会全量重传。
  - 分享列表塞进文件元数据里导致「分享给我的文件」要全表扫。
  - CAP 说反：把云盘设计成强一致而牺牲离线可用。
- **延伸**：Q11、Q22、[system-design/dropbox/](../../system-design/dropbox/)、[system-design/file-storage-system/](../../system-design/file-storage-system/)、[system-design/blob-store/](../../system-design/blob-store/)、来源：[Hello Interview — Dropbox problem breakdown](https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox)（Evan King，2026-02）

---

## 参考来源

- 主题语料：[`system-design/`](../../system-design/) 子模块（<https://github.com/ljluestc/system-design>），每个主题目录含 `00-index`（题面）、`01-requirements`、`02-architecture`、`05-trade-offs`、`06-quiz`（折叠答案）、`20-interview-drills`（速答 + 陷阱）等标准文档；全量目录见 [system-design-catalog.md](system-design-catalog.md)。
- 面试方法论：[system-design/interview-quick-reference.md](../../system-design/interview-quick-reference.md)、[system-design/system-design-primer-guide.md](../../system-design/system-design-primer-guide.md)、[system-design/8-week-system-design-roadmap.md](../../system-design/8-week-system-design-roadmap.md)。
- Hello Interview 问题拆解（[Bitly](https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly)、[Dropbox](https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox)、[Distributed Cache](https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-cache)，Evan King）：Q15、Q35 的「按级别的期望」与深挖顺序参考其框架；Q7 的追问可接 [collections/k8s-web-archive.md](../../collections/k8s-web-archive.md) 第 686–697 题（分布式缓存六个深挖的速答卡）；本仓库只做**提炼与转述**，不收录原文。本地存档见 `~/dev/k8s/slurps/hellointerview-learn-system-design-problem-breakdowns-*.md`。
- 本模块参考答案为自研整理，术语与结论以各主题目录下的一手文档与官方资料为准。
