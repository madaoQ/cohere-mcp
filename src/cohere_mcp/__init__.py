# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Cohere AI MCP server for Dedalus.

Provides chat, embeddings, reranking, classification, and summarization using Cohere AI.
Credentials provided by clients at runtime via DAuth token exchange.
"""

from __future__ import annotations

from cohere_mcp.config import create_cohere_connection
from cohere_mcp.tools import cohere_tools

__all__ = ["create_cohere_connection", "cohere_tools"]