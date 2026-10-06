# 云 / 安全 / 合规面试题（17 题）

> 模板见 [../../docs/STANDARD.md](../../docs/STANDARD.md)。
> **AWS 托管服务选型补充**：[collections/aws-managed-services-only.md](../../collections/aws-managed-services-only.md)（130 题）——IRSA / Pod Identity / Secrets Manager（Pod 自己读 vs External Secrets / CSI）、26 服务目标架构的 chosen/rejected 选型表、MCP/Agent 在 AWS 上的控制缺口。

---

### Q1. 主流云（AWS / 阿里云 / 腾讯云）核心服务对应关系？
- **难度**：🟡 中级
- **关键词**：云服务商, 计算, 对象存储, VPC, 托管K8s
- **概念速记**：各家能力对等：EC2/ECS/CVM、S3/OSS/COS、EKS/ACK/TKE。
- **参考答案**：计算（EC2/ECS/CVM）、对象存储（S3/OSS/COS）、块存储（EBS/云盘）、负载均衡（ALB/CLB）、VPC/子网、数据库托管（RDS）、K8s 托管（EKS/ACK/TKE）、函数（Lambda/函数计算）。关注配额、跨 AZ、计费、IAM。
- **易错点**：把云厂商当黑盒，不关注配额与计费模型。
- **延伸**：Q2（IAM）、Q7（FinOps）

### Q2. IAM / 最小权限原则在云上怎么落地？
- **难度**：🔴 高级
- **关键词**：IAM, 最小权限, STS, 凭证轮换
- **概念速记**：避免长期 AK/SK 硬编码，用临时凭证与角色。
- **参考答案**：按角色/服务建子账号与角色，避免 AK/SK 硬编码（用 STS 临时凭证/实例角色），最小权限策略，定期审计（Access Analyzer），密钥轮转，存 Vault/Secrets Manager。防凭证泄露是头号风险。
- **易错点**：把 AK/SK 写进代码仓库或镜像。
- **延伸**：kubernetes Q25（RBAC）；observability Q12（审计）

### Q3. VPC / 子网 / 安全组 / NACL 网络隔离模型？
- **难度**：🟡 中级
- **关键词**：VPC, 安全组, NACL, 分层隔离
- **概念速记**：安全组有状态（实例级）；NACL 无状态（子网级）。
- **参考答案**：VPC 私有网络；子网分公有/私有（绑 NAT/公网）；安全组（有状态，实例级）；NACL（无状态，子网级）。分层（Web/App/Data 子网）、最小开放、跨 VPC 用 Peering/专线、出口审计。
- **易错点**：混淆有状态安全组与无状态 NACL，规则写反。
- **延伸**：network Q15；Q4

### Q4. 云上成本优化（FinOps）常用手段？
- **难度**：🔴 高级
- **关键词**：FinOps, 预留实例, Spot, 闲置回收
- **概念速记**：降浪费=右配 + 弹性 + 回收 + 分账。
- **参考答案**：预留实例/Savings Plans（长稳态）、Spot（容错）、闲置回收、右配（降配过大实例）、存储分层（标准/低频/归档）、带宽优化、标签分账、预算告警。看利用率与浪费。
- **易错点**：只谈单价不谈闲置率与浪费。
- **延伸**：kubernetes Q37；gpu-ai Q12、Q18

### Q5. 堡垒机 / 跳板机 / 零信任（Zero Trust）运维接入？
- **难度**：🟡 中级
- **关键词**：堡垒机, 零信任, SSO, MFA
- **概念速记**：零信任=不默信任内网，按需鉴权。
- **参考答案**：传统堡垒机集中审计 SSH/RDP；零信任：不默信任内网，按需鉴权、最小权限、持续验证（Teleport/Boundary）。统一身份（SSO）、会话录制审计、短时效凭证、禁直连生产、MFA。
- **易错点**：内网互信，一旦突破边界横向移动无阻力。
- **延伸**：Q2、Q6（审计）

### Q6. 日志/审计/合规要求（等保 / SOC2 / GDPR）对运维的影响？
- **难度**：🔴 高级
- **关键词**：等保, SOC2, GDPR, 审计留存
- **概念速记**：合规要求日志留存、加密、访问控制、灾备。
- **参考答案**：等保（分级保护、日志留存≥6 月、审计）；SOC2（安全控制审计）；GDPR（数据最小化、可删除、跨境限制）。运维：操作审计全留痕、数据加密（静态/传输）、访问控制、定期扫描、灾备合规。
- **易错点**：日志留存不足，等保/合规审计不通过。
- **延伸**：Q5、observability Q12（审计）

### Q7. 密钥/证书管理（Vault / KMS / ACME）？
- **难度**：🔴 高级
- **关键词**：Vault, KMS, ACME, 证书续期
- **概念速记**：动态密钥 + 自动续期，防过期与泄露。
- **参考答案**：Vault（动态密钥、租赁、加密即服务）；KMS（云托管密钥，信封加密）；ACME（自动签发/续期，Let's Encrypt）。证书自动续期监控（防过期）、密钥轮换、HSM、etcd 加密配置。
- **易错点**：证书过期导致大面积不可用，却无监控。
- **延伸**：kubernetes Q21（证书）；Q2

### Q8. 安全基线扫描与漏洞管理（CIS / Trivy / 主机漏扫）？
- **难度**：🟡 中级
- **关键词**：CIS Benchmark, Trivy, 漏洞扫描, 修复SLA
- **概念速记**：基线+镜像+主机三层扫描，高危限时修。
- **参考答案**：CIS Benchmark 做系统/K8s 基线；Trivy/Clair 扫镜像漏洞；主机/中间件漏扫（Nessus/OpenSCAP）；建立修复 SLA（高危限时）。融入 CI（扫描不通过阻塞）与例行巡检。
- **易错点**：扫描出漏洞但无 SLA，长期不修。
- **延伸**：cicd-iac Q7（供应链安全）；Q6

### Q9. DDoS / CC 攻击防护在运维层面怎么做？
- **难度**：🔴 高级
- **关键词**：DDoS, CC, 高防, 限速, CDN
- **概念速记**：多层清洗 + 限速 + 吸收 + 回源保护。
- **参考答案**：云清洗/高防 IP、限速（WAF/网关）、Anycast 分散、CDN 吸收、黑洞策略、异常流量检测。带宽预留、自动触发清洗、回源保护、应急预案（降级静态页）。
- **易错点**：回源无保护，DDoS 打垮源站。
- **延伸**：network Q8（Anycast）、Q13（CDN）

### Q10. 如何做主机/容器入侵检测（HIDS / Falco）？
- **难度**：🔴 高级
- **关键词**：HIDS, Falco, eBPF, 运行时安全
- **概念速记**：Falco 用 eBPF 检测容器运行时异常。
- **参考答案**：HIDS（Osquery/Wazuh）查主机异常；Falco 用 eBPF 检测容器运行时异常（提权、敏感挂载、反弹 shell）。规则调优降误报、告警联动、与 SIEM 集成、定期攻防演练验证。
- **易错点**：规则过多误报淹没，告警被忽略。
- **延伸**：observability Q17（eBPF）；kubernetes Q27（安全上下文）

### Q11. 按 OWASP Kubernetes 安全清单，一个集群该从哪几个阶段加固？
- **难度**：🔴 高级
- **关键词**：OWASP, 主机加固, 构建期, 部署期, 运行期, 纵深防御
- **概念速记**：OWASP 的 K8s 安全清单按**生命周期分层**：主机 → 控制面组件 → 构建期（Build）→ 部署期（Deploy）→ 运行期（Runtime）。面试答这题的价值在于**体系化**，而不是罗列工具。
- **参考答案**：
  1. **主机与控制面**：
     - 及时升级 K8s（只维护最近三个小版本，跑在 EOL 版本上等于放弃补丁）。
     - **etcd 是最高价值目标**——拿到 etcd 等于拿到全部 Secret。必须开客户端/对等 TLS、限制只有 apiserver 能访问、静态加密、备份文件本身加密。
     - 关闭/保护敏感端口：kubelet 只读端口 10255、kubelet API 10250 开认证鉴权（`--anonymous-auth=false`、`--authorization-mode=Webhook`）。
     - Dashboard 不暴露公网、不给 cluster-admin。
  2. **构建期**：只用**授权来源**的镜像（ImagePolicyWebhook / Kyverno 校验仓库与签名）；CI 里做漏洞扫描（Trivy/Grype）并**卡门禁**；最小化镜像（distroless/apko，不带 shell 和包管理器就少了大半攻击面）；不打包密钥进镜像。
  3. **部署期**：
     - namespace 做资源与权限隔离 + ResourceQuota/LimitRange（防单租户耗尽集群）。
     - **securityContext 必配**：`runAsNonRoot: true`、`readOnlyRootFilesystem: true`、`allowPrivilegeEscalation: false`、`drop: [ALL]` capabilities。
     - **Pod Security Admission** 按 namespace 设 `restricted`/`baseline`（PSP 已移除）。
     - **NetworkPolicy 默认拒绝**再按需放行（默认全通是最大的横向移动温床，见 kubernetes Q15）。
     - RBAC 最小权限，持续审计（`kubectl auth can-i --list`、kubectl-who-can）。
  4. **运行期**：Falco/Tetragon 做运行时检测；沙箱运行时（gVisor/Kata）隔离不可信负载；限制加载内核模块；异常 Pod **缩容到零**做取证而不是直接删；凭据定期轮转；审计日志集中留存。
  5. **贯穿始终**：订阅 K8s 安全公告（kubernetes-announce）、定期跑 CIS Benchmark（kube-bench）、做攻防演练验证策略真的生效。
- **易错点**：只做镜像扫描就认为安全做完了；etcd 不加密不限访问；NetworkPolicy 一直是默认全通；用已废弃的 PSP 而不是 PSA。
- **延伸**：Q8、Q10、kubernetes Q15、Q25、Q27、来源：[OWASP Kubernetes Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)

### Q12. seccomp / AppArmor / SELinux 在容器里怎么落地？Security Profiles Operator 解决什么？
- **难度**：🔴 高级
- **关键词**：seccomp, AppArmor, SELinux, RuntimeDefault, Security Profiles Operator, 系统调用白名单
- **概念速记**：
  - **seccomp**：限制进程能调用哪些**系统调用**，是缩小内核攻击面最直接的手段。
  - **AppArmor**：基于**路径**的强制访问控制（能读写哪些文件、能不能用网络）。
  - **SELinux**：基于**标签**的强制访问控制，粒度更细但更难写，RHEL 系默认。
- **参考答案**：
  1. **最低成本的一步**：给所有 Pod 加
     ```yaml
     securityContext:
       seccompProfile: {type: RuntimeDefault}
     ```
     容器运行时自带的默认 profile 已经屏蔽了几十个危险系统调用（如 `keyctl`、`ptrace`、`mount`），**几乎零成本、几乎零兼容风险**，却常被忽略。PSA 的 `restricted` 级别会强制要求它。
  2. **自定义 profile 的难点**：手写系统调用白名单几乎不可行——漏一个调用应用就崩，多留一个就没意义。这正是 **Security Profiles Operator（SPO）** 的价值：
     - **录制模式**：用 eBPF 或 audit 日志观察工作负载在正常运行时**实际用到**的系统调用/文件路径，自动生成 `SeccompProfile`/`SelinuxProfile`/`AppArmorProfile` CR。
     - **分发**：通过 DaemonSet（spod）把 profile 同步到每个节点的 kubelet 目录，并管理生命周期（K8s 原生没有 profile 分发机制，这是最实际的痛点）。
     - **绑定**：`ProfileBinding` 可按镜像自动给 Pod 挂上 profile，不需要改每个 Deployment。
     - **日志增强**：把违规的系统调用记录出来，便于迭代收紧。
  3. **落地路径（一定要渐进）**：`RuntimeDefault` 全量铺开 → 对高价值/高风险工作负载用 SPO 录制 → 先以 **audit/complain 模式**运行观察一段时间 → 确认无误再切 enforce。**直接上 enforce 必然踩坑。**
  4. **和沙箱的关系**：seccomp/AppArmor 是「在共享内核上收紧」；**gVisor/Kata** 是「换一个内核/虚拟机」。跑不可信的多租户代码（如用户提交的训练脚本、CI runner）应该用沙箱，而不是指望 seccomp 挡住一切。
  5. **验证**：`kubectl exec` 里试一个被禁的调用应返回 `Operation not permitted`；检查节点 `/var/lib/kubelet/seccomp/operator/...` 下 profile 是否真的下发。
- **易错点**：连 `RuntimeDefault` 都没开就讨论高级方案；手写 profile 漏调用导致线上崩溃；直接 enforce 不经过 audit 阶段；以为 seccomp 能替代沙箱隔离。
- **延伸**：Q10、Q11、kubernetes Q27

### Q13. 云上怎么彻底摆脱长期 AK/SK？IRSA / Workload Identity / SPIFFE 的共同思路是什么？
- **难度**：🔴 高级
- **关键词**：IRSA, Workload Identity, OIDC, 短期凭据, SPIFFE, 零信任
- **概念速记**：长期 AK/SK 的问题是**不会过期、难以审计、一旦泄露就是持久后门**（GitHub 上泄露的云凭据是最常见的入侵起点）。现代做法统一是：**用平台已有的、可验证的工作负载身份，去换一份短期凭据。**
- **参考答案**：
  1. **共同的三段式模式**：
     ```
     工作负载身份（可验证的凭据）→ 身份提供方校验 → 换取短期访问令牌 → 到期自动续
     ```
     - **AWS IRSA**：K8s 把投影令牌（见 kubernetes Q49）挂进 Pod，audience 设为 `sts.amazonaws.com`；集群的 OIDC provider 注册到 AWS IAM；Pod 用这个 JWT 调 `AssumeRoleWithWebIdentity` 换取**临时** AK/SK/Token。IAM Role 的信任策略里可以精确限定到 `<namespace>:<serviceaccount>`。
     - **GCP Workload Identity**：K8s SA 绑定到 GCP SA，机制同理。
     - **Azure Workload Identity**：同样基于 OIDC 联邦。
     - **SPIFFE/SPIRE**：跨平台的通用版本——两阶段证明（节点证明 + 工作负载证明）后签发短期 SVID 证书，K8s 与虚拟机可以统一到同一信任域（见 service-mesh Q8）。
  2. **为什么安全性质变**：
     - 凭据**短期**（分钟/小时级），泄露窗口极小。
     - 凭据**绑定身份**（namespace + SA），偷出去到别的地方用不了。
     - 凭据**不落盘、不进 Git、不进镜像**。
     - 权限可按 SA 精确切分，天生符合最小权限。
  3. **落地要点**：
     - IAM Role 信任策略必须限定 `sub`（namespace:sa），**不能写通配**——否则集群里任何 Pod 都能 assume。
     - 应用/SDK 必须**每次使用前重读令牌文件**，不能启动时缓存（见 kubernetes Q49）。
     - 审计：CloudTrail 里能看到具体是哪个 SA 发起的调用，这是长期 AK 做不到的。
  4. **存量迁移**：先盘点所有硬编码凭据（gitleaks/trufflehog 扫历史提交）→ 双轨运行 → 切换到 IRSA → **吊销旧 AK 并验证没有调用失败**（不吊销等于白做）。
  5. **兜底**：确实需要静态密钥的场景（外部 SaaS API Key），用 Vault / 云 KMS + External Secrets Operator 集中托管并自动轮转，K8s 里不留明文。
- **易错点**：IAM 信任策略写得太宽；应用缓存令牌导致过期后失败；迁移完不吊销旧凭据；以为 K8s Secret 就算「安全存储」（默认只是 base64）。
- **延伸**：Q2、Q7、kubernetes Q48、Q49、service-mesh Q8

### Q14. 软件供应链安全怎么做？SBOM、镜像签名、准入验签各在哪一环？
- **难度**：🔴 高级
- **关键词**：SBOM, sigstore/cosign, SLSA, 准入验签, distroless, 依赖投毒
- **概念速记**：供应链攻击的路径是「**污染源头，一次投毒，处处中招**」——依赖包投毒、CI 被入侵、镜像仓库被替换。防御思路是给每一环加上**可验证的出处（provenance）**。
- **参考答案**：
  1. **按环节拆解**：
     | 环节 | 风险 | 对策 |
     |---|---|---|
     | 依赖 | 投毒包、typosquatting、已知 CVE | 锁版本（lockfile）、私有代理仓库、SCA 扫描、依赖更新审查 |
     | 构建 | CI 被入侵、构建不可复现 | 构建环境隔离、最小权限、**可复现构建**、SLSA 等级 |
     | 产物 | 镜像被篡改/替换 | **cosign 签名** + 生成 **SBOM** + 构建 provenance 证明 |
     | 分发 | 仓库被攻破、拉到错镜像 | 私有仓库、镜像不可变 tag/digest 引用 |
     | 部署 | 运行未授权镜像 | **准入控制验签**（Kyverno/Gatekeeper/Connaisseur） |
     | 运行 | 新披露的 CVE | 持续扫描已部署镜像、快速重建发布 |
  2. **SBOM（软件物料清单）**：记录镜像里有哪些组件与版本（SPDX / CycloneDX 格式，用 syft 生成）。**它本身不提供防护，价值在事后响应**——Log4Shell 那种级别的漏洞爆出时，能在几分钟内回答「我们哪些镜像受影响」，而不是花几天人肉排查。
  3. **签名与验签（sigstore/cosign）**：
     - 构建完 `cosign sign` 给镜像签名，支持 **keyless**（用 OIDC 身份签名，公开记录在 Rekor 透明日志里，不需要自己管私钥——这是最大的易用性突破）。
     - 集群侧用 Kyverno 的 `verifyImages` 规则做**准入验签**：签名不对、来源仓库不对、没有 provenance 的镜像**直接拒绝创建**。这一步是整条链的闭环——**没有准入验签，前面的签名都只是装饰**。
  4. **减小攻击面**：用 **distroless / apko / Chainguard Images** 这类最小镜像，不带 shell、包管理器、调试工具。被拿到 RCE 也很难横向移动，且 CVE 数量通常少一个数量级。
  5. **SLSA 等级**是衡量成熟度的框架：从「有构建脚本」到「构建可复现 + 有不可伪造的 provenance」分级推进，适合作为团队的路线图。
  6. **务实的落地顺序**：CI 里加 SCA 与镜像扫描并卡门禁 → 生成 SBOM 并归档 → cosign 签名 → 准入验签（先 audit 模式再 enforce）→ 最小化基础镜像。
- **易错点**：只做扫描不做验签（镜像仍可被替换）；签了名但集群不校验；SBOM 生成后没有存档与检索能力，出事时用不上；用 `latest` tag 而非 digest 引用镜像。
- **延伸**：Q8、Q11、cicd-iac Q7、kubernetes Q24

### Q15. CKS（Certified Kubernetes Security Specialist）考的是哪些「动手」能力？一个安全加固任务从头到尾怎么做？
- **难度**：🔴 高级
- **关键词**：NetworkPolicy, AppArmor, seccomp, RBAC, audit policy, kube-bench, RuntimeClass, Falco, ImagePolicyWebhook, trivy, kubesec
- **概念速记**：
  - **CKS**：Linux Foundation 2020 年 KubeCon NA 推出的实操认证，**先过 CKA 才能考**；2 小时、纯命令行，特点是**大量第三方工具**（trivy、kube-bench、Falco、kubesec、AppArmor）会直接出现在题面里。
  - **考察面**分四层：集群加固（apiserver 参数、审计、CIS、升级）→ 工作负载加固（securityContext、PSA、AppArmor/seccomp、RuntimeClass）→ 供应链（镜像扫描、Dockerfile 审查、准入 webhook）→ 运行时（Falco、异常端口与进程处置）。
- **问题**：面试官给你一个 kubeadm 集群，要求：① 让 `dev` 命名空间默认拒绝出站；② 开启 apiserver 审计并只对 Deployment 记 `RequestResponse`；③ 跑 CIS 基线并修复失败项；④ 给某个 Pod 加只读根文件系统与自定义 seccomp；⑤ 发现节点上一个陌生进程监听 9999 端口并处置。逐项说你的操作与验证方式。
- **参考答案**：
  1. **NetworkPolicy 默认拒绝出站**：`podSelector: {}` + `policyTypes: [Egress]` 且不写任何 `egress` 规则即为拒绝全部出站；验证用 `kubectl exec` 从 Pod `curl` 目标 IP 应超时。**易错细节**：跨命名空间放行用 `namespaceSelector` 时目标 namespace **必须真的有那个 label**（`kubectl label ns default ns=default`），否则策略「看起来对但不生效」；`from` 下两个条目是「或」，同一条目里 `namespaceSelector` 与 `podSelector` 并列才是「与」。
  2. **审计策略**：在 `/etc/kubernetes/manifests/kube-apiserver.yaml` 加 `--audit-policy-file`、`--audit-log-path`、`--audit-log-maxsize` / `--audit-log-maxbackup` / `--audit-log-maxage`，并把策略文件与日志目录用 **hostPath 挂进静态 Pod**（漏挂 volume 是最常见的「apiserver 起不来」原因）。策略四个级别 **None / Metadata / Request / RequestResponse**，规则**自上而下首个匹配生效**；只记 Deployment 的完整请求响应就写 `level: RequestResponse` + `group: "apps"` + `resources: ["deployments"]`，末尾放 `level: Metadata` 兜底并 `omitStages: [RequestReceived]` 减少噪音。改完等 apiserver 静态 Pod 重启，`tail` 审计日志确认有 `auditID` 事件。
  3. **CIS 基线**：用 kube-bench（可直接 `docker run --pid=host -v /etc:/etc:ro -v /var:/var:ro ... aquasec/kube-bench run --targets=master|node`）。典型 FAIL 及修复：controller-manager / scheduler / apiserver 的 `--profiling=false`；apiserver 的 `--audit-log-*` 系列；etcd 数据目录属主 `etcd:etcd`；`--kubelet-certificate-authority` 未设。修复方式都是改 `/etc/kubernetes/manifests/*.yaml` 后重跑 kube-bench 看 FAIL 数下降——面试要强调「**理解每条检查在改什么参数**」，而不是记工具安装命令。
  4. **工作负载加固**：容器级 `securityContext.readOnlyRootFilesystem: true`，应用要写的目录（`/var/run`、`/var/cache/nginx`、`/var/log/nginx`）用 `emptyDir` 单独挂成可写；验证 `kubectl exec ... touch /etc/x` 报 Read-only file system。seccomp：把 `{"defaultAction":"SCMP_ACT_LOG"}` 之类的 JSON 放到 **`/var/lib/kubelet/seccomp/profiles/`**（路径错会报 `cannot load seccomp profile` 的 ContainerCreateError），Pod 里 `seccompProfile: {type: Localhost, localhostProfile: profiles/policy.json}`，并且**每个可能被调度到的节点都要有该文件**。AppArmor：`apparmor_parser -q <profile>` 加载后用注解 `container.apparmor.security.beta.kubernetes.io/<容器名>: localhost/<profile>`（新版本已迁到 `securityContext.appArmorProfile`），`cat /proc/1/attr/current` 看到 `(enforce)` 即生效。顺手清理 `privileged: true`、`allowPrivilegeEscalation: true`、`runAsUser: 0` 这类高危配置，可用 `kubesec scan pod.yaml`（Privileged 扣 30 分）做量化。
  5. **可疑端口处置**：`netstat -tunlp | grep 9999`（或 `ss -tunlp`）拿到 PID → `ps -f -p <PID>` 看到真实二进制与 systemd 单元 → `systemctl stop && systemctl disable <unit>`，必要时删掉单元文件；这是把「Linux 基本功」揉进 K8s 安全的典型题。
  6. **补齐其它高频项**：RBAC 组合只有 Role+RoleBinding、ClusterRole+RoleBinding、ClusterRole+ClusterRoleBinding 三种合法（**Role + ClusterRoleBinding 是错的**），验证用 `kubectl auth can-i <verb> <res> --as system:serviceaccount:<ns>:<sa> -n <ns>`；镜像扫描 `trivy image --severity HIGH,CRITICAL <image>`，先用 jsonpath 列出集群里所有镜像再逐个扫；`RuntimeClass`（`handler: runc|runsc|kata`）让不可信负载跑在 gVisor / Kata；Falco 规则在 `/etc/falco/falco_rules(.local).yaml`，输出格式可改成 `[%evt.time][%container.id] [%container.name]`，Helm 装则改 ConfigMap；ImagePolicyWebhook 需要 `--admission-control-config-file` 指向含 `imagePolicy.kubeConfigFile` 的配置，**`defaultAllow: false` 意味着 webhook 不可达时所有 Pod 都创建不了**（生产要想清楚）；PSP 已在 1.25 移除，用 **Pod Security Admission** 的 `restricted` / `baseline` 标签替代；升级走 cordon → drain → 升 kubeadm → `kubeadm upgrade apply|node` → 升 kubelet/kubectl → `systemctl restart kubelet` → uncordon。
- **易错点**：NetworkPolicy 的 namespace 没打标签；审计策略改了但 hostPath 没挂、或把 `deployments` 放在 core group（`""`）下导致规则不匹配；seccomp 文件只放在 control-plane 节点；`defaultAllow: false` 的 webhook 把集群锁死；把 PSP 当现行方案；把 kube-bench 的 WARN 当 FAIL 全改一遍却不理解含义。
- **延伸**：Q8、Q10、Q11、Q12、Q14、kubernetes Q15、Q25、Q26、Q27、Q32、来源：Saiyam Pathak《CKS Book》（19 个实操场景，商业电子书，本地 PDF 存档；本题为主题提炼，不含原题）、[Kubernetes 官方文档 - Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)、[walidshaari/Certified-Kubernetes-Security-Specialist](https://github.com/walidshaari/Certified-Kubernetes-Security-Specialist)

### Q16. Kubernetes 1.24 的官方第三方安全审计（NCC Group）发现了什么？哪些结论直接影响你的集群加固清单？
- **难度**：🔴 高级
- **关键词**：安全审计, 威胁模型, nodes/proxy 提权, 请求头认证 CA, RBAC 无 Deny, NetworkPolicy 局限, Bootstrap Token, 审计日志来源
- **概念速记**：
  - **CNCF 第三方审计**：CNCF 为毕业项目定期委托安全公司做架构评审 + 源码辅助评估。Kubernetes 做过两次：**1.13（2019，Trail of Bits）** 与 **1.24（2022 执行，NCC Group 2023 年发布）**。
  - **1.24 审计范围**：kube-apiserver、kube-scheduler、对 etcd 的使用、kube-controller-manager、cloud-controller-manager、kubelet、kube-proxy、secrets-store-csi-driver；容器运行时自身的逃逸不在范围内。
  - **结果**：**19 个发现，0 Critical / 0 High / 6 Medium / 9 Low / 4 Informational**，其中 13 个落在 apiserver。多数需要已有较高权限或错误配置才能触发，但几条是「配置正确也会踩」的设计层问题。
- **问题**：面试官问：「你看过 Kubernetes 官方安全审计报告吗？说说里面对生产集群最有指导意义的三到五条发现，以及你会据此改什么。」
- **参考答案**：
  1. **`nodes/proxy` 等于对所有节点的 kubelet 拥有 master 级访问（Medium）**：apiserver 代理到 kubelet 时用**自己的客户端证书**（属 `system:masters`）认证，所以只要有 `nodes/proxy` GET 权限就能调 kubelet 的 `/exec` 在任意 Pod 里执行命令；更进一步，若还有 `nodes/status` PATCH 或 `nodes` CREATE，可以把节点地址 / 端口改成 apiserver 自己，让 apiserver「用 master 证书请求自己」，直接拿 cluster-admin。**改法**：把 `nodes/proxy`、`nodes/status` 写权限视同 cluster-admin 来审计，用 `kubectl-who-can` / `can-i --list` 定期扫；监控类组件尽量走 metrics API 而非 kubelet 代理。
  2. **client CA 与 requestheader CA 不能是同一个（Medium，Impact High）**：`--client-ca-file` 和 `--requestheader-client-ca-file` 若共用一个 CA、又没设 `--requestheader-allowed-names`，那么任何持该 CA 签发证书的用户都能伪造 `X-Remote-User` / `X-Remote-Group: system:masters` 冒充任意身份。**改法**：检查 kubeadm / 自建集群的两组 CA 是否分离，`--requestheader-allowed-names` 只列聚合层前置代理的 CN；同理 etcd 客户端 CA 也要独立。
  3. **RBAC 只做加法、没有 Deny，失败即放行（fail open）（Medium）**：宽泛的 Role 一旦误绑就无法用「禁止」抵消；授权器出错只能返回 NoOpinion。**改法**：在准入层补一道（Kyverno / OPA Gatekeeper）做「负向」约束，Role 按资源与动词最小化并做周期 diff。
  4. **NetworkPolicy 只能做到命名空间级隔离（Low）**：策略靠**标签 opt-in**，能改 Pod 标签的人就能「蹭」上宽松策略；CNI 是否真正执行策略集群无从判断；DNS 递归解析可被用作绕过 egress 的隐蔽信道。**改法**：每个命名空间先落 `podSelector: {}` 的默认拒绝，用准入控制器锁定安全相关标签，egress 只放行集群 DNS 并对 DNS 也做策略 / 日志。
  5. **Pod Security Standards 的 Restricted 档有漏（Low）**：只强制 `runAsUser≠0`，**没管 `runAsGroup`**，GID 0 仍可访问 root 组资源；`seccompProfile.type: Localhost` 允许选到比 `RuntimeDefault` 更弱的 profile。**改法**：准入策略补 `runAsGroup≠0`、限制 Localhost seccomp 只能指向白名单 profile。
  6. **其他值得记住的**：命名空间里传 `..` 会缩短 etcd key 前缀、放大 list 范围（Medium，可借分页 token 枚举对象名，对 CRD 可能返回其他类型对象）；apiserver 代理到 Pod / Service 时 `InsecureSkipVerify`（Medium，可被中间人）；审计日志不记录**认证来源**，拿到 CA 的攻击者伪造 SA 证书后与正常请求无法区分（Low）；Bootstrap Token 只有约 83 bit 熵且认证失败时会**明文写进 apiserver 日志**（Info / Low）；loopback token 不校验来源接口且不轮换；emptyDir 不支持 `noexec`，所以「只读根文件系统 + emptyDir 可写目录」仍能被放入并执行恶意二进制。
  7. **方法论层面的启示**：报告先按四类使用场景（生产 + 开发隔离、CI/CD、代码执行即服务、多租户 SaaS）和十类角色建**威胁模型**再审代码；并指出 **1.13 审计的部分发现至今未修**——面试时可以说：架构级问题（RBAC 无 Deny、访问控制割裂）短期只能靠文档与准入层缓释，团队要把「官方已知但未修的设计缺陷」纳入自己的基线。
- **易错点**：把 0 Critical / 0 High 理解成「K8s 很安全不用管」；不知道 `nodes/proxy` 的真实威力；以为 NetworkPolicy 配了就是 Pod 级隔离；只记 finding 不会转成自己集群的检查项。
- **延伸**：Q11、Q15、kubernetes Q25、Q43、Q49、来源：NCC Group《Kubernetes 1.24 Security Audit》（2023-04-05 v1.2，为 CNCF / Kubernetes SIG Security 出具，本地 PDF 存档；发现细节见 `collections/k8s-local-library.md` 第二组）

### Q17. 一次授权的集群 RBAC 攻击面评审列出了哪几类「从一个 Pod 走到 cluster-admin」的路径？作为防守方，你怎么审计并逐条堵住？
- **难度**：🔴 高级
- **关键词**：攻击路径 attack path, RBAC 提权, 最小权限, 横向移动, IRSA / Workload Identity, impersonate, 变更准入, GitOps operator
- **概念速记**：
  - **攻击路径图（attack-path graph）**：把 Pod、ServiceAccount、Role/Binding、Secret、Node、云身份建成节点，把「以谁运行 / 挂载了什么 / 能 exec 谁 / 能 patch 谁 / 能 impersonate 谁」建成边，从某个立足点做最短路径搜索，找出到高价值目标的多跳链路。红队工具（如 k8scout）用它做进攻侧枚举，**蓝队用同一张图做加固审计**——两边看的是同一份 RBAC。
  - **关键前提**：`SelfSubjectRulesReview` / `SelfSubjectAccessReview` 是**任何身份都能调用、不需要额外授权**的，所以「一个 token 到底有什么权限」对攻防双方都是透明的——防守不能靠「攻击者查不到」。
- **问题**：假设一次授权的安全评审把集群里「从一个被攻陷的 Pod 到 cluster-admin / 节点 / 密钥 / 云 IAM」的可达路径都列了出来。请说出这些路径通常分成哪几类，每一类的**根因权限**是什么，以及你作为运维 / 平台方**怎么审计和封堵**。
- **参考答案**：
  1. **直接 RBAC 提权**：SA 拥有 `bind` / `escalate`、或能创建 ClusterRoleBinding、或被绑到带**通配符 verb/resource**的 Role。审计：`kubectl auth can-i --list --as system:serviceaccount:<ns>:<sa>`、kubectl-who-can、rakkess 扫出谁能 `create clusterrolebindings` 与谁持有 `*`；封堵：去通配符、`bind`/`escalate`/`impersonate` 视同 cluster-admin 收敛。
  2. **工作负载变更（workload mutation）**：能 `patch` / `update` Deployment、DaemonSet 的 SA 可以把工作负载的 `serviceAccountName` 改成高权 SA，重建后继承其权限。审计：谁对 workloads 有写权限、命名空间里有没有高权 SA 可被指派；封堵：拆分「能改工作负载」与「能选任意 SA」，用准入策略限制可用 SA。
  3. **容器逃逸到节点**：`privileged`、`hostPID` / `hostNetwork`、危险 capability（`SYS_ADMIN` 等）、`hostPath` 挂 `/`、挂 docker.sock。审计：跑 kube-bench / Pod Security Admission `restricted` 审计模式看有多少违规；封堵：PSA `restricted`、准入策略（Kyverno/Gatekeeper）拒绝这些字段。
  4. **横向移动 + 令牌窃取**：`pods/exec`、`pods/attach`、能读别的 Pod 挂载的 SA token / Secret、`nodes/proxy`（见 Q16，等同任意 kubelet 的 master 级访问）。封堵：收敛 `exec` / `nodes/proxy`，`automountServiceAccountToken: false` 默认关闭投影令牌，敏感 Secret 用外部密钥管理而非 env 明文。
  5. **impersonate 链**：拥有 `impersonate` 的 SA 可冒充更高权限的用户 / 组 / SA。审计：谁有 `impersonate`（users/groups/serviceaccounts）；封堵：几乎所有业务都不该有它，等同 cluster-admin 处理。
  6. **准入 webhook 注入**：能创建 / 改 MutatingWebhookConfiguration 的身份可以给未来所有工作负载注入 sidecar / 改 SA。封堵：把 webhook 配置的写权限锁死，webhook 证书与 `failurePolicy` 纳入审计。
  7. **云 IAM 提权**：IRSA（AWS）、GKE / Azure Workload Identity 下，拿到投影令牌 + 可访问云 metadata（169.254.169.254）就能拿角色凭据；`audience` 配置不当可跨用途复用。封堵：SA 与 IAM 角色一对一最小授权、用 NetworkPolicy / hop-limit 挡 metadata、令牌 audience 收紧。
  8. **GitOps / operator 滥用**：ArgoCD、Flux、External Secrets、Vault operator 往往持有极高权限，控制它们的 CR 就等于控制集群。封堵：给这些 operator 的 SA 也做最小权限与命名空间隔离，审计谁能写它们的 CR。
  9. **审计方法论收尾**：把「导出全量 RBAC → 建图 → 从每个非系统 SA 找到高价值目标的可达路径 → 按‘攻击者成本’排序先修最便宜的」做成**周期性只读作业**（reviewer 模式的只读 SA 即可），发现悬空绑定、通配符、默认自动挂载令牌、env 明文密钥这类 misconfig；每条发现映射到 MITRE ATT&CK 便于和检测（Falco，见 observability Q23）对齐。
- **易错点 / 面试官关注**：
  - 只盯「有没有人是 cluster-admin」，忽略**多跳**路径（patch workload → 换 SA → 继承权限）。
  - 不知道 `bind` / `escalate` / `impersonate` / `nodes/proxy` / `pods/exec` 这几个「等同提权」的动词。
  - 把云 IAM 当成集群之外的事，忘了投影令牌 + metadata 的组合。
  - 只做一次性评审，没有做成周期性只读审计。
- **延伸**：Q11、Q15、Q16、observability Q23、kubernetes Q25（RBAC）、Q27、来源：k8scout（github.com/k8scout/k8scout，MIT，授权评估用的 RBAC 攻击路径引擎，50 条检测规则 + MITRE ATT&CK 映射）的能力清单反推的防守审计视角
