# 监控 / 可观测性面试题（18 题）

> 模板见 [../../docs/STANDARD.md](../../docs/STANDARD.md)。

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
