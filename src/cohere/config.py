# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Cohere API configuration."""

from dedalus_mcp.auth import Connection, SecretKeys

# Cohere API base URL
COHERE_API_BASE = "https://api.cohere.ai"


def create_cohere_connection() -> Connection:
    """Create a DAuth connection to Cohere API.

    Uses Bearer token authentication.
    The API key is encrypted client-side and decrypted in the Dedalus enclave.

    Returns:
        Configured Connection for Cohere API.

    """
    return Connection(
        name="cohere",
        secrets=SecretKeys(token="COHERE_API_KEY"),
        base_url=COHERE_API_BASE,
        auth_header_format="Bearer {api_key}",
    )