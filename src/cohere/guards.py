# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Input validation for Cohere API parameters."""

from __future__ import annotations

import re


# Cohere model names: alphanumeric, hyphens, slashes
_MODEL_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_/-]*$")


def validate_model(model: str) -> None:
    """Validate a Cohere model name."""
    if not model or not _MODEL_RE.match(model):
        msg = f"Invalid model name: {model!r}"
        raise ValueError(msg)


def validate_temperature(temperature: float) -> None:
    """Validate temperature parameter."""
    if not 0.0 <= temperature <= 5.0:
        msg = f"Temperature must be between 0.0 and 5.0, got {temperature}"
        raise ValueError(msg)


def validate_max_tokens(max_tokens: int) -> None:
    """Validate max_tokens parameter."""
    if max_tokens < 1:
        msg = f"max_tokens must be at least 1, got {max_tokens}"
        raise ValueError(msg)


def validate_message(message: str) -> None:
    """Validate chat message."""
    if not message or not message.strip():
        msg = "Message cannot be empty"
        raise ValueError(msg)


def validate_text(text: str) -> None:
    """Validate text input."""
    if not text or not text.strip():
        msg = "Text cannot be empty"
        raise ValueError(msg)


def validate_documents(documents: list[str]) -> None:
    """Validate document list for reranking."""
    if not documents:
        msg = "Documents list cannot be empty"
        raise ValueError(msg)
    for i, doc in enumerate(documents):
        if not doc or not doc.strip():
            msg = f"Document at index {i} is empty"
            raise ValueError(msg)


def validate_query(query: str) -> None:
    """Validate search query."""
    if not query or not query.strip():
        msg = "Query cannot be empty"
        raise ValueError(msg)