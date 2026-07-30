# 01 · Linux 基础概念深度篇

> 关键词：进程/线程、虚拟内存、Swap、OOM、Page Cache、inode、cgroup、namespace、systemd、perf/bpftrace

---

## 1. 进程与线程

- **进程（Process）**：资源分配的基本单位，拥有独立的虚拟地址空间、文件描述符表、信号处理。
- **线程（Thread）**：CPU 调度的基本单位，同一进程内的线程共享地址空间，切换成本低于进程。
- **轻量级进程（LWP）**：Linux 用 `clone()` 实现线程，内核视角下线程≈共享部分资源的进程。
- **上下文切换（Context Switch）**：保存/恢复寄存器与状态。sys 高、`cs`（切换次数）暴涨常意味着锁竞争或过多进程。

```
进程 A ─┬─ 线程 A1 (共享地址空间)
        └─ 线程 A2
进程 B ─┬─ 线程 B1
```

查看：`top -H`（线程）、`cat /proc/<pid>/status`、`pidstat -w`（切换）。

---

## 2. 虚拟内存与 Swap

- **虚拟内存**：每个进程拥有独立的连续虚拟地址空间，由 MMU 映射到物理页。好处：隔离、超卖、共享库。
- **页（Page）**：通常 4KB；大页（HugePages，2MB/1GB）减少 TLB miss。
- **Page Cache**：文件读写缓存，占满空闲内存以加速 IO。**它不是泄漏**——可用内存 = free + cache，cache 可被回收。
- **Swap**：把不常用的匿名页换到磁盘。优点：防 OOM、平滑峰值；缺点：换入换出拖慢。数据库/低延迟服务常关或设 `vm.swappiness=1`。

```
物理内存
┌─────────────┬──────────────┬───────────────┐
│ 用户进程匿名页 │ Page Cache   │ 内核 / 其他    │
└─────────────┴──────────────┴───────────────┘
   ↑ swap out / in ↑
```

---

## 3. OOM 与 OOM Killer

- 当内存（含 swap）不足，内核 OOM Killer 按 `oom_score`（默认与内存占用正相关，可调 `oom_score_adj`）选进程杀掉，保系统不挂。
- 日志在 `dmesg`：`Out of memory: Killed process <pid> (xxx)`。
- **cgroup OOM**：容器超限时被 cgroup 杀（exit 137），与宿主机 OOM 表现不同。

排查：RSS 涨（真泄漏，用 `smem`/`jmap`/`pmap`）vs page cache 涨（正常）。

---

## 4. 文件系统：inode / dentry / superblock

- **superblock**：文件系统整体元数据（大小、块数、状态）。
- **inode**：文件元数据（权限、大小、数据块指针、时间戳），**不含文件名**。
- **dentry**：目录项缓存（路径 → inode 映射），加速查找。
- `df -i` 看 inode 使用；大量小文件会耗尽 inode（而非空间）。

```
路径 /a/b.txt ──dentry──> inode(123) ──> 数据块
```

ext4 vs xfs：ext4 通用稳定；xfs 大文件/高并发/大容量更优（元数据扩展性、延迟分配）。

---

## 5. cgroup 与 namespace（容器底层）

- **namespace**：视图隔离。共 8 类：mnt、pid、net、uts、ipc、user、cgroup、time。容器用前 7 类把「世界」隔成自己的。
- **cgroup（v1/v2）**：资源限制与统计（cpu、memory、io、pids、devices）。
  - v1：各子系统独立层级，接口分散。
  - v2：统一层级（unified），更细粒度（io 限速、cpu.weight），默认开启。

```
容器 = namespace(隔离视图) + cgroup(限制资源) + 受限进程
```

---

## 6. systemd

- 现代 Linux 初始化系统（PID 1），替代 SysV init。
- 单元（unit）：`.service`、`.socket`、`.target`、`.timer` 等。
- 常用：`systemctl status/start/enable`、`journalctl -u <svc> -xe`、`systemd-analyze`。
- 关键配置：`Restart=`、`ExecStart=`、`WantedBy=multi-user.target`、`TimeoutStartSec`。

---

## 7. 性能分析工具链

| 层级 | 工具 | 用途 |
|---|---|---|
| 全局 | `top`/`htop`/`vmstat`/`mpstat` | CPU/内存/IO 概览 |
| CPU | `perf`（`perf top`/`record -g`） | 热点函数、调用栈 |
| 内核/无侵入 | `bpftrace`（`biolatency`/`execsnoop`/`syscount`） | eBPF 追踪，零侵入 |
| 磁盘 | `iostat -x`/`iotop`/`blktrace` | IO 利用率、延迟 |
| 网络 | `ss`/`ip`/`tcpdump`/`ethtool` | 连接、抓包、网卡 |
| 进程 | `strace`/`lsof`/`/proc/<pid>/*` | 系统调用、打开文件 |

**方法论**：先用 `vmstat`/`mpstat` 定位是 CPU/sysc/IO 哪类瓶颈，再下钻具体工具，避免一上来 `strace` 全量（开销大）。

---

## 8. 常见误区

- ❌ 「free 很小 = 内存不够」 → 忽略 page cache 可回收。
- ❌ 「load 高 = CPU 忙」 → D 状态进程（IO 卡）也会推高 load。
- ❌ 「容器是轻量虚拟机」 → 容器只是受限进程，无独立内核。
- ❌ 「关闭 swap 一定更好」 → 低延迟服务合适，通用服务保留少量更安全。

---

## 延伸

- 面试题：见 `modules/linux/linux-questions.md`
- 内核文档：`Documentation/admin-guide/sysctl/`
- 经典：`brendangregg.com` 的 Linux 性能图谱
