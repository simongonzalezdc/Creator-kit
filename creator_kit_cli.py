#!/usr/bin/env python3
"""Creator-kit command-line interface."""

from __future__ import annotations

import argparse
import json
from typing import Any


def project_brief() -> dict[str, Any]:
    return {
        "name": "Creator-kit",
        "summary": "Open-source creator workflow kit for prompts, publishing systems, reusable assets, and AI-assisted content production.",
        "surfaces": {
            "cli": "python -m creator_kit_cli",
            "mcp": "python -m creator_kit_mcp",
            "skill": "skills/creator-kit/SKILL.md",
        },
        "workflows": [
            "turn a raw idea into a publishable content brief",
            "plan reusable creator assets and repurposing paths",
            "check whether a draft has hook, audience, proof, and call-to-action clarity",
        ],
    }


def content_plan(args: dict[str, Any]) -> dict[str, Any]:
    topic = str(args.get("topic") or "untitled idea").strip()
    audience = str(args.get("audience") or "target audience").strip()
    channel = str(args.get("channel") or "general").strip()
    return {
        "topic": topic,
        "audience": audience,
        "channel": channel,
        "brief": f"Create a {channel} piece about {topic} for {audience}.",
        "outline": [
            "hook: name the pain, opportunity, or surprising contrast",
            "context: explain why this matters now",
            "body: give the useful steps, evidence, or example",
            "close: ask for one concrete response or next action",
        ],
        "repurposing": [
            "short post",
            "long-form outline",
            "newsletter section",
            "talking points for video",
        ],
    }


def asset_checklist(args: dict[str, Any]) -> dict[str, Any]:
    asset_type = str(args.get("asset_type") or "content asset").strip()
    return {
        "asset_type": asset_type,
        "checks": [
            "clear audience",
            "specific promise",
            "one reusable source of truth",
            "format-specific constraints",
            "proof, example, or artifact",
            "repurposing notes",
            "publishing owner and next action",
        ],
    }


def _print(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Creator-kit CLI for content workflow planning."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("brief", help="Print the Creator-kit project brief.")

    plan = subparsers.add_parser("plan", help="Create a content plan.")
    plan.add_argument("--topic", required=True)
    plan.add_argument("--audience", default="target audience")
    plan.add_argument("--channel", default="general")

    checklist = subparsers.add_parser(
        "checklist", help="Create an asset readiness checklist."
    )
    checklist.add_argument("--asset-type", default="content asset")

    args = parser.parse_args()
    if args.command == "brief":
        _print(project_brief())
    elif args.command == "plan":
        _print(content_plan(vars(args)))
    elif args.command == "checklist":
        _print(asset_checklist({"asset_type": args.asset_type}))


if __name__ == "__main__":
    main()
