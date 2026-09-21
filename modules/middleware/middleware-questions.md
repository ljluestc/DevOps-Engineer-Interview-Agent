# 中间件运维面试题（20 题）

> 模板见 [../../docs/STANDARD.md](../../docs/STANDARD.md)。

---

### Q1. Kafka 的架构与核心概念（topic/partition/consumer group/replica）？
- **难度**：🟡 中级
- **关键词**：Kafka, partition, replica, ISR, consumer group
- **概念速记**：分布式提交日志；partition 并行单位，replica 保证可靠。
- **参考答案**：topic 分 partition（并行/有序），replica（ISR 同步副本），consumer group 按 partition 分配消费。关注：分区数规划、副本因子（≥3）、ISR 收缩、控制器选举、磁盘/网络吞吐。
- **易错点**：partition 过多导致 controller 与元数据压力。
- **延伸**：Q2、Q6（积压）

### Q2. Kafka 消息积压/消费慢怎么排查？
- **难度**：🔴 高级
- **关键词**：积压, lag, rebalance, 分区不均
- **概念速记**：lag = 生产 - 消费，消费慢或分区不均致积压。
- **参考答案**：看 consumer group lag；分区数与消费者数是否匹配；消费逻辑是否慢（外部依赖）；是否 rebalance 频繁（心跳/session 超时）；网络/磁盘 IO。处理：加分区/消费者、提并行、优化逻辑、谨慎重置 offset。
- **易错点**：消费者数 > 分区数，多余消费者空转。
- **延伸**：Q1、sre Q23

### Q3. Kafka 数据不丢/不重怎么保证？
- **难度**：🔴 高级
- **关键词**：acks, ISR, 幂等, 事务
- **概念速记**：不丢靠acks+副本；不重靠幂等/事务。
- **参考答案**：不丢：producer `acks=all` + 重试；broker `min.insync.replicas`；consumer 处理完再 commit。不重：at-least-once + 消费幂等/事务。权衡吞吐与可靠（acks=all 降吞吐）。
- **易错点**：acks=1 以为不丢，leader 宕机丢消息。
- **延伸**：Q1、sre Q10（幂等）

### Q4. Redis 持久化 RDB / AOF 区别与选型？
- **难度**：🟡 中级
- **关键词**：Redis, RDB, AOF, 持久化
- **概念速记**：RDB 快照快但丢最后一段；AOF 追加命令更全但重。
- **参考答案**：RDB（快照，恢复快、文件小，丢最后一次后数据）；AOF（追加命令，可 everysec，数据更全但大、恢复慢）。生产常混合（AOF 开 + RDB 兜底）或仅 AOF(everysec)。关注 fork 阻塞、AOF 重写、磁盘 IO。
- **易错点**：纯 RDB 在宕机时丢失较多近期数据。
- **延伸**：Q5、Q7（大 key）

### Q5. Redis 内存淘汰策略（maxmemory-policy）有哪些？
- **难度**：🟡 中级
- **关键词**：淘汰策略, LRU, LFU, 缓存
- **概念速记**：内存满时按策略淘汰，防写失败。
- **参考答案**：noeviction（写报错）、allkeys-lru/random、volatile-lru/random/ttl、allkeys-lfu（4.0+ 更优）。缓存用 allkeys-lru/lfu；带过期用 volatile。监控命中率，避免击穿雪崩。
- **易错点**：默认 noeviction，内存满后写入直接报错。
- **延伸**：sre Q12（缓存三崩）

### Q6. Redis 集群（Cluster）数据分片与故障转移？
- **难度**：🔴 高级
- **关键词**：Redis Cluster, slot, 16384, 故障转移
- **概念速记**：16384 槽分片，Gossip + 主从故障转移。
- **参考答案**：16384 槽分片，每节点负责部分；Gossip 协议；主从+哨兵式故障转移。关注槽迁移在线扩缩、避免大 key（热点/迁移慢）、跨槽事务限制、min-replicas-to-write 防脑裂。大 key/热 key 是经典坑。
- **易错点**：大 key 迁移时阻塞集群。
- **延伸**：Q7、sre Q12

### Q7. Redis 大 key / 热 key 怎么发现与治理？
- **难度**：🔴 高级
- **关键词**：大key, 热key, 拆分, 本地缓存
- **概念速记**：大 key 迁移慢、热 key 打爆单节点。
- **参考答案**：发现：`redis-cli --bigkeys`、监控访问分布。治理：拆分、本地缓存、限流、多副本打散。Kafka 大消息（超 1MB 调 max.message.bytes，影响吞吐）。
- **易错点**：大 key 删除阻塞主线程（用 UNLINK 异步）。
- **延伸**：Q6、Q1（Kafka 大消息）

### Q8. MySQL 主从复制原理？半同步/异步/全同步区别？
- **难度**：🟡 中级
- **关键词**：MySQL, 主从, binlog, 半同步
- **概念速记**：binlog→从库重放；半同步折中可靠与性能。
- **参考答案**：binlog→从 IO 线程拉取写 relay log→SQL 线程重放。异步（主不等待，可能丢）；半同步（至少一从确认，折中）；全同步（全确认，慢）。关注复制延迟、GTID、主从一致性校验。
- **易错点**：异步复制从库延迟大，读从库读到旧数据。
- **延伸**：Q9、Q11（死锁）

### Q9. MySQL 高可用方案（MHA / Orchestrator / MGR / 云 RDS）？
- **难度**：🔴 高级
- **关键词**：MHA, Orchestrator, MGR, 高可用
- **概念速记**：MGR 组复制原生高可用；云 RDS 托管主备。
- **参考答案**：MHA（传统，主挂自动切，有脑裂风险）；Orchestrator（拓扑管理强）；MGR（组复制，Paxos，原生高可用）；云 RDS（托管主备/多 AZ）。看自运维能力、一致性与切换速度。
- **易错点**：MHA 切换期间有脑裂窗口。
- **延伸**：Q8、sre Q4（脑裂）

### Q10. MySQL 死锁与锁等待怎么排查？
- **难度**：🔴 高级
- **关键词**：死锁, InnoDB, 锁等待, 事务
- **概念速记**：死锁=两个事务互相等锁；锁等待=等他人释放。
- **参考答案**：`SHOW ENGINE INNODB STATUS` 看最近死锁；`INNODB_TRX`/`LOCKS`（8.0）；慢事务持锁致等待。优化：事务短小、固定加锁顺序、合理索引减锁范围、降隔离级别（RC）。
- **易错点**：长事务持锁，引发大面积锁等待。
- **延伸**：Q8、sre Q11（幂等）

### Q11. Elasticsearch 的架构与分片/副本策略？
- **难度**：🔴 高级
- **关键词**：Elasticsearch, shard, replica, heap
- **概念速记**：index 分 shard 并行；replica 高可用/读扩展。
- **参考答案**：单分片 30–50GB 为宜、副本≥1、避免过多分片（元数据压力）。运维：JVM heap（≤50% 物理、≤32GB）、冷热分层、写入 bulk、refresh 间隔。
- **易错点**：分片数过多导致集群元数据与 heap 压力。
- **延伸**：Q12、Q13

### Q12. ES 写入慢/查询慢怎么排查？
- **难度**：🔴 高级
- **关键词**：ES, 写入吞吐, 慢查询, 深分页
- **概念速记**：写入看 bulk/refresh/副本；查询看慢日志/深分页。
- **参考答案**：写入：bulk、refresh 间隔、副本数（写入时降副本）、mapping（禁用不需索引字段）、分片不均。查询：慢查询日志、深分页（search_after 替代 from/size）、聚合内存、filter cache、硬件（SSD）。监控 heap/GC。
- **易错点**：from/size 深分页导致性能崩。
- **延伸**：Q11

### Q13. 消息队列 vs 缓存 vs 数据库 职责边界？
- **难度**：🟡 中级
- **关键词**：MQ, 缓存, 数据库, 职责边界
- **概念速记**：MQ 异步解耦削峰；缓存加速读；DB 持久化强一致。
- **参考答案**：MQ：异步解耦、削峰、最终一致；缓存：加速读、扛热点；DB：持久化、强一致事务。误区：把 MQ 当存储（丢消息风险）、缓存当源（一致性）、DB 扛高并发读（应前置缓存）。
- **易错点**：把 MQ 当持久存储，消息过期丢失。
- **延伸**：Q1（Kafka）、Q5（Redis）

### Q14. 中间件常见「大 key / 热 key」问题怎么治理？（综合）
- **难度**：🔴 高级
- **关键词**：大key, 热key, 拆分, 打散
- **概念速记**：大 key 拖慢迁移/删除；热 key 打爆单点。
- **参考答案**：Redis/Kafka/ZK 都有。治理：拆分、本地缓存、限流、多副本打散、监控发现。监控 + 提前发现优于故障后救火。
- **易错点**：热 key 无监控，单节点被打满才发现。
- **延伸**：Q7、Q1

### Q15. 如何做中间件的备份与恢复演练？
- **难度**：🔴 高级
- **关键词**：备份, 恢复演练, PITR, RTO
- **概念速记**：备份≠能恢复，必须演练。
- **参考答案**：Redis：RDB/AOF 复制+定期校验；MySQL：xtrabackup/物理备+binlog 时点恢复（PITR）；ES：snapshot 到对象存储；Kafka：靠副本+保留期（备份少，靠重建）。关键是演练恢复（非仅备份），验证 RTO/RPO。
- **易错点**：只做备份从不演练恢复，真故障时恢复失败。
- **延伸**：sre Q8（RTO/RPO）；Q9

### Q16. Redis 放到代理 / 服务网格后面有什么坑？
- **难度**：🔴 高级
- **关键词**：Redis Cluster, MOVED/ASK 重定向, 拓扑感知, 连接复用, 代理透明性
- **概念速记**：Redis Cluster 的客户端是**拓扑感知**的——它从集群拿到 slot→节点的映射，直接连对应节点；访问错节点时服务端回 **MOVED/ASK** 让客户端重定向。一旦中间插入一个代理（Envoy sidecar、网格、L4 LB），这套机制就可能被破坏。
- **参考答案**：
  1. **典型故障**：
     - 客户端拿到的是**代理的地址**而不是真实节点地址，或者 MOVED 返回的节点 IP 客户端根本连不上（网格外/不可路由）→ 无限重定向或连接失败。
     - L4 代理把不同 slot 的请求随机打到不同节点 → 大量 MOVED，延迟劣化。
     - 代理做了连接复用，但 Redis 的 `SELECT`、`MULTI/EXEC`、订阅（`SUBSCRIBE`）、阻塞命令（`BLPOP`）都是**有状态**的，复用连接会串话。
  2. **几种可行姿势**：
     - **不代理（最稳）**：把 Redis 端口从劫持范围排除（`traffic.sidecar.istio.io/excludeOutboundPorts`），让客户端直连。牺牲的是网格的 mTLS 与指标。
     - **只做 L4**：网格只提供 mTLS + L4 授权 + 连接级指标，不解析协议——ambient 模式在这里性价比很高（见 service-mesh Q14、Q21）。
     - **用懂 Redis 协议的代理**：Envoy 有 `redis_proxy` filter，能理解 slot 并做分片路由，此时对客户端可以表现为**单机 Redis**（客户端不需要 cluster 模式）；Aeraki/Envoy Gateway 有基于此的方案。收益是客户端简化、连接收敛；代价是代理成为关键路径且要跟随 Redis 版本。
  3. **连接数问题（上网格的一个真实收益）**：N 个应用实例 × M 个 Redis 节点 = N×M 条连接，大规模下 Redis 的连接数和内存会吃紧。代理层做连接池收敛能显著缓解——**这往往比 mTLS 更能说服团队**。
  4. **通用原则**：**有状态、带拓扑语义的协议，放到透明代理后面之前一定要实测**——单机 Redis 没问题不代表 Cluster 没问题，功能测试通过不代表故障转移时没问题（要专门测主从切换和 slot 迁移）。
- **易错点**：把 Redis Cluster 直接塞进网格然后遇到偶发超时查不出来；忽略阻塞命令与连接复用的冲突；只测正常路径不测 failover。
- **延伸**：Q6、Q7、service-mesh Q21、Q24

### Q17. Redis 集群方案怎么选：Cluster / 代理分片 / 主从 + 哨兵 / 云托管？
- **难度**：🔴 高级
- **关键词**：Redis Cluster, Codis, Sentinel, 分片, 运维成本
- **概念速记**：四类方案的本质差别在于**「分片逻辑放在哪」**和**「谁负责故障转移」**。
- **参考答案**：
  | 方案 | 分片逻辑 | 故障转移 | 适合 |
  |---|---|---|---|
  | 主从 + **Sentinel** | 不分片（单点容量上限） | Sentinel 选主 | 数据量能放进单机、只求高可用 |
  | **Redis Cluster** | 客户端（拓扑感知） | 集群内自治（gossip + 投票） | 原生方案，数据量大、想少一层组件 |
  | **代理分片**（Codis/twemproxy/Envoy redis_proxy） | 代理 | 依赖外部组件（ZK/etcd + 哨兵） | 客户端老旧、想对业务完全透明、要连接收敛 |
  | **云托管**（ElastiCache/云 Redis） | 云厂商 | 云厂商 | 不想自己运维，能接受成本与黑盒 |
  1. **Redis Cluster 的真实约束**（选型时必须讲）：
     - **不支持跨 slot 的多键操作**（`MGET`、事务、Lua 脚本跨 key）——除非用 **hash tag**（`{user123}:profile`）把相关 key 强制放到同一 slot。这条经常是业务改造的最大成本。
     - 客户端必须支持 cluster 模式且实现要靠谱（重定向处理、拓扑刷新）。
     - 扩缩容需要 **slot 迁移**，迁移期间有 ASK 重定向，要验证客户端行为。
  2. **代理分片的取舍**：对业务透明（客户端当单机用）、能收敛连接数、能平滑迁移；代价是多一跳延迟、代理要高可用、社区活跃度普遍不如原生 Cluster。
  3. **共同的运维重点**（无论选哪个）：
     - **大 key / 热 key** 治理（见 Q7）——分片解决不了单个热 key。
     - 持久化与内存策略（见 Q4、Q5）；容量规划留足 buffer，避免 `maxmemory` 触发淘汰时抖动。
     - **故障转移演练**：选主要多久？期间客户端报什么错？业务能不能容忍？**没演练过就等于不知道自己的 RTO。**
  4. **我的默认建议**：新项目优先「云托管或原生 Cluster + 规范 key 设计」，不要一上来就自建代理层；只有当客户端无法改造或连接数确实压不住时，才引入代理。
- **易错点**：没评估跨 slot 操作的改造成本就选 Cluster；以为分片能解决热 key；从不做主从切换演练。
- **延伸**：Q4、Q5、Q6、Q7、Q16、sre Q10

### Q18. 中间件到底该不该上 K8s？怎么判断？
- **难度**：🔴 高级
- **关键词**：StatefulSet, Operator, 本地盘, 有状态, 云托管
- **概念速记**：「上不上 K8s」对无状态服务几乎不是问题，对中间件（MySQL/Kafka/Redis/ES）则是个真实的权衡——K8s 的强项是**编排易变的无状态副本**，而中间件恰恰**有状态、对 IO 敏感、故障转移语义复杂**。
- **参考答案**：
  1. **判断维度**：
     - **是否有成熟 Operator**：有（如 Strimzi 之于 Kafka、ECK 之于 ES、各类 MySQL Operator）→ 风险大降，因为扩缩容、备份、版本升级、故障转移这些有状态逻辑被封装了。没有成熟 Operator 就自己用 StatefulSet 硬扛 → **不建议**。
     - **存储方案**：需要高 IOPS 的（MySQL/Kafka）用网络盘会有明显性能损失，用 **local PV** 则 Pod 被绑死在节点上，节点故障即数据不可用（要靠中间件自身的多副本兜底）。**存储方案定不下来就不要上。**
     - **团队能力**：出问题时要同时懂中间件和 K8s。只懂其一会把 MTTR 拉长几倍。
     - **规模与弹性需求**：需要频繁创建/销毁大量实例（多租户、按需环境）→ K8s 收益大；就那几套稳定跑的集群 → 收益小、风险不小。
  2. **上 K8s 的关键配置**（如果决定上）：
     - StatefulSet（稳定网络标识 + 有序）+ PVC 模板；`podManagementPolicy` 按中间件要求选。
     - **PDB** 防止滚动/驱逐时同时下线多个副本破坏 quorum；**反亲和**保证副本跨节点/跨可用区。
     - 探针要写对：**readiness 反映「能否服务」，liveness 要非常保守**——liveness 配错会在集群压力大时循环重启，把小问题放大成雪崩（见 kubernetes Q4）。
     - 资源用 **Guaranteed QoS**，避免被驱逐；关掉或谨慎对待 CPU limit 的限流影响（见 linux Q27）。
     - 备份与恢复必须是 K8s 之外可独立执行的路径（见 sre Q28）。
  3. **我的默认建议**：**先看云托管**——如果云托管在成本和功能上可接受，它省下的运维精力通常远超账单差价；其次是有成熟 Operator 的自建；最后才是裸 StatefulSet 自己拼。**存量稳定运行的中间件不要为了"统一技术栈"而迁移**，这类迁移的收益通常被高估、风险被低估。
- **易错点**：只讲「K8s 弹性好」不讲存储与故障域；liveness 探针配得太激进；不评估团队排障能力；为了统一而迁移稳定的存量系统。
- **延伸**：Q9、Q15、kubernetes Q4、Q17、Q29、linux Q27、sre Q28

### Q19. MongoDB 的文档模型、BSON 与 Schema Validation：什么时候选它，索引怎么设计？
- **难度**：🟡 中级
- **关键词**：MongoDB, 文档模型, BSON, Schema Validation, 索引, ESR
- **概念速记**：
  - **文档数据库（Document DB）**：以 JSON-like 文档为单位存储，`Database → Collection → Document → Field`，集合无固定列，同一集合的文档可以有不同字段；**单文档写入天然原子**。
  - **BSON（Binary JSON）**：MongoDB 内部存储格式，带类型信息（ObjectId / Date / Decimal128 / Binary），比 JSON 快且类型更丰富。
  - **Schema Validation**：给集合挂 `$jsonSchema` 规则，写入不合规文档被拒绝——「Start flexible, add rules when needed」。
- **问题**：什么样的业务适合 MongoDB 而不是 MySQL？上线前索引与 schema 怎么设计，运维要盯什么？
- **参考答案**：
  1. **选型边界**：字段经常变化 / 半结构化（日志、事件、用户画像、商品属性）、读写模型能「一个文档装下一次访问所需的数据」→ 适合；强事务、多表关联、报表型 JOIN → 关系库更稳。核心思路是**按访问模式建模**（嵌入 vs 引用），而不是先设计三范式再拆。
  2. **索引设计**：`_id` 默认唯一索引；高频过滤字段建索引并加 `unique` 防脏数据；复合索引按 **ESR 原则**（Equality → Sort → Range）排列，如日志查询 `{ service: 1, level: 1, timestamp: -1 }`；用 `explain()` 确认 `IXSCAN` 而非 `COLLSCAN`；时间类字段用 BSON Date 而非字符串，才能范围查询与 **TTL 索引**自动过期。
  3. **Schema 治理**：集合建好就加 `validator`（`required` / `bsonType`），`validationLevel: moderate` 放过存量、`validationAction: error` 拦截新写入；避免「无 schema」变成「谁都能写脏数据」。
  4. **运维要盯**：连接数与游标泄漏、`COLLSCAN` 慢查询（profiler / `currentOp`）、写关注（`w: majority` 与延迟的权衡）、oplog 窗口是否够副本追上、单文档 16MB 上限（数组无限增长是经典事故）、备份必须演练恢复（见 Q15）。
- **易错点 / 面试官关注**：
  - 把 MongoDB 当「不用设计 schema 的 MySQL」用，字段类型混乱（时间存字符串）导致查询与索引失效。
  - 不写 `$set` 直接 `update` 把整个文档替换掉；`deleteMany({})` 清空集合。
  - 只会 `createIndex`，不知道 ESR、不看 `explain`。
- **延伸**：Q20、Q15、[collections/mongodb-zero-to-hero.md](../../collections/mongodb-zero-to-hero.md)（68 题基础到应用）、`collections/ops-question-bank-1502.md` OTHER 40–43（备份 / 分片）

### Q20. 用 MongoDB Atlas Vector Search 做 RAG / 语义检索：链路、索引参数与「要不要上专用向量库」？
- **难度**：🔴 高级
- **关键词**：Vector Search, embedding, $vectorSearch, cosine, RAG, 向量库选型
- **概念速记**：
  - **Embedding**：模型把文本 / 图片编码成固定维度浮点向量，语义相近则向量距离近；写入与查询**必须用同一模型与维度**。
  - **Atlas Vector Search**：在文档的向量字段上建 `type: vector` 索引（`numDimensions` + `similarity: cosine / euclidean / dotProduct`），用聚合阶段 `$vectorSearch`（`queryVector` / `numCandidates` / `limit` / `filter`）做近似最近邻检索；由 Atlas Search（`mongot`）提供，社区版 `mongod` 没有。
- **问题**：团队要给内部知识库做 RAG 问答，已经在用 MongoDB 存业务数据。用 Atlas Vector Search 还是引入 Milvus / Pinecone / pgvector？链路怎么搭，运维上会踩什么坑？
- **参考答案**：
  1. **链路**：离线——文档切块 → embedding → 存 `{ text, embedding, metadata }`；在线——问题 embedding → `$vectorSearch` 召回 top-k（可带 `filter` 做租户 / 权限 / 时间过滤）→ 拼 prompt → LLM 生成 → 记录引用与评测。
  2. **索引参数**：`numDimensions` 与模型一致（如 1536）；相似度**跟模型推荐走**，文本通常 cosine，向量已归一化时 dotProduct 更快；`numCandidates` 是 ANN 候选数，官方建议 ≥ 10–20 × `limit`，越大越准越慢；索引异步构建，查询前先确认 Ready。
  3. **选型权衡**：
     - **留在 MongoDB**：业务数据与向量同库，一条聚合完成「向量召回 + 元数据过滤 + 关联字段」，少一套系统、一致性与权限模型简单，团队已有运维经验 → **中小规模（百万到千万级向量）默认选它**。
     - **上专用向量库**：亿级向量、需要精细的 HNSW / 量化 / GPU 索引调参、检索 QPS 远高于业务库、或必须自建离线环境（社区版没有 Vector Search）时才值得多养一套系统。
     - 关键不是「哪个更强」，而是**多一套有状态系统的运维成本 vs 检索规模需求**。
  4. **运维坑**：Search 节点资源独立、要单独容量规划与计费；换 embedding 模型 = 全量重建向量与索引（要做版本字段与双写灰度）；M0 / 共享层有索引数与存储限制；召回质量要有**黄金问题集**做评测，不能只看「跑通」；向量字段被存成字符串或维度不一致时查询静默返回空。
- **易错点 / 面试官关注**：
  - 只会说「MongoDB 也能存向量」，讲不出 `numCandidates` / 相似度 / 维度一致性这些真正决定效果的参数。
  - 没考虑权限过滤（多租户 RAG 泄露别人的文档）。
  - 不做评测就换模型、改 chunk 大小。
- **延伸**：Q19、gpu-ai（推理与 embedding 服务）、system-design（RAG 主题 `switch system-design rag`）、[collections/mongodb-zero-to-hero.md](../../collections/mongodb-zero-to-hero.md) 第六章
