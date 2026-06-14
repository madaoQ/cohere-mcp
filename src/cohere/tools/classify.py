# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Classify tools for Cohere AI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from cohere.guards import validate_model, validate_text
from cohere.request import request
from cohere.types import JSONObject


@tool(
    description="Classify text into categories using Cohere AI.",
    tags=["classify", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def cohere_classify(
    texts: list[str],
    model: str = "embed-english-v3.0",
) -> JSONObject:
    """Classify texts.

    Args:
        texts: List of texts to classify.
        model: Classification model.

    Returns:
        Classification results with labels and confidence scores.

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
        "inputs": texts,
    }

    result = await request(HttpMethod.POST, "/v1/classify", body)
    return result


classify_tools = [cohere_classify]