"""
Cohere AI MCP Server

A Type 3 DAuth MCP server for Cohere AI API.
Provides chat, embeddings, rerank, classify, and summarize tools.
"""

from .cohere import create_cohere_connection, cohere_tools

__all__ = ["create_cohere_connection", "cohere_tools"]