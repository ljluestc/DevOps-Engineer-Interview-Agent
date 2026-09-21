#!/usr/bin/env python3
"""Verify that the interview agent fully supports the system-design corpus.

Checks the `system-design/` submodule, the generated catalog, the structured question module,
and that every agent prompt (Claude / Codex / universal / WorkBuddy) is wired to the module.

Usage:  python3 scripts/verify_system_design.py [--quiet]
Exit code 0 when every check passes, 1 otherwise.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "system-design"
CATALOG_JSON = ROOT / "modules" / "system-design" / "catalog.json"
CATALOG_MD = ROOT / "modules" / "system-design" / "system-design-catalog.md"
QUESTIONS_MD = ROOT / "modules" / "system-design" / "system-design-questions.md"
PROMPTS = ["CLAUDE.md", "AGENTS.md", "agent/UNIVERSAL.md"]
CATEGORIES = {"fundamentals", "building-blocks", "products", "ops-infra", "ai-ml",
              "os-systems", "hubs", "scaffold"}
HUB_DOCS = {
    "index": "00-index.md", "requirements": "01-requirements.md", "architecture": "02-architecture.md",
    "deep_dives": "04-deep-dives.md", "trade_offs": "05-trade-offs.md", "quiz": "06-quiz.md",
    "walkthrough": "07-walkthrough.md", "scale_slo": "11-scale-and-slo.md",
    "reliability": "16-reliability-failures.md", "observability": "18-observability-sre.md",
    "drills": "20-interview-drills.md",
}
REQUIRED_FIELDS = ["- **难度**", "- **关键词**", "- **概念速记**", "- **问题**",
                   "- **参考答案**", "- **易错点 / 面试官关注**", "- **延伸**"]
LINK_RE = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")

_question_count: int | None = None  # shared between check 6 and check 9


def has_files(d: Path) -> bool:
    return any(p.is_file() and ".git" not in p.parts for p in d.rglob("*"))


def topic_dirs(base: Path) -> set[str]:
    return {d.name for d in base.iterdir() if d.is_dir() and not d.name.startswith(".") and has_files(d)}


def broken_links(md: Path) -> list[str]:
    bad = []
    for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
        if "://" in target or target.startswith("mailto:"):
            continue
        if not (md.parent / target).exists():
            bad.append(target)
    return bad


def check_submodule() -> tuple[bool, list[str]]:
    d: list[str] = []
    if not CORPUS.is_dir() or not any(CORPUS.iterdir()):
        d.append("system-design/ is missing or empty (git submodule update --init)")
    gm = ROOT / ".gitmodules"
    text = gm.read_text() if gm.is_file() else ""
    if "path = system-design" not in text:
        d.append(".gitmodules lacks `path = system-design`")
    if "url = https://github.com/ljluestc/system-design" not in text:
        d.append(".gitmodules lacks the ljluestc/system-design url")
    return not d, d


def check_catalog_fresh() -> tuple[bool, list[str]]:
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_system_design_catalog.py"), "--check"],
                       capture_output=True, text=True)
    return r.returncode == 0, [ln for ln in (r.stdout + r.stderr).splitlines() if ln]


def load_catalog() -> dict:
    return json.loads(CATALOG_JSON.read_text(encoding="utf-8"))


def check_catalog_coverage() -> tuple[bool, list[str]]:
    d: list[str] = []
    cat = load_catalog()
    ids = [t["id"] for t in cat["topics"]]
    dup = {i for i in ids if ids.count(i) > 1}
    expected = topic_dirs(CORPUS)
    missing, extra = sorted(expected - set(ids)), sorted(set(ids) - expected)
    if dup:
        d.append(f"duplicate topic ids: {sorted(dup)}")
    if missing:
        d.append(f"corpus dirs missing from catalog ({len(missing)}): {missing}")
    if extra:
        d.append(f"catalog ids without corpus dir ({len(extra)}): {extra}")
    hub_ids = {t["id"] for t in cat["docs_hubs"]}
    exp_hubs = topic_dirs(CORPUS / "docs") if (CORPUS / "docs").is_dir() else set()
    if exp_hubs != hub_ids:
        d.append(f"docs hubs mismatch: missing={sorted(exp_hubs - hub_ids)} extra={sorted(hub_ids - exp_hubs)}")
    d.append(f"{len(ids)} topics, {len(hub_ids)} docs hubs covered")
    return len(d) == 1, d


def check_catalog_integrity() -> tuple[bool, list[str]]:
    d: list[str] = []
    cat = load_catalog()
    for t in cat["topics"] + cat["docs_hubs"]:
        p = ROOT / t["path"]
        if not p.is_dir():
            d.append(f"{t['id']}: path {t['path']} is not a directory")
        for k, flag in t["docs"].items():
            if flag and not (p / HUB_DOCS[k]).is_file():
                d.append(f"{t['id']}: flag {k} set but {HUB_DOCS[k]} missing")
    bad_cat = [t["id"] for t in cat["topics"] if t["category"] not in CATEGORIES]
    if bad_cat:
        d.append(f"unknown categories on: {bad_cat}")
    askable = sum(1 for t in cat["topics"] if t["category"] != "scaffold")
    if askable < 500:
        d.append(f"only {askable} askable topics (< 500)")
    d.append(f"{askable} askable topics")
    return len(d) == 1, d


def check_catalog_md() -> tuple[bool, list[str]]:
    if not CATALOG_MD.is_file():
        return False, ["catalog markdown missing"]
    bad = broken_links(CATALOG_MD)
    return not bad, [f"broken link: {b}" for b in bad[:20]] + ([f"... {len(bad)} total"] if len(bad) > 20 else [])


def check_questions() -> tuple[bool, list[str]]:
    global _question_count
    d: list[str] = []
    if not QUESTIONS_MD.is_file():
        return False, ["questions module missing"]
    text = QUESTIONS_MD.read_text(encoding="utf-8")
    m = re.search(r"^# 系统设计面试题（(\d+) 题）", text, re.M)
    if not m:
        d.append("H1 title does not match `# 系统设计面试题（N 题）`")
    parts = re.split(r"^### Q(\d+)\.", text, flags=re.M)
    nums = [int(n) for n in parts[1::2]]
    blocks = parts[2::2]
    n = len(nums)
    _question_count = n
    if nums != list(range(1, n + 1)):
        d.append(f"question numbering not contiguous 1..{n}: {nums}")
    if m and int(m.group(1)) != n:
        d.append(f"title says {m.group(1)} questions, found {n}")
    for q, block in zip(nums, blocks):
        body = block.split("\n---", 1)[0]
        for f in REQUIRED_FIELDS:
            if f not in body:
                d.append(f"Q{q}: missing field {f}")
        dm = re.search(r"- \*\*难度\*\*：\s*(\S)", body)
        if dm and dm.group(1) not in "🟢🟡🔴⚫":
            d.append(f"Q{q}: bad difficulty marker {dm.group(1)!r}")
        ext = re.search(r"- \*\*延伸\*\*：(.*)", body)
        if ext and "../../system-design/" not in ext.group(1):
            d.append(f"Q{q}: 延伸 has no link into ../../system-design/")
    for b in broken_links(QUESTIONS_MD):
        d.append(f"broken link: {b}")
    d.append(f"{n} questions parsed")
    return len(d) == 1, d


def check_prompts_wired() -> tuple[bool, list[str]]:
    d: list[str] = []
    for rel in PROMPTS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        switch = [ln for ln in text.splitlines() if "cloud-security / service-mesh" in ln]
        if not switch or "system-design" not in switch[0]:
            d.append(f"{rel}: switch list lacks system-design")
        if "system-design-catalog.md" not in text:
            d.append(f"{rel}: does not mention system-design-catalog.md")
    for rel in ["README.md", "modules/README.md",
                "workbuddy/ops-interview-coach/agents/ops-interview-coach.md",
                "workbuddy/ops-interview-coach/skills/ops-interview/SKILL.md",
                "workbuddy/agents/ops-interview-coach.md", "workbuddy/skills/ops-interview/SKILL.md"]:
        if "system-design" not in (ROOT / rel).read_text(encoding="utf-8"):
            d.append(f"{rel}: no mention of system-design")
    for rel in ["workbuddy/ops-interview-coach/skills/ops-interview/references/questions.md",
                "workbuddy/skills/ops-interview/references/questions.md"]:
        if not re.search(r"^## system-design", (ROOT / rel).read_text(encoding="utf-8"), re.M):
            d.append(f"{rel}: no `## system-design` section")
    return not d, d


def check_prompt_consistency() -> tuple[bool, list[str]]:
    tails = {}
    for rel in PROMPTS:
        lines = (ROOT / rel).read_text(encoding="utf-8").splitlines()
        idx = next((i for i, ln in enumerate(lines) if ln.startswith("## Knowledge base")), None)
        if idx is None:
            return False, [f"{rel}: no `## Knowledge base` heading"]
        tails[rel] = lines[idx:]
    ref = tails[PROMPTS[0]]
    for rel in PROMPTS[1:]:
        other = tails[rel]
        for i, (a, b) in enumerate(zip(ref, other)):
            if a != b:
                return False, [f"{PROMPTS[0]} vs {rel} differ at tail line {i + 1}:", f"  {a}", f"  {b}"]
        if len(ref) != len(other):
            return False, [f"{PROMPTS[0]} vs {rel}: tail length differs ({len(ref)} vs {len(other)})"]
    return True, []


def check_modules_readme() -> tuple[bool, list[str]]:
    text = (ROOT / "modules" / "README.md").read_text(encoding="utf-8")
    row = next((ln for ln in text.splitlines() if "system-design/system-design-questions.md" in ln), None)
    if row is None:
        return False, ["modules/README.md has no row for system-design/system-design-questions.md"]
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    count = next((int(c) for c in cells if c.isdigit()), None)
    if count is None:
        return False, [f"no numeric count cell in row: {row}"]
    if _question_count is not None and count != _question_count:
        return False, [f"row count {count} != questions parsed {_question_count}"]
    return True, [f"row count {count}"]


CHECKS = [
    ("submodule present", check_submodule),
    ("catalog fresh", check_catalog_fresh),
    ("catalog coverage", check_catalog_coverage),
    ("catalog integrity", check_catalog_integrity),
    ("catalog markdown links", check_catalog_md),
    ("questions module", check_questions),
    ("agent prompts wired", check_prompts_wired),
    ("prompt consistency", check_prompt_consistency),
    ("modules/README row", check_modules_readme),
]


def main() -> int:
    quiet = "--quiet" in sys.argv
    passed = 0
    for name, fn in CHECKS:
        try:
            ok, details = fn()
        except Exception as e:  # noqa: BLE001 - report any crash as a failed check
            ok, details = False, [f"exception: {e!r}"]
        passed += ok
        if ok and quiet:
            continue
        print(f"{'PASS' if ok else 'FAIL'} {name}")
        for ln in details:
            print(f"    {ln}")
    print(f"\n{passed}/{len(CHECKS)} checks passed")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
