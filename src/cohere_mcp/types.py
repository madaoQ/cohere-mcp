# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for Cohere API responses.

These are declared for reference / future use. The current tools return the
raw JSON body (`JSONObject`) so the model definitions are loaded only as
documentation, but they must still be import-safe at server startup.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


# Reusable config: immutable, slotted — matches the previous intent.
_FROZEN_SLOT = ConfigDict(frozen=True, slots=True)


class ChatMessage(BaseModel):
    """Chat message."""

    model_config = _FROZEN_SLOT

    role: str
    content: str


class ChatResponse(BaseModel):
    """Chat API response."""

    model_config = _FROZEN_SLOT

    message: ChatMessage | None = None
    conversation_id: str | None = None
    text: str | None = None
    generation_id: str | None = None


class EmbeddingItem(BaseModel):
    """Single embedding result."""

    model_config = _FROZEN_SLOT

    embedding: list[float]
    index: int | None = None


class EmbeddingResponse(BaseModel):
    """Embedding API response."""

    model_config = _FROZEN_SLOT

    embeddings: list[list[float]] = Field(default_factory=list)
    model: str | None = None
    embeddings_: list[EmbeddingItem] = Field(default_factory=list)


class RerankResult(BaseModel):
    """Single reranked result."""

    model_config = _FROZEN_SLOT

    index: int
    text: str
    score: float


class RerankResponse(BaseModel):
    """Rerank API response."""

    model_config = _FROZEN_SLOT

    id: str | None = None
    results: list[RerankResult] = Field(default_factory=list)
    query: str | None = None


class ClassificationLabel(BaseModel):
    """Classification label."""

    model_config = _FROZEN_SLOT

    label: str
    confidence: float


class ClassificationItem(BaseModel):
    """Single classification result."""

    model_config = _FROZEN_SLOT

    input: str
    labels: dict[str, ClassificationLabel] = Field(default_factory=dict)
    predictions: list[str] = Field(default_factory=list)


class ClassifyResponse(BaseModel):
    """Classify API response."""

    model_config = _FROZEN_SLOT

    classification: list[ClassificationItem] = Field(default_factory=list)


class SummarizeResponse(BaseModel):
    """Summarize API response."""

    model_config = _FROZEN_SLOT

    summary: str | None = None
    id: str | None = None


class ModelInfo(BaseModel):
    """Cohere model info."""

    model_config = _FROZEN_SLOT

    name: str
    model_type: str | None = None


# Type aliases
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]
