# 监控 / 可观测性面试题（23 题）

> 模板见 [../../docs/STANDARD.md](../../docs/STANDARD.md)。
> **AWS 托管可观测性补充**：[collections/aws-managed-services-only.md](../../collections/aws-managed-services-only.md) 第 35–50 题——CloudWatch vs AMP + Managed Grafana vs 自建 kube-prometheus-stack：没有直方图与标签选择器对 SLO 的影响、按自定义指标计费与基数治理、告警从 Alertmanager 迁到 SNS 丢掉的分组 / 抑制 / 静默。

---

### Q1. Prometheus 拉模型（pull）优缺点？与 Pushgateway 关系？
- **难度**：🟡 中级
- **关键词**：Prometheus, pull, Pushgateway
- **概念速记**：Prometheus 主动抓取 `/metrics`，而非 agent 推送。
- **参考答案**：优点：目标自暴露、便于服务发现、健康检查（抓不到即异常）、水平分片。缺点：短生命周期 Job 来不及抓，需 Pushgateway 中转（不过期需手动清）。对比 Zabbix/InfluxDB push。
- **易错点**：把所有指标都走 Pushgateway，失去 pull 的健康检查优势。
- **延伸**：Q2（指标类型）、Q6（SLO）

### Q2. Counter / Gauge / Histogram / Summary 四种指标区别？
- **难度**：🟡 中级
- **关键词**：指标类型, Histogram, Summary, 分位数
- **概念速记**：Counter 只增；Gauge 可增减；Histogram 分桶；Summary 客户端算分位。
- **参考答案**：Counter（rate 用）、Gauge（内存/并发）、Histogram（延迟分布、算 P99、可聚合）、Summary（客户端算分位，省服务端但难跨实例聚合）。延迟用 Histogram 便于多实例聚合。
- **易错点**：用 Summary 后无法跨实例聚合分位数。
- **延伸**：Q3（PromQL）

### Q3. 如何用 PromQL 算 P99 延迟和错误率？
- **难度**：🔴 高级
- **关键词**：PromQL, histogram_quantile, rate, 聚合
- **概念速记**：分位数必须在桶级别（`by (le)`）聚合。
- **参考答案**：错误率 `sum(rate(http_requests_total{code=~"5.."}[5m]))/sum(rate(http_requests_total[5m]))`；P99 `histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))`。rate vs irate（后者更灵敏）。分位数不能先算各实例分位再平均。
- **易错点**：直接对 histogram_quantile 结果再 avg。
- **延伸**：Q2、Q6

### Q4. 可观测性三支柱（Metrics/Logs/Traces）？OpenTelemetry 作用？
- **难度**：🟡 中级
- **关键词**：可观测性三支柱, OTel, 追踪
- **概念速记**：指标答「健不健康」、日志答「发生什么」、追踪答「慢在哪」。
- **参考答案**：Metrics（聚合）、Logs（离散事件）、Traces（链路）。OTel 提供厂商无关采集标准（SDK/Collector），统一 trace/metric，避免锁定，对接 Jaeger/Tempo/Prometheus。
- **易错点**：以为装了监控就等于可观测（缺 trace 看不到跨服务瓶颈）。
- **延伸**：Q9（追踪）、Q5（日志）

### Q5. ELK vs Loki 区别与选型？
- **难度**：🟡 中级
- **关键词**：ELK, Loki, 全文索引, 对象存储
- **概念速记**：ELK 全文索引强但重；Loki 只索引标签、轻量省钱。
- **参考答案**：ES 存全文索引，功能强但重/贵；Loki 只索引标签、对象存储存日志、PromQL 查、轻量省钱。要全文检索选 ES；只查日志+省成本选 Loki。容器常见 EFK/PLG（Fluent Bit 采集）。
- **易错点**：小集群硬上 ELK 成本压垮。
- **延伸**：Q4、linux Q17（日志分析）

### Q6. Alertmanager 的分组/抑制/静默？如何避免告警风暴？
- **难度**：🔴 高级
- **关键词**：Alertmanager, 抑制, 静默, 告警风暴
- **概念速记**：grouping 合并、inhibition 高级别抑低级、silence 手动静默。
- **参考答案**：grouping（按标签合并减条数）、inhibition（集群挂抑制其下服务告警）、silence（维护窗）。避免风暴：合理路由树、聚合、`for`（持续才告警）、去重、分级（page/notify），结合 SLO 只告警真影响用户的。
- **易错点**：`for: 0` 导致抖动即告警，噪声大。
- **延伸**：Q3、sre Q（告警设计）

### Q7. 什么是 SLO / SLI / Error Budget？怎么用做发布决策？
- **难度**：🔴 高级
- **关键词**：SLO, SLI, Error Budget, 错误预算
- **概念速记**：SLI 实际指标；SLO 目标；Error Budget=1-SLO 允许的错误额度。
- **参考答案**：SLI（成功率/延迟）；SLO（如 99.9%）；Error Budget 耗尽则冻结发布、优先稳定性。把稳定性变可量化风险额度，避免「100% 可用」空谈。
- **易错点**：SLO 设 100% 导致永远不达标或无人敢发布。
- **延伸**：sre Q（Error Budget 治理）；Q6

### Q8. 如何设计告警规则避免「狼来了」和「漏报」？
- **难度**：🔴 高级
- **关键词**：告警设计, 多指标关联, 分级
- **概念速记**：告警要对「需要人动作」的事，而非所有异常。
- **参考答案**：多指标关联（错误率↑且流量正常）；设 `for` 防抖；分层（page vs ticket）；降噪（因果抑制）；定期回顾误报；关键路径全覆盖，非关键走 dashboard。
- **易错点**：把所有 dashboard 曲线都配告警。
- **延伸**：Q6、Q7

### Q9. 分布式追踪如何在 K8s 中接入（无侵入 vs SDK）？
- **难度**：🔴 高级
- **关键词**：分布式追踪, OpenTelemetry, W3C, 采样
- **概念速记**：trace-id 跨服务透传，串联调用链。
- **参考答案**：SDK 埋点最准但改代码；无侵入：Service Mesh（Istio 自动注入）、eBPF（Pixie）。关注 trace-id 透传（W3C）、采样率（1%~10%）、存储成本（Tempo/Jaeger）。
- **易错点**：采样率过低导致关键慢请求没被采到。
- **延伸**：Q4；kubernetes Q12

### Q10. APM 与 RUM 区别？
- **难度**：🟡 中级
- **关键词**：APM, RUM, 真实用户监控
- **概念速记**：APM 看服务端性能；RUM 看真实用户端体验。
- **参考答案**：APM 监控事务/DB/依赖；RUM 监控首屏/JS 错误/地域延迟。结合全链路看「用户感知慢」vs「服务端慢」。
- **易错点**：只看 APM 忽略用户端实际体验。
- **延伸**：Q4

### Q11. 黑盒监控（Blackbox Exporter）与白盒监控区别？
- **难度**：🟡 中级
- **关键词**：黑盒监控, 白盒, 外部探测
- **概念速记**：白盒从内部暴露；黑盒从外部探测（防假活）。
- **参考答案**：白盒=内部埋点；黑盒=外部探测 HTTP/ICMP/TCP（Blackbox Exporter），模拟用户视角，发现「内部健康但外部不可达」。
- **易错点**：只有白盒，内部健康但入口故障无人知。
- **延伸**：Q4

### Q12. 如何用 Grafana 做高效大盘？
- **难度**：🟡 中级
- **关键词**：Grafana, 大盘设计, 黄金信号
- **概念速记**：大盘按受众分层，黄金信号优先。
- **参考答案**：分层（SRE 总览/业务/组件）；黄金信号优先；模板变量复用；关联跳转（panel→trace/log）；减炫技。告警走 Prometheus/Alertmanager 而非 Grafana 原生。
- **易错点**：把所有指标堆一屏，无人看。
- **延伸**：Q3、Q6

### Q13. 监控数据保留与降采样（downsampling）策略？
- **难度**：🔴 高级
- **关键词**：降采样, 长期存储, Thanos, 冷热分层
- **概念速记**：原始高精短期，长周期降采样省钱。
- **参考答案**：原始短期（15 天），长期降采样（5m/1h 聚合）省钱。Thanos/Cortex/Mimir 长期存储+降采样+全局视图。避免全量长存存储爆炸；冷热分层（对象存储）。
- **易错点**：全量原始数据保留一年，存储爆炸。
- **延伸**：Q1

### Q14. 如何监控「业务指标」而非仅基础设施？
- **难度**：🔴 高级
- **关键词**：业务指标, SLI, 异常检测
- **概念速记**：从「机器活着」升级到「业务健康」。
- **参考答案**：业务埋点（订单量、支付成功率）进 Prometheus/数仓；与 SLI 对齐；业务大盘与异常检测（同比/环比、基线告警）。
- **易错点**：只盯 CPU/内存，业务已跌无人知。
- **延伸**：Q7

### Q15. 合成监控（Synthetic Monitoring）是什么？
- **难度**：🟡 中级
- **关键词**：合成监控, 主动探测, 核心流程
- **概念速记**：用脚本模拟用户关键路径，主动发现问题。
- **参考答案**：定期模拟登录/下单等核心流程，7x24 保障，比用户先发现问题。工具：Grafana Synthetic、Playwright、黑盒探测。
- **易错点**：只做黑盒端口探测，不覆盖业务核心路径。
- **延伸**：Q11

### Q16. OnCall 与 Incident 管理流程？
- **难度**：🔴 高级
- **关键词**：OnCall, Incident, 升级策略, SEV
- **概念速记**：OnCall 轮值派单；Incident 分级指挥。
- **参考答案**：OnCall：轮值、升级（escalation）、去重、静默窗。Incident：分级（SEV1-4）、指挥官（IC）、沟通频道、时间线、复盘。工具自动化派单与 SLA 计时。关注告警疲劳与公平轮值。
- **易错点**：无升级策略，告警无人响应。
- **延伸**：sre Q（复盘、演练）

### Q17. eBPF 在可观测性中的优势？Pixie / Falco / bpftrace？
- **难度**：⚫ 资深
- **关键词**：eBPF, Pixie, Falco, 无侵入
- **概念速记**：eBPF 内核级无侵入采集，开销低覆盖深。
- **参考答案**：Pixie（K8s 自动可观测）、Falco（运行时安全）、bpftrace（脚本追踪）、Cilium Hubble（网络流）。对比传统 agent 更轻更全。
- **易错点**：老内核不支持 eBPF 高级特性。
- **延伸**：network Q16；kubernetes Q34

### Q18. 日志采集架构（Fluent Bit / Filebeat / Vector）怎么选？
- **难度**：🟡 中级
- **关键词**：日志采集, Fluent Bit, Vector, 背压
- **概念速记**：边车/DaemonSet 采集，关注背压与资源。
- **参考答案**：Filebeat（轻、Elastic 生态）；Fluent Bit（极轻、K8s 原生、吞吐高）；Vector（Rust、高性能、变换路由）。关注背压、资源占用、可靠性（至少一次）、多租户隔离。
- **易错点**：采集 agent 资源不设限，反噬业务节点。
- **延伸**：Q5；linux Q17

### Q19. OpenTelemetry Collector 的架构是什么？有哪几种部署模式，怎么选？
- **难度**：🔴 高级
- **关键词**：OTel Collector, receiver/processor/exporter, agent 模式, gateway 模式, 尾部采样
- **概念速记**：Collector 是一条可组装的流水线：**receiver**（收数据，支持 OTLP/Prometheus/Jaeger/Zipkin/filelog 等）→ **processor**（批处理、内存限制、属性增删、采样）→ **exporter**（发往 Prometheus/Tempo/Loki/Kafka/厂商后端），由 **pipeline** 按信号类型（traces/metrics/logs）串起来。
- **参考答案**：
  1. **三种部署形态**：
     | 模式 | 形态 | 适合 |
     |---|---|---|
     | **Agent / DaemonSet** | 每节点一个，就近收集 | 采集主机与容器日志、给数据打节点级标签、降低应用侧开销 |
     | **Sidecar** | 每 Pod 一个 | 需要强隔离或按应用定制处理；成本最高 |
     | **Gateway / Deployment** | 集中一组，接收 agent 汇聚的数据 | 做**需要全局视野**的处理：尾部采样、跨服务聚合、统一鉴权与出口限流 |
     生产常见是 **agent + gateway 两层**：agent 负责就近采集与基础打标，gateway 负责统一策略与后端路由。
  2. **为什么尾部采样必须放 gateway**：头部采样（head sampling）在 trace 开始时就决定采不采，简单但会**丢掉正好出错/慢的那条**；尾部采样（tail sampling）要等一条 trace 的所有 span 都到齐才判断（「有错误就留、P99 慢的留、正常的按 1% 采」）。这要求**同一条 trace 的所有 span 落到同一个 Collector 实例**——所以 gateway 前必须按 `trace_id` 做一致性哈希负载均衡（`loadbalancing` exporter），否则尾部采样直接失效。
  3. **必配的 processor**（漏了会出事故）：
     - `memory_limiter`：**必须放在 pipeline 第一位**，防止后端变慢时 Collector 自己 OOM 把数据全丢。
     - `batch`：批量发送，显著降低后端压力。
     - `resourcedetection` / `k8sattributes`：自动补上 `k8s.pod.name`、`k8s.namespace` 等资源属性，这是后续关联的基础。
  4. **可靠性设计**：Collector 本身要多副本 + HPA；开 `sending_queue` 与磁盘持久化队列应对后端抖动；后端故障时的行为要明确（丢弃还是阻塞），**可观测系统自己不能成为故障放大器**。
  5. **为什么值得上 OTel**：统一的 SDK 与协议（OTLP）让「换后端」不再需要改应用代码；`otelcol` 还能作为 Prometheus 的 remote write 中转与格式转换枢纽，逐步替换存量 agent。
- **易错点**：不配 `memory_limiter`；把尾部采样放在 agent 层导致采样决策错误；gateway 前用普通轮询负载均衡打散了同一条 trace。
- **延伸**：Q4、Q9、Q20、Q22

### Q20. 指标基数爆炸（cardinality explosion）怎么发现、怎么治理？
- **难度**：🔴 高级
- **关键词**：cardinality, 时间序列, label, Prometheus TSDB, 高基数
- **概念速记**：一个指标的时间序列数 = 各 **label 取值的笛卡尔积**。加一个取值 1000 的 label，序列数就 ×1000。Prometheus 的内存、查询延迟与序列数**直接正相关**——基数爆炸是监控系统最常见的自伤型故障。
- **参考答案**：
  1. **典型爆炸源**：`user_id`、`request_id`、`trace_id`、**未归一化的 URL path**（`/order/12345`）、容器 ID、Pod 名（滚动更新时不断产生新值）、错误消息原文、IP 地址。
  2. **怎么发现**：
     ```promql
     # 每个指标名的序列数 TOP
     topk(20, count by (__name__)({__name__=~".+"}))
     # 某指标里哪个 label 基数最高
     count(count by (le, path, pod) (http_request_duration_seconds_bucket))
     ```
     还可以看 `/status/tsdb` 页面（Prometheus 自带 Head Cardinality Stats）、`prometheus_tsdb_head_series` 指标趋势、以及 `scrape_samples_scraped` 突增的 target。
  3. **治理手段（按处理位置由近到远）**：
     - **源头**：应用侧不要把高基数值放进 label，路径先模板化（`/order/{id}`）。
     - **采集侧**：`metric_relabel_configs` 用 `labeldrop`/`drop` 丢掉不需要的 label 与指标；给 target 加 `sample_limit`。
     - **存储侧**：Thanos/Mimir/VictoriaMetrics 有各自的基数限流与按租户配额。
     - **治理机制**：给每个团队设序列数配额并做成看板，新增指标走评审——纯技术手段挡不住持续增长。
  4. **Histogram 是隐藏放大器**：一个 Histogram 的序列数 = `bucket 数 + 2`（`_sum`/`_count`）**再乘以**其他 label 的组合。默认 10+ 个 bucket 意味着 12 倍放大。所以「给 Histogram 加一个 label」的代价远大于给 Counter 加。原生直方图（native histogram）能显著缓解这个问题。
  5. **同类问题在网格里更严重**：Istio 的 `istio_requests_total` 自带大量 label，且指标常驻 Envoy 内存，加高基数 label 会直接把 sidecar 打 OOM（见 service-mesh Q13）。
- **易错点**：只在 Prometheus 侧 drop，应用仍在生成（Envoy/exporter 的内存已经被吃掉了）；不知道 Histogram 的乘数效应；把 Pod 名当作 label 而不用 `service`/`deployment` 这类稳定维度。
- **延伸**：Q2、Q13、service-mesh Q13

### Q21. 怎么观测「服务之间到底在怎么调用」？Kiali / Hubble / service graph 各解决什么？
- **难度**：🟡 中级
- **关键词**：服务拓扑, Kiali, Hubble, 调用关系, 依赖发现
- **概念速记**：拓扑图有三种生成来源，精度与代价各不相同：**指标推导**（从带对端标签的指标聚合）、**流量观测**（eBPF 直接看内核连接）、**追踪聚合**（从 trace 的 span 父子关系还原）。
- **参考答案**：
  1. **Kiali（网格视角）**：数据源是 Istio 的 `istio_requests_total` 等指标——每条指标都带 `source_workload` 和 `destination_service`（靠 Metadata Exchange 拿到，见 service-mesh Q13），按这两个维度聚合就能画出服务图，并叠加成功率、RPS、mTLS 状态。还能做配置校验（等价于 `istioctl analyze` 的可视化）。**局限**：只覆盖被网格纳管的流量。
  2. **Hubble（Cilium / eBPF 视角）**：在内核态直接观测 socket 层流量，**不需要 sidecar、不需要应用改造**，能看到 L3/L4 全量连接（包括没进网格的、被 NetworkPolicy drop 的）。特别适合回答「这条 NetworkPolicy 到底挡了谁」——`hubble observe --verdict DROPPED`。**局限**：L7 解析能力有限（需要额外开启且只支持部分协议）。
  3. **追踪聚合（OTel service graph / Tempo metrics-generator）**：从真实 trace 还原调用链，是**唯一能反映「一次用户请求的完整路径」**的方式，能定位跨服务的长尾延迟。**局限**：依赖埋点覆盖率与采样率，采样低时拓扑会不完整。
  4. **实战用法**：
     - 「有没有没在网格里/没被策略覆盖的流量」→ Hubble。
     - 「服务 A 的下游有哪些、成功率如何」→ Kiali（快、无采样偏差）。
     - 「这次慢在哪一跳」→ 追踪。
     三者是互补关系，成熟平台通常都会有。
  5. **落地价值**：迁移/下线服务前先用拓扑确认「还有谁在调我」；做 NetworkPolicy 默认拒绝前先用观测数据自动生成白名单（Cilium 的 policy 推荐、Kiali 的流量图）——**先观测再收紧**是避免把生产打挂的唯一正确顺序。
- **易错点**：拿低采样率的 trace 画拓扑并当成完整依赖图；只看 Kiali 就以为掌握了全部流量（网格外的看不到）；不做观测直接上 NetworkPolicy 默认拒绝。
- **延伸**：Q9、Q17、kubernetes Q15、service-mesh Q13

### Q22. 三支柱怎么才算「真正打通」？trace_id 关联与 exemplar 是什么？
- **难度**：🔴 高级
- **关键词**：关联, trace_id, exemplar, 语义约定, W3C traceparent
- **概念速记**：把 Metrics/Logs/Traces 三套系统都装上**不等于**可观测性好。真正的价值在于「从一个告警能三次点击跳到根因」，这需要三者之间有**共享的关联键**。
- **参考答案**：
  1. **三条关联链路**：
     - **Metrics → Traces：exemplar**。Prometheus 的 exemplar 允许在直方图的某个 bucket 上附带一个具体的 `trace_id`。于是「P99 延迟涨了」的图上可以直接点进一条**真实的慢请求** trace——这是从「知道有问题」到「看到问题」最短的路径。需要应用 SDK 支持（OTel 默认支持）、Prometheus 开 `--enable-feature=exemplar-storage`、Grafana 配好 data source 链接。
     - **Traces → Logs**：日志里必须打印 `trace_id` / `span_id`（结构化日志字段，不是拼在消息里）。Loki/ES 按 trace_id 一查就能拿到这次请求的全部日志。
     - **Logs → Traces**：反向同理，从一条报错日志跳回完整调用链。
  2. **前提一：上下文传播**。跨服务必须传递 **W3C `traceparent`** header（OTel 默认格式）。常见断链点：
     - 消息队列（要在消息属性里手动带上 context）。
     - 线程池/异步任务（context 没跟着切换）。
     - 老的网关或中间件把未知 header 剥掉。
     - 不同框架用了不同传播格式（B3 vs W3C）没配互转。
  3. **前提二：统一的资源属性**。三种信号上都要有相同的 `service.name`、`k8s.namespace.name`、`deployment.environment` 等 —— 遵循 **OTel 语义约定（semantic conventions）**，否则字段名对不上就无法跨信号跳转。这正是 OTel 相比各自为政的 agent 的核心价值。
  4. **成本控制的正确做法**：Traces 用**尾部采样**（保留错误与慢请求，见 Q19）；Logs 分级（错误全留、访问日志抽样或只留聚合）；Metrics 控基数（见 Q20）。**指标永远全量**（便宜、适合告警），trace 和 log 按需，三者分工明确。
  5. **验收标准**：拿一个真实的线上告警走一遍——从告警 → 指标图 → exemplar 点进 trace → 从 span 跳到对应日志。**走不通就是没打通。**
- **易错点**：三套系统各自为政，字段名不统一，人肉在三个 UI 之间按时间戳对；日志里没有 trace_id；只做了 head sampling 导致出错的 trace 恰好没被采到。
- **延伸**：Q4、Q9、Q19、Q20

### Q23. Falco 的运行时安全生态怎么落地？从内核探针到告警响应，一条完整链路上有哪些组件？
- **难度**：🔴 高级
- **关键词**：Falco, 系统调用, eBPF probe / 内核模块, falco_rules, Falcosidekick, Falcosidekick UI, falcoctl, 响应引擎, k8s audit
- **概念速记**：
  - **Falco**：CNCF 毕业的运行时安全项目，在**内核层解析系统调用**（syscall），按规则实时判断容器 / 主机 / K8s 里的可疑行为并出告警。数据源除 syscall 外还有 **K8s audit 事件**（`k8s_audit_rules.yaml`）与插件（Cloudtrail 等）。
  - **驱动（driver）**：拿到 syscall 的方式有三种——**内核模块**、**eBPF probe**（`falco-driver-loader bpf`）、以及更新的 **modern eBPF**（CO-RE，免编译）。捐给 CNCF 的正是内核模块、eBPF probe 与 libs（libsinsp/libscap）。
- **问题**：团队要在 K8s 上把 Falco 从「装上」做到「告警能被人处理、还能自动响应」，请描述这条链路上的组件、规则怎么管、告警往哪送，以及有哪些坑。
- **参考答案**：
  1. **部署形态**：Falco 以 **DaemonSet** 每节点一个，Helm 装（`falcosecurity/falco`）；节点直装时配置在 `/etc/falco/`。选驱动：新内核优先 **modern eBPF**（免编译、少踩内核版本坑），否则 eBPF probe 或内核模块。
  2. **规则管理**：内置 `falco_rules.yaml`，本地覆盖放 `falco_rules.local.yaml`，K8s 审计规则 `k8s_audit_rules.yaml`；规则由 **宏（macro）+ 列表（list）+ 规则（rule）** 组成，输出字段可自定义（如 `[%evt.time][%container.id] [%container.name]`）。典型规则：容器内起交互 shell、写敏感目录、读 `/etc/shadow`、意外的出站连接、挂载穿透。**falcoctl** 做规则 / 插件的分发与版本管理。
  3. **告警外发（关键的一环）**：Falco 本身只产生事件，**Falcosidekick** 是扇出网关，把告警转发到 Slack、PagerDuty、Kafka、AWS Lambda、Elasticsearch、Loki、SIEM 等几十种后端；**Falcosidekick UI** 给一个轻量的事件查看界面。没有 sidekick 时告警只落 stdout/syslog，容易没人看。
  4. **响应引擎（自动处置）**：Falcosidekick + **response engine**（如 Falco Talon）可按规则联动动作——给 Pod 打隔离标签、加 NetworkPolicy、`kubectl delete`/缩容到零做取证、终止进程。要点是**先审计后处置**，自动删 Pod 前想清楚会不会误杀。
  5. **与可观测 / 安全体系对齐**：Falco 事件带 MITRE ATT&CK 语义，正好和 RBAC 攻击面审计（cloud-security Q17）对齐——审计告诉你「哪条路径可达」，Falco 告诉你「有人正在走这条路径」。事件应进 SIEM 长期留存并接 on-call。
  6. **坑**：规则过多 / 太宽导致**告警风暴**没人看（和 observability Q6 的抑制 / 分组同理）；驱动与内核版本不匹配导致 Falco 起不来（modern eBPF 缓解）；只装 Falco 不接 sidekick 等于没有告警通路；把 syscall 规则和 k8s audit 规则混为一谈（数据源不同）。
- **易错点 / 面试官关注**：
  - 以为「装了 Falco 就安全了」，说不出告警外发与响应这半条链路。
  - 分不清三种驱动的取舍；不知道 modern eBPF。
  - 不会把运行时检测（Falco）与静态 RBAC 审计、准入拦截放在纵深防御里各就各位。
- **延伸**：Q6（告警抑制）、Q17（eBPF）、cloud-security Q10、Q15、Q17、来源：[developer-guy/awesome-falco](https://github.com/developer-guy/awesome-falco)（Falco 官方项目、社区工具与文章的清单）、[Falco 官方文档](https://falco.org/docs/)
