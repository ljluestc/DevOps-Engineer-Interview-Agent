# 03 · Docker 与 Dockerfile 深度篇

> 关键词：镜像分层、UnionFS/overlay2、Dockerfile 指令、多阶段构建、存储驱动、容器 vs 虚拟机

---

## 1. Docker 架构

```
Docker Client ──> Docker Daemon (dockerd)
                       ├── containerd (高级运行时，管理生命周期)
                       │     └── runc (OCI 运行时，真正建容器)
                       └── docker-init / docker-proxy
```

- **dockerd**：守护进程，接收 CLI/API 请求。
- **containerd**：高管容器生命周期（镜像、容器、网络），符合 CRI 标准（K8s 也直接用）。
- **runc**：OCI runtime 实现，按 OCI spec 创建容器（clone namespace、cgroup）。

> 和 K8s 的关系见 [04-kubernetes-concepts.md](04-kubernetes-concepts.md)：K8s 通过 CRI 调 containerd，不再经过 dockerd（dockershim 已废弃）。

---

## 2. 镜像分层（Image Layers）

- 镜像由多个**只读层（ro layer）**组成，构建时每条指令生成一个层。
- 容器运行时在最上层加一个**可写层（writable layer / container layer）**，用 **Copy-on-Write（CoW）**：修改文件时先把底层文件复制到可写层再改，原层不变。
- **共享**：相同基础层在主机上只存一份，节省空间。

```
镜像层（只读，联合挂载）
├── layer N: CMD
├── layer 3: RUN apt install
├── layer 2: COPY app
└── layer 1: FROM ubuntu   ← base，多镜像共享
容器层（可读写，CoW）
```

存储驱动：
- **overlay2**（主流默认）：lowerdir（镜像层）+ upperdir（容器层）+ merged（视图）+ work。性能最好。
- 过时：devicemapper、aufs。
- 运维：`docker system df` 看空间；悬空镜像 `docker image prune`。

---

## 3. Dockerfile 核心指令（必会）

| 指令 | 作用 | 注意 |
|---|---|---|
| `FROM` | 基础镜像（必须第一条） | 优先精简基础（alpine/distroless） |
| `RUN` | 执行命令，**每条约一层** | 合并命令、`&&` 清理缓存，减小层数 |
| `COPY` | 复制本地文件到镜像 | 比 ADD 更可控、可缓存 |
| `ADD` | 复制 + 自动解压 tar + 远程 URL | 慎用，行为隐蔽 |
| `ENV` | 环境变量（持久化进镜像） | 影响缓存 |
| `ARG` | 构建期变量（不进运行时） | 用于版本参数 |
| `CMD` | 容器默认启动命令（可被覆盖） | 容器主进程（PID 1） |
| `ENTRYPOINT` | 入口（不易被覆盖，常配 CMD 传参） | 固定可执行 + CMD 作参数 |
| `WORKDIR` | 工作目录 | 避免 `cd` 链 |
| `EXPOSE` | 声明端口（文档性，不自动映射） | 仍需 `-p` 映射 |
| `VOLUME` | 声明挂载点 | 数据持久化 |
| `USER` | 运行用户 | 安全：避免 root |
| `HEALTHCHECK` | 健康检查 | 配合编排探针 |
| `LABEL` | 元数据 | 版本/维护者 |

**CMD vs ENTRYPOINT**：
- 只有 CMD：命令可被 `docker run image cmd` 完全覆盖。
- ENTRYPOINT + CMD：`ENTRYPOINT` 固定可执行，`CMD` 作为默认参数，运行时参数追加。

```dockerfile
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
# docker run img --help → nginx --help
```

---

## 4. 构建最佳实践

1. **多阶段构建（multi-stage）**：编译阶段用大镜像，运行阶段只 COPY 产物，镜像体积骤减。
   ```dockerfile
   FROM golang:1.22 AS build
   RUN go build -o app .
   FROM gcr.io/distroless/base
   COPY --from=build /app /app
   ENTRYPOINT ["/app"]
   ```
2. **利用层缓存**：不变的内容（依赖安装）放前面，易变的代码放后面。
3. **.dockerignore**：排除 .git、node_modules，避免上下文过大、缓存失效。
4. **精简基础**：alpine / distroless / scratch。
5. **固定版本**：`FROM python:3.12-slim` 而非 `latest`（可重现、防意外）。
6. **安全**：非 root 运行、扫描漏洞（Trivy）、最小权限。

---

## 5. 容器 vs 虚拟机 vs 镜像

| 维度 | 虚拟机 | 容器 | 镜像 |
|---|---|---|---|
| 隔离 | 硬件级（Hypervisor） | 进程级（namespace/cgroup） | 静态模板 |
| 内核 | 各自独立内核 | 共享宿主机内核 | 不含内核 |
| 启动 | 秒~分钟 | 毫秒~秒 | — |
| 体积 | GB | MB | MB~GB |
| 密度 | 低 | 高 | — |

**误区**：「容器里有完整 OS」→ 只有用户态rootfs，内核还是宿主的。

---

## 6. 常见误区

- ❌ 把数据写进容器层不挂卷 → 容器删了数据丢。
- ❌ `latest` 标签生产使用 → 不可重现、难回滚。
- ❌ 一条 RUN 装完不清理 apt cache → 层变大。
- ❌ `ENTRYPOINT`/`CMD` 写成 shell 形式导致信号（SIGTERM）收不到 → 用 exec 形式 `["bin","arg"]`。

---

## 延伸

- 面试题：见 `modules/kubernetes/kubernetes-questions.md`、`modules/cicd-iac/cicd-iac-questions.md`
- OCI 规范：image-spec / runtime-spec
- 构建：BuildKit（`DOCKER_BUILDKIT=1`）
