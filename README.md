# Creator Kit

**Open-source creator workflow kit for prompts, publishing systems, reusable assets, and AI-assisted content production.**

Creator Kit is a Markdown-first, public-safe workspace for building repeatable creative systems. It provides reusable prompt libraries, publishing workflow patterns, content-production checklists, agent-law guidance, and Python CLI/MCP surfaces for creators, solo operators, small studios, and builders.

## What is this?

Creator Kit is a toolkit designed to turn creative work into repeatable output. It offers a suite of tools—including Python CLI and MCP interfaces—to document reusable prompts, organize publishing playbooks, and maintain agent-assisted work that is safe, reviewable, and production-ready. The repository itself serves as a baseline template for public-safe creative operations.

## Features

*   **CLI Interface (`creator_kit_cli.py`):** A local command-line tool for generating project briefs, content plans, and asset checklists.
*   **MCP Server (`creator_kit_mcp.py`):** A stdio MCP server exposing content-planning tools for integration with compatible AI agent hosts.
*   **Agent Skill Surface:** A defined skill manifest (`skills/creator-kit/SKILL.md`) that teaches AI agents how and when to use the kit while preserving the creator's voice.
*   **Markdown-First Documentation:** Core workflows, agent laws, and contribution guidelines are organized in readable, version-controlled `.md` files.
*   **Public-Safe by Design:** Includes CI guardrails, gitleaks scanning, and clear guidelines to prevent the commit of private data.
*   **Channel-Aware Planning:** Tools are designed to generate content briefs and plans tailored for specific channels (e.g., newsletter, social thread).

## Installation

**Prerequisites:** Python 3.8+

```bash
# 1. Clone the repository
git clone https://github.com/simon/Creator-kit.git
cd Creator-kit

# 2. (Recommended) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 3. Install the package in editable mode
pip install -e .
```

## Quick Start

Generate a new project brief, plan content, or create a checklist for a specific asset type.

```bash
# Generate a new creative brief
python -m creator_kit_cli brief

# Create a content plan for a specific topic and channel
python -m creator_kit_cli plan --topic "AI-assisted creator workflow" --audience "solo creators" --channel newsletter

# Get a checklist for a launch thread
python -m creator_kit_cli checklist --asset-type "launch thread"
```

## Usage

### Using the CLI
Run `python -m creator_kit_cli --help` to see all available commands and options.

### Using the MCP Server
Configure your MCP-compatible host (like Claude Desktop) to use the kit by adding this to its configuration:
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
The server exposes tools for content planning and brief generation.

### Agent Skill Integration
Refer to [`skills/creator-kit/SKILL.md`](skills/creator-kit/SKILL.md) for instructions on integrating Creator Kit as a skill in agent frameworks, ensuring agents adhere to the defined agent laws.

## Repo Map

| Path | Description |
| :--- | :--- |
| `README.md` | This public overview and discovery surface. |
| `llms.txt` | AI/agent navigation summary. |
| `docs/agent-law/` | Agent operating rules and contribution boundaries. |
| `creator_kit_cli.py` | CLI for briefs, content plans, and asset checklists. |
| `creator_kit_mcp.py` | Stdio MCP server for agent hosts. |
| `skills/creator-kit/SKILL.md` | Public agent skill definition. |
| `GITHUB_GUARDIAN_AUDIT.md` | Repository hygiene and audit notes. |
| `.github/workflows/` | CI for smoke tests and agent-law checks. |

## FAQ

**Q: Is this just for AI-related content?**
A: No. While it includes AI-assisted production patterns, Creator Kit is designed for any creator workflow—writing, design, publishing, and marketing. The tools focus on creating repeatable systems, whether you use AI or not.

**Q: What is "agent-law"?**
A: Agent-law refers to the set of operating rules, contribution boundaries, and safety guidelines defined in `docs/agent-law/`. They ensure any AI-assisted work remains safe, reviewable, and aligned with the creator's intentions.

**Q: How is this different from a regular template library?**
A: Creator Kit provides interactive surfaces (CLI/MCP) to *generate* templates and plans dynamically, rather than just storing static files. It's an operational toolkit, not just a repository of assets.

**Q: Can I use this for client work or private projects?**
A: The repository is MIT-licensed and public-safe. However, you must **never** commit private data (API keys, client material, etc.) to this repo. Use the provided guidelines in the "Public Safety" section to maintain hygiene.

## Contributing

We welcome contributions to improve Creator Kit. Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on the process, standards, and how to submit pull requests. All contributions must adhere to the agent-law principles.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for the full text.

## Public Safety & Verification

This repository is designed to be public-safe. Do not commit API keys, private drafts, client material, `.env` files, or personal notes.

You can verify the repository's hygiene:
```bash
# Run secret detection
gitleaks git . --no-banner --redact
gitleaks dir . --no-banner --redact

# Run project tests
python -m pytest -q
```

## AI and Search Metadata

*   **Human and search overview:** this README.
*   **AI/agent navigation:** [llms.txt](llms.txt).
*   **License:** [MIT](LICENSE).