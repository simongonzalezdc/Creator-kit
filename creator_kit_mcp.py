#!/usr/bin/env python3
"""Creator-kit stdio MCP server."""

from __future__ import annotations

import json
import sys
from typing import Any

from creator_kit_cli import asset_checklist, content_plan, project_brief

PROTOCOL_VERSION = "2024-11-05"

TOOLS = {
    "creator_kit_project_brief": {
        "description": "Return Creator-kit identity, surfaces, and workflow summary.",
        "handler": lambda _args: project_brief(),
        "inputSchema": {"type": "object", "properties": {}},
    },
    "create_content_plan": {
        "description": "Create a reusable content plan from topic, audience, and channel.",
        "handler": content_plan,
        "inputSchema": {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "audience": {"type": "string"},
                "channel": {"type": "string"},
            },
            "required": ["topic"],
        },
    },
    "asset_readiness_checklist": {
        "description": "Return a creator asset readiness checklist.",
        "handler": asset_checklist,
        "inputSchema": {
            "type": "object",
            "properties": {"asset_type": {"type": "string"}},
        },
    },
}


def handle_tool_call(
    name: str, arguments: dict[str, Any] | None = None
) -> dict[str, Any]:
    if name not in TOOLS:
        raise ValueError(f"Unknown tool: {name}")
    return TOOLS[name]["handler"](arguments or {})


def _tool_list() -> list[dict[str, Any]]:
    return [
        {
            "name": name,
            "description": spec["description"],
            "inputSchema": spec["inputSchema"],
        }
        for name, spec in TOOLS.items()
    ]


def _response(message_id: Any, result: dict[str, Any]) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "result": result}


def _error(message_id: Any, code: int, message: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": message_id,
        "error": {"code": code, "message": message},
    }


def handle_message(message: dict[str, Any]) -> dict[str, Any] | None:
    method = message.get("method")
    message_id = message.get("id")
    params = message.get("params") or {}
    if message_id is None:
        return None
    if method == "initialize":
        return _response(
            message_id,
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "creator-kit", "version": "0.1.0"},
            },
        )
    if method == "tools/list":
        return _response(message_id, {"tools": _tool_list()})
    if method == "tools/call":
        try:
            result = handle_tool_call(
                params.get("name", ""), params.get("arguments") or {}
            )
            return _response(
                message_id,
                {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]},
            )
        except ValueError as exc:
            return _error(message_id, -32602, str(exc))
    return _error(message_id, -32601, f"Unsupported method: {method}")


def main() -> None:
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            reply = handle_message(json.loads(line))
        except json.JSONDecodeError as exc:
            reply = _error(None, -32700, f"Invalid JSON: {exc}")
        if reply is not None:
            sys.stdout.write(json.dumps(reply) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
