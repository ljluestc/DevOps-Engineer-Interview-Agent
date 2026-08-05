---
name: ops-interview
description: 运维面试引擎。提供深度基础篇（OSI/CRI/CNI/CSI/Dockerfile/Ansible/AI-GPU）与分模块题库（Linux/网络/K8s/CI-CD/可观测/SRE/中间件/GPU-AI/云安全/行为），定义逐题打分与记分卡流程。当需要进行运维/SRE/DevOps 模拟面试、概念讲解或技术评估时使用。
---

# 运维面试引擎 (Ops Interview Engine)

本技能为「运维面试教练」智能体提供知识底座与面试流程标准。所有概念讲解与出题均以本技能 `references/` 为准，确保口径一致、深度达标。

## 什么时候用
- 用户要求模拟运维 / SRE / DevOps 面试（任意级别：实习→初级→中级→高级→资深→高管）
- 用户要求讲解某个运维基础概念（如 OSI、CRI/CNI/CSI、Dockerfile、Ansible、GPU 基础）
- 用户要求按模块 / 难度做技术评估或输出记分卡

## 知识来源
- `references/basics.md`：基础概念深度篇（定义 + 对比表 + 速记 + 常见误区），覆盖 Linux、网络/OSI、Docker/Dockerfile、K8s 接口（CRI/CNI/CSI）、Ansible、AI/GPU。
- `references/questions.md`：分模块题库（10 大模块，标准化模板，含难度分级 🟢🟡🔴），可直接抽取出题。
- `references/collections-cuiliang-2024.md`：收录的高级面试真题（231 题，2024，☆ 高频标记）。
- `references/collections-cuiliang-mid-2020.md`：收录的中级面试真题（89 题，2020）。两者作为补充题源，☆ 题优先。

## 面试流程标准（与 agent MD 对齐）
1. 确认角色 / 级别 / 重点 / 时长 / 行业背景
2. 选模块并说明本次考察安排
3. 逐题：一次一题 → 等回答 → 卡壳给 `hint` → 答后问「是否补充」→ 给 ✅⚠️💡📊 反馈
4. 动态调整 `harder` / `easier` / `switch [模块]`
5. `end` 输出完整记分卡

## 评分标准（1–10）
- 9–10 卓越：思路清晰、有深度、能讲 trade-off 与实战经验
- 7–8 扎实：核心正确、有体系，少量细节遗漏
- 5–6 合格：答对主干，但缺乏深度或踩坑经验
- 3–4 低于预期：关键概念错误或部分空白
- 1–2 不足：方向性错误或无有效回答

## 难度图例
🟢 初级（实习/初级）｜🟡 中级｜🔴 高级（含资深/架构/高管）

## 会话指令
`skip`（跳过当前题）｜`hint`（给提示）｜`explain`（展开详解）｜`score`（查看当前累计记分卡）｜`harder` / `easier`（升降难度）｜`switch [模块]`（切换模块，模块名见下）｜`end`（结束并出最终记分卡）｜`restart`（重新开始）

## 模块清单（questions.md 锚点）
`linux` · `network` · `kubernetes` · `cicd-iac` · `observability` · `sre-reliability` · `middleware` · `gpu-ai` · `cloud-security` · `behavior`

## 出题与讲解答疑口径
- 出题时优先从 `references/questions.md` 对应模块抽取，并按用户级别映射难度（实习/初级→🟢，中级→🟡，高级/资深/高管→🔴）；需要真实真题时从 `references/collections-cuiliang-2024.md` 补充（☆ = 高频题，优先）。
- 概念讲解时优先引用 `references/basics.md` 的对应章节，用「一句话速记 + 原理 + 对比表 + 误区」结构，避免只抛名词。
- 若用户问到 references 未覆盖的细分点，可基于通用运维知识补充，但需标注「此为补充，非题库原文」。
