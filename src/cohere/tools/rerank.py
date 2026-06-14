# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Rerank tools for Cohere AI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from cohere.guards import validate_documents, validate_model, validate_query
from cohere.request import _int, request
from cohere.types import JSONObject


@tool(
    description="Rerank documents by relevance using Cohere AI.",
    tags=["rerank", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def cohere_rerank(
    query: str,
    documents: list[str],
    model: str = "rerank-english-v3.0",
    top_n: int = 10,
) -> JSONObject:
    """Rerank documents by relevance to query.

    Args:
        query: Search query.
        documents: List of documents to rerank.
        model: Rerank model.
        top_n: Number of top results to return.

    Returns:
        Reranked results with relevance scores.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_query(query)
    validate_model(model)
    validate_documents(documents)

    if top_n < 1:
        raise ValueError(f"top_n must be at least 1, got {top_n}")

    body: JSONObject = {
        "query": query,
        "documents": documents,
        "model": model,
        "top_n": top_n,
    }

    result = await request(HttpMethod.POST, "/v1/rerank", body)
    return result


rerank_tools = [cohere_rerank]