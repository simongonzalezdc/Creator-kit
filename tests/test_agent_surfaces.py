from creator_kit_mcp import handle_message, handle_tool_call


def test_mcp_creates_content_plan():
    result = handle_tool_call(
        "create_content_plan",
        {"topic": "AI workflow", "audience": "solo creators", "channel": "newsletter"},
    )

    assert result["topic"] == "AI workflow"
    assert "outline" in result


def test_mcp_lists_tools():
    response = handle_message({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})

    assert response is not None
    assert any(
        tool["name"] == "asset_readiness_checklist"
        for tool in response["result"]["tools"]
    )


def test_mcp_content_plan_requires_topic():
    response = handle_message(
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {"name": "create_content_plan", "arguments": {}},
        }
    )

    assert response is not None
    assert response["error"]["code"] == -32602
    assert "topic" in response["error"]["message"]


def test_mcp_content_plan_rejects_whitespace_topic():
    response = handle_message(
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {"name": "create_content_plan", "arguments": {"topic": "   "}},
        }
    )

    assert response is not None
    assert response["error"]["code"] == -32602
