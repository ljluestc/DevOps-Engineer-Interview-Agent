# 05 · Ansible 基础深度篇

> 关键词：幂等、Playbook、Inventory、Module、Role、Facts、变量优先级、Vault、Handler

---

## 1. Ansible 是什么 / 不是什么

- **是什么**：无 agent 的**配置管理 / 自动化编排**工具。通过 SSH 连被管节点，用 YAML 描述「期望状态」。
- **不是什么**：不是 IaC（建基础设施用 Terraform）；不是容器编排。
- 对比：

| 维度 | Ansible | Terraform |
|---|---|---|
| 管理对象 | 已有机器上的软件/配置 | 云基础设施（资源） |
| 模式 | 声明式（配置）+ 过程式（task） | 声明式（HCL） |
| 状态 | 无状态文件（按事实判断） | 有 state 文件 |
| agent | 无（SSH/WinRM） | 无（调云 API） |
| 典型 | 装 nginx、改配置、批量执行 | 建 VPC、开 ECS、建 K8s 集群 |

---

## 2. 核心组件

```
Control Node (ansible / ansible-playbook)
   │  SSH
   ▼
Managed Node 1 ... N
```

- **Inventory**（清单）：被管主机的分组定义（INI/YAML），可静态或动态（云 API 拉）。
- **Module**（模块）：执行单元（`yum`/`copy`/`template`/`service`…），在远端跑完即退，返回 JSON。
- **Playbook**：YAML 编排文件，由一个或多个 play 组成，每个 play 把一组 host 映射到 roles/tasks。
- **Task**：最小执行单元，调用一个 module + 参数。
- **Role**：把 playbook 按「职责」结构化（tasks/handlers/templates/defaults/vars），可复用。
- **Facts**：自动采集的被管节点信息（OS、IP、内存），`gather_facts` 控制是否采集。

---

## 3. 幂等（Idempotence）— 最重要概念

- **定义**：同一 playbook 跑一次和跑 N 次，结果一致（不会改变已正确的状态）。
- **实现靠模块自身**：如 `yum` 检测到已装就跳过（changed=false）；`template` 比对内容一致就不动；`copy` 比对 checksum。
- **反例**：用 `shell`/`command` 直接执行 `echo >> file` 不会幂等（每次都追加）→ 用 `lineinfile` 或 `blockinfile`。

```yaml
- name: 确保 nginx 已安装（幂等）
  yum:
    name: nginx
    state: present     # 已装则 changed=false
```

---

## 4. 变量与优先级（易错）

优先级**从低到高**（高覆盖低）：
1. 命令行 `-e`
2. `vars_files` / `vars` in play
3. `host_vars/` / `group_vars/`
4. Role 的 `defaults/` < `vars/`
5. Inventory 变量
6. Facts

> 口诀：命令行最高，role defaults 最低。**调试用 `ansible-playbook -e` 覆盖、用 `debug` 模块打印。**

---

## 5. Handler / Loop / Tag

- **Handler**：由 notified 触发、在所有 task 结束后按序执行一次（典型：改配置后重启服务）。
- **Loop**：`loop`/`with_items` 批量。
- **Tag**：给 task 打标签，`--tags`/`--skip-tags` 选择性执行（如只跑 `config` 标签）。

```yaml
tasks:
  - name: 写配置
    template: src=nginx.conf.j2 dest=/etc/nginx/nginx.conf
    notify: restart nginx
    tags: config
handlers:
  - name: restart nginx
    service: name=nginx state=restarted
```

---

## 6. Vault（密钥管理）

- `ansible-vault` 加密敏感文件/变量（密码、密钥），运行时 `--ask-vault-pass` 解密。
- 不要明文把密码写进 playbook / 提交 Git。
- 生产更佳：配合外部 Secrets（Vault / AWS SM），playbook 运行时拉取。

---

## 7. 最佳实践

- Role 化、变量分层（`group_vars`/`host_vars`）。
- `--check --diff` 预演（dry run 看会改什么）。
- `ansible-lint` 静态检查。
- 限制范围：`--limit web01`。
- 动态 Inventory 对接云资产，避免清单腐化。

---

## 8. 常见误区

- ❌ 把所有逻辑塞进一个 playbook → 用 Role 拆分复用。
- ❌ 用 `shell` 批量改文件以为幂等 → 用专用模块。
- ❌ 明文写密码 → Vault / 外部 Secrets。
- ❌ 把 Ansible 当 Terraform 建云资源 → 职责错位。

---

## 延伸

- 面试题：见 `modules/cicd-iac/cicd-iac-questions.md`
- 官方：docs.ansible.com
- 对比：Terraform（见同模块题）
