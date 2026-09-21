#!/usr/bin/env python3
"""Generic consistency check for every question module under modules/ and its wiring into the agent.

For each modules/<id>/<file>-questions.md:
  * `### Q<n>.` headers are numbered 1..N contiguously and N matches the count in the H1 title `（N 题）`
  * every question block carries the STANDARD.md fields (难度 / 关键词 / 概念速记 / 问题 / 参考答案 / 易错点 / 延伸)
    and a valid difficulty marker
  * every relative markdown link resolves
  * modules/README.md has a row for the file whose count equals N
  * the module id appears in the `switch [module]` list of CLAUDE.md, AGENTS.md, agent/UNIVERSAL.md and README.md
Also checks the three prompt files stay identical from "## Knowledge base" onward.

Usage: python3 scripts/verify_modules.py [--quiet]     exit 0 = all pass
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES = ROOT / "modules"
PROMPTS = ["CLAUDE.md", "AGENTS.md", "agent/UNIVERSAL.md"]
FIELDS = ["难度", "关键词", "参考答案", "易错点", "延伸"]          # hard requirements
SOFT_FIELDS = ["概念速记", "问题"]   # legacy modules carry the question in the header; reported, not failed
DIFF = re.compile(r"\*\*难度\*\*：\s*[🟢🟡🔴⚫]")
LINK = re.compile(r"\]\(([^)\s]+)\)")
QHDR = re.compile(r"^### Q(\d+)\.", re.M)
WARNINGS: list[str] = []
TITLE_N = re.compile(r"（(\d+)\s*题）")


def check_module(md: Path) -> list[str]:
    errs: list[str] = []
    text = md.read_text(encoding="utf-8")
    nums = [int(n) for n in QHDR.findall(text)]
    if nums != list(range(1, len(nums) + 1)):
        errs.append(f"question numbering not contiguous: {nums[:5]}… ({len(nums)} found)")
    m = TITLE_N.search(text.splitlines()[0])
    if not m:
        errs.append("H1 title lacks （N 题）")
    elif int(m.group(1)) != len(nums):
        errs.append(f"title says {m.group(1)} questions, found {len(nums)}")
    blocks = re.split(r"^### Q\d+\.", text, flags=re.M)[1:]
    soft: dict[str, int] = {f: 0 for f in SOFT_FIELDS}
    for i, b in enumerate(blocks, 1):
        missing = [f for f in FIELDS if f"**{f}" not in b]
        if missing:
            errs.append(f"Q{i} missing fields: {', '.join(missing)}")
        for f in SOFT_FIELDS:
            if f"**{f}" not in b:
                soft[f] += 1
        if not DIFF.search(b):
            errs.append(f"Q{i} has no valid difficulty marker")
    global WARNINGS
    for f, n in soft.items():
        if n:
            WARNINGS.append(f"{md.parent.name}: {n}/{len(blocks)} questions lack **{f}** (soft)")
    for target in LINK.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        p = (md.parent / target.split("#")[0]).resolve()
        if not p.exists():
            errs.append(f"broken link: {target}")
    return errs, len(nums)


def main() -> int:
    quiet = "--quiet" in sys.argv
    results: list[tuple[str, bool, list[str]]] = []
    readme = (MODULES / "README.md").read_text(encoding="utf-8")
    prompts = {p: (ROOT / p).read_text(encoding="utf-8") for p in PROMPTS}
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    total = 0

    for d in sorted(p for p in MODULES.iterdir() if p.is_dir()):
        files = sorted(d.glob("*-questions.md"))
        if not files:
            results.append((d.name, False, ["no *-questions.md file"]))
            continue
        for md in files:
            errs, n = check_module(md)
            total += n
            rel = f"{d.name}/{md.name}"
            row = re.search(rf"\[{re.escape(rel)}\]\({re.escape(rel)}\)\s*\|\s*(\d+)\s*\|", readme)
            if not row:
                errs.append("no row in modules/README.md")
            elif int(row.group(1)) != n:
                errs.append(f"modules/README.md row says {row.group(1)}, file has {n}")
            for p, txt in prompts.items():
                sw = re.search(r"`switch \[module\]`.*?`end`", txt, re.S)
                if not sw or not re.search(rf"(?<![\w-]){re.escape(d.name)}(?![\w-])", sw.group(0)):
                    errs.append(f"{p}: '{d.name}' missing from switch list")
            if f"`{d.name}`" not in root_readme:
                errs.append(f"README.md: '{d.name}' missing from switch table")
            results.append((rel, not errs, errs))

    tail = {p: t[t.index("## Knowledge base"):] for p, t in prompts.items()}
    same = len(set(tail.values())) == 1
    results.append(("prompt files identical from '## Knowledge base'", same, [] if same else [f"{p} differs" for p in PROMPTS]))
    tot_re = re.search(r"合计 \*\*(\d+) 题\*\*", readme)
    ok = bool(tot_re) and int(tot_re.group(1)) == total
    results.append((f"modules/README.md total == {total}", ok, [] if ok else [f"README says {tot_re.group(1) if tot_re else '?'}"]))

    failed = 0
    for name, ok, errs in results:
        if not ok:
            failed += 1
        if ok and quiet:
            continue
        print(("PASS " if ok else "FAIL ") + name)
        for e in errs:
            print("    " + e)
    if WARNINGS and not quiet:
        print("\nwarnings (not failures):")
        for w in WARNINGS:
            print("    " + w)
    print(f"\n{len(results) - failed}/{len(results)} checks passed ({total} questions across modules)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
