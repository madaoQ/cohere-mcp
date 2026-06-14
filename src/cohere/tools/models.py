# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Model listing tools for Cohere AI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from cohere.request import request
from cohere.types import JSONObject


@tool(
    description="List available Cohere AI models.",
    tags=["models", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def cohere_list_models() -> JSONObject:
    """List available Cohere models.

    Returns:
        List of available models with their IDs and configurations.

    Raises:
        RuntimeError: If the API request fails.

    """
    result = await request(HttpMethod.GET, "/v1/models")
    return result


model_tools = [cohere_list_models]