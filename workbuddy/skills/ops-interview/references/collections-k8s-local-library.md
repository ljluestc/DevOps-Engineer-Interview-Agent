# Kubernetes 本地资料库面试题 — 从 15 份本地 PDF 提炼（159 题）

> **来源**：用户本机的 Kubernetes 资料库（`~/Downloads`、`~/devops/Kubernetes`、`~/meetup-slides`）中的 15 份 PDF，逐份提炼；不含任何逐字摘录。
> **收录日期**：2026-09-20
> **说明**：这批资料与 `modules/kubernetes/kubernetes-study-guide.md` 所依据的 `k8s/slurps/` 网页存档互补——那边是官方文档与 Jimmy Song 手册，
> 这边是 **认证实操（CKS）、官方安全审计、行业调研、大厂实践演讲、存储厂商课件、社区笔记与排障手册**。每题附「要点」，只提炼自对应资料
> （命令、路径、数字、阶段划分均以原资料为准）；☆ = 面试高频；🟢/🟡/🔴 见文末图例。年代较早的资料（2018 / 2019）在分组说明里标注了已过时的点。
> **与 modules 的关系**：本批资料同时产出了 5 道标准化模块题——`kubernetes` Q51（超大规模控制面优化）、Q52（DRBD / LINSTOR / Piraeus 存储选型）、
> `cloud-security` Q15（CKS 实操清单）、Q16（1.24 官方安全审计）、`service-mesh` Q25（异构系统迁入网格）。出题时**优先用模块题**，本文件做追问与速答补充。

## 资料清单

| # | 资料 | 作者 / 出版方 | 年份 | 页数 | 版权口径 | 本文分组 |
|---|---|---|---|---|---|---|
| 1 | CKS Book（19 个实操场景） | Saiyam Pathak | 2024 | 66 | 商业电子书，仅提炼主题不含原题 | 一 |
| 2 | Kubernetes 1.24 Security Audit | NCC Group for CNCF / SIG Security | 2023 (v1.2) | 54 | © NCC Group，公开发布的审计报告，要点转述 | 二 |
| 3 | Kubernetes Deployment & Security Patterns | The New Stack（L. Hecht / Janakiram MSV / Chenxi Wang） | 2018 | 93 | © The New Stack，免费电子书，要点转述 | 三 |
| 4 | Introduction to Istio Ambient Mesh | Abdel Sghiouar（Google Cloud），Conf42 Kube Native | 2023 | 42 | 公开演讲 PPT | 四 |
| 5 | Tencent Music's service mesh practice with Istio and Aeraki | 赵化冰（腾讯云）/ 王诚强（腾讯音乐），IstioCon | 2021 | 41 | 公开演讲 PPT | 五 |
| 6 | 阿里巴巴 k8s 超大规模实践 | 曾凡松 / 汪萌海，阿里云云原生应用平台 | 2019 | 33 | 公开演讲 PPT | 六 |
| 7 | 云原生存储实战课程：Linstor + DRBD + Piraeus + KubeStorage 入门篇 | 全速云 MaxSpeedCloud | 2023 | 38 | 商业培训课件，仅提炼开源部分 | 七 |
| 8 | K8S Notes | MADHAV / IntelliQ IT 讲义 | — | 22 | 无声明 | 八 |
| 9 | Kubernetes Basic to Advance | Sagar Choudhary | — | 36 | 无声明 | 八 |
| 10 | Kubernetes Troubleshooting（practitioner's guide） | OpsCruise（厂商电子书） | — | 16 | 无声明 | 八 |
| 11 | Pipelines & Pods: DevOps with Kubernetes | Burr Sutter（Red Hat） | — | 72 | 公开演讲 PPT | 八 |
| 12 | End to End K8s notes | Aman Pathak「30DaysOfKubernetes」 | — | 293 | 无声明 | 九 |
| 13 | Kubernetes Cheatsheet | DevOps 社群速查表 | — | 6 | 无声明 | 十 |
| 14 | Kubernetes Cheat Sheet | Linux Academy | — | 2 | 无声明 | 十 |
| 15 | Spring Boot System Design Ground Up | 用户自有仓库文档（search-platform on EKS） | 2026 | 46 | 自有 | 未出题：内容已由 `system-design/` 子模块覆盖 |

---

## 一、CKS 实操场景：集群与工作负载加固（Saiyam Pathak《CKS Book》，19 题）

> 原书是 19 个「题面 + 解法」式的练习场景（不含真题）。这里把每个场景改写成面试问法，要点只保留可验证的命令、路径与语义。

1. ☆ 🟢 CKS 是什么？考试形式和前置条件有什么特别之处？
   - 要点：Linux Foundation 在 **KubeCon NA 2020** 推出的 **Certified Kubernetes Security Specialist**；**必须先通过 CKA** 才能报考；**2 小时纯实操**；特别之处是**大量第三方工具会直接出现在题面**（trivy、kube-bench、Falco、kubesec、AppArmor、seccomp），所以既考 K8s 又考「安全工具怎么用」。报名附赠两次 killer.sh 模拟环境。
2. ☆ 🟢 让 `dev` 命名空间里所有 Pod **拒绝一切出站流量**的 NetworkPolicy 怎么写？怎么验证？
   - 要点：`podSelector: {}` 选中全部 Pod，`policyTypes: [Egress]` 且**不写任何 `egress` 规则**即为「拒绝所有出站」；验证：策略前 `kubectl exec demo2 -n dev -- curl <demo1 IP>` 能拿到 nginx 页面，策略后 **Connection timed out**。Ingress 同理。
3. ☆ 🟡 写了「只允许 default 命名空间的 Pod 访问」的 NetworkPolicy，为什么 default 里的 Pod 还是连不上？
   - 要点：`namespaceSelector` 是**按 label 匹配**，而 default 命名空间**默认没有任何 label**；执行 `kubectl label ns default ns=default` 后立即生效。另一个细节：`ingress.from` 下**两个并列条目是「或」关系**（一条 `namespaceSelector`、一条 `podSelector`），写在同一条目里才是「与」；只给 Pod 打上 `demo=test` 标签（`kubectl label pod demo3 -n red demo=test`）就能命中第二条。
4. 🟡 怎样给 Pod 套一个「禁止一切写文件」的 AppArmor profile？如何确认生效？
   - 要点：节点上先看 `cat /sys/module/apparmor/parameters/enabled` 为 `Y`；写 profile（`profile deny_write flags=(attach_disconnected) { file, deny /** w, }`）后 `apparmor_parser -q deny_write` 加载，`aa-status | grep deny` 确认；Pod 用注解 `container.apparmor.security.beta.kubernetes.io/<容器名>: localhost/deny_write`（新版本迁到 `securityContext.appArmorProfile`）；验证 `kubectl exec deny -- cat /proc/1/attr/current` 输出 `deny_write (enforce)`，`touch /tmp/x` 报 Permission denied。
5. ☆ 🟡 RBAC 里 Role / ClusterRole 与 RoleBinding / ClusterRoleBinding 有哪些合法组合？怎么验证某个 ServiceAccount 到底能做什么？
   - 要点：合法：**Role + RoleBinding、ClusterRole + RoleBinding（把集群角色限定在一个命名空间）、ClusterRole + ClusterRoleBinding**；**Role + ClusterRoleBinding 是错的**。apiserver 需 `--authorization-mode=RBAC`。验证：`kubectl auth can-i delete deployments --as system:serviceaccount:demo:sam -n demo`；收窄权限直接 `kubectl edit clusterrole cr` 删掉多余的 apiGroups / resources / verbs，再用 `can-i` 复查。
6. 🟢 要求「扫描集群里所有 Pod 的镜像，把含 HIGH / CRITICAL 漏洞的 Pod 名写进文件」，怎么做最快？
   - 要点：先列镜像：`kubectl get pods -o jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{range .spec.containers[*]}{.image}{", "}{end}{end}' | sort`；逐个 `trivy image --severity HIGH,CRITICAL <image>` 看 `Total:` 行；把命中的 Pod 名 `echo` 进 `/opt/badimages.txt`。原书示例：nginx / httpd 有高危，alpine 为 0。
7. ☆ 🔴 怎样给 kube-apiserver 开启审计日志？策略文件的级别与匹配规则是什么？「只对 Deployment 记录 RequestResponse」怎么改？
   - 要点：编辑 `/etc/kubernetes/manifests/kube-apiserver.yaml` 加 `--audit-policy-file`、`--audit-log-path`、`--audit-log-maxsize`、`--audit-log-maxbackup`（还有 `--audit-log-maxage`），并**把策略文件与日志文件用 hostPath 挂进静态 Pod**（漏挂是 apiserver 起不来的头号原因）。级别四档 **None / Metadata / Request / RequestResponse**，规则**自上而下首个匹配生效**，`omitStages: [RequestReceived]` 减噪。改成 Deployment：`level: RequestResponse` + `resources: [{group: "apps", resources: ["deployments"]}]`（注意 Deployment **不在 core group**）。apiserver 静态 Pod 重启后 `audit.log` 里能看到带 `auditID`、`user`、`sourceIPs`、`authorization.k8s.io/decision` 注解的事件。
8. 🟡 用 kubeadm 把控制面从 1.28 升到 1.29，操作顺序是什么？Worker 节点有什么不同？
   - 要点：**cordon → drain（`--ignore-daemonsets`）→ 换 apt 源到 `pkgs.k8s.io/core:/stable:/v1.29` 并安装 `kubeadm=1.29.0-1.1` → `kubeadm upgrade apply v1.29.0` → 安装同版本 kubelet / kubectl → `systemctl daemon-reload && systemctl restart kubelet` → uncordon**；`kubectl get nodes` 看 VERSION。Worker 顺序相同，只是 `kubeadm upgrade node` 替代 `apply`。
9. ☆ 🟡 kube-bench 怎么跑？典型的 FAIL 项有哪些、怎么修？
   - 要点：可直接用容器跑：`docker run --pid=host -v /etc:/etc:ro -v /var:/var:ro -v $(which kubectl):/usr/local/mount-from-host/bin/kubectl -v ~/.kube:/.kube -e KUBECONFIG=/.kube/config -t aquasec/kube-bench:latest run --targets=master`（或 `node`）。原书示例 master 9 项 FAIL：**etcd 数据目录属主非 etcd:etcd（1.1.12）、`--kubelet-certificate-authority` 未设（1.2.5）、apiserver / controller-manager / scheduler 的 `--profiling` 未设 false（1.2.16 / 1.3.2 / 1.4.1）、`--audit-log-path / maxage / maxbackup / maxsize` 未设（1.2.17–1.2.20）**；修法都是改 `/etc/kubernetes/manifests/*.yaml`（例如 kube-controller-manager 加 `--profiling=false`）后重跑对比 PASS / FAIL 数。面试强调：**理解每条检查在改什么参数**，而非记安装命令。
10. 🟡 RuntimeClass 是什么？怎么让某个 Pod 用指定的容器运行时 handler？
   - 要点：containerd 配置里声明 handler（如 `[plugins.cri.containerd.runtimes.runc] runtime_type = "io.containerd.runc.v2"`）；创建 `apiVersion: node.k8s.io/v1, kind: RuntimeClass, metadata.name: demo, handler: runc`；Pod 里 `spec.runtimeClassName: demo`。生产用途是把不可信负载指到 **gVisor（runsc）/ Kata** 这类沙箱 handler。
11. 🟡 Falco 装在集群里和装在节点上有什么区别？怎么改一条规则的输出格式？
   - 要点：Helm 装（`helm install falco falcosecurity/falco`）是 DaemonSet，规则在 **ConfigMap** 里改；节点直装（apt）配置在 **`/etc/falco/`**：`falco.yaml` 的 `rules_file` 列出 `falco_rules.yaml`、`falco_rules.local.yaml`、`k8s_audit_rules.yaml`、`rules.d`，输出默认 stdout / syslog（`cat /var/log/syslog | grep falco`）。把「terminal shell in a container」的 output 改成 `"[%evt.time][%container.id] [%container.name]"`（字段见 falco.org supported-fields），触发方式是 `docker run -it ubuntu bash` 起一个交互 shell。事件可经 falcosidekick 转 Slack / Kafka / Lambda。
12. 🟢 把 Secret 以卷挂进 Pod 后，有哪两种方式把明文取出来？Pod 内 ServiceAccount token 在哪？
   - 要点：`kubectl create secret generic database --from-literal=username=sammy --from-literal=password=demo123`，Pod 里 `volumes[].secret.secretName` + `volumeMounts.mountPath: /etc/sec`（readOnly）。取回：① `kubectl get secret database -o yaml` 拿 base64 后 `echo … | base64 -d`；② `kubectl describe pod` 看 Mounts 找到路径，`kubectl exec demo -- cat /etc/sec/password`。SA token：`/run/secrets/kubernetes.io/serviceaccount/token`。
13. 🟡 PodSecurityPolicy 现在还能用吗？原书那道「禁止特权 Pod」的 PSP 题今天该怎么答？
   - 要点：PSP **1.21 弃用、1.25 移除**。原做法：apiserver `--enable-admission-plugins=NodeRestriction,PodSecurityPolicy`，PSP `privileged: false`（其余 seLinux / runAsUser / fsGroup / supplementalGroups 设 RunAsAny，volumes `'*'`），并给 SA 建 `verb: use` 的 Role + RoleBinding 才能用该策略；开插件前**必须先有一个默认放行策略**否则所有 Pod 都创建失败。今天用 **Pod Security Admission**：给命名空间打 `pod-security.kubernetes.io/enforce: restricted|baseline` 标签。
14. ☆ 🟡 如何让容器根文件系统只读，又不影响 nginx 这类需要写缓存 / 日志 / pid 文件的程序？
   - 要点：容器级 `securityContext.readOnlyRootFilesystem: true`；把 `/var/run`、`/var/log/nginx`、`/var/cache/nginx` 各挂一个 `emptyDir` 使其可写；验证 `kubectl exec … -- touch /etc/test` 报 **Read-only file system** 而 Pod 仍 Running。
15. 🟢 给你一堆 Pod 和 Dockerfile，要求「删掉不安全的」，你会盯哪些特征？
   - 要点：Pod：`privileged: true`、`allowPrivilegeEscalation: true`、`runAsUser: 0`（root）、挂宿主机敏感路径、Secret 明文写在 env；Dockerfile：`COPY secret .` 把密钥打进镜像、`USER root`、把密钥作为 CMD 参数。修法是删或改成非 root、drop 提权、密钥改走 Secret / 外部密钥管理。
16. 🔴 ImagePolicyWebhook 准入控制怎么配置？`defaultAllow: false` 意味着什么？
   - 要点：`--admission-control-config-file=/etc/kubernetes/demo/admission.json`，其中 `imagePolicy: {kubeConfigFile, allowTTL: 50, denyTTL: 50, retryBackoff: 500, defaultAllow: false}`；`kubeConfigFile` 是一个标准 kubeconfig，`cluster.server` 指向镜像校验服务（如 `https://service-check:8888/check-image`），带 CA 与 apiserver 客户端证书；apiserver 加 `--enable-admission-plugins=NodeRestriction,ImagePolicyWebhook` 并把配置目录 hostPath 挂进去。**`defaultAllow: false` = webhook 不可达时拒绝所有 Pod**（原书 dummy 服务下 `kubectl run nginx` 直接 Forbidden：`lookup service-check … no such host`），生产要权衡。真实实现可参考 kube-image-bouncer。
17. 🟡 自定义 seccomp profile 放在哪？Pod 怎么引用？放错位置有什么症状？
   - 要点：JSON（如 `{"defaultAction": "SCMP_ACT_LOG"}`）必须放在 **`/var/lib/kubelet/seccomp/`** 下（示例 `profiles/policy.json`），Pod 里 `securityContext.seccompProfile: {type: Localhost, localhostProfile: profiles/policy.json}`；放错位置事件报 `cannot load seccomp profile` 且容器创建失败；**每个可能调度到的节点都要有该文件**；验证 `kubectl get pod … -o jsonpath='{.spec.containers[*].securityContext.seccompProfile}'`。
18. 🟢 节点上有陌生服务监听 9999 端口，怎样找到并彻底停掉？
   - 要点：`netstat -tunlp | grep 9999`（或 `ss -tunlp`）拿 PID → `ps -f -p <PID>` 看到实际二进制（原书是复制成 `mycustomwebserver` 的 nginx，由自建 systemd 单元拉起）→ `systemctl stop mycustomwebserver && systemctl disable mycustomwebserver`（disable 会移除 `multi-user.target.wants` 里的链接）。
19. 🟢 kubesec 是干什么的？扫描结果里的 `critical` 怎么处理？
   - 要点：**静态扫描 K8s 清单的安全打分工具**（`kubesec scan pod.yaml`），例如 `containers[].securityContext.privileged == true` 记为 critical、**-30 分**，理由是特权容器近乎无限制访问宿主机；修法删掉 `privileged: true`，重扫并 `> /tmp/scan.txt`，`grep critical` 为空即通过。

## 二、Kubernetes 1.24 官方安全审计：19 个发现与威胁模型（NCC Group 为 CNCF / SIG Security 出具，2023 v1.2，15 题）

> 审计对象为 Kubernetes 1.24.0（2022 年夏执行），范围是 apiserver / scheduler / etcd 使用 / controller-manager / cloud-controller-manager / kubelet / kube-proxy / secrets-store-csi-driver。结果 0 Critical / 0 High / 6 Medium / 9 Low / 4 Info。要点里的 finding ID 与严重级别以报告为准。

### 审计范围与方法

20. 🟢 NCC Group 对 Kubernetes 1.24 的安全审计覆盖了哪些组件？最终发现的数量与严重级别分布如何？
   - 要点：范围为 **kube-apiserver、kube-scheduler、etcd 的使用方式、kube-controller-manager、cloud-controller-manager、kubelet、kube-proxy、secrets-store-csi-driver**，加上 **1.13 审计之后变更的所有部分**；**容器运行时自身的逃逸漏洞不在范围**，除非缺陷源自 Kubernetes 设置容器的方式。方法为 **架构评审 + 源码辅助评估**。结果 **19 个发现：0 Critical、0 High、6 Medium、9 Low、4 Informational**；按组件分布为 **架构评审 4、kube-apiserver 13、kubelet 2**；按类别为 Access Controls 7、Authentication 4、Cryptography 4、Auditing/Logging 2、Configuration 1、Data Validation 1。Overall Risk 是 **Impact 与 Exploitability 的综合评分**，属于优先级建议而非绝对结论。

21. ☆ 🟡 这份审计的威胁模型是怎么建立的？它假设了哪几类集群使用场景、哪些角色和哪些资产？
   - 要点：先从真实部署归纳出 **四种典型场景**——**生产应用部署 + 开发/测试环境隔离**、**CI/CD 流水线（含批处理）**、**代码执行即服务（Jupyter、脚本沙箱、PaaS）**、**多租户专属服务（每租户/每层级 SaaS）**；并同时覆盖 **自建集群与托管集群**。角色按权限分层：**平台管理员、节点管理员、集群级管理员、命名空间管理员、基础设施服务（apiserver/etcd/CoreDNS、CNI、Mesh、准入控制器）、工作负载、Operator、开发者、受限用户、外部非集群用户**；除最后一类外均默认拥有 `system:authenticated` 级别访问。资产包括 **组织外部资源、集群内部基础设施、应用密钥（SA token/第三方密钥）、应用数据（PII/PHI）、知识产权、服务可用性**。评审聚焦认证/授权、信任关系、RBAC 与组件权限。

22. ☆ 🔴 本次 1.24 审计相对上一轮 1.13 审计，在"历史遗留问题"上给出了什么结论？对团队的持续安全工作有何提示？
   - 要点：NCC 明确指出 **上一轮 1.13 审计的若干发现至今仍未修复（remain open/unfixed）**，建议在处理本报告发现的同时 **一并复盘并解决旧审计遗留项**。战略建议是：**简单可修的（如未净化的用户输入）应尽快在代码中修复**；**复杂修复短期难落地的，先更新官方文档告知用户风险**，长期再改。这体现了架构级问题（RBAC 无 Deny、访问控制机制割裂）往往只能靠文档缓释的现实。

### 具体发现（按组件）

23. ☆ 🔴 报告认为 Kubernetes RBAC 授权模型存在什么根本性设计缺陷？为什么说它"fail open"？
   - 要点：对应架构评审发现 **"Additive Access Controls"（PA6，Medium，Access Controls）**。RBAC **只做加法、不支持 Deny 规则**，只判断"是否被授予某权限"，无法在既有宽泛授权之上再叠加"禁止访问某资源"。因此当某 principal 因 **过于宽泛/通用的 Role 定义** 被意外授予权限时，模型 **"fail open"（默认放行）**。内部授权器（Node、RBAC）失败时只能返回 `DecisionNoOpinion` 而非 `DecisionDeny`，无法真正拒绝。建议：**引入支持显式 Deny 的 RBAC 模式**、支持"所有授权模式都通过才放行"、允许授权模式间子查询，并可用于对证书用户实现吊销。

24. ☆ 🔴 为什么审计说 Kubernetes NetworkPolicy 只能保证"命名空间级"而非"Pod 级"的隔离？它还有哪些局限？
   - 要点：对应 **"Multiple Concerns with Network Policies"（XE9，Low，Access Controls）**。NetworkPolicy **本质是 opt-in 且基于标签匹配**：只要命名空间内存在一条宽松策略，任何能创建/修改 Pod 的用户就能 **通过改 Pod 标签** 命中它、获得额外访问，即使 RBAC 已禁止其改策略本身。因此 **除非配合准入控制器强制校验标签**，NetworkPolicy 只能做到命名空间级粒度；唯一能覆盖全命名空间的办法是用 `podSelector: {}` 的默认拒绝策略。其他问题：**加法式访问控制**（允许的实体无法再禁止），**CNI 不强制实现、也无从判断策略是否真正被执行**，以及 **与集群 DNS 冲突**——Pod 必须能访问 CoreDNS，而递归解析可 **被滥用为绕过 egress 过滤的隐蔽信道**。建议长期用更聚焦 in-cluster 流量的方案替代，并要求 CNI 提供校验 webhook。

25. 🟡 Pod Security Standards 的 Restricted 配置被指出有哪些弱点？
   - 要点：对应 **"Weaknesses in Pod Security Standards Restricted Profile"（UCG，Low，Access Controls）**。Restricted 在 Baseline 之上要求 **不能以 root 运行、只能保留 `NET_BIND_SERVICE` 能力、必须启用 seccomp**，但 **只强制 `runAsUser` 非零，未要求 `runAsGroup` 非零**——**GID 0 的 Pod 仍可访问 root 组属组资源**。此外 seccomp 允许 `type: Localhost` 指向 `/var/lib/kubelet` 下的自定义 profile，用户可能 **选到比 `RuntimeDefault` 更弱的 profile**。建议：**新增禁止 `runAsGroup=0` 的限制**（允许非零或未定义），文档提醒勿暴露弱于 RuntimeDefault 的 seccomp，并引入 **变更型（mutating）PSS 准入控制器** 用安全默认值填充未设字段。

26. ☆ 🔴 "同一个 CA 同时用于客户端证书和请求头认证"为什么可能让任意认证用户提权到 cluster-admin？
   - 要点：对应 **"Common Certificate Authority Possible for Client CA and Request Header CA"（F9W，Medium，Authentication，Impact High）**。若 `--client-ca-file` 与 `--requestheader-client-ca-file` **配成同一个 CA**，且 **未设 `--requestheader-allowed-names`** 限制允许的 CN，则任何持有该 CA 签发客户端证书的用户，都能用 **请求头认证方案（Authenticating Proxy）** 伪造 `X-Remote-User` / `X-Remote-Group: system:masters`，**冒充任意用户/组**（报告演示：无权限用户直接请求得 403，加伪造头即 200）。建议：**apiserver 应拒绝两 CA 相同且未设 allowed-names 的配置**，并在文档中明确风险（同理共用 etcd 客户端 CA 也会让任意用户直连 etcd）。

27. ☆ 🟡 "Path Traversal in Namespace Specifier"是什么？攻击者用 `..` 作为命名空间能做什么？
   - 要点：对应 **"Path Traversal in Namespace Specifier"（RKV，Medium，Access Controls，Exploitability High，Impact Low）**。API 会把命名空间里的 **`..` 目录穿越序列** 传到后端，`path.Join` 拼接 etcd root（`/registry`）时解析掉，**etcd 查询范围被放大**。RBAC 仍按集群作用域校验，但 **list 请求会从缩短后的路径递归枚举**：借助 **continuation token（分页）** 可逐字符推断 etcd 中对象名（信息泄露）；对 **CRD（按 unstructured 处理、无固定 schema）** 甚至可返回其他类型对象（演示中对 Calico `networksets` 一次拿到 11 个不同类型对象，`remainingItemCount` 暴露总数），构成访问控制绕过。建议：**像 `NamespaceKeyFunc` 一样校验命名空间，拒绝 `..` 和 `.`**（合法命名空间不可能叫这个名字，无副作用）。

28. ☆ 🔴 apiserver 与 kubelet 之间的代理信任链有什么问题？为什么 `nodes/proxy` 权限如此危险？
   - 要点：涉及两条 kube-apiserver/kubelet 发现。**"Redirection of API Server Traffic to Kubelet"（JAV，Medium，Authentication）**：apiserver 代理到 kubelet 时会 **用自己的客户端证书（通常属 `system:masters`）** 认证；拥有 **`nodes/proxy` GET + `nodes/status` PATCH 或 `nodes` CREATE** 的用户可把节点 status 里的地址与 `KubeletEndpoint.Port` **改成 apiserver 自己的 IP 和 6443**，使 apiserver **用 master 证书请求自己**，从而以 cluster-admin 读写任意资源。**"Privilege Escalation via nodes/proxy Permission"（WV3，Medium，kubelet，Impact High）**：仅有 `nodes/proxy` 权限即等于对任意节点 kubelet API 拥有 master 级访问，可调 kubelet `/exec` **在任意 Pod 内执行命令**，而 **官方文档未说明这一点**。建议：**阻止 proxied 请求被发往 apiserver web 端口**，并在文档中明确 `nodes/proxy` 会覆盖其他 nodes 子资源权限。

29. 🟡 API server proxy 在 TLS 校验上有什么隐患？哪种情况例外？
   - 要点：对应 **"API Server Proxy Disables TLS Certificate Validation"（MRE，Medium，Cryptography，Impact High）**。apiserver 代理到 Pod/Service/Node 时 **不校验目标 TLS 证书**（`CreateProxyTransport` 里 `InsecureSkipVerify: true`，且 API 根本没有指定 CA/信任库的入口），**网络中间人可 MITM 拦截/篡改** apiserver 到目标的连接（客户端到 apiserver 的连接不受影响）。**例外**：代理到 kubelet 时 apiserver 会用自身证书认证并 **校验 kubelet 证书**（但由此引出 JAV 问题）。建议：为代理实现证书校验或至少文档标明可能受 MITM。

30. 🟢 审计在审计日志（audit log）里发现了什么弱点？为什么它对"入侵后隐蔽"很关键？
   - 要点：对应 **"Authentication Source Not Shown in Audit Logs"（R44，Low，Auditing and Logging）**。审计日志记录了请求的 **用户名和组，却不记录用于确定身份的认证来源**。攻击者若拿到 **签发用户证书的 CA**，可造一张 CN 为 `system:serviceaccount:kube-system:replication-controller` 的证书，其请求在日志中 **与该 SA 的正常请求无法区分**，从而在 **入侵后持久化/隐蔽** 时不易被察觉。建议：**在审计日志中记录不可变的认证来源**，便于界定入侵范围。

31. 🟡 Bootstrap Token 在报告里被点了哪几处问题？为什么重要？
   - 要点：三条发现。**"Low Entropy Bootstrap Tokens"（WHE，Info，Cryptography，Impact High）**：secret 为 **16 个 base-36 字符 ≈ 83 bit 熵**，低于 **静态密钥应有的 128 bit** 惯例；可基于 `cluster-info` configmap 签名做离线暴力破解，拿到 token 者可 **把自己的节点作为 master 加入集群**。**"Logging of Incorrect Bootstrap Tokens"（WVM，Low，Auditing and Logging）**：认证失败时会把 **token secret 明文写进 apiserver 日志**（verbosity 3），typo 或异地有效的密钥会泄露；建议 **不在日志输出 token 值**。**"Timing Side Channel in Bootstrap Tokens Generation and Handling"（TTV，Info，Cryptography）**：`randBytes()` 查表取字符与用正则 `IsValidBootstrapToken()` 校验 **均非常数时间**，可能通过时序侧信道泄露 token；建议 **常数时间生成/比较、避免用正则处理秘密数据**。

32. 🟡 报告在 apiserver 上还列了哪些低危/信息级弱点（Loopback token、代理头处理、常数时间比较、路径构造）？
   - 要点：一组低影响发现。**"Loopback Token Usable Externally"（47W，Low，Authentication，Impact High）**：启动时生成的 `system:apiserver`（属 `system:masters`）loopback token **不校验来源接口**，且运行期间 **不轮换**；建议校验其只在 loopback 接口被接受。**"Incorrect Handling of Proxy Authentication Headers"（YVU，Low，Authentication）**：聚合层剥离 `X-Remote-*` 头时 **用写死的默认头名**，若管理员改了 `--requestheader-*-headers`，攻击者可用 **自定义名的组头（如 `system:masters`）** 混过剥离并被扩展 API server 采信而提权。**"Non Constant-Time Comparison of Service Account Token Secrets"（PCK，Info，Cryptography）**：SA token 比较用非常数时间的 `bytes.Equal`（当前不可行，且 1.22 起推荐改用 **TokenRequest API**）；建议用 `subtle.ConstantTimeCompare`。**"Dangerous File Path Construction"（B4Y，Info，kubelet）**：kubelet `/logs` 用 `path.Join("/var/log", 用户输入)` 拼路径且未校验 `..`，**仅因 Go `http.Server` 自动净化而不可利用**；**"Inaccurate X-Forwarded-Uri Header"（HFV，Low，Configuration）**：代理构造 `X-Forwarded-Uri` 时解析掉 `../`，下游若信任该头可能做出错误安全决策。

33. 🟢 "EmptyDir Volumes Do Not Support Mount Options"说明了什么问题？
   - 要点：对应 **"EmptyDir Volumes Do Not Support Mount Options"（7HM，Low，Access Controls）**。emptyDir 卷 **不支持 `nosuid`/`noexec` 等挂载选项**，因此当用户按最佳实践用 **只读根文件系统 + 可写 emptyDir 做临时/日志空间** 时，无法禁止在该空间执行文件；攻破容器者可把恶意工具写入 emptyDir 并执行。该问题此前已作为 GitHub issue #48912 上报。建议：**允许 emptyDir 以 `noexec` 挂载**。

### 威胁模型与加固建议

34. ☆ 🔴 综合这份审计：进入并控制一个 Kubernetes 集群有哪几条"经典攻击路径"？据此你会给多租户/代码执行型集群提哪些优先加固建议？
   - 要点：报告把安全关切分为 **集群访问 / 节点访问 / 服务访问** 三类，经典路径包括：(1) **`nodes/proxy` 提权**——apiserver 用 master 证书访问 kubelet，直达任意 Pod exec（WV3、JAV，Medium）；(2) **共用 CA + 请求头认证** 让任意证书用户冒充 `system:masters`（F9W，Medium/Impact High）；(3) **拿到签发 CA 伪造身份**，因审计日志不记认证来源而隐蔽（R44）；(4) **命名空间 `..` 穿越** 扩大 etcd 查询做信息泄露/CRD 越权读取（RKV，Medium）；(5) **RBAC 加法/无 Deny + NetworkPolicy 靠标签 opt-in** 导致意外放行与横向移动（PA6、XE9）；(6) **Bootstrap token 低熵/被日志泄露** 后把恶意节点当 master 加入（WHE、WVM）。对应加固建议：**用准入控制器（OPA Gatekeeper/Kyverno）兜底强制标签、seccomp、`runAsGroup≠0`**；**apiserver 不共用 client-ca 与 requestheader-ca 并设 `--requestheader-allowed-names`**；**审慎授予 `nodes/proxy`、`nodes/status` 写权限（视同 cluster-admin）**；**审计日志记录认证来源、避免日志泄露 token**；**弃用 SA token Secret 改用 TokenRequest API**；**NetworkPolicy 用默认拒绝 `podSelector: {}`**；**复查 1.13 审计遗留未修项**。风险整体为 0 Critical/0 High，多需既有较高权限或错误配置才触发。

## 三、Kubernetes 部署与安全模式（The New Stack《Kubernetes Deployment & Security Patterns》，2018，24 题）

> 2018 年出版的电子书：数据篇（CNCF 2017 调查）+ 部署模式篇 + 安全模式篇。**注意年代**：书里的 PodSecurityPolicy 已在 1.25 移除（用 Pod Security Admission）、ABAC 与静态密码认证已不推荐、`--admission-control` 已改名 `--enable-admission-plugins`；调查百分比是 2017 年的快照，面试引用时要说明背景。

### 数据篇：Kubernetes 部署现状（What the Data Says）

35. ☆ 🟡 根据 CNCF 2017 年调查，Kubernetes 用户面临的主要容器挑战是什么？不同规模、不同部署环境的组织差异在哪里？
   - 要点：挑战排序为 **安全 46%**、网络 42%、存储 41%、监控 38%、复杂度 37%（仅第五）、日志 32%、可靠性 27%、按负载扩缩 23%、选型困难 22%、厂商支持 10%；**1000 人以上企业 55% 认为安全是挑战，100 人以下仅 39%**；6 个以上集群的组织中网络挑战从 42% 升至 53%；**仅私有部署的组织存储是头号挑战（54% vs 云上 34%）**，仅公有云部署的组织更多提到监控与日志；私有部署组织只有 9% 认为扩缩是问题；中型企业（100–999 人）最容易在监控上"卡在中间"。

36. 🟢 2017 年调查中 Kubernetes 用户最常用的网络插件、服务暴露方式和 Ingress 提供者分别是什么？
   - 要点：网络插件 **Flannel 38%、Calico 35%**、发行版默认 27%、CNI 原语（bridge/p2p）20%、kubenet 17%、Weave Net 15%，Canal（Tigera，Flannel+Calico 组合）5%，Cilium 仅 2%；对外暴露以 **LoadBalancer 型 Service 59%** 为主，L7 Ingress 35%、NodePort 29%、集成第三方/硬件负载均衡 28%；Ingress 提供者 **NGINX 56%、HAProxy 30%**、Træfik 13%、F5 13%、Envoy 10%、GLBC 10%；**6 个以上集群的组织 HAProxy 使用率翻倍（20%→43%）**，F5 与 Envoy 也翻倍；纯私有部署组织使用 LB Service 的可能性低 37%，使用硬件 LB 集成的可能性高约 50%。

37. 🟢 调查显示 Kubernetes 用户的监控与日志技术栈是什么样的？用户对 Prometheus 有哪些抱怨？
   - 要点：监控 **Grafana 64%、Prometheus 59%**、InfluxDB 29%、Datadog 22%、Graphite 17%、Sysdig 12%、OpenTSDB 10%；日志 **Elasticsearch 74%、Fluentd 50%**、Splunk 19%、Graylog 14%；Fluentd 常替代 Logstash，故有 **EFK** 栈之称；Splunk 因非开源在中国使用较少；用户反馈：Prometheus 缺少原生认证/授权、希望在 K8s API 中定义规则、**"仅本地存储"的架构不够生产级**、已有 InfluxDB 告警体系难以迁移、厂商声称的原生日志集成常常不可用只能自写转换器。

38. 🟡 从调查数据看，Kubernetes 通常由谁部署、部署在哪里、规模多大？
   - 要点：**69% 的组织用 K8s 管理容器**，但近三分之二的 K8s 用户同时使用其他管理方式（Amazon ECS 20%、Docker Swarm 18%、GKE 17%、OpenShift 12%）；**83% 至少部署到一个公有云**，多云组合占约四分之三；**91% 的部署由内部完成**，78% 由受访者自己团队实施，仅 9% 借助外部公司；**认为耗时超预期的人数（38%）是低于预期（15%）的两倍多**；45% 使用厂商提供方案但 74% 同时使用社区发行版（测试/生产各用一套）；仅 12% 运行 20 个以上集群，1000+ 容器的组织中该比例升至 35%；<1000 容器的组织 74% 只有 ≤5 个集群；容器越多越可能用 K8s（1000+ 容器组织 81% 使用）；云厂商品牌容器服务采用率低，多数人直接在 IaaS 上自部署发行版。

39. 🔴 一家只在自有数据中心跑 Kubernetes 的大企业和一家只在公有云上跑的初创公司，各自应优先解决什么问题？请用数据支撑你的建议。
   - 要点：私有部署优先解决 **存储**（54% 视为挑战，往往由独立存储团队管理），可关注当时主流云原生存储项目 **OpenStorage 12%、OpenEBS 7%、OpenSDS 6%、Minio 6%、Rook 4%**；私有部署还倾向复用已投资的 **硬件负载均衡**，多一个需要管理的组件；OpenStack 用户多为 1000+ 容器的大型组织，集群数也更多；公有云组织优先解决 **监控与日志与云厂商自带工具的集成**（可能因云厂商监控/日志系统与既有工具不兼容）；大企业更关注安全与网络（跨站点带宽、站点数多）；评估新工具时要看其与现有和未来技术栈的集成，网络已开始向 Flannel/Calico 收敛。

### 部署模式篇：从自建到 PaaS（Kubernetes Deployment Patterns）

40. ☆ 🟡 一个生产级 Kubernetes 集群除了 K8s 本身，还需要哪些关键组件？各自作用是什么？
   - 要点：**核心基础设施**（裸金属/虚拟化/私有云/公有云 IaaS，提供计算网络存储）；**Overlay 网络**（Calico、Flannel、Romana、Weave Net）；**软件定义存储**（Gluster、NFS、块存储，以 PV 暴露）；**高可用控制平面**（多 master 暴露 API）；**分布式 KV 数据库 etcd**（单一事实来源，需冗余）；**执行环境**（worker 节点，需可弹性自动扩缩）；容器化负载；**供应与配置管理**（Ansible/Chef/Puppet/Terraform，保证一致可重复、便于升级打补丁）；**镜像仓库应与集群同地部署**（降低延迟、提升安全）；日志监控（Elastic Stack、Grafana、Prometheus）；**负载均衡器同时暴露控制平面 API 和应用入口**；制品库（有时兼作镜像仓库）；构建发布自动化（Bamboo、Jenkins、Shippable）；不同部署模式下这些层的归属在客户和厂商之间转移。

41. 🟢 列举几种自建 Kubernetes 集群的安装工具及各自适用场景。
   - 要点：**kubeadm** — 自动配置控制平面和执行环境，CentOS/Ubuntu 有原生包，可用于裸金属和虚拟化，2017 年 12 月仍为 beta 但足够稳定；**conjure-up**（Canonical）— Ubuntu 16.04+，可面向 AWS/Azure/GCE/Joyent/OpenStack/VMware；**kops** — AWS 官方部署工具，支持跨多可用区高可用，GCE/vSphere 为 alpha；**Kubespray** — 基于 Ansible 的 playbook 集合，可选 Calico/Canal/Flannel/Weave 网络；**Kubernetes-anywhere** — 面向 OpenStack（Keystone v3、Neutron LBaaS v2、Nova）与 VMware，生成 OVF 模板引导集群；**Cloud Foundry Container Runtime** — 用 BOSH 工具链部署，作为 CF PaaS 的底层容器平台；CoreOS 基于 Terraform 的裸金属安装器（安装 Tectonic）；基于 kubeadm 的 Ansible playbook；VMware Photon Controller；书中列出的裸金属支持发行版：CentOS 6、Fedora 25/26、RHEL 7、Ubuntu 16.04。

42. ☆ 🟡 比较自建、托管 Kubernetes、CaaS、Kubernetes PaaS 四种部署模式在控制力、成本、技能要求和内置能力上的差异。
   - 要点：**可定制性**：高 / 中高 / 中低 / 低；**总体成本（软件+基础设施）**：高 / 中 / 高 / 高；**人力与支持成本**：高 / 中 / 低 / 低；**管理技能要求**：高 / 中 / 低 / 低；**镜像仓库**：自建不含、托管视厂商、CaaS 与 PaaS 内置；**跨云可移植性**：自建低、托管高（依赖云厂商认证发行版）、CaaS/PaaS 视厂商；**内置补丁/安全/监控**：除自建外均含；**内置高可用、基础设施自动扩缩、快速供应**：仅 CaaS 与 PaaS；**完整应用生命周期管理（ALM）**：仅 PaaS；决策原则：要控制权选自建，要开发者体验选 PaaS。

43. 🟡 什么情况下应该选择自建（self-hosted）Kubernetes？它的隐性代价是什么？
   - 要点：需要 **对整个栈的绝对控制** 或高度定制（操作系统、存储后端、Overlay 网络），或想用其他模式尚未提供的前沿特性时选自建；软件几乎全开源、**只需投资基础设施，是最便宜的选项**，但要计入人员和支持成本；客户拥有从计算网络存储到镜像仓库的全部责任（公有云上 VM 和块存储由 IaaS 管）；社区频繁发版，**低停机升级需要高级 K8s 管理技能**；镜像要靠近集群，必须自建私有仓库；调查中"实现复杂"是不采用 K8s 的首要原因之一，社区因此推动 kubeadm 等工具简化安装。

44. 🔴 托管 Kubernetes（Managed Kubernetes）与自建相比，责任如何划分？CNCF 一致性认证解决了什么问题？请举例说明厂商差异。
   - 要点：厂商 **远程维护集群健康并周期性升级到最新版本**，客户仍要支付基础设施费用外加订阅/许可费，**比自建贵**，但长期看升级/补丁/安全/监控服务可抵消成本；图示中 **厂商只管核心编排引擎**，负载均衡、制品库、CI/CD、监控日志、镜像仓库等仍归客户（**许多托管厂商没有集成镜像仓库**）；**2017 年 11 月 CNCF 推出 Certified Kubernetes Conformance Program**，认证支持所需 API 的平台，保证跨产品可移植与互操作；厂商示例：Giant Swarm（AWS 与私有，**通过 API 给客户完整管理员权限**）、IBM Cloud Private（数据中心内，含私有镜像库和监控）、Madcore（内置 Spark 与深度学习，仅 AWS）、Platform9（SaaS 型、基础设施无关、承袭 OpenStack 管理经验、单一控制平面、SSO）、StackPoint（三步部署，支持 AWS/DO/GCP/Azure，一键升级、联邦集群、应用市场）、Tectonic（CoreOS，2018 年被 Red Hat 收购；绑定 Container Linux 与 Operator，自维护 etcd/K8s，支持 LDAP/SAML）。

45. ☆ 🔴 CaaS（如 EKS/AKS/GKE）的架构特点、优缺点是什么？各家云厂商在控制平面 HA 与计费上有何差异？
   - 要点：**云厂商托管 master、向客户暴露 worker 节点**，几分钟内获得高可用、安全的集群，是"最短路径"；内置监控、日志、自动扩缩、自动升级、自愈，与 LB、防火墙、存储、镜像仓库、DevOps 工具链深度集成；缺点：**控制力弱、K8s 版本升级可能滞后、不一定支持所有插件、无法选择存储后端**，且多数厂商同时收取 VM 费和节点管理费，**比其他模式贵**；**EKS**（re:Invent 2017 发布）在 **3 个可用区运行 3 个 master**，自动检测替换不健康 master，托管 etcd，集成 VPC/IAM/EBS/ELB/CloudTrail；**AKS 只收节点 VM 费用、master 免费**，并配套托管镜像仓库；**GKE** 有 SLA、最早升级到新版本、配 Google Container Registry；Alibaba 与 Huawei 的 CaaS 当时 **缺少私有镜像仓库**；PKS（Pivotal+VMware+Google）跑在 vSphere 和 GCP 上，与 vRealize/vSAN/Wavefront 集成，负载可在 GKE 与 PKS 间迁移，面向混合云。

46. 🟢 Kubernetes 之上的 PaaS 与其他部署模式的根本区别是什么？有哪些代表产品？
   - 要点：其他模式面向管理员和 DevOps，**PaaS 面向开发者：提交源码而非镜像或 Pod**，平台负责源码转镜像、服务发现、扩缩、自愈、监控与日志，开发者甚至不必知道底层是 K8s；提供跨私有云/公有云一致的开发体验和端到端 ALM；缺点是 **灵活性和可定制性最低，许可模式偏贵**；代表：**Red Hat OpenShift**（开源 Origin、托管 Online、企业版 Container Platform，集成 Ansible/Git/Jenkins 的 ALM 流水线）、Mesosphere DC/OS（Marathon PaaS 层 + 集成 K8s，桥接 Hadoop/Spark 等有状态服务与 12-factor 应用）、Hasura（基于 K8s 的 BaaS，跑在 DigitalOcean，CLI 推送 GitHub 源码）。

47. 🟡 除常规编排外，书中提到 Kubernetes 有哪些新兴使用场景？各自依赖 K8s 的什么能力？
   - 要点：**边缘计算** — 边缘资源被当作一个集群，K8s 作集群管理器，得益于 **同时支持 x64 与 ARM**（例：AWS Greengrass、Azure IoT Edge）；**机器学习** — NVIDIA 提供带 CUDA 库的镜像，数据科学家把算法打包成镜像后并行拉起数千容器训练，**Kubeflow** 提供 TensorFlow CRD，可一键选择 CPU/GPU 并调节规模，常与 GKE/ACS 上的 GPU 资源配合；**Serverless** — 事件驱动，函数以 Docker 容器运行，K8s 做运行时管理（OpenWhisk、Fission、Kubeless、nuclio、OpenFaaS）；**流式分析** — Kafka/Spark 的摄入与实时分析层需快速弹性，依赖 **StatefulSet 与 HPA** 原语（例：Iguazio）。

### 多租户与云原生安全观（赞助商访谈）

48. 🔴 在多租户容器环境中，共享内核带来什么风险？gVisor/Kata 这类方案能解决什么、不能解决什么？
   - 要点：Aqua CTO 观点：容器仍可能 **利用宿主机 Linux 内核漏洞影响同节点其他容器**；**gVisor、Kata Containers 通过增加一层来处理共享内核与多租户问题**；但更大的问题是应用安全——**无需内核漏洞，错误的应用逻辑同样能让人进入容器拿到数据**，需要缩小应用攻击面；容器隔离把安全问题拆成 **基础设施平面与应用平面**，两者可分开治理，但隔离多租户服务在生产中的行为仍是未解问题；Twistlock CTO 补充：**容器行为应当是可预测的，因此安全可以更可预测、更自动化**；Alcide CTO 提出 **"policy fusion"**，把多种策略统一为一套以便安全随集群规模扩展。

### 安全模式篇：威胁模型与基线（Kubernetes Security Patterns）

49. ☆ 🔴 描述 Kubernetes 的四类威胁模型，以及针对每类威胁的核心对策。什么是"爆炸半径"？
   - 要点：**① 外部攻击**（API server、kubelet、etcd 被攻破）→ 只暴露必要服务、始终强制认证、为暴露服务配置网络策略；**② 容器/节点被攻陷**（容器提权控制其他容器或集群）→ 用命名空间和网络分段隔离、启用 OS 级控制、**限制特权容器数量**；**③ 凭证泄露**（管理员凭证被盗）→ 最小权限、RBAC 等细粒度访问控制、密切监控用户行为；**④ 合法权限滥用**（配置错误、缺少控制、缺少监控，如无网络策略时用户可读其他命名空间流量）→ 对容器/Pod/命名空间/kubelet 全面加固、正确设计授权、利用 K8s 授权插件架构；后果包括提权、数据外泄、运营中断、合规违规；**爆炸半径** = 一个被攻陷的容器能危害同节点多少容器、一个被攻陷节点能危害集群多少；整章设计目标就是最小化爆炸半径。

50. 🟢 Kubernetes 安全可以从哪四个维度来组织？各自包含哪些控制？
   - 要点：**认证与授权**（API 是中心接口，用户与 service account 都要经过认证、授权和准入控制）；**资源隔离**（Pod 与命名空间的 CPU、内存请求、持久存储限制，防 DoS 并保护数据隐私）；**加固与网络安全**（限制特权容器、限制提权、限制访问宿主机网络与文件系统；网络分段、**TLS 客户端认证保护 API**、服务网络 ACL）；**日志与审计**（K8s 1.9 beta 的 Audit Logging 记录谁访问了哪个 API）；此外 **S-SDLC 与安全监控** 等集群外控制也应纳入全生命周期考虑。

51. 🟡 从节点、镜像、仓库三个层面说明容器安全的最佳实践。
   - 要点：**节点**：遵循 **CIS Docker Benchmark 与 CIS Kubernetes Benchmark**；启用 **SELinux（内核级文件/网络访问控制）和 Seccomp（限制系统调用集合）**；节点通信用 TLS 客户端证书，关键 API 端到端 TLS；**限制 SSH 直连，所有访问经由 K8s 以保证访问控制与日志**；**镜像**：核心是漏洞管理，扫描 CVE 只是起点，需与 **运行时强制（只部署通过扫描和加固策略的镜像）** 和 **修复（扫描集成进 CI/CD，结合 rolling update 把有漏洞的容器下线换成新镜像）** 打通；**仓库**：管控允许拉取的仓库，用私有仓库只放经扫描审核的镜像，必须用公共仓库时部署前扫描，**扫描不通过就让部署失败**。

52. ☆ 🟢 一个 Kubernetes API 请求会依次经过哪些模块？Kubernetes 支持哪些认证方式？
   - 要点：顺序为 **认证模块 → 授权模块 → 准入控制 → 访问对象**；账号分人类用户与 **service account（受管、绑定到特定命名空间、凭证以 Secret 形式存在）**；多个认证器 **按顺序调用，任一成功即通过，全部失败返回 401**；认证方式：**客户端证书**（`--client-ca-file`，用证书 Subject CN 作用户名）、**静态 Token**（`--token-auth-file`）、**静态密码**（`--basic-auth-file`，不安全且改密码要重启 API server）、**Bootstrap Token**（alpha，动态创建并作为 Secret 存于系统命名空间，`--experimental-bootstrap-token-auth`）、**service account JWT**（挂载进 Pod；**能读 Pod Secret 的用户就能冒充该 service account**）；还可通过认证代理或 webhook 扩展。

53. ☆ 🟡 对比 Kubernetes 的 Node、ABAC、RBAC、Webhook 四种授权模块；配置多个授权模块时如何决策？
   - 要点：**Node** — 专门处理 kubelet 发起的读写和认证相关请求；**ABAC** — 用用户、组、命名空间、资源名、API 动词等属性对照 JSON 策略文件，`--authorization-mode=ABAC --authorization-policy-file=…`，策略文件必须在建集群时指定（例：给 Alice 对 AccountInfo 命名空间 pods 的只读权限，写请求被拒）；**RBAC** — 按角色授权，**Role 限于单命名空间，ClusterRole 跨命名空间**，把 get/watch/list 等动词组合成角色，可通过编辑角色防止不必要的提权，`--authorization-mode=RBAC`；**Webhook** — API server 把用户、组、资源、命名空间、操作打包成 JSON POST 给外部 REST 服务，返回 allowed true/false，适合 **位置、时段等动态上下文** 的授权逻辑，`--authorization-webhook-config-file`；**多个授权模块是逻辑 OR：任一允许即放行，全部拒绝才拒绝**（与准入控制的 AND 语义相反）；模块必须在建集群时配置。

54. ☆ 🟡 准入控制（Admission Control）在什么阶段起作用？PodSecurityPolicy 和 DenyEscalatingExec 分别控制什么？
   - 要点：在 **认证授权之后、请求被最终接受之前** 执行，用于基于容器/资源的运行上下文而非身份的细粒度策略；插件 **编译进 API server**，按 `--admission-control=NamespaceLifecycle,PersistentVolumeLabel,PodSecurityPolicy,DenyEscalatingExec` 的有序列表依次运行，**全部通过才放行，任一拒绝立即拒绝**；**PodSecurityPolicy** 控制：是否允许特权容器、是否允许访问宿主机 root 命名空间/网络/端口/文件系统、根文件系统是否只读、是否允许提权、AppArmor/Seccomp profile；示例策略：`privileged: false`、`allowPrivilegeEscalation: false`、`runAsUser: MustRunAsNonRoot`、`hostNetwork: false`，最常见用途是禁止以 root 运行；PSP 只有在准入控制器中启用才生效；**DenyEscalatingExec** 拒绝对特权 Pod 执行 exec/attach，防止用户借此获得原本没有的权限，运行特权容器时强烈建议启用。

55. 🟢 Kubernetes 的命名空间和 ResourceQuota 分别提供什么隔离？请解释一个配额示例。
   - 要点：**命名空间是虚拟分区**，让多团队共享集群且资源互不可见；初始三个：**default、kube-system、kube-public（全体用户可读）**；常见按 dev/test-QA/staging/prod 划分；优势之一是 **同名服务可跨命名空间复用**（如 account_balance 在各环境同名，也可用 account_balance.dev.myapp 全名区分）；API 请求和授权策略都可限定命名空间（`kubectl --namespace=AccountInfo run …`）；**不要运行无资源上限的容器**，否则有资源饥饿和 DoS 风险；**ResourceQuota** 限制命名空间内 Pod/对象数量、CPU 与内存的 request 和 limit 总量、存储、本地临时存储；示例：`pods: 7`、`requests.cpu: 1`、`requests.memory: 2Gi`、`limits.cpu: 3`、`limits.memory: 3Gi`，即最多 7 个 Pod，所有容器内存请求总和 ≤2GiB、上限总和 ≤3GiB，CPU 请求总和 ≤1、上限总和 ≤3；需在 `--admission-control` 中加入 ResourceQuota 才生效。

56. 🟡 Kubernetes 审计日志记录什么？为什么对 Secret、ConfigMap 这类资源只记录 Metadata 级别？
   - 要点：集群级审计日志应 **独立于应用日志、容器引擎日志和主机日志**；**K8s 1.9 的 Audit Logger（beta）** 记录用户、管理员或系统组件对 API 的操作——发生了什么动作、何时、谁发起、影响了哪些资源；通过 **audit-policy YAML** 指定记录哪些事件及记录级别；对 **secrets、configmaps、tokenreviews 只记 Metadata 级别，因为其内容可能包含敏感数据**，完整记录会把敏感信息写进日志；用途：监控、调试、取证、满足合规并生成合规报告；最佳实践总结为"**记录一切、始终记录**"。

57. ☆ 🟡 Kubernetes 默认的 Pod 网络行为是什么？如何用 NetworkPolicy 做网络分段，它的局限在哪？
   - 要点：**默认所有 Pod 接受来自任何来源的流量**；NetworkPolicy 用于限制谁能与 Pod 通信，防止同命名空间内被攻陷的应用横向攻击；每条策略必须指定作用的 Pod 集合，**`podSelector: {}` 表示作用于命名空间内全部 Pod**，并通过 `policyTypes` 声明是 Ingress 还是 Egress 规则；书中示例是名为 default-deny 的 Ingress 策略，配合 podSelector 限制来自标签 db 的 Pod；NetworkPolicy 相当于 **条件满足时自动下发的动态防火墙规则**；局限：**要实现真正的微分段，策略需超越 ingress/egress、IP 和端口这几个维度**；服务级安全还应叠加客户端证书与认证授权。

58. ☆ 🔴 新接手一个开源发行版搭建的 Kubernetes 集群，你会按什么清单加固它？为什么"默认拒绝"是正确起点？
   - 要点：前提认知：**许多开源发行版默认不开启甚至不包含全部安全特性**，需要深入了解平台；可选捷径是 OpenShift/Tectonic 等预置安全插件的商业平台，或 Alcide、Aqua、Cavirin、HyTrust、Twistlock 等把高层策略自动翻译成 K8s 原生策略的产品；自管清单：**① 配置 PodSecurityPolicy**，对"是否需要特权模式 / 是否允许提权 / 是否需要宿主机网络、PID、IPC 命名空间 / 是否需要 root"四个问题 **默认全部回答"否"**，因为仅 `hostNetwork=true` 就可能导致提权；**② 启用授权插件（RBAC/ABAC）与合适的准入控制器**，DenyEscalatingExec 是好习惯但可能妨碍特殊操作，要权衡；**③ 用 NetworkPolicy 限制服务间访问** 以缩小攻击面；**④ 主动管理漏洞**，来源包括镜像、操作系统乃至硬件（如 Spectre/Meltdown），在应用、环境、部署全生命周期使用漏洞评估工具；**⑤ 全生命周期视角**：只有批准的代码进入镜像、只有批准的镜像进入生产，加固节点，运行时开启正确控制，记录一切日志。

## 四、Istio Ambient Mesh 入门（Abdel Sghiouar，Conf42 Kube Native 2023，8 题）

> 演讲者为 Google Cloud 开发者布道师、Kubernetes Podcast 主持人。当时 ambient 仍标注为「experimental」，以下按演讲内容整理，版本演进请以 Istio 当前文档为准。

59. ☆ 🟡 Sidecar 模式解决了什么问题，又带来了哪四个具体麻烦？
   - 要点：把 mTLS、证书管理、路由、遥测、策略这些「应用层的智能」放到进程外代理，实现语言无关、应用零改造。麻烦：**侵入式**（要改工作负载，不能热插入；安装 / 卸载 / 升级都要重启 Pod）；**会弄坏某些 HTTP 实现不规范的应用**；**为 sidecar 超额预留资源**；升级困难。
60. ☆ 🟡 Ambient 数据面的设计目标是什么？
   - 要点：**对应用无干扰**（不改工作负载即可热插入，破坏流量风险低，透明零停机升级）；**与 sidecar 版 Istio 兼容**（流量可与 sidecar Pod 互通，能从「只要 mTLS」平滑升到完整 Istio）；**像勾选框一样简单地开关**。
61. ☆ 🔴 Ambient 把网格拆成哪两层？每层分别提供什么能力？
   - 要点：去掉 sidecar，把代理拆成两部分：**Secure Overlay 层**由每节点一个共享的 **ztunnel（DaemonSet）** 实现——与其他 ztunnel / waypoint 之间做认证与加密（mTLS 隧道）、**L4 策略与 TCP 指标日志**；**L7 处理层**由完整的 **waypoint proxy（Envoy）** 按需提供——HTTP 路由与负载均衡、熔断、限流、故障注入、重试超时、丰富的授权策略、HTTP 指标 / 访问日志 / 追踪。
62. 🟡 传统 sidecar 与 ambient 分别怎样把流量「劫持」到代理？这对热启用意味着什么？
   - 要点：Sidecar：代理作为容器与应用共享 Pod 网络命名空间，**Pod 内 iptables** 把进出流量转给 sidecar，节点网络栈不动，但注入 sidecar 要改 Pod 定义并重启。Ambient：**由 CNI 在节点层把工作负载流量重定向到 ztunnel**，实现「不可绕过」且可以**动态开启**，Pod 无需重启。
63. ☆ 🔴 HBONE 是什么？它修复了传统 Istio 代理流量的哪些问题？
   - 要点：传统模式下客户端每条连接都对应代理间一条新 TCP 连接，mTLS 流量**沿用原端口**，Envoy 靠**嗅探**判断是否加密——这在 PERMISSIVE 模式下会**弄坏 server-speaks-first 协议（如 MySQL）**。HBONE 把所有流量**通过一条 mTLS 的 HTTP CONNECT 隧道**（固定端口 **15008**）传输：修复 server-speaks-first 问题、**多条连接摊薄一次 mTLS 握手成本**、不再需要嗅探或元数据交换 hack、网络策略只需放行单一端口，并把加密与应用彻底解耦。
64. 🟡 什么情况下仍然应该选 sidecar 而不是 ambient？
   - 要点：应用需要**专属代理资源**；站点需要 **EnvoyFilter 之类深度定制**；受监管环境要求既有部署模型；团队就是习惯 sidecar。演讲者的预期是 ambient 会成为多数用户的首选，但 sidecar 会长期支持，**两者可以共存并互通**。
65. 🟢 Gateway API 的资源模型是怎样按角色划分的？
   - 要点：**GatewayClass** 由基础设施提供方 / 平台管理员定义（如 `istio-ingress`、`gke-l7-gxlb`）；**Gateway** 由集群运维创建，绑定 GatewayClass 与域名 / TLS 证书 / 默认策略；**HTTPRoute** 由应用开发者在自己的命名空间写，可**跨命名空间**挂到共享 Gateway；它是 Ingress 与 Istio API 的演进，标准化 L4 / L7 负载均衡与网格，当时已有 8+ 实现。
66. 🟢 HTTPRoute 比 Ingress 「更有表达力」体现在哪？
   - 要点：同一路由里可按 **header 匹配**（如 `version: canary` 转到 `foo-v2`）和 **权重分流**（`foo-v1` 80% / `foo-v2` 20%）；对比 Istio 的 VirtualService + DestinationRule 子集做 95 / 5 金丝雀，语义相近但资源模型标准化、角色分离更清晰。

## 五、Istio + Aeraki 在腾讯音乐的服务网格落地（赵化冰 / 王诚强，IstioCon 2021，11 题）

> 上半场讲 Aeraki Mesh 与 MetaProtocol 的原理，下半场讲腾讯音乐的迁移实践。要点保留了讲者给出的原始数据与阶段划分。

67. 🟢 服务网格提供哪三类能力？微服务里除了 HTTP 还有哪些常见的七层协议？
   - 要点：**流量控制**（服务发现、路由、负载均衡、灰度、重试、断路器、故障注入）、**可观察性**（遥测、调用跟踪、拓扑）、**通信安全**（身份认证、访问鉴权、加密）。非 HTTP 七层协议：**RPC**（Thrift、Dubbo、私有 RPC）、**消息**（Kafka、RabbitMQ）、**缓存**（Redis、Memcached）、**数据库**（MySQL、PostgreSQL、MongoDB）——多数网格对它们只能按 **TCP** 处理。
68. ☆ 🟡 对这些协议，「四层治理」和「七层治理」到底差在哪？
   - 要点：得到的（L3/L4）：基于 VIP / Pod IP 的服务发现（DNS 只用于拿 IP，Envoy 无感知）、四层负载均衡与基于连接错误的重试 / 熔断、IP + Port 路由、TCP 收发包数指标。期望的（L7）：基于**逻辑服务名**的发现、七层负载均衡与**按应用错误码**重试熔断、**按协议头（服务名 / 方法名）路由**、RPC 层故障注入、**请求级指标**（调用次数 / 失败率）、**调用跟踪**。
69. 🔴 如果不用 Aeraki，要在 Istio 里原生支持一个自定义 RPC 协议需要改哪些东西？为什么难？
   - 要点：控制面要**解析新的 CRD 字段并生成 xDS 下发**；数据面要写一个完整的 Envoy filter 做**编解码、解析 header、路由、负载均衡、熔断、故障注入、遥测采集**。难点：Istio **缺少良好的协议扩展机制**、Istio 代码要理解 Envoy filter 里协议特定的知识、在 Istio 里维护众多七层协议代价太大。
70. 🟡 Aeraki 第一版架构做到了什么、卡在哪？
   - 要点：做到：与 Istio 无缝集成、**对 Istio 无侵入**，能管理 Envoy 已实现的非 HTTP 协议（Dubbo、Thrift、Redis）。卡点：Envoy 的 Dubbo / Thrift filter **功能受限**（不支持 RDS、限流、一致性哈希、流量镜像、调用跟踪，实现也不一致）；支持一个新协议**数据面要写完整 TCP filter、控制面要写一个 Aeraki 协议插件**，工作量巨大。
71. ☆ 🔴 MetaProtocol 的核心洞察是什么？它把「支持一个新协议」压缩到了什么程度？
   - 要点：洞察：**大部分七层协议的路由 / 熔断 / 负载均衡逻辑相似**——HTTP/1.1 用 host + path/method/headers，HTTP/2 用 `:authority` 伪头，gRPC 用 path，TARS 用 ServantName / FuncName / Context，Dubbo 用 service name / version / method，**任何 RPC 协议本质都是「消息头里的服务名 + 若干 key:value」**。因此 MetaProtocol Proxy 把负载均衡、熔断、动态路由、消息头修改、本地 / 全局限流、请求指标、调用跟踪做成通用逻辑，新协议**只实现 Decode / Encode 两个扩展点（数百行代码）**，并提供 C++ / WASM / Lua 的 L7 filter 扩展点做认证授权等自定义逻辑。
72. 🟡 MetaProtocol 的请求路径和响应路径分别是怎样的？Metadata 与 Mutation 两个结构各起什么作用？
   - 要点：请求：**Decoder** 解析下游请求并填充 **Metadata**（decode 时得到的 key:value，供 L7 filter 使用）→ L7 filter 处理并把要修改的数据写入 **Mutation**（encode 时用来改包）→ **Router** 按 RDS 规则选 upstream cluster → **Encoder** 按 Mutation 封包 → 发往上游。响应：Decoder 解析上游响应填 Metadata → Router 按 **connection / stream 对应关系**找回下游连接 → L7 filter 响应方向处理写 Mutation → Encoder 封包 → 回给下游。
73. 🟡 采用 / 不采用 Aeraki Mesh，在网格里管理一个私有协议的工作量差多少？
   - 要点：数据面：不用 → 写一个**完整的 Envoy L4 filter**；用 → **只实现 codec 接口（数百行）**。控制面：不用 → **为该协议专门写一个控制面**（魔改 Istio 或从零写）；用 → **零**，Aeraki 可作为任何基于 MetaProtocol 协议的控制面。项目模板：meta-protocol-awesomerpc。当时已有 MetaProtocol-Dubbo / Thrift / tRPC（腾讯内部）/ 腾讯音乐私有协议 / 融媒体私有协议，Redis、Kafka、ZooKeeper 走 Envoy 原生 filter；落地方包括腾讯融媒体 / 冬奥会直播、腾讯音乐、小红书等。
74. 🟡 腾讯音乐上网格前面临的复杂度是什么？技术选型的五条标准是什么？
   - 要点：业务黏度高、对稳定性敏感、历史包袱重；**多协议**（HTTP / gRPC / 私有协议）、**多网格**（Istio 1.3.6 / 1.10 / 异构 Mesh / 非 Mesh）、**多服务发现**（L5 / Polaris / Consul / DNS）、**多语言框架**（C++ / Go / Node.js）、**K8s 与 VM 混布**。期望：平滑迁移、低侵入、流量透明可控、支持私有协议与多种服务发现。选型标准：**通用性**（sidecar 适配各框架）、**兼容性**（Aeraki 作第二控制面，不改 Istio）、**易用性**（MetaProtocol 轻松支持私有协议）、**完备性**、**可持续性**（基于社区迭代）。接入私有协议只需实现 decode / encode / onError。
75. ☆ 🔴 网格外的旧注册中心（如北极星 Polaris）里的服务，怎样让网格内看得见？服务怎样分步迁进网格？
   - 要点：**Polaris-Controller** 把服务自动注册到北极星；自研 **Polaris2Istio** watch 北极星变更并同步为 Istio **ServiceEntry**；Pilot 再通过 xDS 下发到数据面（Aeraki 还提供 Consul2Istio、Dubbo2Istio、Eureka2Istio）。迁移四步（从 4 到 1 自动推进）：**方式 4** 服务在网格外、用旧服务发现 → **方式 3** 仍在网格外、旧服务名通过网格内 ServiceEntry 接入 → **方式 2** 服务进网格、旧服务名指向 K8s Service → **方式 1** 直接用 K8s Service 名、旧名作别名。
76. 🔴 两套旧 Istio 网格怎样合并到一套新网格？分几个阶段？
   - 要点：**一阶段**：新网格创建指回旧网格的 Gateway、对应 VirtualService、指向旧网格 Gateway 的 ServiceEntry（可编程自动创建），验证网络后把服务迁到新网格；**二阶段**：流量权重切到新网格，在旧网格创建指向新网格 Gateway 的**占位 ServiceEntry**，卸载旧网格中的服务；**三阶段**：移除指向旧网格的 ServiceEntry，全部服务落在新网格。实操还要盯**资源水位**与**网络互通**。
77. 🟡 迁完之后，私有协议在网格里获得了哪些治理能力？本地限流有什么容易误解的地方？
   - 要点：**按命令字路由**：变更前流量不分命令字全去 v1，变更后严格按命令字去对应版本，因此可做**全链路染色**——开发环境按分支版本隔离、生产按业务需求区分版本。**限流**分本地与全局：**本地限流按单 Pod 计**，总量随 Pod 数线性增长（例：Pod 数为 2 时「一分钟前 4 次成功」），可按条件（如只限子命令 2）限流。另有自定义协议指标、全局限流、负载均衡、熔断、改消息头。规划：业务全覆盖、Tracing 全面打通、治理平台化。

## 六、阿里巴巴 K8s 超大规模实践（曾凡松 / 汪萌海，阿里云云原生应用平台，2019，10 题）

> KubeCon China 2019 演讲 PPT（33 页）。数字与阶段划分均为演讲当时口径。

78. 🟢 阿里的容器体系经历了哪几个阶段？
   - 要点：**2013** 初步探索：基于 lxc 自研 t4 容器替代 VM 部署；**2015** 统一资源池：自研 **Sigma** 调度系统收敛众多运维平台，发展出弹性与混部；**2017–2019** 全面拥抱云原生：从 Sigma 转型 k8s 体系，尝试面向终态的运维；**2019 双 11** k8s 支撑了阿里史上规模最大的集群。
79. 🟡 为什么 k8s 能在阿里落地成功？演讲给了三个理由。
   - 要点：**繁荣的社区与生态**（云上云下、集团内外都可用）；**声明式 API 契合阿里「面向终态」的运维设计哲学**；**模块化、可扩展的架构**足以满足多样的应用运维需求。
80. ☆ 🟡 2019 年阿里 k8s 的规模数字是多少？跑了哪些类型的负载？
   - 要点：**数十个集群、数十万节点、单集群 10,000 节点、数万个应用、超百万容器**；负载包括在线服务、AI 作业、FaaS、中间件；底层是 IDC 上的神龙裸金属、ECS、ECI。
81. ☆ 🔴 落地 k8s 面临的两大难题是什么？对应提出了哪三条升级路线？
   - 要点：难题一「**业务形态多样**」：运维链路复杂、应用定义标准缺失；难题二「**集群规模庞大**」：多种工作负载、向全面云化演进。路线：**面向终态升级**（提高应用运维效率）、**自愈能力升级**（统一容器与应用实例生命周期、简化启动流程）、**不可变基础设施**（分离基础设施与应用容器）。
82. 🔴 「过程式运维」在 3000 个实例升级时会出什么问题？面向终态的应用管理需要哪些能力、又要怎么控风险？
   - 要点：过程式由运维平台逐步驱动容器平台，链路长、状态一致性难保证；面向终态只声明期望（例如**最大不可用数 200**），由 k8s 调谐。所需能力：**终态副本数保持、容器原地升级、保持 IP 与卷、并发更新与容错暂停、镜像预热与按需下载**。风险控制：决策分散到 controller / operator / rescheduler 后，要在 **kube-apiserver 的 admission 层与 kubelet 层各做 throttling / circuit breaker**，并做风险识别。
83. 🟡 「容器即应用」想解决传统运维体系的什么效率问题？
   - 要点：传统链路里应用启动要串联监控、VIP、服务注册、配置中心等多个平台，**启动流程复杂、决策链路长、状态一致性有风险**。做法：**统一容器与应用实例的生命周期**、把应用的冗余度信息下沉到 k8s 平台（Eviction Controller 等据此决策），并把公共运维能力沉淀成 **Operator 平台 + sidecar framework + 运维能力编程框架**。
84. 🟡 阿里如何理解「不可变基础设施」？OpenKruise 提供了哪些工作负载？
   - 要点：从「Dockerfile 打包业务 + 运维进程（logtail、monitor、sshd）」进化到「**业务容器与运维基础设施容器分离**，组合成一个 Pod，一次定义多次运行，各自独立升级」——对应 **SidecarSet**。OpenKruise 组件：**AdvancedStatefulSet、SidecarSet、BroadcastJob、CloneSet、UnitedDeployment（当时即将推出）**。
85. ☆ 🔴 apiserver / etcd 这一层做了哪些性能优化？
   - 要点：先建**监控大盘**（RT/QPS、资源使用率、链路、服务异常、队列长度、gRPC、长连接分布、请求分布）和**压测平台**。负载均衡：**周期性重建连接**让长连接在 apiserver 副本间重新均衡、webhook 链路 HTTP/2 → HTTP/1.1 并设置 maxSurge、必要时 kubelet 直连、升级 etcd client 到 v3.3.15。**List & Watch**：网络抖动造成 informer 全量重 List 的风暴，用 **Bookmark** 让客户端持有更新的 resourceVersion（rv=3 → rv=11）避免 `too old version`。**Cache Read & Index**：List / Get 走 apiserver 缓存并做**一致性读**（先取 etcd 的 rv@t0，等缓存 rv 追上再返回，Cache Ready 约 5 s），支持**动态新增索引**（nodename、namespace、labels），Describe node 从 5 s 降到 0.3 s。
86. 🔴 规模化调度在稳定性上考虑哪些维度？调度策略是怎么产生和更新的？
   - 要点：维度：**应用 / 核心应用**、拓扑（**单机 / AZ**）、应用互斥 / 亲和、资源竞争、容灾、负载均衡、节点负载感知、资源利用率预测。策略产生：**调度策略中心**把专家策略与**离线特征分析**结果写成 CR，经 webhook 更新到调度器；具体策略有 **CPU 精细化分配、应用按 AZ / Node 打散、CPU 敏感 Pod 打散、节点 CPU / Load 感知、Pod 近期最大 CPU 利用率感知**；节点负载均衡依赖离线统计出的「应用预估峰值 CPU」CR。
87. 🟢 演讲最后提出的云原生应用管理方向是什么？
   - 要点：特征是**标准化、开放、一次定义随处运行**；对应阿里与微软联合推出的 **OAM（Open Application Model，openappmodel.io）** 应用定义与架构模型。

## 七、云原生块存储：DRBD / LINSTOR / Piraeus / KubeStorage（全速云 MaxSpeedCloud，2023，8 题）

> 商业培训课件「入门篇」。前两部分讲概念与原理，第三部分是基于 Sealos + KubeStorage 的安装实操；KubeStorage 是厂商工具，题目聚焦开源部分。

88. 🟢 课件给云原生存储列了哪六个特点？
   - 要点：**高可用**（副本 + 故障转移）、**存储性能**（吞吐 MB/s / GB/s 与 IOPS）、**可扩展性**（客户端、吞吐、容量、集群四个维度）、**强一致性**（写成功后立即可读到最新）、**耐用性**（长期不丢数据）、**动态部署自动供应**（Operator 部署、CSI 动态供给）。
89. ☆ 🟡 云原生存储方案分哪几类？各类有哪些代表项目？
   - 要点：**本地存储**：OpenEBS（LocalPath / LVM / ZFS）、Carina；**分布式文件**：CephFS（Rook）、CubeFS、JuiceFS、NFS；**分布式块**：Ceph RBD（Rook）、OpenEBS（Mayastor / cStor / Jiva）、Longhorn、**Piraeus + LINSTOR + DRBD**；**S3 对象**：Ceph RGW（Rook）、MinIO。
90. ☆ 🟡 DRBD 是什么？它的四个特性是什么？DRBD 9 新增了什么？
   - 要点：**Distributed Replicated Block Device**，基于软件、无共享、**块级别的镜像复制（网络 RAID 1）**；特性：**实时**（写入即持续复制到对端）、**透明**（应用不知道数据在多节点）、**同步或异步**（同步：所有节点写完才通知应用；异步：本地写完即通知）、**低消耗**（内核驱动，超融合无需独立存储服务器）。Linux **2.6.33（2009）起主线集成**；DRBD 9：**最多 32 副本、双主写、更低 CPU / 内存开销、支持有盘 + 无盘节点（两有盘 + 一无盘仲裁）**。
91. 🟡 DRBD 的同步为什么快？三个管理命令各干什么？
   - 要点：**多次连续写同一块只同步一次**、按磁盘自然布局顺序同步（寻道少）、**可变速率**（检测同步网络可用带宽并与前台 I/O 对比自动调节）、用**校验和**减少传输。工具：`drbdadm`（高级前端，读 `/etc/drbd.conf`，实际调用后两者）、`drbdsetup`（把配置载入内核，参数全走命令行，很少直接用）、`drbdmeta`（创建 / 转储 / 恢复 / 修改元数据，极少直接用）。
92. 🟡 DRBD Proxy 解决什么场景？
   - 要点：**跨站点（双城）近实时复制**：在两站点间加一层**压缩 + 缓存**缓冲区，低带宽下也能高效传输；典型部署是**本地两副本同步 + 异地异步复制**（课件给的例子是北京到上海延迟不超过 1 秒）。
93. ☆ 🟡 LINSTOR 由哪三个组件构成？各自职责和高可用方式？
   - 要点：**linstor-controller**：保存整个集群配置的数据库、做需要全局视角的决策，通常用 Pacemaker 做 HA，可部署多个但**只能激活一个**；**linstor-satellite**：跑在每个要用 DRBD 存储的节点上，**无状态**，通过 `drbdadm` / `lvcreate` / `zpool` 管理本地 LVM 逻辑卷或 ZFS zvol，是节点代理；**linstor-client**：命令行工具，通过 controller 的 REST API 下发命令与查看状态。LINSTOR 支持快照、加密、缓存。
94. ☆ 🔴 Piraeus 是什么？它宣称比 Ceph 快「数倍」的依据和代价分别是什么？
   - 要点：CNCF 开源项目，用 **CSI** 把 DRBD + LINSTOR 接进 K8s，自动化卷的创建 / 扩容 / 删除 / 快照 / 还原；模块：linstor-csi、Piraeus Operator、HA Controller、**linstor-scheduler-extender**、drbd-shutdown-guard、kubectl-linstor。依据：Ceph **用户态**多副本强一致同步产生网络延迟，且 **CPU / 内存随卷数线性增长**、I/O 能力随之下降，难以与容器超融合；Piraeus 走**超融合**——数据与容器在同一批物理机，**调度扩展保证 Pod 只落在本地有副本的节点，读走本地盘**。代价：**没有本地副本的节点不会被调度**，副本数受有盘节点限制，需要维护内核模块。厂商引用的 Ampere 三节点 NVMe 基准：随机 4K 读 25.5M IOPS、写 3.16M、顺序读 103 GiB/s。
95. 🟡 部署 DRBD / LINSTOR 集群时有哪些实践要点？
   - 要点：**NVMe 用 LVM**（性能最佳但不能快照），**SATA / SAS 用 ZFS**（在线换盘、校验自愈、快照，可用 NVMe 做读写缓存）；三节点**必须用 chrony 同步时间**；先卸载旧的 8.4 版 `drbd.ko`，装完 `modinfo drbd` 确认 **9.2.x**；调大 `net.core.rmem_max` / `wmem_max`（示例 16777216）并重启 kube-proxy；**复制网络与管理网络分开**（基准环境用两块 100GbE）；LINSTOR 自己的 etcd 放 **local-path** 本地 StorageClass；客户端 `/etc/linstor/linstor-client.conf` 的 `controllers=` 指向 controller Service IP；用 Rancher / Sealos 装的集群要删掉 `kube-controller-manager` / `kube-scheduler` 静态 Pod 里的 `--port=0` 才能让 `kubectl get cs` 正常。

## 八、K8s 学习笔记与排障手册（IntelliQ IT 讲义 / Sagar Choudhary《Kubernetes Basic to Advance》/ OpsCruise《Kubernetes Troubleshooting》/ Burr Sutter《Pipelines & Pods》，26 题）

> 四份社区笔记与厂商电子书，价值在排障案例（Pending / CreateContainerConfigError / CrashLoopBackOff / NetworkPolicy 阻断 / 抢占驱逐）与命令细节。

### 核心对象与命令速答

96. ☆ 🟢 `kubectl create -f` 和 `kubectl apply -f` 有什么区别？各适合什么环境？
   - 要点：`create` 是**命令式（imperative）**管理，告诉 API 要创建 / 替换 / 删除什么；对象已存在时会**直接报错**。`apply` 是**声明式（declarative）**管理，描述期望状态，对象已存在时不报错，且对活动对象做过的修改（如 `scale`）在再次 `apply` 其他变更时会被**保留**。笔记建议：命令式操作活动对象用于 **Dev / QA 等低环境**，声明式操作 yaml/json 文件用于**生产环境**。

97. 🟢 `kubectl logs` 常用的参数有哪些？容器反复重启时如何看上一次崩溃的日志？
   - 要点：`kubectl logs my-pod` 看 stdout；多容器 Pod 用 `-c my-container`；按标签批量看 `-l name=myLabel`；`-f` 流式跟踪；`-f -l name=myLabel --all-containers` 跟踪一组 Pod 的全部容器。**关键**：容器崩溃重启后当前日志可能为空，要用 **`--previous`**（可与 `-c` 组合）看**上一次实例**的日志。

98. 🟢 Label 与 Selector 有哪两类匹配方式？ReplicationController 与 ReplicaSet 在这点上有何差异？
   - 要点：Label 是无预定义语义的 key/value，创建后可随时增改（`kubectl label pod <name> env=dev`），值 ≤63 字符且首尾必须是字母数字。Selector 分 **equality-based**（`=` / `!=`）和 **set-based**（`in` / `notin` / `exists`），如 `kubectl get pods -l 'env in (dev,test,qa)'`；查看用 `--show-labels`，按标签删除用 `kubectl delete pod -l env=dev`。**RC 只支持 equality selector，RS 支持 set-based selector**，RS 是 RC 的下一代、更偏声明式，但官方建议直接用 Deployment 管理 RS。

99. 🟡 Deployment 的发布、回滚、暂停 / 恢复分别用什么命令？为什么要"暂停"再"恢复"？
   - 要点：改镜像 `kubectl set image deployment.v1.apps/<deploy> <container>=<image>`；看进度 `kubectl rollout status deployment/<deploy>`；看版本 `kubectl rollout history deployment/<deploy>`（`--revision=2` 看某版本细节）；回滚 `kubectl rollout undo deployment/<deploy>`，或 `--to-revision=2` 指定版本。**暂停 / 恢复**：`rollout pause` 后连续 `set image`、`set resources ... --limits=cpu=200m,memory=512Mi` 等多处修改，期间 `get rs` 不会出现新 RS；`rollout resume` 后**只触发一次滚动更新**，避免多次不必要的发布。附：新 RS 命名固定为 `[deployment-name]-[random string]`；`kubectl get deploy` 的 READY 是 ready/desired，UP-TO-DATE 是已更新到期望模板的副本数；滚动更新中途扩容会按比例分配到各活动 RS（proportional scaling）。

100. 🔴 用 Deployment 部署 MySQL 一主多从为什么做不到？StatefulSet 具体解决了哪几个问题？
   - 要点：主从需要**主先起、从依次起并从前一个节点克隆数据**，且从库要用**固定地址**指向主库。Deployment 的 Pod **同时启动、名字随机**，主库 Pod 崩溃重建后名字变化，从库指向的地址失效。StatefulSet：**按序创建**（前一个 Running & Ready 才起下一个）、**序号索引**从 0 递增、名字固定为 `<sts>-0/1/2`（`mysql-0` 即主，`mysql-3` 知道从 `mysql-2` 克隆），Pod 重建后**保留同名（sticky identity）**。使用前提：需要自建 **Headless Service**（`clusterIP: None`）提供网络身份；`volumeClaimTemplates` 为每个 Pod 各分配一个 PVC；缩容 / 删除 STS **不会删 PV**，需手动清理；默认 OrderedReady 策略下滚动更新可能进入需人工修复的坏状态；想有序优雅终止可先缩到 0 再删。

101. ☆ 🟢 ClusterIP、NodePort、LoadBalancer、Headless Service 分别解决什么问题？
   - 要点：**ClusterIP** 是默认类型，只在集群内可达，用于微服务组件互通。**NodePort** 在每个节点开同一端口做 NAT 转发，端口从 `--service-node-port-range` 指定范围分配（默认 **30000–32767**），不写 `nodePort` 则随机分配；可用 kube-proxy 的 `--nodeport-addresses` 限定监听 IP；minikube 上用 `minikube service list` 拿访问 URL。**LoadBalancer** 依赖云厂商 LB，**minikube 跑不了**（笔记原话：只能在托管 K8s 上用），LB 创建是异步的，结果写在 `.status.loadBalancer`，同时会自动创建 NodePort 与 ClusterIP。**Headless**（`clusterIP: None`）不分配 VIP、不做负载均衡，DNS 查询直接返回**各 Pod IP**，客户端可直连，适合 MongoDB 单 Pod、StatefulSet 等场景。

102. 🟢 除了让调度器自动放置，把 Pod 约束到特定节点有哪几种方式？`required` 与 `preferred` 有何区别？
   - 要点：三种方式：**nodeSelector**（最简单，节点必须带齐所有指定 label）、**Affinity / Anti-affinity**、**nodeName**。Affinity 比 nodeSelector 更有表达力，可写**软规则**，还可以基于**其他 Pod 的 label**（inter-pod affinity）决定同置 / 反同置。`requiredDuringSchedulingIgnoredDuringExecution` 不满足就**不调度**（等价于 nodeSelector 的强约束）；`preferredDuringSchedulingIgnoredDuringExecution` 尽量满足，找不到也**照样调度**。笔记提到的典型用途：把 Pod 放到带 SSD 的节点、把通信频繁的两个服务放在同一可用区。

### 排障：Pod 与节点

103. ☆ 🟡 CrashLoopBackOff 中的 Crash、Loop、BackOff 各指什么？为什么重启间隔越来越长？
   - 要点：**Crash** 是容器主动或被动退出（进程退出、**OOM kill** 等），弄清 crash 原因才能修。**Loop** 是 K8s 设计使然：你声明"要有一个 Pod 在跑"，kubelet 发现它死了就再拉起，反复循环。**BackOff** 是为避免失败循环耗尽资源，重试几次后加入**逐渐变长的等待期**，Pod 恢复健康后计时**重置**。笔记归纳的常见根因类别：前置条件配置、所需资源访问、资源分配、性能问题、功能性故障。

104. 🔴 按容器生命周期"三阶段"排查 Pod 故障，各阶段的责任方和典型错误分别是什么？
   - 要点：**Preparation 阶段**是 **K8s 的责任**：锁定前置条件（拉镜像、找配置项、调度），典型错误 `CreateContainerConfigError`、`ImagePullBackOff` / `ErrImagePull`、节点不可用、PV 不可用、安全策略、**资源不足**。**Initialization 阶段**是**应用的责任**：应用读配置、连数据库、访问外部服务、加载依赖库，典型错误是数据库连不上、配置缺失或无效、外部认证服务 / 第三方 API 不可达、库文件缺失。**Run 阶段**：应用正常服务后崩溃，典型是 **Node Pressure 驱逐、PriorityClass 抢占、NodeNotReady 驱逐、应用自身退出**（内存泄漏、未处理异常）。价值在于：先判断故障在哪个阶段，就能决定该看 `describe` 的 Events 还是看 `logs`。

105. ☆ 🟢 Pod 一直 Pending，`kubectl describe` 里看到 `0/5 nodes are available: 1 node(s) had taint that the pod didn't tolerate, 4 Insufficient memory`，怎么解读、怎么修？
   - 要点：调度器按 **resources.requests** 找节点，请求 64Gi 内存而节点只有更少可用时就无法调度，Pod **停在 Pending** 直到请求降低或节点资源变化。事件解读：1 个节点带 taint（是 **Master**，无 toleration 默认不调度业务 Pod），其余 4 个内存不足。三种修法：**加大节点 / 新增大节点**、**调低 request**（案例改成 `2Gi` 后 `kubectl apply` 即 Running）、或用 **nodeSelector / taints & tolerations 重新平衡**已有节点上的负载。若负载确实需要那么多资源，降 request 不是选项。

106. ☆ 🟡 Pod 状态显示 CreateContainerConfigError 通常是什么原因？如何定位并修复？
   - 要点：Pod 引用的 **ConfigMap 或 Secret 不存在**。K8s 启动 Pod 时会校验清单中引用的配置资源是否存在，缺失即报此错。定位：`kubectl describe pod <pod> -n <ns>` 拉到 Events，能看到 `Error: configmap "key-cm" not found`；`kubectl get configmap -n <ns>` 确认确实没有。修复：按 Pod 期望的 key 创建 ConfigMap 并 `kubectl apply`，**Pod 无需重建**，会自动从 `ContainerCreating` 进入 `Running`。附：ConfigMap 存非敏感数据，Secret 存敏感数据，两者都可作环境变量、启动参数或挂载文件，用于把镜像与配置解耦。

107. ☆ 🟡 一个 Pod 先 Running 再 Error 再 CrashLoopBackOff 反复循环，`describe` 只看到 `Back-off restarting failed container`，下一步怎么查？
   - 要点：Pod 已经启动并在跑应用代码，说明**已过 Preparation 阶段**，`describe` 的 Events 里只剩 BackOff 记录，**没有根因**，必须看容器日志 `kubectl logs <pod> -f`。案例：Bitnami Apache 用 `kubectl create configmap httpd-cm --from-file=httpd.conf` 挂载配置，日志最后一行 `Syntax error on line 178 of httpd.conf: Could not open configuration file .../components.conf`，是从别的环境带过来的 `Include` 指令引用了不存在的文件。修复流程：改本地 httpd.conf 注释该行 → `kubectl delete configmap httpd-cm` 再 `create configmap --from-file` 重建 → `helm uninstall apache` 后 `helm install apache bitnami/apache --set httpdConfConfigMap=httpd-cm` 重装 → `kubectl get pods --watch` 确认 RESTARTS 不再增长。

108. 🟡 `kubectl describe pod` 里 `Last State: Terminated, Reason: Error, Exit Code: 1` 说明什么？接下来查什么？
   - 要点：**Exit Code 1 表示应用层错误退出**，问题在应用而非 K8s，应转向 `kubectl logs`。案例：Pod 运行 40 分钟正常，4 小时后 RESTARTS 到 40 并 CrashLoopBackOff；日志显示 `Could not connect to loki after 10 retries` 且是 ws 3100 端口的 IO Error。连接失败的候选原因：DNS 解析、路由、防火墙、配置错误；本案例最终根因是 **NetworkPolicy**（见网络组第 18 题）。修复后判断标准：**RESTARTS 计数停止增长**，即使数值仍显示 41。

109. 🔴 一个健康的、没有报错的 Pod 为什么会被 K8s 主动终止？请说明驱逐阈值与 PriorityClass 抢占机制。
   - 要点：两种情况。**Node Pressure 驱逐**：节点资源超分且吃紧时，kubelet 按软 / 硬阈值驱逐 Pod 回收资源，硬阈值：`memory.available < 100Mi`、`nodefs.available < 10%`、`imagefs.available < 15%`、`nodefs.inodesFree < 5%`。**PriorityClass 抢占**：所有 Pod **默认优先级为 0**；案例中先跑一个 request 5Gi 的 Pod，再创建一个 request 6Gi 且 `priorityClassName: high-priority`（value 100）的 Pod，两者都用 `nodeSelector: kubernetes.io/hostname: worker3`，结果**新 Pod 立即 Running，旧 Pod 被踢成 Pending**。`kubectl get priorityclass` 可见系统内置 `system-cluster-critical`（2000000000）和 `system-node-critical`（2000001000）。修法：降低一方或双方 request、放宽 nodeSelector 让负载可去别的节点、扩大节点、或把两者优先级设成一致。

110. ☆ 🟢 Pod 显示 ImagePullBackOff / ErrImagePull，笔记给出的最简处理流程是什么？
   - 要点：先检查**镜像路径是否正确**；路径确认无误后 `kubectl delete pod/<pod>` 删掉 Pod，由 **Deployment 自动重建**再拉一次。该错误属于 Preparation 阶段、K8s 侧的错误（拉镜像），也是 Deployment 卡住不完成发布的常见原因之一。

111. 🟡 Deployment 一直卡在发布新 ReplicaSet、`rollout status` 不结束，笔记列出的原因有哪些？如何观察？
   - 要点：六类原因：**配额不足（quota）**、**就绪探针失败（readiness probe）**、**镜像拉取错误**、**权限不足**、**LimitRange 限制**、**应用运行时配置错误**。观察方法：`kubectl rollout status deployment/<deploy>` 看进度；`kubectl get rs` 应看到新 RS 扩到 N、旧 RS 缩到 0，卡住时新 RS 副本数不增长；`kubectl describe deployment` 看状态；确认无法修复则 `kubectl rollout undo`。可把 Deployment 的 status 当作"发布是否卡住"的指标。

### 排障：网络、存储与控制面

112. ☆ 🟡 前端配置了后端 Pod 的 IP，一段时间后连不上了，为什么？如何用 Service 修复并验证？
   - 要点：RC / RS / Deployment 在扩缩容、滚动更新时会**销毁并新建 Pod，Pod IP 每次都变**，且 Pod IP 默认**不可从集群外访问**。Service 提供一个**虚拟 IP（VIP）**，它不绑定任何网卡，只负责把流量转到匹配 label 的 Pod；**kube-proxy** 通过查询 API server 维护 VIP → Pod 的映射；创建 Service 会同时创建 Endpoint。验证链路：`kubectl get pod -o wide` 拿 Pod IP，`kubectl exec -it pod/<ubuntu-pod> -- /bin/bash` 进入客户端 Pod，`curl <podIP>:80` 可通；删除后端 Pod 让它换 IP，再 `curl <老 podIP>` 失败，而 `curl <clusterIP>:80` 依旧可通。

113. ☆ 🟡 应用日志显示连不上集群内另一个服务的 3100 端口，DNS 和路由都正常，还要查什么？
   - 要点：查 **NetworkPolicy**。案例用 `kubectl get networkpolicies.projectcalico.org <name> -o yaml` 查看该 Pod 的策略，egress 只允许 TCP 8443 和 9093。**关键规则：NetworkPolicy 一旦含有 egress 规则，除明确允许的流量外全部阻断**，所以 3100 没在白名单里就是根因。修复：在 egress 的 `ports` 列表加上 3100，再看 `kubectl logs` 出现 `Successfully initiated log tailing using web-socket`，并确认 Pod RESTARTS 不再增加。

114. 🟢 Pod 在 `test` 命名空间，用 Service 名访问 `prod` 命名空间的服务失败，为什么？Headless Service 的 DNS 如何验证？
   - 要点：每个 Service 都有 DNS 名，但客户端 Pod 的 **DNS search list 默认只包含自己的命名空间和集群默认域**，跨命名空间**必须写全名**（`<svc>.<ns>.svc.cluster.local`），只写短名找不到。验证 Headless Service：进入客户端 Pod 装 `dnsutils` 后 `nslookup headlessservice`，返回的是**各 Pod IP 而非 Service IP**，再 `curl headlessservice.default.svc.cluster.local:80` 直连。

115. 🟡 Service Topology 的 `topologyKeys` 如何让流量优先走本节点 / 本可用区？有哪些约束？
   - 要点：默认 ClusterIP / NodePort 流量可被转发到**任意节点**上的后端。开启 Service Topology 特性门后，在 Service spec 写 `topologyKeys` 按顺序匹配节点 label：只写 `kubernetes.io/hostname` 则**只走本节点端点，没有就丢弃**；写 `zone` → `region` 表示优先同区、再同地域；末尾加 **`"*"`** 表示兜底到全集群，且 `*` 必须放最后。约束：**不能与 `externalTrafficPolicy=Local` 同用于一个 Service**；合法 key 仅 `kubernetes.io/hostname`、`topology.kubernetes.io/zone`、`topology.kubernetes.io/region`；最多 16 个 key。

116. 🟢 StatefulSet 的存储是怎么分配的？删除 StatefulSet 后数据卷会怎样？
   - 要点：`volumeClaimTemplates` 里的每个条目会给**每个 Pod 单独创建一个 PVC**（示例：`storageClassName: my-storage-class`、`ReadWriteOnce`、1Gi），不写 StorageClass 则用**默认 StorageClass**；Pod 被重新调度到别的节点时 `volumeMounts` 会重新挂回它自己的 PV。存储须由 PV 供应器按 StorageClass 动态供应或管理员预先创建。**删除或缩容 StatefulSet 不会删除对应的 PV / PVC**，这是为了数据安全，需要手动清理。

117. 🟢 用 kubeadm 手工搭集群，节点上要做哪些前置准备？worker 如何加入？
   - 要点：每台机器：安装并启动 docker；**关闭 SELinux**（`setenforce 0` + 改 `/etc/sysconfig/selinux`）；**关闭 swap**（`swapoff -a` 并从 `/etc/fstab` 删除）；写入 `/etc/sysctl.d/kubernetes.conf` 打开 `net.bridge.bridge-nf-call-iptables = 1` / `ip6tables = 1` 后 `sysctl --system`；装 kubeadm / kubelet / kubectl 并 `systemctl enable kubelet`。Master：`kubeadm init --apiserver-advertise-address=<master ip> --pod-network-cidr=192.168.0.0/16`，把 `/etc/kubernetes/admin.conf` 复制到 `~/.kube/config` 并改属主，再 `kubectl apply -f calico.yaml` 部署网络插件。Worker 加入：在 master 上 `kubeadm token create --print-join-command` 生成 join 命令。对比：Kops 用 **S3 bucket 存集群状态**（`KOPS_STATE_STORE`）、Route53 私有域做 DNS，`kops validate cluster` 刚建完时报 validation failed 属于**预期行为**，等一会再验。

### CI/CD 与 Pod（Pipelines & Pods）

118. 🟡 Tekton 是什么？它的 Pipeline / Task / Step / Resource 是怎样的层级关系？
   - 要点：Tekton 由 **CD Foundation（cd.foundation）**治理，Google / CloudBees / IBM / Pivotal / Red Hat 等贡献，**源自 Knative Build 子项目**。它通过 **CRD 定义新 Kind：`Pipeline`、`Task`**，能在**集群内构建容器镜像**并自动部署。层级：**Pipeline 由多个 Task 组成，Task 由多个 Step 组成**；输入 / 输出用 PipelineResource（如 git 仓库、image、cluster）。`tektoncd/catalog` 提供可复用 Task：git clone、mvn / bazel / s2i（python、ruby 等）、以及不用 Docker daemon 的 "docker build"（**buildah、kaniko、makisu**）。

119. 🔴 Blue/Green、Canary、Dark Launch 三种发布方式的差异是什么？在 K8s 上各靠什么实现？
   - 要点：**Blue/Green** 是 K8s / OpenShift 原生就能做的：Router 前面两套 Production，构建产物一路 DEV → QA → STAGING 到新的一套后，把 Router 整体切换，出问题切回。**Canary**：只放一部分流量到新版本，Istio 的关键差异是**流量百分比不依赖 Pod 数量**（原生 K8s 只能靠副本数比例做"粗糙金丝雀"），即所谓 Smart Canary。**Dark Launch**：新版本部署到生产但对用户不可见，通过 **Mirroring 把生产流量镜像一份**打到 dark 版本，只"**监控镜像**"不返回用户，验证通过后再切为 Active。这些能力属于 Service Mesh 提供的语言无关（polyglot）特性，与熔断、故障注入、遥测、加密授权同列。

120. 🟢 K8s 内置的 Kind 有哪些？CRD "自定义 Kind" 举几个生态例子。
   - 要点：开箱即用的 Kind 如 **ConfigMap、Deployment、Service**；通过 CRD 扩展出的自定义 Kind：**`VirtualService`（Istio）**、**Knative 的 Serverless Service**、**`Pipeline`（Tekton）**、**`Kafka`（Strimzi）**、**`Integration`（Camel-K）**。Dev 与 Ops 都通过同一个 **Kubernetes API** 操作这些对象，这是"Pipelines & Pods"演讲的核心：把交付物、流量策略、构建流程都表达成 K8s 对象。

121. 🟡 流水线交付到 K8s 的"部署单元"应该包含什么？已有的 docker-compose 项目如何迁移成 K8s 清单？
   - 要点：幻灯片给出的部署单元四要素：**镜像**（如 `quay.io/images/custservice:1.1.0`，带明确版本 tag）、**副本数**（Replicas: 2）、**Label**（`customerservice=prod,ci_build=1213`，把 CI 构建号打进 label 便于追溯）、**ConfigMap**（`cust_config`，配置与镜像分离）。Pod 本身是 1+ 容器共享 IP、共享临时存储、共享资源与生命周期；Deployment 描述期望状态（replicas、pod template、健康检查、resources、image）。迁移 compose：安装 **Kompose**，对 `docker-compose.yml`（含 `deploy.replicas`、ports、environment）执行 **`kompose convert`** 生成对应的 Deployment / Service 清单。

## 九、End to End K8s notes（Aman Pathak「30DaysOfKubernetes」合订，30 题）

> 293 页从架构、kubeadm、HA 控制面到 Helm / Helmfile、EKS / AKS / GKE 与 DevSecOps 流水线的全流程笔记。

### 集群架构与 kubeadm 搭建

122. ☆ 🟢 Kubernetes 控制平面有哪四个核心组件？工作节点上又有哪些？分别负责什么？
   - 要点：控制面四组件：**API Server** 是所有任务的入口，kubectl 命令先到它再分发；**etcd** 是键值数据库，保存整个集群状态（Pod IP、节点、网络配置），数据由 API Server 写入；**Controller Manager** 从 API Server 读取期望状态并决定该做什么；**Scheduler** 决定 Pod 落到哪个 Worker 节点。工作节点：**kubelet** 管理本节点 Pod、定期检查健康、失败时重建（新 Pod IP 可能变化）；**kube-proxy** 维护网络规则、负责负载均衡与路由；**容器运行时**（containerd / CRI-O 等）真正创建容器；Pod 是最小调度单元，笔记建议一 Pod 一容器。

123. ☆ 🟡 用 kubeadm 在 Ubuntu 上搭集群，`kubeadm init` 之前每个节点必须做哪些系统级准备？漏掉会怎样？
   - 要点：**关闭 swap**：`swapoff -a; sed -i '/swap/d' /etc/fstab`；加载内核模块 `overlay`、`br_netfilter`（写入 `/etc/modules-load.d/k8s.conf`）；sysctl 打开 `net.bridge.bridge-nf-call-iptables=1`、`net.bridge.bridge-nf-call-ip6tables=1`、`net.ipv4.ip_forward=1` 后 `sysctl --system`；安装 `kubelet kubeadm kubectl kubernetes-cni`；安装 docker.io 后生成 containerd 默认配置并把 **`SystemdCgroup = true`**（`containerd config default > /etc/containerd/config.toml` + sed）；`systemctl enable kubelet` 保证重启后自动加入。笔记还提到 AWS 上 Master 需 **2 CPU（t2.medium）**，安全组放行流量，HA 场景先 `ufw disable`。

124. 🟡 `kubeadm init` 成功后，`kubectl get po -n kube-system` 里有两个 Pod 一直不 Ready、节点 NotReady，原因和处理步骤是什么？
   - 要点：原因是**尚未安装网络插件（CNI）**。步骤：先 `mkdir -p $HOME/.kube && cp /etc/kubernetes/admin.conf $HOME/.kube/config && chown` 让普通用户能管集群；用 `kubectl get --raw='/readyz?verbose'` 查组件健康、`kubectl cluster-info` 查端点；`kubectl apply -f .../calico/v3.25.0/manifests/calico.yaml` 安装 Calico，2–3 分钟后两个 Pod 转 Ready；再在 Worker 执行 `kubeadm join <master>:6443 --token ... --discovery-token-ca-cert-hash sha256:...`（笔记强调把 init 输出的 join 命令记下来）。`kubeadm config images pull` 可预拉 kube-apiserver 等镜像。

125. 🔴 如何用 HAProxy 搭一个双 Master 的高可用控制面？kubeadm 的关键参数是什么？
   - 要点：5 台机器：1 HAProxy + 2 Master(t2.medium) + 2 Worker。HAProxy `haproxy.cfg`：`frontend` **bind <haproxy私网IP>:6443 mode tcp**，`backend` **mode tcp / option tcp-check / balance roundrobin**，每个 master 一行 `server kmaster1 <ip>:6443 check fall 3 rise 2`；启动后 backend 显示 DOWN 是正常的（控制面尚未起）。所有节点 `/etc/hosts` 写入五台主机名。Master1：`kubeadm init --control-plane-endpoint="<haproxy-ip>:6443" --upload-certs --apiserver-advertise-address=<master1-ip>`；Master2 用输出里带 **`--control-plane --certificate-key`** 的 join 命令，并**额外加 `--apiserver-advertise-address=<master2-ip>`**；Worker 用普通 join。之后在任一 Master 装 Calico，节点才 Ready。笔记把这称为 "multi-cluster"，实际是多控制面高可用。

126. 🟢 kubeconfig 文件由哪几部分组成？如何切换默认命名空间？
   - 要点：`kind: Config`，三段：**clusters**（`server` 即 API Server 地址 + `certificate-authority-data`）、**users**（`client-certificate-data` / `client-key-data`）、**contexts**（把 cluster + user + namespace 组合）；**`current-context`** 决定命令默认打到哪个集群。默认路径 `~/.kube/config`，也可用 `KUBECONFIG` 环境变量。切换默认命名空间：`kubectl config set-context $(kubectl config current-context) --namespace <ns>`，用 `kubectl config view | grep namespace` 确认。kubeadm 集群的管理员配置来自 `/etc/kubernetes/admin.conf`。

### Pod、标签与控制器

127. ☆ 🟡 标签选择器有哪两类？ReplicationController 和 ReplicaSet 在选择器上的差异是什么？
   - 要点：**等值型**（`=`、`!=`，如 `kubectl get pods -l env=testing`、`-l department!=DevOps`）与**集合型**（`in`、`notin`、`exists`，如 `-l 'env in (testing, development)'`、`-l 'Location notin (India, US)'`），多个选择器逗号分隔。可事后 `kubectl label pods <pod> Location=India` 命令式补标签，`kubectl get pods --show-labels` 查看，`kubectl delete pod -l Location!=China` 按标签批量删。**RC 只支持等值型**（`selector: {Location: India}`），**RS 同时支持集合型**（`selector.matchExpressions: - {key: Location, operator: In, values: [India, US, Russia]}`）。扩缩：`kubectl scale --replicas=5 rc -l Location=India` / `kubectl scale --replicas=5 rs myrs`。

128. 🟢 一个带 `nodeSelector: {hardware: t2-medium}` 的 Pod 一直 Pending，怎么排查和修复？
   - 要点：nodeSelector 要求节点必须有**完全匹配的标签**；没有任何节点带该标签时 Pod 就停在 **Pending**。用 `kubectl get nodes --show-labels` 确认，然后 `kubectl label nodes <node> hardware=t2-medium`，**标签一加上 Pod 立即进入 Running**。同样的机制用于把 Nginx 固定到 node1（`mynode=node1`）、Apache 固定到 node2。

129. ☆ 🟡 Deployment 相比 ReplicaSet 多了什么？修改 Pod 模板后底层发生了什么？如何回滚？
   - 要点：RC / RS **不支持更新与回滚**，Deployment 支持声明式更新、回滚、暂停/恢复、清理旧 RS。修改 `template`（如镜像 ubuntu → centos）并 apply 后，**创建新的 RS，旧 RS 保留且 desired/current 为 0**，用于回滚；`kubectl get rs` 能看到两条。回滚：`kubectl rollout undo deployment <name>`，desired 会切回旧 RS。**坑**：用 `kubectl scale --replicas=5` 扩到 5 后，再 apply 写着 `replicas: 3` 的文件会被拉回 3。Deployment 不直接管 Pod，中间总有一层 RS。

### 网络：Service、CNI、Ingress、NetworkPolicy

130. ☆ 🟢 Service 的四种类型分别怎么用？`port`、`targetPort`、`nodePort` 三者区别？
   - 要点：**ClusterIP** 仅集群内可达；**NodePort** 在每个节点 IP 上开一个静态端口对外暴露（如 `nodePort: 32000`，用 `<节点公网IP>:32000` 访问）；**LoadBalancer** 通过云厂商 LB 暴露，EKS/AKS/GKE 上 `EXTERNAL-IP` 列会出现 LB DNS 或公网 IP；**ExternalName** 没有 selector，只是把服务映射到一个 DNS CNAME（`externalName: k8.learning.com`）。`port` 是 Service 监听的端口，`targetPort` 是 Pod 容器监听的端口——例如 React 在 3000 监听，Service 设 `port: 80, targetPort: 3000`。同一 Pod 内容器通过 **localhost** 互访（`curl localhost:80`）。minikube 用 `minikube service <svc>` 拿访问 URL。

131. 🔴 什么是 CNI？Calico 相比 Flannel / Weave / Cilium / kube-router 的定位如何？没装 CNI 会有什么现象？
   - 要点：CNI（Container Network Interface）决定容器 / Pod 如何接入网络。笔记对比：**Flannel** 简单的三层方案，适合中小集群但网络策略能力弱；**Weave** 提供安全、可扩展网络和策略，功能不如 Calico 丰富；**Cilium** 安全与可观测性最强，适合大型复杂、安全优先的集群；**kube-router** 轻量，带负载均衡和策略，适合中小集群。**Calico** 优势：基于标签/端口的细粒度网络策略、大规模可扩展、跨集群互联、**BGP 路由**便于与机房/公有云集成、流量加密、每 Pod 唯一 IP（IPAM）。未装 CNI：节点 NotReady、kube-system 两个 Pod 不 Ready；minikube 默认是 noop 插件，做 NetworkPolicy 演示要 `minikube start --network-plugin=cni` 再 `cilium install`。

132. ☆ 🟡 既然有 LoadBalancer Service，为什么还需要 Ingress？写一个同时做路径路由和主机路由的 Ingress 需要哪些字段？
   - 要点：LB 只按**端口**分流，做不了 URL 级别的路由；Ingress 暴露 HTTP/HTTPS，支持 **path-based**（`example.com/app1`）与 **host-based**（`demo.example.com`）路由、负载均衡和 **SSL 终止**。必须先部署 Ingress Controller（minikube：`minikube addons enable ingress`，`kubectl get pods -n ingress-nginx` 验证）。清单：`apiVersion: networking.k8s.io/v1`，`spec.rules[].host`，`http.paths[]` 每项含 `path`、**`pathType: Prefix`**、`backend.service.name` 与 `port.number`；示例注解 `nginx.ingress.kubernetes.io/rewrite-target: /$1`。同一 Ingress 内可为 `example.devops.in` 配 `/`、`/menu`、`/reviews` 三个后端，再加一条 `host: example2.devops.in` 做主机路由。本地测试需把 Ingress 地址（如 192.168.49.2）写进 `/etc/hosts`，否则 curl 通而浏览器不通。

133. ☆ 🔴 默认情况下跨命名空间 Pod 能否互访？用 NetworkPolicy 实现"namespace-b 的 QA Pod 只允许 namespace-a 访问"要写什么？
   - 要点：默认**任意 Pod 可访问任意命名空间的 Pod**（笔记用 `kubectl -n namespace-c exec <pod> -- curl <b的PodIP>` 验证可通）。NetworkPolicy 需要支持策略的 CNI（Calico / Cilium）。先用 deny-all 隔离：`podSelector: {}` + `policyTypes: [Ingress, Egress]`，放在 `namespace: namespace-b`，此后 a、c 都访问不到 b；删除策略后恢复。精确放行：先 **给命名空间打标签** `kubectl label namespaces namespace-a ns=namespacea`（namespaceSelector 靠标签匹配），再给目标 Pod 打 `environment=QA`；策略 `podSelector.matchLabels: {environment: QA}`，`policyTypes: [Ingress]`，`ingress[].from[].namespaceSelector.matchLabels: {ns: namespacea}`。结果：a → b 通，c → b 不通。用途：前后端隔离、微服务最小通信、合规、多租户、测试环境隔离生产。

### 存储与健康检查

134. 🟢 emptyDir 和 hostPath 的区别？数据分别在什么时候丢失？
   - 要点：**emptyDir** 随 Pod 创建、随 Pod 删除，初始为空；同一 Pod 内多个容器共享（各自 `mountPath` 可不同，如 `/tmp/container1` 与 `/tmp/container2`），**容器崩溃重建数据仍在，Pod 删除则永久丢失**，新 Pod 的卷是空的。**hostPath** 把节点目录（`hostPath.path: /tmp/data`）映射进容器，宿主机改动会反映到 Pod，Pod 写入宿主机也能看到，本质是把数据放在节点上。

135. ☆ 🟡 PV / PVC 的工作流程是什么？以 AWS EBS 为后端时有哪些限制？
   - 要点：PV 是集群级的可用存储，数据放在 EBS / Azure Disk 等中心位置，Pod 删除后数据仍可被其他节点的 Pod 使用；PVC 是对 PV 的申领，创建后 K8s 找到合适的 PV **绑定（Bound）**，Pod 通过 `volumes[].persistentVolumeClaim.claimName` 挂载。PV 字段：`capacity.storage: 1Gi`、`accessModes: [ReadWriteOnce]`、`persistentVolumeReclaimPolicy: Recycle`、`awsElasticBlockStore: {volumeID, fsType: ext4}`；PVC 用 `resources.requests.storage: 1Gi` 匹配。**EBS 限制**：节点必须是 EC2；EBS 与 EC2 必须在**同一 Region 且同一 AZ**；一个 EBS **只能挂到一台 EC2**。演示：删 Pod 后 Deployment 重建的新 Pod 在 `/tmp/persistent` 仍能看到旧文件。

136. ☆ 🟡 Kubernetes 默认会做应用健康检查吗？写一个 exec 型 livenessProbe 并解释各参数。
   - 要点：**默认不做**，必须在清单里声明。示例：容器 `touch /tmp/healthy; sleep 1000`，探针 `livenessProbe.exec.command: [cat, /tmp/healthy]`，**返回 0 表示健康，非 0 则重建容器**并继续周期检查。参数：`initialDelaySeconds: 5`（首次探测前等待）、`periodSeconds: 5`（探测周期）、`timeoutSeconds: 30`。验证：删掉 `/tmp/healthy` 后 `kubectl describe pod` 末尾 Events 会显示探测失败、容器重启；describe 的 Containers 段会多出 Liveness 行。笔记还提到探针失败的 Pod 会被从负载均衡里摘掉。

### 配置、任务与 Pod 生命周期

137. 🟢 ConfigMap / Secret 有哪几种创建方式？注入 Pod 有哪几种方式？
   - 要点：创建：`--from-literal`（直接给 key=value）、`--from-file`（整个文件当一个 key）、`--from-env-file`（按行解析 key=value）、`--from-file=<目录>`（目录下多个文件一次性导入）；用 `--from-file ... -o yaml` 生成清单再改成声明式。注入：① 单个 key 到环境变量 `env[].valueFrom.configMapKeyRef: {name, key}`（Secret 用 `secretKeyRef`）；② 整个 CM 全部变环境变量 `envFrom[].configMapRef.name`；③ 挂成文件 `volumes[].configMap.name` + `volumeMounts.mountPath` (`readOnly: true`)；④ 只挑部分 key 并改文件名 `configMap.items[]: {key: Subject3, path: topic3}`（Secret 用 `secret.secretName` + `items`）。修改 CM 后已注入的 Pod 能看到更新。Secret 用于数据库账号、API Key 等敏感数据，**上限 1MB**，笔记称其存于 tmpfs 且仅 Pod 可读、`kubectl get` 显示为编码后的值。

138. 🟢 Job 和 CronJob 的区别？`parallelism`、`activeDeadlineSeconds`、`restartPolicy` 各起什么作用？
   - 要点：Job 用于一次性任务（数据库备份、批处理、日志轮转），**完成后 Pod 结束**；`apiVersion: batch/v1`，模板里必须 `restartPolicy: Never`。**`parallelism: 3`** 同时起 3 个 Pod；**`activeDeadlineSeconds: 10`** 为 Job 设置总时限，到期后 Pod 被终止（笔记示例：命令 sleep 30，约 40 秒后终止）。CronJob 用 `schedule: "* * * * *"` 每分钟触发一次，Pod 模板放在 `jobTemplate.spec.template` 下。

139. 🟡 InitContainer 的执行语义是什么？如何把 init 容器生成的文件交给主容器？
   - 要点：`initContainers` 在应用容器之前运行，**必须成功完成**，失败会被 K8s **反复重启直到成功**，主容器才启动。用途：预装依赖、把 git 仓库克隆到卷、动态生成配置、数据库初始化。传递数据：定义一个 `emptyDir` 卷，init 容器挂到 `/tmp/xchange` 写文件，主容器挂到 `/tmp/data` 读取（同一卷，不同挂载点）。Pod 的 **Initialized** condition 表示所有 init 容器已成功。

140. 🟢 列出 Pod 的主要阶段和 `kubectl describe` 里的四个 Conditions，它们分别代表什么？
   - 要点：**Pending**：已创建但还在等调度和 CPU / 内存 / 存储资源；**Running**：已调度到节点、容器在执行；**Succeeded**：任务完成后终止；**Failed**：因配置等问题未能创建，需检查清单；**CrashLoopBackOff**：容器反复崩溃重启；**Unknown**：控制面与节点失联；**Terminating**：删除中，删除后同一个 Pod 不能再启动。Conditions：**PodScheduled**（已分配节点）、**Initialized**（init 容器全部成功）、**ContainersReady**（容器就绪）、**Ready**（Pod 可用）；刚创建时 describe 可能只有 PodScheduled=True，几秒后全部 True。

### 命名空间、资源配额与自动扩缩

141. 🟢 集群预置的三个命名空间是什么？哪些对象不受命名空间约束？
   - 要点：**default**（不指定 `-n` 时对象都建在这里）、**kube-system**（kube-controller-manager、kube-scheduler、kube-dns 等系统组件，**不要在里面放业务对象**）、**kube-public**（集群成员都可见的非敏感信息）。**Node 和 PersistentVolume 不属于任何命名空间**，对所有命名空间可见。用途：多项目隔离、多环境组织、按命名空间做 RBAC 权限。其他命名空间的 Pod 必须带 `-n <ns>` 才能查/删，否则报 not found。

142. ☆ 🔴 说明 requests / limits 的三条默认规则，ResourceQuota 与 LimitRange 各自约束什么？举例说明配额不足时的表现。
   - 要点：默认 Pod **没有 CPU / 内存限制**；CPU 以核为单位（`200m`、`0.5`），内存以字节（`32Mi`）。规则：① requests 与 limits 都给 → 按给定值；② **只给 requests 不给 limits → 使用命名空间默认 limit**（来自 LimitRange）；③ **只给 limits 不给 requests → requests = limits**；requests 大于 limits 则拒绝创建。**ResourceQuota** 作用于命名空间总量：`spec.hard: {limits.cpu: "200m", requests.cpu: "150m", limits.memory: "38Mi", requests.memory: "12Mi"}`，并要求命名空间内每个容器都声明 limit。**LimitRange** 给容器默认值：`limits[].type: Container`，`default.cpu: 1`（默认 limit）、`defaultRequest.cpu: 0.5`（默认 request）。示例：配额 requests.cpu 150m 时，`replicas: 4`、每 Pod `requests.cpu: 50m` 的 Deployment **只能创建部分 Pod，其余因超配额创建失败**，错误在 RS 事件里。调度器只把 Pod 放到有足够 CPU 的节点上。

143. ☆ 🟡 HPA 生效有哪些前提？命令式和声明式各怎么写？缩容为什么要等几分钟？
   - 要点：前提①：安装 **metrics-server**（下载 components.yaml，在 spec 下加 `hostNetwork: true`，args 加 `--kubelet-insecure-tls`，`kubectl get pods -n kube-system` 看到 metrics-server 运行）；前提②：目标 Deployment 的容器必须声明 `resources.requests.cpu`（示例 requests 200m / limits 500m）；只能作用于 Deployment / RS / RC 这类可伸缩对象。命令式：`kubectl autoscale deployment <name> --cpu-percent=20 --min=1 --max=5`。声明式：`apiVersion: autoscaling/v2`，`scaleTargetRef: {apiVersion: apps/v1, kind: Deployment, name}`，`minReplicas: 1`、`maxReplicas: 5`，`metrics[]: type: Resource, resource.name: cpu, target.type: Utilization, averageUtilization: 20`。压测：进容器跑 `while true; do apt update; done`，`watch kubectl get all` 看副本涨到 5；停止后约 **5 分钟**才缩回 1，这是 **cooldown 期**，避免负载反复时抖动。HPA 横向加 Pod 数，VPA 纵向加配置（4G→8G），笔记认为 VPA 成本效率差。

### StatefulSet 与 DaemonSet

144. ☆ 🔴 StatefulSet 与 Deployment 的差异有哪些？headless Service、volumeClaimTemplates、缩容后的 PVC、两种删除方式分别是什么行为？
   - 要点：差异：**固定有序名称** `web-0`、`web-1`；**顺序创建、逆序删除**（Deployment 一次并发创建）；每 Pod 通过 `volumeClaimTemplates` 得到**自己的 PVC**，重建后数据仍在；配合 **headless Service**（`clusterIP: None`，StatefulSet 里 `serviceName: "nginx"`）为每个 Pod 提供稳定 DNS，`nslookup web-0.nginx` 可解析（IP 可能变、名字不变）。缩容：`kubectl scale sts web --replicas=5` 后 PVC 增到 5；`kubectl patch sts web -p '{"spec":{"replicas":3}}'` 缩到 3 后 **5 个 PVC 全部保留**——StatefulSet 假设你是误删。更新：`kubectl patch statefulset web -p '{"spec":{"updateStrategy":{"type":"RollingUpdate"}}}'`，再用 `--type=json` patch `/spec/template/spec/containers/0/image` 换镜像。删除：**非级联** `kubectl delete statefulset web --cascade=orphan` 只删控制器、Pod 留下且不再被重建；**级联** `kubectl delete statefulset web` 连 Pod 一起删。

145. 🟢 DaemonSet 解决什么问题？清单和 Deployment 有什么不同？
   - 要点：保证**每个（或部分）节点各运行一份 Pod**：新节点加入自动补 Pod，节点移除时 Pod 被回收，删 DaemonSet 会清理其 Pod。用途：日志 / 监控采集（Prometheus、Beats）、安全代理（IDS）、节点级网络策略、系统补丁、存储插件。清单 `kind: DaemonSet`，**没有 `replicas` 字段**，只有 `selector` + `template`。笔记演示：两 Worker 上各一个 nginx Pod，`kubeadm join` 第三个 Worker 后，无需任何操作第三份 Pod 自动 Running。

### Operator 与 CRD

146. 🟡 Operator 由哪三部分组成？举例说明 Operator 能自动化什么，CRD 清单里有哪些关键字段？
   - 要点：三步：**CRD**（定义新资源类型）→ **Custom Controller**（watch 并 reconcile 自定义资源，让实际状态趋向期望状态，做自愈；常用 Go + client-go，示例用 `cache.NewSharedInformer` 注册 Add/Update/Delete 处理函数）→ **Custom Resource**（实例，可按命名空间部署）；没有控制器的 CRD 没有意义。示例：Prometheus Operator 用 CR 声明告警规则、ServiceMonitor；MongoDB Operator 改 CR 副本数自动扩缩；Vault Operator 强制安全策略；CockroachDB Operator 逐节点滚动升级实现零停机；Kafka Operator 自动建 topic、重分配分区。CRD 字段：`apiVersion: apiextensions.k8s.io/v1`，`spec.group`，`names.{kind, listKind, plural, singular}`，`scope: Namespaced`，`versions[]: {name: v1, served: true, storage: true}`，`additionalPrinterColumns` 让 `kubectl get` 显示 `.spec.replicas`。做好的 Operator 可发布到 operatorhub.io。

### Helm 与 Helmfile

147. ☆ 🟢 列出 Helm 的常用命令：建 chart、安装、升级、查看版本、回滚、干跑、渲染、校验、测试、卸载。
   - 要点：`helm create helloworld`（生成 Chart.yaml / values.yaml / templates）；`helm install <release> <chart目录>`（release 名在前）；改 `values.yaml`（如 `service.type` ClusterIP → NodePort、replica 1 → 2）后 `helm upgrade <release> <chart>`；`helm list -a` 看 revision；`helm rollback <release> 1` 回到第 1 版；`helm install <release> --debug --dry-run <chart>` 干跑；`helm template <chart>` 渲染 YAML；`helm lint <chart>` 校验 chart；`helm test <release>` 跑 `templates/tests/test-connection.yaml`；`helm uninstall <release>`；仓库 `helm repo add/list/remove`。价值：多份 YAML 打包一条命令部署、按环境改 values、随时回滚。

148. 🟡 Helmfile 相比直接 `helm install` 解决什么问题？如何用它一次部署多个 chart、从 Git 仓库取 chart、以及卸载？
   - 要点：Helm 命令是命令式，**Helmfile 用一个 YAML 声明式管理多个 release**。文件结构：`releases[]: {name, chart: ./path, installed: true}`，执行 **`helmfile sync`**；把 `installed` 改为 `false` 再 sync 即卸载（Pod 进入 Terminating）。多 chart 只需在 `releases` 下追加条目。从 Git 取 chart：装插件 `helm plugin install https://github.com/aslafy-z/helm-git --version 0.15.1`，在 `repositories[]` 写 `url: git+https://github.com/<org>/<repo>@<子目录>?ref=master&sparse=0`，无需手动 clone。演示中部署 Flask chart 时改了 `values.yaml` 的镜像、service type、容器端口 9001，并注释掉了 deployment.yaml 里默认的 liveness / readiness 探针。

### 托管 Kubernetes（EKS / AKS / GKE）

149. 🟡 在 AWS 上从零创建 EKS 需要准备哪些网络与 IAM 资源？为什么创建后第一个 Pod 是 Pending？三家托管服务的计费与差异要点？
   - 要点：网络：VPC + **至少两个公有子网**（高可用）+ Internet Gateway + 关联到两个子网的公有路由表。IAM：**集群角色**（可信实体 EKS，用例 EKS-Cluster）；**节点角色**（可信实体 EC2）附三策略 **AmazonEKSWorkerNodePolicy、AmazonEKS_CNI_Policy、AmazonEC2ContainerRegistryReadOnly**。连接：`aws eks update-kubeconfig --region us-east-1 --name <cluster>`（旧 CLI 报错时把 kubeconfig 里 `alpha` 改 `beta`）。**Pod Pending 是因为还没有 Node Group**，添加节点组（t3.medium，K8s 至少 2 CPU）后即 Running；`type: LoadBalancer` 的 Service 会自动创建 AWS LB，`EXTERNAL-IP` 为 LB DNS。计费：EKS **$0.10/集群/小时**，节点按 EC2 / Fargate 另计；AKS 有免费层（不能自动扩缩），Standard 层 $0.10/小时，Premium $0.60/小时；AKS 默认 `agentpool` 是系统节点池，业务要另加节点池，网络示例选 kubenet + Calico 策略，用 `az login` 后连接；GKE 由 Google 自研，版本最多、控制面和节点自动升级、节点自动修复、Container-Optimized OS，连接需 `gcloud components install gke-gcloud-auth-plugin`，可在 default-pool 把节点数 3 改 1 缩容而应用不中断。

### DevSecOps 端到端流水线

150. 🔴 描述笔记中 Netflix-Clone 项目的 Jenkins 流水线各阶段，安全扫描和部署到 K8s 分别怎么接入？
   - 要点：四台机器：Jenkins（t2.large，35GB，装 Docker、SonarQube 容器、Trivy、kubectl）、监控（t2.medium，Prometheus + Node Exporter + Grafana）、K8s Master、K8s Worker。Jenkins 侧：`usermod -aG docker jenkins`，SonarQube 用 `docker run -d --name sonar -p 9000:9000 sonarqube:lts-community`，在 Sonar 生成 token 存为 Jenkins Secret text `sonar-token`，并在 Sonar 配置指向 Jenkins 的 **Webhook**（Quality Gate 回调）。流水线：`tools {jdk, nodejs}`，`SCANNER_HOME=tool 'sonar-server'`；stages：`cleanWs()` → git checkout → `withSonarQubeEnv('sonar-server') { sonar-scanner -Dsonar.projectKey=Netflix }` → `waitForQualityGate abortPipeline: false, credentialsId: 'sonar-token'` → `npm install` → **OWASP** `dependencyCheck additionalArguments: '--scan ./ --disableYarnAudit --disableNodeAudit'` + `dependencyCheckPublisher` → **`trivy fs . > trivyfs.txt`** → docker build/push（TMDB API key 作为构建参数）→ 对推送后的镜像做 Trivy 镜像扫描 → **`withKubeConfig(credentialsId: 'k8s')`** 内 `kubectl apply -f deployment.yml / service.yml`（把 Master 的 `~/.kube/config` 作为 Secret file 凭据上传，需装 Kubernetes / Kubernetes CLI / Credentials 等插件）。`post { always { emailext attachLog: true, attachmentsPattern: 'trivyfs.txt,trivyimage.txt' } }` 通过 Gmail（smtp.gmail.com:465 + 应用密码）发送成功/失败邮件。应用通过 Worker 公网 IP:32000（NodePort）访问。

151. 🟡 在裸机上用 systemd 部署 Prometheus + Node Exporter + Grafana 的关键步骤是什么？加了新 target 后如何不重启生效？
   - 要点：建专用用户 `useradd --system --no-create-home --shell /bin/false prometheus`；二进制放 `/usr/local/bin`（prometheus、promtool），配置放 `/etc/prometheus`，数据目录 `/data`，`chown -R prometheus:prometheus`。systemd unit：`Type=simple`、`Restart=on-failure`、`ExecStart=/usr/local/bin/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/data --web.listen-address=0.0.0.0:9090 --web.enable-lifecycle`；Node Exporter 同样方式，端口 **9100**，`--collector.logind`。在 `prometheus.yml` 加 `- job_name: "node_exporter"` / `static_configs.targets: ["localhost:9100"]`，Jenkins 装 Prometheus metrics 插件后加 `job_name: "jenkins"`（`<ip>:8080`），K8s Master/Worker 也各装 node_exporter 加 job。改完先 **`promtool check config /etc/prometheus/prometheus.yml`** 校验，再 **`curl -X POST http://localhost:9090/-/reload`** 热加载（依赖 `--web.enable-lifecycle`），到 `:9090/targets` 确认 UP。Grafana 端口 3000，添加 Prometheus 数据源（`<ip>:9090`），导入社区仪表盘 **1860**（Node Exporter）和 **9964**（Jenkins）。

## 十、kubectl 速查（两份社区 cheat sheet，8 题）

> 来源是两份广泛流传的速查表（一份来自 Linux Academy，一份来自 DevOps 社群）。适合作为 `quiz` 速答轮素材。

152. ☆ 🟢 不想手写 YAML，怎样让 kubectl 生成 Pod / Deployment / Service 的清单骨架？
   - 要点：统一套路 **`--dry-run=client -o yaml > file.yaml`**：`kubectl run <pod> --image <img> --dry-run=client -o yaml`、`kubectl create deployment <d> --image <img> --dry-run=client -o yaml`、`kubectl create service <type> <name> --tcp=<port:targetPort> --dry-run=client -o yaml`；`kubectl create deploy <d> --image=nginx --dry-run -o yaml` 亦可（旧写法）。
153. 🟢 怎样一条命令起 Pod 并暴露成 Service？怎样起一个用完即删的调试 Pod？
   - 要点：`kubectl run <pod> --image <img> --port <port> --expose`；调试：`kubectl run <pod> --image=curlimages/curl --rm -it --restart=Never -- curl <目标>`（或 `--image=busybox --rm -it --restart=Never -- sh`）。
154. 🟢 ConfigMap / Secret 从命令行创建有哪三种输入方式？
   - 要点：`--from-literal=<key>=<value>`（可多次）、`--from-file=<文件>`、`--from-env-file=<文件>`；Secret 用 `kubectl create secret generic <name> …` 同样三种。
155. ☆ 🟢 Deployment 的发布控制命令有哪些？
   - 要点：`kubectl set image deployment <d> <容器>=<新镜像>`；`kubectl scale deployment <d> --replicas <n>`；`kubectl rollout restart deployment <d>`；`kubectl rollout history deployment <d>`（`--revision=<n>` 看某版）；`kubectl rollout undo deployment <d>`（`--to-revision <n>` 回到指定版本）；`kubectl rollout status deployment <d>` 看进度。
156. 🟢 节点维护三步与资源用量查看命令？
   - 要点：`kubectl cordon <node>` → `kubectl drain <node>`（通常加 `--ignore-daemonsets`）→ 维护后 `kubectl uncordon <node>`；用量：`kubectl top node [<node>]`、`kubectl top pod [<pod>]`（需 metrics-server）。
157. 🟢 标签与字段选择器怎么用？
   - 要点：查看 `kubectl get <res> --show-labels`；打标签 `kubectl label <res> <name> key=value`；删标签 `kubectl label <res> <name> key-`；筛选 `kubectl get <res> -l key=value`；按字段筛 `kubectl get pods --field-selector status.phase=Running`；节点 `kubectl get node --selector=<label>`。
158. 🟢 看日志和「看 API 原始数据」的常用姿势？
   - 要点：`kubectl logs <pod>`、`--since=1h`、`--tail=20`、`-f -c <容器>`、`kubectl logs deployment/<d> -f`、`kubectl logs <pod> > pod.log`；`kubectl get --raw /apis/metrics.k8s.io/`（直接打 API）；`kubectl explain deploy.spec`（字段文档）；`kubectl get events -w`（跟踪事件）；`kubectl get all --all-namespaces`。
159. 🟡 Job / CronJob 有哪些「一把梭」命令？怎样把节点的 ExternalIP 用 jsonpath 取出来？
   - 要点：`kubectl create job <j> --image=<img>`；**从 CronJob 手动触发一次**：`kubectl create job <j> --from=cronjob/<cj>`；`kubectl create cronjob <cj> --image=<img> --schedule='<cron>' -- <cmd>`；`kubectl create svc nodeport <s> --tcp=8080:80`；jsonpath：`kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="ExternalIP")].address}'`。

---

## 难度图例

🟢 初级（能背出定义 / 命令） · 🟡 中级（能解释为什么、会写配置与排障） · 🔴 高级（能做架构权衡、讲清风险与代价）

## 与 modules 的映射

| 本文件分组 | 对应 modules 模块 | 备注 |
|---|---|---|
| 一、CKS 实操场景 | `cloud-security` Q15（总纲）、Q10–Q12、Q14；`kubernetes` Q15 / Q25 / Q26 / Q27 / Q32 | 动手加固：NetworkPolicy、AppArmor / seccomp、RBAC、审计、kube-bench、Falco、准入 webhook |
| 二、1.24 官方安全审计 | `cloud-security` Q16（总纲）、Q11；`kubernetes` Q25 / Q43 / Q49 | 威胁模型、apiserver / kubelet 信任链、RBAC 无 Deny、NetworkPolicy 局限 |
| 三、部署与安全模式（2018） | `kubernetes` Q10 / Q14 / Q29 / Q32；`cloud-security` Q1 / Q2 / Q11；`cicd-iac`；`observability` | 部署模式对比、共享责任、认证 / 授权 / 准入、审计、配额 |
| 四、Istio Ambient Mesh | `service-mesh` Q14 / Q15 / Q18 / Q24 | ztunnel / waypoint / HBONE / Gateway API 角色模型 |
| 五、Istio + Aeraki 落地 | `service-mesh` Q25（总纲）、Q21 / Q22 / Q10 | MetaProtocol、外部服务发现、多控制面合并、全链路染色 |
| 六、阿里超大规模实践 | `kubernetes` Q51（总纲）、Q38 / Q40 / Q41 | List & Watch / Bookmark / 缓存索引 / 面向终态 / OpenKruise / 负载感知调度 |
| 七、DRBD / LINSTOR / Piraeus | `kubernetes` Q52（总纲）、Q16 / Q17；`middleware`（数据库高可用） | 内核态复制、超融合、数据本地性、与 Ceph 的取舍 |
| 八、学习笔记与排障手册 | `kubernetes` Q3 / Q4 / Q5 / Q7 / Q8 / Q9 / Q20 / Q23 / Q29 / Q30；`cicd-iac`（Tekton、发布策略） | 三阶段排障法、Pending / CrashLoopBackOff / 抢占驱逐 / NetworkPolicy 阻断 |
| 九、End to End 笔记 | `kubernetes` 全模块；`cicd-iac`（Helm / Helmfile / Jenkins）；`observability`（Prometheus 部署）；`cloud-security`（EKS IAM、扫描） | 从 kubeadm 到托管集群到 DevSecOps 流水线 |
| 十、kubectl 速查 | `kubernetes` Q23；`quiz kubernetes` 速答轮 | 命令速答 |
