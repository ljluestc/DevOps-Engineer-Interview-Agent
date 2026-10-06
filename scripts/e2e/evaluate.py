#!/usr/bin/env python3
"""Evaluate headless interview sessions: did the agent read the corpus and ask exactly one scoped question?"""
import json
import re
import sys
from pathlib import Path

E2E = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent / "out")
CATALOG = "system-design-catalog.md"
CJK = re.compile(r"[一-鿿]")

EXPECT = {  # name -> substring expected among read paths (topic folder), or None
    "fund_boe": "system-design/back-of-envelope/",
    "fund_consistency": "system-design/consistency-models-guide/",
    "bb_kv": "system-design/key-value-store/",
    "bb_mq": "system-design/distributed-message-queue/",
    "bb_cdn": "system-design/cdn/",
    "bb_typeahead": "system-design/typeahead/",
    "prod_whatsapp": "system-design/whatsapp",   # any whatsapp* folder
    "prod_newsfeed": "system-design/newsfeed/",
    "prod_uber": "system-design/uber/",
    "prod_ticketmaster": "system-design/ticketmaster/",
    "prod_googledocs": "system-design/google-docs/",
    "ops_monitoring_zh": "monitoring",          # any monitoring* folder
    "ops_logging": "system-design/distributed-logging/",
    "ops_scheduler": "system-design/distributed-job-scheduler/",
    "ops_deploy": "system-design/code-deployment/",
    "ops_dr": "system-design/disaster-recovery-system-design/",
    "ai_rag": "system-design/rag",          # rag-system/ or RAG/
    "ai_llm": "system-design/chatgpt-system-design/",
    "os_boot": "system-design/linux-boot-process/",
    "hub_meta": "system-design/meta-pe-interview/",
    "fallback_parking": None,                   # topic absent: must consult catalog/questions, then still ask
    "free_pick": "system-design/",              # any topic folder
    "explain_hashing": None,                    # concept explanation: no question required
    "zh_named": "url-short",
    "arxiv_attention": "mcp__arxiv__",        # must call the arXiv MCP tools
    "mcp_k8s": "mcp__kubernetes__",
    "mcp_tf": "mcp__terraform__",
    "mcp_c7": "mcp__context7__",
    "mcp_search": "mcp__fetch__",
    "mcp_docker": "mcp__docker__",
    "ai_eng": "modules/ai-engineering/",
    "fde_case": "modules/fde/fde-questions.md",
    "fde_zh": "modules/fde/fde-questions.md",                    # 短链服务 -> url-shortener*/tinyurl*
    "rate_limiter": "system-design/rate-limiter/",
    "k8s_web_gateway": "collections/k8s-web-archive.md",   # collection-backed rounds (added 2026-09-20)
    "sec_kubehound": "collections/k8s-web-archive.md",
    "mesh_istio_api": "collections/k8s-web-archive.md",
    "quiz_instagram_zh": "instagram",                       # system-design/instagram* or the collection's Instagram group
    "homelab_dr_zh": "collections/k8s-web-archive.md",
    "veeramalla_amazon": "collections/veeramalla-devops-interview-guide.md",
    "rag_crash": "collections/k8s-web-archive.md",
    "infer_gateway": "collections/k8s-web-archive.md",
    "sec_rbacpolice": "collections/k8s-web-archive.md",
    "quiz_flashsale_zh": "collections/k8s-web-archive.md",
    "mcp_protocol": "collections/k8s-web-archive.md",
    "es_ops": "collections/k8s-web-archive.md",
    "quiz_distcache_zh": "collections/k8s-web-archive.md",  # HelloInterview distributed-cache group (2026-10-03)
    "sd_quizbank10": "collections/system-design-quiz-bank.md",  # 10-at-a-time from the submodule quiz bank (2026-10-06)
    "sd_batch10": "collections/system-design-exercises-and-notes.md",  # 10-at-a-time system-design round (2026-10-06)
    "acc_extension_choice": "collections/awesome-claude-code.md",   # awesome-claude-code ecosystem rounds (added 2026-09-21)
    "acc_hook_guardrail": "collections/awesome-claude-code.md",
    "acc_cost_zh": "collections/awesome-claude-code.md",
    "aws_managed_backup": "collections/aws-managed-services-only.md",   # AWS-only migration rounds (added 2026-09-26)
    "aws_managed_obs": "collections/aws-managed-services-only.md",
    "aws_managed_gpu_zh": "collections/aws-managed-services-only.md",
    "aws_sd_ticketing": "collections/aws-managed-services-only.md",
    "aws_sd_shortener_zh": "collections/aws-managed-services-only.md",
    "sd_resolve_typo": "system-design/chatgpt/",          # resolver rounds (added 2026-09-26)
    "sd_resolve_zh": "system-design/ticketmaster/",
    "sd_resolve_thin": "modules/system-design/system-design-resolver.md",
}
ZH = {"ops_monitoring_zh", "zh_named", "fde_zh", "quiz_instagram_zh", "homelab_dr_zh", "quiz_flashsale_zh", "aws_managed_gpu_zh", "aws_sd_shortener_zh", "sd_resolve_zh"}
NO_QUESTION_OK = {"explain_hashing", "arxiv_attention", "mcp_tf", "mcp_c7", "mcp_search", "mcp_docker"}


def load(name):
    p = E2E / f"{name}.jsonl"
    err = (E2E / f"{name}.err").read_text() if (E2E / f"{name}.err").exists() else ""
    exit_ok = "exit=0" in err
    reads, texts, final, turns = [], [], "", 0
    if not p.exists():
        return exit_ok, reads, texts, final, turns, err
    for ln in p.read_text().splitlines():
        try:
            ev = json.loads(ln)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant":
            turns += 1
            for c in ev["message"].get("content", []):
                if c.get("type") == "tool_use":
                    reads.append(c.get("name", "") + " " + json.dumps(c.get("input"), ensure_ascii=False))
                elif c.get("type") == "text":
                    texts.append(c["text"])
        if ev.get("type") == "result":
            final = ev.get("result", "") or ""
    return exit_ok, reads, texts, final, turns, err


rows, failures = [], 0
for name in sorted(n for n in EXPECT if (E2E / f"{n}.jsonl").exists() or (E2E / f"{n}.err").exists()):
    exit_ok, reads, texts, final, turns, err = load(name)
    joined = "\n".join(reads)
    corpus_reads = [r for r in reads if "system-design/" in r or "modules/" in r or "collections/" in r or "mcp__" in r]
    exp = EXPECT[name]
    topic_ok = True if exp is None else (exp in joined)
    catalog_ok = CATALOG in joined or "system-design-questions.md" in joined
    asks = ("?" in final or "？" in final or re.search(r"(?i)walk me through|estimate|describe|please|tell me|请|说说|讲讲", final)) or name in NO_QUESTION_OK
    lang_ok = bool(CJK.search(final)) if name in ZH else True
    single = final.count("**Question") <= 1 and final.lower().count("question 2") == 0
    nonempty = len(final.strip()) > 200
    problems = []
    if not exit_ok: problems.append("exit!=0")
    if not nonempty: problems.append("empty/short output")
    if not corpus_reads and not (name == "fallback_parking" and catalog_ok): problems.append("no corpus read")
    if not topic_ok: problems.append(f"topic folder not read (want {exp})")
    if not asks: problems.append("no question asked")
    if not lang_ok: problems.append("wrong language")
    if not single: problems.append("multiple questions")
    if name == "fallback_parking" and not catalog_ok: problems.append("fallback did not consult catalog/questions")
    ok = not problems
    failures += 0 if ok else 1
    rows.append((name, "PASS" if ok else "FAIL", turns, len(corpus_reads), len(final), "; ".join(problems)))

print(f"{'session':22s} {'result':6s} {'turns':>5s} {'corpus':>6s} {'chars':>6s}  problems")
for r in rows:
    print(f"{r[0]:22s} {r[1]:6s} {r[2]:5d} {r[3]:6d} {r[4]:6d}  {r[5]}")
print(f"\n{len(rows) - failures}/{len(rows)} sessions passed")
sys.exit(1 if failures else 0)
