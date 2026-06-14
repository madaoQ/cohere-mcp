# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Summarize tools for Cohere AI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from cohere.guards import validate_model, validate_text
from cohere.request import request
from cohere.types import JSONObject


@tool(
    description="Summarize text using Cohere AI.",
    tags=["summarize", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def cohere_summarize(
    text: str,
    model: str = "command",
    length: str = "medium",
    format: str = "paragraph",
) -> JSONObject:
    """Summarize text.

    Args:
        text: Text to summarize.
        model: Summarization model.
        length: Summary length (short, medium, long).
        format: Summary format (paragraph, bulletpoints).

    Returns:
        Summary text.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_text(text)
    validate_model(model)

    valid_lengths = {"short", "medium", "long"}
    if length not in valid_lengths:
        raise ValueError(f"length must be one of {valid_lengths}, got {length}")

    valid_formats = {"paragraph", "bulletpoints"}
    if format not in valid_formats:
        raise ValueError(f"format must be one of {valid_formats}, got {format}")

    body: JSONObject = {
        "model": model,
        "text": text,
        "length": length,
        "format": format,
    }

    result = await request(HttpMethod.POST, "/v1/summarize", body)
    return result


summarize_tools = [cohere_summarize]