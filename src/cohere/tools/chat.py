# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Chat tools for Cohere AI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from cohere.guards import validate_max_tokens, validate_message, validate_model, validate_temperature
from cohere.request import _int, _opt_str, request
from cohere.types import JSONObject


@tool(
    description="Chat with Cohere AI using natural language.",
    tags=["chat", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def cohere_chat(
    message: str,
    model: str = "command",
    conversation_id: str | None = None,
    temperature: float = 0.7,
    max_tokens: int = 500,
) -> JSONObject:
    """Chat with Cohere AI.

    Args:
        message: User message.
        model: Model to use (command, command-r, command-r-plus).
        conversation_id: Optional conversation ID for multi-turn chat.
        temperature: Sampling temperature (0.0-5.0).
        max_tokens: Maximum response length.

    Returns:
        Chat response with generated text.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_message(message)
    validate_model(model)
    validate_temperature(temperature)
    validate_max_tokens(max_tokens)

    body: JSONObject = {
        "model": model,
        "message": message,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    if conversation_id is not None:
        body["conversation_id"] = conversation_id

    result = await request(HttpMethod.POST, "/v1/chat", body)
    return result


chat_tools = [cohere_chat]