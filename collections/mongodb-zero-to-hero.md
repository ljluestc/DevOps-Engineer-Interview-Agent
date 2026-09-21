# MongoDB 面试题 — 从 MongoDB-Zero-to-Hero 教程提炼（68 题）

> **来源**：[iam-veeramalla/MongoDB-Zero-to-Hero](https://github.com/iam-veeramalla/MongoDB-Zero-to-Hero)（Apache-2.0，含 YouTube 全程课）。
> **收录日期**：2026-09-20
> **说明**：原仓库是一套 6 章的零基础教程（Introduction → Building Blocks → Atlas & Compass → CRUD →
> DevOps Log Explorer 实战 → MongoDB for AI Apps），本身**没有题目**。本文件把 6 章里的每一个知识点都改写成
> 面试题，分组沿用原教程章节顺序，并在每题下附「要点」——要点只提炼自原教程与 MongoDB 官方文档，不含
> 二次来源。☆ = 高频题（面试真实常问）。🟢/🟡/🔴 见难度图例。
> **与其他收录的关系**：`ops-question-bank-1502.md` OTHER 专题第 40–43 题、崔亮中级篇第 4 题已有 4–5 道 MongoDB
> 运维题（备份 / 分片 / 定位），本文件从「概念 → CRUD → 日志场景 → 向量检索」补齐基础与应用层，运维深水区
> （副本集 / 分片 / 备份演练）请配合 `modules/middleware/middleware-questions.md` Q19–Q20 使用。

---

## 一、Introduction：关系型 vs 非关系型、为什么选 MongoDB（14 题）

1. ☆ 🟢 一句话说明 MongoDB 是什么？它属于哪一类数据库？
   - 要点：NoSQL / 非关系型（Non-Relational）**文档数据库**，以「文档（JSON-like）」而非「表」存数据；典型场景：Web / 移动后端、实时系统、日志与分析、AI 应用。
2. ☆ 🟢 关系型数据库（MySQL / PostgreSQL / Oracle）是怎么组织数据的？教程里指出了它的哪几个痛点？
   - 要点：表 / 行 / 列、**先定义 schema 再写数据**；痛点：大量 NULL 空列、改 schema 困难、要做 migration、不适合结构经常变化的数据。
3. ☆ 🟢 非关系型（文档型）数据库怎么组织同一份用户数据？相对 SQL 表的好处是什么？
   - 要点：一个用户就是一个 JSON-like 文档，`phones` 可直接是数组；好处：没有无用字段、数据长得像真实对象、改结构容易、更贴合真实世界数据。
4. 🟢 列出非关系型数据库的四个通用优势，以及它最适合的五类场景。
   - 要点：灵活数据模型、开发更快、**易于水平扩展**、擅长半结构化数据；场景：Web、移动、日志、分析、AI 工作负载。
5. ☆ 🟡 「MongoDB 在灵活性和控制之间取得平衡」——这句话怎么理解？举出教程给的关键理由。
   - 要点：文档像 JSON、**查询也像 JSON**、强大的索引、**可选的 schema 强制（Schema Validation）**、工具链好（Atlas / Compass）、面向现代与 AI 场景。哲学：**Start flexible, add rules when needed**。
6. ☆ 🟢 JSON 与 BSON 的区别是什么？MongoDB 内部用哪一种？
   - 要点：JSON 文本、可读、用于 API / 前端；**BSON = Binary JSON**，MongoDB 内部存储格式，读写更快、**带类型信息**、支持比 JSON 更多的数据类型。
7. 🟡 BSON 比 JSON 多出哪些数据类型？分别在什么场景用？
   - 要点：`ObjectId`（文档主键）、`Date`（真正的时间类型，可排序 / 范围查询）、`Decimal128`（金额等需要精确小数）、`Binary`（文件 / 二进制块）。
8. 🟡 为什么 JSON 里的 `499` 和 `true` 到了 BSON 里更有优势？「stores type information」对运维意味着什么？
   - 要点：BSON 明确记录 int / double / bool / date 等类型，避免字符串比较歧义；运维层面：类型不一致会导致查询「查不到」或索引失效，导入数据时要注意类型（如时间戳存成字符串）。
9. ☆ 🟡 什么是 Schema Validation？既然 MongoDB 是「无 schema」的，为什么还要它？
   - 要点：给集合定义 JSON Schema 规则（`bsonType` / `required` / `properties`），写入不合规文档会被拒绝；MongoDB 是「flexible」不是「schema-less chaos」，验证用来**防脏数据、保持数据干净、不需要重型 migration、可以随时加**。
10. 🟡 写出一个 Schema Validation 规则：要求文档为 object，`name` 与 `email` 必填且都是字符串。
    - 要点：`{ bsonType: "object", required: ["name","email"], properties: { name: { bsonType: "string" }, email: { bsonType: "string" } } }`；通过 `db.createCollection(name, { validator: { $jsonSchema: … } })` 或 `collMod` 挂到集合上。
11. 🔴 Schema Validation 是「best of both worlds」——它跟 SQL 的 DDL 约束比，好在哪、弱在哪？
    - 要点：好：可以晚绑定、按需逐步收紧、只校验新写入（可配 `validationLevel: moderate` 放过存量文档）、不需要停机 migration；弱：没有外键 / 跨集合约束，`validationAction: warn` 时只记日志不拦截，团队容易「忘了开」。
12. ☆ 🟡 什么是向量检索（Vector Search）？MongoDB 文档里的 `embedding` 字段是什么？
    - 要点：把文本 / 图片等经 embedding 模型变成一串浮点数（向量），存到文档字段里；Vector Search 按向量相似度（而非关键字）找「语义相近」的文档。
13. 🟡 向量检索能支持哪四类 AI 应用？
    - 要点：语义搜索、推荐系统、AI 聊天机器人（RAG 检索）、相似度搜索（以图搜图 / 相似商品）。
14. 🟡 用三句话总结教程第一章：关系型 vs 非关系型、MongoDB 的存储格式、MongoDB 为什么「AI-ready」。
    - 要点：关系型用固定表 / 非关系型用灵活文档；MongoDB 内部存 BSON、对外 JSON 语法；Schema Validation 保证数据安全 + Vector Search 让它能直接服务 AI 应用。

## 二、Building Blocks：数据库 / 集合 / 文档 / 字段 / _id / 索引（11 题）

15. ☆ 🟢 说出 MongoDB 的层级结构（从上到下），并与 SQL 的概念一一对应。
    - 要点：**Database → Collection → Document → Field**；Database ≈ 数据库、Collection ≈ 表、Document ≈ 行、Field ≈ 列；类比「文件夹 / 文件」，但为数据设计。
16. 🟢 Database 在 MongoDB 里是什么？举一个命名例子。
    - 要点：顶层容器，装多个集合，与 SQL 的 database 概念相同；例如 `ecommerce_db`。
17. 🟢 Collection 与 SQL 表最大的区别是什么？
    - 要点：都是「一组相关数据」，但集合**没有固定列**，同一集合内文档字段可以各不相同；例如 `users` / `orders` / `products`。
18. ☆ 🟢 为什么说 Document 是 MongoDB「最重要」的概念？它有什么特点？
    - 要点：文档 = 一条记录，JSON-like 存储，**每个文档可以有不同字段**，「不需要 NULL、只存你需要的」。
19. 🟢 Field 是什么？字段值可以是哪些形态？
    - 要点：文档内的键值对（≈ 列）；值可以是标量（`"age": 25`）、数组（`skills`）、嵌套文档（`address.city`）。
20. ☆ 🟢 `_id` 字段有什么特殊之处？
    - 要点：每个文档唯一标识；**不给就自动生成 `ObjectId`**；**默认自动建唯一索引**；集合内不可重复、创建后不可修改。
21. 🟡 `ObjectId` 是怎么构成的？它比自增 ID 好在哪？
    - 要点：12 字节：4 字节时间戳 + 5 字节随机（机器 / 进程）+ 3 字节计数器；无需中心发号器即可在分布式 / 分片环境生成全局唯一 ID，并且大致按时间有序。
22. 🟢 「你写 JSON，MongoDB 存 BSON」——在 Compass 里看到的 `ObjectId("65a1…")` 说明了什么？
    - 要点：Compass / mongosh 显示的是 Extended JSON 表示，底层是 BSON 的 ObjectId 类型，而不是普通字符串；查询时要用 `ObjectId("…")` 而不是裸字符串，否则匹配不到。
23. ☆ 🟢 什么是索引？MongoDB 默认有哪个索引？怎么给 `email` 建索引？
    - 要点：索引提升查询性能（避免全集合扫描）；`_id` 索引默认存在；`db.users.createIndex({ email: 1 })`（1 升序 / -1 降序）。
24. 🟡 给 `email` 建索引后，还应该考虑加什么选项？为什么？
    - 要点：`{ unique: true }` 防重复注册；索引带来写放大与内存占用，只给高频查询字段建；用 `explain()` 看是否命中（`IXSCAN` vs `COLLSCAN`）。
25. 🟢 教程说 MongoDB「beginner friendly」的四个理由是什么？
    - 要点：没有僵硬 schema、JSON-like 语法、容易扩展、贴合真实数据结构。

## 三、MongoDB Atlas 与 Compass（10 题）

26. ☆ 🟢 什么是 MongoDB Atlas？它替你省掉了哪些工作？
    - 要点：MongoDB 官方**全托管云数据库**；不用装 MongoDB、不用管服务器、**不用自己做备份和扩容**。
27. 🟢 Atlas 免费集群叫什么？创建时要选哪几项？
    - 要点：**M0（Free / Shared）**；选云厂商（默认 AWS 即可）、离你最近的 Region；1–3 分钟创建完成。
28. ☆ 🟢 连接 Atlas 之前必须做的两项安全配置是什么？
    - 要点：**Database Access**（创建数据库用户 + 密码，分配角色如 Read and write to any database）和 **Network Access**（IP 白名单）。
29. ☆ 🟡 教程让「Allow Access from Anywhere」并注明 only for learning——生产环境应该怎么做？
    - 要点：0.0.0.0/0 意味着只靠用户名密码防守；生产应限制到固定出口 IP / VPC Peering / Private Endpoint，用户按最小权限建（只读 / 单库），开审计与 TLS（Atlas 默认强制 TLS）。
30. 🟢 什么是 MongoDB Compass？它解决什么问题？
    - 要点：官方 GUI 客户端，可视化查看 / 编辑数据、建索引、看 explain 计划，对初学者比 mongosh 友好。
31. ☆ 🟡 解释这条连接串的每一部分：`mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/`
    - 要点：`mongodb+srv://` 表示通过 **DNS SRV 记录**自动发现副本集所有节点并默认启用 TLS；`<username>:<password>` 是 Database Access 里建的账号；`cluster0.xxxxx.mongodb.net` 是集群主机名；末尾 `/` 后可加默认库名和参数（如 `?retryWrites=true&w=majority`）。
32. 🟡 `mongodb://` 与 `mongodb+srv://` 的区别？
    - 要点：`mongodb://` 要显式列出 host:port（本地 `mongodb://localhost:27017`）；`+srv` 只写一个域名、由 DNS TXT / SRV 记录下发节点列表和连接参数，节点变化不用改客户端配置。
33. 🟢 在 Compass 里从零创建 `myFirstDB.users` 并插入第一条文档的步骤是什么？
    - 要点：Create Database → 填库名 / 集合名 → Create；打开集合 → Add Data → Insert Document → 粘贴 JSON（如 `{ "name": "Alice", "age": 25, "email": "alice@example.com" }`）→ Insert。
34. 🟡 连接串里的密码含特殊字符（`@` `:` `/`）连不上，怎么办？
    - 要点：对密码做 URL 编码（`@` → `%40`），或在 Compass 的高级选项里分字段填写；生产中把连接串放到 Secret / 环境变量，不要写进代码仓库。
35. 🔴 从运维视角比较：自建 MongoDB vs Atlas，各自的责任边界在哪？
    - 要点：Atlas 负责部署 / 补丁 / 备份 / 监控 / 扩容 / 多可用区；你仍要负责 **数据建模、索引、schema 校验、访问控制、成本（M0 免费但有 512MB 存储、连接数、Search 索引数等限制）**；自建则全部自理但可控成本与合规（数据不出境 / 离线环境）。

## 四、CRUD：增删改查（14 题）

36. ☆ 🟢 CRUD 分别对应 MongoDB 的哪些方法？为什么说「What you store is what you query」？
    - 要点：Create → `insertOne / insertMany`；Read → `find`；Update → `updateOne / updateMany`；Delete → `deleteOne / deleteMany`。查询语法本身就是 JSON，按 key:value 匹配。
37. 🟢 写出插入一个包含数组字段和嵌套文档的用户。
    - 要点：`db.users.insertOne({ name: "Rahul", age: 22, skills: ["JavaScript","MongoDB"], address: { city: "Delhi", country: "India" } })`。
38. 🟢 `insertOne` 与 `insertMany` 的区别？`insertMany` 中途有一条失败会怎样？
    - 要点：`insertMany` 接收数组批量插入；默认 `ordered: true`，遇错即停、前面的已写入、后面的不写；`ordered: false` 会继续插入其余文档。
39. ☆ 🟢 查所有用户、按 name 查、按嵌套字段 `address.city` 查，分别怎么写？
    - 要点：`db.users.find()`；`db.users.find({ name: "Rahul" })`；`db.users.find({ "address.city": "Delhi" })`（点号路径**必须加引号**）。
40. 🟡 `find({ skills: "MongoDB" })` 能查到 `skills` 是数组的文档吗？为什么？
    - 要点：能——MongoDB 对数组字段的等值匹配会匹配「数组中包含该元素」；要精确匹配整个数组才写 `{ skills: ["JavaScript","MongoDB"] }`。
41. ☆ 🟢 `updateOne` 里为什么必须写 `$set`？直接写 `{ age: 23 }` 会怎样？
    - 要点：`updateOne / updateMany` 要求更新文档以操作符开头，不写 `$set` 直接报错；只有 `replaceOne`（和已废弃的旧 `update()` 写法）才会用整个文档**替换**原文档、丢掉其他字段。`db.users.updateOne({ name: "Rahul" }, { $set: { age: 23 } })`。
42. 🟢 用 `$inc` 把 Rahul 的年龄加 1，用 `$push` 给他的 skills 追加 "Node.js"。
    - 要点：`{ $inc: { age: 1 } }`；`{ $push: { skills: "Node.js" } }`。
43. 🟡 `$push` 与 `$addToSet` 的区别？什么时候用后者？
    - 要点：`$push` 无脑追加（可重复）；`$addToSet` 只在元素不存在时加入，适合标签 / 技能这类**集合语义**字段。
44. 🟡 除了 `$set / $inc / $push`，再举三个常用更新操作符及用途。
    - 要点：`$unset`（删字段）、`$pull`（从数组移除匹配元素）、`$rename`（改字段名）、`$mul`、`$min / $max`、`$setOnInsert`（配合 upsert）。
45. ☆ 🟢 `deleteOne({ name: "Aman" })` 与 `deleteMany({ age: 21 })` 的区别？`deleteMany({})` 会发生什么？
    - 要点：前者只删第一条匹配、后者删全部匹配；`deleteMany({})` 清空整个集合（但保留索引）——生产上要先 `find` 确认过滤条件再删。
46. 🟡 `updateOne` / `deleteOne` 匹配到多条时，删 / 改的是哪一条？
    - 要点：自然顺序（或索引顺序）下的第一条，**不保证**是「最早」或「最新」的；要确定性操作就用 `_id` 或加 `sort`（`findOneAndUpdate` 支持 sort）。
47. 🟡 什么是 upsert？怎么写「存在就更新、不存在就插入」？
    - 要点：`db.users.updateOne({ name: "Rahul" }, { $set: { age: 23 } }, { upsert: true })`；常用于幂等写入（如按 `service+host` 记录最新心跳）。
48. 🔴 CRUD 里哪些操作是原子的？多文档事务什么时候需要？
    - 要点：**单文档写入天然原子**（含嵌套 / 数组），这是文档模型「把相关数据放一起」的核心收益；跨文档 / 跨集合要用 4.0+ 的多文档事务（需副本集），有性能与 60s 生命周期限制，能靠建模避免就避免。
49. 🟡 `find()` 返回的是什么？一次会把所有数据拉回客户端吗？
    - 要点：返回**游标（cursor）**，默认按批（首批 101 条 / 后续按 16MB batch）取；mongosh 里自动迭代前 20 条，用 `it` 继续；驱动里要 `toArray()` 或迭代。

## 五、实战：DevOps Log Explorer（用 MongoDB 存应用日志）（9 题）

50. ☆ 🟡 教程用 MongoDB 做「DevOps Logs Explorer」——为什么日志适合放 MongoDB？
    - 要点：日志是**半结构化数据**，每个服务字段不同、随时加字段；文档模型不用改表结构；按 `service / level / timestamp` 查询与排序直观；写入吞吐高。
51. 🟢 PyMongo 是什么？连接本地 MongoDB 并拿到 `devops_logs.logs` 集合的三行代码怎么写？
    - 要点：官方 Python 驱动（`pip install pymongo`）；`client = MongoClient("mongodb://localhost:27017")`、`db = client["devops_logs"]`、`logs = db["logs"]`。
52. 🟢 教程的日志文档包含哪些字段？每个字段的类型是什么？
    - 要点：`service`（string，如 auth-service / payment-service / order-service）、`level`（INFO / WARN / ERROR）、`message`（string）、`timestamp`（Python `datetime.utcnow()` → BSON Date）、`host`（server-1..3）。
53. ☆ 🟡 `timestamp` 为什么要用 `datetime` 而不是字符串？
    - 要点：BSON Date 可以做范围查询、正确排序、配合 TTL 索引自动过期；字符串排序只能按字典序，格式不统一就乱序，也无法 TTL。
54. 🟢 写出三条查询：所有 ERROR 日志、payment-service 的日志、按时间倒序看最新日志。
    - 要点：`db.logs.find({ level: "ERROR" })`、`db.logs.find({ service: "payment-service" })`、`db.logs.find().sort({ timestamp: -1 })`。
55. 🟡 查「最近 10 分钟 payment-service 的 ERROR」怎么写？需要什么索引？
    - 要点：`db.logs.find({ service: "payment-service", level: "ERROR", timestamp: { $gte: new Date(Date.now() - 10*60*1000) } }).sort({ timestamp: -1 })`；复合索引 `{ service: 1, level: 1, timestamp: -1 }`（等值字段在前、范围 / 排序字段在后，ESR 原则）。
56. ☆ 🔴 日志每 2 秒一条只是演示；真实系统日志量大了以后，用 MongoDB 存日志要注意什么？
    - 要点：**TTL 索引**自动清理（`createIndex({ timestamp: 1 }, { expireAfterSeconds: 7*86400 })`）；批量写（`insert_many`）而不是逐条；写关注（write concern）按重要性降级；考虑 **Time Series Collection**（5.0+）压缩与按时间分桶；超大规模仍应评估 ELK / Loki / ClickHouse 等专用日志系统，MongoDB 更适合「结构化事件 + 灵活查询」。
57. 🟡 教程的 `while True` 写入器如果 MongoDB 挂了会怎样？生产级写入器要补什么？
    - 要点：`insert_one` 抛异常导致进程退出；应加重试 / 退避、本地缓冲队列、连接超时参数（`serverSelectionTimeoutMS`）、健康检查；`retryWrites=true` 默认只重试一次。
58. 🟡 在 Compass 里 Refresh 才能看到新日志——如果要「实时」推送变更给前端，MongoDB 有什么机制？
    - 要点：**Change Streams**（`db.logs.watch()`，需副本集），基于 oplog 推送 insert / update 事件，比轮询高效。

## 六、MongoDB for AI Apps：向量检索实战（10 题）

59. ☆ 🟡 什么是 Embedding？教程里 `"embedding": [0.20, 0.90, 0.40, 0.18]` 这四个数字代表什么？
    - 要点：Embedding 模型把「意义」编码成固定维度的浮点向量，语义相近的对象向量距离近；教程用 4 维只是演示，真实模型通常 384 / 768 / 1536 维（如 OpenAI text-embedding-3-small 为 1536）。
60. ☆ 🟡 写出教程里的 Vector Search 索引定义，并解释每个字段。
    - 要点：`{ "fields": [ { "type": "vector", "path": "embedding", "numDimensions": 4, "similarity": "cosine" } ] }`；`path` 是向量字段名、`numDimensions` **必须与写入向量维度一致**、`similarity` 可选 `cosine / euclidean / dotProduct`；索引名如 `vector_index`。
61. 🟡 写出 `$vectorSearch` 聚合查询并解释 `numCandidates` 与 `limit`。
    - 要点：`db.products.aggregate([{ $vectorSearch: { index: "vector_index", queryVector: [0.20,0.90,0.40,0.18], path: "embedding", numCandidates: 100, limit: 3 } }])`；`numCandidates` 是 ANN 阶段先召回的候选数（越大越准越慢，官方建议 ≥ 10–20 × limit），`limit` 是最终返回条数。
62. 🟡 cosine / euclidean / dotProduct 三种相似度怎么选？
    - 要点：cosine 只看方向、对向量长度不敏感，文本 embedding 最常用；dotProduct 在向量已归一化时等价于 cosine 且更快；euclidean 看绝对距离，适合数值特征。**要与 embedding 模型推荐的度量一致。**
63. ☆ 🟡 教程强调「Vector Search works only in MongoDB Atlas」——为什么？自建 MongoDB 能做向量检索吗？
    - 要点：`$vectorSearch` 由 Atlas Search（基于 Lucene 的独立 `mongot` 进程）提供，社区版 `mongod` 没有；自建只能用 Atlas Search 的本地部署版（企业版 / 8.0+ 的自管 Search 节点）或退回到应用层暴力计算 / 专用向量库。
64. 🔴 MongoDB 作为向量库 vs 专用向量库（Milvus / Pinecone / Qdrant / pgvector），运维上怎么权衡？
    - 要点：MongoDB 优势：**业务数据与向量同库**，一条聚合就能「向量召回 + 元数据过滤（`filter`）+ 关联字段」，少一套系统的运维、一致性简单；劣势：Search 节点资源独立计费、超大规模（亿级向量）与高级索引（HNSW 参数、量化）不如专用库灵活。教程的建议：AI 应用先用 MongoDB 起步，规模上去再评估。
65. 🟡 在 RAG（检索增强生成）应用里，MongoDB 向量检索处于哪一步？完整链路是什么？
    - 要点：离线：文档切块 → embedding 模型 → 存 `{ text, embedding, metadata }`；在线：用户问题 → 同一模型 embedding → `$vectorSearch` 召回 top-k → 拼进 prompt → LLM 生成。关键：**写入与查询必须用同一个 embedding 模型与维度**。
66. 🔴 向量索引建好后查询结果为空或明显不准，排查思路？
    - 要点：索引是否 Ready（Atlas 里异步构建）；`numDimensions` 与数据是否一致；`path` 拼写；相似度类型与模型是否匹配；`numCandidates` 太小；文档里 embedding 是否被存成字符串 / 嵌套数组；M0 集群只允许 3 个 Search 索引。
67. 🟡 教程插入的 10 款手机里，为什么 Galaxy S23 / iPhone 14 Pro 的向量 `[0.40, 0.95, 0.60, 0.30]` 与其他不同？查询 `[0.20,0.90,0.40,0.18]` 会先返回谁？
    - 要点：演示「语义分群」——旗舰机向量与中端机明显不同；查询向量与 Pixel 7a 完全相同，所以 Pixel 7a 相似度最高，其次是 iPhone SE / Nothing Phone 1 等中端机；旗舰机排在后面。
68. ☆ 🔴 把教程的 6 章串成一句「MongoDB 学习路径」，并说出每一章在生产里对应的运维关注点。
    - 要点：概念（文档模型 / BSON / 校验）→ 建模（库 / 集合 / 文档 / 索引）→ 托管（Atlas 网络与账号）→ CRUD（原子性 / 操作符 / 游标）→ 日志实战（TTL / 批写 / 复合索引 / Change Streams）→ AI（向量索引 / 相似度 / RAG）；运维主线是 **索引设计、访问控制、容量与过期策略、备份与副本集**（后两者见 `ops-question-bank-1502.md` OTHER 40–43 与 middleware Q19–Q20）。

---

## 难度图例

🟢 初级（能背出定义 / 命令） · 🟡 中级（能解释为什么、会写查询与索引） · 🔴 高级（能做架构权衡与排障）

## 与 modules 的映射

| 本文件分组 | 对应 modules 模块 | 备注 |
|---|---|---|
| 一、Introduction / 二、Building Blocks / 四、CRUD | `middleware`（Q19 文档模型与索引） | 概念与建模基础 |
| 三、Atlas & Compass | `middleware` + `cloud-security` | 托管服务的网络 / 账号 / 责任边界 |
| 五、DevOps Log Explorer | `observability` + `middleware` | 日志存储选型、TTL、批写 |
| 六、MongoDB for AI Apps | `middleware`（Q20 向量检索）+ `gpu-ai` + `system-design`（RAG 主题） | 向量库选型与 RAG 链路 |
