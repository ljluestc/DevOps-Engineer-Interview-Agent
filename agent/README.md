# 运维面试教练 · 智能体（Agent）

本目录是「运维面试教练」智能体的**工具无关定义**。它不是某个平台的私有格式，
而是标准的系统提示词（System Prompt），可被任意支持系统提示词的 LLM 工具加载。

## 文件

- **`UNIVERSAL.md`** — 权威系统提示词。定义了角色、核心能力、面试工作流、评分标准、
  难度图例、会话指令与规则。可直接粘贴到任意 LLM 的 System Prompt。
- 仓库根目录的 **`CLAUDE.md`** 与 **`AGENTS.md`** 是 `UNIVERSAL.md` 的等价副本，
  供 **Claude Code** 与 **Codex** 自动加载（这两个工具会读取仓库根目录对应文件）。

## 知识来源

智能体不内置题目，而是**直接读取本仓库的知识库**，保证与题库同步、不重复维护：

- `basics/` — 基础概念深度篇（Linux / 网络·OSI / Docker·Dockerfile / K8s·CRI·CNI·CSI / Ansible / AI·GPU）
- `modules/` — 200+ 道标准化面试题（10 大模块）

> 所以在使用时，请让模型能访问到本仓库（克隆到本地，或在支持文件读取的工具中打开本目录）。
> 若环境无法读取文件（例如网页版纯对话），可把 `basics/` + `modules/` 的内容一并作为上下文附上。

## 与其他格式的关系

| 目标工具 | 用哪个文件 |
|---|---|
| Claude Code | 根目录 `CLAUDE.md`（自动加载）|
| Codex / OpenAI | 根目录 `AGENTS.md`（自动加载）|
| 任意 LLM（API/网页）| `agent/UNIVERSAL.md` 粘贴为 System Prompt |
| WorkBuddy | `../workbuddy/ops-interview-coach/`（原生专家插件，内置 80 题浓缩版）|

修改提示词时，请同步更新 `UNIVERSAL.md`、`CLAUDE.md`、`AGENTS.md` 三处，保持口径一致。
