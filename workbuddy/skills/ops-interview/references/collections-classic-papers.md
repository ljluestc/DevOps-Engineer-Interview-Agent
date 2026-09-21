# 经典论文面试题 — 从本机 `~/ebooks/` 的 19 篇公开论文与技术白皮书提炼（111 题）

> **来源**：用户本机 `~/ebooks/`（github.com/frankyyyt/ebooks 的克隆）中篇幅较短、公开可得的论文与白皮书；教材类版权书籍不出题，只在文末做书架索引。
> **收录日期**：2026-09-20
> **说明**：每题附「要点」，只提炼自论文原文（术语中英并存，保留原文数字与论证），不含逐字摘录；☆ = 系统设计 / SRE 面试高频；🟢/🟡/🔴 见文末图例。
> 需要原文时用 `arxiv` MCP 服务器（`search_papers` / `get_abstract`）或本机 PDF；本文件的定位是「候选人说到 Raft / GFS / CAP 时，面试官能追问到论文级细节」。
> **与 modules 的关系**：`system-design` Q1–Q4（方法论）与共识 / 存储 / 批处理类主题、`sre-reliability`（容错与可用性）、`kubernetes` Q40（etcd / Raft）、`linux`（I/O 模型与并发）、`network`（HTTP/2 / REST）、`middleware`（数据库与 JVM）。

## 论文清单

**一、共识与复制：Paxos / Raft / Spinnaker**

- **Paxos Made Simple** — Leslie Lamport；2001-11-01（后刊于 ACM SIGACT News 32(4)，2001-12）。
- **In Search of an Understandable Consensus Algorithm (Extended Version)** — Diego Ongaro, John Ousterhout（Stanford University）；技术报告，2014-05-20 发布，为 USENIX ATC'14 论文的扩展版。
- **Using Paxos to Build a Scalable, Consistent, and Highly Available Datastore** — Jun Rao, Eugene J. Shekita, Sandeep Tata（IBM Almaden Research Center / LinkedIn）；Proceedings of the VLDB Endowment, Vol. 4, No. 4（VLDB 2011, Seattle）。

**二、容错、时钟与可用性取舍：VM-FT / Lamport 时钟 / 拜占庭将军 / Harvest & Yield**

- **The Design of a Practical System for Fault-Tolerant Virtual Machines** — Daniel J. Scales, Mike Nelson, Ganesh Venkitachalam（VMware, Inc.）。正文未印出会议/期刊名与年份；文中描述的是 VMware vSphere 4.0 上的实现，页码 30–39（通常引作 ACM SIGOPS Operating Systems Review, 2010）。
- **Time, Clocks, and the Ordering of Events in a Distributed System** — Leslie Lamport（Massachusetts Computer Associates, Inc.）。Communications of the ACM, Vol. 21, No. 7, July 1978, pp. 558–565。
- **The Byzantine Generals Problem** — Leslie Lamport, Robert Shostak, Marshall Pease（SRI International）。ACM Transactions on Programming Languages and Systems, Vol. 4, No. 3, July 1982, pp. 382–401。
- **Harvest, Yield, and Scalable Tolerant Systems** — Armando Fox（Stanford University）, Eric A. Brewer（UC Berkeley）。正文未印出会议名与年份（通常引作 HotOS VII, 1999）。

**三、大规模存储与计算：GFS / MapReduce / Codd 关系模型 / 客户端缓存一致性**

- "The Google File System"，Sanjay Ghemawat, Howard Gobioff, Shun-Tak Leung（Google）；SOSP'03，2003 年 10 月 19–22 日，Bolton Landing, New York。
- "MapReduce: Simplified Data Processing on Large Clusters"，Jeffrey Dean, Sanjay Ghemawat（Google, Inc.）；OSDI'04（6th Symposium on Operating Systems Design and Implementation），USENIX，2004。
- "A Relational Model of Data for Large Shared Data Banks"，E. F. Codd（IBM Research Laboratory, San Jose）；Communications of the ACM, Vol. 13, No. 6, June 1970（收稿 1969-09，修订 1970-02）。
- "Maintaining Consistency of Client-Cached Data"，Kevin Wilkinson, Marie-Anne Neimat（Hewlett-Packard Laboratories, Palo Alto）；Proceedings of the 16th VLDB Conference, Brisbane, Australia, 1990。

**四、系统与并发、协议与运行时：Reactor / AQS / 线程 vs 事件 / 事务策略 / HTTP/2 / REST / JVM 内存管理**

- *Reactor: An Object Behavioral Pattern for Demultiplexing and Dispatching Handles for Synchronous Events*，Douglas C. Schmidt（Washington University, St. Louis；Siemens 资助）。文中说明早期版本是 *Pattern Languages of Program Design*（Addison-Wesley, 1995）一章；本版本年份未明示（参考文献引到 1998）。
- *The java.util.concurrent Synchronizer Framework*，Doug Lea（SUNY Oswego）。CSJP'04，2004 年 7 月 26 日，St John's, Newfoundland。
- *Why Events Are A Bad Idea (for high-concurrency servers)*，Rob von Behren, Jeremy Condit, Eric Brewer（UC Berkeley）。HotOS IX，Lihue, Hawaii，2003 年 5 月。
- *Transaction strategies: The High Concurrency strategy*，Mark Richards（Collaborative Consulting）。IBM developerWorks "Transaction strategies" 系列，2009 年 6 月 16 日。
- *http2 explained*（Background, the protocol, the implementations and the future），Daniel Stenberg（Mozilla，curl 作者）。文档版本 1.12，2015 年 5 月 21 日，CC BY 4.0；对应 RFC 7540。
- InfoQ eMag Issue 12 *REST*，2014 年 4 月。收录五篇：*A Brief Introduction to REST*（Stefan Tilkov）、*What Is REST?*（Mike Amundsen，演讲整理）、*How to GET a Cup of Coffee*（Jim Webber, Savas Parastatidis, Ian Robinson）、*REST Anti-Patterns*（Stefan Tilkov）、*RESTful Java Evolves*（Bill Burke，演讲整理）。
- *Memory Management in the Java HotSpot Virtual Machine*，Sun Microsystems 白皮书，2006 年 4 月（面向 J2SE 5.0）。
- *Accept() Scalability on Linux*，Stephen P Molloy（University of Michigan）与 Chuck Lever（Sun-Netscape Alliance），Linux Scalability Project / CITI。FREENIX Track, 2000 USENIX Annual Technical Conference，San Diego，2000 年 6 月 18–23 日。

---

## 一、共识与复制：Paxos / Raft / Spinnaker（27 题）

### Paxos Made Simple（Lamport, 2001）

1. 🟢 共识（consensus）问题的安全性要求是什么？Paxos 里有哪三种角色，系统模型有什么假设？
   - 要点：三条安全性（safety）：**只有被提出（proposed）的值才能被选定（chosen）**、**只能选定一个值**、**进程不会"学到"一个实际没被选定的值**；活性（liveness）目标是最终有值被选定且能被学到，论文不做精确规定。三种角色：**proposer（提议者）、acceptor（接受者）、learner（学习者）**，一个进程可以兼任多个角色。模型是**异步、非拜占庭（non-Byzantine）**：进程速度任意、可以宕机停止再重启（因此必须有**稳定存储**记住信息，否则全部宕机重启后无解）；消息可以任意延迟、重复、丢失，但**不会被篡改**。

2. ☆ 🟡 为什么 Paxos 用多数派（majority）来判定"值被选定"？为什么 acceptor 必须允许接受多个提案？
   - 要点：单 acceptor 最简单，但它一挂就无法继续。改用多个 acceptor 后，需要"足够大"的集合接受同一个值才算选定；取**任意多数派**，因为**任意两个多数派至少有一个公共 acceptor**——若每个 acceptor 最多接受一个值，就能保证唯一性。但无失败时希望"只有一个 proposer 提一个值"也能被选定，于是要求 **P1：acceptor 必须接受它收到的第一个提案**。P1 与多数派规则结合会出现"每个 acceptor 都接受了值、却没有任何值达到多数"的僵局，因此 **acceptor 必须能接受多个提案**，为区分它们给每个提案编号（proposal number），提案 = 编号 + 值；不同提案编号必须不同。

3. ☆ 🟢 描述 Paxos 的两阶段消息流程（Phase 1 / Phase 2），acceptor 需要持久化哪些信息？
   - 要点：**Phase 1a**：proposer 选编号 n，向多数 acceptor 发 **prepare(n)**；**Phase 1b**：若 n 大于该 acceptor 已回复过的任何 prepare 编号，则回复**承诺（promise）不再接受编号小于 n 的提案**，并附上**它已接受的最高编号提案**（若有）。**Phase 2a**：proposer 收到多数回复后发 **accept 请求 (n, v)**，其中 v 是回复里**最高编号提案的值**，若回复中都没有提案则可以**任选**；**Phase 2b**：acceptor 收到 accept(n, v) 时，除非它已回复过更大编号的 prepare，否则接受（P1a）。acceptor 只需记住两样东西：**已接受的最高编号提案** 和 **已回复的最高 prepare 编号**，并且要在**稳定存储**里先记录再发送回复；proposer 可以随时放弃提案，只要不再复用同一个编号。忽略任何请求都不影响安全性。

4. ☆ 🔴 论文如何从 P2 一步步推导出不变式 P2c？为什么"提取承诺"是关键？
   - 要点：允许多个提案被选定，但必须**值相同**。**P2**：若值为 v 的提案被选定，则所有更高编号的被选定提案值也为 v。被选定必先被接受，故加强为 **P2a**（更高编号被任一 acceptor 接受的提案值为 v）；但异步下某 acceptor c 可能从未收到任何提案，此时 P1 要求它接受新 proposer 的不同值，与 P2a 冲突，于是再加强为 **P2b**（更高编号被任一 proposer 发出的提案值为 v）。P2b ⇒ P2a ⇒ P2。对 n 归纳证明 P2b 时得到不变式 **P2c**：发出 (n, v) 前必须存在一个多数派 S，使得 **(a) S 中无人接受过编号 < n 的提案，或 (b) v 是 S 中所有编号 < n 的已接受提案里最高编号的值**。要维持 P2c，proposer 必须知道每个 acceptor "已经或将会"接受的最高提案——预测未来不可行，所以**通过让 acceptor 承诺不再接受编号 < n 的提案来控制未来**，这就是 prepare 阶段的由来。

5. 🟢 learner 如何得知一个值已被选定？论文给出了哪几种方案及其代价？
   - 要点：learner 必须知道某提案被**多数 acceptor 接受**。方案一：每个 acceptor 接受后通知所有 learner，最快但消息数是 **acceptor 数 × learner 数**。方案二：acceptor 只通知一个**特权 learner（distinguished learner）**，由它转告其他 learner，消息数降为 **acceptor 数 + learner 数**，代价是**多一轮**且该 learner 可能故障。方案三：通知**一组**特权 learner，可靠性与通信开销折中。因为消息丢失，可能值已选定却没有 learner 知道；learner 可以让 proposer 再发起一次提案来确认结果。

6. ☆ 🔴 Paxos 为什么可能永远无法取得进展（活锁）？如何保证活性，以及这和 FLP 不可能结果的关系？
   - 要点：两个 proposer 交替提高编号：p 完成 n1 的 Phase 1，q 用 n2 > n1 完成 Phase 1，p 的 accept(n1) 被拒；p 再用 n3 > n2 完成 Phase 1，q 的 accept(n2) 被拒……**无限循环，没有值被选定**。解决：选出一个**特权 proposer（distinguished proposer）** 作为唯一发起者；只要它能与多数 acceptor 通信且使用比已用过的都大的编号，就能成功。**FLP 结果**意味着可靠的选举算法必须依赖**随机性或真实时间（如超时）**。核心结论：**选举成功与否只影响活性，安全性在任何情况下都成立**。

7. ☆ 🟡 Paxos 如何用来实现复制状态机（Multi-Paxos）？为什么新 leader 上任只需一条消息就能对"无穷多个实例"执行 Phase 1？日志空洞怎么处理？
   - 要点：把系统建成**确定性状态机**的多副本，第 i 个共识实例选定第 i 条命令；每台 server 在每个实例里同时扮演三种角色。正常运行时选一个 leader 作特权 proposer，客户端把命令发给它，由它决定命令序号。关键效率点：**要提的值直到 Phase 2 才确定**，所以新 leader 可以对所有未决实例（论文例子：135–137 及 >139）**用同一个提案编号、一条短消息**完成 Phase 1；acceptor 也只需对收到过 Phase 2 消息的实例附上值。空洞（如 136、137）用**特殊 no-op 命令**填补，之后才能执行 138–140。leader 可以领先 **α** 条命令，因此宕机可能留下最多 **α−1** 的空洞。稳态成本只有 **Phase 2**，论文引用 Keidar & Rajsbaum 指出这是容错共识的**最小代价**，故 Paxos "本质上最优"。

8. ☆ 🟡 如果有两个 server 同时认为自己是 leader（脑裂）会发生什么？成员集合变化怎么处理？
   - 要点：多个 leader 可能在同一实例里各自提议，**可能导致没有值被选定**（活性受损），但**绝不会让两台 server 对第 i 条命令的值产生分歧**——安全性由共识算法本身保证，**选举单一 leader 只是为了进展**。提案编号唯一性靠**不同 proposer 使用不相交的编号集合**，并在稳定存储里记住自己用过的最高编号。成员变化：**把当前 server 集合作为状态机状态的一部分，用普通状态机命令修改**；配合"领先 α"的规则，**执行第 i+α 个实例的 server 集合由第 i 条命令执行后的状态决定**，可以实现任意复杂的重配置。

---

### In Search of an Understandable Consensus Algorithm — Raft（Ongaro & Ousterhout, 2014）

9. ☆ 🟢 Raft 里 server 有哪三种状态？什么是 term（任期），它起什么作用？
   - 要点：三种状态：**leader、follower、candidate**；正常时恰有一个 leader，其余是被动的 follower（不主动发请求，客户端找错节点会被重定向到 leader）。典型集群 **5 台，可容忍 2 台故障**。时间被划分为编号连续递增的 **term**，每个 term 以一次选举开始；选举可能因分票（split vote）无 leader 结束。term 是 Raft 的**逻辑时钟**：每台 server 持久保存 currentTerm，通信时交换；看到更大的 term 就更新自己并**退回 follower**，收到过期 term 的请求则拒绝。基础算法只有 **两种 RPC：RequestVote 和 AppendEntries**（后者也做心跳），第三种 InstallSnapshot 用于快照。持久化状态：currentTerm、votedFor、log[]。

10. ☆ 🟡 Raft 的 leader 选举是如何触发和完成的？为什么用随机化超时而不是排名？
   - 要点：leader 定期发**空 AppendEntries 心跳**维持权威；follower 在 **election timeout** 内没收到任何有效 RPC 就**递增 term、转为 candidate、给自己投票、并行发 RequestVote**。三种结局：(a) 得到**全集群多数票**当选；(b) 收到 term ≥ 自己的 leader 的 AppendEntries，退回 follower；(c) 超时无人胜出，再开新一轮。**每台 server 每个 term 只投一票（先到先得）**，多数规则保证 **Election Safety：每 term 至多一个 leader**。为减少分票，超时从固定区间**随机**选（如 **150–300ms**），通常只有一台先超时并抢先发心跳；分票后每个 candidate 也重新随机等待。作者最初设计过**排名制**（低排名者让位），但发现可用性上的微妙角落案例不断出现，最终认为随机重试更直观、更易懂。

11. ☆ 🟡 什么是 Log Matching Property？AppendEntries 的一致性检查如何让 follower 日志收敛到 leader？
   - 要点：Log Matching 两条：**不同日志中索引和 term 相同的条目存储相同命令**；**且它们之前的所有条目也完全相同**。第一条来自 leader 在一个 term 内对同一索引只创建一个条目且条目位置不变；第二条靠 AppendEntries 的**一致性检查**：leader 带上新条目前一条的 **prevLogIndex / prevLogTerm**，follower 找不到匹配就拒绝——这是归纳步骤，空日志满足性质，每次扩展都保持。leader 崩溃可能留下不一致（follower 缺条目、多出未提交条目或两者兼有，可跨多个 term，见 Figure 7）。leader 用 **nextIndex[]**（初始化为自己最后索引 +1）处理：被拒就**递减 nextIndex 重试**，直到找到匹配点，然后**删除 follower 冲突条目并追加 leader 的条目**。优化：follower 拒绝时返回冲突条目的 term 及该 term 首索引，可一次跳过整个 term。**leader 永不覆盖或删除自己的日志（Leader Append-Only）**，日志只从 leader 流向 follower。

12. ☆ 🟡 Raft 中一条日志何时算"已提交（committed）"？follower 怎么知道？
   - 要点：leader 把客户端命令追加到本地日志，并行发 AppendEntries；**当创建该条目的 leader 把它复制到多数 server 上时即为 committed**（Figure 6 的 entry 7），同时**间接提交 leader 日志中所有之前的条目，包括前任 leader 创建的**。leader 应用到状态机后回复客户端；对慢或宕机的 follower **无限重试**（即使已回复客户端）。leader 跟踪最高已知的 commitIndex，通过后续 AppendEntries（含心跳）的 **leaderCommit** 字段传播；follower 得知后按日志顺序应用。Figure 2 的规则：存在 N > commitIndex，多数 matchIndex[i] ≥ N **且 log[N].term == currentTerm** 时才设置 commitIndex = N。正常情况下**一轮 RPC 到多数派即可**，单个慢 follower 不影响性能。

13. ☆ 🔴 Raft 的选举限制（election restriction）是什么？请给出 Leader Completeness 的证明思路。
   - 要点：Raft 不像 Viewstamped Replication 那样允许缺少已提交条目的 server 当选再补传，而是**用投票直接保证新 leader 已含全部已提交条目**。RequestVote 携带候选人的 **lastLogIndex / lastLogTerm**，投票者若自己的日志**更新（more up-to-date）** 则拒绝投票；比较规则：**最后条目 term 大者更新，term 相同则更长者更新**。候选人必须得到多数票，而已提交条目也存在于多数 server 上，两者必有交集。证明（反证）：设 term T 的 leader 提交了某条目，而后来最小的 term U > T 的 leader 不含它。则 (1) 该条目在 leaderU 当选时就不在其日志中（leader 不删日志）；(2) 存在一个 **"投票者"** 既接受了 leaderT 的条目又投票给 leaderU；(3) 投票者接受条目在先，否则会因 term 更高拒绝 leaderT；(4) 投票时仍保留该条目，因为中间所有 leader 都含它且 follower 只在与 leader 冲突时删条目；(5) 因此 leaderU 的日志至少和投票者一样新：若末尾 term 相同则 leaderU 更长故包含该条目——矛盾；若 leaderU 末尾 term 更大，则创建那条末尾条目的更早 leader 含已提交条目，由 Log Matching leaderU 也含——矛盾。由此得 **State Machine Safety**：任何 server 在某索引应用的条目全局唯一。

14. ☆ 🔴 为什么 Raft 的 leader 不能通过"计数副本"来提交前一任期的日志条目（Figure 8）？Raft 怎么处理？
   - 要点：Figure 8 时序：S1 在 term 2 部分复制索引 2；S1 崩溃，S5 靠 S3、S4 当选 term 3 并在索引 2 写入不同条目；S5 崩溃，S1 重新当选并继续复制，term 2 的条目已在多数派上却**未提交**——若此时 S1 崩溃，S5 仍可赢得选举并**覆盖**该条目。因此 Raft **只对当前 term 的条目通过计数副本提交**，一旦当前 term 的条目提交，之前的条目由 Log Matching **间接提交**；即使旧条目已在所有 server 上也不做特殊判断，选择更保守的规则以求简单。这种额外复杂性源于 Raft 让条目**保留原始 term 号**（其他算法会用新 term 重新编号再复制），好处是条目在时间和不同日志间保持同一 term，更易推理，且新 leader 需重发的旧条目更少。

15. 🟢 follower 或 candidate 崩溃时 Raft 怎么处理？为什么 RPC 需要幂等？
   - 要点：比 leader 崩溃简单得多，两者处理方式相同：发给它们的 RequestVote / AppendEntries 会失败，Raft **无限重试**，节点恢复后 RPC 即完成。若 server 完成 RPC 后、回复前崩溃，重启后会**再次收到同一 RPC**；因 Raft 的 RPC 是**幂等**的，不会造成损害——例如 AppendEntries 中已存在于日志的条目会被直接忽略。

16. ☆ 🟡 Raft 对时间有什么要求？election timeout 应该怎么选，论文的实验数据是什么？
   - 要点：安全性**不依赖时序**，但可用性不可避免地依赖。要求 **broadcastTime ≪ electionTimeout ≪ MTBF**：广播时间应比选举超时小一个数量级，leader 才能可靠发出心跳、分票也少见；选举超时应比 MTBF 小几个数量级，因 **leader 崩溃后系统不可用时间约等于一个选举超时**。RPC 通常要持久化，broadcastTime 约 **0.5ms–20ms**，故超时大致在 **10ms–500ms**，MTBF 通常数月。实验（5 节点、广播约 15ms、leader 在心跳间隔内随机崩溃）：**无随机化时选举经常超过 10 秒**（大量分票）；加 **5ms 随机量**中位停机 **287ms**；**50ms** 随机量最坏 **513ms**（1000 次）；超时 **12–24ms** 时平均 **35ms** 选出（最长 152ms），但再低就违反时序要求导致不必要换主。推荐保守的 **150–300ms**。

17. ☆ 🔴 Raft 如何安全地变更集群成员（joint consensus）？还要处理哪三个额外问题？
   - 要点：直接从 C_old 切到 C_new 不安全：无法原子切换，过渡期可能出现**两个不相交的多数派在同一 term 各选出一个 leader**（Figure 10，3→5 节点）。Raft 用两阶段：先进入**联合共识 C_old,new**——日志复制到两个配置的所有 server，任一配置的 server 都可当 leader，但**选举和提交都需要 old 与 new 各自的多数派**。配置作为**特殊日志条目**存储，server **一旦看到该条目就立即使用（不等提交）**；C_old,new 提交后，只有含该条目的 server 能当选，再写入 C_new 条目并按 C_new 规则提交，旧配置即可下线。三个问题：(1) 新节点无日志会拖慢提交——先作为**非投票成员**追赶；(2) leader 不在 C_new 中——**提交 C_new 后再退位**，期间管理不含自己的集群、不把自己计入多数；(3) 被移除的节点收不到心跳会超时发起选举、用更高 term 打扰 leader——server **在最小选举超时内收到过 leader 消息时忽略 RequestVote**。与 VR、SMART 相比，Raft 变更期间不停止正常请求、机制更少。

18. 🟡 Raft 的日志压缩（快照）怎么做？为什么允许 follower 自行快照而不是由 leader 统一发？
   - 要点：日志不能无限增长（占空间、重放慢）。快照：状态机把当前状态写入稳定存储，丢弃之前的日志；每台 server **独立**对**已提交**条目做快照，元数据包括 **lastIncludedIndex / lastIncludedTerm**（供快照后第一条日志做一致性检查）以及**最新的集群配置**。leader 只在**已丢弃某 follower 所需条目**时（极慢 follower 或新节点）用 **InstallSnapshot RPC** 分块发送，每块也充当"活着"信号重置选举计时；follower 若快照包含新信息则**丢弃全部日志**，若快照只是自身日志的前缀则保留其后的条目。这偏离了"强 leader"，但共识已达成、不会产生冲突决定。不采用 leader 统一发送，因为**浪费网络带宽、更慢，且 leader 要并行处理快照与新日志更复杂**。何时快照：简单策略是**日志达到固定字节数**，且远大于快照大小以控制磁盘开销；写快照耗时，用**写时复制（copy-on-write）**，如函数式数据结构或 Linux fork（作者实现用后者）。也可用 LSM 树等增量方式通过同一接口实现。

19. ☆ 🔴 Raft 如何实现线性一致（linearizable）语义？只读请求为什么不能直接由 leader 回答，Raft 加了哪两项措施？
   - 要点：目标是每个操作看起来在调用与响应之间**瞬时、恰好一次**执行。写重复问题：leader 提交后、回复前崩溃，客户端会向新 leader 重试导致执行两次；解决是**客户端给每条命令分配唯一序列号**，状态机记录每个客户端最新序列号及响应，重复直接返回。只读请求不写日志，但 leader 可能已被新 leader 取代而不自知，返回**过期数据**。两项措施：(1) leader 必须知道最新的已提交条目——Leader Completeness 保证它拥有，但任期开始时不知道哪些已提交，故 **每个 leader 上任先提交一条空 no-op**；(2) 处理只读请求前**与多数派交换一次心跳确认自己未被罢免**。替代方案是基于心跳的 **lease**，但那依赖有界时钟偏移，把安全性寄托在时序上。客户端启动时随机连一台 server，非 leader 会返回它最近知道的 leader 地址（AppendEntries 中包含）。

20. 🟢 Raft 论文用什么证据证明它比 Paxos 更易理解？实现和形式化验证情况如何？
   - 要点：用户研究：Stanford 与 Berkeley **43 名学生**，各看一段 Raft 和 Paxos 视频并做对应测验，一半先学 Paxos、一半先学 Raft。**33 人 Raft 分数更高**；60 分制平均 **Raft 25.7 vs Paxos 20.8**，高出 **4.9 分**；配对 t 检验 95% 置信下 Raft 均值至少高 **2.5 分**。实验偏向 Paxos：**15 人有 Paxos 经验**，Paxos 视频**长 14%**；回归模型预测差距 12.5 分。问卷中 **33/41** 认为 Raft 更易实现、也更易解释。正确性：**TLA+ 规约约 400 行**，Log Completeness 用 TLA 证明系统机械验证，State Machine Safety 有约 3500 词的非形式化证明。实现：RAMCloud 中约 **2000 行 C++**（LogCabin），另有约 **25 个第三方开源实现**。消息类型只有 **4 种**（两种 RPC 及其响应），而 VR 和 ZooKeeper 各 **10 种**。

---

### Using Paxos to Build a Scalable, Consistent, and Highly Available Datastore — Spinnaker（Rao, Shekita, Tata, VLDB 2011）

21. ☆ 🟢 Spinnaker 是什么？它与 Dynamo、Bigtable、PNUTS 的核心区别是什么？
   - 要点：面向**单数据中心**大规模商用服务器集群的实验性数据存储：**基于 key 的范围分区（range partitioning）、3 副本、事务性 get-put API**，读可选 **强一致（strong）或时间线一致（timeline）**；CAP 术语下是 **CA 系统**，跨数据中心假定用另一套（大概率异步）复制。对比：**Dynamo** 是 AP、最终一致，靠向量时钟解冲突、read-repair / merkle tree 反熵，应用需自行处理冲突；Spinnaker **无需冲突解决，只用 Paxos 一种机制**同步副本。**Bigtable** 把数据、日志和复制都交给 GFS：强制刷日志页要与集中式 GFS master 通信并等远端副本确认，**没有热备**，节点宕机后其数据**直到重启并重放 GFS 日志前不可用**。**PNUTS** 支持时间线一致，但侧重跨数据中心，依赖未公开细节的 Yahoo Message Broker。API：get/put/delete/conditionalPut/conditionalDelete，版本号单调递增，用于**乐观并发控制**的读-改-写。

22. ☆ 🟡 为什么 Spinnaker 不用传统同步主从复制？为什么选 3 副本而不是 2 副本？2PC 为什么不合适？
   - 要点：Figure 1 的失败序列：主从都在 LSN=10；从库宕机，主库继续写到 LSN=20 后也宕机；从库先恢复但**没有最新状态，不能读写**；若主库永久故障，**LSN 11–20 的已提交写丢失**。避免它只能在任一节点宕机时阻塞写，牺牲可用性；大集群里"罕见事件"会变得常见。**Paxos 用 2F+1 副本容忍 F 个失败**，且**无论失败顺序如何**，只要多数副本存活就可读写。3 副本：**双盘故障**在大集群更常见；单节点故障不再进入"再坏一个就丢数据"的 panic 模式；可**下线一个副本做在线升级**。2PC 不合适：把每个参与者当独立资源管理器，**单节点故障即中止**、每事务 **2 次刷盘 + 2 次消息延迟**、**协调者故障会阻塞**；3PC 性能差很少使用。

23. ☆ 🟡 什么是 cohort？描述 Spinnaker 稳态下一次写的完整流程，提交一次写需要多少次刷盘和消息？
   - 要点：每个节点负责一个基础 key 范围，并复制到**后续 N−1 个节点**（N=3，类似 chained declustering）；复制同一范围的 3 个节点称为 **cohort**，cohort 相互重叠（A-B-C 管 [0,199]，B-C-D 管 [200,399]…）。每个 cohort 有一个 **leader** 和两个 follower；协议分**选举阶段**和**法定人数（quorum）阶段**，无故障时只跑后者。写 W 总被路由到 leader：leader 追加日志并**强制刷盘**，**并行地**把 W 放入 **commit queue** 并向 follower 发 **propose**；follower 强制刷盘、入 commit queue、回 **ack**；leader 收到**至少一个 follower 的 ack** 后把 W 应用到 memtable 即提交，回复客户端。**没有单独的 commit 记录**，因为是单操作事务，持久性靠恢复时重新提议保证。leader 周期性发**异步 commit 消息**让 follower 应用到某 LSN，双方用**非强制日志写**记录 **last committed LSN**；间隔叫 **commit period**。合计 **3 次刷盘 + 4 条消息**，但大量重叠，关键路径是 **1 次刷盘 + 2 次消息延迟**；使用 group commit。节点内共享 WAL，各 cohort 用**逻辑 LSN**；memtable 定期刷成 SSTable 并后台合并（Bigtable 设计）。**ZooKeeper 不在读写关键路径上**，平时只交换心跳，一个 ZooKeeper 服务预期可支撑数千节点。

24. ☆ 🟡 强一致读与时间线一致读有何区别？各自的可用性条件是什么？与 Cassandra 的性能对比结论是什么？
   - 要点：**强一致读只路由到 cohort leader**，必定看到最新值；**时间线读可路由到任一节点**，在 commit 消息到达前可能看到旧值，缩短 commit period 可减少陈旧度。可用性：写和强一致读需要 cohort 中**多数（2）节点存活**；时间线读**只需 1 个节点存活**。实验（同源于 Cassandra 代码库，4KB 值，10 节点，关闭磁盘写缓存）：Cassandra **quorum 读延迟比 Spinnaker 强一致读差 1.5x–3.0x**，且更早到达拐点，因为 quorum 读要访问 2 个副本并检查冲突，而强一致读只访问 leader 副本；**时间线读延迟与 Cassandra weak 读几乎相同**；**写比 Cassandra quorum 写慢 5%–10%**，因为要等 leader 和一个特定 follower 的 ack，而 quorum 写等任意 2 个副本。混合负载：10% 写时 Spinnaker 强一致组合好约 10%，50% 写时 Cassandra 好约 7%。注意 Cassandra 的 quorum 读写**仍不保证强一致**——没有 leader 串行化写，也没有基于 quorum 的恢复算法。

25. ☆ 🔴 Spinnaker 如何用 ZooKeeper 做 leader 选举？为什么能保证新 leader 不丢任何已提交写？epoch 号起什么作用？
   - 要点：按 cohort 运行，触发条件是 leader 故障或系统重启后的本地恢复完成。步骤（Figure 7）：清理 /r 下旧状态；每个节点在 **/r/candidates** 下创建**顺序临时（sequential ephemeral）znode**，值为自己的**最后 LSN n.lst**；设置 watch 等待**多数（2 个）候选者**出现；**n.lst 最大者当选**，用 znode 序号打破平局；新 leader 在 **/r/leader** 写临时 znode（自己失败时 cohort 能被通知），执行 leader takeover；其他节点读 /r/leader 得知 leader。不丢已提交写的论证：**一次已提交写至少强制写入 cohort 中 2 个节点的日志**，而**至少 2 个节点参与选举**，3 节点下两者必有交集，所以至少一个参选者含最后一条已提交写，**选 n.lst 最大者**保证新 leader 含有它；若它在别的节点仍是未决状态，takeover 会重新提议。**Epoch 号**保存在 ZooKeeper、每次换主递增，占 LSN 的高位，保证新 leader 分配的 LSN 大于 cohort 此前用过的任何 LSN——**LSN 实际上扮演 Paxos 提案编号的角色**。ZooKeeper 自身基于 Paxos，用 Paxos 协调服务简化另一套 Paxos 实现也是 Vertical Paxos 提倡的思路。

26. ☆ 🔴 描述 Spinnaker 的 leader takeover 与 follower 恢复流程；什么是日志的"逻辑截断"？恢复时间由什么决定？
   - 要点：**Leader takeover（Figure 6）**：取 leader 的 l.cmt（last committed）和 l.lst（last LSN）；对每个 follower 发送 (f.cmt, l.cmt] 的已提交写并发 commit 消息（follower 用 LSN 去重）；**等至少一个 follower 追到 l.cmt**；把 (l.cmt, l.lst] 的**未决写重新提议**并按常规协议提交；然后**开放写入**，起始 LSN 大于此前任何 LSN。旧 leader 回来后作为 follower 走恢复流程。**Follower 恢复**分两阶段：**本地恢复**——从最近 checkpoint 幂等地重放到 f.cmt；f.cmt 之后的写状态**不确定**（可能已被 leader 提交也可能没有）；**catch up**——向 leader 通告 f.cmt，leader 回送之后所有已提交写，结束时**短暂阻塞新写**确保追平；磁盘全丢则直接进入 catch up。日志被 SSTable 捕获后会滚动，leader 可能没有所需日志，故每个 SSTable 打上 **min/max LSN** 标签，必要时直接发 SSTable。**逻辑截断**：新 leader 可能丢弃了 f.cmt 之后的一些记录（如 Figure 10 里节点 C 的 LSN 1.22），但不能物理截断，因为**日志被多个 cohort 共享**，其他 cohort 可能还需要那些记录；于是把这些 LSN 记入 **skipped-LSN 列表**持久化，后续本地恢复跳过。可用性实验：恢复时间（含选举和清理未决状态，**不含 ZooKeeper 2 秒故障检测超时**）与 commit period 成正比：**1s → 0.4s，5s → 1.5s，10s → 2.6s，15s → 4.0s**；取 1 秒可使恢复 **小于半秒**，还可把 commit 消息**捎带在新写的 propose 上**进一步缩短。

27. 🟡 Spinnaker 的协议与教科书 Multi-Paxos 有哪些不同？论文承认的设计权衡和持久性边界是什么？
   - 要点：差异：(1) 把**复制、提交处理与恢复整合进同一个协议框架和共享 WAL**；(2) 增加强制的 **catch up 阶段**——基本 Multi-Paxos 允许故障节点恢复后立即参与下一轮，Spinnaker 中带缺口的日志会导致数据不一致，不可接受；(3) 用 **TCP 可靠有序消息**简化协议（ZooKeeper 也如此），而 Multi-Paxos 假设不可靠消息层；(4) 交给 **ZooKeeper 做选举**。Multi-Paxos 稳态下 leader 稳定即跳过选举，只跑 quorum 阶段，**2 次消息延迟**确认。权衡：所有写和强一致读都必须经 cohort leader，性能/扩展/可用性可能低于 Dynamo 类系统；ZooKeeper 作为集中协调者**限制扩展上限**；不做跨数据中心，Cassandra 无中心协调者且能跨 DC。持久性边界：正常情况下 2/3 节点永久故障也不丢已提交数据，但 **leader 与一个 follower 快速相继永久故障**时可能丢失一小窗口的已提交写。其他数据：EC2 上 20/40/80 节点写延迟基本恒定（写只涉及 3 个节点）；**SSD 做日志盘**后两者写延迟降到 **6ms 以内**，Spinnaker 受益更大且可去掉共享日志文件；**2/3 内存日志**提交可达约 **2ms**（强一致 + 弱持久，全 cohort 同时断电才丢少量写）；Cassandra quorum 写比 weak 写慢 **40%–50%**；conditional put 仅比普通 put 略慢（多一次版本读取比较），且因写按 LSN 顺序执行，其结果在 cohort 各节点一致。

---

## 二、容错、时钟与可用性取舍：VM-FT / Lamport 时钟 / 拜占庭将军 / Harvest & Yield（25 题）

### VM-FT：实用的容错虚拟机系统（Scales / Nelson / Venkitachalam）

28. 🟢 VM-FT 采用的是哪种容错思路？为什么论文认为 hypervisor 上的虚拟机是实现"状态机复制"的理想平台？
   - 要点：**主/备（primary/backup）** 方式：备机随时可接管，且故障对外部客户端不可见、不丢数据。两种同步方式：一是把主机的全部状态变化（CPU、内存、I/O）持续发给备机，**带宽极大**；二是 **状态机方法（state-machine approach）**——把服务器建模为确定性状态机，从同一初始状态出发、以相同顺序喂入相同输入，只需额外传递非确定性操作的信息，**远小于内存变更量**。VM 是"定义良好的状态机"，操作就是被虚拟化的机器（含所有设备）的操作；hypervisor 完全控制 VM 执行（包括所有输入的投递），因此能捕获主机上所有非确定性信息并在备机上重放。结果是无需硬件改动、可立即支持最新处理器、且对**任意 x86 OS 与应用**透明；论文只处理 **fail-stop** 故障（故障在造成对外可见的错误动作前即可被检测到）。

29. ☆ 🟡 解释 VM-FT 中的确定性重放（deterministic replay）与日志通道（logging channel）：主机要记录哪些东西？备机如何做到与主机执行完全一致？
   - 要点：VM 的输入包括网络包、磁盘读、键鼠；**非确定性事件**（如虚拟中断）与**非确定性操作**（如读时钟周期计数器）也影响状态，三大挑战是：正确捕获所有输入与非确定性、正确在备机上应用、且不拖慢性能；x86 上许多指令有未定义副作用，需要一并复现。VMware deterministic replay 把输入与所有非确定性写成 **log entries**；对中断类事件还记录**发生时的精确指令位置**，重放时在指令流同一点投递（借助与 AMD/Intel 合作的硬件性能计数器），因此**无需 Bressoud/Schneider 的 epoch 批处理**。FT 把日志不写盘而是经 **logging channel** 发给备机实时重放；备机产生的输出被 hypervisor **丢弃**，只有主机对外输出；共享磁盘（FC/iSCSI）供两者访问，只有主机在网络上宣告自身存在。生产版 replay/FT **只支持单处理器 VM**——多处理器下几乎每次共享内存访问都是非确定性操作。

30. ☆ 🔴 什么是 Output Rule？它解决的 Output Requirement 是什么？为什么它不要求停止主机执行，也为什么不能保证输出"恰好一次"？
   - 要点：**Output Requirement**：备机接管后必须与主机已发往外部世界的所有输出保持一致。接管后备机执行路径大概率与主机不同（非确定性事件），但只要满足该要求，外部就看不到中断或不一致。必要条件是备机已收到输出操作之前的全部日志；但若主机在输出后立刻宕机，备机必须 **重放到输出点再 go live**——若停在更早的日志点，一个定时器中断就可能改变路径。做法：在每个输出操作处生成**特殊日志项**，并遵守 **Output Rule：主机在备机收到并确认（ack）该输出操作对应的日志项之前，不得向外部发送输出**。与 [3,9] 等前人工作不同，**只延迟输出本身，VM 继续执行**——OS 的网络/磁盘输出本来就是非阻塞、异步中断通知完成，所以 VM 不会立刻被延迟影响。无法保证 **exactly-once**：不用两阶段提交事务，备机无法判断主机是在最后一次输出之前还是之后崩溃；好在网络基础设施（TCP）本就能处理**丢包与重复包**。

31. ☆ 🔴 VM-FT 如何检测主/备故障？出现脑裂（split-brain）时怎么保证只有一个 VM go live？
   - 要点：检测：服务器之间的 **UDP heartbeat**，加上监控 logging channel 上的**日志流与 ack 流**——因为定时器中断规律发生，正常 guest OS 的日志流不会停；日志/ack 停止超过一个超时（**几秒量级**）即宣告故障。备机故障：主机 go live（退出记录模式、停发日志）。主机故障：备机需**先把已收到、已确认但尚未消费的日志重放完**，再切换为正常执行，成为新主机。任何基于超时的检测都会遇到脑裂：心跳丢失可能只是网络断了，若备机 go live 而主机仍在运行，会造成数据损坏。解法：利用存放虚拟磁盘的 **共享存储上的原子 test-and-set**——想 go live 的 VM 先执行该操作，成功才能接管；失败说明对方已接管，本 VM **自杀（commits suicide）**；若暂时访问不了共享存储就等待——因为虚拟盘也在同一存储上，访问不到时 VM 本来也干不了活，所以**不引入额外不可用**。非共享盘配置下则需外部仲裁：第三方 tiebreaker 服务器，或集群超过两节点时按**多数派子集群**决定。

32. 🟡 主机故障后，备机"go live"具体要做哪些事？VM-FT 又如何自动恢复冗余？
   - 要点：go live 前先重放完所有已确认的日志；成为主机后开始对外输出，需要设备相关的收尾：在网络上**自动宣告新主机的 MAC 地址**，让物理交换机学到新位置；对故障时**主机尚未完成的磁盘 IO**，新主机无法知道它们是否已下发/完成，且备机侧没有对应的完成通知（会导致 guest 触发 abort/reset）——不选择返回错误（guest 可能处理不好本地盘错误），而是在 go-live 时**重新下发这些 pending IO**；因为已消除 IO 竞争、且每个 IO 明确指定内存与磁盘块，重发是**幂等**的。恢复冗余：接管后 VM 通知 vSphere 的集群服务，由其按资源用量挑选最佳主机，用 **FT VMotion** 创建新备机，通常**数分钟内**恢复冗余且不中断执行；不能把两 VM 放到同一台服务器上。

33. 🟡 FT VMotion 是什么？logging channel 上的缓冲与流控如何工作？为什么要限制备机的执行滞后（execution lag）？
   - 要点：启动备机需要从**任意状态**复制正在运行的主机且不明显打扰它，于是改造 VMotion：**克隆而非迁移**——在远端建立一份完全一致的运行副本、不销毁源 VM，同时建立 logging channel，源进入记录模式、目标进入重放模式；对主机的中断**不到 1 秒**。两端 hypervisor 各维护大的 **log buffer**：主机尽快把缓冲刷到通道，备机收到即读入并回 ack（ack 让主机知道被 Output Rule 延迟的输出何时可发）。备机日志读空就**暂停**，不影响客户端；主机缓冲写满也必须停，这是天然流控，但会让主机对外**无响应**，需尽量避免。滞后不能太大的原因：主机故障时备机要**追完所有已确认日志**才能 go live，故障切换时间 ≈ 检测时间 + 当前 lag，所以不希望 lag 超过 1 秒。做法：协议里附带实时 lag 信息（通常 **<100 ms**）；超过约 1 秒时通过调度器**给主机少几个百分点 CPU**，用缓慢的反馈环逐步找到能让备机跟上的 CPU 上限，追上后再逐步放开；这种减速很少见，仅在系统极度紧张时出现，性能数据已包含其代价。

34. 🟡 磁盘 IO 与网络 IO 各自给确定性重放带来了什么麻烦？VM-FT 分别怎么处理？
   - 要点：磁盘：IO 非阻塞可并行，访问同一磁盘位置或（因 DMA 直达 VM 内存）同一内存页的并发 IO 会造成非确定性——检测这类**罕见的 IO race**，在主/备上以同样方式**强制串行执行**；磁盘 IO 还可能与 guest 应用/OS 对同一内存块的访问竞争——可用页保护（访问未完成 IO 的目标页就 trap 并暂停），但改 MMU 保护很贵，改用 **bounce buffer**：读盘先读到临时缓冲，IO 完成投递时再拷入 guest 内存，写盘先拷到缓冲再写，未见明显性能损失。网络：vSphere 的优化让 hypervisor **异步更新虚拟网卡状态**（如直接更新接收环），这引入非确定性，因此 FT 下**禁用异步优化**，接收环更新改为 guest trap 到 hypervisor 记录后再应用，发送也走 trap。为了补偿性能：**聚簇（clustering）** 减少 trap/中断——高速流时一组包一次 trap（最好零 trap，随收包顺带发包）、一组包一次中断；缩短发送延迟——收发日志与 ack 在 **无线程上下文切换** 的延迟执行上下文（类似 Linux tasklet）里完成，主机入队待发包时立即调度日志刷出。

35. 🟡 共享磁盘与非共享磁盘两种配置各有什么权衡？备机"自己执行磁盘读"这一替代设计何时值得？
   - 要点：默认**共享盘**：磁盘被视为主/备之外的**外部世界**，故障切换后内容天然正确可用；只有主机真正写盘，且写盘作为对外输出**受 Output Rule 约束**。**非共享盘**：备机自己写自己的盘从而保持同步，磁盘属于各 VM 内部状态，写盘**不必延迟**；适用于共享存储不可达/太贵，或主备相距很远的 **long-distance FT**；代价是开启 FT 时要先显式同步两份盘，故障后可能失步、重启备机时要重新同步（FT VMotion 需同步运行态和磁盘态），且没有共享存储做脑裂仲裁，要靠第三方 tiebreaker 或多数派。默认备机**从不读盘**，读结果作为输入经 logging channel 发送；替代是备机自己读盘以大幅减少日志流量，但备机必须等物理读完成可能变慢；主机读成功而备机失败要**重试到成功**，主机读失败则要把目标内存内容经通道发给备机；共享盘下主机读后很快写同一位置时，**写必须延迟到备机完成那次读**。实测吞吐降 **1–4%**（Swingbench 约 4%，DVD Store 约 1%），日志带宽由 **12→3 Mbit/s、18→8 Mbit/s**，因此在通道带宽受限（如长距离）时值得。

36. 🟢 VM-FT 的性能开销与带宽需求大致是多少？为什么论文认为长距离容错可行，而 Remus 式检查点方案不行？
   - 要点：测试环境 8 核 Xeon 2.8 GHz/8 GB，10 Gbit/s 直连。真实应用 FT/非 FT 性能比：SPECJbb2005 **0.98**、内核编译 **0.95**、Oracle Swingbench **0.99**、MS-SQL DVD Store **0.94**——开销**低于 10%**；日志带宽 **1.5 / 3.0 / 12 / 18 Mbit/s**，即"典型 **<20 Mbit/s**"，1 Gbit/s 网络可承载多组 FT。guest 空闲时日志 **0.5–1.5 Mbit/s**（主要是定时器中断记录）；有负载时带宽由收到的网络包与读盘块主导。netperf：1 Gb 通道下接收从 940 降到 **604 Mbit/s**（所有入包都要进通道，通道成瓶颈），发送 855；10 Gb 通道接收 860、发送 935（发送数据不记日志，只记中断）；hypervisor 间 ping 1 Gb 约 150 µs、10 Gb 约 90 µs。长距离：主备相隔 **1–100 km** 的光纤可提供 100–1000 Mbit/s、延迟 <10 ms，对表 1 应用足够，但输出会被额外延迟**最多约 20 ms**，只适合能容忍该延迟的客户端；日志流可压缩。Remus 靠高频检查点（每秒 40 次）传内存增量，内核编译/SPECweb **慢 100%–225%**，1 Gbit/s 下难以达到合理性能；优点是同样适用于多处理器 VM。

### Lamport：分布式系统中的时间、时钟与事件排序（1978）

37. ☆ 🟢 给出 Lamport 的"happened before（→）"关系的定义。什么叫两个事件并发？为什么它只是偏序？
   - 要点：论文里"分布式"的定义：**消息传输延迟相对进程内事件间隔不可忽略**；每个进程是一个事件序列（先验全序），收发消息都是事件。**→ 是满足以下三条的最小关系**：(1) 同一进程内 a 先于 b 则 a→b；(2) a 是某进程发消息、b 是另一进程收到同一消息则 a→b；(3) 传递性。**a 与 b 并发** 当且仅当 a↛b 且 b↛a；假设 a↛a，故 → 是**非自反偏序**。直观含义：a→b 意味着 **a 可能因果影响 b**，并发则彼此都不可能影响；即使时空图上 q3 物理时间更早，P 在收到消息前也无法知道 Q 做了什么。定义有意**不依赖物理时钟**（规范应基于系统内可观察事件，真实时钟也不精确），并且只考虑**实际发送**的消息而非可能发送的（与狭义相对论的差别）。

38. ☆ 🟡 什么是逻辑时钟？Clock Condition、C1/C2 与实现规则 IR1/IR2 分别是什么？为什么 Clock Condition 的逆命题不成立？
   - 要点：时钟 Ci 只是给进程 Pi 的每个事件赋一个数 Ci(a)，可以是**没有计时机制的计数器**。**Clock Condition**：若 a→b 则 C(a)<C(b)。**逆命题不能要求**：否则并发事件必须同时发生——图 1 中 p2、p3 都与 q3 并发，将迫使 p2、p3 同时刻，与 p2→p3 矛盾。由 → 的定义，只要满足 **C1**（同进程内 a 先于 b ⇒ Ci(a)<Ci(b)）和 **C2**（发送事件时钟 < 接收事件时钟）即可；用"tick line"看：C1 要求同一进程两事件之间必有 tick 线，C2 要求每条消息线跨过 tick 线。实现规则：**IR1** 每个进程在相邻两事件间递增 Ci；**IR2** (a) 消息 m 携带时间戳 Tm=Ci(a)，(b) 收到 m 时把 Cj 设为**大于等于当前值且大于 Tm**。改变时钟本身不算事件。

39. 🟢 如何用逻辑时钟把偏序扩展成全序（⇒）？这个全序是唯一的吗？
   - 要点：按时间戳排序，**平局用任意事先约定的进程全序 < 打破**：a⇒b 当且仅当 Ci(a)<Cj(b)，或二者相等且 Pi<Pj；Clock Condition 保证 a→b ⇒ a⇒b，即 ⇒ 是 → 的一个全序完成。脚注给出更"公平"的做法：让优先级随时钟值变化（按 C(a) mod N 轮转）。**全序不唯一**：不同的合法时钟给出不同的 ⇒，且任何扩展 → 的全序都能由某个满足 Clock Condition 的时钟系统得到；**唯一由事件系统决定的只有偏序**。实现逻辑时钟的目的就是获得这样一个全序，用它可以实现分布式同步。

40. 🔴 描述论文里基于全序的分布式互斥算法：正确性条件、五条规则、依赖的假设，以及它如何推广为状态机方法；这一方法对故障的容忍如何？
   - 要点：条件：**(I)** 持有者必须先释放才能授予他人；**(II)** 请求按发出顺序授予；**(III)** 若每个获得者最终释放，则每个请求最终被授予。**中心调度不够**：P1 先向 P0 请求再给 P2 发消息，P2 收到后再请求，P2 的请求可能先到，违反 II。假设：任意两进程间消息 **按发送顺序到达** 且最终送达（可用消息编号和 ack 去掉），进程可直达所有其他进程；各进程维护自己的私有请求队列，初始含 T0:P0 requests。规则：(1) 请求时向所有人广播 Tm:Pi requests 并入本地队列；(2) 收到请求者入队并回**带时间戳的 ack**；(3) 释放时删除自己的请求并广播 releases；(4) 收到 releases 删除对应请求；(5) 当**自己的请求按 ⇒ 排在队列最前**，且**已收到每个其他进程时间戳晚于 Tm 的消息**时获得资源——两条件均本地可判定。证明：(ii)+有序到达保证已知所有更早请求 ⇒ I；⇒ 扩展 → ⇒ II；规则 2、3、4 保证最终性 ⇒ III。推广：把同步描述为**状态机（命令集 C、状态集 S、e:C×S→S）**，每个进程按时间戳顺序**独立模拟**同一命令序列，当已知所有其他进程 ≤T 的命令后执行 T 时刻命令。代价：需要**所有进程主动参与**，单个进程失效就使谁也无法继续执行命令，系统停摆；论文指出"失败"的概念**只在物理时间下才有意义**——没有物理时间无法区分崩溃与暂停。

41. 🟡 什么是"异常行为（anomalous behavior）"？Strong Clock Condition 为何逻辑时钟一般满足不了？有哪两种规避方法？
   - 要点：例子：某人在计算机 A 上发出请求 A，然后**打电话**让另一城市的朋友在计算机 B 上发请求 B，B 可能拿到更小的时间戳而被排在 A 之前——系统无法得知 A 先于 B，因为该先后来自**系统外部的消息**。形式化：令 𝒮 为系统事件集，扩大为含外部相关事件的集合，其 happened-before 记为 ⇢；任何只基于 𝒮 内事件、不与外部事件关联的算法都无法保证 A 排在 B 前。**Strong Clock Condition**：对扩大集合中的任意 a、b，a⇢b ⇒ C(a)<C(b)，比普通 Clock Condition 强，逻辑时钟一般不满足。两种办法：(1) 把顺序信息**显式带进系统**——用户拿到 TA，让朋友指定 B 的时间戳晚于 TA，由用户负责；(2) 构造满足 Strong Clock Condition 的时钟系统——独立运行的**物理时钟**恰好能做到（与相对论下的时空偏序一致）。

42. 🔴 Lamport 如何把逻辑时钟规则特化为物理时钟同步算法？PC1/PC2、μ、κ、ε 之间的约束是什么，同步误差上界是多少？
   - 要点：Ci(t) 连续可微（重置处除外），**PC1**：|dCi/dt − 1| < κ，κ≪1（石英钟约 **10⁻⁶**）；**PC2**：|Ci(t) − Cj(t)| < ε。令 μ 小于进程间**最短消息传输时间**（最保守取距离/光速），要避免异常行为需 Ci(t+μ) − Cj(t) > 0；假设时钟**只往前拨、永不回拨**（回拨会破坏 C1），由 PC1 得 Ci(t+μ) − Ci(t) > (1−κ)μ，再结合 PC2 得充分条件 **ε/(1−κ) ≤ μ**。算法：**IR1'** 不收消息时时钟以正速率连续运行；**IR2'** 发送带时间戳 Tm=Ci(t)，接收方设 Cj(t') = **max(Cj(t'−0), Tm + μm)**，μm 是已知的最小传输延迟，ξm = 实际延迟 − μm 为不可预测延迟。定理：强连通进程图直径 d，每 τ 秒每条弧上至少发一条不可预测延迟 < ξ 的消息，PC1 成立，则 t > t0 + τd 后 PC2 成立且 **ε ≈ d(2κτ + ξ)**（假设 μ+ξ ≪ τ）；证明中把消息看作以恒定速率运行的时钟，重置只是"把时钟设为等于另一个时钟"。附带结论：任一进程发起、经所有进程转发的一轮消息可在**不到 2d(μ+ξ) 秒**内完成初始同步或重新同步；"永不回拨"是与既往文献的区别。

### Lamport / Shostak / Pease：拜占庭将军问题（1982）

43. 🟢 用论文的语言陈述拜占庭将军问题：IC1、IC2 是什么？它是怎样从"n 个将军就 v(1)…v(n) 达成一致"归约来的？
   - 要点：可靠系统必须应对一种常被忽视的故障——组件向系统不同部分**发送相互矛盾的信息**。原始目标：**A.** 所有忠诚将军采用同一计划；**B.** 少数叛徒不能让忠诚将军采用坏计划。做法是每个将军 i 广播观察值 v(i)，大家用同一（且稳健的）方法合并，例如多数表决——少数叛徒只在忠诚者几乎对半分时才能左右结果，而那时哪种决定都不算坏。为此需要 **1'. 任意两个忠诚将军对 v(i) 使用相同值**，以及 **2. 若第 i 位将军忠诚，则所有忠诚将军使用他实际发送的值**。两者都只关于"一个将军把自己的值发给其他人"，于是归约为**司令向 n−1 名副官下达命令**：**IC1** 所有忠诚副官服从同一命令；**IC2** 若司令忠诚，每个忠诚副官服从他发的命令——称为 **interactive consistency** 条件；司令忠诚时 IC1 由 IC2 推出，但司令可能是叛徒。每位将军用该问题的解发送"以 v(i) 作为我的值"即可解决原问题。

44. ☆ 🔴 为什么口头消息下容忍 m 个叛徒至少需要 3m+1 个将军？请复述三将军不可解的论证、到一般 m 的归约，以及"近似一致同样难"的结论。
   - 要点：**口头消息**：内容完全受发送者控制，叛徒可发任意内容（对应计算机之间的普通消息）。三将军一叛徒：场景一司令忠诚发"attack"，副官 2 叛变告诉副官 1"他说 retreat"，由 IC2 副官 1 必须 attack；场景二司令叛变，给副官 1 发 attack、给副官 2 发 retreat——两场景对副官 1 **完全不可区分**，因此收到 attack 就必须 attack；对称地副官 2 收到 retreat 就必须 retreat，于是场景二违反 IC1。论文特别提醒这种非形式推理极易出错，严格证明见 Pease/Shostak/Lamport 1980。推广：反证，假设 ≤3m 个"阿尔巴尼亚将军"能容忍 m 个叛徒，让 3 个拜占庭将军**各模拟约三分之一**（司令模拟阿尔巴尼亚司令加至多 m−1 名副官，每名副官模拟至多 m 名），单个叛徒至多对应 m 个叛变的被模拟者，从而得到不可能存在的三将军解。**近似一致**（IC1' 忠诚副官攻击时间相差 ≤10 分钟；IC2' 与忠诚司令的时间相差 ≤10 分钟）同样需要 >2/3 忠诚：用 1:00 编码 attack、2:00 编码 retreat，≤1:10 攻、≥1:50 退、否则问另一副官并跟随其决定（无则退），即可构造三将军精确解，矛盾。

45. 🟡 描述口头消息算法 OM(m)：依赖哪三条假设、递归怎么展开、majority 函数要满足什么，正确性由哪两个结论保证，消息代价多大？
   - 要点：假设 **A1** 发出的消息都被正确送达；**A2** 接收者知道发送者是谁；**A3** 消息缺失可被检测——A1/A2 防止叛徒干扰他人通信或冒名，A3 挫败"不发消息"的叛徒；司令不发令时用默认 **RETREAT**。majority 只需满足"多数 vi 等于 v 则结果为 v"，可取多数值（无则 RETREAT）或**中位数**。**OM(0)**：司令发值，副官用收到的值或 RETREAT。**OM(m)**：(1) 司令向每个副官发值；(2) 每个副官 i 以收到的 vi 为司令，用 OM(m−1) 发给其他 n−2 人；(3) 副官 i 取 majority(v1…vn−1)。m=1、n=4 例子：副官 3 叛变发 x，副官 2 得 majority(v,v,x)=v；司令叛变发 x,y,z 时每人都得 majority(x,y,z)，仍一致。递归展开时每人向同一人发多条消息，需**在值前加副官编号前缀**去歧义。**Lemma 1**：>2k+m 将军、≤k 叛徒时 OM(m) 满足 IC2（归纳，n−1>2k 保证副官中多数忠诚）；**Theorem 1**：>3m 将军、≤m 叛徒时满足 IC1 与 IC2（司令叛变时副官中至多 m−1 叛徒且 3m−1>3(m−1)，两忠诚副官得到相同向量）。代价：消息路径长达 **m+1**（Fischer–Lynch 证明任何解都必须如此，故最优）、消息数达 **(n−1)(n−2)…(n−m−1)**。

46. 🟡 签名消息算法 SM(m) 增加了什么假设？算法如何运行，为什么三个将军就能容忍一个叛徒，又为什么对任意数量的叛徒都可解？
   - 要点：新增 **A4**：(a) 忠诚将军的签名不可伪造，篡改可被发现；(b) 任何人都能验证签名——对叛徒的签名不作假设，允许叛徒之间**串通伪造彼此签名**。choice 函数只需：单元素集合返回该元素、空集返回 RETREAT（可取中位数）。记 v:0:j1:…:jk 为逐层签名。每个副官维护**已收到的合法命令集合 Vi**（不是消息集合）：(1) 司令签名发送；(2A) 首次收到 v:0 则 Vi={v} 并把 v:0:i 发给其他副官；(2B) 收到 v:0:j1:…:jk 且 v∉Vi 则加入 Vi，若 **k<m** 则追加签名转发给未签名者；(3) 不再有消息时服从 **choice(Vi)**；已在 Vi 的命令一律忽略。终止判定：每个签名序列至多收到一条消息，可要求 jk 发"不再发送"声明，或用**超时**。三将军例子：叛变司令发 attack:0 给一人、retreat:0 给另一人，两人在步骤 2 都得到 {attack, retreat} 而**做同样选择**，且能**确认司令是叛徒**——两份不同命令都带他的签名。第 m 个签名多余，SM(1) 中副官不必签名。**Theorem 2**：任意 m，≤m 叛徒即可解。IC2：忠诚司令的 v:0 无法被伪造成 v':0，Vi 只含 v；IC1（司令叛变）：i 收到 k<m 层签名会转发给 j；k=m 时司令占一个叛徒名额，m 个签名者中**至少一人忠诚**，他首次收到时已转发给 j。重复使用时应附**序列号**，避免同一消息签两次。

47. 🔴 当将军之间不是完全连通时，OM 与 SM 各自需要什么连通性条件？论文给出的最弱可解条件是什么？
   - 要点：OM 的扩展需要 **regular set of neighbors**：节点 i 的 p 个邻居，且对任意其他节点 k 存在从各邻居到 k、不经过 i、除 k 外**两两无公共节点**的路径；图对每个节点都有 p 个这样的邻居即 **p-regular**。**OM(m,p)**：司令只发给正则邻居集 N 中的 p 名副官；m=1 时各副官沿互不相交的路径把值送给每个 k，m>1 时以移除司令后的图（仍 (p−1)-regular）递归 OM(m−1,p−1)；k 取 majority。**Lemma 2**：p ≥ 2k+m 且 ≤k 叛徒时满足 IC2（p ≥ 2k+1 条不相交路径中多数全由忠诚者组成）；**Theorem 3**：p ≥ 3m 时可解，即图需 **3m-regular**——这是很强的条件，若恰好 3m+1 人则等价于完全连通，退化为 OM(m)（Dolev 的后续算法要求更弱连通性）。SM 则只要求最弱条件：**忠诚将军构成的子图连通**——若司令到某副官的所有路径都要经叛徒中转，IC2 无法保证；两副官只能经叛徒互通则 IC1 无法保证。**Theorem 4**：≤m 叛徒、忠诚子图直径 d 时 **SM(m+d−1)**（只向邻居发送）可解——k<m 时 i 会转发、d−1 步内到达 j，k ≥ m 时前 m 个签名者中有忠诚者已向邻居转发；**推论**：忠诚子图连通时 **SM(n−2)** 对任意叛徒数可解（因 d < 忠诚者数，叛徒 < n−d，取 m=n−d−1）。即使子图不连通，经 ≤d 条全忠诚路径相连的两忠诚者也服从同一命令。

48. 🔴 把这些算法用于可靠计算机系统时，A1–A4 各自对应什么工程假设？为什么"多数表决 + 同一根线读输入"不够，为什么超时检测缺失消息需要同步时钟？
   - 要点：论文所知的唯一可靠化手段是**多处理器计算同一结果再多数表决**（芯片冗余或导弹防御的多站点，只是"处理器"大小不同）；表决前提是所有非故障处理器**使用同一输入**——但任一输入来自单一物理部件，故障部件可给不同处理器不同值，甚至非故障时钟在变化时被读到新旧两个值。多数表决可靠需要的两条件正是 **IC1/IC2**（司令=输入单元，副官=处理器，忠诚=非故障）。硬件捷径无效：同一根线可能传**边缘信号**，被有的处理器读成 0、有的读成 1；只有处理器间通信解决拜占庭问题才能保证一致，冗余输入（多部雷达）本身仍需一致性；取 majority/choice 为中位数时，得到的值落在输入单元给出的范围内。**A1**：通信线路故障对 OM 而言**等价于处理器故障**，只能保证总故障数 ≤m；SM 在"线路故障不会伪造签名"前提下对线路故障不敏感，Theorem 4 仍成立——断线只是降低连通性。**A2**：需要故障处理器不能冒充他人，实践上意味着**固定线路**而非交换网络（交换节点故障会再次引出拜占庭问题）；若全部签名则 A2 不必要。**A3**：只能靠超时检测缺失，需两条假设——消息生成+传输有**固定上限 μ**，且收发双方**时钟同步在 τ 内**；否则消息应在接收方时钟 T+μ+τ 前到达，超时即视为未发送（迟到者必为故障，不影响正确性）；SM(m) 中带 k 个签名的消息要等到 T0+k(μ+τ)。论文指出若算法只能在固定初始时刻、收到消息时或随机定时器触发时行动（无法构造同步时钟），那么**即使有传输延迟上限、即使叛徒只会"不发消息"**，问题也不可解；时钟会漂移，须周期重同步，而容错时钟同步本身与拜占庭问题同样难。**A4**：签名 Si(M) 是冗余信息，(a) 非故障者签名不可被伪造、(b) 人人可验证；(a) 无法绝对保证，只能把概率压到任意小——随机故障场景用"随机化"函数，如 **Si(M)=M·Ki mod P**（Ki 为随机奇数，P 为 2 的幂），伪造概率约 **1/P**；恶意智能场景则是密码学问题（Diffie–Hellman、RSA）。结论：任意故障下的可靠性**本质上昂贵**，降低成本的唯一办法是对故障类型作假设（如"只会停止、不会答错"），但极高可靠性要求时不能这么假设。

### Fox & Brewer：Harvest、Yield 与可扩展容错系统

49. ☆ 🟢 什么是 yield 和 harvest？为什么说这两个指标比"可用/不可用"更能描述大规模互联网服务的正确行为？
   - 要点：假设客户端向服务器发查询，正确行为至少有两个度量：**yield（产出率）= 完成一个请求的概率**，是常用指标，以"几个 9"衡量（四个 9 = 完成概率 0.9999，好的 HA 系统追求四到五个 9）；**harvest（收获率）= 响应中反映的数据比例**，即答案的完整度。故障下典型的权衡是：**不给答案（降低 yield）** 还是 **给不完整答案（保 yield、降 harvest）**。有的应用不容忍 harvest 退化——如只输出"存在/不存在"的二值传感器，任何偏离都使结果无用（脚注：这与半导体制造中 yield 的用法一致——每个晶粒不容忍退化，yield 是晶圆上良品比例）；有的则容忍优雅退化——如 **online aggregation** 让用户用运行时间换聚合查询的精度与置信度。看似只适用于查询，但对**单一位置更新**（局限于单个节点/分区的修改）同样适用：能到达的节点上更新正确完成但可见性受限（harvest 降低），需要不可达节点的更新失败（yield 降低），这些局部修改之所以一致恰恰因为新值并非处处可见；不适用于全局修改，但对个性化数据库、协同过滤足够有用。

50. ☆ 🟡 Fox 与 Brewer 如何表述 Strong CAP 原则？三个词各自的定义是什么？"Weak CAP"又指什么？
   - 要点：定义：**强一致性 = 单副本 ACID 一致性**，且假定系统支持更新（否则谈一致性无意义）；**高可用**通过冗余（如数据复制）实现，任一消费者总能到达**某个副本**即算高可用；**分区弹性（partition-resilience）** = 系统整体能在副本间网络分区下存活。**Strong CAP Principle：强一致、高可用、分区弹性，最多选两个**。用穷举实例勾勒证明：**CA 无 P**——提供分布式事务语义的数据库只能在服务器之间无分区时做到；**CP 无 A**——分区时 ACID 数据库的后续事务可能被阻塞直到分区愈合，以免引入合并冲突；**AP 无 C**——HTTP Web 缓存靠复制文档获得客户端–服务器分区弹性，但分区时无法验证过期副本的新鲜度。一般地，任何分布式数据库问题都可用 **基于过期的缓存得到 AP**，或 **副本 + 多数表决得到 PC**（少数派不可用）。现实中许多系统是"降低了一致性或可用性"：Bayou 的弱一致模型、Coda 明确选可用性而非强一致、lease 这类基于过期的一致性机制；由此提出尚未精确刻画的 **Weak CAP Principle**：对三者中任意两者作的保证越强，能对第三者作的保证就越弱。两种策略都建立在"放宽正确行为的定义、再利用 CAP 权衡提升可用性"之上；文末把形式化框架视为 Weak CAP 的构造性证明。

51. 🟡 解释策略一"用 harvest 换 yield——概率可用性"，并用 Inktomi 搜索引擎的例子说明随机放置与重点复制的作用。
   - 要点：**几乎所有系统本质上都是概率可用的**：即使单故障下 100% 可用，多重故障概率非零；互联网服务还依赖尽力而为的 Internet，因此可用性天然映射到概率方法，应直接面对它以理解并限制故障影响，这要求先决定"什么必须可用"与故障的预期性质。**Inktomi** 例子：节点故障移除相应比例的搜索数据库，**100 节点集群单节点故障使 harvest 下降 1%**（harvest 通常在更长区间上度量），多节点故障下 harvest **线性退化**；**随机放置**数据保证丢失的是随机 1%，让平均情况与最坏情况一致；**复制高优先级数据子集**降低丢失它们的概率，从而更精确地控制 harvest（既提高它也减小缺失数据的实际影响）；全量复制成本大而收益小，且因 Internet 尽力而为**永远无法保证 100% 的 harvest 或 yield**。运行机制上，**每节点超时约束使整体 yield 保持恒定**，代价是 harvest 概率性退化，从而几乎总能给出概率上足够好的答案（yield 仍不能是 100%）。同类例子：面向瘦客户端的**转换代理**按需降级结果以换取原本拿不到结果的客户端能得到响应；带宽受限时即使 100% harvest 有用，也可能宁愿用 harvest 换响应时间（智能降级为低带宽格式）。

52. 🔴 解释策略二"应用分解与正交机制"：分解的实际收益与潜在收益分别是什么？什么叫正交机制？用 SNS、MediaPad/SRM 及安全领域的例子说明，并给出作者最终总结的可复用机制。
   - 要点：有些大应用可分解为**各自不容忍 harvest 退化（只会以降低 yield 的方式失败）**的子系统，但它们的独立失败只让整体功能降级，于是整体变得容忍 harvest 退化。**实际收益**：可**分别**为每个子系统配置状态管理，只给需要的子系统强一致或持久状态；电商站点例：只读子系统（基于用户画像从静态语料生成内容）、事务子系统（计费）、会话期持久的购物车、真正持久但读多写少的个性化画像——除计费外任一失败都不致整站无用（画像挂了仍可浏览但无个性化，购物车挂了仍可逐件购买）。**潜在收益**来自正交机制：与分层机制不同，**正交机制独立于其他机制、与它们本质上没有运行时接口**（至多有配置接口）；依据 Brooks（复杂度随工程师数平方增长）与 Leveson（复杂系统多数故障源于组件间意外交互而非组件内 bug），得出"**机器越少越好（平方级）**"。**SNS**（cluster-based Scalable Network Server）提供高可用与增量扩展，但**不提供持久状态或一致性保证**，要求每个应用模块**可在几乎任意时刻重启**；这一约束使其能用**超时、重试、沙箱**等简单正交机制自动处理瞬时故障与负载不均。仍能部署群组状态应用 **MediaPad**（PalmPilot 参与共享白板的适配代理）：底层 **SRM** 中没有硬拷贝的群组/会话状态，各对等体维护**软状态**并靠组播修复机制协同维护，崩溃恢复即刷新软状态——与可重启约束兼容，且 SNS 未为它改动任何接口，状态维护对 SNS 正交。正交组合把有害交互的检查从**运行时移到编译期**，正交守卫机制改善运行时的故障隔离，应用作者无需自己处理复制/负载管理/高可用。既有例子：StackGuard、系统调用监控、软件故障隔离等沙箱（正交安全）；**SSL** 先带外握手建立安全通道再承载任意流（正交隐私与完整性）；适合给遗留应用添加安全/健壮性；安全关键领域的反例——**Therac-25** 去掉机械联锁后暴露软件竞争导致患者死亡，支持"状态空间小的简单失效安全机制"。总结的机制：状态空间小、易推理的简单机制（基于超时的部分故障处理、守卫定时器、正交安全）；把这些机制与应用逻辑正交化（SNS+SRM 为例）；**用可刷新的软状态替代硬状态**，常带来"恢复代码即主线代码"的副作用（SNS 负载均衡管理器即如此，借鉴 IP 组播路由与 SRM 状态修复）；硬件复制与冗余下的大规模工程可处理性（只有 Teradata 768 节点集群这类昂贵专用系统在规模上可比）。目标是一套从 ACID 到 BASE 的大规模健壮应用设计指南。

## 三、大规模存储与计算：GFS / MapReduce / Codd 关系模型 / 客户端缓存一致性（25 题）

### GFS（The Google File System, SOSP 2003）

53. ☆ 🟢 GFS 基于哪些工作负载假设做设计？它的基本架构由哪几类角色组成？
   - 要点：四条核心假设——**组件故障是常态而非例外**（成百上千台商用机器，必须内建监控、容错、自动恢复）；**文件巨大**（多 GB 常见，预期几百万个 100 MB 以上的文件，小文件支持但不优化）；**以追加（append）为主而非覆写**，随机写几乎不存在，写后多为顺序读；**高持续带宽比低延迟更重要**。读负载是大顺序读（数百 KB~1 MB+）加小随机读。架构：**单个 master + 多个 chunkserver + 客户端**，均为运行用户态进程的商用 Linux 机器。文件切成固定大小 chunk，每个 chunk 由 master 在创建时分配的**不可变、全局唯一的 64 位 chunk handle** 标识；chunk 在 chunkserver 上以普通 Linux 文件保存，默认 **3 副本**，可按命名空间区域设不同副本数。**客户端和 chunkserver 都不缓存文件数据**（流式读工作集太大，且省去缓存一致性问题；chunkserver 依赖 Linux buffer cache），客户端只缓存元数据。不提供 POSIX API，额外提供 **snapshot 与 record append** 两个操作。

54. ☆ 🟡 GFS 为什么把 chunk 大小选为 64 MB？这个选择有什么代价，实践中如何处理？
   - 要点：64 MB 远大于传统文件系统块大小。**优点**：(1) 减少客户端与 master 的交互——同一 chunk 上的读写只需向 master 查一次位置，顺序读写大文件时收益尤其大，客户端甚至能缓存多 TB 工作集的全部位置信息；(2) 客户端更可能在同一 chunk 上做多次操作，可**保持持久 TCP 连接**降低网络开销；(3) **减少 master 上的元数据量**，使元数据可以全部放内存（每个 64 MB chunk 不到 64 字节元数据）。**惰性空间分配（lazy allocation）** 避免内部碎片，这本是对大 chunk 的最大反对理由。**缺点**：小文件可能只有一个 chunk，多客户端同时访问时该 chunkserver 成为**热点**。真实案例：批处理系统把可执行文件以单 chunk 文件写入 GFS，然后在数百台机器同时启动，存该文件的少数 chunkserver 被压垮；修复办法是**给此类文件设更高副本数**并让批处理系统**错开启动时间**，长期方案是允许客户端从其他客户端读数据。

55. ☆ 🟡 GFS 的单 master 负责什么、不负责什么？它保存哪三类元数据，为什么 chunk 位置不做持久化？
   - 要点：master 维护**全部元数据**：命名空间、访问控制、文件到 chunk 的映射、每个 chunk 副本的当前位置；并负责系统级活动：**chunk lease 管理、孤儿 chunk 的垃圾回收、chunk 在 chunkserver 间迁移**，通过周期性 **HeartBeat** 向 chunkserver 下发指令并收集状态。master **不参与数据路径**：客户端只向 master 要"该找哪些 chunkserver"，随后直接与 chunkserver 交互，并把（文件名, chunk index）→（chunk handle, 副本位置）缓存一段时间；master 还会顺带返回后续 chunk 的信息以减少交互。所有元数据放内存，因此周期性全量扫描（GC、再复制、迁移）很便宜。前两类（命名空间、映射）通过**操作日志**持久化并复制到远程机器；**chunk 位置不持久化**，master 启动时和 chunkserver 加入时向其轮询。理由：chunkserver 对自己磁盘上有哪些 chunk 拥有"最终发言权"（磁盘坏掉 chunk 会自行消失、运维可能重命名机器），在有数百台机器的集群中加入/离开/重启太频繁，试图在 master 上维护一致视图没有意义；作者最初尝试过持久化，后来放弃。实测 master 负载约 **200–500 ops/s**，不是瓶颈；早期版本曾因顺序扫描大目录成为瓶颈，改为可二分查找的命名空间结构后解决。

56. ☆ 🔴 GFS 的操作日志（operation log）为什么被称为"GFS 的核心"？master 如何用它和 checkpoint 保证元数据可靠且快速恢复？
   - 要点：操作日志是**元数据唯一的持久记录**，同时是定义并发操作顺序的**逻辑时间线**——文件、chunk 及其版本都由创建时的逻辑时间唯一且永久标识。可靠性规则：日志**复制到多台远程机器**，master **只有在日志记录本地和远程都刷盘之后才响应客户端**，否则即使 chunk 还在也会丢失整个文件系统或最近的操作；为降低刷盘和复制开销，master **批量刷多条日志记录**。恢复靠**重放日志**；为控制日志长度，日志超过阈值时做 **checkpoint**，其格式是**类 B 树的紧凑结构，可直接 mmap 进内存用于命名空间查找而无需解析**。构建 checkpoint 时 master **切换到新日志文件并在单独线程中生成**，不阻塞新的变更；几百万文件的集群约一分钟完成，完成后写到本地和远程。恢复只需**最新完整 checkpoint + 之后的日志文件**；旧的可删（保留几份防灾难）；checkpoint 途中失败不影响正确性，因为恢复代码会检测并跳过不完整的 checkpoint。

57. ☆ 🟡 描述 GFS 中 lease 的作用和一次写操作的完整控制流，以及数据流为什么与控制流分离。
   - 要点：每次变更（mutation）要应用到 chunk 的所有副本；master 把 **chunk lease 授予某个副本作为 primary**，primary 为该 chunk 的所有变更选定**串行顺序**，其他副本照此顺序应用。全局变更顺序 = master 的 lease 授予顺序 + lease 内 primary 分配的序列号。lease 初始超时 **60 秒**，chunk 持续被写时 primary 可无限续期，续期请求捎带在 HeartBeat 中；master 可提前撤销 lease（如重命名文件时），与 primary 失联时也可等 lease 过期后安全地授予新副本。写流程七步：(1) 客户端问 master 谁持有 lease 及其他副本位置（无 lease 则 master 授予）；(2) master 回复 primary 身份与 secondary 位置，客户端缓存；(3) **客户端把数据以任意顺序推到所有副本**，chunkserver 存在内部 LRU 缓冲区；(4) 所有副本确认后客户端向 primary 发写请求，primary 分配**连续序列号**并本地应用；(5) primary 把写请求转发给所有 secondary，按同一序列号顺序应用；(6) secondary 回复 primary；(7) primary 回复客户端，任何副本的错误都上报。出错时写可能在 primary 和部分 secondary 成功，区域进入**不一致**状态，客户端代码重试 (3)–(7) 数次后再从头重试。**数据流与控制流分离**的理由：控制流走客户端→primary→secondary，而数据沿**精心选择的 chunkserver 链线性、流水线式推送**（不是树形），以用满每台机器的出口带宽；每台机器转发给拓扑上"最近"的未收到者（距离可由 IP 估算），避免交换机间链路瓶颈；chunkserver 收到部分数据即开始转发。理想传输时间 **B/T + RL**，100 Mbps 链路下 1 MB 约 80 ms 分发完毕。跨 chunk 边界的大写会被客户端拆成多个写，可能与其他客户端交错覆盖，导致"一致但未定义"。

58. ☆ 🔴 解释 GFS 一致性模型中的 consistent / defined / undefined / inconsistent，四种情形（串行写、并发写、record append、失败）分别处于什么状态，GFS 靠什么机制达成，应用又如何配合？
   - 要点：**命名空间变更（如建文件）是原子的**，由 master 用命名空间锁独占处理，操作日志定义全局全序。文件区域 **consistent** = 所有客户端无论读哪个副本都看到相同数据；**defined** = consistent 且客户端能完整看到该变更写入的内容。表 1：**串行成功写 → defined**；**并发成功写 → consistent but undefined**（各副本相同但可能是多个变更的碎片混合）；**失败变更 → inconsistent（因而也 undefined）**，不同客户端可能在不同时刻看到不同数据；**record append → defined 但夹杂 inconsistent 区域**（填充 padding 或重复记录）。保证机制：(a) 在所有副本上以**相同顺序**应用变更；(b) 用 **chunk 版本号**识别因 chunkserver 宕机错过变更的**过期副本**，过期副本不会参与变更、不会返回给客户端，并尽早被 GC。由于客户端缓存位置，可能在缓存过期前读到过期副本，窗口受**缓存超时和下一次 open**限制；文件多为追加，过期副本通常返回"过早的 chunk 结尾"而非旧数据。应用侧配合三招：**只追加不覆写**、**checkpoint**（写完后原子重命名或周期记录已写多少，可带应用级校验和，读者只处理到最后一个 checkpoint）、**自校验、自标识的记录**（用校验和丢弃 padding 与碎片，用唯一 ID 过滤重复）。长期看组件故障仍可能损坏数据：通过握手发现故障 chunkserver、校验和发现损坏，几分钟内从有效副本恢复；只有所有副本在 GFS 反应前全部丢失才会不可逆丢失，此时表现为**不可用而非损坏**。

59. ☆ 🔴 GFS record append 的语义是什么？为什么会出现重复记录和 padding，为什么"至少一次原子追加"能成立？
   - 要点：传统写由客户端指定偏移，并发写同一区域不可串行化；record append 中**客户端只给数据，GFS 以原子方式（一段连续字节）至少追加一次，偏移由 GFS 决定并返回**，类似 Unix O_APPEND 但没有多写者竞争。用途：多生产者/单消费者队列、多路合并结果；否则需要分布式锁管理器之类昂贵同步。流程与普通写相同，只在 primary 上多一点逻辑：客户端把数据推到文件**最后一个 chunk** 的所有副本后向 primary 发请求；primary 检查追加后是否超过 **64 MB**，若超过则**把当前 chunk 填充到最大值**、让 secondary 照做，并回复客户端**在下一个 chunk 重试**；record 大小限制为 **chunk 的 1/4** 以控制最坏碎片率。若在任一副本失败，客户端重试，因此**同一 chunk 的各副本可能包含不同数据、含整条或部分重复记录**——GFS **不保证副本逐字节相同**，只保证数据作为原子单元至少写入一次。成立理由：操作报告成功意味着数据已在**某个 chunk 的所有副本的同一偏移**写入；此后所有副本长度都至少到该记录末尾，即使换了 primary，后续记录也只会拿到更高偏移或另一个 chunk。成功追加的区域是 defined，中间区域是 inconsistent，由应用按 2.7.2 的方法处理。性能上 append 吞吐受**存放最后一个 chunk 的 chunkserver 网络带宽**限制，与客户端数无关（1 客户端 6.0 MB/s，16 客户端 4.8 MB/s）。

60. ☆ 🟡 GFS 如何决定副本放在哪里？再复制（re-replication）的触发条件和优先级是什么，如何避免克隆流量压垮客户端流量？
   - 要点：集群跨多机架，机架间流量经交换机且机架出入带宽可能小于机架内总带宽。放置策略两目标：**最大化可靠性/可用性**与**最大化网络带宽利用**。仅跨机器分布只能防单机/单盘故障，还必须**跨机架分布**：整机架（共享交换机、电源）故障时仍有副本存活，读流量可利用多机架聚合带宽；代价是**写流量必须跨机架**，作者主动接受。副本产生的三种场景：创建、再复制、重平衡。**创建**时考虑：放到磁盘利用率低于平均的 chunkserver；限制每台的"最近创建数"（创建预示即将有大量写，且追加一次读多次的负载写完后基本只读）；跨机架。**再复制**在可用副本数低于用户目标时立即触发（chunkserver 不可用、报告损坏、磁盘出错被禁用、目标副本数上调），优先级：离目标越远越优先（丢两个副本比丢一个优先）、**活文件优先于近期删除的文件**、**阻塞客户端进度的 chunk 优先**。master 挑最高优先级 chunk，让某 chunkserver 直接从有效副本"克隆"。限流：master **限制集群和每台 chunkserver 的活跃克隆数**，每台 chunkserver **限制单个克隆操作向源读取的带宽**。**重平衡**周期性移动副本以均衡磁盘和负载，新 chunkserver 逐步填满而非瞬间灌满；删除副本时优先删空闲空间低于平均的机器上的。实测：杀掉一台约 15,000 chunk / 600 GB 的 chunkserver，限 91 个并发克隆、每个 ≤ 6.25 MB/s，**23.2 分钟**全部恢复，有效复制速率 440 MB/s；杀两台使 266 个 chunk 只剩单副本，这些 chunk 高优先级克隆，**2 分钟内**恢复到至少 2 副本。

61. ☆ 🟡 GFS 为什么用惰性垃圾回收而不是删除时立即回收？机制是什么？过期副本（stale replica）又如何被检测？
   - 要点：机制：应用删文件时 master **立即记日志**，但只是把文件**重命名为带删除时间戳的隐藏名**；master 常规扫描命名空间时，删除存在超过 **3 天**（可配置）的隐藏文件，此前可用隐藏名读取或改名回来"反删除"。隐藏文件被移除后内存元数据被清，与 chunk 的关联断开；随后对 chunk 命名空间的扫描找出**不被任何文件引用的孤儿 chunk**并删其元数据。每次 HeartBeat 中 chunkserver 汇报自己的一部分 chunk，master 回复其中已不在元数据里的 chunk，chunkserver 可自行删除。这里分布式 GC 很简单：所有引用都在 master 的文件→chunk 映射里，所有副本都是各 chunkserver 指定目录下的 Linux 文件，master 不认识的副本就是垃圾。**优点**：(1) 在故障常态化的系统中简单可靠——chunk 创建可能部分成功留下 master 不知道的副本，删除消息可能丢失需要跨故障重发，GC 提供统一兜底；(2) 并入 master 常规后台扫描与握手，**批量摊销**且只在 master 空闲时做；(3) 延迟回收是**误删的安全网**。**缺点**：存储紧张时不能立即复用空间；应对：**再次显式删除可加速回收**，并允许按命名空间区域配置不同副本/回收策略（如某目录不复制、删除即刻不可逆移除）。**过期副本检测**：master 为每个 chunk 维护**版本号**，每次授予新 lease 时递增并通知最新副本，master 与副本都持久记录后才通知客户端；宕机的副本版本不会推进，重启汇报时被识别为过期；若 master 看到比自己记录更高的版本，认为自己在授予 lease 时失败，采用更高版本。过期副本在 GC 中删除，之前对客户端视为不存在；master 向客户端和克隆操作下发版本号，读写时校验。

62. 🟢 GFS 如何检测磁盘导致的静默数据损坏？为什么不能靠副本间比对？
   - 要点：数千块盘的集群常出现读写路径上的损坏（论文第 7 节：IDE 驱动协议版本不匹配导致内核静默损坏数据，这直接促成了校验和的引入）。不能靠跨 chunkserver 比对副本：一是不现实，二是**副本合法地可以不同**（record append 不保证副本一致），所以每个 chunkserver 必须**独立校验自己的副本**。chunk 切成 **64 KB 块，每块 32 位校验和**，校验和作为元数据放内存并以日志持久化，与用户数据分离。**读**时先校验覆盖范围内的块再返回，因而不会把损坏传播给其他机器；不匹配则向请求方返错并向 master 报告，请求方改读其他副本，master 从别的副本克隆后让该 chunkserver 删除损坏副本。对读性能影响小：读通常跨多块、客户端尽量按校验块边界对齐、校验查找无 I/O 且可与 I/O 重叠。**追加写**的校验计算高度优化：只增量更新最后一个部分块的校验和并为新块计算，即使末块已损坏未被发现，新校验和也不会与数据匹配，下次读时会暴露；**覆写**则必须先读并校验范围首尾块再写再算新校验和，否则新校验和可能掩盖未覆盖区域的既有损坏。空闲时 chunkserver **扫描不活跃 chunk**，防止很少被读的损坏副本让 master 误以为副本充足。chunkserver 上的元数据（数十 GB）主要就是这些校验和。

63. ☆ 🔴 GFS master 故障时如何恢复？shadow master 是什么，它和 primary master 的关系是"镜像"吗？
   - 要点：高可用靠两条：**快速恢复**与**复制**。master 和 chunkserver 都设计为无论如何终止都能在**秒级**恢复状态并启动，不区分正常/异常终止，常规关机就是杀进程；客户端和其他服务器只经历短暂超时、重连、重试。master 状态复制：**操作日志和 checkpoint 复制到多台机器**，变更**只有在日志记录在本地和所有 master 副本上都刷盘后才算提交**。为简单起见仍由**一个 master 进程负责所有变更和后台活动**；进程挂掉可几乎瞬间重启；机器或磁盘坏掉时由 **GFS 之外的监控基础设施**用复制的操作日志在别处启动新 master，客户端只使用 master 的**规范名（DNS 别名，如 gfs-test）**，迁移时改别名即可。**shadow master** 在 primary 宕机时提供**只读访问**；它是"影子"而非"镜像"——可能**滞后 primary 零点几秒**，适合不在活跃修改中的文件或能容忍略旧结果的应用。由于文件内容从 chunkserver 读，应用不会读到过期文件内容，可能过期的只是目录内容、访问控制等元数据。shadow master 通过**读取操作日志的副本并按相同顺序应用**来保持同步，启动时同样轮询 chunkserver 并与之握手；只在 primary 创建/删除副本导致的位置更新上依赖 primary。恢复用时：单个服务器只有 50–100 MB 元数据，几秒读完即可应答，但 master 在拉取所有 chunk 位置前的 **30–60 秒**内能力受限。相关工作中作者指出：由于更新以追加 write-ahead log 持久化，未来可采用 Harp 式 primary-copy 方案获得更强一致性。

### MapReduce（OSDI 2004）

64. ☆ 🟢 描述 MapReduce 的编程模型和一次作业在 Google 实现中的执行流程（七步）。
   - 要点：用户写 **Map**（输入 k/v 对 → 中间 k/v 对列表）与 **Reduce**（中间 key + 该 key 的所有值 → 通常 0 或 1 个输出值），类型为 map (k1,v1)→list(k2,v2)，reduce (k2,list(v2))→list(v2)；中间值通过**迭代器**传给 reduce，以处理放不进内存的值列表。库负责切分输入、调度、故障处理、机器间通信，让**没有并行/分布式经验的程序员**也能用上大集群。执行流程：(1) 库把输入切成 **M 片（通常 16–64 MB）**，在集群上启动多份程序副本；(2) 一份是 **master**，其余是 worker，共 M 个 map 任务和 R 个 reduce 任务，master 挑空闲 worker 分配；(3) map worker 读对应分片，解析 k/v 交给用户 Map，中间结果**缓存在内存**；(4) 周期性写到**本地磁盘**，按分区函数分成 R 个区域，位置回报 master，由 master 转给 reduce worker；(5) reduce worker 收到通知后用 **RPC 远程读取** map worker 本地磁盘的数据，读完后**按中间 key 排序**（多个 key 落到同一 reduce 任务，必要时外部排序）；(6) 遍历排序数据，把每个 key 及其值集传给用户 Reduce，输出**追加到该分区的最终输出文件**；(7) 全部完成后 master 唤醒用户程序，MapReduce 调用返回。输出是 R 个文件，通常不合并，直接作为下一个 MapReduce 或其他分布式应用的输入。

65. ☆ 🟡 MapReduce master 维护哪些数据结构？M 和 R 应当如何取值，受什么约束？
   - 要点：master 为每个 map/reduce 任务记录**状态（idle / in-progress / completed）**和非空闲任务所在的 **worker 身份**。master 是中间文件位置从 map 传到 reduce 的**唯一管道**：对每个完成的 map 任务保存其产生的 **R 个中间文件区域的位置和大小**，map 完成时更新，并**增量推送**给正在执行 reduce 的 worker。任务粒度：理想情况下 **M 和 R 远大于 worker 机器数**，让每台机器做许多不同任务，既改善**动态负载均衡**，又加快故障恢复——故障机器已完成的大量 map 任务可摊到所有其他机器重做。上限：master 要做 **O(M+R) 次调度决策**并在内存保存 **O(M×R) 状态**（常数很小，每对 map/reduce 约 1 字节）；R 还受用户限制，因为每个 reduce 任务输出一个文件。实践：M 取到每个任务约 **16–64 MB 输入**（使本地性优化最有效），R 取 worker 数的一个小倍数；常见配置 **M = 200,000、R = 5,000，2,000 台 worker**。

66. ☆ 🔴 MapReduce 如何处理 worker 故障与 master 故障？在有故障重执行时，如何保证输出等价于无故障的顺序执行？
   - 要点：**worker 故障**：master 周期性 ping worker，超时无响应即标记失败；该 worker **已完成的 map 任务重置为 idle** 重新调度，因为其输出在故障机器的本地磁盘上不可访问；**已完成的 reduce 任务不必重做**，输出在全局文件系统。map 任务先由 A 执行后改由 B 执行时，所有 reduce worker 都被通知，尚未从 A 读取的改从 B 读。案例：网络维护使每次 80 台机器不可达数分钟，master 重执行其工作并继续推进直至完成。**master 故障**：可以周期性 checkpoint master 数据结构以便从上次 checkpoint 重启，但因为只有一个 master，其故障概率低，**当前实现直接中止计算**，客户端可自行检测并重试。**故障语义**：当 map/reduce 是**确定性函数**时，分布式执行输出等于无故障顺序执行。依赖 **map/reduce 任务输出的原子提交**：每个进行中任务写**私有临时文件**（reduce 一个，map R 个）；map 完成时把 R 个临时文件名发给 master，master 对**已完成任务的重复完成消息直接忽略**，否则记录文件名；reduce 完成时**原子重命名**临时文件为最终文件，同一 reduce 任务在多台机器执行时会有多次 rename，依赖底层文件系统的原子 rename 保证最终只含一次执行的数据。**非确定性**算子只有较弱语义：某个 reduce 任务 R1 的输出等于某次顺序执行的结果，但另一个 R2 的输出可能对应另一次顺序执行——因为 e(R1) 和 e(R2) 可能读了 map 任务 M 的不同执行的输出。副作用文件由应用自己保证原子且幂等（写临时文件再原子重命名），库不提供多输出文件的两阶段提交。

67. ☆ 🟡 MapReduce 的本地性（locality）优化是什么？它依赖 GFS 的哪些特性？
   - 要点：在其环境中**网络带宽是相对稀缺资源**（机器级 100 Mbps 或 1 Gbps，整体二分带宽平均远低于此）。输入数据由 **GFS** 管理，存在组成集群的机器的本地磁盘上：GFS 把每个文件切成 **64 MB 块**，每块通常 **3 副本**在不同机器。master 调度时考虑输入文件的位置信息，**尽量把 map 任务放到持有对应输入副本的机器上**；不行则放到副本"附近"（如同一网络交换机下的 worker）。在集群大部分 worker 上跑大作业时，**大多数输入数据从本地读取，不消耗网络带宽**。这解释了排序基准里输入速率高于 shuffle 和输出速率。灵感来自 active disks（把计算推到靠近磁盘的处理单元）。结论部分再次强调：本地性优化让数据从本地磁盘读，而**中间数据只在本地磁盘写一份**也是省网络带宽的措施。

68. ☆ 🟡 什么是 straggler？MapReduce 的 backup task 机制如何缓解，效果如何？
   - 要点：straggler 是在计算最后阶段**异常缓慢地完成最后几个 map 或 reduce 任务**的机器，会拉长整体时间。成因举例：坏盘频繁可纠正错误使读速从 **30 MB/s 降到 1 MB/s**；集群调度系统在同机安排了其他任务导致 CPU、内存、磁盘、网络竞争；一次机器初始化代码 bug 关闭了处理器缓存，受影响机器**慢 100 倍以上**。机制：当作业**接近完成**时，master 为**剩余进行中的任务调度备份执行**，主执行或备份执行**任一完成即标记任务完成**。经调优后通常只多消耗**不超过几个百分点**的计算资源，却显著缩短大作业时间：排序程序关闭备份任务后耗时增加 **44%**（1283 秒 vs 891 秒，最后 5 个 reduce 任务拖了 300 秒）。相关工作指出这类似 Charlotte 的 eager scheduling，而 eager scheduling 遇到反复失败的任务会导致整个计算无法完成，MapReduce 用**跳过坏记录**机制修补部分情形。计数器聚合时 master 会**剔除同一任务重复执行的影响**以免重复计数（重复来自备份任务和故障重执行）。

69. ☆ 🟡 Combiner 函数解决什么问题？它和 Reduce 有什么区别？分区函数和排序保证分别是什么？
   - 要点：**Combiner**：某些情况下每个 map 任务产生大量重复中间 key，且 Reduce **满足交换律和结合律**（如词频统计，词频符合 Zipf 分布，每个 map 会产出成百上千条 <the, 1>），全部经网络送到单个 reduce 再相加很浪费；用户可指定可选的 Combiner 在数据**发送前做部分合并**。Combiner 在**每台执行 map 任务的机器上**执行，通常与 reduce 用**同一份代码**；唯一区别是库如何处理输出——**reduce 的输出写最终输出文件，combiner 的输出写到将发给 reduce 任务的中间文件**。附录示例用 `set_combiner_class("Adder")` 启用。**分区函数**：用户指定 R，默认 **hash(key) mod R**，分区相当均衡；需要时可自定义，如 **hash(Hostname(urlkey)) mod R** 让同一主机的 URL 落到同一输出文件。**排序保证**：在给定分区内，中间 k/v 对**按 key 递增顺序处理**，便于生成每个分区有序的输出文件，支持按 key 高效随机查找或方便用户使用。分布式排序（Distributed Sort）示例正是依赖分区与排序保证。

70. ☆ 🟢 论文用 grep 和 sort 两个基准展示了什么？关键数字是什么？
   - 要点：集群约 **1800 台机器**，双 2 GHz Xeon（超线程）、4 GB 内存（约 1–1.5 GB 被其他任务占用）、两块 160 GB IDE 盘、千兆以太网，两级树形交换网络根部聚合带宽约 100–200 Gbps，任意两机 RTT 小于 1 ms，在周末下午空闲时运行。**Grep**：扫描 10^10 条 100 字节记录（约 1 TB）找一个罕见三字符模式（命中 92,337 条），M = 15000（约 64 MB 一片），R = 1；输入扫描速率随分配机器增加而上升，**1764 个 worker 时峰值超过 30 GB/s**，约 80 秒时降到 0，全程约 **150 秒**，其中约 **1 分钟是启动开销**（程序分发到所有 worker、与 GFS 交互打开 1000 个输入文件并获取本地性信息）。**Sort**：仿 TeraSort，排序 10^10 条 100 字节记录，不到 50 行用户代码，Map 提取 10 字节 key，Reduce 为恒等函数；M = 15000，R = 4000，分区函数内置 key 分布知识（通用程序需先跑一遍采样 MapReduce 计算分割点）；输出写为 **2 副本的 GFS 文件**（写出 2 TB）。输入速率峰值约 13 GB/s、200 秒内 map 全部完成（低于 grep 是因为 map 要花一半时间和 I/O 写中间结果到本地盘）；shuffle 在第一个 map 完成时即开始，第一批约 1700 个 reduce 任务（每机一次一个 reduce）、约 300 秒后开始第二批，约 600 秒 shuffle 完成；输出 2–4 GB/s，约 850 秒写完，总计 **891 秒**（当时 TeraSort 最好成绩 1057 秒）。输入速率 > shuffle 速率 > 输出速率，分别因本地性优化和输出写两副本。**杀掉 200/1746 个 worker 进程**的实验：输入速率出现负值（已完成 map 工作丢失需重做），总耗时 **933 秒**，仅比正常多 5%。2004 年 8 月统计：29,423 个作业，平均 634 秒，读 3,288 TB，平均每作业 157 台 worker、1.2 次 worker 死亡。

### Codd 关系模型（CACM 1970）

71. ☆ 🟢 Codd 所说的"关系（relation）"是什么？用数组表示关系时有哪五条性质？
   - 要点：关系取其**数学定义**：给定集合 S1, …, Sn（不必互异），R 是这些集合上的关系，若它是**n 元组的集合**，每个元组第 j 个元素来自 Sj；Sj 称为 R 的第 j 个**域（domain）**，n 为**度（degree）**，度 1/2/3/n 分别称一元/二元/三元/n 元。数组表示只是为方便说明，**不是关系视图的本质**。五条性质：(1) 每行是 R 的一个 n 元组；(2) **行的顺序无关紧要**；(3) **所有行互不相同**；(4) 列的顺序有意义，对应域的顺序；(5) 每列的含义部分由域名标注传达。两列可能有相同域名但意义不同（如 component(part, part, quantity) 表示零件装配关系，是零件展开问题的核心），当时 IMS/360 等树形文件系统无法表示这种有重复域的关系。为避免用户记忆域顺序（度为 30 的关系并不罕见），Codd 提出用户面对的是**域无序的"关系体（relationship）"**，重复域用**角色名（role name）**限定，如 sub.part 与 super.part。数据库全部数据可视为**随时间变化的关系集合**，会插入、删除、修改元组。

72. ☆ 🟡 什么是数据独立性（data independence）？Codd 指出当时系统有哪三类需要消除的数据依赖，为什么树/网络模型做不到？
   - 要点：数据独立性 = **应用程序和终端活动独立于数据类型的增长和数据表示的变化**。三类依赖：(1) **顺序依赖（ordering dependence）**——系统允许程序假定记录呈现顺序等于存储顺序（如按零件序号升序），一旦要换存储顺序程序就失效；当时所有商用系统都不区分"呈现顺序"和"存储顺序"。(2) **索引依赖（indexing dependence）**——索引从信息角度是**冗余**的、纯性能组件，随访问模式变化需要创建/销毁；IDS 中程序要按名引用索引链，链被删除程序就出错，而 TDMS/IMS 因索引由系统无条件提供才没有此问题。(3) **访问路径依赖（access path dependence）**——树/网络模型要求程序利用一组用户访问路径。例子：零件-项目数据可用 5 种树结构表示；一个不检测当前结构的程序 P 在某一种结构下正确，就会在**至少三种其他结构下失败**（引用不存在的文件，或漏掉包含所需信息的文件）；为所有可能结构都写检测不现实。"一旦定义访问路径就永不废弃"的策略也不可行，因为路径总数会过大。关系视图**只描述数据的自然结构，不叠加任何机器表示用的结构**，因而是高层数据语言和最大程度程序/表示独立的基础；它还能更清楚地评估现有系统的逻辑局限。

73. ☆ 🟡 什么是主键、外键与非简单域？Codd 的规范化（normal form）过程如何进行，前提条件是什么，好处是什么？
   - 要点：**主键（primary key）**：能唯一标识关系中每个元组的域或域组合；若是简单域或没有多余参与域的组合，则称**非冗余**主键；有多个非冗余主键时任选一个作为主键（如零件名唯一时零件名也可）。**外键（foreign key）**：R 中不是 R 主键、但其值是某关系 S 主键值的域（S 可以是 R 自身）；supply 关系中 (supplier, part, project) 组合是主键，三者各自是外键。因为外键可出现在任意关系中，过去把数据分成"实体描述"和"实体间关系"两部分的做法难以维持。**非简单域（nonsimple domain）**：元素不是原子值而是关系（如 employee 的 salary history 域，元素是 (date, salary) 二元关系），对应当时术语的 repeating group；简单域对应 attribute。**规范化**：从树顶关系开始，取其主键，**把该主键插入每个直接下级关系**，下级的新主键 = 原主键 + 从父关系复制来的主键；然后**从父关系中删去所有非简单域**，移除树顶，对每个子树重复。前提：(1) 非简单域的关联图是**一组树**；(2) **主键不含非简单域**；作者不知道有应用需要放宽这两个条件。好处：所有关系都能用二维列同质数组存储，也适合在**表示差异很大的系统之间传输批量数据**——传输格式**无指针、不依赖哈希寻址、无索引或排序列表**；一阶谓词演算足以作为规范形集合上的通用数据子语言。

74. ☆ 🔴 什么是"连接陷阱（connection trap）"？Codd 如何定义强冗余、弱冗余与一致性，并建议系统如何检测不一致？
   - 要点：**连接陷阱**：供应商描述用指针链到它供应的零件，零件再链到使用它的项目；由此得出"沿所有路径从供应商经零件走到项目，就能得到该供应商供应的全部项目"的结论**一般是错的**——只有当项目-供应商目标关系恰好**永远是**另两个关系的**自然复合（natural composition）**时才成立。原因是对关系复合理解不足：复合可能不止一种（多个 join 对应多个复合），路径跟随只给出自然复合。**可导出性**：R 从集合 S 可导出，指存在一系列产生唯一结果的操作（投影、自然连接、tie、限制；join 不合格因结果不唯一）**在所有时间**都能从 S 得到 R。**强冗余**：集合中某关系有一个投影可由其他关系的投影导出，如 employee(serial#, name, manager#, managername) 中 managername 多余；用等式表示。强冗余常为用户方便（保留半废弃关系让旧程序继续跑）而存在，管理员了解后可更自由地选存储表示；若直接反映到存储集则多耗空间和更新时间换取部分查询更快。**弱冗余**：不能用等式刻画，某投影不可由其他成员导出、但**始终是**其他投影某个连接的投影（条件 C 不恒成立时的 P, Q, R）；弱冗余源于用户群的逻辑需求，**管理员无法消除**，命名集和存储集中都会出现。**一致性**：给定时变关系集合 C、约束语句集 Z 与瞬时值 V，状态 (C, Z, V) 一致当且仅当 V 满足 Z；一致性是**瞬时状态的属性，与如何到达该状态无关**，不区分用户是因遗漏还是错误操作造成的不一致（例：向 P 插入 (2,5) 可能是尚未插入 Q、R 的正确输入，也可能是错误输入，系统不问环境无法判断）。检测方式两种：**每次插入/删除/键更新时检查**（会拖慢操作，不一致记录内部日志，超时未修复则通知用户或数据安全负责人）；或**每天一次或更低频的批处理检查**，配合记录所有状态变更事务的**日志（journal）**追踪来源——若非暂态不一致很少，后者更优。

### 客户端缓存一致性（Wilkinson & Neimat, VLDB 1990）

75. ☆ 🟡 论文提出的 cache locks 算法如何把缓存对象的状态映射到锁模式？envelope transaction 是什么，为什么需要它？
   - 要点：背景：客户端-服务器数据库中客户端缓存部分数据以减少消息往返，需要协议保证缓存与共享数据库一致；作者把"活动数据库问题"视为**并发控制同步的特例**——持有活动数据相当于持有锁，别人更新即"打破"锁，问题是如何通知锁持有者。做法是**把缓存一致性集成进服务器的锁管理器**：不需新模块、请求路径几乎不变长、对非缓存事务透明。假设服务器用 **2PL**，客户端事务有读阶段和提交阶段，**更新到提交时才发给服务器**。缓存对象相对服务器当前版本有四种状态：**正在复制中、与服务器一致、因未提交事务更新而过期、因已提交事务更新而过期**。第一种用常规 **S 锁**建模；其余三种新增三种锁模式：**C 锁（Cache lock）**表示持有者正在缓存该对象，**不阻塞其他事务**；其他事务请求 X 锁会"打破"C 锁并将其变为 **P 锁（Pending update）**；更新事务中止则 P 回到 C，提交则 P 变成 **O 锁（Out-of-date）**。加载时 envelope transaction 先持 S 锁保证装入一致快照，装完后请求服务器**把 S 锁降级为 C 锁**。**envelope transaction**：由于常规 2PL 在事务结束时丢弃锁，而客户端缓存应跨事务存活，因此引入一个**长期、只读、代表客户端缓存管理器**的事务，缓存创建时开始，负责从服务器装载对象并维护一致性，通常只持 C/P/O 锁，S 锁只短暂持有，因此不降低系统吞吐。用户事务对缓存对象**继承** envelope 的锁再升级为 S/X（不同于嵌套事务：父事务永不提交但子事务可提交）；采用**乐观策略**，缓存对象的加锁延迟到提交时随读写集一起请求。升级规则：读集中的 **P 锁可以提交**（利用缓存读的可重复性），写集中的 P 锁需**阻塞**直到变为 C 或 O，升级 **O 锁则中止事务**；服务器在响应中附带已变为 O 锁的对象标识，客户端标记为过期（作者为优化吞吐选择按需重载而非立即刷新），若在活动事务读写集中则中止该事务。假设客户端不缓存热点对象。

76. ☆ 🔴 notify locks 算法为什么需要消息序列号握手？它存在哪两个"暴露窗口"，分别如何处理？
   - 要点：notify locks 源自 Observer 系统用于共享未提交结果的机制，作者改造为在**更新提交时**向缓存了该对象的客户端发通知——这是既能防止注定中止的事务做无用功、又使消息数最少的时机，且只考虑已提交更新可利用缓存读的可重复性。客户端收到通知后**用服务器附带的新值直接刷新缓存**（更新刚提交，数据多在服务器内存中，这样减少 I/O 和消息，客户端永不需显式刷新请求），并检查更新对象是否在活动事务读写集中，是则中止。服务器收到提交请求时**假定客户端已正确执行一致性检查**。**第一个窗口**：通知是**异步**发送的，客户端判定可提交并发出提交请求后、服务器收到之前，服务器可能仍在发送会导致该事务中止的通知。处理：**每条服务器→客户端消息带序列号，客户端每个请求附带最近收到的序列号**；提交请求的序列号过低时，服务器拒绝并让客户端核实事务是否仍应提交后重发。**第二个窗口**：事务被服务器接受提交后、**延迟更新正在写入中央数据库期间**，其他事务可能使其读写集失效，因此**所有延迟更新写完后要再比对一次序列号**；核实期间服务器**不释放该事务的 X 锁**，以便返回后迅速提交。服务器算法：(1) 校验序列号；(2) 对写集逐个取标准 2PL 的 X 锁并写入更新（受常规阻塞和死锁约束）；(3) 再次比对序列号；(4) 释放锁并回复；(5) 若提交，对写集中每个对象所在的客户端发送带新值和新序列号的通知。两种算法都是**半乐观（semi-optimistic）**：缓存未命中或过期时走 2PL，缓存命中时不对最新缓存对象加锁，但事务可能在读阶段即被中止；正确性可用 Boral & Gold 结合 2PL 与乐观并发控制的框架证明。

77. ☆ 🔴 模拟实验中 cache locks 与 notify locks 相比 2PL 各表现如何？为什么 notify locks 会"灾难性"退化，而 cache locks"从不比 2PL 差"？
   - 要点：模型：封闭排队模拟（基于 Agrawal/Carey/Livny 模型扩展到一服务器多客户端带缓存），客户端资源无限、服务器 CPU 与磁盘有限，用多道程序度 **mpl** 间接控制冲突率；缓存内容固定（非 LRU），cache-hit-prob 为读集对象落到缓存的概率（cache locks 下不保证命中，因可能过期）。**第一组（cache size 15，int think 0）**：两种算法吞吐都随命中率上升；低命中率时 cache locks 几乎等于 2PL；notify locks 在**低 mpl 时表现突出**（缓存始终最新且很少被失效），高 mpl 时缓存频繁失效导致中止，退化比 cache locks 快。**缓存从 15 增到 60 个对象时两者收益反而明显下降**：命中率不随缓存大小变化，更大缓存只是更容易被随机更新失效；notify locks 在低命中率下付出大量通知消息却收益极少。根本差异：2PL 与 cache locks 是 **I/O bound**，而 notify locks 缓存总是最新、只为未命中和延迟更新发 I/O，因此是 **CPU bound**——任何增加通知消息的设置都会恶化它：缓存 60 时每次更新平均要发 **4 倍**于缓存 15 的通知消息，吞吐骤降**不是因为重试增多（重试和磁盘利用率反而下降）而是 CPU 饱和**。cache locks 的 CPU/磁盘利用率与 2PL 相近却吞吐更高，因为它把 I/O 从服务器卸载缩短响应时间；缓存变大时其重试数也下降，因为命中减少、行为更像 2PL。**第二组（int think 5s，纯数据竞争）**：吞吐先升后急剧下降，源于对象竞争而非 CPU/磁盘；命中率提高只带来温和提升，且 cache locks 超过 notify locks 的交叉点更早出现，因为 notify locks 命中更多、更乐观、重启更多。**第三组（mpl 25，变缓存客户端数）**：缓存 15 时增加缓存客户端提升总吞吐，notify locks 提升显著；缓存 60 时 notify locks 在缓存客户端超过 **50** 后因通知消息导致 CPU 饱和，到 190 时吞吐严重恶化；mpl 200 时因缓存太常失效，缓存客户端数量几乎无影响。结论：notify locks 某些条件下更优但**对 CPU 利用率和 mpl 极敏感**，而 DBMS 往往 CPU bound，采用它有风险；**cache locks 在所有条件下稳定，从不比非缓存 2PL 差**；应按当前条件选择算法。集成的额外代价：服务器为缓存客户端要维护更多锁（可用更粗粒度缓解），且两种算法都需要**逻辑（对象）锁**，可能要做锁管理器标识到缓存标识的转换。

---

## 四、系统与并发、协议与运行时：Reactor / AQS / 线程 vs 事件 / 事务策略 / HTTP/2 / REST / JVM 内存管理（34 题）

### Reactor 模式（Schmidt）

78. ☆ 🟢 Reactor 模式的意图（intent）是什么？它由哪几个参与者组成，各自职责是什么？
   - 要点：意图是处理**由多个客户端并发投递的服务请求**——每个服务由一个独立的 **Event Handler** 负责，**Initiation Dispatcher（初始化分发器）** 管理已注册的 handler 并做分发，**Synchronous Event Demultiplexer（同步事件多路分解器）** 负责多路分解；别名 **Dispatcher / Notifier**。参与者：**Handle**（OS 管理的资源：网络连接、打开的文件、定时器、同步对象；日志服务器里就是 socket 句柄）；**Synchronous Event Demultiplexer**（阻塞等待一组 handle 上出现事件，典型实现是 UNIX/Win32 的 **select**，返回时表示可以在某 handle 上**无阻塞地发起操作**）；**Initiation Dispatcher**（提供 `register_handler / remove_handler / handle_events` 接口，事件循环入口）；**Event Handler**（定义 hook 方法 `handle_event` 和 `get_handle` 的抽象接口）；**Concrete Event Handler**（例中的 **Logging Acceptor** 负责建连并创建 **Logging Handler**，后者接收并处理日志记录）。

79. ☆ 🟡 论文为什么认为 "thread-per-connection（每连接一线程）" 不是并发日志服务器的最佳方案？Reactor 要解决哪些 forces？
   - 要点：多线程方案的缺点——**效率**（上下文切换、同步、数据搬运带来的性能损失）、**编程复杂度**（需要复杂的并发控制）、**可移植性**（并非所有 OS 都有线程）。要解决的 forces：**可用性**（服务器等待某个事件源时不能无限阻塞而牺牲其它客户端的响应）、**效率**（最小化延迟、最大化吞吐、不浪费 CPU）、**编程简单**、**适应性**（新增服务/改消息格式/加缓存不应改动通用的多路分解与分发机制）、**可移植性**（移植到新 OS 代价小）。解决方案：把**同步多路分解与 handler 分发整合**，并把**应用特定的服务实现与通用分发机制解耦**——一个线程在 `select` 上等待，就绪后**同步回调** handler。Known Uses：InterViews 的 Dispatcher、ACE 框架、单线程 CORBA ORB（VisiBroker/Orbix/TAO）、Ericsson EOS 呼叫中心、Project Spectrum 医学影像。（面试常顺势追问 Nginx/Redis/Node 这类事件驱动服务器——原文并未提及，属延伸。）

80. 🟢 描述 Reactor 日志服务器处理"一次客户端连接"和"一条日志记录"的完整协作流程。
   - 要点：**建连场景**——服务器把 Logging Acceptor 注册为 **ACCEPT_EVENT** → 调 `handle_events()` 进入事件循环 → dispatcher 调 **select** 等待 → 客户端 connect → dispatcher 回调 Acceptor 的 `handle_event` → Acceptor 调 `accept()` 建立 SOCK_Stream → **new 一个 Logging Handler** → Handler 在构造函数里把自己的 socket 句柄注册为 **READ_EVENT**。**收记录场景**——客户端 send → OS 把记录排在 socket 上，dispatcher 通知对应 Handler → Handler **非阻塞 recv**（步骤 2、3 反复直到记录收全）→ 写到 **STDOUT** → 返回 dispatcher 的事件循环；收到 **CLOSE_EVENT** 时关闭流并 `delete this`。事件类型用**2 的幂位掩码**（ACCEPT=01, READ=02, WRITE=04, TIMEOUT=010, SIGNAL=020, CLOSE=040）便于按位或组合。dispatcher 用就绪的 handle 作为"key"定位 handler；dispatcher 通过 `get_handle()` 向 handler 索取 handle（"double dispatch"）。

81. 🟡 实现 Reactor 时有哪些设计选择：handler 是对象还是函数？单方法接口还是多方法接口？一个还是多个 dispatcher？
   - 要点：**对象 vs 函数**——对象便于继承复用、状态与方法聚合；函数免去定义子类；可用 **Adapter** 让对象持有函数指针同时支持两者。**单方法接口** `handle_event(Event_Type)`：可新增事件类型而不改接口，但鼓励子类里写 switch，限制扩展性；**多方法接口** `handle_accept/handle_input/handle_output/handle_timeout/handle_close`：可选择性覆盖、避免二次分解，但框架要**预先设定事件集合**（该接口针对 UNIX select，不够覆盖 Win32 **WaitForMultipleObjects** 的事件类型）。两者都是 hook method / Factory Callback 模式。**dispatcher 数量**：多数应用一个 **Singleton** 即可；但 Win32 的 select / WaitForMultipleObjects **单线程最多等 64 个 handle**，需多线程各跑一个 Reactor；handler **只在一个 Reactor 实例内串行化**，跨线程共享状态需额外同步。handler 表可用哈希、线性查找或直接索引（handle 为小连续整数时）。

82. ☆ 🔴 Reactor 的 liabilities（缺陷）有哪些？何时应改用 Proactor 或 Active Object？它与 Observer、Chain of Responsibility 的区别？
   - 要点：**适用受限**——只有 OS 支持 handle 时才高效；用"每 handle 一线程 + 队列"模拟会串行化所有 handler、增加同步与切换开销却不增加并行度。**非抢占**——单线程内 handler 执行不被抢占，因此 **handler 不能做阻塞 I/O**，否则阻塞整个进程、拖累其它客户端；长时操作（如传多 MB 医学影像）应用 **Active Object**（多线程/多进程与事件循环并行）。**难调试**——控制流在框架与回调间**振荡（inverted flow of control）**，像调试 LEX/YACC 生成的 DFA 骨架一样难单步。收益一并记住：关注点分离、模块化可复用可配置、可移植（select/poll/WaitForMultipleObjects 都可替换）、**粗粒度并发控制**（在 dispatcher 层串行化，常免去应用内加锁）。**Proactor** 是异步变体：由**异步操作完成**触发分发；Reactor 由"**可以无阻塞发起操作**"触发。**Observer**：单主题变化通知所有依赖者、通常单一事件源；Reactor 是多源事件分派给各自的 handler。**CoR**：沿链搜索第一个匹配 handler；Reactor 是 handler 与事件源**固定绑定**。Reactor 实现同时是事件多路分解的 **Facade**。

### java.util.concurrent 同步器框架 AQS（Doug Lea）

83. ☆ 🟢 AbstractQueuedSynchronizer 要协调的三个基本组件是什么？acquire / release 的基本形态？为什么状态只用 32 位 int？
   - 要点：三个组件：**原子管理同步状态**、**阻塞与唤醒线程**、**维护队列**。基本 acquire：`while(状态不允许){ 未入队则入队; 可能阻塞 }; 若曾入队则出队`；release：`更新状态; 若可能允许阻塞线程通过则唤醒一个或多个`。状态是**单个 32 位 int**，通过 `getState / setState / compareAndSetState` 访问，依赖 j.u.c.atomic 提供 **JSR133 volatile 语义**与原生 **CAS / LL-SC**。子类实现 **`tryAcquire`（成功返回 true）/ `tryRelease`（新状态可能允许后续 acquire 返回 true）**，int 参数可传递期望状态（如重入锁从条件等待返回时恢复递归计数）。只用 32 位是务实选择：**64 位 long 的原子操作在不少平台仍需内部锁模拟**，性能差；j.u.c 中只有 **CyclicBarrier** 需要更多位，因此它改用锁实现。支持**独占（exclusive）**与**共享（shared）**两种模式：`acquireShared` 的 `tryAcquireShared/tryReleaseShared` 通过返回值告知"还能继续 acquire"，从而**级联唤醒多个线程**。设计目标是**可扩展性**：在争用下开销保持常量，而非像内建锁优先优化零争用场景。

84. ☆ 🟡 AQS 为什么用 `LockSupport.park/unpark` 而不用 `Thread.suspend/resume`？park 的语义有哪些"坑"？
   - 要点：`suspend/resume` 有**无解的竞态**——若 resume 先于 suspend 执行，resume 无效。**park** 阻塞当前线程直到有 **unpark**（也允许**虚假唤醒**）。注意：unpark **不计数**——park 之前多次 unpark 只解除一次 park；且**按线程而非按同步器**记录，线程在新同步器上 park 可能因上次"**遗留的 unpark**"立即返回，但下一次没有 unpark 时会阻塞；论文认为显式清理不值得，**需要时多调几次 park 更便宜**，所以 park 必须放在重检状态的循环里。park 支持**相对/绝对超时**，并与 `Thread.interrupt` 集成——**中断会 unpark**。该机制类似 Solaris-9 线程库、Win32 "consumable events"、Linux NPTL，可高效映射（但当时 Hotspot 在 Solaris/Linux 上实际用 pthread condvar 实现）。

85. ☆ 🔴 AQS 的等待队列基于 CLH 锁的变体，它与经典 CLH 自旋锁有何不同？"signal 位"、`next` 链接、取消（cancellation）和 Condition 队列分别怎么处理？
   - 要点：选 **CLH 而非 MCS**，因为 CLH **更易适配取消与超时**；队列是**严格 FIFO**，不支持优先级。经典 CLH：`head/tail` 初始指向哑节点，入队用 `do{pred=tail}while(!tail.CAS(pred,node))`，**释放状态存在前驱节点**，自旋 `pred.status`；出队只需 `head=node`；优点是入队/出队快、lock-free、obstruction-free，判断有无等待者只需比较 head==tail。AQS 改动：(1) 阻塞同步器需要**显式 unpark 后继**，故加 **`next` 链**，但双向链表无法用 CAS 原子插入，`next` 只是插入后简单赋值的**优化路径**——发现 next 为空或已取消时**从 tail 沿 pred 反向遍历**确认；(2) 单个"released"位不够，线程只有 **`tryAcquire` 通过**才能返回，是否有资格尝试由"**前驱是否为 head**"决定，status 字段用于阻塞控制与取消；(3) **signal 位**：线程 park 前设置"signal me"位并**再检查一次**状态，释放方仅当 head 的 signal 位置位才清除并 unpark 后继，避免无谓的 park/unpark 及 Java/JVM/OS 边界开销，也免去释放方多数情况下遍历找后继；(4) **取消**：从 park 返回时检查中断/超时，取消线程设置节点状态并 unpark 后继以重设链接，可能有 **O(n)** 遍历，但因不再阻塞很快重新稳定；无取消时各步均摊 **O(1)**；(5) 节点回收**依赖 GC**，但出队时要**置空链接**避免不可回收；哑节点**首次争用时懒初始化**。**ConditionObject**：仅用于独占模式且实现 Lock 接口的同步器，每把锁可挂多个条件；节点与同步器共用但放在**单独的条件队列**（`nextWaiter`，持锁时可用顺序链表操作）；`await` = 入条件队列 → 释放锁 → 阻塞直到节点被转移到锁队列 → 重新获取锁；`signal` = **把条件队列首节点转移到锁队列（CLH 插入）**，不必立刻唤醒被 signal 的线程。取消与 signal 几乎同时发生时用 CAS 争夺节点的"已转移"位：signal 输了就转移下一个节点；取消输了要中止转移并等待锁重获，此处需**罕见的 spin + `Thread.yield`** 等 signal 方完成 CLH 插入；JSR133 规定：中断先于 signal → 重获锁后抛 InterruptedException，中断后于 signal → 正常返回但置中断标志。

86. 🔴 什么是 barging FIFO？它与"公平"模式如何权衡？论文的性能数据说明了什么？各 j.u.c 同步器如何用状态字段？
   - 要点：基本 acquire **先 `tryAcquire` 再入队**，新来线程可"**插队（barge）**"抢走本该给队头的访问；这减少了"**锁可用但无人持有**"（队头线程正在唤醒途中）的时间，且每次释放**只唤醒队头一个线程**，避免无效争用，因而总吞吐更高；公平性只是**概率性**的——若新线程到达比队头唤醒还快，队头几乎总是输。**严格公平**：`tryAcquire` 在当前线程不是队头时返回 false（用 `getFirstQueuedThread` 检查）；j.u.c 的 "fair" 模式采用更快的变体——**队列（瞬时）为空时也允许直接获取**。JLS 不提供调度保证，公平设置无绝对保证；多处理器上交错更多、公平设置影响更大。数据：**饱和（256 线程）时 barging-FIFO 锁开销比内建锁低约一个数量级、比 Fair 锁低约两个数量级**，Fair 锁性能完全由**上下文切换**决定；短持锁下公平性对方差影响小（4P 机器 Fair 0.7% vs Reentrant 6.0%）；模拟长持锁（每次持锁算 16K 随机数）总时长几乎一致（**9.79s vs 9.72s**）但方差 **0.1% vs 29.5%**——公平锁适合**长临界区/长间隔**场景，此时 barging 收益小而无限期推迟风险大。争用中等时多处理器出现"早期峰值"：插队与被唤醒线程互相迫使对方阻塞（flailing），未来可考虑自适应自旋。同步器映射：**ReentrantLock** 状态=递归计数并记录 owner（fair/nonfair 两个内部子类）；**ReentrantReadWriteLock** 高 16 位写计数、低 16 位读计数，读锁用 acquireShared；**Semaphore** 状态=许可数；**CountDownLatch** 到 0 全部放行；**FutureTask** 状态=运行状态，set/cancel 即 release；**SynchronousQueue** 用等待节点配对生产者与消费者。所有同步器类都用**私有内部 AQS 子类**并委托，避免暴露内部控制方法；反序列化时**重置为初始状态**。

### 线程 vs 事件（von Behren, Condit, Brewer）

87. ☆ 🟡 论文反驳了"事件优于线程"的哪四个主要论点？各自怎么反驳？
   - 要点：四个论点：**协作式多任务使同步廉价**、**无栈从而状态管理开销低**、**基于应用信息的更好调度与局部性**、**更灵活的控制流**。反驳：(1) **性能**——线程慢是**具体线程包的缺陷**而非范式本质：**O(n) 操作**、抢占带来的寄存器保存与内核穿越；他们优化 **GNU Pth** 去掉调度器 O(n) 操作后重跑 SEDA 基准，**扩展到 10 万线程**并与事件服务器持平；(2) **控制流**——考察 Flash、Ninja、SEDA、TinyOS，实际只用 **call/return、并行调用、pipeline** 三类模式，线程表达更自然；只有**动态 fan-in/fan-out**（multicast、pub/sub）事件更自然，但高并发服务器都没用到；健壮系统总需要"返回"来做错误处理与清理；(3) **同步**——Adya 等指出"免费同步"来自**协作式调度（无抢占）**而非事件本身，协作式线程同样受益，且**仅在单处理器上**成立；(4) **状态管理**——固定栈面临溢出 vs 浪费地址空间的取舍，提出**动态栈增长**；事件系统迫使程序员手动最小化阻塞点的活跃状态，线程的调用栈自动管理但可能浪费——由编译器解决；(5) **调度**——Lauer-Needham 对偶意味着同样的调度技巧可用于协作式线程。结论：**缺少可扩展的用户级线程**是推向事件风格的最大动力，而这只是实现产物。

88. 🟡 Lauer-Needham 对偶（duality）、"blocking graph" 和 "stack ripping" 各指什么？为什么作者说"修好事件系统等于换成线程"？
   - 要点：**Lauer-Needham（1978）**：消息传递系统与进程/线程系统在结构与性能上**互为对偶**——monitor ↔ event handler；模块导出函数 ↔ handler 接受的事件；过程调用/fork-join ↔ SendMessage/AwaitReply；return ↔ SendReply；等待条件变量 ↔ 等待消息；实现同样好则性能应等价，选择取决于哪种对应用更自然。现代事件系统与其经典模型不完全对应（忽略协作调度、用共享内存），**SEDA** 的 stage+queue 是唯一严格匹配的。**blocking graph**：节点=阻塞/让出点，边=其间执行的代码；对偶即"同一张图"。**stack ripping**（Adya 等命名）：事件系统里跨模块"调用"要靠发事件、收事件配对，程序员必须**手动保存/恢复活跃状态**、在代码不同位置匹配 call/return，导致隐晦竞态与逻辑错误；线程用调用栈自然封装状态，异常清理简单、调试工具有效。事件系统靠 GC（Ninja/SEDA）或引用计数（Traffic Server，几乎每个版本都有慢泄漏、限制 MTBF）管理堆上状态。Ninja 最复杂的恢复逻辑最终改用线程。若为事件系统造工具解决 reply 匹配/状态管理，就等于**复制线程的语法与运行时行为**（Adya 的协作任务管理把类线程代码变成阻塞点周围的 continuation）。

89. 🔴 Knot 与 Haboob 的对比实验说明了什么？作者提出的编译器支持有哪三个方向？
   - 要点：实现了 **5000 行**用户级协作线程包（**coro** 协程库做最小上下文切换；阻塞 I/O 内部转异步；socket 用 **poll()**，磁盘 I/O 用线程池做阻塞操作；覆盖阻塞系统调用并**仿真 pthreads**，程序无需改动）。用它写了 **700 行**的 Knot web 服务器（静态请求、持久连接、页面缓存，几乎不用调优）。测试机 **2×2000MHz Xeon、1GB、Linux 2.4.20**，Haboob 跑 IBM 1.4 JVM+JIT，两者都用 poll()（/dev/poll 补丁已弃用）。两种策略：**Knot-C 偏向已有连接**（饱和时天然限流）、**Knot-A 偏向 accept**（接近 Haboob 策略）。结果：模式相同——线性上升后饱和；Knot-C 稳态 **≈700 Mbit/s**，受**内核中断处理**限制；Haboob 上限 **500 Mbit/s**，在 512 客户端时 CPU 受限：**每 handler 一个线程池导致事件跨 handler 就切换，满载每秒 30,000 次上下文切换（Knot 的 6 倍以上）**、大量小模块带来模块跨越与排队、临时对象与 GC、**运行时分派**（下一个 handler 静态未知，减少编译器优化、增加流水线停顿）；Knot-A 与 Haboob 的衰减源于 **poll() 扩展性差**，换 **epoll** 后 Knot 扩展优秀（未用于对比因 Haboob 的 socket 库不兼容）；Haboob 超过 16384 客户端**内存耗尽**。编译器方向：(1) **动态栈增长**——静态分析每个调用点的栈上界、识别需扩栈的调用点（递归与函数指针需额外分析）；(2) **活跃状态管理**——调用前弹出临时变量、尾调用弹整帧、重排重叠生命周期变量、对跨阻塞调用持有大量状态发出警告；(3) **同步**——静态竞态检测；参考 **nesC/TinyOS**：原子区必须落在 blocking graph 的一条边内（不可阻塞或让出），分析哪些原子区可并发以在多处理器上安全运行，自动化 libasync 的手工图着色。

### 事务策略：High Concurrency（Mark Richards, IBM developerWorks）

90. ☆ 🟡 High Concurrency 事务策略的核心思想是什么？"read-first" 与 "lower-level" 两种实现技术有何区别？
   - 要点：由 **API Layer 策略**派生：总在调用栈最高层开事务会**持锁过久、占资源过久**；本策略把事务范围**缩到架构中尽可能低的层**，让事务更快提交/回滚，以提高 DB 并发、吞吐和性能。与 API Layer 一样**客户端层不含事务逻辑**（Web、桌面、Web 服务、JMS 均可），因此**一个逻辑工作单元（LUW）只能有一次客户端调用**；无论在哪层开启，**开启事务的方法是事务 owner，应是唯一提交/回滚者**。**read-first**：重构工作流让**所有读操作与处理先在事务外完成**，只把 insert/update 包进**编程式事务**（`UserTransaction` begin/commit/rollback）——示例 `processTrade()` 总耗时 **6100 ms**，其中写操作仅 **300 ms**，重构后事务从 6100 ms 降到 300 ms，理论上**吞吐提升 20 倍**；EJB 3.0 下需**类级**注解 `@TransactionManagement(BEAN)`，说明**同一类不能混用声明式与编程式**。**lower-level**：保留声明式模型，把 update 移到调用栈更低的**另一个 public 方法**——外层 `@TransactionAttribute(SUPPORTS)`，内层 `processTradeUpdates()` 用 **REQUIRED** 开启事务，内层只更新父方法创建/修改的实体。通常需要编程式模型才能缩小范围，且不宜混用两种模型；若用声明式，把开启事务那一层的所有公共写方法标 **REQUIRED**。

91. 🔴 该策略牺牲了什么？持锁过久会引发哪些问题？什么情况下不该采用？给出实施指南。
   - 要点：**代价一**：读操作（即便带更新意图）在事务外执行，**不持读锁**，更新时**过期数据异常（stale data exception）**概率上升——若用 ORM 务必开启**版本控制**；必须确认被更新的实体通常**不会被多个用户同时修改**（交易场景里一笔交易/账户同一时刻只有一个交易员操作）。**代价二**：整体事务健壮性下降，**更难实现、开发测试更久、更易出错**；事务起点分散在 API/业务/DAO 各层，不一致导致难维护、难治理（作者比喻为"缺牙的老曲棍球手"）；**非 owner 的低层方法**在异常时可能回滚，父方法再 commit/rollback 已标记回滚的事务会得到异常，无法采取纠正措施。持锁过久的后果：**耗尽数据库连接**导致应用等待、共享/排他锁引发**死锁**、**锁升级**（行锁→页锁→表锁，启发式不可控；SQL Server 可禁页锁但通常收效不大）。数据库差异：**Oracle、MySQL InnoDB 不持读锁**，SQL Server（未开 Snapshot Isolation）会。指南：**先用 API Layer 策略并以高于峰值的负载压测**，出现吞吐差、等待长、死锁再迁移；**先 read-first 再 lower-level**（事务至少仍留在 API 层）；声明式时用 **REQUIRED 而非 MANDATORY**（防止开启事务的方法调用另一个事务方法出错）；不是所有读都要移出事务——**频繁被多用户同时修改的实体可放回事务内**，但事务内读越多吞吐越低。结论：高并发要求高 DB 并发，高 DB 并发要求少锁、短持有，主要靠代码与事务设计。

### HTTP/2（Daniel Stenberg, *http2 explained* v1.12）

92. ☆ 🟢 HTTP/1.1 的哪些问题催生了 http2？Web 开发者曾用哪些 workaround，为什么它们是"kludge"？
   - 要点：**规范庞大且可选项多**：HTTP 1.0（RFC 1945）60 页，HTTP 1.1（RFC 2616，1999）176 页，更新后拆成六份（RFC 7230 系列）；几乎没有实现做全，少用特性互操作差，**pipelining** 是典型；**TCP 利用不足**，存在本可收发数据的空档；页面**平均 >1.9MB、100+ 个对象**（httparchive）；**延迟敏感**——带宽涨了延迟没涨，移动网络尤甚；**队头阻塞（HOL）**——pipelining 像排队等前面的人办完，2015 年多数桌面浏览器默认关闭。Workaround：**spriting**（小图拼大图，缓存一起失效）、**inlining**（CSS 里 data: URL，同样利弊）、**concatenation**（JS 合并成大文件，改一点全部重载）、**sharding**（原规范每主机最多 2 个 TCP 连接，现今 6–8 个，靠造域名突破；top 300K 站点平均需 **38 个 TCP 连接**；另可用无 cookie 域减小请求）。http2 目标：**降低 RTT 敏感**、**修好 pipelining/HOL**、**停止增加连接数**、**保留所有接口/内容/URI 格式与 scheme**、在 IETF **HTTPbis** 工作组内完成；从 **SPDY/3** 草案起步（draft-00 基本是查找替换）。

93. ☆ 🟢 http2 为什么改成二进制？帧格式是什么？"流（stream）"与多路复用如何消除 HTTP 层的队头阻塞？
   - 要点：二进制使**分帧简单**——HTTP/1 判断帧起止很复杂（可选空白、同一事物多种写法），去掉后实现更简单，也把协议与 framing 分离；协议本身有压缩且常跑 TLS，线上本就看不到文本，调试改用 **curl 或 Wireshark http2 dissector**。帧头统一：**Type、Length、Flags、Stream Identifier、payload**；规范定义 **10 种帧**，最基础的是 **DATA 与 HEADERS**（映射 HTTP/1.1 的体与头）。**Stream**：连接内**独立、双向的帧序列**，任一端可创建/使用/关闭，**流内帧顺序有意义**（接收方按序处理）；一条连接可同时打开多流，帧**交织**发送再在对端拆开（"两列火车并成一列"），创建新流成本极低，会有成百上千并发流；**RST_STREAM** 可在不断 TCP 的情况下中止某个消息（HTTP/1.1 发出 Content-Length 后无法轻易停止，只能断连重握手）。**不再有 minor version**，需要改就是 http3；接收方必须**忽略未知帧类型**，扩展帧可逐跳协商、不能改状态、不受流控。注意作者在 QUIC 一节指出：http2 里**丢包仍会阻塞所有流**（TCP 层），QUIC 才做到只阻塞单流。

94. ☆ 🟡 为什么 http2 需要头压缩？为什么不能直接用通用压缩？HPACK 的设计目标是什么？
   - 要点：HTTP **无状态**，每个请求都要带齐信息，同一站点的一系列请求几乎相同，**cookie** 每次都带且越来越大；HTTP/1.1 请求有时**大于初始 TCP 窗口**，要等一个 RTT 的 ACK 才能发完。HTTPS/SPDY 的压缩被证明易受 **BREACH / CRIME** 攻击——注入已知文本、观察输出变化即可推断内容；对动态内容做压缩而不中招需要专门设计。**HPACK**（单独的 RFC 7541）是专为 http2 头设计的压缩格式；配合"**请求中间件不要压缩此头**"的比特与**可选帧填充（padding）**降低被利用风险。Roberto Peon 的目标：**让合规实现难以泄露信息、编解码快且便宜、接收方可控制压缩上下文大小、允许代理重索引（前后端共享状态）、Huffman 编码字符串可快速比较**。

95. ☆ 🟡 http2 如何在不改 URI scheme 的前提下协商？TLS 上 ALPN 与 NPN 的区别？明文 http:// 上（h2c）如何升级？TLS 是强制的吗？
   - 要点：`http://` 与 `https://` 不能改、也不能有新 scheme，所以要有升级/协商机制。**明文**：用 HTTP/1.1 的 **`Upgrade:` 头**，服务器返回 **101 Switching** 后该连接改说 http2，**代价一个完整 RTT**，但 http2 连接可更长久复用；部分浏览器声明不实现，**IE 团队和 curl 支持**（curl 用 `--http2`，libcurl 设 `CURLOPT_HTTP_VERSION=CURL_HTTP_VERSION_2`，尽力而为、失败则回落 1.1）。**TLS**：SPDY 团队不接受 Upgrade 的 RTT 代价，发明 TLS 扩展 **NPN**（服务器告知支持的协议，**客户端做最终选择**）；经 IETF 标准化为 **ALPN**（**客户端按偏好列出协议，服务器选择**）；因 ALPN 标准化慢，早期实现两者都做，且许多服务器同时提供 SPDY 与 http2。规范中 **TLS 是可选的**（强制 TLS 未达成共识），但 **Firefox 与 Chrome 只实现 TLS 上的 http2**——理由是用户隐私，以及测量表明**新协议走 TLS 成功率更高**（中间盒假定 80 端口一定是 HTTP/1.1 会破坏流量）；规范要求 **TLS ≥ 1.2** 并有密码套件限制。curl 构建于新版 OpenSSL/NSS 同时得到 ALPN+NPN，GnuTLS/PolarSSL 只有 ALPN。Google 宣布 2016 年在 Chrome 移除 SPDY 与 NPN。

96. ☆ 🟡 优先级/依赖、服务器推送、流控与 Alt-Svc 各解决什么问题？http2 普及后对 Web 开发与负载均衡有什么影响？
   - 要点：**优先级与依赖**：每个流有优先级告诉对端谁更重要，并可声明**依赖另一个流**；可**运行时动态调整**（用户滚动到图片区、切换标签页时重排）；细节在标准化中多次变动。**Server push（cache push）**：客户端请求 X 时服务器推测其还会要 Z，主动发送以填充客户端缓存；**必须由客户端显式允许**，且客户端可随时用 **RST_STREAM** 拒绝某个推送流。**流控**：每个流有自己的**通告窗口**，对端只能发送窗口内的数据、需等待窗口扩展，风格类似 SSH；**只有 DATA 帧受流控**。扩展帧 **BLOCKED**：有数据但被流控禁止时发送一次，提示实现有问题或传输不理想。**Alt-Svc / ALTSVC 帧**：http2 连接会**更长寿**、一站一连接，影响 HTTP 负载均衡器的工作方式；服务器可通告替代服务（另一 host/port）用于性能或下线维护，客户端**异步尝试**、可用才切换；opportunistic TLS（http:// 内容也可走未认证 TLS，不显示锁）有争议。开发影响：spriting、inlining **不应再做**，sharding **可能有害**（http2 受益于更少连接）；短期内需同时服务 HTTP/1.1 与 http2 客户端而不做两套前端。

97. 🟡 对 http2 的常见批评有哪些，作者如何回应？http2 的部署前景和 QUIC 的定位？
   - 要点："**Google 造的**"→ 在 IETF 按 30 年来的方式开发，SPDY 只是证明了可部署并给出数据；"**只对浏览器有用**"→ 部分成立，主要驱动是修 pipelining，小型 REST API 收益不大但几乎没坏处，多路复用会催生更多应用场景；"**只对大站有用**"→ 恰恰相反，多路复用对小站常见的高延迟连接帮助更大；"**TLS 让它更慢**"→ 握手与 CPU/功耗开销存在，但 http2 非强制 TLS、多路复用减少 TLS 握手次数，电信运营商（ATIS OWA）需要明文做缓存/压缩；"**非 ASCII 不可接受**"→ 文本协议更易出解析问题，TLS 与压缩早已让线上不可读；"**不比 1.1 快**"→ SPDY 时代和 http2 的测试表明高延迟、多对象场景更快；"**分层违反**"→ 层不是宗教；"**没修 1.1 的缺陷**"→ 为了保持 HTTP/1.1 范式（cookie、授权头等）以便代理互通，**http2 本质只是一个新的 framing 层**。部署：不像 IPv6，跑在 TCP 之上、用现有升级机制与端口，**路由器/防火墙无需改动**；Firefox 35（2015-01-13）默认开启，Chrome 40 逐步放量；2015 年初 Google 全球流量约 5%，5 月升至 **18%**，Firefox 约 9–10%；HAProxy、Squid、Varnish 表态支持，nginx 计划 2015 年底，Apache 有 "very alpha" 的 mod_h2。**QUIC**：Google 用 **UDP 实现的 TCP+TLS+SPDY 替代品**，连接延迟更低，**丢包只阻塞单个流**，可跨网络接口（覆盖 MPTCP 的目标）；当时仅 Chrome 与 Google 服务端实现，规范模糊多变、尚未进 IETF。

### REST（InfoQ eMag Issue 12）

98. ☆ 🟢 Tilkov 的五条 REST 原则与 Fielding 的六个架构约束分别是什么？REST 与 HTTP 是什么关系？
   - 要点：**五原则**（Tilkov）：**给每个"东西"一个 ID**（URI 是全球命名空间；集合、流程、报价请求等都值得标识，不等于暴露数据库行）；**把东西链接起来**（HATEOAS，链接可指向其它公司/服务器）；**使用标准方法**（GET/POST/PUT/DELETE/HEAD/OPTIONS，每个资源同一接口，"数据类型—操作—实例"三角）；**资源有多种表示**（`Accept` 内容协商，提供 HTML+XML 让浏览器也能消费、Web UI 即 Web API）；**无状态通信**（状态变成资源状态或留在客户端，服务器不保留会话；客户端不依赖连续两次请求打到同一台服务器，服务器换硬盘/升级/重启也不受影响）。**六约束**（Amundsen 讲 Fielding）：**client-server**（客户端发起，无 P2P）、**stateless**（服务器可立即忘记客户端）、**cache**（Web 靠缓存才扩展）、**uniform interface**（人人用同一 API，最难）、**layered system**（随时增减硬件、24/7）、**code on demand**（applet/ActiveX，如今是 JavaScript）。目标是**最小化延迟、最大化可扩展性与组件独立性**。REST 是 Fielding 博士论文定义的**架构风格**（约 25 页/172 页），可用多种技术实现；**HTTP+URI（Web 架构）是它唯一重要的实例**，HTTP 用其动词实例化了统一接口；不按 REST 用 HTTP 可称"滥用 HTTP"（"RESTful HTTP"一词由此而来）。

99. ☆ 🟢 统一接口的四个要素是什么？Fielding 的 connector 与 component 有何区别，为什么重要？
   - 要点：四要素：**标识**（URI，涵盖 URL 与 URN）；**表示**（media type，源自邮件的 MIME，但 Web 上的 media type 还**标识处理规则**）；**自描述消息**（理解消息所需的一切都在消息里：头+体——来源、是否缓存、是否过期、可保留多久、格式、是否已认证；有请求头、响应头、内容头如语言/压缩/字节数）；**超媒体**（HATEOAS，用**链接和表单**实现，是"应用控制信息"）。**Component**（数据库、文件系统、消息队列、事务管理器、源代码、OS）是**私有的**，各自做法不同（MySQL vs SQL Server、CouchDB vs MongoDB）、可随时更换，网络层面无人关心；**Connector**（Web 服务器、浏览器代理、代理服务器、缓存服务器）是**大家事先约定的共享 API**，在 Web 上通常就是 HTTP，也包括 FTP/IRC/DNS/SMTP；**你不构建 connector，你使用它**（各语言都有 HTTP/缓存类库）。Fielding 约束的是**连接方式而非运作方式**，所以只要支持共享 connector，语言和组件可任意选择——这带来"能长久运行的东西"。

100. ☆ 🟡 安全（safe）与幂等（idempotent）分别指什么？GET/PUT/DELETE/POST 各属哪类？这对分布式集成中的重试为什么关键？
   - 要点：**GET 是 safe**——调用者没有任何义务，可做高效缓存，很多时候不必发请求；**GET、PUT、DELETE 幂等**——没收到结果时不知道请求没到还是响应丢了，**重发即可**；PUT 意为"用这些数据更新资源，若 URI 不存在则创建"；DELETE 可反复尝试，删不存在的东西无妨；**POST 通常是创建新资源，也可触发任意处理，既不安全也不幂等**。用 GET 删除对象违反安全约束（调用者不能被追责、**爬虫会造成副作用**、不可书签）。Starbucks 支付案例：PUT 支付时可能**连不上、连接中断、收到 4xx/5xx**；前两种（及 500/503/504）**直接重复 PUT** 直到成功——收到 **200 表示先前的 PUT 其实已成功（服务器对 NOP 的确认）**，**201** 表示这次才成功；**400** 说明载荷服务器看不懂，修正后重发；**403** 表示服务器理解但拒绝、**不要重试**，应从响应中找其它状态转换。状态码是**语义丰富的确认**，靠它可以在 HTTP 请求/响应之上叠加**协调协议**，获得健壮性与可靠性。GET 与 HEAD 不引发状态转换，只用于检查当前状态。

101. ☆ 🔴 用 HTTP 做条件更新 / 乐观并发控制：OPTIONS、Expect: 100-Continue、If-Match/ETag、If-Unmodified-Since、409 与 412 各扮演什么角色？为什么 ETag 被视为 RESTful 的试金石？
   - 要点：改单前先 **OPTIONS /order/1234** 看 `Allow: GET, PUT` 判断是否还可改（只反映当时，**无长期保证**）；可选做"look before you leap"：带 **`Expect: 100-Continue`** 试探 PUT，服务器答 **100 Continue** 才发正文，否则 **417 Expectation Failed**；PUT 只传**增量**（`<additions>shot</additions>`），在现有资源状态上下文中处理。竞态（与咖啡师赛跑）失败时得到 **409 Conflict**，响应体给出客户端提交与服务器当前状态的差异，客户端需 GET 当前状态再决定下一步。保护性头：**If-Unmodified-Since**（时间戳，**一秒粒度**，只适合慢变资源）或 **If-Match**（ETag——资源状态的唯一标识，通常是 MD5/SHA1 校验）；不满足则 **412 Precondition Failed**，虽然输了比赛但**资源不会进入不一致状态**。作者的三步配方：(1) OPTIONS（可选）；(2) If-Unmodified-Since / If-Match；(3) **直接 PUT 并处理 409**——因为前两步都是**乐观**检查；W3C 非规范性 note 推荐 ETag，作者首选 ETag；即使不用 OPTIONS/Expect 也要处理 **405 与 409**。Tilkov 引 Sam Ruby："**你支持 ETag 吗**"是评估 RESTfulness 的关键问题——ETag 是 HTTP 1.1 引入的、让客户端用校验和验证缓存表示是否仍有效的机制；框架默认 `Cache-control: no-cache` 会毁掉缓存与再验证；最省事的做法是交给 Apache HTTPD 之类会正确生成头的基础设施；客户端也应尊重 600 秒新鲜期之类的信息、或干脆前置 Squid。其它状态码：**202 Accepted**（异步，轮询 Location）、**303 See Other**、**404**、**500**。

102. ☆ 🔴 以 "How to GET a Cup of Coffee" 为例，HATEOAS 如何驱动工作流？它如何支持服务演进与兼容旧客户端？URI 模板的风险是什么？
   - 要点：客户与咖啡师是**两个并发状态机**，每次转换 = **HTTP 动词作用于某 URI**。`POST /order` → **201 Created + Location** + 表示中含 `<next rel="http://starbucks.example.org/payment" uri="https://.../payment/order/1234" type="application/xml"/>`——`<next>` 放在**公共命名空间**（转换不限于 Starbucks，便于复用/标准化），`rel` 是**私有微格式**的语义，`type` 告知表示格式，再用 OPTIONS 问该资源支持的动词。**URI 就是状态机的转换**，客户端靠跟随链接驱动应用状态；状态机与工作流**在导航中逐步自描述**，而不是像 WS-BPEL/WS-CDL 那样预先描述；**表示格式与转换的语义事先约定，"如何到达目标"运行时发现**。咖啡师侧用 **Atom feed** `/orders` 列出待做订单，通过 **AtomPub** 的 `rel="edit"` URI **PUT** `<status>preparing</status>` 锁定订单（之后 /orders/1234 只接受 GET），做完 **DELETE** 该条目（之后 GET 得 404）。**演进**：7 月上线标准工作流 → 8 月表示中新增免费 WiFi 促销的 `<next>` 链接（可指向第三方）——**旧客户端忽略不认识的转换，仍能沿原转换达到目标** → 9 月客户端升级后跟随促销转换；关键是**消费者默认预期变化**，每步由服务提供命名资源的 URI，而不是**直接绑定 URI 模板**。**URI 模板**（如 S3 的 `http://s3.amazonaws.com/{bucket_name}/{key_name}`、`/payment/order/{order_id}`）是与消费者的**契约**，服务演进时必须维持，是隐式耦合——**只在可推断 URI 有用且不太可能变化时使用，慎用**；替代方案是只对授权系统开放的 `/payments` feed（不可推断链接）。Tilkov 补充：表示版本（v1.1/v1.2）可通过 **MIME 类型**区分；Burke 指出 **JAX-RS 最大弱点是几乎没有标准化的超媒体支持**（只有 URI 模板辅助 API）。缓存与故障：反向代理 + **`Expires`（10 秒）** 使源站每分钟最多约 6 个请求，还能**掩盖间歇故障、辅助崩溃恢复**；**Web 以延迟换取大规模扩展**，外汇交易这类延迟敏感领域不适合。

103. 🟢 Tilkov 列出的八个 REST 反模式是什么？cookie 一定不 RESTful 吗？"忘记超媒体"的表现是什么？
   - 要点：八条：(1) **一切通过 GET 隧道**（`?method=deleteCustomer&id=1234`：URI 编码的是操作与参数而非资源、方法与语义不符、不可书签、**爬虫触发副作用**；只读接口可能"意外 RESTful"，加写操作后幻觉破灭）；(2) **一切通过 POST 隧道**（单一 URI + 不同消息表达意图，即 SOAP 1.1 over HTTP；无法缓存与书签，"不是违反而是忽略"REST）；(3) **忽略缓存**（框架默认 `Cache-control: no-cache`）；(4) **忽略状态码**（只返回 200/500 或只 200 + 体内错误文本——"通过 200 隧道错误"；客户端应按类处理，如所有 2xx 视为成功；201+Location、409、412）；(5) **误用 cookie**；(6) **忘记超媒体**；(7) **忽略 MIME 类型**（XML/JSON/YAML、PDF/JPEG、v1.1/v1.2，优先用现成广为人知的格式）；(8) **破坏自描述性**（自造头、格式、协议；PDF 例子：认证、缓存、content-type 触发查看器，全世界都能用自己的基础设施重复）。**Cookie**：REST 禁止的是**会话状态**（可扩展性、可靠性、耦合），资源状态与客户端状态都可以；cookie 存指向服务器内存结构的会话键是反模式，存**服务器无需会话即可验证的认证令牌**则 RESTful，但能用 URI/标准头/HTTP 认证传递的信息不要塞进 cookie。**忘记超媒体**的表现：表示中**没有链接**，客户端按配方拼 URI；理想是**客户端只需知道一个 URI**，其余 URI 与查询配方由表示中的链接给出（AtomPub 的 service document 是好例子；HTML 让浏览器提供完全动态界面）；作者建议少花时间争论"完美 URI 设计"（它们只是字符串），多花在表示中放链接。反模式与设计模式一样**只在匹配上下文时应用**，可以有理由地放宽约束，但要有意识。

### JVM 内存管理（Sun HotSpot 白皮书, 2006）

104. ☆ 🟢 HotSpot 的分代（generation）布局是什么？"弱分代假设"是什么？minor 与 full GC 的触发与顺序？
   - 要点：三代：**young**（**Eden + 两个较小的 survivor 空间 From/To**，任一时刻一个 survivor 为空）、**old**（存活若干次 young GC 后**晋升/tenured** 的对象，以及**直接分配的大对象**）、**permanent**（JVM 让 GC 管理的元数据：描述类与方法的对象及类/方法本身）。**弱分代假设**：**多数对象早死**；**老→新的引用很少**。young 区小、垃圾多，收集**频繁但快**；old 区大、占用增长慢，收集**不频繁但耗时长**；young 算法重速度，old 算法重空间效率、需在低垃圾密度下工作。**young 满 → minor collection**（只收 young）；**old 或 perm 满 → full/major collection**（收所有代）：通常**先用 young 算法收 young，再对 old+perm 运行 old 算法，各代分别压缩**；若 old 太满、放不下可能晋升的对象，则（**除 CMS 外**）跳过 young 算法、直接对整堆用 old 算法——CMS 是特例，**它不能收集 young**。GC 的职责：分配内存、保证被引用对象留在内存、回收不可达对象；GC 解决悬垂引用与空间泄漏，但持续引用无用对象仍会耗尽内存。设计维度：**串行 vs 并行**、**并发 vs stop-the-world**、**压缩 vs 非压缩 vs 复制**；指标：吞吐、GC 开销、停顿时间、频率、footprint、promptness。

105. ☆ 🟡 HotSpot 为什么能做到快速分配？bump-the-pointer 与 TLAB 各解决什么问题？这与压缩/非压缩收集器有何关联？
   - 要点：多数情况下有**大块连续空闲内存**，用 **bump-the-pointer**：记录上一个对象末尾，新分配只需检查剩余空间够不够，然后**更新指针并初始化对象**。多线程下若用**全局锁**保护分配，会成为瓶颈；HotSpot 用 **TLAB（Thread-Local Allocation Buffer）**：每个线程从代中拿一小块私有缓冲区，**只有该线程在其中分配，无需加锁**，只有 TLAB 用尽需要新的时才同步；分配器按需给 TLAB 定尺寸，平均**浪费不到 Eden 的 1%**；两者结合使一次分配只需**约 10 条本机指令**。关联：压缩（mark-sweep-compact 滑动压缩）或复制（Eden→To）后空闲空间连续，才能 bump-the-pointer；**CMS 是唯一不压缩的收集器**，空闲空间不连续，必须用 **free list**、按需求大小搜索链表，老年代分配（主要发生在 young GC 晋升时）更贵，也给 young GC 增加开销。

106. ☆ 🟡 J2SE 5.0 HotSpot 的四种收集器（serial / parallel / parallel compacting / CMS）分别用什么算法、适用什么场景、如何选择？
   - 要点：**Serial**（`-XX:+UseSerialGC`，非 server-class 机器默认）：young 与 old 都**单 CPU、stop-the-world**。young：Eden 存活对象**复制到 To**（过大的直接进 old），From 中较年轻的复制到 To、较老的晋升 old；**To 满则剩余存活对象不论年龄一律晋升**；Eden 与 From 中剩下的即垃圾，无需检查；之后 **From/To 交换角色**。old+perm：**mark-sweep-compact**——标记存活、清扫识别垃圾、**滑动压缩**把存活对象移到一端，空闲连成一块以便 bump-the-pointer。适合客户端机器、无低停顿要求，**64MB 堆 full GC 最坏停顿 <0.5 秒**。**Parallel / throughput collector**（`-XX:+UseParallelGC`，server-class 默认）：young 用**并行版复制算法**（仍 STW），old 仍是**串行 mark-sweep-compact**；适合多 CPU、无停顿约束的批处理、计费、薪资、科学计算。**Parallel compacting**（`-XX:+UseParallelOldGC`，5.0 update 6 引入，最终会取代 parallel）：young 同上；old+perm **STW、大部分并行、滑动压缩**，三阶段——**marking**（根集分给多个 GC 线程并行标记，按固定大小 region 记录存活数据）、**summary**（串行；从左侧找**dense prefix**——压缩收益不值成本的密集区域不动，其右侧全部压缩，计算每 region 存活数据新位置）、**compaction**（线程独立填充 region，得到一端密集、一端一大块空闲）；适合多 CPU 且有停顿约束；在大型共享机（SunRay）上不宜独占多 CPU，可减小 **`-XX:ParallelGCThreads=n`**（默认=CPU 数）或换收集器。**CMS / low-latency**（`-XX:+UseConcMarkSweepGC`）：young 同 parallel；old 大部分与应用并发：**initial mark**（短停顿，根直达对象）→ **concurrent mark**（可达传递标记，应用同时在改引用）→ **remark**（停顿，重访并发期间被修改的对象，因较重故**多线程并行**）→ **concurrent sweep**；增量模式 **`-XX:+CMSIncrementalMode`**（配 `-XX:+CMSIncrementalPacing`）把并发工作切成小块穿插在 young GC 之间，适合 1–2 个处理器的低停顿场景。

107. ☆ 🔴 CMS 的代价有哪些？它何时启动老年代收集，"退化"成什么？如何调优、适合什么应用？
   - 要点：代价：(1) **唯一非压缩**——释放后不移动存活对象，需 **free list**，老年代分配更贵、young GC 也受累；**碎片**——CMS 跟踪常见对象大小、预估需求、拆分/合并空闲块应对；(2) **需要更大的堆**——标记期间应用继续分配、老年代继续增长；(3) **floating garbage**——标记期间变成垃圾的对象要等下一轮才回收；(4) remark 重访对象**增加总开销**（降低停顿的典型代价）；(5) **并发期间抢占应用 CPU**。综合：相比 parallel，**老年代停顿显著缩短**，代价是 **young 停顿略长、吞吐略降、堆更大**。启动时机：**不等老年代满**，而是根据**历史收集耗时与老年代填充速度的统计**提前启动，力争在填满前完成；否则**退化为 serial/parallel 使用的、更耗时的 STW mark-sweep-compact**；也会在占用超过 **initiating occupancy** 时启动——`-XX:CMSInitiatingOccupancyFraction=n`（老年代百分比，**默认 68**）。适用：需要**更短停顿**且**能分出处理器资源**给 GC 的应用；典型是**长生存数据集大（大老年代）、≥2 处理器**的应用，如 **Web 服务器**；有低停顿要求的应用都应考虑；单处理器上老年代适中的交互应用也可能有好效果。

108. ☆ 🟡 什么是 ergonomics？server-class 机器如何判定，默认 JVM/收集器/堆大小是什么？基于行为的并行收集器调优有哪三个目标，优先级如何？
   - 要点：**Ergonomics** = **平台相关的自动选择**（收集器、堆大小、client/server JVM）+ **按期望行为动态调优**（并行收集器），目标是尽量少的命令行参数得到好性能。**Server-class 机器**：**≥2 个物理处理器且 ≥2GB 物理内存**（**32 位 Windows 除外**）。非 server-class 默认：**client JVM、serial GC、初始堆 4MB、最大堆 64MB**。Server-class：**server JVM**（除非显式 `-client`）+ **parallel GC**；用 parallel 时**初始堆 = 物理内存 1/64（最小 32MB）、上限 1GB；最大堆 = 物理内存 1/4、上限 1GB**；否则仍用 4MB/64MB。行为目标（仅并行收集器）：**最大停顿目标 `-XX:MaxGCPauseMillis=n`**（提示，**按每代分别应用**，未达标则**缩小该代**，可能降低吞吐，且不一定能达成，默认不设）；**吞吐目标 `-XX:GCTimeRatio=n`**——GC 时间 : 应用时间 = **1/(1+n)**，**默认 99 即 1%**，`19` 即 5%，计入所有代；未达标则**增大各代**让应用在两次收集间跑更久；**footprint 目标**——前两者达成后缩小堆直到某目标（通常是吞吐）不达标。**优先级：停顿 → 吞吐 → footprint**。堆大小会在竞争目标间**振荡**，稳态也如此。

109. 🔴 白皮书推荐的 GC 调优策略是什么？堆与各代大小的关键参数？`OutOfMemoryError` 有哪几种消息，各如何排查？用什么工具？
   - 要点：策略：**首先什么都不做**，让系统自动选择，测试后可接受就结束；有问题先考虑默认收集器是否合适、显式换收集器；**先测量再调**，用贴近真实用法的测试，警惕过度优化（数据集、硬件甚至 GC 实现都会变）。堆：非 server-class 默认 64MB 常太小，用 `-Xmx` 加大；**除非有长停顿问题，尽量把内存给堆——吞吐与可用内存成正比，内存充足是影响 GC 性能的首要因素**；**第二因素是 young 占比**——除非老年代收集过多或停顿过长，多给 young，但 **serial 下 young 不超过总堆一半**；并行收集器下**指定期望行为而非固定大小**：先设吞吐目标、不设最大堆（除非确知需要更大）；堆涨到最大说明目标在该上限内不可达，把最大堆设到**接近物理内存但不引起 swap**再试；仍不达则目标对内存来说太高；吞吐达标但停顿太长再加最大停顿目标并接受折中。参数：`-Xms/-Xmx`；`-XX:MinHeapFreeRatio=40 / -XX:MaxHeapFreeRatio=70`（按代应用，空闲比例低于/高于阈值则扩/缩）；`-XX:NewSize`；`-XX:NewRatio`（**client 2、server 8**，n=3 即 young:old=1:3）；`-XX:SurvivorRatio`（默认 32，n=7 时每个 survivor 占 young 的 1/9，因为有两个）；`-XX:MaxPermSize`；单位后缀 k/m/g。**OOM 不一定是泄漏**，可能只是配置；先看完整消息：**"Java heap space"**——`-Xmx` 不足，或应用无意持有引用（用 **HAT** 看从根集到对象的引用路径），或 **finalizer 积压**（finalizer 线程跟不上，用 **jconsole** 看待终结对象数）；**"PermGen space"**——加载类过多，调 `-XX:MaxPermSize=n`（JSP/Web 容器常见，`jmap -permstat` 看统计）；**"Requested array size exceeds VM limit"**——申请的数组大于堆（如 256MB 堆申请 512MB 数组），多半是堆太小或大小计算 bug。工具：**`-XX:+PrintGCDetails`**（各代收集前后存活大小、可用空间、耗时）、**`-XX:+PrintGCTimeStamps`**（关联其它日志）、**jmap**（Solaris/Linux；`-heap` 收集器名与线程数与堆配置、`-histo` 按类实例数与字节数直方图、`-permstat`）、**jstat**（内建插桩，各代容量与使用、GC 统计）、**HPROF**（JVM TI 代理：CPU、堆分配、监视器争用、完整堆转储）、**HAT**（浏览 HPROF 堆快照的对象拓扑，查"从 rootset 到此对象的所有引用路径"）。

### accept() 惊群（Molloy & Lever, FREENIX 2000）

110. ☆ 🟡 Linux 2.2 上 `accept()` 的"惊群（thundering herd）"问题是怎么产生的？为什么作者说 accept 路径把影响放大了三倍？OpenBSD 怎么处理？
   - 要点：网络服务器预创建多个线程/进程在**同一 TCP socket 上 `accept()`** 等待连接；Linux 把它们放进 socket 的 **wait queue**（链表），线程状态从 TASK_RUNNING 改为 **TASK_INTERRUPTIBLE** 后睡眠（`tcp_accept()` 做这些工作）。连接到达时 `tcp_v4_rcv()` 识别出对监听 socket 的连接请求，调用 **`wake_up_interruptible()`**——它**遍历整个 wait queue 唤醒所有人**，但**只有一个线程能拿到连接，其余都重新入队睡眠**；这种无谓唤醒就是惊群，白白消耗 CPU、损害可扩展性。作者对可扩展性的定义：不论 wait queue 上有多少线程，**accept 应接近常量时间**。放大原因：socket 结构有一个含六个方法的虚操作向量（`state_change/data_ready/write_space/error_report` 等，默认指向 `sock_def_wakeup/sock_def_readable/tcp_write_space/sock_def_error_report`），**每个方法都调 `wake_up_interruptible()`**，而 **accept 路径依次调用了 `tcp_write_space()`、`sock_def_readable()`、`sock_def_wakeup()` 三个**，惊群影响**三倍**；且因最常用的 socket 方法都这样，几乎任何 TCP 操作都可能无谓唤醒任务。**OpenBSD 2.6** 表面上也唤醒所有睡在该 socket 标识上的线程，但内核**序列化所有 accept 调用**，同一时刻只有一个线程在等待——避免了惊群，却**限制了性能**。

111. 🔴 论文提出的 "task exclusive" 与 "wake one" 两种方案分别如何工作，各有什么局限？"always wake" 是什么？微基准与 SpecWeb99 的结果说明了什么，为什么要改 Apache？
   - 要点：解决思路都是**阻止所有睡眠线程被唤醒**。**Task Exclusive**（社区提出，已并入 2.3 开发系列）：线程在 `state` 上设 **TASK_EXCLUSIVE** 标志并用新函数 **`add_wait_queue_exclusive()`** 把自己加到**队尾**；`__wake_up()` 遍历队列，**唤醒到第一个 exclusive 线程即停止**；普通 `add_wait_queue()` 把线程加到**队头**，保证非 exclusive 的都被唤醒；由程序员负责正确使用，**异常情况（如监听 socket 意外关闭）需特殊处理唤醒全部 exclusive 等待者**。**Wake One**（CITI 提出）：认为**唤醒方比睡眠方更清楚该唤醒一个还是全部**，决策**推迟到唤醒时**——新增宏 **`wake_one()` / `wake_one_interruptible()`**，与 `wake_up*` 参数相同，只多传一个标志给 `__wake_up()`；为不影响其它协议，给 TCP 复制专用方法（`tcp_wakeup/tcp_data_ready/tcp_write_space`）改调 wake_one，accept 用到的三个方法都只唤醒一个；**难点：`select()` 这类调用依赖每次都被唤醒**，即使前面还有其它线程。**Always Wake**（未实现的混合方案）：仍由唤醒方用 wake_one 决定，但像 select 这样必须被唤醒的线程在 state 上设一个位、置于**队头**、每次 `__wake_up()` 都被唤醒；作者认为最健全优雅。设计准则：不破坏现有系统调用、保留依赖"唤醒所有"的行为、尽量简单且局限于 TCP 代码、不改熟悉接口、方案通用可用于整个内核。**微基准**（4×450MHz Pentium II Xeon、Linux 2.2.9，用 printk 估算 wait queue 恢复平静的时间）：stock 内核 **O(n)**——100 线程 4708 µs、1000 线程 **177274 µs**；两个补丁**接近常量**（约 0.6–1.8 ms），仅粗略估计（printk 有开销、只跑一次）。**宏基准**：SpecWeb99 预发布版，四台 K6-2 客户端打 4×400MHz Xeon 服务器，Linux 2.2.14，Apache **200 个 httpd**、无 keep-alive、300–1000 并发连接：两种补丁**吞吐稳定提升略超 50%**，两者无明显差别（SPEC 规则限制公布细节）。**Apache 改动原因**：stock Apache 1.3 在 Linux 上用**锁串行化 accept**，防止多 IP/端口下的内部错误；单 IP 单端口时不必要——去锁后每个 httpd 可在连接到达前先完成大半 accept 工作，降低有效开销；单处理器 K6-2 上 20 个 httpd 的测试显示**非加锁 Apache 提高了开始丢性能的请求率阈值**；但 stock 2.2.14 上 httpd 越多惊群越重（中高流量站点常 >100 个 httpd）。结论：惊群确实是高负载服务器瓶颈，任一方案都能显著改善，收益来自**减少内核中无谓调度未就绪任务的时间**；task exclusive 与 2.3 的双向链表 wait queue 契合但对程序员要求高，wake one 更干净、只需一行代码。
---

## 难度图例

🟢 初级（能说出定义与结论） · 🟡 中级（能讲清机制与「为什么这样设计」） · 🔴 高级（能复述正确性论证、做取舍、推到失败场景）

## 与 modules 的映射

| 本文件分组 | 对应 modules 模块 | 备注 |
|---|---|---|
| 一、Paxos / Raft / Spinnaker | `system-design` Q1–Q4 方法论、共识与复制类主题；`kubernetes` Q40（etcd）；`middleware`（分布式数据库） | 多数派、领导者选举、日志复制、成员变更、一致性读 |
| 二、VM-FT / Lamport 时钟 / 拜占庭 / Harvest-Yield | `sre-reliability`（容错、脑裂、可用性取舍）；`system-design`（CAP 与 harvest / yield） | 输出规则、happens-before、3f+1、按子系统分解 |
| 三、GFS / MapReduce / Codd / 客户端缓存一致性 | `system-design`（分布式文件与批处理主题）；`middleware`（存储与数据库）；`linux`（文件系统与缓存） | 单 master、租约与变更顺序、记录追加、备份任务、数据独立性 |
| 四、Reactor / AQS / 线程 vs 事件 / 事务策略 / HTTP/2 / REST / JVM 内存 | `linux`（I/O 模型、并发）；`network`（HTTP/2、REST）；`middleware`（JVM 调优、事务）；`system-design`（API 设计） | Nginx / Redis / Node 的 Reactor 根源、HPACK、代际 GC |

## 附：本机书架索引（不出题，作为 explain / 延伸阅读的一手来源）

`~/ebooks/` 里除上述论文外还有约 70 本教材与手册（版权书籍，本项目不提炼题目，只做索引；讲解概念时可指向对应章节）：

| 主题 | 书目 | 对应模块 |
|---|---|---|
| Linux / 操作系统 | Advanced Programming in the UNIX Environment（2e 与旧版）· Linux Kernel Development 3e · Understanding the Linux Virtual Memory Manager · 《Linux 内核完全注解》· Operating Systems 4e · x86 Assembly Language Reference · Intel i386 手册 · Compilers（龙书预览） | `linux` |
| 网络 | Computer Networking: A Top-Down Approach · Beej's Guide to Network Programming · Java Network Programming · http2 explained | `network` |
| 数据库 / 存储 | Database System Concepts 6e · Fundamentals of Database Systems 6e · Database Systems: The Complete Book 2e · 《数据库系统实现（第二版）》· Beginning Database Design · MySQL Reference Manual · Redis in Action | `middleware` |
| 分布式 / 并发 | Distributed Systems: Principles and Paradigms 2e（Tanenbaum）· Seven Concurrency Models in Seven Weeks · The Art of Multiprocessor Programming · Java Concurrency in Practice · Getting Started with NIO / NIO Trick and Trap | `system-design` · `linux` |
| 算法 / 面试 | Introduction to Algorithms 3e · Algorithms 4e（Sedgewick）· The Algorithm Design Manual · Algorithm Design（Kleinberg / Tardos）· Cracking the Coding Interview 4e · Elements of Programming Interviews · Data Structures and Algorithms in Java | 编程基础（非运维模块） |
| Java / Web | Effective Java 2e · JVM 规范 7 / 8 · Java 语言规范 8 · Java EE 6 Tutorial · Pro Spring 3 · Pro Spring MVC · Design Patterns（Java / UML）· Expert One-on-One J2EE · Node.js 开发指南 | 开发向补充 |
| 安全 / 其他 | 《Metasploit 渗透测试指南》· Apache Thrift · API Design eBook · Building and Testing with Gradle · log4j 用户指南 · Refactoring 节选 · QR 码标准 · The Little Schemer | `cloud-security`（渗透测试基础）· 其他 |
