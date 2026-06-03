#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "README.md"
  "AGENTS.md"
  "CLAUDE.md"
  "CONTRIBUTING.md"
  "LICENSE"
  "llms.txt"
  "docs/agent-law/empower-orchestrator.md"
  ".github/pull_request_template.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

grep -q "EMPOWER_ORCHESTRATOR:START" AGENTS.md
grep -q "EMPOWER_ORCHESTRATOR:START" CLAUDE.md
grep -q "EMPOWER_ORCHESTRATOR:START" .github/pull_request_template.md
grep -q "four-question blast-radius check" docs/agent-law/empower-orchestrator.md

echo "Creator Kit structural tests passed."
