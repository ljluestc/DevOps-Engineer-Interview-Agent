# 04 · Kubernetes 核心概念深度篇

> 关键词：**CRI / CNI / CSI**、OCI、对象模型、调度、控制器

这是面试「讲不透」的重灾区。先把三个 **I** 讲清楚，再讲对象模型。

---

## 1. 三个 I：CRI / CNI / CSI（必考）

三者都是 K8s 的**插件接口（Interface）**，目的是**解耦 K8s 与各厂商实现**——K8s 只定义接口，具体谁来实现由插件决定。

| 接口 | 全称 | 管什么 | 典型实现 |
|---|---|---|---|
| **CRI** | Container Runtime Interface | 容器运行时（创建/启停容器、拉镜像） | containerd、CRI-O（runc 是真正干活的 OCI 运行时） |
| **CNI** | Container Network Interface | 容器网络（分配 IP、建网桥/路由、网络策略） | Calico、Flannel、Cilium、Weave |
| **CSI** | Container Storage Interface | 容器存储（挂盘、快照、动态供给） | Ceph CSI、AWS EBS CSI、NFS CSI |

记忆：**R=Runtime（跑起来）、N=Network（连起来）、S=Storage（存下来）**。

### 1.1 CRI（容器运行时接口）

- kubelet 通过 CRI 的 **RuntimeService**（Pod/容器生命周期）和 **ImageService**（镜像）两个 gRPC 接口调用运行时。
- 底层真正创建容器的是 **OCI runtime**（如 runc / crun），按 OCI runtime-spec 执行。
- **历史坑**：早期 K8s 内置 `dockershim` 桥接 Docker；1.20 弃用、1.24 移除。现在生产推荐 **containerd**（通用）或 **CRI-O**（安全向）。
- 排查命令：`crictl`（CRI 层）、`ctr`/`nerdctl`（containerd 层），而非 `docker`。

```
kubelet ──CRI(gRPC)──> containerd ──> runc(OCI) ──> 容器进程
```

### 1.2 CNI（容器网络接口）

- 规范：容器创建时调用 CNI 插件「加网」，删除时「撤网」。插件接收一个 JSON 网络配置 + 环境变量（容器 netns 路径等），返回分配的 IP。
- 插件分类：
  - **main**：创建网络设备（bridge、ipvlan、macvlan、host-interface）。
  - **ipam**：IP 地址管理（host-local、dhcp）。
  - **meta**：链式调用（portmap、bandwidth、firewall）。
- Pod 网络流程：kubelet 调 CRI 建 pause 容器（拿 netns）→ 调 CNI 把 veth 一端进 Pod、一端进主机 bridge → 配 IP/路由。
- 主流选型：Flannel（vxlan，简单）、Calico（BGP/IPIP，网络策略强）、Cilium（eBPF，性能+可观测+替代 kube-proxy）。

### 1.3 CSI（容器存储接口）

- 把存储供给从 K8s 内部解耦，云厂商/存储商实现 CSI 驱动即可被 K8s 用。
- 组件：External Provisioner（动态建卷）、External Attacher（挂接）、External Snapshotter（快照）、Node Plugin（节点侧挂载）。
- 流程：PVC 引用 StorageClass → Provisioner 调驱动建 PV → Attach 到节点 → Node 插件 mount 进 Pod。
- 运维关注：`reclaimPolicy`（Delete/Retain）、扩容、快照、跨区限制。

---

## 2. K8s 对象模型（基础）

| 对象 | 作用 | 关键字段 |
|---|---|---|
| Pod | 最小调度单位（一个或多个容器共享 net/ipc） | containers、resources、probe |
| Deployment | 管理无状态副本、滚动更新 | replicas、strategy、selector |
| StatefulSet | 有状态、稳定标识/卷、有序启停 | serviceName、volumeClaimTemplates |
| DaemonSet | 每节点一个（agent/日志） | — |
| Service | 稳定访问入口（VIP） | ClusterIP/NodePort/LoadBalancer、selector |
| Ingress | 七层 HTTP 路由 | rules（host/path → service） |
| ConfigMap / Secret | 配置 / 密钥 | data、immutable |
| PV / PVC | 存储资源 / 申请 | storageClassName、accessModes |
| Namespace | 逻辑隔离 | — |
| ResourceQuota / LimitRange | 资源配额 / 默认限制 | — |
| RBAC | 权限（Role/Binding） | — |

**声明式 vs 命令式**：K8s 核心是「期望状态」，控制器持续 Reconcile 让实际趋近期望（这是 Operator 的基础）。

---

## 3. 调度（Scheduler）

- 两阶段：**过滤（Filtering）**（资源够不够、污点匹配、亲和性）→ **打分（Scoring）**（均衡、镜像 locality）。
- 亲和性：`nodeAffinity`（选节点）、`podAntiAffinity`（打散）。
- 污点/容忍：`Taint`（节点排斥）+ `Toleration`（Pod 接受），用于专用节点（GPU/机房）。
- 局限：原生不支持 Gang 调度（训练任务需要，见 `modules/gpu-ai` 的 Volcano）。

---

## 4. 常见误区

- ❌ 混淆 **CRI（接口）/ OCI（规范）/ 运行时（containerd/runc）**。
- ❌ 以为 K8s「自带网络」→ 实际靠 CNI 插件，K8s 只定规则。
- ❌ 以为 Pod IP 稳定 → Pod 重建 IP 变，靠 Service/Headless 解耦。
- ❌ 容器 OOM 就是宿主机 OOM → 多为 cgroup 限制触发（exit 137）。

---

## 延伸

- 面试题：见 `modules/kubernetes/kubernetes-questions.md`
- 官方：kubernetes.io/docs/concepts/extend-kubernetes/
- 深入：《Kubernetes 权威指南》；CNCF 文档
