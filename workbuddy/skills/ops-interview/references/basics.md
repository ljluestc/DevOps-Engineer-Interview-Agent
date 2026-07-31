# 运维基础概念深度篇（Basics Deep-Dive）

> 本文件是「运维面试教练」概念讲解的权威口径。每条概念按「一句话速记 → 原理 → 对比表 → 常见误区」组织，避免只抛名词、不讲原理。
> 完整 200 题开源题库见项目仓库 `ops-interview`（GitHub）。本篇是高频基础词的浓缩版。

---

## 1. Linux 基础速记

### 1.1 平均负载（Load Average）
- **速记**：单位时间内「可运行 + 不可中断睡眠」的进程平均数，≠ CPU 使用率。
- **原理**：`load1/5/15` 分别对应 1/5/15 分钟滑动均值。可运行状态 = R 状态（正在跑或在就绪队列）；不可中断 = D 状态（通常等磁盘 IO）。所以 load 高可能是 CPU 忙，也可能是 IO 忙或锁。
- **误区**：「load 高 = CPU 不够」是错的。要看 `vmstat` 的 `r`（运行队列）、`b`（阻塞）、`wa`（IO 等待）。经验值：load 长期 > 核心数即需关注。

### 1.2 OOM 与 cgroup
- **速记**：OOM 有两种——进程级 `OOM Killer`（内核挑得分最高的进程杀掉）和 cgroup 级（`memory.limit` 触发，杀组内进程）。
- **原理**：`/proc/sys/vm/panic_on_oom`、各 cgroup 的 `memory.oom_control`。cgroup v1 在 `memory` 子系统，v2 在 `memory.max`。
- **误区**：容器 OOM 是被 cgroup 杀，不一定是宿主机内存真的耗尽；`dmesg` 看 `Out of memory: Kill process`。

### 1.3 零拷贝（Zero-Copy）
- **速记**：减少内核态⇄用户态的数据拷贝次数与上下文切换。典型：`sendfile`、`splice`、`mmap+write`。
- **对比**：传统 `read+write` 4 次拷贝（磁盘→内核页缓存→用户缓冲→socket 缓冲→网卡）；`sendfile` 2 次（DMA 拷贝 + 一次 CPU 拷贝到 socket 缓冲），配合 `DMA gather` 可降到 1 次。

### 1.4 epoll vs select/poll
| 维度 | select/poll | epoll |
|------|-------------|-------|
| 实现 | 轮询 fd 集合 | 内核回调就绪链表 |
| 复杂度 | O(n) 每次扫描 | O(1) 仅返回就绪 |
| fd 上限 | 1024（select） | 系统限制，十万级 |
| 触发 | 水平触发（LT）默认 | 支持 LT + 边缘触发（ET） |

- **误区**：epoll ET 必须循环 `read` 到 `EAGAIN`，否则会丢事件。

### 1.5 cgroup v1 vs v2
| 维度 | v1 | v2 |
|------|----|----|
| 设计 | 每子系统独立层级 | 单一统一层级 |
| 资源 | cpu/memory/... 各自树 | 合并树 |
| 新特性 | — | 压力 stall 信息 PSI、更干净接口 |
| 现状 | 旧发行版默认 | 新内核（≥4.5，RHEL8+）默认 |

---

## 2. 网络与 OSI 七层

### 2.1 OSI 七层（从上到下）
| 层 | 名称 | 单位 | 代表协议/设备 | 运维排障关注点 |
|----|------|------|--------------|----------------|
| 7 | 应用层 | 报文 | HTTP/DNS/SSH | 应用日志、TLS、重试 |
| 6 | 表示层 | — | TLS/编码 | 加密、序列化 |
| 5 | 会话层 | — | 连接管理 | 长连接、会话保持 |
| 4 | 传输层 | 段 | TCP/UDP | 端口、重传、拥塞、连接数 |
| 3 | 网络层 | 包 | IP/ICMP/BGP | 路由、MTU、丢包、延迟 |
| 2 | 数据链路层 | 帧 | 以太网/VLAN/MAC | 双工、ARP、交换机、MAC 冲突 |
| 1 | 物理层 | 比特 | 网线/光模块 | 线缆、速率、错包（`ifconfig eth0` 的 errors） |

- **速记**：「应表会传网数物」= 应用/表示/会话/传输/网络/数据链路/物理。
- **与 TCP/IP 四层对应**：应用层≈7+6+5；传输层=4；网际层=3；网络接口层=2+1。

### 2.2 TCP 三次握手 / 四次挥手
- **握手**：SYN → SYN+ACK → ACK。建立双向通道，防止历史脏连接。
- **挥手**：FIN → ACK → FIN → ACK。因为 TCP 全双工，关闭需双向各关一次。
- **TIME_WAIT**：主动关闭方最后停留 2*MSL，确保最后 ACK 可达、旧报文消亡。大量 TIME_WAIT 常见于短连接服务，可调 `net.ipv4.tcp_tw_reuse`（客户端安全）或连接复用。

### 2.3 关键排障命令口径
- `tcpdump -i any -nn port 443` 抓包；`ss -lntp` 看监听；`ip route get <ip>` 看路由；`conntrack -L` 看 NAT 表；`iperf3` 测吞吐；`mtr` 看逐跳丢包。

### 2.4 常见误区
- 「ping 通 = 网络正常」错：ICMP 通只说明三层可达，不代表 TCP 端口/应用正常。
- 「MTU 越大越好」错：超过路径 MTU 会分片或丢包（DF 位时），VPN/隧道场景尤甚。

---

## 3. Docker 与 Dockerfile

### 3.1 镜像分层与写时复制
- **速记**：镜像 = 只读层栈；容器 = 镜像层 + 可写层（Copy-On-Write）。同名层可跨镜像共享缓存。
- **原理**：每个 `RUN`/`COPY`/`ADD` 产生新层；容器修改文件时，从底层复制（COW）到可写层，原层不变。

### 3.2 Dockerfile 核心指令（必考）
| 指令 | 作用 | 注意点 |
|------|------|--------|
| `FROM` | 基础镜像 | 生产用 `distroless`/`slim`，固定 tag/摘要 |
| `RUN` | 执行命令建层 | 合并命令、清理缓存（`apt-get clean`） |
| `COPY`/`ADD` | 拷文件 | `COPY` 不自动解压；`ADD` 支持 URL/解压（慎用） |
| `ENV` | 环境变量 | 会固化进镜像，敏感信息用 `--env` 或 secret |
| `ARG` | 构建期变量 | 不进最终镜像，可用于基础镜像版本 |
| `EXPOSE` | 声明端口 | 仅文档作用，不等于 `-p` 映射 |
| `CMD` | 容器默认命令 | 可被 `docker run` 覆盖；仅一个生效 |
| `ENTRYPOINT` | 入口 | 与 `CMD` 配合：`ENTRYPOINT` 固定程序，`CMD` 默认参数 |
| `WORKDIR` | 工作目录 | 避免 `cd`，用绝对路径 |
| `USER` | 运行用户 | 生产不用 root |
| `HEALTHCHECK` | 健康检查 | 自定义探测命令 |
| `VOLUME` | 挂载点 | 持久化数据，不写进镜像层 |

### 3.3 多阶段构建（Multi-stage）
- **速记**：用一个阶段编译，另一个阶段只拷产物，最终镜像不含构建工具链。
- 例：Go 用 `golang:1.22` 编译，再 `COPY --from=builder /app/bin /app/bin` 到 `scratch`/`alpine`，镜像从 ~1GB 降到 ~10MB。

### 3.4 常见误区
- 「`CMD` 和 `ENTRYPOINT` 一样」错：前者易覆盖，后者更像固定入口；常组合 `ENTRYPOINT ["exec"]` + `CMD ["--default"]`。
- 「层越多越好」错：层多膨胀且构建慢，应合并 `RUN`、用 `.dockerignore`。
- 忘记 `.dockerignore` 把 `.git`/`node_modules` 塞进上下文，拖慢构建并泄露。

---

## 4. Kubernetes 接口：CRI / CNI / CSI

> 这是高频混淆点，必须讲清「谁对接谁」。K8s 通过三个标准接口解耦底层实现，让运行时/网络/存储可插拔。

### 4.1 三者总览
| 接口 | 全称 | 对接对象 | 解决的问题 | 典型实现 |
|------|------|----------|------------|----------|
| **CRI** | Container Runtime Interface | kubelet ↔ 容器运行时 | 解耦 kubelet 与 Docker/containerd | containerd、CRI-O、Docker（经 dockershim，已废弃）|
| **CNI** | Container Network Interface | kubelet ↔ 网络插件 | 给 Pod 分配 IP、配置路由/网络策略 | Calico、Flannel、Cilium、Weave |
| **CSI** | Container Storage Interface | kubelet ↔ 存储插件 | 对接外部存储卷（PV）| Ceph CSI、AWS EBS CSI、NFS CSI |

### 4.2 CRI（容器运行时接口）
- **速记**：kubelet 不直接管容器，通过 CRI 调运行时（containerd/CRI-O）来「创建/启动/停止/删除」沙箱与容器。
- **演进**：早期 kubelet 内置 dockershim 调 Docker；K8s 1.24 起移除 dockershim，Docker 需经 `cri-dockerd` 才能用，推荐直接用 containerd/CRI-O。
- **误区**：「K8s 不支持 Docker 了」不准确——是不再内置 dockershim，Docker 镜像（OCI 格式）仍通用。

### 4.3 CNI（容器网络接口）
- **速记**：Pod 创建时 kubelet 调 CNI 插件给网络命名空间配 IP、路由、桥接；插件按 `CNI_CONFIG` 执行 `ADD`/`DEL`。
- **模式**：Overlay（VXLAN，跨节点隧道，如 Flannel）vs Underlay（直接二层，如 Calico BGP）；eBPF 数据面（Cilium）绕过 kube-proxy。
- **排查**：Pod 拿不到 IP 常因 CNI 配置缺失、`/opt/cni/bin` 无二进制、或节点路由冲突。

### 4.4 CSI（容器存储接口）
- **速记**：让存储厂商实现一套驱动，K8s 通过 `external-provisioner`/`external-attacher` 等 sidecar 调它完成卷的 provision/attach/mount。
- **对象**：`StorageClass` → 动态供给 `PersistentVolume`（PV）→ 绑定 `PersistentVolumeClaim`（PVC）→ 挂载进 Pod。
- **误区**：PVC 是「申请」，PV 是「实际卷」；`Delete` 回收策略会删底层数据，`Retain` 保数据。

### 4.5 速记口诀
「**C**RI 管**跑**（运行时）、**C**NI 管**连**（网络）、**C**SI 管**存**（存储）」——三个 C 都是 K8s 解耦底层的插件接口。

---

## 5. Ansible 基础

### 5.1 核心概念
- **速记**：无 Agent（走 SSH）、声明式 Playbook、幂等（重复执行结果一致）、基于 YAML。
- **组成**：`Inventory`（主机清单）→ `Playbook`（剧本）→ `Task`（任务）→ `Module`（模块）→ `Role`（角色复用）。

### 5.2 幂等性（必考）
- **原理**：模块自身保证状态收敛，如 `apt` 装过就不再装、`template` 内容不变就不重写。这正是 Ansible 敢重复跑的原因。
- **反例**：用 `shell/command` 直接执行非幂等命令（如 `echo >> file`）会每次追加——需用 `lineinfile` 或 `changed_when: false`。

### 5.3 变量优先级（从高到低，易错）
1. 命令行 `--extra-vars`
2. 任务内 `vars`
3. block / play 的 `vars`
4. inventory 的 host/group vars
5. `group_vars/` / `host_vars/`
6. role 的 `defaults`（最低）
- **误区**：以为 `defaults` 优先级高——其实它最低，最易被覆盖。

### 5.4 常用模块
`apt/yum`（包）、`copy/template`（文件）、`service`（服务）、`lineinfile/blockinfile`（行）、`user`（用户）、`debug`、`register`（存结果）、`when`（条件）、`handlers`（变更后触发，如重启服务）。

### 5.5 与 Terraform 区别
| 维度 | Ansible | Terraform |
|------|---------|-----------|
| 定位 | 配置管理 / 应用部署 | 基础设施编排（IaC）|
| 状态 | 无状态（或事实缓存）| 有 state 文件 |
| 连接 | SSH | 云 API |
| 幂等 | 模块内置 | 声明式 plan/apply |

---

## 6. AI / GPU 运维基础

### 6.1 CUDA / 显存 / SM（必考）
- **CUDA**：NVIDIA 的并行计算平台与编程模型；应用通过 CUDA API 调用 GPU。
- **SM（Streaming Multiprocessor）**：GPU 基本计算单元，含多个 CUDA Core / Tensor Core；一卡有多组 SM。
- **显存（HBM）**：GPU 自有高带宽内存（如 A100 80GB），训练/推理的模型权重与激活都在这里；与主机内存通过 PCIe/NVLink 搬运。

### 6.2 驱动 / CUDA Toolkit / CUDA 算子的兼容
- **速记**：驱动决定「最高支持的 CUDA 版本」；容器里的 CUDA Toolkit 版本 ≤ 驱动支持版本。常见坑：宿主驱动太旧，新镜像跑不了（`CUDA driver version is insufficient`）。
- **三者**：Driver（内核模块 `nvidia.ko`）↔ CUDA Runtime ↔ 应用框架（PyTorch/TensorRT）。

### 6.3 MIG / MPS / Time-Slicing（多租户切分）
| 方案 | 粒度 | 隔离性 | 适用 |
|------|------|--------|------|
| MIG | 物理切分（A100/H100）| 强，硬件级 | 多小模型独享 |
| MPS | 共享上下文多进程 | 中，共享显存 | 多进程提利用率 |
| Time-Slicing | 时间片复用整卡 | 弱 | 轻度超卖 |

### 6.4 Device Plugin（K8s 调度 GPU）
- **速记**：`nvidia-device-plugin` 向 kubelet 暴露 `nvidia.com/gpu` 资源，Pod 声明 `resources.limits["nvidia.com/gpu"]: 1` 即可被调度到带 GPU 的节点。
- **误区**：不配置 device plugin 时，Pod 无法申请 GPU 资源；多卡需 `NVIDIA_VISIBLE_DEVICES` 或 `CUDA_VISIBLE_DEVICES` 控制可见性。

### 6.5 利用率低 / 显存 OOM 排查口径
- **利用率低**：看 `nvidia-smi` 的 `GPU-Util` 与 `nvidia-smi dmon`；常见原因：数据 pipeline 瓶颈（CPU 喂不动）、batch 太小、通信等待（NCCL）。
- **显存 OOM**：`torch.cuda.OutOfMemoryError`；手段：减小 batch、开 `gradient_checkpointing`、用 `mixed precision`(fp16/bf16)、`torch.compile`、清理缓存 `empty_cache`、或换更大卡 / 张量并行。

### 6.6 监控：DCGM + Prometheus
- **速记**：`DCGM-exporter` 暴露 GPU 指标（温度、显存、利用率、功耗、ECC、XID 错误）给 Prometheus，配合 Grafana 看板；XID 错误码是 GPU 硬件故障信号。

### 6.7 推理服务：vLLM / TGI
- **速记**：vLLM 用 PagedAttention 做 KV Cache 分页，大幅提升吞吐、降低显存碎片；TGI 类似。运维关注：并发、TTFT（首 token 延迟）、TPS、显存占用、连续批处理（continuous batching）。

---

## 附：概念讲解话术模板（agent 使用）
1. **一句话速记**（先给结论，防止堆名词）
2. **原理 / 它解决什么问题**（必要时画 ASCII 图或对比表）
3. **与其他概念的边界 / 对比**
4. **常见误区 / 面试易错点**
5. **实战排查口径或延伸题**
