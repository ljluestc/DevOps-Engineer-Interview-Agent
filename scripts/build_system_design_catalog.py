#!/usr/bin/env python3
"""Generate the system-design topic catalog consumed by the interview agent.

Scans the `system-design/` submodule (github.com/ljluestc/system-design), which holds
600+ topic folders that follow a numbered 00–21 study-hub layout, and writes:

  modules/system-design/system-design-catalog.md   (agent/human readable, grouped by category)
  modules/system-design/catalog.json               (machine readable, used by verify script)

Every non-hidden, non-empty top-level directory of the submodule is assigned to exactly one
category so that the agent can serve *all* topics, not just the famous ones.

Usage:  python3 scripts/build_system_design_catalog.py [--check]
        python3 scripts/build_system_design_catalog.py --resolve "<what the candidate said>"
        --check    : do not write, exit 1 if the generated output differs from what is on disk
        --resolve  : print the canonical topic for a spoken request (brand name, Chinese, typo,
                     or any of the duplicate spellings) — the same order the agent follows
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
OUT_RES_MD = ROOT / "modules" / "system-design" / "system-design-resolver.md"
OUT_RES_JSON = ROOT / "modules" / "system-design" / "resolver.json"

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


# --------------------------------------------------------------------------------------
# Topic resolver: fold near-duplicate folders, and map what a candidate actually says
# (typos, brand names, Chinese terms, "design X" phrasings) onto a canonical topic.
# The corpus grew organically, so the same topic exists under up to eight spellings
# (url-shortener / url_shortener / url-shortening / url-shorten / tinyurl / bitly-...)
# and a few folders are outright typos (chatpgt, typehead, kuberentes, new-aggregator).
# Without this, `switch system-design <whatever the candidate said>` misses.
# --------------------------------------------------------------------------------------

# Whole tokens dropped before comparing two folder names.
NOISE_TOKENS = {
    "system", "systems", "design", "designs", "test", "tests", "educative", "grokking",
    "complete", "hub", "hubs", "detailed", "prototype", "demo", "v2", "guide",
}
# Variant stems folded together (applied per token, longest pattern first).
STEM_MAP = {
    "shortening": "shorten", "shortener": "shorten", "shorteners": "shorten",
    "crawlers": "crawler", "webcrawler": "webcrawler", "webcrawlers": "webcrawler",
    "monitoring": "monitor", "logging": "log", "logs": "log",
    "scheduling": "schedule", "scheduler": "schedule",
    "recommendation": "recommend", "recommendations": "recommend", "recommender": "recommend",
    "messaging": "message", "messages": "message", "queues": "queue",
    "typehead": "typeahead",  # corpus typo
    "chatpgt": "chatgpt",     # corpus typo
    "kuberentes": "kubernetes",  # corpus typo
    "newsfeed": "newsfeed", "new": "news",  # new-aggregator -> news-aggregator
    "aggregator": "aggregator", "aggregators": "aggregator",
    "notification": "notification", "notifications": "notification",
    "analytic": "analytics",
}

def norm_key(name: str) -> str:
    """Normalised comparison key for a folder name."""
    toks = [t for t in re.split(r"[-_\s.]+", name.lower()) if t]
    out = []
    for t in toks:
        t = STEM_MAP.get(t, t)
        if t in NOISE_TOKENS:
            continue
        out.append(t)
    return "".join(out) or name.lower()


def doc_score(t: dict) -> int:
    return sum(1 for v in t["docs"].values() if v)


def noise_penalty(name: str) -> int:
    """How far a folder name is from the plain name a candidate would say.

    At equal documentation completeness we want `blob-store`, not
    `blob-store-educative-tests`, and `dns`, not `dns_system`.
    """
    toks = [t for t in re.split(r"[-_\s.]+", name.lower()) if t]
    return sum(1 for t in toks if t in NOISE_TOKENS) + ("_" in name)


# Curated aliases: what a candidate says -> a folder id that must exist in the corpus.
# Keys are matched case-insensitively after the same normalisation as folder names, so
# "Design TinyURL!" and "tinyurl" both hit the "tinyurl" entry.
CURATED_ALIASES: dict[str, str] = {
    # brand / product phrasings
    "tinyurl": "url-shortener", "bitly": "url-shortener", "shorturl": "url-shortener",
    "pastebin": "pastebin", "dropbox": "dropbox", "googledrive": "file-storage-service",
    "onedrive": "file-storage-service", "whatsapp": "whatsapp", "messenger": "facebook-messenger-system",
    "facebookmessenger": "facebook-messenger-system", "slack": "messaging-system",
    "discord": "messaging-system", "telegram": "messaging-system",
    "twitter": "twitter", "x": "twitter", "facebook": "fb-news-feed", "instagram": "instagram",
    "tiktok": "tiktok", "douyin": "tiktok", "youtube": "youtube", "netflix": "video-streaming",
    "twitch": "twitch", "spotify": "spotify", "uber": "uber", "lyft": "uber", "didi": "uber",
    "doordash": "doordash", "ubereats": "uber-eats", "meituan": "food-delivery",
    "airbnb": "rental-search-ranking", "booking": "hotel-booking-system", "yelp": "yelp",
    "googlemaps": "google-maps", "maps": "google-maps", "googledocs": "google-docs",
    "notion": "google-docs", "figma": "google-docs", "ticketmaster": "ticketmaster",
    "stripe": "payment", "paypal": "payment", "venmo": "payment", "robinhood": "robinhood",
    "leetcode": "leetcode-online-judge", "quora": "quora", "reddit": "newsfeed",
    "craigslist": "craigslist-system", "linkedin": "linkedin-feed-ranking",
    "strava": "strava", "tinder": "tinder", "chatgpt": "chatgpt", "gmail": "email-service",
    "zoom": "live-streaming-platform", "airtag": "airtag", "alexa": "alexa",
    # building blocks by the words interviewers use
    "ratelimiter": "rate-limiter", "throttling": "rate-limiter",
    "idgenerator": "unique-id-generator", "snowflake": "unique-id-generator",
    "sequencer": "unique-id-generator", "autocomplete": "typeahead",
    "searchsuggestion": "typeahead", "searchautocomplete": "typeahead",
    "kvstore": "key-value-store", "keyvaluestore": "key-value-store",
    "objectstore": "object-storage", "blobstore": "blob-store", "s3": "s3-like-storage",
    "messagequeue": "distributed-message-queue", "kafka": "distributed-message-queue",
    "pubsub": "pubsub", "cdn": "cdn", "loadbalancer": "load-balancer", "dns": "dns",
    "webcrawler": "web-crawler-system", "searchengine": "distributed-search",
    "metrics": "metrics-monitoring-hello-interview", "monitor": "monitoring-system",
    "logsearch": "distributed-logging", "tracing": "observability",
    "leaderboard": "dream11-leaderboard", "topk": "topk", "trending": "trending-topic-system",
    "adclick": "ad-click-aggregator", "adsclick": "ad-click-aggregator",
    "distributedlock": "distributed-locking", "cronjob": "distributed-job-scheduler",
    "taskscheduler": "distributed-job-scheduler", "jobscheduler": "distributed-job-scheduler",
    "sessionstore": "session-management-system", "featureflag": "app",
    "timeseries": "time-series-database", "tsdb": "time-series-database",
    "vectordb": "vectordb", "rag": "rag-system", "llmserving": "inference-optimization",
    "flashsale": "ticketmaster", "seckill": "ticketmaster", "onlinejudge": "online-judge-system",
    "collaborativeeditor": "google-docs", "videoconferencing": "live-streaming-platform",
    "livecomments": "fb-live-comments", "proximityservice": "yelp", "nearbyfriends": "yelp",
}

# Chinese terms -> folder id (the coach must accept 中文 topic names).
ZH_ALIASES: dict[str, str] = {
    "短链": "url-shortener", "短链接": "url-shortener", "短网址": "url-shortener",
    "发号器": "unique-id-generator", "唯一id": "unique-id-generator", "分布式id": "unique-id-generator",
    "限流": "rate-limiter", "限流器": "rate-limiter", "令牌桶": "rate-limiter",
    "秒杀": "ticketmaster", "抢票": "ticketmaster", "票务": "ticketmaster",
    "信息流": "newsfeed", "朋友圈": "newsfeed", "新闻推荐": "news-feed-aggregator",
    "聊天": "messaging-system", "即时通讯": "messaging-system", "群聊": "messaging-system",
    "网盘": "file-storage-service", "文件同步": "file-storage-service", "云盘": "file-storage-service",
    "对象存储": "object-storage", "键值存储": "key-value-store", "缓存": "distributed-cache",
    "分布式缓存": "distributed-cache", "消息队列": "distributed-message-queue",
    "发布订阅": "pubsub", "定时任务": "distributed-job-scheduler", "任务调度": "distributed-job-scheduler",
    "分布式锁": "distributed-locking", "爬虫": "web-crawler-system", "搜索": "distributed-search",
    "自动补全": "typeahead", "搜索提示": "typeahead", "监控": "monitoring-system",
    "日志": "distributed-logging", "可观测性": "observability", "链路追踪": "observability",
    "网约车": "uber", "打车": "uber", "外卖": "food-delivery", "配送": "food-delivery",
    "直播": "live-streaming-platform", "弹幕": "fb-live-comments", "点赞评论": "fb-live-comments",
    "视频": "video-streaming", "短视频": "tiktok", "推荐系统": "recommendation",
    "广告点击": "ad-click-aggregator", "支付": "payment", "订单": "e-commerce",
    "电商": "e-commerce", "库存": "ticketmaster", "通知": "notification-system",
    "推送": "notification-system", "排行榜": "dream11-leaderboard", "热门话题": "trending-topic-system",
    "协同文档": "google-docs", "在线文档": "google-docs", "地图": "google-maps",
    "附近的人": "yelp", "酒店预订": "hotel-booking-system", "会议室预订": "conference-room-booking",
    "时序数据库": "time-series-database", "数据管道": "data-pipeline", "数仓": "big-data-pipeline",
    "向量检索": "vectordb", "大模型推理": "inference-optimization", "训练平台": "distributed-genai-training",
    "灾备": "disaster-recovery-system", "容灾": "disaster-recovery-system",
    "负载均衡": "load-balancer", "网关": "api-gateway",
    "会话管理": "session-management-system", "权限": "rbac", "秒级估算": "back-of-envelope",
    "一致性": "consistency-models-guide", "容量估算": "back-of-envelope",
}


def build_resolver(cat: dict) -> dict:
    """Group duplicate folders and resolve aliases. Pure function of the scan result."""
    askable = [t for t in cat["topics"] if t["category"] != "scaffold"]
    topics = {t["id"]: t for t in askable}   # aliases may only target askable topics
    groups: dict[str, list[dict]] = {}
    for t in askable:
        groups.setdefault(norm_key(t["id"]), []).append(t)
    resolved, group_rows = {}, []
    for key, members in sorted(groups.items()):
        members.sort(key=lambda t: (-doc_score(t), noise_penalty(t["id"]), -t["files"],
                                    len(t["id"]), t["id"]))
        canon = members[0]
        variants = [m["id"] for m in members[1:]]
        group_rows.append({
            "key": key, "canonical": canon["id"], "title": canon["title"],
            "category": canon["category"], "docs": doc_score(canon),
            "md_files": canon["md_files"],
            "quiz": canon["docs"]["quiz"], "drills": canon["docs"]["drills"],
            "variants": variants,
            # Thin means "little to read", not "missing the standard filenames": several topics use
            # their own numbering (airtag has 01-clarify-problem.md, 03-nfr-slos.md ...) and are
            # richly documented. Only call a topic thin when both signals are low.
            "thin": doc_score(canon) < 4 and canon["md_files"] < 6,
        })
        for m in members:
            resolved[m["id"]] = canon["id"]
    # aliases (curated + Chinese); keep only those whose target exists
    aliases, dangling = {}, []
    for src, target in list(CURATED_ALIASES.items()) + list(ZH_ALIASES.items()):
        if target in topics:
            aliases[src] = resolved.get(target, target)
        else:
            dangling.append((src, target))
    return {"groups": group_rows, "folder_to_canonical": resolved,
            "aliases": aliases, "dangling_aliases": sorted(dangling)}


def render_resolver_md(cat: dict, res: dict) -> str:
    groups, aliases = res["groups"], res["aliases"]
    dupes = [g for g in groups if g["variants"]]
    thin = [g for g in groups if g["thin"]]
    zh = {k: v for k, v in aliases.items() if any("一" <= c <= "鿿" for c in k)}
    en = {k: v for k, v in aliases.items() if k not in zh}
    out = [
        "# 系统设计主题解析器（resolver）——候选人说什么都能接上",
        "",
        "> **自动生成，请勿手改** —— 由 `scripts/build_system_design_catalog.py` 生成，"
        "`scripts/verify_system_design.py` 校验。配套目录见 "
        "[system-design-catalog.md](system-design-catalog.md)。",
        ">",
        f"> 语料是长年累积的，同一个主题最多有 **{max((len(g['variants']) + 1) for g in groups)}** 种拼法，"
        f"还有几个目录本身是错别字。本文件把 **{len(res['folder_to_canonical'])}** 个可出题目录折叠成 "
        f"**{len(groups)}** 个主题，并给出 **{len(aliases)}** 条别名（含 {len(zh)} 条中文）。",
        "",
        "## 智能体解析顺序（照这个顺序做，不要跳步）",
        "",
        "1. **别名表**：把候选人的说法（去掉「设计 / design / 一个 / a」等词、忽略大小写与连字符）"
        "在下面两张别名表里查——命中即得到规范主题目录。",
        "2. **目录名精确匹配**：再到 [catalog](system-design-catalog.md) 里按目录名查；命中后用"
        "「重复主题」表把它折叠到规范目录（变体目录里的 `06-quiz.md` 也值得读，常有不同的追问）。",
        "3. **关键词模糊匹配**：用标题与一句话摘要在 catalog 里搜关键词（英文 + 中文都试）。",
        "4. **都没命中**：**照样开面**——用 `system-design-questions.md` 的 Q1–Q4 方法论驱动"
        "（需求澄清 → 估算 → 高层设计 → 深挖 → 权衡与可运维性），并**明确告诉候选人语料里没有这个主题**，"
        "不要假装在读某份文档。",
        "5. **AWS 岗位**：若候选人面的是 AWS / 云岗，再叠加 "
        "[collections/aws-managed-services-only.md](../../collections/aws-managed-services-only.md)"
        "（195 题，其中 131–195 是 11 个经典题的 AWS-only 渲染）作为「同一道题只用托管服务怎么答」的追问层。",
        "",
        "## 一、别名 → 规范主题（英文 / 品牌 / 口语说法）",
        "",
        "| 候选人可能说 | 规范主题目录 |",
        "|---|---|",
    ]
    for k in sorted(en):
        out.append(f"| `{k}` | [`{en[k]}`](../../system-design/{en[k]}/) |")
    out += ["", "## 二、别名 → 规范主题（中文）", "",
            "> 中文候选人直接说中文题名；这张表让 `switch system-design 秒杀` 能用。", "",
            "| 中文说法 | 规范主题目录 |", "|---|---|"]
    for k in sorted(zh):
        out.append(f"| {k} | [`{zh[k]}`](../../system-design/{zh[k]}/) |")
    out += ["", f"## 三、重复主题：{len(dupes)} 组（同一题的多种拼法）", "",
            "> 规范目录是文档最全的那个；变体目录**不要当成新题**，但可以借它们的 `06-quiz.md` 做追问。", "",
            "| 规范主题 | 文档数 | 变体目录（同一题） |", "|---|---|---|"]
    for g in sorted(dupes, key=lambda g: (-len(g["variants"]), g["canonical"])):
        vs = " · ".join(f"`{v}`" for v in g["variants"])
        out.append(f"| [`{g['canonical']}`](../../system-design/{g['canonical']}/) | {g['docs']}/11 | {vs} |")
    alt = [g for g in groups if g["docs"] < 4 and g["md_files"] >= 6]
    out += ["", f"## 四、文档偏薄的主题：{len(thin)} 个（标准文档 <4 份**且** md 总数 <6）", "",
            "> 这些主题**仍然可以面**，但不要假装有完整语料：先 `ls` 该目录读实际存在的 md，"
            "再用 Q1–Q4 方法论补齐流程，并按需从同类主题（同一分类下文档齐全的那个）借追问。", "",
            "| 主题 | 分类 | 标准文档 | md 总数 | 有 quiz | 有 drills |", "|---|---|---|---|---|---|"]
    for g in sorted(thin, key=lambda g: (g["docs"], g["md_files"], g["canonical"])):
        out.append(f"| [`{g['canonical']}`](../../system-design/{g['canonical']}/) | {g['category']} | "
                   f"{g['docs']}/11 | {g['md_files']} | {'✓' if g['quiz'] else '·'} | "
                   f"{'✓' if g['drills'] else '·'} |")
    out += ["", f"### 四之二、用了**非标准编号**的主题：{len(alt)} 个（别误判成薄）", "",
            "> 这些目录缺少 `00-index.md` / `06-quiz.md` 这类标准名，但自带另一套编号"
            "（例如 `airtag/` 有 `01-clarify-problem.md`、`03-nfr-slos.md`、`13-security-privacy.md`）。"
            "**先 `ls` 目录，再决定读什么**；不要对候选人说「语料很薄」。", "",
            "| 主题 | 分类 | 标准文档 | md 总数 |", "|---|---|---|---|"]
    for g in sorted(alt, key=lambda g: (-g["md_files"], g["canonical"])):
        out.append(f"| [`{g['canonical']}`](../../system-design/{g['canonical']}/) | {g['category']} | "
                   f"{g['docs']}/11 | {g['md_files']} |")
    out.append("")
    return "\n".join(out) + "\n"


# Words to drop from a spoken topic request before matching ("design a URL shortener, please").
REQUEST_STOPWORDS = {
    "design", "designing", "designs", "a", "an", "the", "please", "system", "service",
    "interview", "question", "for", "me", "how", "would", "you", "build", "lets", "let",
    "设计", "一个", "一下", "系统", "服务", "题", "面试", "请", "帮我", "我想", "来",
}


def phrase_probes(phrase: str) -> tuple[str, list[str]]:
    """Normalised key and the whole-phrase probes used for alias lookup, in order."""
    raw = phrase.strip().lower()
    toks = [t for t in re.split(r"[^0-9a-z\u4e00-\u9fff]+", raw) if t and t not in REQUEST_STOPWORDS]
    key = norm_key("-".join(toks))
    return raw, [key, "".join(toks), raw]


def alias_redirect(res: dict, phrase: str) -> str | None:
    """The canonical topic a curated whole-phrase alias redirects to, if any."""
    canon = {g["canonical"] for g in res["groups"]}
    for probe in phrase_probes(phrase)[1]:
        tgt = res["aliases"].get(probe)
        if tgt in canon:
            return tgt
    return None


def resolve_phrase(res: dict, phrase: str) -> list[dict]:
    """Resolve what a candidate said to canonical topics.

    Precedence, most specific first — an exact folder name always beats an alias, otherwise a
    folder like `conference-room-booking` gets hijacked by the `booking` alias.
    """
    groups = {g["canonical"]: g for g in res["groups"]}
    folders = res["folder_to_canonical"]
    norm_index = {norm_key(f): c for f, c in folders.items()}
    raw = phrase.strip().lower()
    toks = [t for t in re.split(r"[^0-9a-z\u4e00-\u9fff]+", raw) if t and t not in REQUEST_STOPWORDS]
    key = norm_key("-".join(toks))
    joined = "".join(toks)

    def hit(how: str, canon: str) -> list[dict]:
        return [{"how": how, **groups[canon]}] if canon in groups else []

    # 1. whole-phrase curated alias — a deliberate redirect to the best-documented topic for
    #    this concept ("bitly" -> url-shortener), so it outranks a same-named thin folder
    redirect = alias_redirect(res, phrase)
    if redirect:
        return hit(f"alias:{redirect}", redirect)
    # 2. exact folder name (raw, then the obvious re-spellings), folded to canonical
    for probe in [raw, "-".join(toks), "_".join(toks), joined]:
        if probe in folders:
            h = hit(f"folder:{probe}", folders[probe])
            if h:
                return h
    # 3. normalised folder name — catches "dns network services", "url shortener"
    if key in norm_index:
        h = hit(f"folder~{key}", norm_index[key])
        if h:
            return h
    # 4. Chinese has no word separators, so "设计一个秒杀系统" arrives as one token: match the
    #    longest CJK alias that appears as a substring ("短链接" before "短链")
    for k in sorted((k for k in res["aliases"]
                     if any("\u4e00" <= c <= "\u9fff" for c in k) and k in raw),
                    key=len, reverse=True):
        h = hit(f"alias:{k}", res["aliases"][k])
        if h:
            return h
    # 5. a single token of the phrase is an alias ("build me a cdn thing") — deliberately after
    #    the folder steps, so `conference-room-booking` is not hijacked by the `booking` alias
    for tok in toks:
        if tok in res["aliases"]:
            h = hit(f"alias:{tok}", res["aliases"][tok])
            if h:
                return h
    # 6. keyword match on canonical id / title
    hits = [{"how": "keyword", **g} for g in res["groups"]
            if toks and all(tok in f"{g['canonical']} {g['title']}".lower() for tok in toks)]
    return hits[:8]


def cmd_resolve(phrase: str) -> int:
    if not OUT_RES_JSON.is_file():
        sys.exit("resolver.json missing — run this script with no arguments first")
    res = json.loads(OUT_RES_JSON.read_text(encoding="utf-8"))
    hits = resolve_phrase(res, phrase)
    if not hits:
        print(f"no corpus topic for {phrase!r}\n"
              "  -> run the interview from the Q1-Q4 methodology in "
              "modules/system-design/system-design-questions.md, and say the corpus has no doc for it")
        return 0
    for h in hits:
        thin = "  [THIN: read what exists, borrow probes from a sibling]" if h["thin"] else ""
        print(f"{h['canonical']}  ({h['how']}, {h['docs']}/11 docs, "
              f"quiz={'y' if h['quiz'] else 'n'} drills={'y' if h['drills'] else 'n'}){thin}")
        print(f"  path : system-design/{h['canonical']}/")
        print(f"  title: {h['title']}")
        if h["variants"]:
            print(f"  same question, extra probes in: {' '.join(h['variants'])}")
    return 0


def main() -> int:
    if "--resolve" in sys.argv:
        i = sys.argv.index("--resolve")
        phrase = " ".join(sys.argv[i + 1:]).strip()
        if not phrase:
            sys.exit("usage: build_system_design_catalog.py --resolve <what the candidate said>")
        return cmd_resolve(phrase)
    check = "--check" in sys.argv
    cat = build()
    md = render_md(cat)
    js = json.dumps(cat, ensure_ascii=False, indent=1) + "\n"
    res = build_resolver(cat)
    res_md = render_resolver_md(cat, res)
    res_js = json.dumps(res, ensure_ascii=False, indent=1) + "\n"
    if res["dangling_aliases"]:
        print("alias targets missing from the corpus (fix CURATED_ALIASES / ZH_ALIASES):", file=sys.stderr)
        for src, tgt in res["dangling_aliases"]:
            print(f"  {src} -> {tgt}", file=sys.stderr)
        return 1
    if check:
        files = [(OUT_MD, md), (OUT_JSON, js), (OUT_RES_MD, res_md), (OUT_RES_JSON, res_js)]
        stale = [f.name for f, want in files if not f.is_file() or f.read_text() != want]
        print("catalog + resolver up to date" if not stale
              else f"STALE ({', '.join(stale)}) — rerun scripts/build_system_design_catalog.py")
        return 0 if not stale else 1
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(md, encoding="utf-8")
    OUT_JSON.write_text(js, encoding="utf-8")
    OUT_RES_MD.write_text(res_md, encoding="utf-8")
    OUT_RES_JSON.write_text(res_js, encoding="utf-8")
    n = len(cat["topics"])
    by = {}
    for t in cat["topics"]:
        by[t["category"]] = by.get(t["category"], 0) + 1
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)}: {n} topics, "
          f"{len(cat['docs_hubs'])} docs hubs; by category: {by}")
    print(f"wrote {OUT_RES_MD.relative_to(ROOT)} and {OUT_RES_JSON.relative_to(ROOT)}: "
          f"{len(res['groups'])} canonical topics folded from {len(res['folder_to_canonical'])} folders, "
          f"{len(res['aliases'])} aliases, "
          f"{sum(1 for g in res['groups'] if g['thin'])} thin topics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
