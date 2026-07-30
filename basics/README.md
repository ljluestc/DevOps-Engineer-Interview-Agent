# 基础概念深度篇（basics）

> 面试的地基。这里把常被「一笔带过」的关键词系统讲透：**定义 → 原理图 → 对比 → 常见误区**。
> 每篇对应 `modules/` 中一类题目的「概念速记」溯源。建议先读完本目录，再刷题。

## 为什么要单独写「基础」

很多面试题只问「K8s 网络怎么实现」，却默认你已经懂 CNI、netns、veth、overlay。一旦追问「CRI 和 OCI 什么关系」「OSI 每层干什么」，就容易露怯。

本项目的原则：**概念不清楚，题目答不透**。所以把地基单独成篇。

## 索引

| 文件 | 覆盖关键词 | 关联模块 |
|---|---|---|
| [01-linux-basics.md](01-linux-basics.md) | 进程/线程、虚拟内存、swap、OOM、inode、cgroup、systemd、性能工具 | `modules/linux` |
| [02-network-osi.md](02-network-osi.md) | OSI 七层、TCP/IP、封装、DNS、HTTP、负载均衡 | `modules/network` |
| [03-docker-basics.md](03-docker-basics.md) | 镜像分层、Dockerfile、存储驱动、容器 vs 虚拟机 | `modules/kubernetes` `modules/cicd-iac` |
| [04-kubernetes-concepts.md](04-kubernetes-concepts.md) | **CRI / CNI / CSI**、对象模型、调度 | `modules/kubernetes` |
| [05-ansible-basics.md](05-ansible-basics.md) | 幂等、Playbook、Inventory、变量优先级、Vault | `modules/cicd-iac` |
| [06-ai-gpu-basics.md](06-ai-gpu-basics.md) | CUDA、显存、SM、MIG、Device Plugin、NCCL、vLLM | `modules/gpu-ai` |

## 使用建议

1. 通读一遍，把每个「对比表」记熟。
2. 刷题时遇到不熟悉的关键词，回本目录查「概念速记」的溯源。
3. 自己尝试用一句话复述每个加粗关键词——能复述，才算过关。
