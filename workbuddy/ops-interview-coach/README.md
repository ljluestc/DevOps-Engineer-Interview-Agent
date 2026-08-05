# Ops Interview Coach（运维面试教练）

一个基于结构化运维知识体系的面试模拟智能体：既能**逐题模拟面试并打分**，也能**讲透基础概念**（OSI、CRI/CNI/CSI、Dockerfile、Ansible、GPU 等）。覆盖 Linux、网络、Kubernetes、CI/CD、可观测性、SRE、中间件、GPU/AI、云安全、行为与架构共 10 大模块，适配实习到高管各层级。

> 本智能体的题库与基础篇源自开源项目 [ops-interview](https://github.com/)（200 题 + 深度基础篇），本专家内置其浓缩版，可离线独立使用。

## 类型
Agent 型（单个 AI 专家）

## 核心能力
- **逐题模拟面试**：一次一题，按模块/难度/级别动态出题；作答后给 ✅⚠️💡📊 结构化反馈与 1–10 评分；支持 `hint`/`skip`/`explain`/`score`/`harder`/`easier`/`switch`/`end`/`restart` 指令。
- **概念深度讲解**：用「速记 + 原理 + 对比表 + 误区」讲清高频基础词，拒绝只抛名词。
- **完整记分卡**：结束输出各模块得分、总分、录用裁决（Strong Hire → No Hire）、关键优势、待改进项与推荐学习主题。
- **简历驱动定制**：可分析简历并针对性出题、动态调难度。

## 内置知识（skills/ops-interview）
- `references/basics.md`：深度基础篇（Linux / 网络·OSI / Docker·Dockerfile / K8s·CRI·CNI·CSI / Ansible / AI·GPU）
- `references/questions.md`：分模块题库（10 模块，标准化模板 + 🟢🟡🔴⚫ 难度图例）

## 使用示例
- 「模拟一场高级运维工程师面试，从 Linux 与系统内核开始」
- 「考我一道 Kubernetes 网络面试题（CNI/CRI/CSI）」
- 「讲透 OSI 七层模型以及它和真实排障的对应关系」

## 头像
头像已自动生成在 `avatars/` 目录下。如需替换，要求：PNG/JPG、512×512 px、≤500KB。

## 安装 / 注册
专家包已置于专家目录：
```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/ops-interview-coach/
```
注册后即在 WorkBuddy 中可见：
```bash
python3 scripts/register_expert.py <expert-dir>
```

## 打包分享
```bash
zip -r ops-interview-coach.zip ops-interview-coach/
```
