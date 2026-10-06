#!/usr/bin/env bash
# Headless end-to-end test of the system-design interview mode.
# Runs every row of matrix.tsv (name <TAB> model <TAB> prompt) as a `claude -p` session from the repo root,
# then scores the transcripts with evaluate.py (did the agent read the corpus, ask one scoped question, right language?).
#   usage: scripts/e2e/run_matrix.sh [parallelism] [name-regex]   (default 6, all rows; needs the `claude` CLI and API access)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(cd "$HERE/../.." && pwd)"; OUT="$HERE/out"; P="${1:-6}"; FILTER="${2:-.*}"
mkdir -p "$OUT"; [ "$FILTER" = ".*" ] && rm -f "$OUT"/*.jsonl "$OUT"/*.err
run_one() {  # name model prompt — prompt goes on stdin because --allowedTools is variadic
  local name=$1 model=$2 prompt=$3
  ( cd "$ROOT" && printf '%s' "$prompt" | timeout 420 claude -p --model "$model" --max-turns 15 --verbose --output-format stream-json \
      --allowedTools "Read" "Glob" "Grep" "Bash(ls:*)" "Bash(cat:*)" "Bash(head:*)" "Bash(sed:*)" "Bash(grep:*)" "Bash(find:*)" "Bash(wc:*)" "mcp__arxiv__*" "mcp__duckduckgo__*" "mcp__fetch__*" "mcp__kubernetes__*" "mcp__terraform__*" "mcp__context7__*" "mcp__docker__*" \
      > "$OUT/$name.jsonl" 2> "$OUT/$name.err"; echo "exit=$?" >> "$OUT/$name.err" )
}
export -f run_one; export ROOT OUT
start=$(date +%s)
grep -v '^#' "$HERE/matrix.tsv" | grep -E "^($FILTER)	" | while IFS=$'\t' read -r name model prompt; do printf '%s\0%s\0%s\0' "$name" "$model" "$prompt"; done \
  | xargs -0 -n3 -P "$P" bash -c 'run_one "$0" "$1" "$2"'
echo "matrix finished in $(( $(date +%s) - start ))s"
python3 "$HERE/evaluate.py" "$OUT"
