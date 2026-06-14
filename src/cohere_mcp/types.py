# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for Cohere API responses."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ChatMessage(BaseModel, frozen=True, slots=True):
    """Chat message."""

    role: str
    content: str


class ChatResponse(BaseModel, frozen=True, slots=True):
    """Chat API response."""

    message: ChatMessage | None = None
    conversation_id: str | None = None
    text: str | None = None
    generation_id: str | None = None


class EmbeddingItem(BaseModel, frozen=True, slots=True):
    """Single embedding result."""

    embedding: list[float]
    index: int | None = None


class EmbeddingResponse(BaseModel, frozen=True, slots=True):
    """Embedding API response."""

    embeddings: list[list[float]] = Field(default_factory=list)
    model: str | None = None
    embeddings_: list[EmbeddingItem] = Field(default_factory=list)


class RerankResult(BaseModel, frozen=True, slots=True):
    """Single reranked result."""

    index: int
    text: str
    score: float


class RerankResponse(BaseModel, frozen=True, slots=True):
    """Rerank API response."""

    id: str | None = None
    results: list[RerankResult] = Field(default_factory=list)
    query: str | None = None


class ClassificationLabel(BaseModel, frozen=True, slots=True):
    """Classification label."""

    label: str
    confidence: float


class ClassificationItem(BaseModel, frozen=True, slots=True):
    """Single classification result."""

    input: str
    labels: dict[str, ClassificationLabel] = Field(default_factory=dict)
    predictions: list[str] = Field(default_factory=list)


class ClassifyResponse(BaseModel, frozen=True, slots=True):
    """Classify API response."""

    classification: list[ClassificationItem] = Field(default_factory=list)


class SummarizeResponse(BaseModel, frozen=True, slots=True):
    """Summarize API response."""

    summary: str | None = None
    id: str | None = None


class ModelInfo(BaseModel, frozen=True, slots=True):
    """Cohere model info."""

    name: str
    model_type: str | None = None


# Type aliases
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]