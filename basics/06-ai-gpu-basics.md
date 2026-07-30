# 06 · AI / GPU 基础深度篇

> 关键词：CUDA、显存（HBM）、SM、Tensor Core、Compute Capability、MIG/MPS、Device Plugin、IB/RDMA/NCCL、NVLink、vLLM/PagedAttention、DCGM

---

## 1. GPU 是什么，和 CPU 有何不同

- **CPU**：少数强核心，擅长串行、低延迟、复杂控制（分支预测、乱序执行）。
- **GPU**：大量弱核心（数千），擅长并行、高吞吐（矩阵运算）。AI 训练/推理本质是海量并行乘加。

```
CPU: ██ (大核，几个)
GPU: ░░░░░░░░░░ (小核，几千个，SM 内排布)
```

---

## 2. NVIDIA GPU 核心概念

| 概念 | 含义 | 运维关注 |
|---|---|---|
| **CUDA** | NVIDIA 并行计算平台/编程模型 | 驱动支持的最高 CUDA 版本向后兼容 |
| **SM**（Streaming Multiprocessor） | GPU 内的计算单元，含 CUDA Core + Tensor Core + 共享内存 | 算力基本单位 |
| **CUDA Core** | 通用浮点/整数核心 | FP32/INT 算力 |
| **Tensor Core** | 专做矩阵乘加（AI 核心） | 混合精度（TF32/FP16/INT8/FP8）加速 |
| **HBM**（高带宽内存） | 显卡上的显存，带宽远高于普通 DDR | **容量与带宽都是瓶颈** |
| **Compute Capability** | 架构代际（Ampere=8.x、Hopper=9.0、Blackwell=10.0） | 决定支持的特性（如 Hopper 的 FP8/Transformer Engine） |

> 常见架构：Volta(V100) → Ampere(A100) → Hopper(H100) → Blackwell(B200)。

---

## 3. 驱动 vs CUDA Toolkit 兼容性（高频坑）

- **宿主机驱动**决定能支持的最高 CUDA 版本（驱动内含 libcuda，向后兼容）。
- 容器内 CUDA Toolkit/runtime 版本 **≤** 驱动上限即可。
- 报错：`CUDA driver version is insufficient for CUDA runtime version` → 镜像 CUDA 版本高于宿主机驱动支持。
- 实践：用 `nvidia/cuda:<ver>-runtime` 基础镜像；升级驱动而非降级镜像。

---

## 4. GPU 切分 / 虚拟化

| 方式 | 隔离性 | 利用率 | 适用 |
|---|---|---|---|
| **整卡** | 强 | 低（小任务浪费） | 默认 |
| **MIG**（Multi-Instance GPU，A100/H100） | **硬件级强隔离**（独立显存/算力/带宽） | 高 | 多租户、小模型推理 |
| **MPS**（Multi-Process Service） | **无隔离**（共享上下文，一崩全崩） | 高 | 同信任域提效 |
| **time-slicing** | 无显存隔离（分时复用） | 中 | K8s 原生简单共享 |
| **vGPU** | 强（虚拟化） | 中 | 需 vSphere/license |

> 选型核心矛盾：**隔离性 vs 利用率**。MIG 要硬件支持；MPS 快但危险。

---

## 5. K8s 里用 GPU：Device Plugin 机制

```
节点：NVIDIA 驱动 → nvidia-container-toolkit → k8s-device-plugin(DaemonSet)
      上报 nvidia.com/gpu 资源给 kubelet
Pod：resources.limits["nvidia.com/gpu"]: 1
     运行时用 NVIDIA Container Runtime 把 GPU 设备挂进容器
```

- 申请整卡（`nvidia.com/gpu: 1`）；MIG 用对应 MIG 资源名。
- 多卡直接写 `2` 或切分 MIG。
- 排查：`nvidia-smi`、device-plugin 日志、kubelet 资源账目。

---

## 6. 训练通信：NVLink / IB / RDMA / NCCL

- **多卡/多机训练**靠集合通信（AllReduce/AllGather）同步梯度，传统 TCP/Ethernet 成瓶颈。
- **NVLink / NVSwitch**：GPU 间高速互联（带宽远高于 PCIe），HGX 整机全互联。
- **IB（InfiniBand）+ RDMA**：跨机低延迟高带宽，RDMA 绕过 CPU/内核零拷贝。
- **NCCL**（NVIDIA Collective Communications Library）：GPU 间集合通信库，自动选最优拓扑（NVLink→IB）。`NCCL_DEBUG=INFO` 排查。

```
单机多卡：NVLink (快)
多机：   IB/RDMA (快，需专用网络)
```

---

## 7. 推理引擎：vLLM / TGI

- 瓶颈：大模型推理受 **KV Cache（注意力缓存）** 显存限制，且传统实现显存碎片严重。
- **vLLM 的 PagedAttention**：像操作系统分页管理内存一样管理 KV Cache，消除碎片，大幅提升并发与 GPU 利用率。
- **continuous batching**：不同请求动态组批，吞吐更高。
- TGI：张量并行、量化、流式输出。
- 运维关注：实例数、显存、KV cache 上限、队列长度、P99、多模型路由。

---

## 8. 监控：DCGM Exporter

- `dcgm-exporter` 暴露 GPU 指标给 Prometheus：
  - 利用率 `DCGM_FI_DEV_GPU_UTIL`
  - 显存 `DCGM_FI_DEV_FB_USED`
  - 温度/功耗、`NVLink` 带宽
  - ECC 错误 `DCGM_FI_DEV_ECC_DBE`、XID 错误
- 配合 Node Exporter、容器指标做统一大盘与告警。

---

## 9. 常见误区

- ❌ 「显存大就够」 → 带宽（HBM）和容量同样关键，碎片也会 OOM。
- ❌ 「容器内 CUDA 版本随便选」 → 受宿主机驱动上限约束。
- ❌ 「MPS 和 MIG 一样」 → MPS 无隔离、危险；MIG 硬件强隔离。
- ❌ 「GPU 利用率低就是卡坏了」 → 多为数据加载/通信瓶颈（见 `modules/gpu-ai`）。

---

## 延伸

- 面试题：见 `modules/gpu-ai/gpu-ai-questions.md`
- 官方：NVIDIA docs（CUDA/DCGM/MIG/NCCL）；vLLM/TGI 文档
- 调度：Volcano / KubeFlow（训练任务 Gang 调度）
