# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Embedding tools for Cohere AI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from cohere_mcp.guards import validate_model, validate_text
from cohere_mcp.request import request
from cohere_mcp.types import JSONObject


@tool(
    description="Generate text embeddings using Cohere AI.",
    tags=["embed", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def cohere_embed(
    texts: list[str],
    model: str = "embed-english-v3.0",
    input_type: str = "search_document",
) -> JSONObject:
    """Generate embeddings for text.

    Args:
        texts: List of texts to embed.
        model: Embedding model.
        input_type: Type of input (search_document, search_query, classification, clustering).

    Returns:
        Embeddings vectors.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_model(model)

    if not texts:
        raise ValueError("Texts list cannot be empty")
    for i, text in enumerate(texts):
        validate_text(text)

    body: JSONObject = {
        "model": model,
        "texts": texts,
        "input_type": input_type,
    }

    result = await request(HttpMethod.POST, "/v1/embed", body)
    return result


embed_tools = [cohere_embed]