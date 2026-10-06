#!/usr/bin/env python3
"""Build collections/system-design-quiz-bank.md from the system-design/ submodule.

Most topic folders carry the same 8 templated quiz questions ("How would you handle a sudden 10x traffic
spike?" ...); this script keeps only the topic-specific material:

  * 06-quiz.md            -> questions minus the templates, with the answer's first prose as key points  (🟡)
  * 20-interview-drills.md -> real drill sections (stubs skipped), title as prompt                       (🔴)
  * rapid-fire tables      -> "topic | one-liner" rows as quick-recall items                             (🟢)

Variant folders are folded to their canonical topic with modules/system-design/resolver.json, and identical
questions are kept once. Re-run after updating the submodule:  python3 scripts/build_system_design_quiz_bank.py
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SD = ROOT / "system-design"
OUT = ROOT / "collections" / "system-design-quiz-bank.md"
RES = json.loads((ROOT / "modules/system-design/resolver.json").read_text(encoding="utf-8"))

TEMPLATES = ["10x traffic spike", "sql vs nosql", "monitor and debug this system", "interact.",
             "data consistency across microservices", "primary database goes down", "design the caching layer",
             "core functional requirements for", "component handle high load"]
SKIP_DRILL = re.compile(r"rapid|recap|summary|outline|index|common traps|whiteboard|pitch|links|references|checklist|spine|one-minute|60-second", re.I)
TABLE_SECTION = re.compile(r"rapid|recap|one-liner|cheat", re.I)
CATS = [("fundamentals", "基础与方法论"), ("building-blocks", "基础组件"), ("products", "产品端到端设计"),
        ("ops-infra", "运维与基础设施"), ("ai-ml", "AI / ML 系统"), ("os-systems", "操作系统与底层"), ("hubs", "综合题库")]
CNUM = "一二三四五六七八九十"
MAXLEN = 360


def text(p):
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def clean(s):
    s = re.sub(r"<summary>.*?</summary>|</?details[^>]*>", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r"^\*\*Answer:?\*\*:?\s*", "", s)


def key_points(body):
    """First prose of an answer (tables / code compacted), capped at MAXLEN characters."""
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    prose, table = [], []
    for line in body.splitlines():
        l = line.strip()
        if not l or l.startswith(("<details", "</details", "<summary", "---", "#")):
            continue
        if l.startswith("|"):
            cells = [c.strip() for c in l.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                table.append(" — ".join(c for c in cells if c))
            continue
        prose.append(re.sub(r"^[-*]\s+|^\d+\.\s+", "", l))
    s = clean(" ".join(prose)) or clean("; ".join(table[1:4] or table[:3]))
    if len(s) > MAXLEN:
        cut = s[:MAXLEN]
        s = (cut[: cut.rfind(". ") + 1] if ". " in cut[120:] else cut.rstrip() + " …")
    return s.replace("|", "/")


def sections(t, level_re):
    parts = re.split(level_re, t, flags=re.M)
    return [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


def norm(q):
    return re.sub(r"[^a-z0-9]+", " ", q.lower()).strip()


def main():
    groups = {}  # canonical -> list of (kind, question, answer)
    seen = set()
    meta = {g["canonical"]: g for g in RES["groups"]}
    folders = sorted(p.name for p in SD.iterdir() if p.is_dir() and not p.name.startswith("."))
    # canonical folder first, then its variants, so the canonical's wording wins on duplicates
    folders.sort(key=lambda f: (RES["folder_to_canonical"].get(f, f), f != RES["folder_to_canonical"].get(f, f), f))
    for f in folders:
        canon = RES["folder_to_canonical"].get(f)
        if not canon or canon not in meta:
            continue
        items = groups.setdefault(canon, [])
        quiz = text(SD / f / "06-quiz.md")
        for head, body in sections(quiz, r"^#{2,4}\s*Q\d+[:.)]?\s*(.+)$"):
            if any(t in head.lower() for t in TEMPLATES) or norm(head) in seen:
                continue
            kp = key_points(body)
            if kp:
                seen.add(norm(head)); items.append(("quiz", clean(head), kp))
        drills = text(SD / f / "20-interview-drills.md")
        if "(Stub" in drills[:400] or len(drills) < 800:
            continue
        for head, body in sections(drills, r"^#{2,3}\s+(.+)$"):
            title = re.sub(r"^((Drill|Scenario)\s*)?\d+\s*[:.)—-]\s*", "", head).strip()
            if SKIP_DRILL.search(head):
                if TABLE_SECTION.search(head):
                    lines = [l.strip() for l in body.splitlines() if l.strip().startswith("|")]
                    for i, l in enumerate(lines):
                        cells = [c.strip() for c in l.strip("|").split("|")]
                        is_sep = all(re.fullmatch(r":?-{2,}:?", c) for c in cells)
                        nxt_sep = i + 1 < len(lines) and all(re.fullmatch(r":?-{2,}:?", c) for c in lines[i + 1].strip("|").split("|"))
                        if is_sep or nxt_sep or len(cells) < 2 or not cells[1]:
                            continue  # separator or header row
                        q = cells[0].strip("* ")
                        if (q.endswith("?") or len(q.split()) >= 2) and norm(q) not in seen:
                            seen.add(norm(q)); items.append(("rapid", clean(q), clean(cells[1]).replace("|", "/")))
                continue
            kp = key_points(body)
            if kp and norm(title) not in seen and len(title) > 3:
                seen.add(norm(title)); items.append(("drill", clean(title), kp))

    out, total, mapping, n = [], 0, [], 0
    body = []
    for gi, (cat, label) in enumerate(c for c in CATS if any(meta[k]["category"] == c[0] and groups.get(k) for k in groups)):
        topics = sorted(k for k in groups if groups[k] and meta[k]["category"] == cat)
        count = sum(len(groups[k]) for k in topics)
        body.append(f"## {CNUM[gi]}、{label}（`{cat}`，{len(topics)} 个主题，{count} 题）\n")
        for k in topics:
            m = meta[k]
            var = f"（变体：{', '.join('`' + v + '`' for v in m['variants'])}）" if m["variants"] else ""
            body.append(f"### [`{k}`](../system-design/{k}/) — {m['title']}{var}\n")
            for kind, q, a in groups[k]:
                n += 1
                mark = {"quiz": "🟡", "drill": "🔴", "rapid": "🟢"}[kind]
                tag = {"quiz": "", "drill": "[drill] ", "rapid": "[速答] "}[kind]
                q = q if kind != "rapid" or q.endswith("?") else q + "?"
                body.append(f"{n}. {mark} {tag}{q}\n   - 要点：{a}")
            body.append("")
        mapping.append(f"| {CNUM[gi]}、{label} | `system-design`（`system-design-questions.md` 方法论 Q1–Q4 + 对应结构化题）；主题目录见 `system-design-catalog.md` 的 `{cat}` 分类 | {len(topics)} 个主题；🟡 quiz · 🔴 drill · 🟢 速答 |")
        total += count
    head = f"""# 系统设计题库（system-design 子模块提炼）— 各主题的专属 quiz、drill 与速答（{total} 题）

> **来源**：用户自有仓库 [ljluestc/system-design](https://github.com/ljluestc/system-design)（本仓库的 `system-design/` 子模块，630 个主题目录）。
> 由 `scripts/build_system_design_quiz_bank.py` **自动生成，请勿手改**；子模块更新后重新运行即可。
> **筛选口径**：约 3,900 道「每个主题都一样」的模板题（10x 流量、SQL vs NoSQL、主库宕机、缓存层设计……）被剔除，
> 只保留**主题专属**内容：`06-quiz.md` 的真题（🟡，要点取自答案首段）、`20-interview-drills.md` 中非占位的 drill（🔴）、
> 以及 drill 文件里的速答表（🟢）。变体目录（如 `google_docs` / `google-docs-k8s`）经 `resolver.json` 折叠到规范主题，重复题只保留一次。
> **版权**：用户自有，答案要点可直接引用。**用法**：「一次 10 题」的系统设计批量轮次、`quiz <主题>` 速答，或在单主题面试中做追问；
> 完整答案在对应主题目录的 `06-quiz.md` / `20-interview-drills.md`。

"""
    legend = ("\n---\n\n## 难度图例\n\n🟢 速答（一句话记忆点） · 🟡 主题 quiz 题（需解释原因与取舍） · 🔴 drill（开放式深挖，按面试阶段口述）\n\n"
              "## 与 modules 的映射\n\n| 本文件分组 | 对应 modules 模块 | 备注 |\n|---|---|---|\n" + "\n".join(mapping) + "\n")
    OUT.write_text(head + "\n".join(body) + legend, encoding="utf-8")
    kinds = {}
    print(f"wrote {OUT.relative_to(ROOT)}: {total} questions, {sum(1 for k in groups if groups[k])} topics, {len(mapping)} groups")
    return 0


if __name__ == "__main__":
    sys.exit(main())
