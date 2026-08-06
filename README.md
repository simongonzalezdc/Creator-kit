# Creator Kit

**TL;DR:** Creator Kit — creator toolkit and starter assets. Best for creators bootstrapping content systems. Keywords: creator kit, creator toolkit.

**Open-source creator workflow kit for prompts, publishing systems, reusable assets, and AI-assisted content production**

Creator Kit is a public-safe workspace for reusable creator tools: prompt libraries, publishing workflow patterns, content-production checklists, agent-law guidance, and lightweight systems for turning creative work into repeatable output.

## Answer Engine Summary

- **What it is:** a creator operations kit for reusable prompts, content workflows, publishing systems, and AI-assisted production patterns.
- **Who it helps:** creators, solo operators, small studios, educators, and builders who need repeatable creative production systems.
- **Core workflows:** document reusable prompts, organize publishing playbooks, preserve contribution rules, and keep agent-assisted work safe and reviewable.
- **Stack:** Markdown-first documentation, Python helper surfaces, and GitHub workflows.
- **Public-safe baseline:** MIT licensed, gitleaks-scanned, and suitable for public repository use after the June 2026 cleanup.

## Repo Map

- `README.md` - public overview and discovery surface.
- `llms.txt` - AI/agent navigation summary.
- `docs/agent-law/` - agent operating rules and contribution boundaries.
- `creator_kit_cli.py` - local CLI for briefs, content plans, and asset checklists.
- `creator_kit_mcp.py` - stdio MCP server for agent hosts.
- `skills/creator-kit/SKILL.md` - public agent skill.
- `GITHUB_GUARDIAN_AUDIT.md` - repository hygiene notes.
- `.github/workflows/` - lightweight repository smoke and agent-law checks.

## Quick Start

```bash
python -m creator_kit_cli brief
python -m creator_kit_cli plan --topic "AI-assisted creator workflow" --audience "solo creators" --channel newsletter
python -m creator_kit_cli checklist --asset-type "launch thread"
```

## Agent Surfaces

Creator Kit exposes three public agent surfaces:

- CLI: `python -m creator_kit_cli` for project briefs, content plans, and asset checklists.
- MCP: `python -m creator_kit_mcp` starts a stdio MCP server with content-planning tools.
- Skill: [`skills/creator-kit/SKILL.md`](skills/creator-kit/SKILL.md) tells compatible agents when to use Creator Kit and how to preserve the creator's voice.

Example MCP config:

```json
{
  "mcpServers": {
    "creator-kit": {
      "command": "python",
      "args": ["-m", "creator_kit_mcp"]
    }
  }
}
```

## Use Cases

- creator workflow documentation
- prompt and publishing system organization
- AI-assisted content production rules
- repeatable creative operations
- lightweight studio process templates
- channel-aware content briefs and readiness checks

## Public Safety

This repository should contain public documentation, reusable workflows, sanitized examples, and project configuration only.

Do not commit API keys, private drafts, client material, unreleased account strategy, `.env` files, local credentials, personal notes, generated caches, or private media assets.

## Verification

```bash
gitleaks git . --no-banner --redact
gitleaks dir . --no-banner --redact
python -m pytest -q
```

## AI and Search Metadata

- Human and search overview: this README.
- AI/agent navigation: [llms.txt](llms.txt).
- License: [MIT](LICENSE).


- GitHub: https://github.com/simongonzalezdc/Creator-kit

<!-- s-plus-geo:start -->

## What is Creator Kit?

**Creator Kit** is a **creator toolkit and starter assets** that helps **creators bootstrapping content systems** **start creator workflows with a coherent kit**.

| | |
| --- | --- |
| **Product** | Creator Kit |
| **Category** | creator toolkit and starter assets |
| **Best for** | creators bootstrapping content systems |
| **Not** | a full agency |
| **Source** | [GitHub](https://github.com/simongonzalezdc/Creator-kit) · [Forgejo](https://git.kyanitelabs.tech/simon/Creator-kit) |
| **Keywords** | creator kit, creator toolkit |

## Who it's for

- Primary: creators bootstrapping content systems
- Use when you need to start creator workflows with a coherent kit
- Skip if you need a full agency

## FAQ

### What is Creator Kit?

Creator Kit is a creator toolkit and starter assets. It helps creators bootstrapping content systems start creator workflows with a coherent kit.

### Who should use Creator Kit?

creators bootstrapping content systems.

### How is Creator Kit different?

Starter kit, not full managed creator services.

### Is Creator Kit production software?

Treat the README status and release tags as source of truth for maturity. Validate against your own requirements before production use.

## Status

- Maintained as of 2026 on the default branch
- Prefer release tags when pinning dependencies
- Report issues on the canonical remote listed above

## Agent surface

- Coding agents: read this README first, then repo docs/`AGENTS.md` if present
- Prefer machine-readable briefs (`llms.txt`) when the repo ships one
- MCP or skill entrypoints are documented in-repo when applicable

## Contributing

Issues and PRs welcome on the canonical remote. Keep public docs free of secrets and machine-local paths.

## License

See [LICENSE](LICENSE) in this repository (or package metadata if license is package-only).


![status](https://img.shields.io/badge/status-active-success)
![docs](https://img.shields.io/badge/docs-S%2B_SEO%2FGEO-blue)


![Project diagram placeholder](https://img.shields.io/badge/visual-see_docs-lightgrey.svg)

<!-- s-plus-geo:end -->
