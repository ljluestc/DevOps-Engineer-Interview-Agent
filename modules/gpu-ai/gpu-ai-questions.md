# GPU / AI 运维面试题（20 题）

> 模板见 [../../docs/STANDARD.md](../../docs/STANDARD.md)。基础概念见 [../../basics/06-ai-gpu-basics.md](../../basics/06-ai-gpu-basics.md)。

---

### Q1. NVIDIA GPU 核心概念：CUDA / 显存 / SM / Compute Capability？
- **难度**：🟡 中级
- **关键词**：CUDA, HBM, SM, Compute Capability
- **概念速记**：SM=流处理器（含 Tensor Core）；Compute Capability=架构代际（Ampere=8.x、Hopper=9.0）。
- **参考答案**：CUDA=并行计算平台；SM 含 CUDA Core+Tensor Core；显存（HBM）容量与带宽皆瓶颈；Compute Capability 决定特性（如 Hopper FP8/Transformer Engine）。
- **易错点**：以为显存大就够，忽略带宽与碎片。
- **延伸**：[basics/06-ai-gpu-basics.md](../../basics/06-ai-gpu-basics.md)；Q2

### Q2. GPU 虚拟化/切分：MIG / MPS / time-slicing / vGPU 区别？
- **难度**：🔴 高级
- **关键词**：MIG, MPS, time-slicing, vGPU, 隔离
- **概念速记**：MIG 硬件级强隔离；MPS 无隔离提效但危险。
- **参考答案**：MIG（A100/H100 硬件切分，独立显存/算力，强隔离，多租户）；MPS（共享上下文，提效但一崩全崩）；time-slicing（分时复用整卡，无显存隔离）；vGPU（虚拟化，需 license）。选型：隔离 vs 利用率。
- **易错点**：把 MPS 当隔离方案给多租户用。
- **延伸**：Q3、Q9

### Q3. K8s 里 Pod 如何用 GPU？Device Plugin 机制？
- **难度**：🔴 高级
- **关键词**：Device Plugin, nvidia-container-toolkit, 资源申请
- **概念速记**：节点装驱动 + toolkit + device-plugin，Pod 申请 nvidia.com/gpu。
- **参考答案**：节点装驱动 + `nvidia-container-toolkit` + `k8s-device-plugin`（DaemonSet，上报 `nvidia.com/gpu`）。Pod 申请 `nvidia.com/gpu: 1`（整卡；MIG 资源名不同）。调度由 kubelet device plugin 分配，容器运行时挂 GPU 设备。多卡写 `2` 或 MIG。
- **易错点**：节点未装 device-plugin，Pod 一直 Pending。
- **延伸**：[basics/04-kubernetes-concepts.md](../../basics/04-kubernetes-concepts.md)；Q2

### Q4. 容器跑 CUDA，驱动版本与 CUDA 工具包版本兼容规则？
- **难度**：🟡 中级
- **关键词**：驱动, CUDA toolkit, 向后兼容
- **概念速记**：驱动决定支持的最高 CUDA 版本，向后兼容。
- **参考答案**：宿主机驱动决定上限，容器内 CUDA Toolkit ≤ 驱动上限即可。报错 `CUDA driver version is insufficient` → 镜像 CUDA 高于驱动支持。用 `nvidia/cuda:<ver>-runtime` 基础镜像。
- **易错点**：升级镜像 CUDA 版本不升驱动导致起不来。
- **延伸**：Q1；[basics/06-ai-gpu-basics.md](../../basics/06-ai-gpu-basics.md)

### Q5. 大模型训练/推理为何用 IB / RDMA？NCCL 是什么？
- **难度**：🔴 高级
- **关键词**：IB, RDMA, NCCL, 集合通信
- **概念速记**：多卡通信靠集合通信，TCP 成瓶颈；IB+RDMA 低延迟高带宽。
- **参考答案**：多卡/多机靠 AllReduce/AllGather 同步梯度，TCP/Ethernet 瓶颈。IB+RDMA（绕过 CPU/内核，零拷贝）低延迟高带宽。NCCL 是 GPU 间集合通信库，自动选拓扑（NVLink/IB），`NCCL_DEBUG=INFO` 排查。
- **易错点**：用普通以太跑多机训练，通信成主要瓶颈。
- **延伸**：Q6（NVLink）、Q7（利用率）

### Q6. NVLink / NVSwitch 是什么？相比 PCIe 的优势？
- **难度**：🔴 高级
- **关键词**：NVLink, NVSwitch, HGX, 互联带宽
- **概念速记**：GPU 间高速互联，带宽远高于 PCIe。
- **参考答案**：NVLink GPU 间高速互联；NVSwitch 多卡全网交换（HGX 8 卡全互联）。优势：训练多卡通信不再受 PCIe 瓶颈，AllReduce 大幅加速。运维看拓扑（`nvidia-smi topo -m`）、NVLink 故障影响。
- **易错点**：忽略 NVLink 故障导致多卡通信失败。
- **延伸**：Q5

### Q7. 训练任务 GPU 利用率低（如仅 30%）怎么排查？
- **难度**：🔴 高级
- **关键词**：GPU 利用率, 数据加载, 通信瓶颈, py-spy
- **概念速记**：低利用率多为数据加载/通信/CPU 预处理瓶颈，而非算力不足。
- **参考答案**：瓶颈：① 数据加载慢（DataLoader 线程/预处理/存储 IO）→ 加 num_workers/prefetch、更快存储；② 通信开销（NCCL/IB）；③ CPU 预处理瓶颈；④ 混合精度/梯度累积配置不当；⑤ 日志/checkpoint 频繁写盘。用 `nvidia-smi dmon`/`dcgm-exporter`/`py-spy` 定位。
- **易错点**：直接加卡不解决数据加载瓶颈。
- **延伸**：Q5、Q8（显存 OOM）

### Q8. GPU 显存 OOM 怎么排查与缓解？
- **难度**：🔴 高级
- **关键词**：显存 OOM, PagedAttention, 梯度检查点, ZeRO
- **概念速记**：显存碎片与容量都会 OOM；推理用 PagedAttention 省碎片。
- **参考答案**：定位：`nvidia-smi`、`torch.cuda.memory_summary()`。缓解：① 减小 batch；② 梯度检查点（时间换显存）；③ 混合精度/FP8；④ 模型/张量并行切分（推理用 vLLM PagedAttention）；⑤ 及时释放引用；⑥ ZeRO 优化器分片。
- **易错点**：只减小 batch 不解决碎片（需 PagedAttention 类方案）。
- **延伸**：Q7、Q10（vLLM）

### Q9. vLLM / TGI 相比裸模型服务解决了什么？
- **难度**：🔴 高级
- **关键词**：vLLM, PagedAttention, 连续批处理, 吞吐
- **概念速记**：vLLM 用 PagedAttention 消除 KV cache 碎片，大幅提升利用率。
- **参考答案**：核心吞吐与显存利用。vLLM PagedAttention 分页管理 KV cache 消除碎片、continuous batching 动态组批；TGI 提供张量并行/量化/流式。运维关注实例数、显存、KV cache 上限、队列、P99、多模型路由。
- **易错点**：裸推理不重视 KV cache 碎片，并发上不去。
- **延伸**：Q8、Q11（推理架构）

### Q10. 如何监控 GPU 集群？DCGM Exporter 关键指标？
- **难度**：🟡 中级
- **关键词**：DCGM, Prometheus, GPU 指标, 告警
- **概念速记**：dcgm-exporter 把 GPU 指标暴露给 Prometheus。
- **参考答案**：关键指标：利用率 `DCGM_FI_DEV_GPU_UTIL`、显存 `FB_USED`、温度/功耗、NVLink 带宽、ECC 错误 `DCGM_FI_DEV_ECC_DBE`、XID 错误。配合 Node Exporter、容器指标做大盘与告警。
- **易错点**：只监控 GPU 利用率，忽略温度/ECC/XID 故障前兆。
- **延伸**：observability Q；analytics Q（监控）

### Q11. 推理服务架构（网关 / 路由 / 批处理 / 多模型）？
- **难度**：⚫ 资深
- **关键词**：推理架构, 网关, 动态批处理, 多模型路由
- **概念速记**：入口网关→推理引擎→多模型实例，关注排队与成本。
- **参考答案**：入口网关（鉴权/限流/路由）→ 推理引擎（vLLM/Triton/TGI）→ 多模型实例（按热度扩缩）。关注请求排队、动态批处理、流式输出、KV cache、多 LoRA 共享、GPU 分片（MIG）、冷启动、成本计量（token）。
- **易错点**：无排队与限流，突发打满显存致 OOM。
- **延伸**：Q9、Q12（成本）

### Q12. 大模型推理成本怎么估算（token / 显存 / 算力）？
- **难度**：⚫ 资深
- **关键词**：推理成本, token, KV cache, FinOps
- **概念速记**：成本≈算力×单价 + 显存决定卡数与并发。
- **参考答案**：成本随上下文长度线性涨显存（KV cache）；优化：量化（INT8/FP8）、投机解码、批处理、上下文截断、路由小模型。FinOps 视角看 token 单价。
- **易错点**：忽略长上下文 KV cache 导致显存爆炸与成本陡增。
- **延伸**：Q8、Q9、cloud-security Q（FinOps）

### Q13. MoE（混合专家）模型对基础设施的特殊要求？
- **难度**：⚫ 资深
- **关键词**：MoE, 专家路由, 显存, NVLink
- **概念速记**：MoE 稀疏激活，显存大但单步算力低，需高带宽。
- **参考答案**：要求大显存（所有专家常驻）、高带宽（专家路由通信）、负载均衡（专家不均致热点）、调度需感知拓扑。运维关注 expert 分布与 NVLink 利用。
- **易错点**：专家不均导致部分 GPU 热点、整体利用率低。
- **延伸**：Q6、Q11

### Q14. 向量数据库（Milvus / pgvector / ES）在 RAG 中的运维？
- **难度**：🔴 高级
- **关键词**：向量数据库, RAG, 索引, 召回率
- **概念速记**：RAG 用向量检索召回知识，索引类型权衡召回与性能。
- **参考答案**：索引（HNSW/IVF）权衡召回率/性能；向量维度与存储、QPS 与延迟、与 LLM 服务链路、embedding 版本一致性。Milvus 分布式；pgvector 简单但规模有限。
- **易错点**：embedding 模型升级后旧向量不兼容，召回失真。
- **延伸**：Q11

### Q15. MLOps / 模型生命周期管理？
- **难度**：⚫ 资深
- **关键词**：MLOps, 实验追踪, 模型注册, 漂移
- **概念速记**：区别于 DevOps：数据版本、模型可复现、漂移检测。
- **参考答案**：实验追踪（MLflow）、数据/模型版本、流水线（训练/评估/注册）、部署（推理服务）、监控（漂移/质量/成本）、回滚。平台化（KubeFlow/MLflow/自研）。
- **易错点**：只管部署不管漂移，模型质量悄悄下降。
- **延伸**：Q11、Q15（k8s 调度）

### Q16. AI 平台的安全与合规（模型安全 / 越狱 / 数据隐私）？
- **难度**：⚫ 资深
- **关键词**：模型安全, 越狱, 数据隐私, 合规
- **概念速记**：网关层防护 + 租户隔离 + 审计。
- **参考答案**：防越狱/提示注入、输出过滤、内容安全；训练数据脱敏、PII 不落盘、租户隔离；合规：模型备案、审计日志、可追溯。运维参与网关防护、配额、日志留存、漏洞扫描。
- **易错点**：只防外部攻击忽略租户间数据泄露。
- **延伸**：cloud-security Q；Q15

### Q17. GPU 常见硬件故障与表现？XID / ECC 错误处理？
- **难度**：🔴 高级
- **关键词**：XID, ECC, 掉卡, RMA
- **概念速记**：XID=GPU 上报错误码（如 79 掉卡）；ECC=显存位翻转。
- **参考答案**：XID 错误（如 79 GPU 掉卡，需换/重插）；ECC 错误（单/双位，DBE 不可纠正预示老化）；NVLink 故障致通信失败。处理：cordon 隔离、迁移任务、收集 `nvidia-bug-report`、RMA、记故障库。运维要自动识别+摘流+工单。
- **易错点**：故障卡未隔离，任务反复调度到坏卡。
- **延伸**：Q10、Q3

### Q18. 如何提升 GPU 集群利用率、降低成本？
- **难度**：⚫ 资深
- **关键词**：GPU 利用率, 分时调度, 混部, MIG
- **概念速记**：看利用率/单价/闲置率三件套。
- **参考答案**：① 分时调度（训练夜、推理昼，Volcano/Kueue 队列）；② 弹性推理（按需扩缩、潮汐）；③ 混部（在线+离线，QoS 隔离）；④ MIG 细粒度切分；⑤ 批处理/量化降显存；⑥ 闲置检测回收；⑦ 多租户配额优先级。
- **易错点**：只降单价不降闲置率，整体成本仍高。
- **延伸**：Q2、Q12、cloud-security Q（FinOps）

### Q19. 训练任务调度为何用 Volcano / KubeFlow？与传统调度差异？
- **难度**：⚫ 资深
- **关键词**：Volcano, Gang 调度, podgroup, 容错训练
- **概念速记**：训练需 Gang 调度（一组 Pod 同时起），原生 K8s 不满足。
- **参考答案**：训练需 Gang 调度（一组 Pod 必须同时起，否则全失败重来，防碎片死锁），需队列/优先级/公平/Checkpoint 容错。原生 K8s 不满足，Volcano 提供 podgroup+gang、Queue、抢占；KubeFlow 提供 TFJob/PyTorchJob CRD，支持弹性/容错训练。
- **易错点**：用原生 Deployment 跑分布式训练，资源不足时碎片死锁。
- **延伸**：Q3、kubernetes Q（调度）

### Q20. 分布式训练并行策略：DP / TP / PP / ZeRO？
- **难度**：⚫ 资深
- **关键词**：数据并行, 模型并行, 流水线并行, ZeRO
- **概念速记**：DP 最常用；TP/PP 切模型；ZeRO 分片优化器状态。
- **参考答案**：数据并行（DP，多副本各吃数据分片，梯度同步）；张量并行（TP，切张量，单卡放不下用）；流水线并行（PP，切层段跨设备）；ZeRO（优化器/梯度/参数分片，降显存）。混合并行（3D）是超大模型常态。
- **易错点**：不理解通信量差异，并行策略选错导致瓶颈在通信。
- **延伸**：Q5、Q6、Q19
