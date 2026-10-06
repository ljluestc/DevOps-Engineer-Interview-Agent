# 系统设计主题目录（system-design catalog）

> **自动生成，请勿手改** —— 由 `scripts/build_system_design_catalog.py` 扫描 `system-design/` 子模块生成；
> 校验用 `scripts/verify_system_design.py`。语料来源：<https://github.com/ljluestc/system-design>。
>
> 共 **630** 个顶层主题目录（可出题主题 **597** 个，工程脚手架 33 个）
+ `docs/` 下 **13** 个二级专题枢纽。其中 **599** 个主题带 `06-quiz.md`（带折叠答案的面试问答），
**600** 个带 `20-interview-drills.md`（60 秒 pitch / 速答表 / 白板顺序 / 常见陷阱）。

## 智能体如何使用本目录

1. 候选人说 `switch system-design` 或 `switch system-design <主题>` 时，先在本文件里按目录名 / 标题 / 关键词定位主题目录。
2. 出题前**必读**该目录下的 `00-index.md`（题面与文档索引）、`01-requirements.md`（FR/NFR/规模）、`05-trade-offs.md`；
   追问题优先取自 `06-quiz.md`（有参考答案）与 `20-interview-drills.md`（速答表 + 常见陷阱）。
3. 评分依据 `modules/system-design/system-design-questions.md` 开头的「系统设计评分维度」。
4. 「工程脚手架」分类的目录是代码/配置，不当作面试主题；「面试合集」分类可作为行为题 / 编码题补充来源。

文档列标记顺序：`index · quiz · drills · trade-offs · architecture`（✓ 存在 · 缺失）。

## 方法论与基础 / Fundamentals & methodology（51）

> 面试框架、估算、一致性/权衡、通用架构模式

| 目录 | 标题 | 一句话 | 文档 | 文件数 |
|---|---|---|---|---|
| [`api`](../../system-design/api/) | API migration — when customers must ship code | Cross-functional programs to move B2B integrators from v1 to v2 without surprise outages, ambiguous errors, or infinite dual-run. Shapes to TryExponent 2081 (de | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`api-design`](../../system-design/api-design/) | API Design — System Design & Interview Walkthrough | API contracts for large surfaces: resources, error envelopes, idempotency, pagination, versioning, webhooks, and migration programs when integrators must ship c | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`app`](../../system-design/app/) | App backends & BFF | First-party mobile/web: session, device trust, feature flags, BFF aggregation. See spotify-tests for listening-analytics style deep dives when present. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`back-of-envelope`](../../system-design/back-of-envelope/) | Back Of Envelope | Back Of Envelope — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 80 |
| [`cache`](../../system-design/cache/) | Cache | Cache — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`caching`](../../system-design/caching/) | Caching | Caching — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 56 |
| [`components`](../../system-design/components/) | Components | Components — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 29 |
| [`consistency-models-guide`](../../system-design/consistency-models-guide/) | Consistency Models Guide | Consistency Models Guide — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`consistency-models-spectrum`](../../system-design/consistency-models-spectrum/) | Consistency Models Spectrum | Consistency Models Spectrum — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`core-concepts`](../../system-design/core-concepts/) | Core Concepts | Core Concepts — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 52 |
| [`core-infrastructure`](../../system-design/core-infrastructure/) | Core Infrastructure | Core Infrastructure — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`database`](../../system-design/database/) | Database | Database — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 53 |
| [`database-demo`](../../system-design/database-demo/) | Database Demo | Database Demo — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 286 |
| [`database-module`](../../system-design/database-module/) | Database Module | Database Module — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 414 |
| [`database-system`](../../system-design/database-system/) | Database System | Database System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 89 |
| [`database-system-design`](../../system-design/database-system-design/) | Database | Comprehensive system design documentation for Database. | ✓ ✓ ✓ ✓ ✓ | 763 |
| [`database-types-2025`](../../system-design/database-types-2025/) | Database Types 2025 | Database Types 2025 — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`databases`](../../system-design/databases/) | Databases | Databases — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`distributed-systems-tradeoffs`](../../system-design/distributed-systems-tradeoffs/) | Distributed Systems Tradeoffs | Distributed Systems Tradeoffs — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 330 |
| [`end-to-end`](../../system-design/end-to-end/) | End-to-end system design | Clarify → estimate → design → trade-offs → operate—one coherent path for any large system prompt. | ✓ · · · · | 35 |
| [`failure-scenarios-analysis`](../../system-design/failure-scenarios-analysis/) | Failure Scenarios Analysis | Failure Scenarios Analysis — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`fault-tolerance-system`](../../system-design/fault-tolerance-system/) | Fault Tolerance System | Fault Tolerance System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 82 |
| [`fault-tolerance-system-design`](../../system-design/fault-tolerance-system-design/) | Fault Tolerance | Comprehensive system design documentation for Fault Tolerance. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`maintainability-system-design`](../../system-design/maintainability-system-design/) | Maintainability | Comprehensive system design documentation for Maintainability. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`modern-system-design`](../../system-design/modern-system-design/) | Modern | Comprehensive system design documentation for Modern. | ✓ ✓ ✓ ✓ ✓ | 452 |
| [`nfr-assessments`](../../system-design/nfr-assessments/) | Nfr Assessments | Nfr Assessments — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 80 |
| [`non-functional-requirements`](../../system-design/non-functional-requirements/) | Non Functional Requirements | Non Functional Requirements — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 83 |
| [`object-oriented-design`](../../system-design/object-oriented-design/) | Object Oriented Design | Object Oriented Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 221 |
| [`object-oriented-design-system`](../../system-design/object-oriented-design-system/) | Object Oriented Design System | Object Oriented Design System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 112 |
| [`pe-system-design`](../../system-design/pe-system-design/) | Pe | Comprehensive system design documentation for Pe. | ✓ ✓ ✓ ✓ ✓ | 437 |
| [`production-engineering-system-design`](../../system-design/production-engineering-system-design/) | Production Engineering | Comprehensive system design documentation for Production Engineering. | ✓ ✓ ✓ ✓ ✓ | 267 |
| [`reliability-system-design`](../../system-design/reliability-system-design/) | Reliability | Comprehensive reliability engineering framework — SLI/SLO/SLA, fault tolerance, circuit breakers, chaos engineering, graceful degradation, and safe deployments. | ✓ ✓ ✓ ✓ ✓ | 31 |
| [`replicated-sites`](../../system-design/replicated-sites/) | Replicated Sites | Replicated Sites — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 63 |
| [`reshaded-approach-system-design`](../../system-design/reshaded-approach-system-design/) | Reshaded Approach | Comprehensive system design documentation for Reshaded Approach. | ✓ ✓ ✓ ✓ ✓ | 228 |
| [`scalability-system-design`](../../system-design/scalability-system-design/) | Scalability | Comprehensive system design documentation for Scalability. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`scale-from-zero`](../../system-design/scale-from-zero/) | Scale From Zero | Scale From Zero — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 150 |
| [`scale-from-zero-to-millions`](../../system-design/scale-from-zero-to-millions/) | Scale From Zero To Millions | Scale From Zero To Millions — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 96 |
| [`specialized-systems`](../../system-design/specialized-systems/) | Specialized Systems | Specialized Systems — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 29 |
| [`system-design-docs`](../../system-design/system-design-docs/) | System Design Docs | System Design Docs — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 96 |
| [`system-design-foundations`](../../system-design/system-design-foundations/) | System Design Foundations | System Design Foundations — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 49 |
| [`system-design-implementation`](../../system-design/system-design-implementation/) | System Design Implementation | System Design Implementation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 154 |
| [`system-design-interview`](../../system-design/system-design-interview/) | system-design-interview — local index |  | ✓ ✓ ✓ ✓ ✓ | 1224 |
| [`system-design-interview-prep`](../../system-design/system-design-interview-prep/) | System Design Interview Prep | System Design Interview Prep — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 166 |
| [`system-design-notes`](../../system-design/system-design-notes/) | System Design Notes | System Design Notes — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 123 |
| [`system-design-scaling`](../../system-design/system-design-scaling/) | System Design Scaling | System Design Scaling — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 31 |
| [`system-designs`](../../system-design/system-designs/) | System Designs | System Designs — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 122 |
| [`system_design`](../../system-design/system_design/) | System Design | System Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 49 |
| [`system_design_master_guide`](../../system-design/system_design_master_guide/) | System Design Master Guide | System Design Master Guide — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 38 |
| [`system_designs`](../../system-design/system_designs/) | System Designs | System Designs — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 225 |
| [`three-tier-architecture`](../../system-design/three-tier-architecture/) | Three-tier architecture — system design hub | Presentation, application (business logic), and data tiers—how to separate concerns, scale and secure each layer, and how the pattern maps to modern API gateway | ✓ ✓ ✓ ✓ ✓ | 34 |
| [`wrapping-up-the-building-blocks-discussion`](../../system-design/wrapping-up-the-building-blocks-discussion/) | Wrapping Up The Building Blocks Discussion | Wrapping Up The Building Blocks Discussion — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 134 |

## 基础构件 / Building blocks（131）

> 限流/KV/缓存/唯一 ID/分布式锁/消息队列/CDN/LB/对象存储/搜索/TSDB

| 目录 | 标题 | 一句话 | 文档 | 文件数 |
|---|---|---|---|---|
| [`05-rate-limiter`](../../system-design/05-rate-limiter/) | 05 Rate Limiter | 05 Rate Limiter — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 62 |
| [`amazon-storage`](../../system-design/amazon-storage/) | Amazon Storage — interview hub (object storage) | System design for Amazon-class object storage: buckets, keys, durable blobs, REST access, multipart uploads, strong durability, and multi-tenant isolation—commo | ✓ · · · · | 25 |
| [`api-gateway`](../../system-design/api-gateway/) | API Gateway | North–south edge: TLS, auth, routing, rate limits, WAF, version-aware routing. Complements api-design and api. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`api-search-folders`](../../system-design/api-search-folders/) | API search folders — alias hub |  | ✓ ✓ ✓ ✓ ✓ | 23 |
| [`big-data-pipeline`](../../system-design/big-data-pipeline/) | Big Data Pipeline | Big Data Pipeline — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 655 |
| [`big-data-pipeline-go`](../../system-design/big-data-pipeline-go/) | Big Data Pipeline Go | Big Data Pipeline Go — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 179 |
| [`big-data-processing-pipeline-design`](../../system-design/big-data-processing-pipeline-design/) | Big Data Processing Pipeline Design | Big Data Processing Pipeline Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 471 |
| [`bitly-shortener`](../../system-design/bitly-shortener/) | Bitly Shortener | Bitly Shortener — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 30 |
| [`bitly-system-design`](../../system-design/bitly-system-design/) | Bitly | Comprehensive system design documentation for Bitly. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`blob-storage`](../../system-design/blob-storage/) | Blob Storage | Blob Storage — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`blob-store`](../../system-design/blob-store/) | Blob Store | Blob Store — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`blob-store-educative-tests`](../../system-design/blob-store-educative-tests/) | Blob Store | Blob Store — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 29 |
| [`cassandra`](../../system-design/cassandra/) | Apache Cassandra — System design hub | Cassandra — query-driven modeling, partitioning, replication, consistency levels, LSM storage, and operations. Original interview notes; not a copy of any third | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`cdn`](../../system-design/cdn/) | Cdn | Cdn — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 590 |
| [`cdn-educative-tests`](../../system-design/cdn-educative-tests/) | Cdn | Cdn — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`cdn-system`](../../system-design/cdn-system/) | Cdn System | Cdn System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 189 |
| [`cdn_system`](../../system-design/cdn_system/) | Cdn System | Cdn System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 72 |
| [`communication-messaging`](../../system-design/communication-messaging/) | Communication Messaging | Communication Messaging — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`crawler`](../../system-design/crawler/) | Crawler | Crawler — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 352 |
| [`data-infrastructure`](../../system-design/data-infrastructure/) | Data Infrastructure | Data Infrastructure — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`data-pipeline`](../../system-design/data-pipeline/) | Data Pipeline | Data Pipeline — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 275 |
| [`distributed-cache`](../../system-design/distributed-cache/) | Distributed Cache | Distributed Cache — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 386 |
| [`distributed-cache-design`](../../system-design/distributed-cache-design/) | Distributed Cache Design | Distributed Cache Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 85 |
| [`distributed-cache-educative-tests`](../../system-design/distributed-cache-educative-tests/) | Distributed Cache | Distributed Cache — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`distributed-cache-grokking`](../../system-design/distributed-cache-grokking/) | Distributed Cache Grokking | Distributed Cache Grokking — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 62 |
| [`distributed-cache-system`](../../system-design/distributed-cache-system/) | Distributed Cache System | Distributed Cache System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 187 |
| [`distributed-locking`](../../system-design/distributed-locking/) | Distributed Locking | Distributed Locking — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 504 |
| [`distributed-lru-cache`](../../system-design/distributed-lru-cache/) | Distributed Lru Cache | Distributed Lru Cache — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 377 |
| [`distributed-message-queue`](../../system-design/distributed-message-queue/) | Distributed Message Queue | Distributed Message Queue — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 210 |
| [`distributed-messaging-queue`](../../system-design/distributed-messaging-queue/) | Distributed Messaging Queue | Distributed Messaging Queue — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`distributed-messaging-queue-complete`](../../system-design/distributed-messaging-queue-complete/) | Distributed Messaging Queue Complete | Distributed Messaging Queue Complete — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`distributed-messaging-queue-design`](../../system-design/distributed-messaging-queue-design/) | Distributed Messaging Queue Design | Distributed Messaging Queue Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 85 |
| [`distributed-messaging-queue-educative-tests`](../../system-design/distributed-messaging-queue-educative-tests/) | Distributed Messaging Queue | Distributed Messaging Queue — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`distributed-messaging-queue-grokking`](../../system-design/distributed-messaging-queue-grokking/) | Distributed Messaging Queue Grokking | Distributed Messaging Queue Grokking — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 53 |
| [`distributed-mq`](../../system-design/distributed-mq/) | Distributed Mq | Distributed Mq — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 33 |
| [`distributed-search`](../../system-design/distributed-search/) | Distributed Search | Distributed Search — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 102 |
| [`distributed-search-system`](../../system-design/distributed-search-system/) | Distributed Search System | Distributed Search System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 270 |
| [`distributed_cache`](../../system-design/distributed_cache/) | Distributed Cache | Distributed Cache — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 344 |
| [`dns`](../../system-design/dns/) | Dns | Dns — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`dns-system`](../../system-design/dns-system/) | Dns System | Dns System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 50 |
| [`dns_network_services`](../../system-design/dns_network_services/) | Dns Network Services | Dns Network Services — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 222 |
| [`dns_system`](../../system-design/dns_system/) | Dns System | Dns System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 450 |
| [`dynamodb`](../../system-design/dynamodb/) | DynamoDB — System design hub | Amazon DynamoDB — access patterns, keys, indexes, consistency, streams, and cost. Original notes for interviews; not a copy of any third-party course. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`elastic`](../../system-design/elastic/) | Elastic | Elastic — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`email-service`](../../system-design/email-service/) | Email Service | Email Service — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 84 |
| [`file-cache`](../../system-design/file-cache/) | Design a File Cache System |  | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`file-storage-service`](../../system-design/file-storage-service/) | File Storage Service | File Storage Service — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 189 |
| [`file-storage-system`](../../system-design/file-storage-system/) | File Storage System | File Storage System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 155 |
| [`file-storage-system-design`](../../system-design/file-storage-system-design/) | File Storage | Comprehensive system design documentation for File Storage. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`filelock`](../../system-design/filelock/) | Filelock | Filelock — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 67 |
| [`filesystem`](../../system-design/filesystem/) | Design a File System |  | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`flink`](../../system-design/flink/) | Flink | Flink — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`folder-search-api`](../../system-design/folder-search-api/) | Folder search API | Prefix / typeahead search over folder hierarchies with ACL filtering. Related typeahead patterns: bq/00-index.md (trie / top-K cards). | ✓ ✓ ✓ ✓ ✓ | 54 |
| [`key-value-store`](../../system-design/key-value-store/) | Key Value Store | Key Value Store — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 380 |
| [`key-value-store-design`](../../system-design/key-value-store-design/) | Key Value Store Design | Key Value Store Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`key-value-store-tests`](../../system-design/key-value-store-tests/) | Key Value Store | Key Value Store — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`key-values`](../../system-design/key-values/) | Key Values | Key Values — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`load-balancer`](../../system-design/load-balancer/) | Load Balancer | Load Balancer — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`load-balancer-system`](../../system-design/load-balancer-system/) | Load Balancer System | Load Balancer System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 434 |
| [`load-balancer-system-design`](../../system-design/load-balancer-system-design/) | Load Balancer | Comprehensive system design documentation for Load Balancer. | ✓ ✓ ✓ ✓ ✓ | 155 |
| [`load-balancer-tests`](../../system-design/load-balancer-tests/) | Load Balancer | Load Balancer — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`loadbalancer`](../../system-design/loadbalancer/) | Loadbalancer | Loadbalancer — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 32 |
| [`lru-cache`](../../system-design/lru-cache/) | LRU Cache | Design a Least Recently Used (LRU) Cache | ✓ · · · · | 23 |
| [`message-queues`](../../system-design/message-queues/) | Message Queues | Message Queues — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 157 |
| [`messaging-system`](../../system-design/messaging-system/) | Messaging System | Messaging System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 299 |
| [`messaging_system`](../../system-design/messaging_system/) | Messaging System | Messaging System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 497 |
| [`mongodb`](../../system-design/mongodb/) | MongoDB — Document Database System Design |  | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`mq-demo`](../../system-design/mq-demo/) | Mq Demo | Mq Demo — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 55 |
| [`msg-queue`](../../system-design/msg-queue/) | Msg Queue | Msg Queue — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`mussel-key-value-store`](../../system-design/mussel-key-value-store/) | Mussel Key Value Store | Mussel Key Value Store — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 214 |
| [`notification-service`](../../system-design/notification-service/) | Notification Service | Notification Service — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 371 |
| [`notification-system`](../../system-design/notification-system/) | Notification System | Notification System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 95 |
| [`object-storage`](../../system-design/object-storage/) | Object Storage | Object Storage — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 117 |
| [`paste-bin`](../../system-design/paste-bin/) | Paste Bin | Paste Bin — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 160 |
| [`pastebin`](../../system-design/pastebin/) | Pastebin | Pastebin — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 261 |
| [`pastebin-system`](../../system-design/pastebin-system/) | Pastebin System | Pastebin System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 62 |
| [`pastebin-system-design`](../../system-design/pastebin-system-design/) | Pastebin | Comprehensive system design documentation for Pastebin. | ✓ ✓ ✓ ✓ ✓ | 207 |
| [`postgresql`](../../system-design/postgresql/) | PostgreSQL — Key Technology Deep Dive | PostgreSQL — when and how to use it in system design interviews. | ✓ ✓ ✓ ✓ ✓ | 33 |
| [`pub-sub-educative-tests`](../../system-design/pub-sub-educative-tests/) | Pub Sub | Pub Sub — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`pub-sub-system-design`](../../system-design/pub-sub-system-design/) | Pub-Sub | Comprehensive system design documentation for Pub-Sub. | ✓ ✓ ✓ ✓ ✓ | 98 |
| [`pubsub`](../../system-design/pubsub/) | Pubsub | Pubsub — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`rate-limiter`](../../system-design/rate-limiter/) | Rate Limiter | Design a distributed rate limiter for a social media API that handles 1M requests/sec across 100M DAU, using Token Bucket algorithm with Redis, API Gateway plac | ✓ ✓ ✓ ✓ ✓ | 336 |
| [`rate-limiter-design`](../../system-design/rate-limiter-design/) | Rate Limiter | Design a distributed rate limiter for a social media API that handles 1M requests/sec across 100M DAU, using Token Bucket algorithm with Redis, API Gateway plac | ✓ ✓ ✓ ✓ ✓ | 111 |
| [`rate-limiter-educative-tests`](../../system-design/rate-limiter-educative-tests/) | Rate Limiter | Design a distributed rate limiter for a social media API that handles 1M requests/sec across 100M DAU, using Token Bucket algorithm with Redis, API Gateway plac | ✓ ✓ ✓ ✓ ✓ | 61 |
| [`rate-limiter-production`](../../system-design/rate-limiter-production/) | Rate Limiter | Design a distributed rate limiter for a social media API that handles 1M requests/sec across 100M DAU, using Token Bucket algorithm with Redis, API Gateway plac | ✓ ✓ ✓ ✓ ✓ | 184 |
| [`rate-limiter-system`](../../system-design/rate-limiter-system/) | Rate Limiter | Design a distributed rate limiter for a social media API that handles 1M requests/sec across 100M DAU, using Token Bucket algorithm with Redis, API Gateway plac | ✓ ✓ ✓ ✓ ✓ | 95 |
| [`rate-limiter-system-design`](../../system-design/rate-limiter-system-design/) | Rate Limiter | Design a distributed rate limiter for a social media API that handles 1M requests/sec across 100M DAU, using Token Bucket algorithm with Redis, API Gateway plac | ✓ ✓ ✓ ✓ ✓ | 155 |
| [`rate-limiting`](../../system-design/rate-limiting/) | Rate Limiter | Design a distributed rate limiter for a social media API that handles 1M requests/sec across 100M DAU, using Token Bucket algorithm with Redis, API Gateway plac | ✓ ✓ ✓ ✓ ✓ | 59 |
| [`ratelimit`](../../system-design/ratelimit/) | Rate Limiter | Design a distributed rate limiter for a social media API that handles 1M requests/sec across 100M DAU, using Token Bucket algorithm with Redis, API Gateway plac | ✓ ✓ ✓ ✓ ✓ | 59 |
| [`ratelimiter`](../../system-design/ratelimiter/) | Rate Limiter | Design a distributed rate limiter for a social media API that handles 1M requests/sec across 100M DAU, using Token Bucket algorithm with Redis, API Gateway plac | ✓ ✓ ✓ ✓ ✓ | 60 |
| [`redis`](../../system-design/redis/) | Redis | Redis — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`s3`](../../system-design/s3/) | S3 | S3 — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 154 |
| [`s3-like-storage`](../../system-design/s3-like-storage/) | S3 Like Storage | S3 Like Storage — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 100 |
| [`sharded-counters`](../../system-design/sharded-counters/) | Sharded Counters | Sharded Counters — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 439 |
| [`shared-counters`](../../system-design/shared-counters/) | Shared Counters | Shared Counters — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`tidb-transaction`](../../system-design/tidb-transaction/) | Tidb Transaction | Tidb Transaction — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 174 |
| [`time-series`](../../system-design/time-series/) | Time Series | Time Series — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 197 |
| [`time-series-database`](../../system-design/time-series-database/) | Time Series Database | Time Series Database — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 192 |
| [`tinyurl`](../../system-design/tinyurl/) | Tinyurl | Tinyurl — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 454 |
| [`tinyurl-system`](../../system-design/tinyurl-system/) | Tinyurl System | Tinyurl System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 156 |
| [`topk`](../../system-design/topk/) | Topk | Topk — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 324 |
| [`trending-topic-system`](../../system-design/trending-topic-system/) | Trending Topic System | Trending Topic System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 245 |
| [`tsdb_demo`](../../system-design/tsdb_demo/) | Tsdb Demo | Tsdb Demo — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`typeahead`](../../system-design/typeahead/) | Typeahead | Typeahead — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 422 |
| [`typeahead-box-search`](../../system-design/typeahead-box-search/) | Typeahead box for a search engine — system design interview hub | Real-time query suggestions as the user types into a search box—ranked completions, low latency, high availability, and a pipeline that learns from implicit fee | ✓ · · · ✓ | 45 |
| [`typeahead-suggestion-system`](../../system-design/typeahead-suggestion-system/) | Typeahead Suggestion System | Typeahead Suggestion System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 340 |
| [`typeahead-system`](../../system-design/typeahead-system/) | Typeahead System | Typeahead System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 217 |
| [`typeahead-tests`](../../system-design/typeahead-tests/) | Typeahead | Typeahead — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`typehead`](../../system-design/typehead/) | Typehead | Typehead — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 340 |
| [`unique-id`](../../system-design/unique-id/) | Unique Id | Unique Id — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`unique-id-educative-tests`](../../system-design/unique-id-educative-tests/) | Unique Id | Unique Id — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`unique-id-generator`](../../system-design/unique-id-generator/) | Unique Id Generator | Unique Id Generator — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 202 |
| [`unique_id_generator`](../../system-design/unique_id_generator/) | Unique Id Generator | Unique Id Generator — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 180 |
| [`url-handling`](../../system-design/url-handling/) | Url Handling | Url Handling — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`url-shorten`](../../system-design/url-shorten/) | Url Shorten | Url Shorten — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`url-shortener`](../../system-design/url-shortener/) | Url Shortener | Url Shortener — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 122 |
| [`url-shortener-bitly`](../../system-design/url-shortener-bitly/) | Url Shortener Bitly | Url Shortener Bitly — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 50 |
| [`url-shortener-design`](../../system-design/url-shortener-design/) | Url Shortener Design | Url Shortener Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 66 |
| [`url-shortener-educative-tests`](../../system-design/url-shortener-educative-tests/) | Url Shortener | Url Shortener — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`url-shortener-system`](../../system-design/url-shortener-system/) | Url Shortener System | Url Shortener System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 82 |
| [`url-shortening`](../../system-design/url-shortening/) | Url Shortening | Url Shortening — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`url-shortening-service`](../../system-design/url-shortening-service/) | Url Shortening Service | Url Shortening Service — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 84 |
| [`url_shortener`](../../system-design/url_shortener/) | Url Shortener | Url Shortener — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`web-analytics`](../../system-design/web-analytics/) | Web Analytics | Web Analytics — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 188 |
| [`web-analytics-system`](../../system-design/web-analytics-system/) | Web Analytics System | Web Analytics System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 402 |
| [`web-crawler-system`](../../system-design/web-crawler-system/) | Web Crawler System | Web Crawler System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 376 |
| [`web-crawler-system-design`](../../system-design/web-crawler-system-design/) | Web Crawler | Comprehensive system design documentation for Web Crawler. | ✓ ✓ ✓ ✓ ✓ | 93 |
| [`web-crawler-tests`](../../system-design/web-crawler-tests/) | Web Crawler | Web Crawler — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`webcrawler`](../../system-design/webcrawler/) | Webcrawler | Webcrawler — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`webcrawlers`](../../system-design/webcrawlers/) | Webcrawlers | Webcrawlers — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`zookeeper`](../../system-design/zookeeper/) | Zookeeper | Zookeeper — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |

## 经典产品设计 / Classic product designs（142）

> 短链/信息流/IM/视频/打车/外卖/票务/支付/文档协同/地图……

| 目录 | 标题 | 一句话 | 文档 | 文件数 |
|---|---|---|---|---|
| [`airtag`](../../system-design/airtag/) | AirTag-class finding network — system design interview hub | Crowdsourced lost-item locating: BLE (and optionally UWB) tags, mobile devices that report sightings, backend that aggregates estimates and serves last known /  | ✓ · · · · | 31 |
| [`alexa`](../../system-design/alexa/) | Alexa — pointer hub |  | ✓ · · · · | 1 |
| [`alexa-emergency-break-in`](../../system-design/alexa-emergency-break-in/) | Alexa-class emergency service — break-in scenario (system design) | Voice-forward home emergency for a break-in or intrusion scenario: fast SOS, household coordination, optional camera/stream context, and strong false-positive c | ✓ · · · ✓ | 37 |
| [`alexa-voice-commands`](../../system-design/alexa-voice-commands/) | How Alexa processes voice commands — system design hub | End-to-end voice assistant pipeline: wake → stream → ASR → NLU → route / skill / smart home → TTS → playback; plus latency, privacy, security, and failure behav | ✓ ✓ ✓ ✓ ✓ | 31 |
| [`amazon-food-delivery-launch`](../../system-design/amazon-food-delivery-launch/) | Amazon restaurant food delivery — launch (product & strategy hub) |  | ✓ ✓ ✓ ✓ ✓ | 29 |
| [`amazon-kindle-payment`](../../system-design/amazon-kindle-payment/) | Amazon Kindle payment (digital goods) | System design for e-book purchase and fulfillment in a Kindle-class product: checkout, payment orchestration, entitlement (right to read), notifications, and au | ✓ · · · · | 27 |
| [`amazon-prime-day`](../../system-design/amazon-prime-day/) | Amazon Prime Day / flash-sale — System design hub | Peak retail traffic, availability vs scalability, dependency fan-out, and runbook patterns—without pasting third-party course text. Not affiliated with Amazon o | ✓ ✓ ✓ ✓ ✓ | 31 |
| [`auction`](../../system-design/auction/) | Auction | Auction — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`book_subscription`](../../system-design/book_subscription/) | Book Subscription | Book Subscription — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 457 |
| [`book_subscription_system`](../../system-design/book_subscription_system/) | Book Subscription System | Book Subscription System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 32 |
| [`calendar-system`](../../system-design/calendar-system/) | Calendar System | Calendar System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 58 |
| [`chat-app-system`](../../system-design/chat-app-system/) | Chat App System | Chat App System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 31 |
| [`chess`](../../system-design/chess/) | Chess | Chess — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 322 |
| [`chessboard-netflix-system-design`](../../system-design/chessboard-netflix-system-design/) | Chess board + Netflix-style recommendations — System design hub |  | ✓ ✓ ✓ ✓ ✓ | 40 |
| [`conference-room-booking`](../../system-design/conference-room-booking/) | Conference Room Booking | Conference Room Booking — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 178 |
| [`conference-room-booking-system`](../../system-design/conference-room-booking-system/) | Conference Room Booking System | Conference Room Booking System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`craigslist-system`](../../system-design/craigslist-system/) | Craigslist System | Craigslist System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 111 |
| [`cyclist`](../../system-design/cyclist/) | Cyclist performance tracking — system design interview hub | Mobile-first app for recording rides, sensor telemetry (GPS, HR, power), offline capture, cloud sync, history, and light social/leaderboards—typical of a fitnes | ✓ · · · · | 28 |
| [`doordash`](../../system-design/doordash/) | DoorDash — detecting & preventing review abuse (entry hub) | Find in-repo material for prompts like “Design how we detect and prevent review abuse on a marketplace / food-delivery platform.” This page does not duplicate t | ✓ · · · · | 4 |
| [`doordash-logistics`](../../system-design/doordash-logistics/) | DoorDash-class real-time food delivery logistics | Three-sided marketplace — diners, restaurants, couriers — with order management, batching-aware dispatch, geospatial routing / ETA, demand prediction, dynamic d | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`dream11-leaderboard`](../../system-design/dream11-leaderboard/) | Dream11-style fantasy leaderboard — System design hub | Real-time leaderboard for fantasy gaming: ~100,000 registered teams, per-league boards, live score updates, fast top-N and my rank reads. | ✓ ✓ ✓ ✓ ✓ | 36 |
| [`dropbox`](../../system-design/dropbox/) | Dropbox | Dropbox — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`e-commerce`](../../system-design/e-commerce/) | E-commerce platform | Design an e-commerce website — catalog, cart, checkout, orders, inventory, payments, recommendations — architecture, trade-offs, and scale. | ✓ ✓ ✓ ✓ ✓ | 31 |
| [`ecommerce-microservices`](../../system-design/ecommerce-microservices/) | E-commerce microservices | Design an e-commerce website decomposed into microservices — bounded contexts, gateway/BFF, async integration, and polyglot data. | ✓ ✓ ✓ ✓ ✓ | 312 |
| [`ecommerce-platform-design`](../../system-design/ecommerce-platform-design/) | Ecommerce platform design | Design an e-commerce website — same domain as e-commerce/00-index.md, with extra rust/, cpp/, and docs/ study trees. | ✓ ✓ ✓ ✓ ✓ | 167 |
| [`facebook-messenger-system`](../../system-design/facebook-messenger-system/) | Facebook Messenger System | Facebook Messenger System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 276 |
| [`fb-live-comments`](../../system-design/fb-live-comments/) | Fb Live Comments | Fb Live Comments — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`fb-live-comments-tests`](../../system-design/fb-live-comments-tests/) | Fb Live Comments | Fb Live Comments — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`fb-news-feed`](../../system-design/fb-news-feed/) | Fb News Feed | Fb News Feed — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`fb-news-feed-tests`](../../system-design/fb-news-feed-tests/) | Fb News Feed | Fb News Feed — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`fb-post-search`](../../system-design/fb-post-search/) | Fb Post Search | Fb Post Search — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`food`](../../system-design/food/) | Food — Food Delivery Marketplace System Design |  | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`food-delivery`](../../system-design/food-delivery/) | Food delivery marketplace — system design hub |  | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`food-delivery-service`](../../system-design/food-delivery-service/) | Food delivery marketplace — system design hub (Zomato / Swiggy / Uber Eats–class) | Three-sided marketplace: customers discover restaurants and place orders, restaurants manage menus and prep, couriers deliver; includes search, checkout, paymen | ✓ ✓ ✓ ✓ ✓ | 161 |
| [`food-delivery-service-v2`](../../system-design/food-delivery-service-v2/) | Food Delivery Service V2 | Food Delivery Service V2 — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 94 |
| [`food-delivery-system`](../../system-design/food-delivery-system/) | Food Delivery System | Food Delivery System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 131 |
| [`food-delivery-time`](../../system-design/food-delivery-time/) | Food Delivery Time | Food Delivery Time — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 120 |
| [`food-delivery-time-estimation`](../../system-design/food-delivery-time-estimation/) | Food Delivery Time Estimation | Food Delivery Time Estimation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 223 |
| [`gaming`](../../system-design/gaming/) | Gaming — Multiplayer Online Gaming Platform System Design |  | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`google-docs`](../../system-design/google-docs/) | Google Docs — System Design Hub | Design a collaborative document editor (Google Docs) supporting real-time multi-user editing with Operational Transformation, WebSocket scaling via consistent h | ✓ ✓ ✓ ✓ ✓ | 660 |
| [`google-docs-demo`](../../system-design/google-docs-demo/) | Google Docs — System Design Hub | Design a collaborative document editor (Google Docs) supporting real-time multi-user editing with Operational Transformation, WebSocket scaling via consistent h | ✓ ✓ ✓ ✓ ✓ | 103 |
| [`google-docs-k8s`](../../system-design/google-docs-k8s/) | Google Docs — System Design Hub | Design a collaborative document editor (Google Docs) supporting real-time multi-user editing with Operational Transformation, WebSocket scaling via consistent h | ✓ ✓ ✓ ✓ ✓ | 29 |
| [`google-docs-system`](../../system-design/google-docs-system/) | Google Docs — System Design Hub | Design a collaborative document editor (Google Docs) supporting real-time multi-user editing with Operational Transformation, WebSocket scaling via consistent h | ✓ ✓ ✓ ✓ ✓ | 273 |
| [`google-maps`](../../system-design/google-maps/) | Google Maps | Google Maps — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 56 |
| [`google-maps-tests`](../../system-design/google-maps-tests/) | Google Maps | Google Maps — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`google_docs`](../../system-design/google_docs/) | Google Docs — System Design Hub | Design a collaborative document editor (Google Docs) supporting real-time multi-user editing with Operational Transformation, WebSocket scaling via consistent h | ✓ ✓ ✓ ✓ ✓ | 34 |
| [`google_maps`](../../system-design/google_maps/) | Google Maps | Google Maps — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 88 |
| [`hardware`](../../system-design/hardware/) | Hardware — IoT Warehouse Temperature & Social Distance System Design | Hardware — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 29 |
| [`hotel-booking-system`](../../system-design/hotel-booking-system/) | Hotel Booking System | Hotel Booking System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 114 |
| [`image-hosting-service`](../../system-design/image-hosting-service/) | Image Hosting Service | Image Hosting Service — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 94 |
| [`image-hosting-system`](../../system-design/image-hosting-system/) | Image Hosting System | Image Hosting System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 86 |
| [`instagram`](../../system-design/instagram/) | Instagram | Instagram — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 432 |
| [`instagram-design-comprehensive-hub`](../../system-design/instagram-design-comprehensive-hub/) | Design Instagram — Comprehensive Interview Hub | Instagram-like photo/video sharing — requirements, BOE, architecture, feed, search, engagement, scaling, and interview prep. | ✓ · · · · | 30 |
| [`instagram-interview-hub`](../../system-design/instagram-interview-hub/) | Instagram System Design Hub |  | ✓ · · · · | 27 |
| [`instagram-system`](../../system-design/instagram-system/) | Instagram System | Instagram System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 183 |
| [`instagram-system-design`](../../system-design/instagram-system-design/) | Instagram | Comprehensive system design documentation for Instagram. | ✓ ✓ ✓ ✓ ✓ | 269 |
| [`instagram-tests`](../../system-design/instagram-tests/) | Instagram | Instagram — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`instagram_clone`](../../system-design/instagram_clone/) | Instagram Clone | Instagram Clone — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 257 |
| [`job-aggregator`](../../system-design/job-aggregator/) | Job Aggregator | Job Aggregator — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 175 |
| [`job-collector`](../../system-design/job-collector/) | Job Collector | Job Collector — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 144 |
| [`job-scraper-system`](../../system-design/job-scraper-system/) | Job Scraper System | Job Scraper System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 246 |
| [`job-system`](../../system-design/job-system/) | Job System | Job System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 168 |
| [`jobright-ai-backend`](../../system-design/jobright-ai-backend/) | Jobright Ai Backend | Jobright Ai Backend — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`jobright-ai-system`](../../system-design/jobright-ai-system/) | Jobright Ai System | Jobright Ai System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 280 |
| [`jobright-clone`](../../system-design/jobright-clone/) | Jobright Clone | Jobright Clone — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 1070 |
| [`kindle`](../../system-design/kindle/) | Kindle digital-goods payment — system design interview hub | End-to-end payment for digital content (e-books, subscriptions) on a Kindle-class storefront: checkout, PSP integration, entitlement grant, idempotency, receipt | ✓ · · · · | 28 |
| [`live-comments-system`](../../system-design/live-comments-system/) | Live Comments System | Live Comments System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`live-streaming-platform`](../../system-design/live-streaming-platform/) | Live Streaming Platform | Live Streaming Platform — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 131 |
| [`live-streaming-platform-detailed`](../../system-design/live-streaming-platform-detailed/) | Live Streaming Platform — System Design Hub | Design a live streaming platform (Twitch / YouTube Live) supporting real-time video ingest, adaptive-bitrate transcoding, CDN distribution, live chat, and strea | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`live-streaming-system`](../../system-design/live-streaming-system/) | Live Streaming System | Live Streaming System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 82 |
| [`live-streaming-system-design`](../../system-design/live-streaming-system-design/) | Live Streaming | Comprehensive system design documentation for Live Streaming. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`local-delivery-service`](../../system-design/local-delivery-service/) | Local Delivery Service | Local Delivery Service — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`messenger`](../../system-design/messenger/) | Messenger | Messenger — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 405 |
| [`new-aggregator`](../../system-design/new-aggregator/) | New Aggregator | New Aggregator — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`news-aggregator`](../../system-design/news-aggregator/) | News Aggregator | News Aggregator — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`news-feed-aggregator`](../../system-design/news-feed-aggregator/) | News Feed Aggregator | News Feed Aggregator — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 140 |
| [`newsfeed`](../../system-design/newsfeed/) | Newsfeed | Newsfeed — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`newsfeed-system`](../../system-design/newsfeed-system/) | Newsfeed System | Newsfeed System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 723 |
| [`newsfeed-tests`](../../system-design/newsfeed-tests/) | Newsfeed | Newsfeed — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`newsfeed_system`](../../system-design/newsfeed_system/) | Newsfeed System | Newsfeed System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 50 |
| [`online-auction`](../../system-design/online-auction/) | Online Auction | Online Auction — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`online-chess`](../../system-design/online-chess/) | Online Chess | Online Chess — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 230 |
| [`online-education-system-design`](../../system-design/online-education-system-design/) | Online Education | Comprehensive system design documentation for Online Education. | ✓ ✓ ✓ ✓ ✓ | 171 |
| [`online-judge-system`](../../system-design/online-judge-system/) | Online Judge System | Online Judge System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 56 |
| [`payment`](../../system-design/payment/) | Payment System (Stripe) | Design a payment processing platform (like Stripe) that allows merchants to accept credit/debit card payments, guarantees transaction safety with idempotency, a | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`payment-system-hello-interview`](../../system-design/payment-system-hello-interview/) | Payment System Like Stripe |  | ✓ ✓ ✓ ✓ ✓ | 37 |
| [`payment-tests`](../../system-design/payment-tests/) | Payment System — Test Suite & Validation | Test infrastructure and validation strategy for the payment system design demos. Covers smoke tests, integration tests, and idempotency verification across mult | ✓ ✓ ✓ ✓ ✓ | 29 |
| [`price-tracking-service`](../../system-design/price-tracking-service/) | Price Tracking Service | Price Tracking Service — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`prime-video`](../../system-design/prime-video/) | Design Prime Video — System design hub | Amazon Prime Video streaming platform: video upload, transcoding, adaptive bitrate delivery via CDN, search, recommendations, watchlist, multi-device playback f | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`public-transit-system`](../../system-design/public-transit-system/) | Public Transit System | Public Transit System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 103 |
| [`public-transportation-system`](../../system-design/public-transportation-system/) | Public Transportation System | Public Transportation System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 204 |
| [`quora`](../../system-design/quora/) | Quora | Quora — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 79 |
| [`quora-system-design`](../../system-design/quora-system-design/) | Quora | Comprehensive system design documentation for Quora. | ✓ ✓ ✓ ✓ ✓ | 165 |
| [`quora-tests`](../../system-design/quora-tests/) | Quora | Quora — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`robinhood`](../../system-design/robinhood/) | Robinhood | Design a commission-free stock brokerage that shows live prices via SSE, manages orders (market/limit) through an exchange, and scales to 20M DAU with 100M trad | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`spotify`](../../system-design/spotify/) | Spotify | Music streaming, discovery, and qualified listen analytics (e.g. >30s play → history / DWH) — in-repo TryExponent 2073 is link-only in 22 (not affiliated). | ✓ ✓ ✓ ✓ ✓ | 34 |
| [`spotify-system-design`](../../system-design/spotify-system-design/) | Spotify | Comprehensive system design documentation for Spotify. | ✓ ✓ ✓ ✓ ✓ | 32 |
| [`spotify-tests`](../../system-design/spotify-tests/) | spotify-tests — hub index |  | ✓ ✓ ✓ ✓ ✓ | 32 |
| [`stock-exchange`](../../system-design/stock-exchange/) | Stock Exchange | Design a stock exchange (order matching engine) that matches buy/sell orders with < 1ms latency, handles 100K orders/sec, and maintains strict price-time priori | ✓ ✓ ✓ ✓ ✓ | 64 |
| [`stock-trading-platform`](../../system-design/stock-trading-platform/) | Stock Trading Platform | Stock Trading Platform — retail brokerage architecture for portfolio management, order execution, and real-time market data. | ✓ ✓ ✓ ✓ ✓ | 61 |
| [`strava`](../../system-design/strava/) | Strava | Strava — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`task-management`](../../system-design/task-management/) | Task Management | Task Management — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 147 |
| [`ticketing`](../../system-design/ticketing/) | Peak-traffic ticketing — system design hub | Large-scale event ticketing under flash crowds (on-sale spikes, Black Friday–class peaks): inventory, no double booking, payments, and read-heavy discovery vs w | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`ticketmaster`](../../system-design/ticketmaster/) | Ticketmaster | Ticketmaster — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`ticketmaster-educative-tests`](../../system-design/ticketmaster-educative-tests/) | Ticketmaster | Ticketmaster — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`ticketmaster-system`](../../system-design/ticketmaster-system/) | Ticketmaster System | Ticketmaster System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`ticketmaster-system-design`](../../system-design/ticketmaster-system-design/) | Ticketmaster | Comprehensive system design documentation for Ticketmaster. | ✓ ✓ ✓ ✓ ✓ | 143 |
| [`tictactoe`](../../system-design/tictactoe/) | Remote Tic Tac Toe — System design hub | Two-player Tic Tac Toe over the network: realtime moves, authoritative server state, reconnect, minimal cheating surface. | ✓ ✓ ✓ ✓ ✓ | 35 |
| [`tiktok`](../../system-design/tiktok/) | Design TikTok — System design hub | Short-form UGC video at billion-user scale: capture and upload, transcode to an encoding ladder, CDN delivery, For You personalized feed (retrieval + ranking),  | ✓ ✓ ✓ ✓ ✓ | 32 |
| [`tinder`](../../system-design/tinder/) | Tinder | Tinder — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`transit-system`](../../system-design/transit-system/) | Transit System | Transit System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 92 |
| [`translation-service-system`](../../system-design/translation-service-system/) | Translation Service System | Translation Service System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`twitch`](../../system-design/twitch/) | Twitch | Twitch — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 289 |
| [`twitch-system`](../../system-design/twitch-system/) | Twitch System | Twitch System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 294 |
| [`twitter`](../../system-design/twitter/) | Twitter | Twitter — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 181 |
| [`twitter-educative-tests`](../../system-design/twitter-educative-tests/) | Twitter | Twitter — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`twitter-facebook-system-design`](../../system-design/twitter-facebook-system-design/) | Twitter Facebook | Comprehensive system design documentation for Twitter Facebook. | ✓ ✓ ✓ ✓ ✓ | 99 |
| [`twitter-system`](../../system-design/twitter-system/) | Twitter System | Twitter System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 125 |
| [`twitter-tests`](../../system-design/twitter-tests/) | Twitter | Twitter — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`twitter_clone`](../../system-design/twitter_clone/) | Twitter Clone | Twitter Clone — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 410 |
| [`uber`](../../system-design/uber/) | Uber | Uber — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 300 |
| [`uber-eats`](../../system-design/uber-eats/) | Uber Eats–class food delivery — system design interview hub | Three-sided marketplace: diners discover menus, restaurants accept and prepare orders, couriers fulfill delivery; backend handles search, checkout, payments, di | ✓ · · · · | 38 |
| [`uber-eats-system`](../../system-design/uber-eats-system/) | Uber Eats System | Uber Eats System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 98 |
| [`uber-tests`](../../system-design/uber-tests/) | Uber | Uber — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 41 |
| [`uber_clone`](../../system-design/uber_clone/) | Uber Clone | Uber Clone — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 61 |
| [`vending`](../../system-design/vending/) | Vending & unattended retail — cross-link hub |  | ✓ ✓ ✓ ✓ ✓ | 33 |
| [`video-streaming`](../../system-design/video-streaming/) | Video Streaming | Video Streaming — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 58 |
| [`video_streaming`](../../system-design/video_streaming/) | Video Streaming | Video Streaming — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 429 |
| [`voting-system`](../../system-design/voting-system/) | Voting System | Voting System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 277 |
| [`whatsapp`](../../system-design/whatsapp/) | Whatsapp | Whatsapp — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 234 |
| [`whatsapp-high-level-simulation`](../../system-design/whatsapp-high-level-simulation/) | Whatsapp High Level Simulation | Whatsapp High Level Simulation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 30 |
| [`whatsapp-messenger-design`](../../system-design/whatsapp-messenger-design/) | Whatsapp Messenger Design | Whatsapp Messenger Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`whatsapp-system`](../../system-design/whatsapp-system/) | Whatsapp System | Whatsapp System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 153 |
| [`whatsapp-system-design`](../../system-design/whatsapp-system-design/) | WhatsApp | Comprehensive system design documentation for WhatsApp. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`whatsapp-tests`](../../system-design/whatsapp-tests/) | Whatsapp | Whatsapp — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`yelp`](../../system-design/yelp/) | Yelp | Yelp — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`yelp-system`](../../system-design/yelp-system/) | Yelp System | Yelp System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 197 |
| [`youtube`](../../system-design/youtube/) | Youtube | Youtube — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 175 |
| [`youtube-reality-is-more-complicated`](../../system-design/youtube-reality-is-more-complicated/) | Youtube Reality Is More Complicated | Youtube Reality Is More Complicated — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 160 |
| [`youtube-system`](../../system-design/youtube-system/) | Youtube System | Youtube System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 56 |
| [`youtube-system-design`](../../system-design/youtube-system-design/) | YouTube | Comprehensive system design documentation for YouTube. | ✓ ✓ ✓ ✓ ✓ | 177 |
| [`youtube-tests`](../../system-design/youtube-tests/) | Youtube | Youtube — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |

## 运维与基础设施系统 / Ops & infrastructure systems（98）

> 监控/日志/任务调度/发布系统/容灾/K8s 与容器编排/会话/安全合规

| 目录 | 标题 | 一句话 | 文档 | 文件数 |
|---|---|---|---|---|
| [`ansible-complete-implementation`](../../system-design/ansible-complete-implementation/) | Ansible Complete Implementation | Ansible Complete Implementation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 283 |
| [`ansible-meta-pe`](../../system-design/ansible-meta-pe/) | Ansible & platform engineering | Idempotent automation, inventory, rollout safety—PE interview angles. Pairs with API migrations when infra moves too. | ✓ ✓ ✓ ✓ ✓ | 131 |
| [`async-communication-web-service-hub`](../../system-design/async-communication-web-service-hub/) | Design a Web Service for Asynchronous Communication |  | ✓ · · · · | 25 |
| [`aviatrix-deep-dive`](../../system-design/aviatrix-deep-dive/) | Aviatrix Deep Dive | Aviatrix Deep Dive — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 385 |
| [`bank-legacy-digitalization`](../../system-design/bank-legacy-digitalization/) | Bank legacy data → digital platform | *How would you digitalize a bank with legacy data?* (typical Solutions Architect / transformation framing — in-repo original material; TryExponent [5533] is not | ✓ · · · ✓ | 13 |
| [`client-side`](../../system-design/client-side/) | Client Side | Client Side — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`client-side-monitoring-educative-tests`](../../system-design/client-side-monitoring-educative-tests/) | Client Side Monitoring | Client Side Monitoring — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`client_side_monitoring`](../../system-design/client_side_monitoring/) | Client Side Monitoring | Client Side Monitoring — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 305 |
| [`cloud-infra-system`](../../system-design/cloud-infra-system/) | Cloud Infra System | Cloud Infra System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 256 |
| [`cloud-infra-tech-company`](../../system-design/cloud-infra-tech-company/) | Cloud Infra Tech Company | Cloud Infra Tech Company — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 195 |
| [`cloud-infrastructure`](../../system-design/cloud-infrastructure/) | Cloud Infrastructure | Cloud Infrastructure — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 503 |
| [`cloud-infrastructure-design`](../../system-design/cloud-infrastructure-design/) | Cloud Infrastructure Design | Cloud Infrastructure Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 124 |
| [`cloud-infrastructure-system`](../../system-design/cloud-infrastructure-system/) | Cloud Infrastructure System | Cloud Infrastructure System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 422 |
| [`code-deployment`](../../system-design/code-deployment/) | Code Deployment | Code Deployment — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`code-deployment-tests`](../../system-design/code-deployment-tests/) | Code Deployment | Code Deployment — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`code-deployments`](../../system-design/code-deployments/) | Code Deployments | Code Deployments — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`colima`](../../system-design/colima/) | Colima | Colima — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`container-orchestration-system`](../../system-design/container-orchestration-system/) | Container Orchestration System | Container Orchestration System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 196 |
| [`container-orchestration-system-design`](../../system-design/container-orchestration-system-design/) | Container Orchestration | Comprehensive system design documentation for Container Orchestration. | ✓ ✓ ✓ ✓ ✓ | 144 |
| [`cybersecurity-incident-response`](../../system-design/cybersecurity-incident-response/) | Cybersecurity Incident Response | Cybersecurity Incident Response — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 119 |
| [`data-privacy-compliance-system`](../../system-design/data-privacy-compliance-system/) | Data Privacy Compliance System | Data Privacy Compliance System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`dhcp-data-center`](../../system-design/dhcp-data-center/) | Dhcp Data Center | Dhcp Data Center — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`disaster-recovery-system`](../../system-design/disaster-recovery-system/) | Disaster Recovery System | Disaster Recovery System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 221 |
| [`disaster-recovery-system-app`](../../system-design/disaster-recovery-system-app/) | Disaster Recovery System App | Disaster Recovery System App — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 178 |
| [`disaster-recovery-system-design`](../../system-design/disaster-recovery-system-design/) | Disaster Recovery | Comprehensive system design documentation for Disaster Recovery. | ✓ ✓ ✓ ✓ ✓ | 60 |
| [`disaster-recovery-system-enhanced`](../../system-design/disaster-recovery-system-enhanced/) | Disaster Recovery System Enhanced | Disaster Recovery System Enhanced — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 186 |
| [`distribute-logging`](../../system-design/distribute-logging/) | distribute-logging (navigation alias) |  | · · · · · | 1 |
| [`distribute-logs`](../../system-design/distribute-logs/) | Distribute Logs | Distribute Logs — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`distributed-job-scheduler`](../../system-design/distributed-job-scheduler/) | Distributed Job Scheduler | Distributed Job Scheduler — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 241 |
| [`distributed-job-scheduler-hub`](../../system-design/distributed-job-scheduler-hub/) | 00 – Index |  | ✓ · · · · | 27 |
| [`distributed-logging`](../../system-design/distributed-logging/) | Distributed Logging | Distributed Logging — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 29 |
| [`distributed-logging-educative-tests`](../../system-design/distributed-logging-educative-tests/) | Distributed Logging | Distributed Logging — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`distributed-monitoring`](../../system-design/distributed-monitoring/) | Distributed Monitoring | Distributed Monitoring — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`distributed-monitoring-system`](../../system-design/distributed-monitoring-system/) | Distributed Monitoring System | Distributed Monitoring System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 321 |
| [`distributed-process-monitor`](../../system-design/distributed-process-monitor/) | Distributed Process Monitor | Distributed Process Monitor — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 32 |
| [`distributed-task-scheduler`](../../system-design/distributed-task-scheduler/) | Distributed Task Scheduler | Distributed Task Scheduler — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 176 |
| [`distributed-task-scheduler-tests`](../../system-design/distributed-task-scheduler-tests/) | Distributed Task Scheduler | Distributed Task Scheduler — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`distributed-task-scheduler-zookeeper`](../../system-design/distributed-task-scheduler-zookeeper/) | Distributed Task Scheduler Zookeeper | Distributed Task Scheduler Zookeeper — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 103 |
| [`drs-scaffold`](../../system-design/drs-scaffold/) | Drs Scaffold | Drs Scaffold — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 500 |
| [`dynamic-kubernetes-scaling`](../../system-design/dynamic-kubernetes-scaling/) | Dynamic Kubernetes Scaling | Dynamic Kubernetes Scaling — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 215 |
| [`enterprise-monitoring`](../../system-design/enterprise-monitoring/) | Enterprise Monitoring | Enterprise Monitoring — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 50 |
| [`enterprise_monitoring`](../../system-design/enterprise_monitoring/) | Enterprise Monitoring | Enterprise Monitoring — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 266 |
| [`f5_data_platform`](../../system-design/f5_data_platform/) | F5 Data Platform | F5 Data Platform — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`firmware`](../../system-design/firmware/) | Design a Firmware Update System — study hub |  | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`health-monitoring-system`](../../system-design/health-monitoring-system/) | Health Monitoring System | Health Monitoring System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 132 |
| [`health-monitoring-system-v2`](../../system-design/health-monitoring-system-v2/) | Health Monitoring System V2 | Health Monitoring System V2 — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 95 |
| [`helm-chart`](../../system-design/helm-chart/) | Helm Chart | Helm Chart — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 52 |
| [`incident-response-system`](../../system-design/incident-response-system/) | Incident Response System | Incident Response System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 97 |
| [`infra-dr-system`](../../system-design/infra-dr-system/) | Infra Dr System | Infra Dr System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 342 |
| [`intelligent-automation`](../../system-design/intelligent-automation/) | Intelligent Automation | Intelligent Automation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 214 |
| [`job-scheduler`](../../system-design/job-scheduler/) | Job Scheduler | Job Scheduler — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`job-scheduler-system`](../../system-design/job-scheduler-system/) | Job Scheduler System | Job Scheduler System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 503 |
| [`juicefs_metadata_engine`](../../system-design/juicefs_metadata_engine/) | Juicefs Metadata Engine | Juicefs Metadata Engine — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 31 |
| [`k8s`](../../system-design/k8s/) | K8S | K8S — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 381 |
| [`k8s-manifests`](../../system-design/k8s-manifests/) | K8S Manifests | K8S Manifests — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 388 |
| [`kubectl-api-demo`](../../system-design/kubectl-api-demo/) | Kubectl Api Demo | Kubectl Api Demo — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 190 |
| [`kuberentes`](../../system-design/kuberentes/) | Kuberentes | Kuberentes — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`kubernetes`](../../system-design/kubernetes/) | Kubernetes | Kubernetes — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 594 |
| [`kubernetes-manifests`](../../system-design/kubernetes-manifests/) | Kubernetes Manifests | Kubernetes Manifests — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 44 |
| [`kubernetes-meta-pe`](../../system-design/kubernetes-meta-pe/) | Kubernetes Meta Pe | Kubernetes Meta Pe — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 75 |
| [`kubernetes-operator-system`](../../system-design/kubernetes-operator-system/) | Kubernetes Operator System | Kubernetes Operator System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 153 |
| [`kubernetes-services`](../../system-design/kubernetes-services/) | Kubernetes Services | Kubernetes Services — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 29 |
| [`kubernetes_tls_bootstrap`](../../system-design/kubernetes_tls_bootstrap/) | Kubernetes Tls Bootstrap | Kubernetes Tls Bootstrap — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`kubetools`](../../system-design/kubetools/) | Kubetools | Kubetools — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 53 |
| [`kubetools-automation`](../../system-design/kubetools-automation/) | Kubetools Automation | Kubetools Automation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`kubetools-cli`](../../system-design/kubetools-cli/) | Kubetools Cli | Kubetools Cli — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 149 |
| [`kubetools-go`](../../system-design/kubetools-go/) | Kubetools Go | Kubetools Go — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 324 |
| [`kubetools-portal`](../../system-design/kubetools-portal/) | Kubetools Portal | Kubetools Portal — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 214 |
| [`kubetools_scraper`](../../system-design/kubetools_scraper/) | Kubetools Scraper | Kubetools Scraper — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`metrics`](../../system-design/metrics/) | Metrics | Metrics — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`metrics-monitoring-hello-interview`](../../system-design/metrics-monitoring-hello-interview/) | Metrics Monitoring Platform (Datadog-like) - Hello Interview Guide |  | ✓ ✓ ✓ ✓ ✓ | 38 |
| [`metro-build-system`](../../system-design/metro-build-system/) | Metro Build System | System design documentation and implementation for Metro Build System. | ✓ ✓ ✓ ✓ ✓ | 266 |
| [`monitor`](../../system-design/monitor/) | Monitor — Monitoring System Interview Mirror | Alias mirror for the monitoring-system interview package in monitor/ — architecture, trade-offs, and operational scaling. | ✓ ✓ ✓ ✓ ✓ | 35 |
| [`monitoring`](../../system-design/monitoring/) | Monitoring | Monitoring system for 1000 web servers — architecture, trade-offs, and operational scaling. | ✓ ✓ ✓ ✓ ✓ | 101 |
| [`monitoring-system`](../../system-design/monitoring-system/) | Monitoring System | Monitoring system for 1000 web servers — architecture, trade-offs, and operational scaling. | ✓ ✓ ✓ ✓ ✓ | 515 |
| [`monitoring-system-complete`](../../system-design/monitoring-system-complete/) | Monitoring System Complete | Monitoring system for 1000 web servers — architecture, trade-offs, and operational scaling. | ✓ ✓ ✓ ✓ ✓ | 172 |
| [`monitoring_system`](../../system-design/monitoring_system/) | Monitoring System | Monitoring system for 1000 web servers — architecture, trade-offs, and operational scaling. | ✓ ✓ ✓ ✓ ✓ | 483 |
| [`moon-machine-upgrade`](../../system-design/moon-machine-upgrade/) | Moon machine fleet upgrade (remote edge deploy) |  | ✓ · ✓ · ✓ | 30 |
| [`observability`](../../system-design/observability/) | Observability & monitoring — system design hub | Telemetry (metrics, logs, traces), SLOs, alerting, and operations as first-class design concerns—how teams know a distributed system is healthy, why it broke, a | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`pingdom`](../../system-design/pingdom/) | Pingdom | Design a SaaS website monitoring platform combining synthetic monitoring (uptime, page speed, transaction flows), Real User Monitoring (RUM), and a global alert | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`rbac`](../../system-design/rbac/) | Rbac | Rbac — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`scalable-session-management`](../../system-design/scalable-session-management/) | Scalable Session Management | Scalable Session Management — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 148 |
| [`scheduling`](../../system-design/scheduling/) | Scheduling | Scheduling — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 53 |
| [`security`](../../system-design/security/) | Web Application Security — System Design Hub | Design a web application security system covering XSS/SQLi/CSRF prevention, WAF, vulnerability scanning, and defense-in-depth — aligned with OWASP Top 10 and Ch | ✓ ✓ ✓ ✓ ✓ | 132 |
| [`server-side-monitoring`](../../system-design/server-side-monitoring/) | Server Side Monitoring | Server Side Monitoring — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`server-side-monitoring-educative-tests`](../../system-design/server-side-monitoring-educative-tests/) | Server Side Monitoring | Server Side Monitoring — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`service-debugging-lab`](../../system-design/service-debugging-lab/) | Service Debugging Lab | Service Debugging Lab — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 121 |
| [`session-management-system`](../../system-design/session-management-system/) | Session Management System | Session Management System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 120 |
| [`session-management-system-v2`](../../system-design/session-management-system-v2/) | Session Management System V2 | Session Management System V2 — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 89 |
| [`storage`](../../system-design/storage/) | Storage work server (Nitro-class local NVMe) |  | ✓ ✓ ✓ ✓ ✓ | 70 |
| [`superedge_tunnel`](../../system-design/superedge_tunnel/) | Superedge Tunnel | Superedge Tunnel — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 356 |
| [`task-scheduler`](../../system-design/task-scheduler/) | Task Scheduler | Task Scheduler — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 5181 |
| [`tengine-load-balancer`](../../system-design/tengine-load-balancer/) | Tengine Load Balancer | Tengine Load Balancer — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`terraform-infrastructure`](../../system-design/terraform-infrastructure/) | Terraform Infrastructure | Terraform Infrastructure — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`upgrade`](../../system-design/upgrade/) | Remote fleet upgrade (Moon / disconnected edge) — System design hub | Earth-controlled rollouts to hundreds of thousands of machines across a high-latency, bandwidth-constrained link — interview framing often uses the Moon; the sa | ✓ ✓ ✓ ✓ ✓ | 30 |
| [`viaduct`](../../system-design/viaduct/) | Viaduct | Viaduct — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 179 |
| [`vm-communication`](../../system-design/vm-communication/) | Vm Communication | Vm Communication — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 419 |
| [`web-applications`](../../system-design/web-applications/) | Web Applications | Web Applications — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |

## AI / ML 系统 / AI & ML systems（95）

> RAG/LLM 服务/推荐/排序/Agent 编排/训练推理/评测

| 目录 | 标题 | 一句话 | 文档 | 文件数 |
|---|---|---|---|---|
| [`ace-causal-inference`](../../system-design/ace-causal-inference/) | Ace Causal Inference | Ace Causal Inference — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 215 |
| [`ace_causal_inference`](../../system-design/ace_causal_inference/) | Ace Causal Inference | Ace Causal Inference — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 43 |
| [`ad-click-aggregator`](../../system-design/ad-click-aggregator/) | Ad Click Aggregator | Ad Click Aggregator — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 205 |
| [`ad-click-prediction`](../../system-design/ad-click-prediction/) | Ad Click Prediction | Ad Click Prediction — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 51 |
| [`ad-recommendation`](../../system-design/ad-recommendation/) | Ad Recommendation | Ad Recommendation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`adclick`](../../system-design/adclick/) | Adclick | Adclick — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`adclicker`](../../system-design/adclicker/) | Adclicker | Adclicker — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`ads-click-aggregator`](../../system-design/ads-click-aggregator/) | Ads Click Aggregator | Ads Click Aggregator — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 91 |
| [`ads-recommendation`](../../system-design/ads-recommendation/) | Ads Recommendation | Ads Recommendation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 125 |
| [`ads-recommendation-ml-educative-tests`](../../system-design/ads-recommendation-ml-educative-tests/) | Ads Recommendation Ml | Ads Recommendation Ml — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`ads-recommendation-system`](../../system-design/ads-recommendation-system/) | Ads Recommendation System | Ads Recommendation System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 50 |
| [`adtech_platform`](../../system-design/adtech_platform/) | Adtech Platform | Adtech Platform — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 460 |
| [`agent-orchestration`](../../system-design/agent-orchestration/) | Agent Orchestration | Agent Orchestration — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 264 |
| [`agentic-orchestration`](../../system-design/agentic-orchestration/) | Agentic Orchestration | Agentic Orchestration — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 132 |
| [`agentic-orchestration-system`](../../system-design/agentic-orchestration-system/) | Agentic Orchestration System | Agentic Orchestration System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 108 |
| [`agentic-system-design`](../../system-design/agentic-system-design/) | Agentic | Comprehensive system design documentation for Agentic. | ✓ ✓ ✓ ✓ ✓ | 102 |
| [`ai-agent`](../../system-design/ai-agent/) | Ai Agent | Ai Agent — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`ai-bootstrap`](../../system-design/ai-bootstrap/) | Ai Bootstrap | Ai Bootstrap — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 542 |
| [`ai-hospital-system`](../../system-design/ai-hospital-system/) | Ai Hospital System | Ai Hospital System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 193 |
| [`ai-ml-data-infrastructure`](../../system-design/ai-ml-data-infrastructure/) | Ai Ml Data Infrastructure | Ai Ml Data Infrastructure — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 381 |
| [`ai-model-switcher`](../../system-design/ai-model-switcher/) | Ai Model Switcher | Ai Model Switcher — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 125 |
| [`ai-network-traffic-classifier`](../../system-design/ai-network-traffic-classifier/) | Ai Network Traffic Classifier | Ai Network Traffic Classifier — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 147 |
| [`ai-system-design`](../../system-design/ai-system-design/) | AI system design | Inference, RAG, vector DB, eval, safety, cost, multi-tenant—at system design depth, not model-math tutorials. | ✓ · · · · | 25 |
| [`ai-traffic-classifier`](../../system-design/ai-traffic-classifier/) | Ai Traffic Classifier | Ai Traffic Classifier — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 333 |
| [`amazon-book-reviews-recommendations`](../../system-design/amazon-book-reviews-recommendations/) | Amazon book reviews ingestion + on-site recommendations — System design hub | Ingest book reviews (prompt: Amazon.com framing) under compliant data access, index for search, and serve recommendations on your website. | ✓ ✓ ✓ ✓ ✓ | 34 |
| [`care_finder`](../../system-design/care_finder/) | Care Finder | Care Finder — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 1955 |
| [`chatgpt`](../../system-design/chatgpt/) | Chatgpt | Chatgpt — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 972 |
| [`chatgpt-system`](../../system-design/chatgpt-system/) | Chatgpt System | Chatgpt System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 778 |
| [`chatgpt-system-design`](../../system-design/chatgpt-system-design/) | Chatgpt | Comprehensive system design documentation for Chatgpt. | ✓ ✓ ✓ ✓ ✓ | 357 |
| [`chatpgt-system-design`](../../system-design/chatpgt-system-design/) | Chatpgt | Comprehensive system design documentation for Chatpgt. | ✓ ✓ ✓ ✓ ✓ | 130 |
| [`claude-skills`](../../system-design/claude-skills/) | Claude Skills | Claude Skills — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`code-agent`](../../system-design/code-agent/) | Code Agent | Code Agent — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 169 |
| [`distributed-genai-training`](../../system-design/distributed-genai-training/) | Distributed Genai Training | System design documentation and implementation for Distributed Genai Training. | ✓ ✓ ✓ ✓ ✓ | 84 |
| [`document-retrieval`](../../system-design/document-retrieval/) | Document Retrieval | Document Retrieval — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 195 |
| [`document-retrieval-prototype`](../../system-design/document-retrieval-prototype/) | Document Retrieval Prototype | Document Retrieval Prototype — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 258 |
| [`ecommerce-recommendation-hub`](../../system-design/ecommerce-recommendation-hub/) | E-commerce Recommendation System — Interview hub index | Design a recommendation system for an e-commerce platform (candidate generation, ranking, real-time updates, experimentation, and operations). | ✓ · · · · | 26 |
| [`embedding-retrieval`](../../system-design/embedding-retrieval/) | Embedding Retrieval | Embedding Retrieval — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 162 |
| [`eureka-reward-design`](../../system-design/eureka-reward-design/) | Eureka Reward Design | Eureka Reward Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 178 |
| [`feed-ranking`](../../system-design/feed-ranking/) | Feed Ranking | Feed Ranking — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 228 |
| [`food-ranking-system`](../../system-design/food-ranking-system/) | Food Ranking System | Food Ranking System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 1886 |
| [`genai-evaluation`](../../system-design/genai-evaluation/) | Genai Evaluation | Genai Evaluation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 192 |
| [`genai-evaluation-platform`](../../system-design/genai-evaluation-platform/) | Genai Evaluation Platform | Genai Evaluation Platform — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 108 |
| [`genai-key-concepts`](../../system-design/genai-key-concepts/) | Genai Key Concepts | Genai Key Concepts — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 109 |
| [`genai-parallelism`](../../system-design/genai-parallelism/) | Genai Parallelism | Genai Parallelism — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 192 |
| [`genai-resource-estimation`](../../system-design/genai-resource-estimation/) | Genai Resource Estimation | Genai Resource Estimation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 175 |
| [`genai-system-design`](../../system-design/genai-system-design/) | Genai | Comprehensive system design documentation for Genai. | ✓ ✓ ✓ ✓ ✓ | 139 |
| [`graph-ml`](../../system-design/graph-ml/) | Graph Ml | Graph Ml — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 162 |
| [`graph-social-recommender`](../../system-design/graph-social-recommender/) | Graph Social Recommender | Graph Social Recommender — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 171 |
| [`hello-agents`](../../system-design/hello-agents/) | Hello Agents | Hello Agents — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 149 |
| [`human-loop-ml`](../../system-design/human-loop-ml/) | Human Loop Ml | Human Loop Ml — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 136 |
| [`image-captioning`](../../system-design/image-captioning/) | Image Captioning | Image Captioning — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 80 |
| [`image-captioning-blip2`](../../system-design/image-captioning-blip2/) | Image Captioning Blip2 | Image Captioning Blip2 — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 82 |
| [`image-captioning-deployment`](../../system-design/image-captioning-deployment/) | Image Captioning Deployment | Image Captioning Deployment — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 80 |
| [`image-captioning-system`](../../system-design/image-captioning-system/) | Image Captioning System | Image Captioning System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 108 |
| [`inference-optimization`](../../system-design/inference-optimization/) | Inference Optimization | Inference Optimization — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 108 |
| [`interleaving-experiments`](../../system-design/interleaving-experiments/) | Interleaving Experiments | Interleaving Experiments — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 214 |
| [`job-recommendation-system`](../../system-design/job-recommendation-system/) | Job Recommendation System | Job Recommendation System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 307 |
| [`job-recommender-system`](../../system-design/job-recommender-system/) | Job Recommender System | Job Recommender System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 129 |
| [`lending_product`](../../system-design/lending_product/) | Lending Product | Lending Product — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 446 |
| [`linkedin-feed-ranking`](../../system-design/linkedin-feed-ranking/) | Social Feed / News Feed | Social Feed / News Feed — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 106 |
| [`llm-customer-support-bot`](../../system-design/llm-customer-support-bot/) | LLM-Powered Customer Support Bot — System Design Hub | Design an LLM-powered customer support bot with RAG-based response generation, multi-turn dialogue management, function calling for backend operations, human es | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`llm-interview-prep`](../../system-design/llm-interview-prep/) | Llm Interview Prep | Llm Interview Prep — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 39 |
| [`llm-vlm-agent-rag-system`](../../system-design/llm-vlm-agent-rag-system/) | Llm Vlm Agent Rag System | Llm Vlm Agent Rag System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 157 |
| [`llmops-evaluation-suite`](../../system-design/llmops-evaluation-suite/) | Llmops Evaluation Suite | Llmops Evaluation Suite — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 108 |
| [`ml-design-principles`](../../system-design/ml-design-principles/) | Ml Design Principles | Ml Design Principles — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 114 |
| [`ml-system`](../../system-design/ml-system/) | Ml System | Ml System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 184 |
| [`ml-systems-design`](../../system-design/ml-systems-design/) | Ml Systems Design | Ml Systems Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 1101 |
| [`molmo-system`](../../system-design/molmo-system/) | Molmo System | Molmo System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`mulan-agentic-image-generation`](../../system-design/mulan-agentic-image-generation/) | Mulan Agentic Image Generation | Mulan Agentic Image Generation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 64 |
| [`music-listening-analytics`](../../system-design/music-listening-analytics/) | Music listening history (30s threshold) — analytics system | Design an app that records listening history for analytics only after the user has played a song for more than 30 seconds. Typical Amazon TPM / system-design fr | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`network-traffic-classifier`](../../system-design/network-traffic-classifier/) | Network Traffic Classifier | Network Traffic Classifier — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 108 |
| [`parallelism-genai`](../../system-design/parallelism-genai/) | Parallelism Genai | Parallelism Genai — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 180 |
| [`RAG`](../../system-design/RAG/) | Rag | Rag — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 165 |
| [`rag`](../../system-design/rag/) | Rag | Rag — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 69 |
| [`rag-context-engineering-tests`](../../system-design/rag-context-engineering-tests/) | Rag Context Engineering | Rag Context Engineering — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`rag-document-chunking-tests`](../../system-design/rag-document-chunking-tests/) | Rag Document Chunking | Rag Document Chunking — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`rag-finetuning`](../../system-design/rag-finetuning/) | Rag Finetuning | Rag Finetuning — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 282 |
| [`rag-retrieval-platform`](../../system-design/rag-retrieval-platform/) | Rag Retrieval Platform | Rag Retrieval Platform — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 298 |
| [`rag-system`](../../system-design/rag-system/) | Rag System | Rag System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 1011 |
| [`recommendation`](../../system-design/recommendation/) | Recommendation system — Interview hub | Large-scale recommendation (e-commerce / feed surfaces): retrieval, ranking, features, training loop, and production SLOs. | ✓ ✓ ✓ ✓ ✓ | 167 |
| [`rental-search-ranking`](../../system-design/rental-search-ranking/) | Rental Search Ranking | Rental Search Ranking — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 218 |
| [`rental-search-ranking-system`](../../system-design/rental-search-ranking-system/) | Rental Search Ranking System | Rental Search Ranking System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 49 |
| [`review-abuse`](../../system-design/review-abuse/) | Detecting and Preventing Review Abuse | Design a system to detect and prevent review abuse on a marketplace platform (DoorDash, Yelp, Amazon). Fake reviews, review bombing, incentivized reviews, and c | ✓ · · · · | 24 |
| [`social-recommendation`](../../system-design/social-recommendation/) | Social Recommendation | Social Recommendation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 237 |
| [`social-recommender`](../../system-design/social-recommender/) | Social Recommender | Social Recommender — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 181 |
| [`spotify-wrapped-system`](../../system-design/spotify-wrapped-system/) | Spotify Wrapped System | Spotify Wrapped System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 32 |
| [`text-to-image-gen`](../../system-design/text-to-image-gen/) | Text To Image Gen | Text To Image Gen — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 93 |
| [`text-to-image-generation`](../../system-design/text-to-image-generation/) | Text To Image Generation | Text To Image Generation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 124 |
| [`text-to-speech-gen`](../../system-design/text-to-speech-gen/) | Text To Speech Gen | Text To Speech Gen — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 107 |
| [`text-to-text-generation`](../../system-design/text-to-text-generation/) | Text To Text Generation | Text To Text Generation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 173 |
| [`text-to-video-gen`](../../system-design/text-to-video-gen/) | GenAI / LLM System Design | GenAI / LLM System Design — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 149 |
| [`tiny-a2a`](../../system-design/tiny-a2a/) | Tiny A2A | Tiny A2A — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 430 |
| [`trigger_detection`](../../system-design/trigger_detection/) | Trigger Detection | Trigger Detection — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 146 |
| [`vectordb`](../../system-design/vectordb/) | Vectordb | Vectordb — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`video-recommendation`](../../system-design/video-recommendation/) | Video Recommendation | Video Recommendation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 123 |

## 操作系统与系统编程 / OS & systems programming（28）

> 启动/内存/进程/同步/IPC/磁盘/Socket/文件系统

| 目录 | 标题 | 一句话 | 文档 | 文件数 |
|---|---|---|---|---|
| [`boot_process`](../../system-design/boot_process/) | Boot Process | Boot Process — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 53 |
| [`computer-boot-process`](../../system-design/computer-boot-process/) | Linux / Operating System Internals | Linux / Operating System Internals — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 34 |
| [`context_switching`](../../system-design/context_switching/) | Context Switching | Context Switching — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 53 |
| [`deadlock`](../../system-design/deadlock/) | Deadlock | Deadlock — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 53 |
| [`disk-scheduling-simulator`](../../system-design/disk-scheduling-simulator/) | Disk Scheduling Simulator | Disk Scheduling Simulator — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 104 |
| [`disk-sort-toolkit`](../../system-design/disk-sort-toolkit/) | Disk Sort Toolkit | Disk Sort Toolkit — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 36 |
| [`disk_scheduling`](../../system-design/disk_scheduling/) | Disk Scheduling | Disk Scheduling — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 53 |
| [`disk_scheduling_simulator`](../../system-design/disk_scheduling_simulator/) | Disk Scheduling Simulator | Disk Scheduling Simulator — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 106 |
| [`ipc`](../../system-design/ipc/) | Ipc | Ipc — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 59 |
| [`kernel-distribution`](../../system-design/kernel-distribution/) | Kernel Distribution System | Design a system to build, test, sign, and distribute custom Linux kernels to 10,000+ VMs across datacenter and cloud environments with minimal downtime. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`linux`](../../system-design/linux/) | Linux | Linux — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 108 |
| [`linux-boot-process`](../../system-design/linux-boot-process/) | Linux Boot Process | Linux Boot Process — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 50 |
| [`linux-fundamentals`](../../system-design/linux-fundamentals/) | Linux Fundamentals | Linux Fundamentals — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 322 |
| [`linux-memory-exhaustion`](../../system-design/linux-memory-exhaustion/) | Linux Memory Exhaustion | Linux Memory Exhaustion — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 59 |
| [`linux-network-stack`](../../system-design/linux-network-stack/) | Linux Network Stack | Linux Network Stack — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 179 |
| [`linux-opensource-projects-interview-hub`](../../system-design/linux-opensource-projects-interview-hub/) | Linux Opensource Projects Interview Hub |  | · · · · · | 22 |
| [`linux-system-admin`](../../system-design/linux-system-admin/) | Linux System Admin | Linux System Admin — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 60 |
| [`linux_storage_stack`](../../system-design/linux_storage_stack/) | Linux Storage Stack | Linux Storage Stack — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 182 |
| [`memory_management`](../../system-design/memory_management/) | Memory Management | Memory Management — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 193 |
| [`networking-fundamentals`](../../system-design/networking-fundamentals/) | Networking Fundamentals | Networking Fundamentals — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`operating-system-design`](../../system-design/operating-system-design/) | Operating | Comprehensive system design documentation for Operating. | ✓ ✓ ✓ ✓ ✓ | 54 |
| [`os-linux`](../../system-design/os-linux/) | Networking fundamentals — HTTP/S, TCP/IP, OSI (interview hub) | L3/L4/L7 basics for SRE, backend, and Linux interviews—HTTP vs HTTPS, ports, TLS handshake, OSI, addressing, NAT, routing. Original Q&A; not a paste of any sing | ✓ · · · · | 26 |
| [`process_management`](../../system-design/process_management/) | Process Management | Process Management — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 57 |
| [`socket-programming-examples`](../../system-design/socket-programming-examples/) | Socket Programming Examples | Socket Programming Examples — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`socket-programming-linux`](../../system-design/socket-programming-linux/) | Socket Programming Linux | Socket Programming Linux — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 69 |
| [`socket_programming_linux`](../../system-design/socket_programming_linux/) | Socket Programming Linux | Socket Programming Linux — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 65 |
| [`synchronization`](../../system-design/synchronization/) | Synchronization | Synchronization — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 56 |
| [`unix_file_system`](../../system-design/unix_file_system/) | Unix File System | Unix File System — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 112 |

## 面试合集与公司专项 / Interview hubs & company tracks（52）

> Meta PE/编码题/行为题/专项练习

| 目录 | 标题 | 一句话 | 文档 | 文件数 |
|---|---|---|---|---|
| [`AI-interviews`](../../system-design/AI-interviews/) | Ai Interviews | Ai Interviews — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`algorithms`](../../system-design/algorithms/) | Algorithms | Algorithms — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`ansible-exercises-complete`](../../system-design/ansible-exercises-complete/) | Ansible Exercises Complete | Ansible Exercises Complete — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 290 |
| [`blind-75-leetcode`](../../system-design/blind-75-leetcode/) | Blind 75 Leetcode | Blind 75 Leetcode — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 296 |
| [`bq`](../../system-design/bq/) | BQ hub — behavioral, TPM, incident metrics & typeahead (01–20) |  | ✓ · · · · | 3405 |
| [`code-implementations`](../../system-design/code-implementations/) | Code Implementations | Code Implementations — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 154 |
| [`coding-interview-prep`](../../system-design/coding-interview-prep/) | Coding Interview Prep | Coding Interview Prep — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`coding-interview-university`](../../system-design/coding-interview-university/) | Coding Interview University | Coding Interview University — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 311 |
| [`cpp-interview-prep`](../../system-design/cpp-interview-prep/) | Cpp Interview Prep | Cpp Interview Prep — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 290 |
| [`cpp-oop-interview`](../../system-design/cpp-oop-interview/) | Cpp Oop | Cpp Oop — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 119 |
| [`design-leetcode`](../../system-design/design-leetcode/) | Design Leetcode | Design Leetcode — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 59 |
| [`devinterview-automation`](../../system-design/devinterview-automation/) | Devinterview Automation | Devinterview Automation — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 1169 |
| [`devinterview-database`](../../system-design/devinterview-database/) | Devinterview Database | Devinterview Database — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 39 |
| [`devops`](../../system-design/devops/) | Devops | Devops — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 48 |
| [`devops-exercises`](../../system-design/devops-exercises/) | Devops Exercises | Devops Exercises — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 811 |
| [`devops-sre-coding-prep`](../../system-design/devops-sre-coding-prep/) | Devops Sre Coding Prep | Devops Sre Coding Prep — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 28 |
| [`devops-sre-interview-prep`](../../system-design/devops-sre-interview-prep/) | Devops Sre Interview Prep | Devops Sre Interview Prep — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`devops-sre-meta-pe`](../../system-design/devops-sre-meta-pe/) | Devops Sre Meta Pe | Devops Sre Meta Pe — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`go-exercises`](../../system-design/go-exercises/) | Go Exercises | Go Exercises — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 414 |
| [`go-exercises-solutions`](../../system-design/go-exercises-solutions/) | Go Exercises Solutions | Go Exercises Solutions — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`golang`](../../system-design/golang/) | Golang | Golang — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 50 |
| [`google_sre`](../../system-design/google_sre/) | Google Sre | Google Sre — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`interview-experiences-page`](../../system-design/interview-experiences-page/) | Interview Experiences Page | Interview Experiences Page — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 82 |
| [`interview-prep`](../../system-design/interview-prep/) | Interview Prep | Interview Prep — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 841 |
| [`interview-prep-systems`](../../system-design/interview-prep-systems/) | Interview Prep Systems | Interview Prep Systems — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 357 |
| [`java-algorithms`](../../system-design/java-algorithms/) | Java Algorithms | Java Algorithms — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 185 |
| [`java-assessment`](../../system-design/java-assessment/) | Java Assessment | Java Assessment — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 210 |
| [`java-integration-tests`](../../system-design/java-integration-tests/) | Java Integration | Java Integration — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 325 |
| [`kubernetes-exercises`](../../system-design/kubernetes-exercises/) | Kubernetes Exercises | Kubernetes Exercises — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 147 |
| [`kubernetes-interview`](../../system-design/kubernetes-interview/) | Kubernetes | Kubernetes — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 55 |
| [`kubernetes-interview-prep`](../../system-design/kubernetes-interview-prep/) | Kubernetes Interview Prep | Kubernetes Interview Prep — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`leetcode`](../../system-design/leetcode/) | Leetcode | Leetcode — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 350 |
| [`leetcode-online-judge`](../../system-design/leetcode-online-judge/) | Leetcode Online Judge | Leetcode Online Judge — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 305 |
| [`leetcode-patterns`](../../system-design/leetcode-patterns/) | Leetcode Patterns | Leetcode Patterns — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 379 |
| [`leetcode-system-design`](../../system-design/leetcode-system-design/) | LeetCode | Comprehensive system design documentation for LeetCode. | ✓ ✓ ✓ ✓ ✓ | 306 |
| [`linux-commands-interview-hub`](../../system-design/linux-commands-interview-hub/) | Linux Commands — Interview Hub (Newbie → SysAdmin) |  | ✓ · · · · | 49 |
| [`meta-coding-advanced`](../../system-design/meta-coding-advanced/) | Meta Coding Advanced | Meta Coding Advanced — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 90 |
| [`meta-infra-interview`](../../system-design/meta-infra-interview/) | Meta Infra | Meta Infra — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 85 |
| [`meta-interview`](../../system-design/meta-interview/) | Meta | Meta — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 1078 |
| [`meta-interview-coding`](../../system-design/meta-interview-coding/) | Meta Interview Coding | Meta Interview Coding — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 84 |
| [`meta-interview-questions`](../../system-design/meta-interview-questions/) | Meta Interview Questions | Meta Interview Questions — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 87 |
| [`meta-ml-interview`](../../system-design/meta-ml-interview/) | Meta Ml | Meta Ml — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 45 |
| [`meta-pe-interview`](../../system-design/meta-pe-interview/) | Meta Pe | Meta Pe — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 35 |
| [`meta_pe_interview`](../../system-design/meta_pe_interview/) | Meta Pe Interview | Meta Pe Interview — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 327 |
| [`resume-designs`](../../system-design/resume-designs/) | Resume Designs | Resume Designs — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`resume_replay`](../../system-design/resume_replay/) | Resume Replay | Resume Replay — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 146 |
| [`security-interview-comprehensive`](../../system-design/security-interview-comprehensive/) | Security Interview — Comprehensive Guide (redirect) |  | ✓ · · · · | 34 |
| [`sql-interview-prep`](../../system-design/sql-interview-prep/) | Sql Interview Prep | Sql Interview Prep — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 30 |
| [`study_guides`](../../system-design/study_guides/) | Study Guides | Study Guides — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 29 |
| [`technical-assessments`](../../system-design/technical-assessments/) | Technical Assessments | Technical Assessments — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 294 |
| [`terraform-exercises`](../../system-design/terraform-exercises/) | Terraform Exercises | Terraform Exercises — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 202 |
| [`web-security-interview`](../../system-design/web-security-interview/) | Web Security Interview — 春招面试题深度解析 | Web安全面试核心知识体系 — XSS、SQL注入、CSRF、同源策略、渗透测试、扫描器设计、提权、代码审计，覆盖阿里/百度/360等一线互联网企业春招真题。 | ✓ ✓ ✓ ✓ ✓ | 35 |

## 工程脚手架 / 泛化别名（非出题主题） / Engineering scaffolding & generic aliases (not asked)（33）

> 代码/配置目录或仅含模板化 00–21 文档的泛化别名，仅为覆盖完整性列出；候选人点名时仍可按目录内文档作答

| 目录 | 标题 | 一句话 | 文档 | 文件数 |
|---|---|---|---|---|
| [`beautifulMention`](../../system-design/beautifulMention/) | Beautifulmention | Beautifulmention — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 96 |
| [`cmd`](../../system-design/cmd/) | Cmd | Cmd — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 50 |
| [`common`](../../system-design/common/) | Common | Common — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 369 |
| [`config`](../../system-design/config/) | Config | Config — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 242 |
| [`cpp`](../../system-design/cpp/) | Cpp |  | · · · · · | 10 |
| [`delivery`](../../system-design/delivery/) | Delivery | Delivery — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`docs`](../../system-design/docs/) | docs（仓库级文档 + 二级专题枢纽，见文末） | Repository-level docs; topic hubs are listed in the docs/ section below. | ✓ ✓ ✓ ✓ ✓ | 392 |
| [`examples`](../../system-design/examples/) | Examples | Examples — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 27 |
| [`go`](../../system-design/go/) | Go |  | · · · · · | 7 |
| [`internal`](../../system-design/internal/) | Internal | Internal — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 268 |
| [`localservice`](../../system-design/localservice/) | Localservice | Localservice — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`logs`](../../system-design/logs/) | Logs | Logs — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`maps`](../../system-design/maps/) | Maps | Maps — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`memory`](../../system-design/memory/) | Memory | Memory — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 53 |
| [`pages`](../../system-design/pages/) | Pages | Pages — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 52 |
| [`pela`](../../system-design/pela/) | Pela | Pela — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 120 |
| [`pkg`](../../system-design/pkg/) | Pkg | Pkg — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 76 |
| [`playwright-report`](../../system-design/playwright-report/) | Playwright Report | Playwright Report — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`prisma`](../../system-design/prisma/) | Prisma | Prisma — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`public`](../../system-design/public/) | Public | Public — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`references`](../../system-design/references/) | References |  | · · · · · | 1 |
| [`rust`](../../system-design/rust/) | Rust |  | · · · · · | 9 |
| [`scripts`](../../system-design/scripts/) | Scripts | Scripts — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 82 |
| [`services`](../../system-design/services/) | Services | Services — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 625 |
| [`skills`](../../system-design/skills/) | Skills | Skills — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 34 |
| [`src`](../../system-design/src/) | Src | Src — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 218 |
| [`styles`](../../system-design/styles/) | Styles | Styles — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`templates`](../../system-design/templates/) | Templates | Templates — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 87 |
| [`tests`](../../system-design/tests/) | Tests | Tests — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 551 |
| [`tests_generated`](../../system-design/tests_generated/) | Tests Generated | Tests Generated — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 1300 |
| [`timetravel`](../../system-design/timetravel/) | Timetravel | Timetravel — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 24 |
| [`vanilla-router`](../../system-design/vanilla-router/) | Vanilla Router | Vanilla Router — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 192 |
| [`zones`](../../system-design/zones/) | Zones | Zones — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 29 |

## `docs/` 二级专题枢纽 / Second-layer hubs（13）

> `system-design/docs/<hub>/` 下的跨主题综述（架构 / 数据库 / 分布式 / 基础设施 / Linux / 网络 / 服务网格 / 存储……）。

| 目录 | 标题 | 一句话 | 文档 | 文件数 |
|---|---|---|---|---|
| [`docs/architecture`](../../system-design/docs/architecture/) | Architecture | Architecture — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 32 |
| [`docs/databases`](../../system-design/docs/databases/) | Databases | Databases — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`docs/distributed-systems`](../../system-design/docs/distributed-systems/) | Distributed Systems | Distributed Systems — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`docs/hello-interview`](../../system-design/docs/hello-interview/) | Job Scheduler — Hello Interview Index |  | ✓ · · · · | 13 |
| [`docs/infrastructure`](../../system-design/docs/infrastructure/) | Infrastructure | Infrastructure — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 31 |
| [`docs/interview-guides`](../../system-design/docs/interview-guides/) | Interview Guides | Interview Guides — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`docs/linux`](../../system-design/docs/linux/) | Linux | Linux — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`docs/networking`](../../system-design/docs/networking/) | Networking | Networking — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`docs/programming`](../../system-design/docs/programming/) | Programming | Programming — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`docs/repository-top-level-matrix-hub`](../../system-design/docs/repository-top-level-matrix-hub/) | Repository top-level matrix hub | Navigate the system-design monorepo by a matrix (rows = top-level folders, columns = signals). Includes a ~1 h spoken transcript and a generator for a machine-c | ✓ · · · · | 25 |
| [`docs/service-mesh`](../../system-design/docs/service-mesh/) | Service Mesh | Service Mesh — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 25 |
| [`docs/storage`](../../system-design/docs/storage/) | Storage | Storage — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |
| [`docs/technical-assessments`](../../system-design/docs/technical-assessments/) | Technical Assessments | Technical Assessments — architecture, trade-offs, and scaling considerations. | ✓ ✓ ✓ ✓ ✓ | 26 |

