# Linux 系统面试题（25 题）

> 模板见 [../../docs/STANDARD.md](../../docs/STANDARD.md)。基础概念详见 [../../basics/01-linux-basics.md](../../basics/01-linux-basics.md)。

---

### Q1. load average 很高但 CPU 使用率不高，可能是什么原因？
- **难度**：🟡 中级
- **关键词**：load average, D 状态, 上下文切换, IO wait
- **概念速记**：load = 可运行进程数 + 不可中断睡眠（D 状态）进程数；D 状态通常是 IO/磁盘卡死导致。
- **问题**：服务器 load 高但 CPU 不高，怎么排查？
- **参考答案**：
  - CPU 不高但 load 高常见于：① 大量 D 状态进程（磁盘/网络存储卡死）；② 大量进程等待（锁竞争、IO wait）；③ 上下文切换过高（sys 高）。
  - 排查：`top` 看 `wa%`/`cs`；`ps -eo pid,stat | grep D` 找 D 状态；`vmstat 1` 看 `r/b`；`iostat -x 1` 看 `%util`/`await`。
- **易错点**：把 load 高直接等同于 CPU 忙。
- **延伸**：[basics/01-linux-basics.md](../../basics/01-linux-basics.md)；Q2、Q13

### Q2. TCP TIME_WAIT 为什么需要 2MSL？过多怎么治理？
- **难度**：🟡 中级
- **关键词**：TIME_WAIT, 2MSL, tcp_tw_reuse
- **概念速记**：主动关闭方进入 TIME_WAIT，持续 2MSL 是为确保最后 ACK 到达 + 让旧报文消亡。
- **问题**：TIME_WAIT 过多怎么办？
- **参考答案**：
  - 治理：① `net.ipv4.tcp_tw_reuse=1`（客户端侧复用 outbound）；② 切勿用已废弃的 `tcp_tw_recycle`（NAT 下致问题）；③ 长连接/连接池；④ 调低 `tcp_fin_timeout`；⑤ `SO_REUSEADDR/SO_REUSEPORT`。
- **易错点**：在 NAT/负载均衡后开启 recycle 导致连接异常。
- **延伸**：[basics/02-network-osi.md](../../basics/02-network-osi.md)；network Q（拥塞控制）

### Q3. 进程被 OOM kill，怎么定位内存涨在哪？
- **难度**：🔴 高级
- **关键词**：OOM Killer, RSS, PSS, page cache
- **概念速记**：OOM Killer 按 oom_score 选进程杀，保系统不挂；RSS 是常驻内存，PSS 是按比例分摊的真实占用。
- **问题**：线上进程被 OOM 杀，如何定位？
- **参考答案**：
  - 看 `dmesg` OOM 日志（含占用最多进程）；`cat /proc/<pid>/status` 看 VmRSS/VmSwap；`smem` 看 PSS；Java 用 `jmap -histo`；`pmap -x` 看映射；持续监控上 atop/eBPF（`memleak`）。
  - 区分 RSS 涨（真泄漏）vs page cache 涨（可回收，非元凶）。
- **易错点**：把 page cache 占用当成内存泄漏。
- **延伸**：[basics/01-linux-basics.md](../../basics/01-linux-basics.md)；Q4

### Q4. 零拷贝（zero-copy）是什么？哪些场景用到？
- **难度**：🟡 中级
- **关键词**：zero-copy, sendfile, 上下文切换
- **概念速记**：零拷贝减少内核态/用户态数据拷贝与上下文切换，典型用 `sendfile()`。
- **问题**：零拷贝解决什么问题？
- **参考答案**：
  - 减少拷贝次数与上下文切换；场景：Nginx 静态资源、Kafka 落盘（`sendfile`）、`mmap`、`splice`、RDMA。
  - 价值：大文件/高并发转发显著降低 CPU 与延迟。
- **易错点**：零拷贝不是「一次拷贝都没有」，而是减少冗余拷贝。
- **延伸**：network Q（高性能网络）

### Q5. epoll 的 LT 与 ET 区别？ET 注意什么？
- **难度**：🔴 高级
- **关键词**：epoll, LT, ET, 非阻塞 IO
- **概念速记**：LT 水平触发（未处理完持续通知）；ET 边缘触发（仅状态变化时通知一次）。
- **问题**：ET 模式编程要注意什么？
- **参考答案**：
  - ET 必须用非阻塞 IO + 循环读写到 `EAGAIN`，否则丢事件；性能更高但苛刻。Nginx/Redis 用 ET。
- **易错点**：ET 下只读一次就返回，导致事件丢失、连接饿死。
- **延伸**：Q6

### Q6. CPU sys 占用异常高，如何定位到系统调用？
- **难度**：🔴 高级
- **关键词**：sys 高, perf, strace, bpftrace
- **概念速记**：sys 高多因上下文切换、系统调用频繁、缺页、锁竞争。
- **问题**：sys 飙高怎么逐步定位？
- **参考答案**：
  - `top`/`mpstat -P ALL` 确认；`perf top` 看热点；`perf record -g`+`perf report` 抓栈；`strace -p <pid> -c`（有开销）；eBPF `syscount`/`funclatency` 更轻量。结合 `vmstat`/`pidstat`。
- **易错点**：直接全量 `strace` 生产环境导致雪上加霜。
- **延伸**：[basics/01-linux-basics.md](../../basics/01-linux-basics.md)；Q125（CPU 100% 排障）

### Q7. cgroup v1 与 v2 核心区别？容器隔离靠什么？
- **难度**：🔴 高级
- **关键词**：cgroup v1/v2, namespace, 容器隔离
- **概念速记**：容器 = namespace（视图隔离）+ cgroup（资源限制）；v2 统一层级更细粒度。
- **问题**：容器隔离底层靠什么实现？
- **参考答案**：
  - namespace 隔离视图（pid/net/mnt…），cgroup 限制 cpu/mem/io/device。v1 子系统独立挂载；v2 unified hierarchy、支持 io 限速、cpu.weight。
  - 排查：`/sys/fs/cgroup`（v2）或各子系统目录（v1）。
- **易错点**：认为容器有独立内核（实际共享宿主内核）。
- **延伸**：[basics/04-kubernetes-concepts.md](../../basics/04-kubernetes-concepts.md)；kubernetes Q（QoS）

### Q8. swap 到底是什么？什么时候该关？
- **难度**：🟡 中级
- **关键词**：swap, vm.swappiness, 内存回收
- **概念速记**：swap 把不常用匿名页换到磁盘，防 OOM、平滑峰值，但换入换出拖慢。
- **问题**：数据库机器要不要关 swap？
- **参考答案**：
  - 优点：防 OOM、平滑峰值；缺点：抖动。低延迟/数据库常关（`swapoff -a` + `vm.swappiness=1`），一般服务保留少量做安全网。看 `si/so` 是否非零。
- **易错点**：认为关 swap 永远更好（通用服务保留少量更安全）。
- **延伸**：Q3

### Q9. 软中断与硬中断区别？网络收包瓶颈怎么排查？
- **难度**：🔴 高级
- **关键词**：softirq, irq, RSS/RPS, 网络瓶颈
- **概念速记**：硬中断由硬件触发上半部快速响应；软中断（NET_RX）在下半部批量处理。
- **问题**：单核 si% 打满怎么处理？
- **参考答案**：
  - 看 `/proc/softirqs`、`mpstat -I SUM`；优化：RSS/RPS/RFS、多队列、中断亲和性（`smp_affinity`）、busy polling。
- **易错点**：只加 CPU 不解决单队列网卡瓶颈。
- **延伸**：network Q（网络延迟）

### Q10. NUMA 是什么？对性能有什么影响？
- **难度**：🔴 高级
- **关键词**：NUMA, 内存亲和, 跨节点访问
- **概念速记**：NUMA = 非一致内存访问，CPU 访问本地内存快、跨节点慢。
- **问题**：大内存应用为什么要绑 NUMA？
- **参考答案**：
  - 跨 NUMA 访存拖慢；`numactl --hardware` 查看；MySQL/Redis 常绑 NUMA 节点；`numa_balancing` 内核特性。
- **易错点**：忽略 NUMA 导致跨节点访存延迟。
- **延伸**：Q7

### Q11. 大页（HugePages）是什么？什么场景用？
- **难度**：🔴 高级
- **关键词**：HugePages, THP, TLB
- **概念速记**：默认 4KB 页 TLB 命中率低；HugePages（2MB/1GB）减少 TLB miss。
- **问题**：数据库为什么要开大页？
- **参考答案**：
  - 减少 TLB miss、降低页表开销；Oracle/大内存 Java/DPDK 常用。THP 对部分数据库反而有害（碎片/抖动），常关。配置 `vm.nr_hugepages`。
- **易错点**：盲目开 THP 导致延迟尖刺。
- **延伸**：Q7

### Q12. 如何用 perf / bpftrace 做无侵入性能分析？
- **难度**：🔴 高级
- **关键词**：perf, bpftrace, 火焰图, eBPF
- **概念速记**：perf 基于采样；bpftrace 基于 eBPF，内核挂点零侵入。
- **问题**：不重启应用怎么抓热点？
- **参考答案**：
  - `perf top` 实时；`perf record -F 99 -a -g -- sleep 30` + `perf report` 火焰图；bpftrace `profile`/`biolatency`/`execsnoop` 查 IO/进程。
- **易错点**：perf 采样有开销，生产短时用。
- **延伸**：[basics/01-linux-basics.md](../../basics/01-linux-basics.md)；Q6

### Q13. 磁盘 IO 瓶颈怎么定位？iostat/iotop/blktrace 怎么读？
- **难度**：🟡 中级
- **关键词**：iostat, await, %util, 调度器
- **概念速记**：`%util`≈100% 表示设备饱和；`await` 高表示响应慢。
- **问题**：磁盘慢怎么分步定位？
- **参考答案**：
  - `iostat -x 1` 看 `%util`/`await`/`r/s w/s`；`iotop` 找重 IO 进程；`blktrace`+`blkparse` 看各层延迟。关注调度器（mq-deadline/bfq/none）、RAID、文件系统。
- **易错点**：`%util` 高就换盘，忽略是随机小 IO 还是顺序大 IO。
- **延伸**：[basics/01-linux-basics.md](../../basics/01-linux-basics.md)；Q1

### Q14. ext4 与 xfs 选型？inode 耗尽怎么处理？
- **难度**：🟡 中级
- **关键词**：ext4, xfs, inode, 小文件
- **概念速记**：inode 存文件元数据（不含名）；`df -i` 看 inode 使用。
- **问题**：磁盘有空间但写不进文件？
- **参考答案**：
  - 可能是 inode 耗尽（`df -i`）；小文件多导致。解决：删无用小文件、重建文件系统时调 `-i`、用 xfs。ext4 通用稳定；xfs 大文件/高并发更优。
- **易错点**：只看 `df -h` 不看 `df -i`。
- **延伸**：[basics/01-linux-basics.md](../../basics/01-linux-basics.md)；Q15

### Q15. inode、dentry、superblock 分别是什么？
- **难度**：🟡 中级
- **关键词**：inode, dentry, superblock
- **概念速记**：superblock 文件系统元数据；inode 文件元数据（不含名）；dentry 路径→inode 缓存。
- **问题**：为什么硬链接不能跨文件系统？
- **参考答案**：
  - inode 号只在同文件系统内有意义，跨文件系统 inode 含义不同，故硬链接受限；dentry 加速路径查找。
- **易错点**：混淆 inode（不含名）与文件名。
- **延伸**：Q14

### Q16. Shell 脚本里 $?、$$、$!、$@ 与 $* 区别？
- **难度**：🟢 初级
- **关键词**：shell 变量, 特殊变量, set -e
- **概念速记**：`$?` 上条退出码；`$@` 各参数独立（循环安全）。
- **问题**：`set -e` 有什么坑？
- **参考答案**：
  - `$?` 退出码、`$$` 当前 PID、`$!` 后台 PID、`$@` 独立参数 vs `$*` 整体。`set -e` 遇非 0 退出即终止，需显式处理部分命令失败；`set -u` 未定义变量报错；`set -o pipefail` 管道任一失败即失败。
- **易错点**：`for x in $*` 在含空格参数时断裂。
- **延伸**：Q17

### Q17. 如何用 awk/sed/grep 做日志统计（TOP IP、状态码）？
- **难度**：🟡 中级
- **关键词**：awk, sed, grep, 日志分析
- **概念速记**：awk 按列处理；`uniq -c` 计数；`LC_ALL=C` 提速。
- **问题**：怎么快速统计 access log 的 TOP IP？
- **参考答案**：
  - `awk '{print $1}' access.log | sort | uniq -c | sort -rn | head`；状态码 `awk '{print $9}' | sort | uniq -c`。TB 级上用 ripgrep/ELK。
- **易错点**：大文件用 `grep -c` 逐模式扫，慢；用 LC_ALL=C。
- **延伸**：observability Q（日志采集）

### Q18. 进程夯死（hang）但不退出，怎么定位卡在哪？
- **难度**：🔴 高级
- **关键词**：进程状态, /proc, gdb, py-spy
- **概念速记**：D 状态不可中断（IO 卡）；S 可中断睡眠；`/proc/<pid>/stack` 看内核栈。
- **问题**：进程卡住不动怎么查？
- **参考答案**：
  - `cat /proc/<pid>/status` 看 State；`/proc/<pid>/stack` 内核栈；`/proc/<pid>/syscall` 看卡在哪个调用；`gdb -p`/`py-spy` 抓用户态栈；strace 看阻塞点。
- **易错点**：只对 S 状态进程 strace，忽略 D 状态需查内核栈。
- **延伸**：Q3、Q6

### Q19. 系统时间不准会导致哪些问题？chrony 与 ntp 区别？
- **难度**：🟡 中级
- **关键词**：NTP, chrony, 时间漂移
- **概念速记**：chrony 比 ntpd 在长断网/虚拟机下更快收敛、更准。
- **问题**：时间漂移会引发什么故障？
- **参考答案**：
  - 影响：TLS 证书校验失败、日志错乱、DB 复制（GTID）、分布式锁租约、对账。`timedatectl` 管理；容器需挂载宿主时钟或 ptp/chrony 同步。
- **易错点**：容器独立改时间导致与宿主不一致。
- **延伸**：sre Q（分布式）

### Q20. SELinux / AppArmor 是什么？容器里怎么处理？
- **难度**：🔴 高级
- **关键词**：SELinux, AppArmor, MAC, 权限拒绝
- **概念速记**：强制访问控制（MAC）；SELinux 标签型、AppArmor 路径型。
- **问题**：`permission denied` 但权限看起来对，可能是什么？
- **参考答案**：
  - 可能是 SELinux/AppArmor 拦截；查 `/var/log/audit/audit.log`（`ausearch`/`sealert`）；容器可启 selinux 安全选项；临时 `setenforce 0` 验证。
- **易错点**：只改文件权限不查 MAC。
- **延伸**：cloud-security Q（安全基线）

### Q21. 如何用 systemd 做优雅启停与故障自愈？
- **难度**：🟡 中级
- **关键词**：systemd, Restart, 优雅停机, 看门狗
- **概念速记**：systemd 是 PID 1 初始化系统；`Restart=` 控制自愈。
- **问题**：服务崩了怎么自动拉起且优雅退出？
- **参考答案**：
  - `Restart=on-failure`、`RestartSec`、`StartLimitInterval`；`ExecStop` 优雅退出；`TimeoutStopSec` 防卡死；`KillMode`/`KillSignal`；`WatchdogSec` 看门狗；`journalctl -u <svc> -xe` 排查。
- **易错点**：`TimeoutStopSec` 过短导致数据未落盘被强杀。
- **延伸**：kubernetes Q（探针）

### Q22. 内核参数调优常调哪些？
- **难度**：🔴 高级
- **关键词**：sysctl, somaxconn, swappiness, 文件描述符
- **概念速记**：sysctl 改运行时内核参数，立即生效（`sysctl -p`）。
- **问题**：高并发服务器要调哪些内核参数？
- **参考答案**：
  - 网络：`net.core.somaxconn`、`tcp_max_syn_backlog`、`tcp_tw_reuse`、`ip_local_port_range`；内存：`vm.swappiness`、`vm.dirty_*`；文件：`fs.file-max`、`nofile` ulimit。`sysctl -p` 生效；逐项有依据，勿盲目照搬。
- **易错点**：抄模板不验证，导致连接问题。
- **延伸**：Q2、Q8

### Q23. core dump 怎么配置与分析？
- **难度**：🟡 中级
- **关键词**：core dump, ulimit, gdb
- **概念速记**：core dump 是进程崩溃时的内存镜像，用于事后调试。
- **问题**：程序段错误怎么拿到现场？
- **参考答案**：
  - `ulimit -c unlimited` + `kernel.core_pattern` 指定路径；`gdb <bin> <core>` → `bt` 看栈；`coredumpctl` 管理。容器需配落盘路径与大小。
- **易错点**：容器默认不落 core，排障无现场。
- **延伸**：Q18

### Q24. 如何用 strace/ltrace 追踪系统调用与库调用？
- **难度**：🟡 中级
- **关键词**：strace, ltrace, 系统调用
- **概念速记**：strace 追踪系统调用；ltrace 追踪库调用。
- **问题**：应用卡住但日志无输出怎么查？
- **参考答案**：
  - `strace -p <pid>` 实时；`strace -f -e trace=network` 只看网络；`-T` 看耗时；`-c` 统计。`perf trace` 更现代。`ltrace` 查 libc 调用。
- **易错点**：生产全量 strace 开销大，用 `-e` 过滤。
- **延伸**：Q6、Q12

### Q25. 新服务器上线，你的初始化/基线检查清单？
- **难度**：🟡 中级
- **关键词**：基线, 安全加固, CMDB, 监控接入
- **概念速记**：基线 = 统一的安全/配置/监控标准，避免「雪花服务器」。
- **问题**：一台新机器上线前要检查什么？
- **参考答案**：
  - 内核/补丁、NTP、时区 locale、ulimit/nofile、swap 策略、内核参数、防火墙、SSH 加固、监控 agent、日志采集、磁盘分区、主机名/CMDB 登记、安全基线（SELinux/fail2ban）、备份。
- **易错点**：漏接监控/审计，出问题无数据。
- **延伸**：cloud-security Q（基线扫描）
