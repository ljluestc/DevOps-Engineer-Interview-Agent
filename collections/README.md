# Collections — 收录的外部真题

本目录收录来自社区公开文章的**真实面试真题**，用于扩充智能体出题覆盖面。
与 `modules/`（自研标准化题库）不同，这里**保留原作者的分组与标记**，便于对照原始出处。

## 收录清单

| 文件 | 来源 | 题量 | 说明 |
|---|---|---|---|
| `cuiliang-ops-interview-2024.md` | [崔亮博客：高级运维工程师面试题汇总](https://www.cuiliangblog.cn/detail/article/89) | 231 题 | 2024 年 7–8 月面试 20+ 家公司 50+ 场，☆ 标记高频题 |
| `cuiliang-mid-ops-interview-2020.md` | [崔亮博客：中级运维工程师面试题汇总](https://www.cuiliangblog.cn/detail/article/2) | 89 题 | 2020 年发布的中级运维面试题（含 MySQL/NoSQL/Docker/K8s/Prometheus/ELK/运维开发）|

## 版权与使用口径（重要）

- 本目录**仅收录题目列表**（公开网页上可直接阅读的问题文本），**不收录**原作者的参考答案、个人心得与付费内容。
- 每题保留原文措辞与 ☆ 高频标记；分组沿用原文（Linux / Kubernetes / Prometheus / ELK / DevOps / Python-VUE / 开放性）。
- 如需商用或对题目做二次加工分发，请自行评估原作者版权声明；本项目以「学习与参考」为目的收录，并明确标注出处。
- 收录日期：2026-08-05。

## 智能体如何用它

面试官出题时：**优先**从 `modules/` 抽取标准化题（有参考要点与难度），**补充**从 `collections/` 抽取真题（带 ☆ 的高频题优先）。两者的分类映射关系：

| 原分类 | 对应 modules 模块 |
|---|---|
| Linux | `linux` |
| MySQL / NoSQL | `middleware` |
| Docker | `kubernetes`（容器基础）|
| Kubernetes | `kubernetes` |
| Prometheus | `observability` |
| ELK | `middleware`（ES 部分）|
| DevOps / 运维开发 | `cicd-iac` |
| Python/VUE | 无直接对应（开发向，作为补充题源）|
| 日常工作 / 开放性问题 | `sre-reliability` + `behavior` |
