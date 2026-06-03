---
name: creator-kit
description: Use Creator-kit for creator workflows, content briefs, publishing systems, reusable asset planning, prompt kits, and AI-assisted content production. Trigger when an agent needs to turn an idea into a channel-aware plan or check whether a draft is ready to publish.
---

# Creator-kit

Use this skill when a task involves creator systems, content planning, reusable prompt/assets, publishing workflows, or draft readiness.

## Start Here

- Read `../../README.md` for the current public surface.
- Use the CLI for local planning: `python -m creator_kit_cli`.
- Use the MCP server when an agent host should call creator workflow tools directly: `python -m creator_kit_mcp`.

## Workflow

1. Identify the topic, audience, and channel before writing.
2. Produce a short brief first: hook, context, useful body, and close.
3. Design every asset with reuse in mind: source of truth, derivatives, owner, and next action.
4. Keep generated copy ready to edit, not over-polished into a generic voice.
5. If publishing advice depends on current platform rules or trends, verify before claiming specifics.

## CLI Examples

```bash
python -m creator_kit_cli brief
python -m creator_kit_cli plan --topic "AI-assisted creator workflow" --audience "solo creators" --channel newsletter
python -m creator_kit_cli checklist --asset-type "launch thread"
```

## MCP Setup

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

## Guardrails

- Do not invent platform policy, pricing, or performance claims from memory.
- Preserve the creator's voice; do not flatten everything into generic marketing copy.
- Separate draft text from publishing strategy when the user needs both.
