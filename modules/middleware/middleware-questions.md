# 中间件运维面试题（15 题）

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
