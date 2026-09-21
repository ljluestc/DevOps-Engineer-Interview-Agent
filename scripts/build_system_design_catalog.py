#!/usr/bin/env python3
"""Generate the system-design topic catalog consumed by the interview agent.

Scans the `system-design/` submodule (github.com/ljluestc/system-design), which holds
600+ topic folders that follow a numbered 00–21 study-hub layout, and writes:

  modules/system-design/system-design-catalog.md   (agent/human readable, grouped by category)
  modules/system-design/catalog.json               (machine readable, used by verify script)

Every non-hidden, non-empty top-level directory of the submodule is assigned to exactly one
category so that the agent can serve *all* topics, not just the famous ones.

Usage:  python3 scripts/build_system_design_catalog.py [--check]
        --check  : do not write, exit 1 if the generated output differs from what is on disk
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "system-design"
OUT_MD = ROOT / "modules" / "system-design" / "system-design-catalog.md"
OUT_JSON = ROOT / "modules" / "system-design" / "catalog.json"

# Standard hub documents (numbered layout used throughout the corpus).
HUB_DOCS = {
    "index": "00-index.md",
    "requirements": "01-requirements.md",
    "architecture": "02-architecture.md",
    "deep_dives": "04-deep-dives.md",
    "trade_offs": "05-trade-offs.md",
    "quiz": "06-quiz.md",
    "walkthrough": "07-walkthrough.md",
    "scale_slo": "11-scale-and-slo.md",
    "reliability": "16-reliability-failures.md",
    "observability": "18-observability-sre.md",
    "drills": "20-interview-drills.md",
}

# Ordered (regex, category-id). First match wins. Anchored on the directory name.
CATEGORY_RULES: list[tuple[str, str]] = [
    # --- engineering scaffolding / generic alias folders (kept for 100% coverage, not asked) ---
    (r"^(cmd|common|config|internal|pkg|public|pages|src|services|styles|templates|scripts|tests|"
     r"tests_generated|examples|playwright-report|prisma|docs|references|cpp|go|rust|"
     r"beautifulMention|vanilla-router|timetravel|pela|zones|maps|delivery|localservice|logs|memory|"
     r"skills|0a9700fc.*|ml-system-design)$", "scaffold"),
    # --- interview hubs / behavioural / company / language tracks ---
    (r"^(meta[-_].*|devops-sre-meta-pe|AI-interviews|bq|interview-.*|technical-assessments|"
     r"sql-interview-prep|web-security-interview|security-interview-comprehensive|coding-interview.*|"
     r"leetcode.*|blind-75-leetcode|design-leetcode|algorithms|devops-sre-(coding|interview)-prep|"
     r"devops-exercises|devops|kubernetes-interview.*|kubernetes-exercises|terraform-exercises|"
     r"ansible-exercises-complete|linux-commands-interview-hub|google_sre|study_guides|"
     r"code-implementations|cpp-.*|java-.*|go-exercises.*|golang|resume-designs|resume_replay|"
     r"devinterview.*)$", "hubs"),
    # --- fundamentals & methodology ---
    (r"^(back-of-envelope|consistency-models.*|distributed-systems-tradeoffs|system[-_]design.*|"
     r"scale-from-zero.*|non-functional-requirements|nfr-assessments|three-tier-architecture|"
     r"core-concepts|core-infrastructure|components|api-design|api|app|end-to-end|specialized-systems|"
     r"wrapping-up.*|reshaded-approach.*|modern-system-design|"
     r"(maintainability|scalability|reliability)-system-design|fault-tolerance.*|"
     r"failure-scenarios-analysis|object-oriented-design.*|caching|cache|database-types-2025|"
     r"databases|database|database-system.*|database-demo|database-module|replicated-sites|"
     r"pe-system-design|production-engineering-system-design|8-week.*)$", "fundamentals"),
    # --- AI / ML systems ---
    (r"^(rag.*|RAG|llm.*|chatgpt.*|chatpgt.*|genai.*|ml-.*|ai-.*|agent.*|agentic.*|embedding.*|"
     r"vectordb|.*recommend.*|.*-ranking.*|feed-ranking|image-captioning.*|text-to-.*|molmo.*|"
     r"mulan.*|inference-optimization|distributed-genai-training|parallelism-genai|graph-ml|"
     r"human-loop-ml|interleaving-experiments|ace[-_]causal.*|ad-?click.*|ads-.*|adtech_platform|"
     r"trigger_detection|llmops.*|document-retrieval.*|.*traffic-classifier|review-abuse|"
     r"music-listening-analytics|spotify-wrapped-system|eureka-reward-design|lending_product|"
     r"care_finder|ai-hospital-system|hello-agents|tiny-a2a|code-agent|claude-skills)$", "ai-ml"),
    # --- operations / infrastructure facing designs ---
    (r"^(monitoring.*|.*monitoring.*|monitor|metrics.*|distribute-log.*|distributed-logging.*|"
     r".*scheduler.*|scheduling|code-deployment.*|disaster-recovery.*|infra-dr-system|"
     r"kubernetes.*|kuberentes|k8s|k8s-manifests|kubectl-api-demo|helm-chart|kubetools.*|colima|"
     r"container-orchestration.*|dynamic-kubernetes-scaling|terraform-infrastructure|"
     r"ansible-.*|cloud-infra.*|incident-response-system|cybersecurity-incident-response|security|"
     r"rbac|pingdom|observability|service-debugging-lab|session-management.*|scalable-session-management|"
     r"superedge_tunnel|tengine-load-balancer|vm-communication|moon-machine-upgrade|upgrade|"
     r"firmware|dhcp-data-center|data-privacy-compliance-system|metro-build-system|viaduct|"
     r"drs-scaffold|distributed-process-monitor|health-monitoring-system.*|enterprise_monitoring|"
     r"client[-_]side.*|server-side-monitoring.*|juicefs_metadata_engine|f5_data_platform|"
     r"aviatrix-deep-dive|bank-legacy-digitalization|web-applications|intelligent-automation|"
     r"async-communication-web-service-hub|storage)$", "ops-infra"),
    # --- building blocks ---
    (r"^(rate-?limit.*|05-rate-limiter|ratelimit.*|key-value.*|key-values|.*cache.*|unique[-_]id.*|"
     r"distributed-lock.*|filelock|.*messag.*queue.*|distributed-mq|msg-queue|mq-demo|message-queues|"
     r"messaging[-_]system|communication-messaging|pub-?sub.*|cdn.*|load-?balancer.*|loadbalancer|"
     r"blob.*|object-storage|s3.*|amazon-storage|file-storage.*|filesystem|dns.*|api-gateway|"
     r"sharded-counters|shared-counters|topk|zookeeper|distributed-search.*|typeahead.*|typehead|"
     r"folder-search-api|api-search-folders|time-series.*|tsdb.*|cassandra|dynamodb|mongodb|"
     r"postgresql|redis|elastic|tidb-transaction|flink|kafka.*|big-data.*|data-pipeline|"
     r"data-infrastructure|ai-ml-data-infrastructure|notification.*|email-service|crawler|"
     r"webcrawler.*|web-crawler.*|url-.*|url_shortener|tinyurl.*|bitly.*|paste-?bin.*|"
     r"mussel-key-value-store|lru-cache|distributed-lru-cache|realtime.*|trending-topic-system|"
     r"web-analytics.*)$", "building-blocks"),
    # --- OS / Linux / systems programming ---
    (r"^(linux.*|os-.*|operating-system.*|boot_process|computer-boot-process|memory_management|"
     r"process_management|context_switching|deadlock|synchronization|ipc|disk.*|socket.*|"
     r"unix_file_system|kernel-distribution|networking-fundamentals|linux_storage_stack|"
     r"linux-opensource-projects-interview-hub)$", "os-systems"),
    # --- everything else with a product name is a classic product design ---
    (r".*", "products"),
]

CATEGORY_META = {
    "fundamentals": ("方法论与基础", "Fundamentals & methodology",
                     "面试框架、估算、一致性/权衡、通用架构模式"),
    "building-blocks": ("基础构件", "Building blocks",
                        "限流/KV/缓存/唯一 ID/分布式锁/消息队列/CDN/LB/对象存储/搜索/TSDB"),
    "products": ("经典产品设计", "Classic product designs",
                 "短链/信息流/IM/视频/打车/外卖/票务/支付/文档协同/地图……"),
    "ops-infra": ("运维与基础设施系统", "Ops & infrastructure systems",
                  "监控/日志/任务调度/发布系统/容灾/K8s 与容器编排/会话/安全合规"),
    "ai-ml": ("AI / ML 系统", "AI & ML systems",
              "RAG/LLM 服务/推荐/排序/Agent 编排/训练推理/评测"),
    "os-systems": ("操作系统与系统编程", "OS & systems programming",
                   "启动/内存/进程/同步/IPC/磁盘/Socket/文件系统"),
    "hubs": ("面试合集与公司专项", "Interview hubs & company tracks",
             "Meta PE/编码题/行为题/专项练习"),
    "scaffold": ("工程脚手架 / 泛化别名（非出题主题）", "Engineering scaffolding & generic aliases (not asked)",
                 "代码/配置目录或仅含模板化 00–21 文档的泛化别名，仅为覆盖完整性列出；候选人点名时仍可按目录内文档作答"),
}
CATEGORY_ORDER = ["fundamentals", "building-blocks", "products", "ops-infra", "ai-ml",
                  "os-systems", "hubs", "scaffold"]

TITLE_SUFFIXES = [" — System Design Walkthrough", " — Interview Hub", " — interview hub",
                  " - System Design", " — System Design"]


def classify(name: str) -> str:
    for pattern, cat in CATEGORY_RULES:
        if re.match(pattern, name):
            return cat
    return "products"


def strip_md(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\[(.+?)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def read_head(path: Path, n: int = 40) -> list[str]:
    try:
        with path.open(encoding="utf-8", errors="replace") as f:
            return [next(f) for _ in range(n)]
    except (StopIteration, OSError):
        try:
            return path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            return []


def title_and_summary(d: Path) -> tuple[str, str]:
    for cand in ("00-index.md", "README.md", "readme.md", "INDEX.md"):
        f = d / cand
        if f.is_file():
            lines = read_head(f)
            title = ""
            summary = ""
            for ln in lines:
                if not title and ln.startswith("# "):
                    title = strip_md(ln[2:])
                    for suf in TITLE_SUFFIXES:
                        if title.endswith(suf):
                            title = title[: -len(suf)]
                    continue
                if title and not summary:
                    m = re.match(r"^\*\*(Topic|Purpose|Goal)\s*:?\*\*:?\s*(.+)$", ln.strip())
                    if m:
                        summary = strip_md(m.group(2))
                        break
                    if ln.strip().startswith(">"):
                        summary = strip_md(ln.strip().lstrip("> "))
                        break
            if title:
                return title, summary[:160]
    # Fallback: humanise the directory name.
    return re.sub(r"[-_]+", " ", d.name).strip().title(), ""


def scan_topic(d: Path, rel_prefix: str = "") -> dict | None:
    if d.name.startswith(".") or not d.is_dir():
        return None
    files = [p for p in d.rglob("*") if p.is_file() and ".git" not in p.parts]
    if not files:
        return None
    md_files = [p for p in files if p.suffix.lower() == ".md"]
    docs = {k: (d / v).is_file() for k, v in HUB_DOCS.items()}
    title, summary = title_and_summary(d)
    if d.name == "docs" and not rel_prefix:
        title, summary = "docs（仓库级文档 + 二级专题枢纽，见文末）", "Repository-level docs; topic hubs are listed in the docs/ section below."
    return {
        "id": d.name,
        "path": f"system-design/{rel_prefix}{d.name}",
        "title": title,
        "summary": summary,
        "category": classify(d.name),
        "files": len(files),
        "md_files": len(md_files),
        "docs": docs,
    }


def build() -> dict:
    if not CORPUS.is_dir() or not any(CORPUS.iterdir()):
        sys.exit("system-design/ submodule is missing or empty — run: git submodule update --init")
    topics = []
    for d in sorted(CORPUS.iterdir(), key=lambda p: p.name.lower()):
        t = scan_topic(d)
        if t:
            topics.append(t)
    # Second-layer hubs under system-design/docs/<hub>/
    hubs = []
    docs_dir = CORPUS / "docs"
    if docs_dir.is_dir():
        for d in sorted(docs_dir.iterdir(), key=lambda p: p.name.lower()):
            t = scan_topic(d, rel_prefix="docs/")
            if t:
                t["category"] = "docs-hubs"
                hubs.append(t)
    return {"source": "https://github.com/ljluestc/system-design", "topics": topics, "docs_hubs": hubs}


def flag(b: bool) -> str:
    return "✓" if b else "·"


def render_md(cat: dict) -> str:
    topics, hubs = cat["topics"], cat["docs_hubs"]
    by_cat: dict[str, list[dict]] = {k: [] for k in CATEGORY_ORDER}
    for t in topics:
        by_cat[t["category"]].append(t)
    askable = [t for t in topics if t["category"] != "scaffold"]
    quiz_n = sum(1 for t in topics if t["docs"]["quiz"])
    drills_n = sum(1 for t in topics if t["docs"]["drills"])

    out: list[str] = []
    out.append("# 系统设计主题目录（system-design catalog）")
    out.append("")
    out.append("> **自动生成，请勿手改** —— 由 `scripts/build_system_design_catalog.py` 扫描 `system-design/` 子模块生成；")
    out.append("> 校验用 `scripts/verify_system_design.py`。语料来源：<https://github.com/ljluestc/system-design>。")
    out.append(">")
    out.append(f"> 共 **{len(topics)}** 个顶层主题目录（可出题主题 **{len(askable)}** 个，工程脚手架 {len(topics) - len(askable)} 个）")
    out.append(f"+ `docs/` 下 **{len(hubs)}** 个二级专题枢纽。其中 **{quiz_n}** 个主题带 `06-quiz.md`（带折叠答案的面试问答），")
    out.append(f"**{drills_n}** 个带 `20-interview-drills.md`（60 秒 pitch / 速答表 / 白板顺序 / 常见陷阱）。")
    out.append("")
    out.append("## 智能体如何使用本目录")
    out.append("")
    out.append("1. 候选人说 `switch system-design` 或 `switch system-design <主题>` 时，先在本文件里按目录名 / 标题 / 关键词定位主题目录。")
    out.append("2. 出题前**必读**该目录下的 `00-index.md`（题面与文档索引）、`01-requirements.md`（FR/NFR/规模）、`05-trade-offs.md`；")
    out.append("   追问题优先取自 `06-quiz.md`（有参考答案）与 `20-interview-drills.md`（速答表 + 常见陷阱）。")
    out.append("3. 评分依据 `modules/system-design/system-design-questions.md` 开头的「系统设计评分维度」。")
    out.append("4. 「工程脚手架」分类的目录是代码/配置，不当作面试主题；「面试合集」分类可作为行为题 / 编码题补充来源。")
    out.append("")
    out.append("文档列标记顺序：`index · quiz · drills · trade-offs · architecture`（✓ 存在 · 缺失）。")
    out.append("")

    for cid in CATEGORY_ORDER:
        items = by_cat[cid]
        zh, en, desc = CATEGORY_META[cid]
        out.append(f"## {zh} / {en}（{len(items)}）")
        out.append("")
        out.append(f"> {desc}")
        out.append("")
        if not items:
            out.append("（无）")
            out.append("")
            continue
        out.append("| 目录 | 标题 | 一句话 | 文档 | 文件数 |")
        out.append("|---|---|---|---|---|")
        for t in items:
            d = t["docs"]
            flags = " ".join(flag(d[k]) for k in ("index", "quiz", "drills", "trade_offs", "architecture"))
            summary = t["summary"].replace("|", "\\|")
            title = t["title"].replace("|", "\\|")
            out.append(f"| [`{t['id']}`]({'../../' + t['path']}/) | {title} | {summary} | {flags} | {t['files']} |")
        out.append("")

    out.append(f"## `docs/` 二级专题枢纽 / Second-layer hubs（{len(hubs)}）")
    out.append("")
    out.append("> `system-design/docs/<hub>/` 下的跨主题综述（架构 / 数据库 / 分布式 / 基础设施 / Linux / 网络 / 服务网格 / 存储……）。")
    out.append("")
    out.append("| 目录 | 标题 | 一句话 | 文档 | 文件数 |")
    out.append("|---|---|---|---|---|")
    for t in hubs:
        d = t["docs"]
        flags = " ".join(flag(d[k]) for k in ("index", "quiz", "drills", "trade_offs", "architecture"))
        out.append(f"| [`docs/{t['id']}`]({'../../' + t['path']}/) | {t['title'].replace('|', '\\|')} | "
                   f"{t['summary'].replace('|', '\\|')} | {flags} | {t['files']} |")
    out.append("")
    return "\n".join(out) + "\n"


def main() -> int:
    check = "--check" in sys.argv
    cat = build()
    md = render_md(cat)
    js = json.dumps(cat, ensure_ascii=False, indent=1) + "\n"
    if check:
        ok = OUT_MD.is_file() and OUT_JSON.is_file() and OUT_MD.read_text() == md and OUT_JSON.read_text() == js
        print("catalog up to date" if ok else "catalog is STALE — rerun scripts/build_system_design_catalog.py")
        return 0 if ok else 1
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(md, encoding="utf-8")
    OUT_JSON.write_text(js, encoding="utf-8")
    n = len(cat["topics"])
    by = {}
    for t in cat["topics"]:
        by[t["category"]] = by.get(t["category"], 0) + 1
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)}: {n} topics, "
          f"{len(cat['docs_hubs'])} docs hubs; by category: {by}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
