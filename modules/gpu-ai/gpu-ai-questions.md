# GPU / AI 运维面试题（26 题）

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

### Q21. HAMi 是什么？它怎么实现 GPU 显存与算力的细粒度切分？
- **难度**：🔴 高级
- **关键词**：HAMi, vGPU, gpumem, gpucores, 显存超配, CNCF Sandbox
- **概念速记**：**HAMi**（Heterogeneous AI Computing Virtualization Middleware，前身 k8s-vGPU-scheduler，CNCF Sandbox 项目）是异构设备管理中间件，让**一张物理卡被多个容器安全共享**，且对 CUDA 应用**零侵入**。
- **参考答案**：
  1. **组件构成**（都是 K8s 原生扩展点，理解了就好记）：
     - **Admission Webhook**：拦截并改写 Pod spec，注入设备需求、校验资源请求。
     - **Scheduler Extender**（hami-scheduler）：做设备感知的节点过滤与打分。
     - **Device Plugin**（hami-device-plugin）：节点侧管理设备、向 kubelet 上报。
     - **ConfigMap**：存设备参数与调度策略。
  2. **资源申请维度**（相比原生只能 `nvidia.com/gpu: 1`）：
     - `nvidia.com/gpu`：虚拟 GPU 实例数
     - `nvidia.com/gpumem`：显存 MB（硬限制，容器只能看到/用到这么多）
     - `nvidia.com/gpumem-percentage`：按百分比分配显存
     - `nvidia.com/gpucores`：SM 计算核心百分比
  3. **调度策略**：节点级 `binpack`（集中，利于装箱率）/`spread`（分散，利于容错）；GPU 级 `binpack`（多任务共享单卡）/`spread`（分散到多卡）；支持 NUMA 与互联拓扑感知；可按 UUID、设备型号过滤。Pod 注解 `hami.io/gpu-scheduler-policy` 可单独覆盖全局策略。
  4. **和 MIG / MPS / time-slicing 的关系**（面试常被追问）：
     | 方案 | 隔离强度 | 灵活度 | 限制 |
     |---|---|---|---|
     | **MIG** | 硬件级隔离，最强 | 只有固定几种切分规格 | 仅 A100/H100 等支持 |
     | **MPS** | 无显存隔离 | 并发性能好 | 一个进程崩溃可能影响其他 |
     | **time-slicing** | 无隔离，纯分时 | 最简单 | 显存互相挤占、无 QoS |
     | **HAMi** | 软件层显存硬限 + SM 配额 | 任意比例、跨厂商 | 有一定拦截开销，非硬件级隔离 |
  5. **多厂商**：插件化架构，除 NVIDIA 外还支持昇腾 NPU、寒武纪 MLU、海光 DCU 等——这是国产化环境里选它的主要理由。
  6. **注意**：支持**显存超配**（比例 >1.0），但超配意味着真实争抢时会 OOM，要配合监控和任务优先级使用。
- **易错点**：以为 HAMi 是硬件级隔离（它是软件层拦截 CUDA 调用）；开了显存超配却没做 OOM 防护；在支持 MIG 的卡上盲目用软件切分而放弃更强的硬件隔离。
- **延伸**：Q2、Q3、Q18、kubernetes Q45、来源：[Kubernetes Handbook - HAMi](https://jimmysong.io/book/kubernetes-handbook/ai-native-hami/)

### Q22. 为什么说「K8s 不理解硬件拓扑」会悄悄拖慢 GPU 训练？怎么修？
- **难度**：⚫ 资深
- **关键词**：拓扑感知调度, NUMA, PCIe switch, GPUDirect RDMA, Kueue, 性能静默退化
- **概念速记**：现代 AI 服务器（HGX H100/H200）是 NUMA 架构：两个 CPU socket、各自的本地内存与 PCIe 通道，多个 PCIe switch 下挂 GPU 和 RDMA 网卡。**跨 socket 通信要走 UPI/Infinity Fabric，明显慢于同一 PCIe 层级内通信。**
- **参考答案**：
  1. **默认调度器看不到的东西**：K8s scheduler 只认识 CPU/内存/存储和「资源数量」。当 Pod 写 `nvidia.com/gpu: 2`，调度流程只是「找到有 2 张空闲卡的节点 → 分配」，它**从不询问**：这两张卡在同一个 PCIe switch 下吗？和网卡同 NUMA 吗？RDMA 流量会跨 socket 吗？
  2. **静默退化的典型场景**：一台机器 GPU0/1 挂在 PCIe Switch A，GPU2/3 挂在 Switch B。任务要 2 卡，调度器给了 **GPU1 + GPU2** —— 两张卡都在、请求也满足、**什么都没报错**，但 NCCL 通信要跨 switch 和 CPU 互联，AllReduce 带宽腰斩。**没有告警、没有失败，只有账单变贵、训练变慢。**
  3. **GPUDirect RDMA 为什么对拓扑敏感**：正常路径是 `GPU → CPU 内存 → 内核 → NIC`；GPUDirect RDMA 让 GPU 显存与网卡直接 DMA，跳过 CPU 和内核拷贝。但这个优化**只有在 GPU 和 NIC 挂在同一 PCIe root complex 下才能发挥**，跨 NUMA 时收益大幅衰减甚至失效。
  4. **修复手段（组合拳，单独一个都不够）**：
     - **Topology Manager** 设 `single-numa-node` + `pod` scope，让 kubelet 把 CPU、GPU、网卡对齐到同一 NUMA（见 kubernetes Q46）。
     - **NVIDIA Device Plugin** 开启拓扑感知分配，让它优先给出同 switch 下的卡组合。
     - **Kueue**（或 Volcano）做作业级排队与 gang scheduling，保证整组 Pod 一起落到拓扑友好的位置。
     - **Multus + NVIDIA Network Operator** 给 Pod 挂上与 GPU 同 NUMA 的 RDMA 网卡（NetworkAttachmentDefinition）。
     - **HAMi** 等调度中间件也提供拓扑感知打分。
  5. **怎么验证**：`nvidia-smi topo -m` 看卡间连接矩阵（NV# > PIX > PXB > NODE > SYS，越靠后越慢）；用 `nccl-tests`（all_reduce_perf）实测总线带宽，对比理论值；`numactl -H` + `lstopo` 看设备的 NUMA 归属。
- **易错点**：只盯 GPU 利用率不看通信带宽，错过拓扑问题；以为配了 Topology Manager 就万事大吉（还需要 Guaranteed QoS 和设备插件配合）；忽略网卡的 NUMA 归属。
- **延伸**：Q5、Q7、Q19、kubernetes Q46、linux Q10、来源：[Why Kubernetes Is Slowing Down Your GPUs](https://mananpaliwal.medium.com/why-kubernetes-is-slowing-down-your-gpus-and-how-topology-aware-scheduling-fixes-it-214d628c094c)

### Q23. vLLM 为什么快？PagedAttention 和 continuous batching 分别解决什么？
- **难度**：🔴 高级
- **关键词**：PagedAttention, KV cache, continuous batching, 显存碎片, 吞吐 vs 延迟
- **概念速记**：LLM 推理的瓶颈不是算力而是**显存与调度**：每个请求都要维护随生成长度增长的 **KV cache**，传统实现为它预分配「最大长度」的连续显存，浪费极大。
- **参考答案**：
  1. **PagedAttention**——把操作系统的**虚拟内存分页**思想搬到 KV cache：
     - KV cache 切成固定大小的 block，**物理上不要求连续**，用一张 block table 做逻辑→物理映射。
     - 消除内部碎片（不用按 max_len 预分配）与外部碎片，显存利用率大幅提升 → 同样显存能装下更多并发请求。
     - 附带好处：多个请求共享相同前缀（如同一个 system prompt、beam search 的多个分支）时可以**共享物理 block**（copy-on-write），进一步省显存。
  2. **Continuous batching（又称 in-flight batching）**——解决**调度**问题：
     - 传统静态 batching 要等整批请求都生成完才能换下一批，短请求被长请求拖住，GPU 大量时间空转。
     - Continuous batching 以 **token 为粒度**调度：某个请求生成结束就立刻把它移出、把排队的新请求填进来，batch 始终是满的 → 吞吐大幅提升。
  3. **运维视角的关键参数与权衡**：
     - `gpu_memory_utilization`：留给 KV cache 的显存比例，调高提升并发但逼近 OOM。
     - `max_num_seqs` / `max_num_batched_tokens`：并发上限，**吞吐与单请求延迟（TTFT/TPOT）是此消彼长**的，要按业务 SLO 定。
     - 张量并行 `tensor_parallel_size`：单卡放不下才用，会引入卡间通信，受 Q22 的拓扑影响。
     - **Prefix caching**：多轮对话/固定 system prompt 场景收益巨大。
  4. **关键监控指标**：TTFT（首 token 延迟）、TPOT（每 token 延迟）、吞吐（tokens/s）、KV cache 使用率、等待队列长度、抢占（preemption）次数——**抢占次数上升说明显存不够，是扩容信号**。
  5. **和 TGI / TensorRT-LLM 的取舍**：vLLM 通用性与社区最好；TensorRT-LLM 在 NVIDIA 卡上单机性能更强但编译与版本绑定重；按「团队运维能力 + 模型更新频率」选。
- **易错点**：只关心 GPU 利用率，不看 KV cache 使用率和抢占次数；把 `gpu_memory_utilization` 拉到 0.98 导致偶发 OOM；不区分 TTFT 与 TPOT 就谈「延迟」。
- **延伸**：Q8、Q9、Q11、Q12

### Q24. 部署一个大模型推理服务，怎么估算显存需求？
- **难度**：🔴 高级
- **关键词**：权重显存, KV cache 显存, 量化, 激活显存, 容量规划
- **概念速记**：推理显存 ≈ **模型权重 + KV cache + 激活/框架开销**，三者中 KV cache 是**唯一随并发和上下文长度增长**的部分，也是容量规划的核心变量。
- **参考答案**：
  1. **权重显存**：`参数量 × 每参数字节数`。
     - FP16/BF16 = 2 bytes → 7B ≈ 14GB，70B ≈ 140GB。
     - INT8 ≈ 1 byte → 70B ≈ 70GB；INT4 ≈ 0.5 byte → 70B ≈ 35GB。
     - 经验口径：**「参数量(B) × 2」GB 就是 FP16 权重的近似值**，面试口算够用。
  2. **KV cache 显存**（关键公式）：
     ```
     KV = 2 (K和V) × layers × kv_heads × head_dim × 序列长度 × 精度字节 × 并发数
     ```
     - 注意是 `kv_heads` 而非 `heads`——**GQA/MQA** 通过减少 KV 头数把这一项砍掉数倍，是现代模型能支持长上下文的关键。
     - 直觉：长上下文 + 高并发时，KV cache 可以轻松**超过权重本身**。
  3. **其他开销**：激活值、CUDA context、框架缓冲、碎片——工程上按总量再留 **10%～20% 余量**。
  4. **容量规划的正确姿势**：
     - 先定业务 SLO（P99 TTFT、并发数、平均/最大上下文长度）。
     - 算出权重 + 目标并发下的 KV cache → 选卡型与张量并行度。
     - **压测校准**：理论值只是起点，真实吞吐必须用生产 prompt 分布实测。
  5. **成本优化杠杆**（按性价比排序）：量化（INT8/INT4，注意精度损失要评测）→ prefix caching → 合理的 max 上下文限制（不要无脑开 128k）→ 多模型共卡（见 Q21）→ 动态扩缩容（KEDA 按队列长度）。
- **易错点**：只算权重忘了 KV cache，上线后一有并发就 OOM；用 `heads` 而非 `kv_heads` 算 GQA 模型，结果高估数倍；不留碎片余量。
- **延伸**：Q8、Q12、Q23

### Q25. 用 DCGM Exporter 之外，AI 平台还该监控什么？怎么判断训练任务「不健康」？
- **难度**：🔴 高级
- **关键词**：DCGM, XID, SM 占用率, NCCL, 慢节点 straggler, checkpoint
- **概念速记**：GPU 利用率（`DCGM_FI_DEV_GPU_UTIL`）**是个骗人的指标**——它只表示「有 kernel 在跑」，不表示跑得有多满。一个反复跑微小 kernel 的低效任务也能显示 100%。
- **参考答案**：
  1. **该看的 GPU 层指标**：
     - `DCGM_FI_PROF_SM_OCCUPANCY` / `PIPE_TENSOR_ACTIVE`：真实的 SM 占用与 Tensor Core 利用率，**这才反映算力是否吃满**。
     - `DCGM_FI_DEV_FB_USED/FREE`：显存水位。
     - `DCGM_FI_DEV_GPU_TEMP` / `POWER_USAGE` / **`SM_CLOCK`**：温度过高或功耗墙触发**降频**时，SM_CLOCK 会掉——这是「任务突然变慢但代码没改」的常见原因。
     - `DCGM_FI_DEV_XID_ERRORS`：硬件/驱动错误码，需重点告警（如 Xid 48/63/64 ECC 错误、Xid 79 GPU 掉卡）。
     - `DCGM_FI_PROF_NVLINK_*` / PCIe 带宽：判断通信瓶颈。
  2. **任务层指标（GPU 指标看不出来的）**：
     - 每步耗时（step time）与其**方差**——方差变大往往意味着出现**慢节点（straggler）**，分布式训练会被最慢的那个拖住。
     - 数据加载耗时占比：GPU 等数据是低利用率的头号原因（dataloader workers 不够、存储 IO 慢）。
     - NCCL 通信耗时占比与 AllReduce 带宽。
     - checkpoint 保存耗时与成功率。
     - loss 是否为 NaN / 不下降——「任务在跑但没在学」。
  3. **健康判定的实操做法**：
     - 定义「有效算力利用率」= Tensor Core 活跃时间占比，而非 GPU_UTIL。
     - 对每个任务建立 step time 基线，偏离阈值告警。
     - 慢节点检测：同一 job 内各 rank 的 step time 做离群检测，自动标记并驱逐问题节点。
     - XID 错误自动打 taint 隔离节点，避免下一个任务又调度上去。
  4. **成本视角**：把「GPU 卡时 × 有效利用率」做成看板，按团队/项目分摊——这是推动业务方自己优化的最有效手段。
- **易错点**：只看 GPU_UTIL 就宣称「利用率 90%，很健康」；不监控 SM_CLOCK，错过散热/功耗导致的降频；XID 错误只记日志不隔离节点。
- **延伸**：Q7、Q10、Q17、Q18、observability Q14

### Q26. AI 推理服务怎么做弹性伸缩？为什么 HPA 的 CPU 指标在这里没用？
- **难度**：🔴 高级
- **关键词**：KEDA, 队列长度, 冷启动, 模型加载, 缩容到零
- **概念速记**：推理服务的负载特征与传统 Web 服务完全不同：**扩容代价极高**（拉几十 GB 镜像 + 加载模型到显存，分钟级冷启动），而 CPU 使用率与真实负载几乎无关。
- **参考答案**：
  1. **为什么 CPU/内存指标失效**：推理的瓶颈在 GPU 和 KV cache，进程 CPU 可能一直很低；GPU 利用率又因为 continuous batching 而长期接近饱和（见 Q23），**无法反映「排队有多严重」**。
  2. **该用什么指标**（按优先级）：
     - **等待队列长度 / 排队时间**——最直接反映「供不应求」。
     - **KV cache 使用率**与**抢占次数**——显存快满说明并发到顶。
     - **P99 TTFT**——直接对应用户体验的 SLO。
     用 **KEDA** 按这些自定义指标（Prometheus scaler）扩缩，比原生 HPA 的 CPU/内存合适得多。
  3. **冷启动是最大难题，解法组合**：
     - **镜像瘦身 + 预拉取**：模型权重不打进镜像，放共享存储/OCI artifact；节点预热镜像（DaemonSet 或 `imagePullPolicy` 配合预拉）。
     - **模型缓存层**：权重放本地 NVMe 缓存或用 Fluid/JuiceFS 这类数据编排加速，避免每次从对象存储拉几十 GB。
     - **预留缓冲容量**：保持 1～2 个 warm 副本（低优先级 Pod 占位，用 PriorityClass 让真实流量来时抢占），用确定性的成本换确定性的延迟。
     - **提前扩容**：基于时间序列预测（业务有明显日周期时）在流量到来前扩，而不是事后追。
  4. **缩容到零**：离线/低频场景可用 Knative 或 KEDA 的 `minReplicaCount: 0`，但必须接受首个请求的分钟级延迟，或在网关层做排队提示。
  5. **配套设置**：`stabilizationWindowSeconds` 设大（避免抖动导致反复加载模型）；缩容比扩容更保守；PDB 保证滚动更新时不会同时下线过多副本。
- **易错点**：直接套用 Web 服务的 CPU HPA；缩容窗口太短导致「扩了又缩、模型反复加载」；忽略冷启动把 `minReplicas` 设成 0 后被投诉超时。
- **延伸**：Q11、Q18、Q23、kubernetes Q6、Q36
