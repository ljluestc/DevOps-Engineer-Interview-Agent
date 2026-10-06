# 系统设计题库（system-design 子模块提炼）— 各主题的专属 quiz、drill 与速答（458 题）

> **来源**：用户自有仓库 [ljluestc/system-design](https://github.com/ljluestc/system-design)（本仓库的 `system-design/` 子模块，630 个主题目录）。
> 由 `scripts/build_system_design_quiz_bank.py` **自动生成，请勿手改**；子模块更新后重新运行即可。
> **筛选口径**：约 3,900 道「每个主题都一样」的模板题（10x 流量、SQL vs NoSQL、主库宕机、缓存层设计……）被剔除，
> 只保留**主题专属**内容：`06-quiz.md` 的真题（🟡，要点取自答案首段）、`20-interview-drills.md` 中非占位的 drill（🔴）、
> 以及 drill 文件里的速答表（🟢）。变体目录（如 `google_docs` / `google-docs-k8s`）经 `resolver.json` 折叠到规范主题，重复题只保留一次。
> **版权**：用户自有，答案要点可直接引用。**用法**：「一次 10 题」的系统设计批量轮次、`quiz <主题>` 速答，或在单主题面试中做追问；
> 完整答案在对应主题目录的 `06-quiz.md` / `20-interview-drills.md`。

## 一、基础与方法论（`fundamentals`，10 个主题，57 题）

### [`api`](../system-design/api/) — API migration — when customers must ship code（变体：`api-design`）

1. 🔴 [drill] Why migrate (value, not “API churn”)
   - 要点：Name **forcing functions**: new auth (OAuth2/mTLS), **scale** (payload or QPS caps on v1), **unifying** three legacy surfaces, **compliance** (audit fields, data residency), or product consolidation. That paragraph leads **release notes** and **customer kickoffs** so partners schedule work instead of deprioritizing you.
2. 🔴 [drill] Stakeholders and RACI (interview-appropriate)
   - 要点：**RACI in one breath:** one **DRI** for tech, one for **comms calendar**, one **exec** sponsor for date slips and exceptions.
3. 🔴 [drill] Communication (predictable beats)
   - 要点：**Kickoff:** why, what changes, what does **not** change, sunset **and** buffer, sandbox base URLs, support channels, SLA for answers. **Recurring:** office hours or async **forum**; record sessions; single **FAQ** updated from real tickets. **Executive:** monthly—**v2 traffic %**, P1/P2 by migration, top doc gaps.
4. 🔴 [drill] Technical pattern (dual-run, phased)
   - 要点：**v1 and v2** for a **bounded** window (quarters, not “forever”). **Route** by path, `Accept-Version`, or **per-tenant** flag for large partners. **Order risk:** read-only or low-stakes methods before **money-moving** or irreversible operations. **Compat shims** only if cheaper than big-bang; shims get their own sunset.
5. 🔴 [drill] Docs, sandbox, SDKs
   - 要点：**Sandbox** matches prod **error shapes, auth, rate limits**; throttle mismatches are a top source of “works in UAT, fails in prod.” **Migration guide:** before/after JSON, field mapping, webhook diff tables. **SDKs** versioned with the API; per-language **upgrade recipe**.
6. 🔴 [drill] Testing (ours + theirs)
   - 要点：**Contract tests** and golden JSON in CI; replay of anonymized production samples where policy allows. **Partner cert** (optional): checklist of ten happy paths + two negative auth tests. **Load** on v2 before wide invite; watch **p99** and error **code** mix.
7. 🔴 [drill] Program metrics
   - 要点：**SLO burn** during bridge quarters: freeze unrelated high-variance work if the budget is thin.
8. 🔴 [drill] Risks (name in interview)
   - 要点：**Largest** integrator misses date → **written** extension, dedicated assist, or **feature** in their SDK—not silent eternal v1. **Semantic** rename without version bump → **CI** breaking rules + `oasdiff`. **Webhooks** lag → dual-send only with an **end** date, or versioned **subscription** id.
9. 🔴 [drill] Closure
   - 要点：Public thanks; short **integrator** survey; internal retro on lead time to **90%** v2 and **incident** count. Feed into the **next** deprecation (templates improve).

### [`database`](../system-design/database/) — Database（变体：`database-demo`, `database-system`, `database-system-design`）

10. 🟡 How would you scale Database to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
11. 🟡 What database would you choose for Database and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
12. 🟡 How do you handle failures in Database?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
13. 🟡 What caching strategy would you use for Database?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
14. 🟡 How do you ensure consistency in a distributed Database?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`fault-tolerance-system`](../system-design/fault-tolerance-system/) — Fault Tolerance System（变体：`fault-tolerance-system-design`）

15. 🟡 How would you scale Fault Tolerance to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
16. 🟡 What database would you choose for Fault Tolerance and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
17. 🟡 How do you handle failures in Fault Tolerance?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
18. 🟡 What caching strategy would you use for Fault Tolerance?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
19. 🟡 How do you ensure consistency in a distributed Fault Tolerance?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`maintainability-system-design`](../system-design/maintainability-system-design/) — Maintainability

20. 🟡 How would you scale Maintainability to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
21. 🟡 What database would you choose for Maintainability and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
22. 🟡 How do you handle failures in Maintainability?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
23. 🟡 What caching strategy would you use for Maintainability?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
24. 🟡 How do you ensure consistency in a distributed Maintainability?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`modern-system-design`](../system-design/modern-system-design/) — Modern

25. 🟡 How would you scale Modern to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
26. 🟡 What database would you choose for Modern and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
27. 🟡 How do you handle failures in Modern?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
28. 🟡 What caching strategy would you use for Modern?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
29. 🟡 How do you ensure consistency in a distributed Modern?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`pe-system-design`](../system-design/pe-system-design/) — Pe

30. 🟡 How would you scale Pe to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
31. 🟡 What database would you choose for Pe and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
32. 🟡 How do you handle failures in Pe?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
33. 🟡 What caching strategy would you use for Pe?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
34. 🟡 How do you ensure consistency in a distributed Pe?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`production-engineering-system-design`](../system-design/production-engineering-system-design/) — Production Engineering

35. 🟡 How would you scale Production Engineering to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
36. 🟡 What database would you choose for Production Engineering and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
37. 🟡 How do you handle failures in Production Engineering?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
38. 🟡 What caching strategy would you use for Production Engineering?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
39. 🟡 How do you ensure consistency in a distributed Production Engineering?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`reliability-system-design`](../system-design/reliability-system-design/) — Reliability

40. 🟡 What's the difference between SLI, SLO, and SLA?
   - 要点：**SLI** = what you measure (p99 latency, error rate). **SLO** = the target you set (p99 < 200 ms). **SLA** = the contract with customers (99.99% uptime or financial credits). SLOs should be stricter than SLAs to give you a buffer. Error budget = 100% - SLO = how much failure you're allowed before freezing feature releases.
41. 🟡 How does a circuit breaker prevent cascading failures?
   - 要点：Three states: **Closed** (normal, requests flow through), **Open** (failing, all requests return fallback immediately), **Half-Open** (test with a few requests). After N failures in a time window, circuit opens — stops sending traffic to failing dependency, preventing your service from exhausting threads waiting for timeouts.
42. 🟡 Why is MTTR more important than MTBF?
   - 要点：In distributed systems, failures are **inevitable** — you can't prevent them all. MTTR (Mean Time To Recovery) directly controls user impact. A system that fails once a week but recovers in 10 seconds is more reliable than one that fails once a month but takes 2 hours to recover.
43. 🟡 How do you prevent a thundering herd on cache expiry?
   - 要点：Four techniques: (1) **Stampede lock** — only one thread refreshes cache, others wait. (2) **Jittered TTL** — add random offset to prevent synchronized expiry. (3) **Request coalescing** — merge concurrent identical requests into one DB query.
44. 🟡 When would you choose active-active over active-passive?
   - 要点：**Active-active** when you need near-zero downtime (financial systems, global services). Both sites serve traffic simultaneously — failover is instantaneous (just stop routing to failed site). Cost: 2x infrastructure + data consistency complexity (conflict resolution).
45. 🟡 What is a gray failure and how do you detect it?
   - 要点：A server that passes health checks (TCP/HTTP probe returns 200) but delivers degraded service — high latency, partial errors, or wrong results for some requests. Standard up/down monitoring misses it.
46. 🟡 How do you safely deploy to production?
   - 要点：**Canary deploy**: route 1-5% of traffic to new version. Compare canary SLIs against baseline for 10-30 minutes. If SLOs hold, gradually increase to 100%. If SLOs breach, **automated rollback** within seconds. Pre-deploy: run integration tests in staging with production-like data. Post-deploy: monitor error rates, latency, and business metrics for 24 hours.
47. 🟡 What is chaos engineering and when should you use it?
   - 要点：Deliberately injecting failures (kill instances, add latency, corrupt data) to verify that reliability mechanisms work. **When:** after you have basic reliability patterns in place (circuit breakers, retries, health checks). **Start small:** kill one instance in staging; if that breaks things, fix that before doing anything fancier.

### [`reshaded-approach-system-design`](../system-design/reshaded-approach-system-design/) — Reshaded Approach

48. 🟡 How would you scale Reshaded Approach to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
49. 🟡 What database would you choose for Reshaded Approach and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
50. 🟡 How do you handle failures in Reshaded Approach?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
51. 🟡 What caching strategy would you use for Reshaded Approach?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
52. 🟡 How do you ensure consistency in a distributed Reshaded Approach?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`scalability-system-design`](../system-design/scalability-system-design/) — Scalability

53. 🟡 How would you scale Scalability to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
54. 🟡 What database would you choose for Scalability and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
55. 🟡 How do you handle failures in Scalability?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
56. 🟡 What caching strategy would you use for Scalability?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
57. 🟡 How do you ensure consistency in a distributed Scalability?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

## 二、基础组件（`building-blocks`，12 个主题，98 题）

### [`bitly-system-design`](../system-design/bitly-system-design/) — Bitly

58. 🟡 How would you scale Bitly to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
59. 🟡 What database would you choose for Bitly and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
60. 🟡 How do you handle failures in Bitly?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
61. 🟡 What caching strategy would you use for Bitly?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
62. 🟡 How do you ensure consistency in a distributed Bitly?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`cassandra`](../system-design/cassandra/) — Apache Cassandra — System design hub

63. 🟡 What is **query-driven** modeling?
   - 要点：**A:** You choose **partition key** and **clustering** so each user-facing query hits **one partition** (or a small bounded set). Relational **normal form first** is the wrong default.
64. 🟡 Why is `QUORUM` special?
   - 要点：**A:** With RF=3, quorum is 2 — write and read quorums **overlap** on at least one replica, improving **freshness** vs `ONE`/`ANY` (still not SQL serializability).
65. 🟡 What causes large partition problems?
   - 要点：**A:** Unbounded growth in one partition (e.g. all messages in one channel forever) → slow compactions, heap pressure, repair pain. Mitigate with **time buckets** or **composite partition keys**.
66. 🟡 What is a tombstone?
   - 要点：**A:** A **delete** record that must participate in merges until **GC grace** elapses — delete-heavy workloads need tuning.
67. 🟡 Coordinator role?
   - 要点：**A:** Any node can coordinate; it **routes** to replicas and applies **CL** rules.
68. 🟡 `NetworkTopologyStrategy` vs `SimpleStrategy`?
   - 要点：**A:** **NTS** is **DC/rack aware** for real DR; **Simple** is demos.
69. 🟡 Materialized views — interview stance?
   - 要点：**A:** Convenient but **operational complexity** and **consistency** caveats — many teams prefer **explicit dual writes** to second tables with clear ownership. [← 05](./05-trade-offs.md) · [07 Walkthrough](./07-walkthrough.md)

### [`dynamodb`](../system-design/dynamodb/) — DynamoDB — System design hub

70. 🟡 When do you use `Query` vs `Scan`?
   - 要点：**A:** `Query` targets one **partition key** (and optional sort-key condition) and reads only the matching slice. `Scan` reads the whole table or index. At scale, **`Scan` is for batch jobs or tiny tables**, not user-facing hot paths.
71. 🟡 Why can’t you do “read-your-write” on a GSI for a booking invariant?
   - 要点：**A:** GSIs are **eventually consistent**. For “must see my write immediately,” read the **base table** with **`ConsistentRead`** or design the key so the read hits the primary item directly.
72. 🟡 What breaks if you use a timestamp alone as sort key for chat messages?
   - 要点：**A:** **Collisions** if two messages share the same millisecond. Prefer **time-ordered unique IDs** (ULID, Snowflake, UUIDv7) or a **counter** layered with time.
73. 🟡 How do you model “all orders for user U newest first”?
   - 要点：**A:** Table or GSI with **`PK = user_id`**, **`SK = order_id`** (or inverted time + id). One `Query` with `ScanIndexForward=false`.
74. 🟡 What is write amplification?
   - 要点：**A:** Each **GSI** projection may require an extra write on every base-table mutation. Transactions and Streams consumers add **application-side** work — not free.
75. 🟡 DAX vs ElastiCache Redis?
   - 要点：**A:** **DAX** speaks the DynamoDB API and caches **`GetItem`/`Query`** results with **write-through** when used correctly. **Redis** is generic; you own serialization and invalidation. DAX does **not** cache strongly consistent reads.
76. 🟡 How do you discover hot partitions in production?
   - 要点：**A:** **CloudWatch** throttles, **Contributor Insights** for hot keys, and metrics on **`ConsumedWriteCapacityUnits`** per partition trends. Interview: “I’d verify key distribution and add sharding suffixes or caches.” [← 05](./05-trade-offs.md) · [07 Walkthrough](./07-walkthrough.md)
77. 🔴 [drill] minute drill
   - 要点：Interviewer names a product feature → you respond with **`Query` shape**. They ask for **strong consistency** on a secondary lookup → you move read to **base table** or accept **GSI lag**. They spike one key → you add **cache** or **sharded writes**.
78. 🔴 [drill] Drill prompts (self-serve)
   - 要点：Shopping cart with **guest checkout** **Messaging** threads **Leaderboard** (would you still use DynamoDB or Redis? argue both) [← 19](./19-cost-efficiency.md) · [21 Transcript](./21-one-hour-speaking-transcript.md)

### [`file-cache`](../system-design/file-cache/) — Design a File Cache System

79. 🟡 Why is LRU vulnerable to sequential scans, and how does ARC solve this?
   - 要点：LRU treats every access equally — a sequential scan that touches every file once will push all entries to the head of the LRU list, evicting genuinely hot data. After the scan completes, the cache is cold with scan data that will never be re-accessed. ARC solves this by maintaining two lists: **T1** (accessed once) and **T2** (accessed at least twice).
80. 🟡 What is a cache stampede (thundering herd) and how do you prevent it?
   - 要点：A cache stampede occurs when a popular cache entry expires or is evicted, and hundreds of concurrent requests all experience a cache miss simultaneously. All of them race to fetch from origin, overwhelming the backend.
81. 🟡 How does consistent hashing minimize key redistribution when adding a node?
   - 要点：In consistent hashing, the key space is mapped onto a ring (0 to 2^32-1). Each node is assigned multiple positions (virtual nodes) on the ring. A key is assigned to the first node found clockwise from its hash position.
82. 🟡 What is the difference between cache-aside and read-through patterns?
   - 要点：In **cache-aside**, the client is responsible for the full cache interaction: check cache → on miss, fetch from origin → store result in cache → return to caller. The cache is passive and stores whatever the client gives it. In **read-through**, the client only talks to the cache.
83. 🟡 Why use Direct I/O for the SSD cache tier instead of buffered I/O?
   - 要点：The SSD cache tier already **is** the cache — the data stored there is a cached copy of origin data. Using buffered I/O would cause the OS to cache the SSD data again in the page cache (DRAM), creating a redundant cache-of-a-cache situation. This wastes DRAM that should be used for the L1 memory tier.
84. 🟡 How does TTL interact with invalidation-based coherence?
   - 要点：They serve complementary roles: **Invalidation** handles the common case: when a file changes, the writer publishes an invalidation event, and all cache nodes delete the stale entry within milliseconds.
85. 🟡 What are huge pages and why do they matter for a file cache?
   - 要点：Standard memory pages are 4 KB. A 256 GB memory cache means ~67 million page table entries. The CPU's TLB (Translation Lookaside Buffer) typically holds only 1,000–2,000 entries. At 67 million pages, nearly every memory access is a TLB miss, requiring a slow 4-level page table walk. **2 MB huge pages** reduce the entry count to ~131K.
86. 🟡 How would you handle multi-tenant cache isolation?
   - 要点：Multi-tenant isolation requires preventing one tenant from consuming all cache resources and evicting another tenant's data. **Mechanisms:** **Per-tenant quotas:** Each tenant is allocated a maximum number of bytes in cache. The eviction manager only evicts within a tenant's allocation.
87. 🟡 What is cache poisoning and how do you prevent it?
   - 要点：Cache poisoning occurs when corrupted or malicious data is stored in the cache and served to all subsequent readers. This can happen if: The origin returns an error that is mistakenly cached An attacker manipulates the cache key to store malicious content under a legitimate key A bug in the cache population path stores partial or corrupted data **Prevention: …
88. 🟡 How would you size a file cache cluster?
   - 要点：The sizing process: **Determine the working set** — analyze access logs to find the Zipf exponent α. Compute what percentage of files account for 95% and 99% of accesses. **Size L1 (memory)** — fit the top 1% of files by access frequency. If top 1% = 100K files × 500 KB = 50 GB, provision 64 GB per node (with headroom).
89. 🔴 [drill] Data structures
   - 要点：What data structure gives O(1) get + O(1) eviction? — **HashMap + doubly-linked list.** Map gives O(1) lookup; DLL gives O(1) removal and insertion at head/tail.; How do you implement O(1) LFU? — **Frequency buckets.** Each frequency value has its own DLL. On access, move entry from freq `f` bucket to `f+1` bucket.
90. 🔴 [drill] Architecture
   - 要点：Why multi-tier (L1 memory + L2 SSD + L3 origin)? — **Latency vs capacity trade-off.** Memory: 0.5 ms, 256 GB. SSD: 5 ms, 4 TB. Origin: 100 ms, unlimited. Tiering matches the access frequency curve.; Why consistent hashing over modular hashing? — **Minimal key redistribution.** Adding a node to N moves 1/N keys vs (N-1)/N for modular.
91. 🔴 [drill] Coherence and consistency
   - 要点：How do you keep cache consistent with origin? — **TTL + invalidation.** TTL = safety net (30s). Active invalidation via Redis Pub/Sub = sub-second coherence.
92. 🔴 [drill] Reliability
   - 要点：How do you prevent thundering herd? — **Singleflight** (request coalescing) + **stale-while-revalidate** + probabilistic early refresh. Only 1 origin fetch per key per stampede.; What happens when a cache node crashes? — Consistent hash redistributes keys. L2 SSD survives restart. L1 warms organically.
93. 🔴 [drill] Performance
   - 要点：Why use mmap for L1? — Avoids `read()` syscall overhead. Data accessed via page table — pure memory reads after initial page fault.; Why huge pages? — 256 GB / 4 KB pages = 67M entries → TLB thrashing. 2 MB huge pages = 131K entries → fits TLB.
94. 🔴 [drill] Scaling and operations
   - 要点：How do you size the cache? — **Zipf analysis** of access logs → working set. Top 1% (by freq) = L1 size. Top 10% = L2 size.
95. 🔴 [drill] Drill: Design a Distributed LRU Cache in 10 Minutes
   - 要点：**Step 1 (2 min):** Requirements — N nodes, K million keys, sub-ms hits, LRU eviction. **Step 2 (3 min):** Architecture — Consistent hash ring → cache nodes. Each node: HashMap + DLL. Sharded index (256 shards) for concurrency. **Step 3 (3 min):** Read path — hash(key) → node → shard → map lookup → hit/miss. On hit: move to head.
96. 🔴 [drill] Drill: Explain Cache Stampede to a Non-Technical Stakeholder
   - 要点："Imagine a bestselling book in a library. It's so popular that it's always on the front desk. One day, the front-desk copy gets returned and needs re-shelving. Suddenly, 50 people arrive at once asking for the same book. Instead of all 50 going to the warehouse, the first person goes to fetch it while the other 49 wait at the front desk.
97. 🔴 [drill] Drill: Walk Through a Cache Miss
   - 要点：[← Index](./00-index.md)

### [`file-storage-system`](../system-design/file-storage-system/) — File Storage System（变体：`file-storage-system-design`）

98. 🟡 How would you scale File Storage to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
99. 🟡 What database would you choose for File Storage and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
100. 🟡 How do you handle failures in File Storage?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
101. 🟡 What caching strategy would you use for File Storage?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
102. 🟡 How do you ensure consistency in a distributed File Storage?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`filesystem`](../system-design/filesystem/) — Design a File System

103. 🔴 [drill] Data Structures & Layout
   - 要点：1 — What is an inode? — A fixed-size on-disk structure (typically 256 bytes on ext4) that stores a file's metadata — permissions, timestamps, size, link count — and maps logical blocks to physical blocks via an extent tree or indirect pointers.
104. 🔴 [drill] Journaling & Crash Recovery
   - 要点：6 — What is the journal and why does it exist? — The journal is a write-ahead log that records metadata changes before they're applied to their final on-disk locations.
105. 🔴 [drill] Caching & Performance
   - 要点：11 — What is the page cache? — The page cache maps (inode, file offset) → physical memory page. It caches file data in RAM, serving reads from memory and absorbing writes (write-back mode).
106. 🔴 [drill] Operations & Reliability
   - 要点：16 — What is the safe pattern for crash-consistent file replacement? — Write to a temporary file → `fsync(tmp_fd)` → `rename(tmp, target)` → `fsync(dir_fd)`. The rename is atomic (journaled). If crash occurs before rename, the old file is intact.
107. 🔴 [drill] Design Decision Drills
   - 要点：Database server — ext4 or XFS for a 50 TB PostgreSQL data volume? — XFS: better large-file handling, dynamic inode allocation, parallel allocation groups.
108. 🔴 [drill] "Explain file system journaling in 60 seconds"
   - 要点："A file system journal is a write-ahead log — before any metadata change hits its permanent location on disk, a copy goes into a small dedicated journal area. The journal commit record is the crash-safe boundary: if we crash before the commit, we discard the partial transaction. If we crash after, we replay the committed changes on mount.
109. 🔴 [drill] "Explain the VFS layer in 60 seconds"
   - 要点："The VFS — Virtual File System — is Linux's abstraction layer that provides a uniform POSIX interface to applications regardless of the underlying storage. Whether data lives on ext4, XFS, NFS, or even /proc, the application uses the same open/read/write/close syscalls.
110. 🔴 [drill] "Explain extent trees in 60 seconds"
   - 要点："Traditional Unix file systems used indirect block pointers — a 1 GB file needed 262,000 individual block pointers. Extent trees replaced this with ranges: each extent is a (logical start, physical start, length) tuple. A contiguous 1 GB file needs just one 12-byte extent instead of a megabyte of pointers.

### [`loadbalancer`](../system-design/loadbalancer/) — Loadbalancer（变体：`load-balancer`, `load-balancer-system`, `load-balancer-tests`, `load-balancer-system-design`）

111. 🟡 How would you scale Load Balancer to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
112. 🟡 What database would you choose for Load Balancer and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
113. 🟡 How do you handle failures in Load Balancer?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
114. 🟡 What caching strategy would you use for Load Balancer?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
115. 🟡 How do you ensure consistency in a distributed Load Balancer?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`pastebin`](../system-design/pastebin/) — Pastebin（变体：`paste-bin`, `pastebin-system`, `pastebin-system-design`）

116. 🟡 How would you scale Pastebin to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
117. 🟡 What database would you choose for Pastebin and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
118. 🟡 How do you handle failures in Pastebin?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
119. 🟡 What caching strategy would you use for Pastebin?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
120. 🟡 How do you ensure consistency in a distributed Pastebin?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`postgresql`](../system-design/postgresql/) — PostgreSQL — Key Technology Deep Dive

121. 🟡 Why is PostgreSQL often the default database choice in system design interviews?
   - 要点：PostgreSQL is the safest default because it covers the widest range of requirements: **ACID compliance** — strong consistency and transaction support out of the box **Rich query language** — full SQL with joins, aggregations, window functions, CTEs **Extensibility** — JSONB for semi-structured data, PostGIS for geospatial, pg_trgm for fuzzy search, full-text …
122. 🟡 When would you NOT use PostgreSQL?
   - 要点：Three main scenarios: **Extreme write throughput (>1M writes/sec):** PostgreSQL's WAL architecture bottlenecks at the single-primary level. Use Cassandra, ScyllaDB, or buffer through Kafka. **Global multi-region active-active writes:** PostgreSQL only supports single-primary writes.
123. 🟡 What's the difference between B-tree, GIN, and GiST indexes?
   - 要点：**Key distinctions:** B-tree is the default and handles 90% of cases GIN indexes are larger but support complex containment operators (`@>`, `@@`, `?`) GiST supports spatial operations (`ST_DWithin`, `&&`) and nearest-neighbor (`<->`) BRIN is tiny but only useful when data is physically ordered on disk by the indexed column
124. 🟡 How does PostgreSQL handle concurrent transactions?
   - 要点：PostgreSQL uses **Multi-Version Concurrency Control (MVCC)**. Each transaction sees a snapshot of the database — readers never block writers and vice versa. **Three isolation levels with increasing strictness:** **Read Committed (default):** Each statement sees the latest committed data.
125. 🟡 Explain replication lag and read-your-writes consistency.
   - 要点：**Replication lag** is the delay between a write committed on the primary and that write being visible on a replica. With async replication, this is typically milliseconds to seconds. **The read-your-writes problem:** **Solutions:** **Interview tip:** always mention replication lag when proposing read replicas.
126. 🟡 How would you handle a table with 500M rows?
   - 要点：**Table partitioning** is the primary tool. The approach depends on access patterns: **Time-series data (most common):** **Even distribution by key:** **Additional strategies:** **Indexes** — ensure queries always use indexes; partial indexes for hot subsets **Archival** — move cold data to separate tables or cold storage **Materialized views** — precompute …
127. 🟡 When would you use JSONB over a separate NoSQL store?
   - 要点：**Use JSONB when:** Flexible attributes vary per row (product metadata, user preferences) JSONB fields are queried alongside relational columns in the same query You want a single database to manage (operational simplicity) The JSONB data is secondary — not the primary access pattern Scale is moderate (up to hundreds of millions of rows) **Use a separate NoS …
128. 🟡 How does PostgreSQL's WAL ensure durability?
   - 要点：The **Write-Ahead Log (WAL)** guarantees that committed data survives crashes: **Write path:** Client writes → data modified in buffer cache (memory) → WAL record written and fsynced to disk → client receives ACK **Key invariant:** WAL is flushed to disk *before* the client is told the write succeeded **Crash recovery:** On restart, PostgreSQL replays all WA …
129. 🟡 PostgreSQL vs DynamoDB for a social media feed?
   - 要点：**It depends on scale and access patterns:** **Recommended hybrid approach at scale:** **PostgreSQL** for user profiles, relationships, posts (source of truth) **Redis** for precomputed feed cache (fast reads) **Kafka** for async fanout-on-write (decouple write from fan-out) **DynamoDB or Cassandra** for feed storage if Redis eviction is a problem at scale * …
130. 🟡 How to implement optimistic concurrency control in PostgreSQL?
   - 要点：Add a `version` column and use conditional updates: **Application-level retry loop:** **When to use OCC vs pessimistic locking:** OCC: high read volume, low write contention (user profiles, product details) Pessimistic (`SELECT FOR UPDATE`): critical sections with frequent contention (inventory, payments) [← When to Use](./05-when-to-use.md) / [Next: Cheat S …

### [`pubsub`](../system-design/pubsub/) — Pubsub（变体：`pub-sub-system-design`, `pub-sub-educative-tests`）

131. 🟡 How would you scale Pub-Sub to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
132. 🟡 What database would you choose for Pub-Sub and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
133. 🟡 How do you handle failures in Pub-Sub?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
134. 🟡 What caching strategy would you use for Pub-Sub?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
135. 🟡 How do you ensure consistency in a distributed Pub-Sub?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`rate-limiter`](../system-design/rate-limiter/) — Rate Limiter（变体：`ratelimiter`, `rate-limiter-design`, `rate-limiter-system`, `rate-limiter-system-design`, `rate-limiter-educative-tests`）

136. 🟡 Why place the rate limiter at the API Gateway instead of in each service?
   - 要点：**API Gateway** gives centralized control — one place to enforce all rules, blocked requests never reach backend, and you avoid the N-server coordination problem (in-process limiters each see only 1/Nth of traffic, allowing N× the intended limit). Trade-off: gateway only has HTTP request context, not deep business logic.
137. 🟡 Why Token Bucket over Fixed Window or Sliding Window Log?
   - 要点：Token Bucket stores only 2 values per client (vs thousands of timestamps), handles bursts naturally (bucket capacity = burst size), and enforces a steady refill rate. Stripe uses Token Bucket for these reasons.
138. 🟡 How do you prevent race conditions in Redis?
   - 要点：The entire read-modify-write (check tokens → calculate refill → decrement → update) runs in a **single Redis Lua script**. Lua scripts execute atomically in Redis — no other command can interleave.
139. 🟡 Should the system fail-open or fail-closed when Redis is down?
   - 要点：**Fail-closed** for a social media platform. Rate limiter outages often coincide with traffic spikes (the cause of the outage). Failing open during a spike sends ALL traffic to the backend → cascading failure → total platform outage. Brief 429 responses are preferable to cascading collapse. Financial systems also prefer fail-closed.
140. 🟡 How do you scale to 1M requests/second?
   - 要点：Single Redis handles ~100K ops/sec. Use **Redis Cluster** with 10+ shards: Keys auto-distributed across 16,384 hash slots Client ID hashed to determine shard → all requests for one client hit same shard Each shard: master + replica for HA Gateways connect to cluster; routing is transparent No custom consistent hashing needed — Redis Cluster handles it.
141. 🟡 How do you handle users behind corporate NATs sharing one IP?
   - 要点：Set **higher IP-based limits** (e.g., 1000/min vs 100/min for user-based). Layer multiple rules: IP limit + user limit + endpoint limit. Rely primarily on **authenticated user limits** (user ID from JWT). IP-based limiting is a fallback for unauthenticated traffic, not the primary enforcement mechanism.
142. 🟡 How do you update rate limit rules without redeploying?
   - 要点：Two approaches: **Poll-based**: Gateways query a config DB every 30 s and cache rules locally. Simple, 30 s max staleness. **Push-based (ZooKeeper)**: Changes pushed to all gateways instantly via persistent connections. More complex but needed for emergency rule changes (e.g., blocking an ongoing attack).
143. 🟡 What HTTP headers should the 429 response include?
   - 要点：These headers let well-behaved clients implement proper backoff instead of hammering the API with retries. [← Back to index](./00-index.md)
144. 🟢 [速答] Why not in-process only?
   - 要点：Each instance sees 1/N traffic → **N× burst** unless coordinated.
145. 🟢 [速答] Fixed window vs token bucket?
   - 要点：Fixed window **doubles** allowed traffic at boundaries; token bucket **smooths** bursts.
146. 🟢 [速答] Sliding window log cost?
   - 要点：**O(events)** memory — too heavy at high RPS.
147. 🟢 [速答] How to limit 10M distinct IPs?
   - 要点：**Bloom filter** admission + Redis for suspects only; or **CDN** IP throttle.
148. 🟢 [速答] Multi-region?
   - 要点：**Regional buckets** + optional async sync; or **global Redis** with latency hit.
149. 🟢 [速答] Exactly-once consumption?
   - 要点：Not needed; **at-most-once** debit per request is fine.
150. 🟢 [速答] Test atomicity?
   - 要点：Parallel load test same key; verify count matches expected.

### [`webcrawler`](../system-design/webcrawler/) — Webcrawler（变体：`webcrawlers`, `web-crawler-system`, `web-crawler-tests`, `web-crawler-system-design`）

151. 🟡 How would you scale Web Crawler to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
152. 🟡 What database would you choose for Web Crawler and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
153. 🟡 How do you handle failures in Web Crawler?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
154. 🟡 What caching strategy would you use for Web Crawler?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
155. 🟡 How do you ensure consistency in a distributed Web Crawler?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

## 三、产品端到端设计（`products`，23 个主题，132 题）

### [`amazon-food-delivery-launch`](../system-design/amazon-food-delivery-launch/) — Amazon restaurant food delivery — launch (product & strategy hub)

156. 🔴 [drill] Product / strategy angle
   - 要点：**“Why a standalone app?”** — **Iteration** velocity and app-store presence vs embedding only in **retail**; trade **distribution** for **independent** release cadence; **identity** and **Prime** **tie-ins** must be explicit.
157. 🔴 [drill] Operations & marketplace
   - 要点：**“What if incumbents match discounts?”** — Expected; **defend** on **reliability**, **ETAs**, **refunds**, and **restaurant** **fairness**, not only **price**. **“What breaks ETAs more than distance?”** — **Prep** **variance**, **restaurant** **accept** **bursts**, **batching** **decisions**, **traffic**, **weather**, **courier** **scarcity**.
158. 🔴 [drill] When they pivot to system design
   - 要点：**“How does the order actually move?”** — **Bridge** to [food-delivery/00-index.md](../food-delivery/00-index.md): **orchestration**, **idempotency**, **dispatch**, **search** / [folder-search-api/00-index.md](../folder-search-api/00-index.md) as needed. [← 19](./19-cost-efficiency.md) · [21](./21-one-hour-speaking-transcript.md)

### [`e-commerce`](../system-design/e-commerce/) — E-commerce platform

159. 🔴 [drill] Clarifying questions (first 3 minutes)
   - 要点：Geos, **B2B vs B2C**, **marketplace** vs 1P, **peak** (events), **compliance** (PCI, minors). **SLA** for checkout vs browse; **return** and **refund** in scope? Is **recommendation** in scope for deep dive or “nice to have”?
160. 🔴 [drill] Common follow-ups
   - 要点：Hot SKU oversell? — **Reservation** in DB/Redis, **version** or single-writer; **queue** checkout per SKU in extreme case; Double charge? — **Idempotency** keys, **PSP** state check before retry; Search freshness? — **Near-real-time** index updates; **stale-OK** for browse with labels

### [`ecommerce-microservices`](../system-design/ecommerce-microservices/) — E-commerce microservices

161. 🔴 [drill] Clarifiers
   - 要点：**How many** services vs a **modular monolith**? (Mention **strangler** if brownfield.) **Sync vs event-first** for order flow—pick one story and stay consistent. **Mesh** optional (Istio/Linkerd)—only if interviewer goes deep on **mTLS** and **canary**.
162. 🔴 [drill] Drills
   - 要点：Monolith vs micro? — **Team** and **scale** fit; start **modular monolith** + **outbox** to migrate; **Distributed debug**? — **Traces** + **correlation**; feature flags to **disable** non-critical paths; **Data** duplication? — **Read models** from events; **projections** in search vs OLTP store
163. 🔴 [drill] Third-party prompts
   - 要点：In-repo **00-index** and **22**-style **link-only** tables for Exponent / course URLs—**not** pasted solutions. [← Index](./00-index.md)

### [`food`](../system-design/food/) — Food — Food Delivery Marketplace System Design

164. 🔴 [drill] STAR bridge
   - 要点：When interviewers pivot to behavioral, use the food delivery domain for: **Prioritization:** how to triage between improving ETA accuracy vs reducing dispatch latency → [bq/prioritize-tasks/00-index.md](../bq/prioritize-tasks/00-index.md).

### [`food-delivery`](../system-design/food-delivery/) — Food delivery marketplace — system design hub（变体：`food-delivery-system`）

165. 🔴 [drill] Behavioral bridges (Amazon LP–class)
   - 要点：**Customer obsession:** transparent ETA when kitchen is slow. **Insist on highest standards:** price snapshot so we never charge the wrong amount. **Dive deep:** explain why courier pings don’t live on the order row.

### [`google-docs`](../system-design/google-docs/) — Google Docs — System Design Hub（变体：`google-docs-system`, `google-docs-demo`, `google_docs`）

166. 🟡 Why can't you just send the full document on every edit?
   - 要点：Two problems: (1) **Bandwidth** — a fast typer would send the entire document (potentially 100s of KB) on every keystroke. (2) **Last-writer-wins** — if two users edit concurrently and send their full document, whichever arrives last overwrites the other's changes entirely.
167. 🟡 What is Operational Transformation (OT) and why does Google Docs use it?
   - 要点：OT transforms each operation based on operations that precede it, adjusting positions so the intent is preserved regardless of arrival order. Example: if INSERT(5, ", world") arrives before DELETE(5), the delete's position is shifted to 12 to still target the original character.
168. 🟡 How do CRDTs differ from OT, and when would you choose CRDTs?
   - 要点：CRDTs assign each character a unique fractional position ID that never changes. Inserts create new IDs between existing ones; deletes mark as tombstones. Operations are **commutative** — any order produces the same result, so no central server is needed.
169. 🟡 Why do clients also need to run OT, not just the server?
   - 要点：Editors apply their own changes **immediately** (optimistic update) before the server confirms them. If another editor's operation is committed on the server first, the local client has already applied its own op but hasn't seen the remote op yet. The perceived operation order differs between clients.
170. 🟡 How do you scale WebSocket connections to millions of concurrent editors?
   - 要点：Use a **consistent hash ring** (managed by ZooKeeper) to distribute documents across Document Service servers. All editors of the same document connect to the same server (required by OT's central ordering). When a client connects, any server can check the hash ring and redirect to the correct server.
171. 🟡 Why store operations in Cassandra instead of PostgreSQL?
   - 要点：Operations are **append-only** and write-heavy (~500K ops/sec globally). Cassandra excels at fast sequential writes with partition-level ordering. We partition by `(docId, versionId)` and cluster by `seq_num` — perfect for Cassandra's data model. PostgreSQL would work at small scale but struggles with this write pattern at billions of documents.
172. 🟡 What is operation compaction and why is it necessary?
   - 要点：A document with 10,000 ops means every new editor must download and replay 10,000 operations before they can start editing. Compaction collapses all operations into a single INSERT of the final document text. This reduces storage, speeds up document loading, and keeps the in-memory footprint small.
173. 🟡 How do you handle cursor positions and user presence?
   - 要点：Cursor and presence are **ephemeral** — they only matter while a user is connected. Store them **in-memory** on the Document Service (not in any database). When a user moves their cursor, broadcast the position to all other editors via the same WebSocket.
174. 🟡 What happens when a Document Service server crashes?
   - 要点：All editors connected to that server are disconnected. Clients auto-reconnect with exponential backoff. The hash ring is updated (ZooKeeper detects the failure), and the document's hash range is reassigned to another server. The new server loads all operations from Cassandra and rebuilds the in-memory state.
175. 🟡 How would you add offline editing support to this design?
   - 要点：OT is poorly suited for offline (needs server for ordering). You'd either: (1) Switch to **CRDTs** — clients buffer ops locally in IndexedDB, merge on reconnect with guaranteed convergence.

### [`instagram`](../system-design/instagram/) — Instagram（变体：`instagram-system`, `instagram-tests`, `instagram-system-design`）

176. 🟡 How would you scale Instagram to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
177. 🟡 What database would you choose for Instagram and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
178. 🟡 How do you handle failures in Instagram?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
179. 🟡 What caching strategy would you use for Instagram?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
180. 🟡 How do you ensure consistency in a distributed Instagram?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`live-streaming-platform`](../system-design/live-streaming-platform/) — Live Streaming Platform（变体：`live-streaming-platform-detailed`）

181. 🟡 Why use HLS over WebRTC for a live streaming platform with millions of viewers?
   - 要点：HLS (HTTP Live Streaming) uses standard HTTP, which means every piece of infrastructure built for the web — CDNs, load balancers, caches, proxies — works out of the box. A single origin server can serve millions of viewers through CDN fan-out because segments are cacheable HTTP resources.
182. 🟡 A streamer with 10 followers suddenly goes viral and hits 500K concurrent viewers in 5 minutes. How does the system handle this?
   - 要点：This is the **hot partition problem**. The system handles it in layers: **CDN absorbs 99.9% of traffic.** Each of 200+ CDN edge PoPs caches HLS segments. Viewers are served from edge cache — origin never sees most of the traffic.
183. 🟡 How do you guarantee chat message ordering in a distributed WebSocket system?
   - 要点：**Short answer:** You don't guarantee strict global ordering — and you don't need to. Chat messages flow through multiple WebSocket gateways, each publishing to Redis Pub/Sub independently. Messages from different users may arrive at different gateways in different orders.
184. 🟡 How does CDN cache invalidation work for live content vs static content?
   - 要点：Live streaming inverts the normal CDN caching model: **Static content (VOD):** Long TTL (days/weeks), explicit invalidation on update. Cache hit ratio >99%. **Live content:** The *playlist* changes every 2 seconds. The *segments* are immutable. There is **no explicit cache invalidation** for live segments.
185. 🟡 How would you reduce glass-to-glass latency from 10s to under 3s?
   - 要点：Each stage of the pipeline contributes latency. To get below 3s: **Resulting budget:** The cost: more CDN requests (10x more partials), slightly worse compression (no B-frames), and more complex player logic.
186. 🟡 Why not just use WebSockets for video delivery instead of HLS?
   - 要点：WebSockets maintain a persistent TCP connection per viewer. For 1M concurrent viewers, that's 1M open TCP connections. Each connection consumes: Server memory: ~10KB per connection = 10GB for 1M viewers File descriptors: 1M FDs (requires kernel tuning) No caching: each viewer gets a dedicated data stream, CDNs can't help With HLS, viewers make independent HT …
187. 🟡 How do you handle a broadcaster with an unstable network connection?
   - 要点：Broadcaster network instability manifests as: **Bitrate drops** — source quality degrades **Packet loss** — frames are corrupted or lost **Connection drops** — stream disconnects entirely **Ingest-side mitigations:** **SRT protocol** — if the broadcaster uses SRT instead of RTMP, the protocol has built-in ARQ (Automatic Repeat Request) that retransmits lost …
188. 🟡 How would you design the system to support 100K concurrent live streams?
   - 要点：100K concurrent streams means 100K independent ingest + transcoding pipelines running simultaneously. The main challenge is **resource allocation** for transcoding.

### [`live-streaming-system`](../system-design/live-streaming-system/) — Live Streaming System（变体：`live-streaming-system-design`）

189. 🟡 How would you scale Live Streaming to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
190. 🟡 What database would you choose for Live Streaming and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
191. 🟡 How do you handle failures in Live Streaming?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
192. 🟡 What caching strategy would you use for Live Streaming?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
193. 🟡 How do you ensure consistency in a distributed Live Streaming?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`online-education-system-design`](../system-design/online-education-system-design/) — Online Education

194. 🟡 How would you scale Online Education to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
195. 🟡 What database would you choose for Online Education and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
196. 🟡 How do you handle failures in Online Education?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
197. 🟡 What caching strategy would you use for Online Education?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
198. 🟡 How do you ensure consistency in a distributed Online Education?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`payment`](../system-design/payment/) — Payment System (Stripe)（变体：`payment-tests`）

199. 🟡 Why does Stripe use PaymentIntent instead of a simple "charge" API?
   - 要点：PaymentIntent separates the **intent to collect** from the **actual charge**. This enables: **Idempotent retries**: same `PaymentIntent` ID + idempotency key = safe to retry **Multi-step lifecycle**: created → authorized → captured (authorization and capture can be split for hotel/rental use cases) **One-to-many**: a single PaymentIntent can have multiple Tr …
200. 🟡 How do you prevent double-charging when the merchant retries?
   - 要点：**Idempotency keys.** Every mutating API call includes an `Idempotency-Key` header. On first request, we execute the operation and cache the response (keyed by hash of idempotency key). On retry with the same key, we return the cached response without re-executing. Implementation: `SELECT ...
201. 🟡 Why use CDC instead of dual-write for the audit trail?
   - 要点：**Dual-write** (update main table + insert audit record) has two problems: A developer can forget the audit insert → silent data loss If the audit insert fails mid-transaction, you lose the audit record **CDC** (Change Data Capture from PostgreSQL WAL) solves both: Every DB write is **automatically** captured at the database level — no application code neede …
202. 🟡 How do you ensure card data security across the system?
   - 要点：Three layers of defense (defense in depth): **iframe isolation**: JS SDK creates an iframe from our domain → browser same-origin policy blocks merchant code from accessing card data **Client-side encryption**: SDK encrypts card data with our RSA public key before it leaves the browser → even if iframe is compromised, attacker gets ciphertext **HSM decryption …
203. 🟡 How does webhook delivery handle failures?
   - 要点：Payment status change → Kafka event → webhook consumer POST to merchant's registered URL with **HMAC signature** (merchant verifies authenticity) Expect HTTP 2xx within 5 seconds On failure: **exponential backoff** — 1s, 2s, 4s, 8s, ...
204. 🟡 How do you handle payment network timeouts?
   - 要点：Payment networks (Visa, MC) are external and can timeout. Strategy: Set a **5-second timeout** on the auth request On timeout, Transaction status → `PENDING` (not failed — we don't know if it went through) **Reconciliation worker** checks with payment network after T+1 for the real outcome Merchant sees status `PENDING` — they should NOT fulfill the order ye …
205. 🟡 What database would you choose and why?
   - 要点：**PostgreSQL** for the primary payment database: **ACID transactions** are critical for financial data (no partial updates) **Strong consistency** — cannot tolerate eventual consistency for balances **Joins** for reporting (PaymentIntents × Transactions × Merchants) **Mature ecosystem** for tooling, monitoring, CDC (Debezium) DynamoDB/Cassandra are wrong cho …
206. 🟡 How do you test idempotency in a payment system?
   - 要点：Call the create endpoint twice with the **same idempotency key and params** → assert same response, same PaymentIntent ID, only one transaction created Call with **same key but different params** → assert error (prevents misuse) Test **concurrent retries** → use threading/locking to verify only one execution Test **key expiry** → after TTL, same key creates …
207. 🟡 How do you test a payment state machine?
   - 要点：Test both valid and invalid transitions: **Happy path**: created → processing → authorized → captured → settled **Failure path**: created → processing → failed **Invalid**: failed → captured (must raise error), captured → authorized (must raise error) **Edge**: processing → processing (idempotent retry should be safe) Use parameterized tests to enumerate all …
208. 🟡 Why mock the payment network instead of using a sandbox?
   - 要点：**Speed**: Mocks run in microseconds; sandbox calls take 100+ ms **Determinism**: Mocks return configured results; sandboxes can have transient failures **CI compatibility**: No API keys or network access needed in CI **Edge case control**: Can simulate timeouts, partial failures, specific error codes Trade-off: You lose confidence that the real integration …

### [`prime-video`](../system-design/prime-video/) — Design Prime Video — System design hub

209. 🟡 Why does Prime Video use adaptive bitrate streaming instead of serving a single fixed-quality stream?
   - 要点：Network conditions are **heterogeneous and dynamic** — a user on 4G may have 5 Mbps one moment and 1 Mbps the next. A fixed-quality stream either **buffers** (if bitrate exceeds bandwidth) or **wastes quality** (if set too low). ABR solves this by offering **multiple renditions** (240p–4K) via an encoding ladder.
210. 🟡 What is CENC and why is it important for multi-DRM support?
   - 要点：**CENC (Common Encryption Standard, ISO 23001-7)** defines a standard way to encrypt media content using **AES-128-CTR** such that a single encrypted file can be decrypted by **multiple DRM systems** (Widevine, FairPlay, PlayReady).
211. 🟡 Explain the CDN cache hierarchy for video streaming. Why not serve directly from S3?
   - 要点：Serving directly from S3 would mean every segment request hits the origin, which is: **Slow** — S3 latency is 50–200ms vs CDN edge < 10ms **Expensive** — S3 egress costs ~$0.09/GB; CDN is ~$0.02–0.04/GB at scale **Unreliable** — S3 can throttle under high request rates The **three-tier hierarchy** is: **L1 — Edge PoP** (200+ locations): Closest to users.
212. 🟡 How would you handle a massive premiere event (e.g., new season launch) without overwhelming the origin?
   - 要点：**CDN prewarming:** **T-24h:** Push all segments for premiere episodes to L2 regional caches. **T-2h:** Push to high-traffic L1 PoPs (top 20 cities by viewership). **T-0:** At launch, virtually all requests are served from warm CDN cache.
213. 🟡 Why use a message queue between upload and transcoding instead of synchronous processing?
   - 要点：**Decoupling:** Upload and transcode have vastly different resource profiles. Upload is I/O-bound (network transfer); transcode is CPU/GPU-bound. A queue lets each side scale independently. **Reliability:** If a transcoding worker crashes, the message remains in the queue and is re-processed after the visibility timeout. No data loss.
214. 🟡 Compare collaborative filtering vs content-based filtering for video recommendations.
   - 要点：**Prime Video uses both (hybrid):** **Collaborative** for personalized carousels ("Because you watched...") **Content-based** for new release boosting and cold-start users **Popularity-based** as a fallback for anonymous/new users A **ranking model** (typically a neural network or gradient-boosted trees) combines all signals into a final ordered list
215. 🟡 What happens if the DRM license server is unavailable during playback?
   - 要点：**Impact:** The player cannot obtain decryption keys, so new content cannot start playing. However, **currently playing content is not interrupted** — the player already has the license for the current session. **Mitigations:** **License caching:** Players cache licenses for a configurable duration (e.g., 24 hours for offline playback).
216. 🟡 Why might Prime Video choose AV1 codec over H.265 for 4K content?
   - 要点：**Decision:** Use AV1 for **popular 4K content** where the bandwidth savings justify the encoding cost. For long-tail content, H.265 is more cost-effective. Netflix reported **20% bandwidth savings** by switching top titles to AV1. The encoding cost is a **one-time investment** amortized across millions of views.
217. 🟡 How does the playback resume feature work across devices?
   - 要点：**Position sync:** During playback, the player sends `PUT /playback/{session_id}/position` every **10 seconds** with the current timestamp. **Server storage:** The Playback Service writes `{user_id, title_id, position_sec, updated_at}` to **Redis** (fast writes) and asynchronously persists to **DynamoDB** (durable).
218. 🟡 What is the difference between an HLS master manifest and a media playlist?
   - 要点：**Master manifest** (also called multivariant playlist): Lists all available **renditions** (resolutions/bitrates) Player uses this to discover what quality options exist Fetched once at playback start **Media playlist** (per-rendition): Lists the actual **segments** (`.ts` or `.mp4` chunks) for one rendition Player fetches this repeatedly during playback (f …
219. 🔴 [drill] "How would you add live streaming?"
   - 要点：Add **live encoder** (AWS MediaLive) that ingests RTMP/SRT feeds Produce segments in real-time (2-second duration for low latency) **LL-HLS** with partial segments (CMAF chunks) for < 3-second glass-to-glass **Rolling-window manifest** updated every segment duration **DVR buffer** in S3 for rewind (2-hour sliding window) CDN cache TTLs drop to 2 seconds for …
220. 🔴 [drill] "How would you handle ad insertion?"
   - 要点：**SSAI (Server-Side Ad Insertion):** Stitch ads into the manifest at the server/CDN edge Player sees a seamless stream (no client-side ad SDK) Ad decision server called at manifest generation time with user context Prevents ad blockers (ads are indistinguishable from content segments)
221. 🔴 [drill] "What about offline downloads?"
   - 要点：Player requests **offline DRM license** (extended duration: 48h rental, 30 days purchase) Download segments to **encrypted local storage** (no clear content on disk) License renewal check on reconnection Storage limit per device (e.g., 25 titles max)
222. 🔴 [drill] "How do you prevent account sharing?"
   - 要点：Track **concurrent streams** per account (limit: 3) **Device fingerprinting:** flag if streams from > 5 unique devices/month **IP diversity check:** flag if streams from geographically distant IPs simultaneously Offer **household plans** as a legitimate alternative
223. 🔴 [drill] STAR-ready talking points
   - 要点：For behavioral tie-ins during system design:

### [`public-transit-system`](../system-design/public-transit-system/) — Public Transit System

224. 🟡 How would you scale Public Transit System to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
225. 🟡 What database would you choose for Public Transit System and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
226. 🟡 How do you handle failures in Public Transit System?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
227. 🟡 What caching strategy would you use for Public Transit System?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
228. 🟡 How do you ensure consistency in a distributed Public Transit System?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics. [← Back to index](./00-index.md)

### [`quora`](../system-design/quora/) — Quora（变体：`quora-tests`, `quora-system-design`）

229. 🟡 How would you scale Quora to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
230. 🟡 What database would you choose for Quora and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
231. 🟡 How do you handle failures in Quora?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
232. 🟡 What caching strategy would you use for Quora?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
233. 🟡 How do you ensure consistency in a distributed Quora?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`robinhood`](../system-design/robinhood/) — Robinhood

234. 🟡 Why SSE instead of WebSockets for live stock prices?
   - 要点：SSE is **unidirectional** (server → client) and runs over **HTTP** — no separate protocol needed. Stock prices are server-push only (client doesn't send price data back). SSE has **built-in auto-reconnect**, simpler load balancer config, and works with existing HTTP infrastructure.
235. 🟡 Why not use a message queue between Order Service and Exchange?
   - 要点：Latency. Our SLA is < 200 ms for order placement. During traffic spikes, a queue can build up backlog before auto-scaling kicks in. For a user trying to buy/sell a volatile stock, waiting for queue consumers to process ahead of them is unacceptable.
236. 🟡 Why store order as `pending` before calling the Exchange?
   - 要点：**Safety-first pattern.** If we call the exchange first and our system crashes after the exchange accepts the order, we have an outstanding order with no record in our database. By writing `pending` first, we always have a record. If the exchange call fails, we mark it `failed`.
237. 🟡 How does Redis Pub/Sub scale for 50K price updates/sec?
   - 要点：Redis Pub/Sub handles ~1M messages/sec on a single instance. For 50K updates/sec we're well within capacity. Each Symbol Service server subscribes only to channels for symbols its connected users care about — so load is self-regulating. If needed, partition Redis by symbol prefix (e.g., A-M on shard 1, N-Z on shard 2).
238. 🟡 Why RocksDB instead of a secondary index on the Order DB?
   - 要点：Order DB is **partitioned by userId**. A secondary index on `externalOrderId` would require a **cross-shard scatter query** (checking every partition) to find which user's order corresponds to a trade. RocksDB provides O(1) key-value lookup: `externalOrderId → (orderId, userId)`, then route to the correct partition.
239. 🟡 How do you handle a partially filled limit order?
   - 要点：The trade feed sends multiple trade events for the same `externalOrderId` as the order is partially filled. Each trade event includes the number of shares filled. The Trade Processor looks up the order via RocksDB, updates the `filled_shares` count in the Order DB. When `filled_shares == total_shares`, status changes to `filled`.
240. 🟡 What happens during an exchange outage?
   - 要点：Display "Market unavailable" in the UI. New order submissions return an error immediately (fail-fast). Existing orders remain in their current state. The cleanup job pauses exchange queries. When the exchange recovers, the cleanup job resumes reconciliation of any `pending` or `pending_cancel` orders.
241. 🟡 How do you prevent duplicate orders?
   - 要点：**Idempotency key** on POST /order — client generates a unique key per order intent. Order Service checks for existing order with that key before processing. If found, return the existing order. The exchange also supports `clientOrderId` which prevents duplicate submissions on their side. This protects against network retries and client-side double-taps.

### [`spotify`](../system-design/spotify/) — Spotify（变体：`spotify-tests`, `spotify-system-design`）

242. 🟡 How would you scale Spotify to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
243. 🟡 What database would you choose for Spotify and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
244. 🟡 How do you handle failures in Spotify?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
245. 🟡 What caching strategy would you use for Spotify?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
246. 🟡 How do you ensure consistency in a distributed Spotify?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`stock-exchange`](../system-design/stock-exchange/) — Stock Exchange

247. 🟡 Why single-threaded per symbol instead of a multi-threaded matching engine?
   - 要点：A single-threaded matching engine eliminates **all lock contention** and produces **deterministic** behavior (critical for replay/audit). At the per-symbol level, even the busiest ticker doesn't exceed one CPU core's throughput. Multi-threading would add latency from locks and make event-sourced replay non-deterministic.
248. 🟡 Why use a centralized sequencer instead of distributed ordering?
   - 要点：**Fairness is a regulatory requirement.** If two orders arrive at the same price, the one that arrived first must be matched first (price-time priority). A centralized sequencer assigns a globally monotonic sequence number, guaranteeing strict FIFO.
249. 🟡 Why UDP multicast for L1 market data instead of TCP?
   - 要点：UDP multicast sends **one packet** that all subscribers receive simultaneously — O(1) fan-out regardless of subscriber count. For 10K subscribers, TCP would require 10K separate sends. The trade-off is reliability: subscribers must handle packet loss via sequence number gaps and retransmission requests. This is standard practice at NYSE, NASDAQ, and CME.
250. 🟡 How do you recover an order book after a matching engine crash?
   - 要点：Load the **latest snapshot** (taken every ~60 seconds), then **replay events** from the event store since the snapshot timestamp. Validate the reconstructed state against the last known sequence number. With hot standby, failover takes < 1 second — the shadow engine already has identical state and just gets promoted.
251. 🟡 Why event sourcing instead of just persisting current state?
   - 要点：Regulatory requirement. SEC and MiFID II require a complete audit trail of every order action. Event sourcing provides: (1) full audit history, (2) ability to replay and reconstruct state at any point in time, (3) debugging capability for matching disputes. Periodic snapshots keep recovery time manageable.
252. 🟡 How do you handle a partial fill?
   - 要点：When a large order matches against multiple smaller orders at the same price level, the matching engine generates multiple `OrderMatched` events — one per fill. The order's `filledQty` is updated incrementally. The order remains in the book until `filledQty == quantity` (fully filled) or the user cancels the remainder.
253. 🟡 What is the LMAX Disruptor pattern and why use it?
   - 要点：A **lock-free ring buffer** that eliminates contention between producer (gateway) and consumer (matching engine). Pre-allocated entries mean zero GC pressure. Cache-line padding prevents false sharing. BusySpinWaitStrategy gives lowest possible latency (at the cost of burning a CPU core).
254. 🟡 How do you prevent a single hot symbol from affecting others?
   - 要点：Symbols are **sharded across CPU cores**. Hot symbols (AAPL, TSLA during earnings) get **dedicated cores** with no co-tenants. Circuit breakers halt trading if price moves > 10% in 5 minutes. Per-member rate limits prevent any single broker from overwhelming a symbol's matching engine. Queue depth monitoring alerts when the ring buffer exceeds 80% capacity.

### [`stock-trading-platform`](../system-design/stock-trading-platform/) — Stock Trading Platform

255. 🟡 Why PostgreSQL over DynamoDB for order storage?
   - 要点：Financial systems demand **ACID guarantees**. Orders involve complex queries (join with trades, filter by date/status/symbol, aggregate for reports). PostgreSQL provides transactions, foreign keys, and rich SQL. DynamoDB's eventual consistency and limited query patterns are inadequate for regulatory audit trails and financial reconciliation.
256. 🟡 How do you implement fractional shares when exchanges only trade whole shares?
   - 要点：Use an **omnibus (pooled) account**. The broker buys whole shares on the exchange and allocates fractions internally via a ledger. When a user buys 0.5 shares of AAPL, the broker either (1) matches against another user selling 0.5 shares internally, or (2) buys 1 whole share and holds 0.5 in inventory. The broker takes inventory risk on unmatched fractions.
257. 🟡 How does smart order routing achieve best execution?
   - 要点：Subscribe to the **consolidated market data feed (SIP)** for real-time NBBO across all exchanges. For each order, compare available liquidity and prices at NYSE, NASDAQ, BATS, IEX, etc. Route to the venue with the best price. For large orders, **split across multiple venues** to minimize market impact.
258. 🟡 Why WebSocket instead of SSE for a trading platform?
   - 要点：Unlike a pure price feed (server → client), a trading platform needs **bidirectional** communication. Users dynamically subscribe/unsubscribe to symbols, place orders, and receive confirmations — all over the same connection. SSE's 6-connection-per-domain browser limit is also problematic for a feature-rich trading UI with multiple data streams.
259. 🟡 How do you handle tax lot accounting for sell orders?
   - 要点：Each purchase creates a **TaxLot record** (shares, costBasis, purchaseDate). On sell, apply the user's selected method: **FIFO** (oldest first), **LIFO** (newest first), **Specific ID** (user picks), or **Average Cost** (mutual funds). Calculate realized gain/loss per lot. Track holding period (> 1 year = long-term capital gains, lower tax rate).
260. 🟡 How do you scale portfolio valuation for 2M concurrent users?
   - 要点：Maintain a **reverse index** in Redis: `Symbol → Set[userId]`. When AAPL's price updates, look up all users holding AAPL and push delta P&L updates via WebSocket. This avoids re-valuing entire portfolios on every tick — only affected positions are recalculated. Holdings (source of truth) stay in PostgreSQL; real-time prices cached in Redis.
261. 🟡 How do you handle an exchange outage?
   - 要点：**Circuit breaker per exchange.** If latency > 2s or error rate > 5%, stop routing to that exchange. Re-route orders to alternate venues (multi-exchange connectivity). Display degraded mode in the UI (e.g., "Some exchanges temporarily unavailable — orders may execute at slightly different prices").
262. 🟡 What's the biggest consistency challenge in a trading platform?
   - 要点：**Account balance vs order state.** When a user places a buy order, we must reserve funds (buying power check) atomically with order creation. If the order is rejected by the exchange, we must release the reservation. If the system crashes between exchange acceptance and DB update, a cleanup job must reconcile.

### [`ticketing`](../system-design/ticketing/) — Peak-traffic ticketing — system design hub

263. 🟡 How do you prevent two users buying the same seat?
   - 要点：**Authoritative write** in OLTP with **row lock** or **conditional update** (`WHERE status = 'available'`). Optional Redis hold must **confirm** in DB before payment capture. Never “check then act” across two requests without locking.
264. 🟡 Why use a waiting room?
   - 要点：Protects origin from **thundering herd**; converts unbounded concurrency into **admission-controlled** RPS; gives a place to run **bot checks** and **rate limits**.
265. 🟡 Where does Elasticsearch fit?
   - 要点：**Search / filter** over events (geo, text, facets). **Not** for inventory commits — too slow and wrong consistency model.
266. 🟡 Idempotency key placement?
   - 要点：On **POST /orders** (or payment confirm). Server stores `(key → order_id)`; retries from client or PSP webhook replays return same order.
267. 🟡 How to release expired holds at scale?
   - 要点：**Redis TTL** + periodic **reaper** scanning DB for stuck `held` rows; partition reaper by `event_id`. Metrics on hold age p99. [← Index](./00-index.md)

### [`ticketmaster`](../system-design/ticketmaster/) — Ticketmaster（变体：`ticketmaster-system`, `ticketmaster-system-design`, `ticketmaster-educative-tests`）

268. 🟡 How would you scale Ticketmaster to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
269. 🟡 What database would you choose for Ticketmaster and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
270. 🟡 How do you handle failures in Ticketmaster?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
271. 🟡 What caching strategy would you use for Ticketmaster?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
272. 🟡 How do you ensure consistency in a distributed Ticketmaster?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`twitter-facebook-system-design`](../system-design/twitter-facebook-system-design/) — Twitter Facebook

273. 🟡 How would you scale Twitter Facebook to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
274. 🟡 What database would you choose for Twitter Facebook and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
275. 🟡 How do you handle failures in Twitter Facebook?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
276. 🟡 What caching strategy would you use for Twitter Facebook?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
277. 🟡 How do you ensure consistency in a distributed Twitter Facebook?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`whatsapp`](../system-design/whatsapp/) — Whatsapp（变体：`whatsapp-system`, `whatsapp-tests`, `whatsapp-system-design`）

278. 🟡 How would you scale WhatsApp to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
279. 🟡 What database would you choose for WhatsApp and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
280. 🟡 How do you handle failures in WhatsApp?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
281. 🟡 What caching strategy would you use for WhatsApp?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
282. 🟡 How do you ensure consistency in a distributed WhatsApp?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`youtube`](../system-design/youtube/) — Youtube（变体：`youtube-system`, `youtube-tests`, `youtube-system-design`）

283. 🟡 How would you scale YouTube to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
284. 🟡 What database would you choose for YouTube and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
285. 🟡 How do you handle failures in YouTube?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
286. 🟡 What caching strategy would you use for YouTube?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
287. 🟡 How do you ensure consistency in a distributed YouTube?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

## 四、运维与基础设施（`ops-infra`，11 个主题，82 题）

### [`container-orchestration-system`](../system-design/container-orchestration-system/) — Container Orchestration System（变体：`container-orchestration-system-design`）

288. 🟡 How would you scale Container Orchestration to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
289. 🟡 What database would you choose for Container Orchestration and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
290. 🟡 How do you handle failures in Container Orchestration?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
291. 🟡 What caching strategy would you use for Container Orchestration?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
292. 🟡 How do you ensure consistency in a distributed Container Orchestration?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`disaster-recovery-system`](../system-design/disaster-recovery-system/) — Disaster Recovery System（变体：`disaster-recovery-system-design`）

293. 🟡 How would you scale Disaster Recovery to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
294. 🟡 What database would you choose for Disaster Recovery and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
295. 🟡 How do you handle failures in Disaster Recovery?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
296. 🟡 What caching strategy would you use for Disaster Recovery?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
297. 🟡 How do you ensure consistency in a distributed Disaster Recovery?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`distributed-task-scheduler`](../system-design/distributed-task-scheduler/) — Distributed Task Scheduler（变体：`distributed-task-scheduler-tests`）

298. 🔴 [drill] Trade-offs
   - 要点：[← Index](./00-index.md)

### [`firmware`](../system-design/firmware/) — Design a Firmware Update System — study hub

299. 🟡 Why is a pull-based model preferred over push for OTA updates to IoT devices?
   - 要点：Most IoT devices sit behind NAT or firewalls, making it difficult for the server to initiate connections. A pull model lets the device initiate the request on its own schedule, which is NAT-friendly and avoids the server needing to manage millions of persistent connections.
300. 🟡 A device loses power midway through writing a firmware image to the inactive partition. What happens on the next boot?
   - 要点：The boot control block still points to the **active (old) partition** because the `pending_boot` flag hasn't been set yet — that flag is only written after the image is fully staged and verified. The device boots normally into the old firmware.
301. 🟡 Explain why deterministic ring assignment (hash-based) is better than random for canary rollouts.
   - 要点：Using `hash(device_id) % 100` produces a **consistent** assignment: the same device always lands in the same ring across campaigns. This means: **Reproducibility:** If a canary device reports a problem, you can identify it again in the next campaign. **Progressive testing:** Ring 0 devices accumulate soak time across many releases, building confidence.
302. 🟡 What is the purpose of the `min_version` field in the firmware manifest, and what attack does it prevent?
   - 要点：The `min_version` field enforces an **anti-rollback policy**. When a device sees `min_version: 3.2.0` in the manifest, it stores this value persistently and rejects any future update with a version below 3.2.0, even if that update has a valid signature.
303. 🟡 A firmware rollout shows a 98.5% success rate at Ring 2. The gate threshold is 99.5%. What should the system do?
   - 要点：The rollout scheduler **pauses** the campaign automatically — it does not advance to Ring 3. Specifically: **Pause** — Stop expanding to new devices **Alert** — Notify the on-call SRE via PagerDuty with the success rate, failure breakdown by error code, and affected device cohort **Analyze** — Dashboard shows failure distribution by hardware revision, region …
304. 🟡 Why generate only consecutive deltas (v(N-1) → v(N)) instead of all pairs?
   - 要点：Generating deltas for all version pairs creates O(V²) artifacts per hardware variant, where V is the number of active versions. With 100 versions and 5 HW variants, that's 50,000 delta patches — enormous storage and build time. Consecutive deltas keep it at O(V), which is manageable.
305. 🟡 How does the system handle a firmware image that passes all automated health checks but causes subtle performance degradation?
   - 要点：Automated health checks catch hard failures (boot loops, network unreachable, services not starting). Subtle degradation — like a 15% increase in CPU usage or a memory leak that manifests after 48 hours — requires **fleet-level observability**: **Baseline metrics:** Before a rollout, the system captures baseline CPU, memory, network error rate, and applicati …
306. 🟡 Describe the key rotation process for the intermediate signing key without bricking devices.
   - 要点：Key rotation uses a **key-transition manifest** signed by **both** the old and new intermediate keys: Generate a new intermediate key pair in the HSM Create a special manifest: `{"type": "key_rotation", "new_public_key": "...", "effective_date": "..."}` Sign this manifest with the **old** intermediate key (devices can verify it) Devices that receive and veri …
307. 🟡 What are the trade-offs of using MQTT vs CoAP for device-to-cloud communication in a firmware update system?
   - 要点：**Decision:** MQTT for devices with persistent power and reliable connectivity (routers, gateways). CoAP for battery-powered, constrained devices (sensors, wearables) where every byte and wake cycle counts.
308. 🟡 A customer reports that 500 devices in a single building all failed to update. All other devices in the region succeeded. What's your investigation approach?
   - 要点：This pattern strongly suggests a **local network issue** rather than a firmware bug: **Check CDN logs** — Did these 500 devices get HTTP 200 responses? Or timeouts / 5xx errors? **Correlate by IP range** — A building likely shares an external IP or small IP block. Check if a firewall or proxy is blocking the CDN domain or stripping Range headers.
309. 🔴 [drill] Why Pull, Not Push?
   - 要点：**Q: "Why not push firmware directly to devices?"** Most IoT devices sit behind NAT or firewalls. A push model requires millions of persistent connections (MQTT or WebSocket), which is expensive and fragile. Pull lets the device initiate on its own schedule — NAT-friendly, stateless server.
310. 🔴 [drill] Anti-Bricking
   - 要点：**Q: "How do you prevent bricking 10 million devices with a bad update?"** Four layers: (1) **A/B partitions** — never modify the running partition; write to inactive slot. (2) **Watchdog timer** — if the new firmware doesn't confirm health within 120 s, hardware reset kicks in.
311. 🔴 [drill] Delta Updates
   - 要点：**Q: "How do delta updates work? Why not always send the full image?"** Delta updates use bsdiff — it builds a suffix array of the old image, finds longest byte matches in the new image, and emits compact (copy-offset, copy-length, extra-bytes) triples. For a 50 MB firmware, the delta is typically 10–15 MB.
312. 🔴 [drill] Security & Signing
   - 要点：**Q: "Walk me through the signing chain."** Offline root CA (Ed25519, air-gapped HSM, 10-year key) signs an intermediate key stored in AWS CloudHSM (2-year rotation). The intermediate key signs firmware manifests containing SHA-256 hashes of the full image and delta. Devices verify using a root-of-trust public key burned into ROM.
313. 🔴 [drill] Rollout Phases
   - 要点：**Q: "How does phased rollout work?"** Devices are assigned to rings via `hash(device_id) % 100` — deterministic, so the same devices canary every time. Ring schedule: 1 % → 5 % → 20 % → 50 % → 100 %, each gated on success rate (99.9 % → 99.7 % → 99.5 %) and minimum soak time (24 h).
314. 🔴 [drill] Data Model
   - 要点：**Q: "What are the core tables?"** Three tables: **devices** (device_id PK, hw_revision, current_version, region, group, last_checkin — 10 M rows, hash-partitioned), **firmware_manifests** (version + hw_revision unique, SHA-256 hashes, signature, S3 path, min_version), **rollouts** (rollout_id PK, target_version, cohort_filter JSONB, phases JSONB, current_ph …
315. 🔴 [drill] CDN & Caching
   - 要点：**Q: "Why CDN for firmware delivery?"** Firmware has an ideal CDN cache profile: one artifact served to millions of identical devices. Cache-hit ratio exceeds 95 %. At 10 M devices × 50 MB, direct S3 egress would cost ~$45,000/campaign at $0.09/GB. CDN at $0.04/GB with 95 % cache hits: ~$5,600.
316. 🔴 [drill] Reliability Scenarios
   - 要点：**Q: "What happens if a device loses power during the update?"** Depends on the stage. **During download:** Cache file is partial; on next boot, device resumes from where it left off via HTTP Range request. **During partition write:** Slot B is corrupted, but Slot A is untouched — BCB still points to A, device boots normally.
317. 🔴 [drill] Observability
   - 要点：**Q: "What metrics would you monitor?"** Five categories: (1) **Update success rate** — per campaign, per ring, per HW revision; gate threshold for rollout advancement. (2) **Brick rate** — devices unresponsive > 60 min after starting update; any brick → immediate page. (3) **CDN cache-hit ratio** — should be ≥ 95 %; low ratio means wasted bandwidth cost.
318. 🔴 [drill] Cost
   - 要点：**Q: "What's the biggest cost driver and how do you optimize it?"** CDN bandwidth — 40–50 % of total cost. At $0.04/GB average, a full-image campaign to 10 M devices costs ~$20,000. Optimizations: (1) Delta patches reduce per-device download by 70–80 %, saving ~$14,400/campaign. (2) Origin shield reduces origin fetches.
319. 🔴 [drill] Push-Notify for Critical CVEs
   - 要点：**Q: "How do you handle an emergency security patch?"** CVE published → engineering produces patch within 24 h → signing + upload → campaign created with **accelerated schedule** (soak times halved). Server publishes MQTT "check-now" nudge to all device command topics.
320. 🟢 [速答] Delivery model?
   - 要点：Pull-based with MQTT push-notify for urgency
321. 🟢 [速答] Partition scheme?
   - 要点：A/B with watchdog-based rollback
322. 🟢 [速答] Diff algorithm?
   - 要点：bsdiff (consecutive only); courgette for ELF
323. 🟢 [速答] Brick prevention?
   - 要点：4 layers: A/B + watchdog + retry counter + phased rollout
324. 🟢 [速答] Cost driver?
   - 要点：CDN bandwidth → delta patches save 70–80 %
325. 🟢 [速答] Key SLOs?
   - 要点：99.5 % success, < 0.001 % brick, 99.95 % availability

### [`metrics-monitoring-hello-interview`](../system-design/metrics-monitoring-hello-interview/) — Metrics Monitoring Platform (Datadog-like) - Hello Interview Guide

326. 🟡 How would you scale Metrics Monitoring Platform (Datadog-like) - Hello Interview Guide to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
327. 🟡 What database would you choose for Metrics Monitoring Platform (Datadog-like) - Hello Interview Guide and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
328. 🟡 How do you handle failures in Metrics Monitoring Platform (Datadog-like) - Hello Interview Guide?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
329. 🟡 What caching strategy would you use for Metrics Monitoring Platform (Datadog-like) - Hello Interview Guide?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
330. 🟡 How do you ensure consistency in a distributed Metrics Monitoring Platform (Datadog-like) - Hello Interview Guide?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics. [← Back to index](./00-index.md)

### [`monitoring`](../system-design/monitoring/) — Monitoring（变体：`monitor`, `monitoring-system`, `monitoring_system`, `monitoring-system-complete`）

331. 🟡 What are the main functional areas for a **1000 server** monitoring platform?
   - 要点：(1) **Ingest** metrics (pull and/or push) with discovery of targets, (2) **store** time series with **retention** tiers, (3) **query** for dashboards and SLOs, (4) **alert** (rules + routing + on-call), (5) optional **logs/traces** for triage, (6) **visualize** health over time. Name **agent overhead** and **end-to-end alert latency** as NFRs you will-size.
332. 🟡 Size ingest for 1000 servers, 80 metrics, 15 s scrape. Why does cardinality still matter if QPS is small?
   - 要点：**5.3K samples/s** is modest; the risk is **unique label combinations** (per-pod or per-URL labels) that explode **index** and **memory** in the TSDB. You budget **active series** and **samples/s**; you **drop** or **aggregate** high-card labels at the collector. Raw QPS is necessary but not sufficient.
333. 🟡 Pull vs push—when do you use each for web servers?
   - 要点：**Pull** when targets expose **/metrics** and you control scrape intervals (classic Prometheus). **Push** for **ephemeral** jobs, **networks** that block inbound scrape, or **OTLP**/remote-write–native paths. In hybrid clouds, a **remote-write gateway** is often the compatibility layer; both end in the same **label model**.
334. 🟡 How do you keep monitoring from **harming** production?
   - 要点：**Bound** agent CPU and memory, **batch** and **compress**, cap **scrape fan-out** (skip expensive collectors on hot paths), use **jitter** on scrape start times, and run collectors as **separate** capacity from the TSDB. If you double metrics, you double your problem—govern with **governance** and **quotas** per service.
335. 🟡 What happens when the TSDB is slow or partially unavailable?
   - 要点：Dashboards return **503**/partial data; the **query API** should **timeout** and show **stale** cache where acceptable. **Alerting** should prefer **federated** or **out-of-band** health for the alert pipeline (don’t only monitor Alertmanager with Alertmanager). On-call may widen **SLOs** temporarily and use **runbooks** that don’t require perfect graphs.
336. 🟡 How do you avoid alert **noise**?
   - 要点：`for` delays on rules, **grouping** and **inhibition** in Alertmanager, **routing** by severity, **SLO-based** burn alerts instead of every threshold, and **on-call** feedback to delete bad rules. Measure **false-positive** rate and **ack** time.
337. 🟡 How is this system **observed** in production (meta-monitoring)?
   - 要点：**RED/USE** on the **collectors, query path, and rule evaluators**; track **ingest lag**, **query latency** histograms, **dropped** samples, **replication** lag, and **active series**. Export **`/metrics`** from every tier (as in this repo’s [api.go](api.go) pattern).
338. 🟡 Where do **Kafka and Flink** fit—do I need them?
   - 要点：**Not** for every design. Ingest at 5.3K samples/s fits **direct** write to a TSDB. Add a **stream** (Kafka) + **Flink** when you need **cross-tenant** pre-aggregates, **enrichment**, or **fan-in** from many regions with **at-least-once** and **replay**. Say “optional scale path” unless the interviewer gives **RPS/series** that force it.
339. 🔴 [drill] minute interview flow
   - 要点：**Clarify scope (3–5 min)**: metrics only vs logs/traces, regions, retention. **Requirements + scale (5–8 min)**: 1000 servers, ingestion math, SLOs. **High-level design (10–12 min)**: agents → collectors → TSDB → query/rules/alerts. **Deep dives (12–15 min)**: cardinality, alerting quality, failure handling.
340. 🔴 [drill] Common mistakes to avoid
   - 要点：Treating logs, metrics, and traces as identical storage workloads. Ignoring alert deduplication/grouping. Missing “monitor the monitoring system” telemetry. Hand-waving cardinality without concrete guardrails. [← 19](./19-cost-efficiency.md) · [21](./21-one-hour-speaking-transcript.md) · [Index](./00-index.md)

### [`moon-machine-upgrade`](../system-design/moon-machine-upgrade/) — Moon machine fleet upgrade (remote edge deploy)

341. 🔴 [drill] Follow-up prompts to expect
   - 要点：What if Earth is down for **days**? How do you avoid **duplicate** downloads? How do you **canary** safely? How do you **rollback**? Why not **SSH from Earth** to every machine?
342. 🔴 [drill] Timebox
   - 要点：**5 min** requirements **10 min** diagram **10 min** one deep dive **5 min** failures + security [← 19](./19-trade-offs.md) · [Index](./00-index.md) · [21](./21-one-hour-speaking-transcript.md)

### [`observability`](../system-design/observability/) — Observability & monitoring — system design hub

343. 🔴 [drill] 2 minutes
   - 要点：“Observability is **metrics** for aggregates, **logs** for rich context, **traces** for latency across services—with **shared IDs** so you can pivot. Monitoring is **thresholds** on known signals; observability supports **why** questions.
344. 🔴 [drill] 5 minutes
   - 要点：Add: **OpenTelemetry**-style pipeline (SDK → collector → backends), **cardinality** risks, **tail sampling** for outliers, **error budgets** for release policy, **PII** redaction.
345. 🔴 [drill] 15 minutes
   - 要点：Add: **multi-tenant** quotas, **Kafka** telemetry bus for fan-out, **Alertmanager** noise controls, **failure** of the observability stack (buffer/drop metrics), walk through **one** upload or **bid** request with spans.
346. 🔴 [drill] Tie-ins (say aloud)
   - 要点：**Object storage:** erasure coding / replication lag as **saturation** or **queue** metrics. **Online auction:** **strong consistency** on bids—metrics on **conflict** rate, traces on **lock** contention. **OOD services:** each **bounded context** exports consistent **service.name** and **semantic** span names. [← Index](./00-index.md)

### [`pingdom`](../system-design/pingdom/) — Pingdom

347. 🟡 Why check from multiple regions instead of just one?
   - 要点：A single probe region can experience local network issues (ISP outage, DNS resolution failure, routing problems) that don't affect the monitored service. Checking from **3+ regions** and requiring majority confirmation (e.g. 2/3 DOWN) eliminates **false positives** from single-region blips.
348. 🟡 How do you handle 10 million checks per minute?
   - 要点：**Partition checks** across probe fleet using Kafka (partitioned by check_id) **Scale probes horizontally** — each region runs N probe instances as a consumer group **Stagger intervals** — not all checks fire at :00; distribute across the interval window Each probe handles ~5K checks/min (HTTP requests are I/O-bound, not CPU-bound) **20 regions × 100 probes/ …
349. 🟡 How does the alert state machine prevent alert storms?
   - 要点：The state machine has intermediate states (DEGRADED, RECOVERING) with **cooldown windows**: UP → DEGRADED: some regions fail, start tracking DEGRADED → DOWN: majority confirm, **wait 30 s**, re-verify, then alert DOWN → RECOVERING: all regions pass, **wait 60 s** before resolving RECOVERING → UP: stable for cooldown, send recovery notification This prevents …
350. 🟡 What is the difference between Synthetic Monitoring and RUM?
   - 要点：**Both are needed**: Synthetic guarantees coverage and SLA tracking even at 3 AM. RUM captures what real users actually experience (slow mobile networks, browser-specific bugs, CDN cache misses by geography).
351. 🟡 How does Transaction Monitoring differ from uptime checks?
   - 要点：Uptime checks test a single URL — "is this endpoint returning 200?" Transaction monitoring tests **multi-step user flows** — "can a user actually log in, search, and checkout?" A site can return 200 on the homepage while the checkout flow is broken due to a downstream microservice failure.
352. 🟡 Why use ClickHouse for RUM instead of the same TSDB as synthetic data?
   - 要点：RUM data has **much higher cardinality** than synthetic data: Synthetic: `(check_id, region, timestamp)` — millions of series RUM: `(site_id, page, browser, browser_version, OS, device, country, city, ISP)` — billions of combinations ClickHouse is a **columnar OLAP** database optimized for: High-cardinality aggregations (`GROUP BY browser, country`) Fast ana …
353. 🟡 How do you ensure notifications are delivered exactly once?
   - 要点：Use an **idempotency key** = `(check_id, incident_id, channel_type)`. The notification service checks this key in a dedup store (Redis with TTL) before sending. If the key exists, skip. If not, send and record.
354. 🟡 How does Pingdom protect data in transit and at rest?
   - 要点：**In transit**: HTTPS/TLS 1.3 for all communication — probe ↔ control plane, RUM beacon ↔ collector, API ↔ user. Probes authenticate via mutual TLS. **At rest**: AES-256 encryption for stored check results, credentials, and RUM analytics data.

### [`security`](../system-design/security/) — Web Application Security — System Design Hub

355. 🟡 What are the three types of XSS? How does DOM XSS differ from reflected XSS?
   - 要点：The three types are **reflected**, **stored**, and **DOM-based**. **Reflected XSS**: The payload is sent via a URL parameter, the server includes it in the response without encoding, and it executes once. The payload travels: `client → server → client`. Server-side output encoding prevents it.
356. 🟡 Should XSS filtering be done on input or output? Why?
   - 要点：**Output encoding is superior**, but both have a role: **Input filtering** (on write): Removes obviously malicious payloads (`<script>`, event handlers) Problem: context-dependent — `<script>` is dangerous in HTML but safe in a `<textarea>` value Problem: encoding bypasses — `%3Cscript%3E`, `&#60;script&#62;`, Unicode normalization Problem: double-encoding c …
357. 🟡 How do you bypass HTTPOnly cookies? What else can XSS do besides cookie theft?
   - 要点：**HTTPOnly bypass methods:** `phpinfo()` or server diagnostics pages expose all cookies including HTTPOnly Apache `server-status` leaks request details with cookies HTTP TRACE method echoes the full request (Cross-Site Tracing — XST) Session fixation: set a known session ID before victim authenticates **XSS capabilities beyond cookie theft:** Keylogging: `do …
358. 🟡 Explain wide-byte (宽字节) injection. Where does encoding happen? How to prevent it?
   - 要点：**How it works:** When the database uses GBK/GB2312 encoding and the application uses `addslashes()` to escape quotes: **Where encoding happens:** The encoding mismatch occurs between the **application layer** (which treats input as ASCII/UTF-8) and the **database connection** (which uses GBK).
359. 🟡 How does a penetration test methodology work? What's your approach to testing a website?
   - 要点：**Systematic approach (渗透测试思路):**
360. 🟡 SQL injection — what do you test first? How do you write a shell? What if single quotes are filtered?
   - 要点：**What to test first:** Single quote `'` — check for error messages (error-based detection) `1 AND 1=1` vs `1 AND 1=2` — boolean-based blind detection `1 AND SLEEP(5)` — time-based blind detection `1 UNION SELECT NULL,NULL--` — determine column count **Writing a shell via SQLi:** **If single quotes are filtered:** Use hex encoding: `SELECT 0x3C3F706870` (hex …
361. 🟡 What is CSRF? How do you perform CSRF without Referer? How to prevent it?
   - 要点：**CSRF (Cross-Site Request Forgery):** Forces a logged-in user to perform unintended actions by tricking their browser into sending a request to a target site with their existing session cookies.
362. 🟡 Explain the same-origin policy. Why does it exist? How does XSS bypass it?
   - 要点：**Same-origin policy (SOP):** Two URLs share the same origin if **protocol, host, and port** are identical. SOP prevents JavaScript on one origin from reading data from another origin.
363. 🟡 Port 1521 is which service? Name common service ports.
   - 要点：**21** — FTP — Anonymous login, credential brute-force; **22** — SSH — Brute-force, key-based auth recommended; **25** — SMTP — Open relay, email spoofing
364. 🟡 How do you detect WAF presence? How do you bypass WAF?
   - 要点：**WAF Detection (如何知道 WAF 信息):** Send a malicious payload (`<script>alert(1)</script>`) → if you get a custom 403/block page, WAF is present Tool: `wafw00f target.com` — fingerprints WAF vendor (Cloudflare, AWS WAF, ModSecurity) Check response headers: `X-Sucuri-ID`, `cf-ray` (Cloudflare), `X-WAF-*` headers Timing analysis: requests with attack signatures ta …
365. 🔴 [drill] minute opening
   - 要点：State **defense in depth**: edge (CDN/DDoS) → WAF → app (auth, CSRF, encoding) → data (parameterized queries, least privilege) → detection (SIEM, scanner). Name **one** OWASP category you’ll deep-dive (e.g. injection or XSS).
366. 🔴 [drill] minute deep dives (pick one)
   - 要点：**XSS:** reflected vs stored vs DOM; why output encoding beats blacklist; CSP role; DOM XSS invisible to server WAF. **SQLi:** prepared statements; ORM pitfalls (string concat); defense in depth with WAF. **CSRF:** synchronizer token + SameSite; when JSON APIs reduce CSRF (still need CORS discipline).
367. 🔴 [drill] Trade-off drill (2 minutes)
   - 要点：**WAF false positives vs miss rate:** staged rollout, canary rules, FP budget, unblock workflow.
368. 🔴 [drill] Scale drill (2 minutes)
   - 要点：Peak QPS → WAF instance count; audit log GB/day → storage tiers (cite [11-scale-and-slo](./11-scale-and-slo.md)).

### [`upgrade`](../system-design/upgrade/) — Remote fleet upgrade (Moon / disconnected edge) — System design hub

369. 🔴 [drill] STAR anchors (pair with behavioral guide)
   - 要点：Link to [bq/prioritize-tasks/24-star-method-canonical-reference.md](../bq/prioritize-tasks/24-star-method-canonical-reference.md) for **Situation / Task / Action / Result** phrasing when interviewers ask for **past experience** analogies.

## 五、AI / ML 系统（`ai-ml`，9 个主题，57 题）

### [`agentic-system-design`](../system-design/agentic-system-design/) — Agentic

370. 🟡 How would you scale Agentic to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
371. 🟡 What database would you choose for Agentic and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
372. 🟡 How do you handle failures in Agentic?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
373. 🟡 What caching strategy would you use for Agentic?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
374. 🟡 How do you ensure consistency in a distributed Agentic?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`amazon-book-reviews-recommendations`](../system-design/amazon-book-reviews-recommendations/) — Amazon book reviews ingestion + on-site recommendations — System design hub

375. 🔴 [drill] STAR
   - 要点：[bq/prioritize-tasks/24-star-method-canonical-reference.md](../bq/prioritize-tasks/24-star-method-canonical-reference.md)
376. 🔴 [drill] Related hubs
   - 要点：[recommendation/00-index.md](../recommendation/00-index.md) [blob-store/00-index.md](../blob-store/00-index.md) [blob-store-educative-tests/00-index.md](../blob-store-educative-tests/00-index.md) [book_subscription/00-index.md](../book_subscription/00-index.md) [book_subscription_system/00-index.md](../book_subscription_system/00-index.md) [boot_process/00-i …
377. 🔴 [drill] Runnable
   - 要点：`python3 lab/review_ingest_sketch.py` — idempotent keys `python3 lab/recommendation_sketch.py` — TF-IDF similarity `python3 lab/mini_pipeline.py` — ingest + “also like” flow [← 19](./19-cost-efficiency.md) · [Index](./00-index.md) · [21-one-pager](./21-one-pager-speaking-transcript.md)

### [`chatgpt`](../system-design/chatgpt/) — Chatgpt（变体：`chatgpt-system`, `chatgpt-system-design`, `chatpgt-system-design`）

378. 🟡 How would you scale Chatgpt to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
379. 🟡 What database would you choose for Chatgpt and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
380. 🟡 How do you handle failures in Chatgpt?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
381. 🟡 What caching strategy would you use for Chatgpt?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
382. 🟡 How do you ensure consistency in a distributed Chatgpt?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.
383. 🟡 How would you scale Chatpgt to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
384. 🟡 What database would you choose for Chatpgt and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
385. 🟡 How do you handle failures in Chatpgt?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
386. 🟡 What caching strategy would you use for Chatpgt?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
387. 🟡 How do you ensure consistency in a distributed Chatpgt?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`genai-system-design`](../system-design/genai-system-design/) — Genai

388. 🟡 How would you scale Genai to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
389. 🟡 What database would you choose for Genai and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
390. 🟡 How do you handle failures in Genai?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
391. 🟡 What caching strategy would you use for Genai?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
392. 🟡 How do you ensure consistency in a distributed Genai?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`linkedin-feed-ranking`](../system-design/linkedin-feed-ranking/) — Social Feed / News Feed

393. 🟡 How would you scale Social Feed / News Feed to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
394. 🟡 What database would you choose for Social Feed / News Feed and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
395. 🟡 How do you handle failures in Social Feed / News Feed?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
396. 🟡 What caching strategy would you use for Social Feed / News Feed?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
397. 🟡 How do you ensure consistency in a distributed Social Feed / News Feed?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics. [← Back to index](./00-index.md)

### [`llm-customer-support-bot`](../system-design/llm-customer-support-bot/) — LLM-Powered Customer Support Bot — System Design Hub

398. 🟡 Why use RAG instead of fine-tuning the LLM on company knowledge?
   - 要点：RAG decouples knowledge from the model. Fine-tuning bakes knowledge into model weights, which means every knowledge base update requires retraining (hours), evaluation, and redeployment. RAG updates happen in minutes — re-index the changed documents in the vector DB, and the next query automatically retrieves the updated information.
399. 🟡 You have 250M queries/day. Explain how you'd keep GPU inference costs under $0.01 per query.
   - 要点：Three-tier cost-aware routing: **Tier 1 — Semantic Cache (30% of queries, $0.00/query):** Embed the user query, search a vector cache for semantically similar past queries (cosine > 0.95). FAQ-style questions like "What is your return policy?" have hundreds of paraphrases that all map to the same answer. Cache hit rate for FAQ category: ~70%.
400. 🟡 A user asks "What about the other item?" — how does the system resolve this without explicit context?
   - 要点：This is the **coreference resolution** problem in multi-turn dialogue. The system resolves it through conversation history in the session store: The orchestrator builds the LLM prompt with the full conversation history.
401. 🟡 How does the semantic cache avoid serving stale or incorrect responses?
   - 要点：Four invalidation mechanisms: **1. TTL-based expiry (24 hours):** Every cache entry has a maximum TTL. Knowledge base content changes are assumed to propagate within 24 hours. This is the safety net. **2.
402. 🟡 Walk me through the latency budget. Where would you optimize if p95 exceeds 3 seconds?
   - 要点：If p95 exceeds 3s, optimization priority: **1. LLM inference (1,500ms — largest component):** Switch to speculative decoding: draft tokens with 7B model, verify with 70B. Reduces token generation time by ~2×. Reduce output token limit from 500 to 300 (shorter responses). Use quantized model (INT4 instead of FP16): 40% faster, ~2% quality loss. **2.
403. 🟡 The system serves 8,700 QPS at peak. How many GPU servers do you need and how do you scale them?
   - 要点：**Baseline calculation:** **Scaling strategy:** **Horizontal pod autoscaling (HPA)** on GPU utilization: scale up at >80%, scale down at <30%. **Warm pool**: Keep 5 pre-loaded GPU instances in standby. GPU model loading takes ~2 minutes (loading 140GB model weights into VRAM), so cold starts are expensive.
404. 🟡 How do you detect and handle LLM hallucinations in production?
   - 要点：**Detection (multi-layered):** **Grounding classifier** (post-generation): A lightweight model checks if each claim in the response is supported by the retrieved documents. If the response says "Your order ships in 2 days" but no retrieved document mentions shipping time, it's flagged as potentially hallucinated.
405. 🟡 Why not use a single vector database for both the semantic cache and the knowledge base?
   - 要点：They have fundamentally different access patterns: Using a single index would cause: **Write amplification**: Cache inserts (6K/sec) would trigger index rebalancing that affects knowledge base search quality. **Eviction conflicts**: Cache TTL eviction could accidentally affect knowledge base entries.
406. 🟡 A support bot handles sensitive data (payment info, addresses). How do you ensure privacy and compliance?
   - 要点：**Data protection layers:** **PII detection and masking** (pre-processing): Before the query reaches the LLM, a PII detector scans for credit card numbers, SSNs, addresses, and phone numbers. Detected PII is replaced with tokens: `[CARD_****1234]`. The mapping is stored in an encrypted vault, and the LLM never sees raw PII.
407. 🟡 The Educative article estimates 50M requests per second for server sizing. Why is that unrealistic, and what's the correct calculation?
   - 要点：The article assumes all 50M DAUs send requests **simultaneously**, which is a worst-case thought experiment, not a realistic peak load estimate.

### [`music-listening-analytics`](../system-design/music-listening-analytics/) — Music listening history (30s threshold) — analytics system

408. 🔴 [drill] Follow-ups (TryExponent 2073 style)
   - 要点：**What** if the **user** **seeks** **past** **30s**? **How** do you **handle** **offline** **listening**? **Exactly-once** vs **at-least-once**? **How** fast **does** **data** **reach** **the** **warehouse**?
409. 🔴 [drill] Pairing hubs
   - 要点：**Async web service (task-scheduler):** [async-communication-web-service-interview-hub/00-index.md](../task-scheduler/docs/async-communication-web-service-interview-hub/00-index.md) **Idempotency & dedup (same hub):** [12-idempotency-dedup.md](../task-scheduler/docs/async-communication-web-service-interview-hub/12-idempotency-dedup.md) **Local sketch:** [lab …

### [`recommendation`](../system-design/recommendation/) — Recommendation system — Interview hub

410. 🟡 Why two-stage retrieve-then-rank instead of scoring the whole catalog?
   - 要点：Full **N × scoring** is infeasible for **N in the millions/billions**. Retrieval cuts **N** down to **hundreds** with cheap, parallelizable methods (co-occurrence, ANN, graphs). The ranker then runs a **rich model** only on that set.
411. 🟡 How do you handle position bias in click logs?
   - 要点：Clicks over-index top slots. Mitigations: **inverse propensity scoring** using randomized experiments, position features in the ranker, or **off-policy** learning. Mention that naive click-only training **reinforces** bad positions.
412. 🟡 What is point-in-time correctness in feature joins?
   - 要点：For each training example at time **t**, features must reflect **only information available at t** (no future clicks or labels). Otherwise **label leakage** inflates offline metrics and fails online.
413. 🟡 How would you size caches for the serving path?
   - 要点：Cache **hot user profiles**, **popular item features**, and **model warm-up** artifacts. Size from **p95 working set** and **TTL** based on freshness SLO. Use **request coalescing** for thundering herds on cold keys.
414. 🟡 Name three online metrics you’d watch after a launch.
   - 要点：**CTR**, **conversion rate**, **revenue per impression**, plus guardrails: **latency p99**, **error rate**, **coverage** (% catalog with impressions), and **diversity** proxies.
415. 🟡 Cold item with no interactions—what do you recommend?
   - 要点：Use **content** signals (title, category, image embedding, brand), map to **nearest neighbors** in embedding space, apply a **new item boost** with decay, and fall back to **category popularity**. [← Index](./00-index.md)
416. 🔴 [drill] Drill: sketch the diagram
   - 要点：Draw **5 boxes:** gateway, retrieve, rank, feature store, event bus → warehouse → trainer → model registry.
417. 🔴 [drill] Drill: latency budget
   - 要点：For **150 ms p99**, allocate: **20 ms** retrieve, **40 ms** features, **60 ms** rank, **30 ms** margin.
418. 🔴 [drill] Drill: one trade-off
   - 要点：**Strong inventory join** vs **stale features**—pick based on OOS pain vs latency.
419. 🔴 [drill] Drill: metric pair
   - 要点：Name **one north star** and **one guardrail** (e.g. conversion vs latency).
420. 🔴 [drill] Drill: cold start
   - 要点：New item: **content embedding** + **category popularity** + capped **exploration boost**.
421. 🔴 [drill] Doc map
   - 要点：[← Prev](./19-cost-efficiency.md) · [Index](./00-index.md) · [Next →](./21-one-hour-speaking-transcript.md)

### [`text-to-video-gen`](../system-design/text-to-video-gen/) — GenAI / LLM System Design

422. 🟡 How would you scale GenAI / LLM System Design to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
423. 🟡 What database would you choose for GenAI / LLM System Design and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
424. 🟡 How do you handle failures in GenAI / LLM System Design?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
425. 🟡 What caching strategy would you use for GenAI / LLM System Design?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
426. 🟡 How do you ensure consistency in a distributed GenAI / LLM System Design?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

## 六、操作系统与底层（`os-systems`，3 个主题，16 题）

### [`computer-boot-process`](../system-design/computer-boot-process/) — Linux / Operating System Internals

427. 🟡 How would you scale Linux / Operating System Internals to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
428. 🟡 What database would you choose for Linux / Operating System Internals and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
429. 🟡 How do you handle failures in Linux / Operating System Internals?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
430. 🟡 What caching strategy would you use for Linux / Operating System Internals?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
431. 🟡 How do you ensure consistency in a distributed Linux / Operating System Internals?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`kernel-distribution`](../system-design/kernel-distribution/) — Kernel Distribution System

432. 🟡 Why pull-based over push-based for 10K VMs?
   - 要点：Push (SSH/Ansible) creates **connection storms** at scale — 10K concurrent SSH sessions overwhelm the control plane. Pull lets each agent converge independently with jittered intervals, is **self-healing** (agent retries on failure), and works through NATs/firewalls (agents initiate outbound connections).
433. 🟡 How does kexec reduce rollout downtime compared to a full reboot?
   - 要点：`kexec` loads a new kernel directly from the running kernel, **skipping BIOS/UEFI POST, bootloader, and hardware re-initialization**. This reduces downtime from ~60 s to **< 10 s**. The trade-off is that hardware state is not fully reset, which can cause issues with certain drivers. Use `kexec_file_load()` for Secure Boot compatibility.
434. 🟡 What happens if a canary kernel causes panics?
   - 要点：The panicking VM reboots into the **GRUB fallback entry** (previous kernel). The agent reports **boot failure** to the orchestrator. The orchestrator checks the canary gate: if panic rate exceeds the threshold (e.g. > 0 panics in canary), it **pauses** the rollout.
435. 🟡 How do you handle 800 GB of bandwidth per rollout?
   - 要点：**Regional mirrors**: origin uploads to ~5 mirrors; each mirror serves ~2K local VMs (reduces cross-DC traffic by ~80%). **Delta updates**: for minor patches, `bsdiff` produces 60–80% smaller deltas (only changed bytes). **Staggered waves**: spreading rollout over 2–4 hours avoids burst bandwidth.
436. 🟡 How do you ensure only authorized kernels boot on VMs?
   - 要点：**Full Secure Boot chain**: UEFI platform keys → signed shim → signed GRUB → signed vmlinuz. The build pipeline signs kernels with an **HSM-backed key** enrolled in each VM's MOK database. The agent verifies the GPG signature before staging. If verification fails, the kernel is **rejected** and the agent reports the anomaly.
437. 🟡 What consistency model does the fleet use?
   - 要点：**Eventual consistency**. The orchestrator sets a **desired version** per VM pool. Agents independently poll and converge. At any point, the fleet may have mixed versions (especially during rollout). The monitoring dashboard shows **convergence progress** (% at target).

### [`operating-system-design`](../system-design/operating-system-design/) — Operating

438. 🟡 How would you scale Operating to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
439. 🟡 What database would you choose for Operating and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
440. 🟡 How do you handle failures in Operating?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
441. 🟡 What caching strategy would you use for Operating?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
442. 🟡 How do you ensure consistency in a distributed Operating?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

## 七、综合题库（`hubs`，2 个主题，16 题）

### [`leetcode`](../system-design/leetcode/) — Leetcode（变体：`design-leetcode`, `leetcode-system-design`）

443. 🟡 How would you scale LeetCode to handle 10x traffic?
   - 要点：Horizontal scaling with sharding, read replicas, caching layers (Redis/Memcached), CDN for static assets, and async processing via message queues. Shard by user ID or content ID for even distribution.
444. 🟡 What database would you choose for LeetCode and why?
   - 要点：PostgreSQL for transactional data (ACID, joins), DynamoDB/Cassandra for high-throughput key-value access, Redis for caching and real-time counters. Choose based on access pattern and consistency requirements.
445. 🟡 How do you handle failures in LeetCode?
   - 要点：Circuit breakers to isolate failing services, retries with exponential backoff, dead letter queues for failed async operations, health checks for auto-recovery, and graceful degradation showing cached data.
446. 🟡 What caching strategy would you use for LeetCode?
   - 要点：Cache-aside (lazy loading) for reads. Write-through for consistency-critical data. TTL-based expiry with cache warming for predictable traffic. Redis Cluster for distributed caching across regions.
447. 🟡 How do you ensure consistency in a distributed LeetCode?
   - 要点：Eventual consistency for most operations (faster, more available). Strong consistency for critical paths (payments, auth) using distributed transactions or saga pattern. Idempotency keys for exactly-once semantics.

### [`web-security-interview`](../system-design/web-security-interview/) — Web Security Interview — 春招面试题深度解析

448. 🟡 什么是XSS? 有哪几种类型? 如何防范?
   - 要点：**XSS (Cross-Site Scripting)**: 攻击者将恶意脚本注入到受害者浏览器中执行。 **三种类型:** **防范 (按优先级):** **输出编码** (首要): 根据上下文选择编码方式 — HTML实体编码(`html.escape()`)、JS编码、URL编码 **CSP** (Content-Security-Policy): `script-src 'self'` 禁止内联脚本 **HttpOnly Cookie**: 阻止JS读取Cookie **Trusted Types**: 强制要求所有DOM写入经过安全化 **关键**: 过滤在输出时做，而不是输入时，因为不知道输出上下文。
449. 🟡 如何通过代码审计找到安全漏洞?
   - 要点：**方法: 从Sink追溯Source (危险函数 → 输入来源)** **常见审计入口点:** 文件上传功能 → 检查后缀名验证、存储路径 搜索框 → 检查SQL和XSS 富文本编辑器 → 检查HTML过滤 文件下载 → 检查路径遍历 (`../../../etc/passwd`) 反序列化入口 → `unserialize()`, `pickle.loads()` **PHP高危函数备忘:** `eval()`, `assert()`, `system()`, `exec()`, `passthru()`, `shell_exec()`, `include()`, `require()`, `unserialize()`, `preg_replace('/e')`
450. 🟡 UDF提权原理和防范?
   - 要点：**原理:** 攻击者通过SQLi获得MySQL FILE权限 将恶意共享库(.so/.dll)写入MySQL插件目录 MySQL 5.1+: `SHOW VARIABLES LIKE 'plugin_dir'` → `/usr/lib/mysql/plugin/` `CREATE FUNCTION sys_exec RETURNS STRING SONAME 'udf.so'` `SELECT sys_exec('id')` → 以mysql进程权限执行系统命令 **如果mysql以root运行 → 完全系统控制** **防范:** MySQL数据库用户 **REVOKE FILE** 权限 (最重要) MySQL进程以低权限用户运行 (非root, 非admin) `plugin_dir` 目录owner是 …
451. 🟡 SQL注入只有UPDATE语句时如何利用?
   - 要点：**场景:** `UPDATE users SET email='INPUT' WHERE id=1` **利用方式:** **危害:** 修改数据 (密码/权限/余额) 比SELECT型注入更危险，因为直接导致数据损坏
452. 🟡 MySQL 4和5的区别?
   - 要点：**核心区别:** **MySQL 4时代注入技巧:** 只能依赖猜测或报错信息推断表名 或通过ORDER BY测试列数，UNION暴破表名 **MySQL 5+ 注入:** **影响:** 大多数现代应用运行MySQL 5+，information_schema让注入利用变得系统化
453. 🟡 如何绕过HttpOnly获取Cookie?
   - 要点：**HttpOnly阻止的:** `document.cookie` 读取 **仍然可行的方法:** **phpinfo()页面**: 如果开启且可访问，会在HTTP headers区域显示所有Cookie (包括HttpOnly) **XST (Cross-Site Tracing)**: HTTP TRACE方法将请求头原样返回 JS发送TRACE请求 → 响应包含Cookie头 现代浏览器已禁止JS发TRACE: 此方法基本无效 **应用层漏洞**: 某些应用会在JSON响应或错误页中泄露Cookie **更重要: XSS能做的其他事:** 键盘记录 (不需要Cookie): `document.onkeypress` 截取表单提交 AJAX代替Cookie的操作 (浏览器自动带Cookie) 账户接管 …
454. 🟡 TCP vs UDP区别? TCP能做反射DDoS吗?
   - 要点：**TCP vs UDP:** **TCP能做反射DDoS吗?** 不适合，原因: TCP三次握手: SYN → SYN-ACK → ACK 攻击者伪造源IP发SYN → 受害者IP收到SYN-ACK → 但攻击者不完成握手 没有放大效果: SYN-ACK(44字节) vs SYN(44字节) = 1:1 **SYN Flood (不是反射放大):** 发送大量SYN但不完成握手 耗尽服务器的半连接队列 (backlog queue) 这是资源耗尽攻击，不是流量放大 **UDP反射放大 (有效):** 无连接验证 → 可以伪造源IP DNS放大: 60B查询 → 3000B响应 = 50倍放大 NTP monlist: 8B → 4500B = 562倍放大
455. 🟡 DNS协议在哪一层? 什么时候用TCP?
   - 要点：**DNS层级:** 应用层 (Application Layer, OSI第7层) **传输协议:** 默认UDP，端口53 **什么时候用TCP:** **区域传送 (Zone Transfer, AXFR)**: 主DNS向从DNS同步全量记录 数据量大，需要可靠传输 → TCP **响应超过512字节**: DNS over UDP限制512字节 早期规范: 超过512字节截断，客户端用TC标志位重试TCP 现代: EDNS0扩展允许UDP最大4096字节 **DNS over TLS (DoT)**: 安全DNS，使用TCP 853端口 **DNS over HTTPS (DoH)**: 通过HTTPS传输，TCP 443端口 **安全影响:** Zone Transfer如果暴露给公网 → 泄露所有 …
456. 🟡 1521是什么端口?
   - 要点：**Oracle数据库TNS监听器端口** (Transparent Network Substrate) Oracle使用TCP 1521作为默认监听端口，客户端通过此端口连接到Oracle数据库实例。 **安全风险:** TNS Poison攻击 (CVE-2012-1675): 中间人攻击，重定向客户端连接到假服务器 暴力破解: 常见弱密钥 (system/manager, sys/change_on_install) 未授权访问: 某些配置允许无需密码连接 SID枚举: 猜测数据库实例名 **安全建议:** 不要将1521暴露在公网 使用网络访问控制列表限制访问 定期更换TNS listener密码 **常见数据库端口:** 1433 → SQL Server **1521 → Oracle** 330 …
457. 🟡 CSRF如何不带Referer访问? (如何绕过Referer检查)
   - 要点：某些网站通过检查`Referer`头来防CSRF，以下方法可绕过: **方法1: Meta Referrer Policy** → 页面内所有请求不发送Referer头 **方法2: HTTPS降级到HTTP** **方法3: data: URI** → data:URI没有origin，不发送Referer **方法4: Redirect链** → 某些浏览器redirect后不带Referer **结论:** Referer检查作为CSRF防御是不可靠的，应使用CSRF Token + SameSite Cookie
458. 🟡 给写PHP的程序员提什么安全建议?
   - 要点：**Top 10 PHP安全建议:** **SQL注入**: 使用PDO + 参数化查询，永远不要字符串拼接SQL **XSS**: 输出时使用 `htmlspecialchars($data, ENT_QUOTES, 'UTF-8')` **CSRF**: 所有表单加CSRF Token，验证Referer或SameSite Cookie **文件上传**: 白名单后缀 + 存储在webroot外 + 随机文件名 **密码**: 使用 `password_hash()` (bcrypt) + `password_verify()`，禁止MD5 **会话**: `session_regenerate_id()` 登录后重新生成Session ID **错误处理**: 生产环境关闭错误显示 (`display_e …

---

## 难度图例

🟢 速答（一句话记忆点） · 🟡 主题 quiz 题（需解释原因与取舍） · 🔴 drill（开放式深挖，按面试阶段口述）

## 与 modules 的映射

| 本文件分组 | 对应 modules 模块 | 备注 |
|---|---|---|
| 一、基础与方法论 | `system-design`（`system-design-questions.md` 方法论 Q1–Q4 + 对应结构化题）；主题目录见 `system-design-catalog.md` 的 `fundamentals` 分类 | 10 个主题；🟡 quiz · 🔴 drill · 🟢 速答 |
| 二、基础组件 | `system-design`（`system-design-questions.md` 方法论 Q1–Q4 + 对应结构化题）；主题目录见 `system-design-catalog.md` 的 `building-blocks` 分类 | 12 个主题；🟡 quiz · 🔴 drill · 🟢 速答 |
| 三、产品端到端设计 | `system-design`（`system-design-questions.md` 方法论 Q1–Q4 + 对应结构化题）；主题目录见 `system-design-catalog.md` 的 `products` 分类 | 23 个主题；🟡 quiz · 🔴 drill · 🟢 速答 |
| 四、运维与基础设施 | `system-design`（`system-design-questions.md` 方法论 Q1–Q4 + 对应结构化题）；主题目录见 `system-design-catalog.md` 的 `ops-infra` 分类 | 11 个主题；🟡 quiz · 🔴 drill · 🟢 速答 |
| 五、AI / ML 系统 | `system-design`（`system-design-questions.md` 方法论 Q1–Q4 + 对应结构化题）；主题目录见 `system-design-catalog.md` 的 `ai-ml` 分类 | 9 个主题；🟡 quiz · 🔴 drill · 🟢 速答 |
| 六、操作系统与底层 | `system-design`（`system-design-questions.md` 方法论 Q1–Q4 + 对应结构化题）；主题目录见 `system-design-catalog.md` 的 `os-systems` 分类 | 3 个主题；🟡 quiz · 🔴 drill · 🟢 速答 |
| 七、综合题库 | `system-design`（`system-design-questions.md` 方法论 Q1–Q4 + 对应结构化题）；主题目录见 `system-design-catalog.md` 的 `hubs` 分类 | 2 个主题；🟡 quiz · 🔴 drill · 🟢 速答 |
