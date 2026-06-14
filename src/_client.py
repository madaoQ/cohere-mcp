# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Direct API testing client for Cohere MCP.

This module is used for local testing without going through the MCP server.
"""

from __future__ import annotations

import asyncio
import os

import httpx
from dotenv import load_dotenv

load_dotenv()


async def test_chat() -> None:
    """Test chat endpoint."""
    print("Testing cohere_chat...")

    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        print("Error: COHERE_API_KEY not found in environment")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    body = {
        "model": "command",
        "message": "Hello, how are you?",
        "temperature": 0.7,
        "max_tokens": 50,
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.cohere.ai/v1/chat",
            headers=headers,
            json=body,
            timeout=30,
        )

    if resp.status_code == 200:
        data = resp.json()
        print(f"✓ Chat successful")
        print(f"  Response: {data.get('text', 'N/A')[:100]}")
    else:
        print(f"✗ Error {resp.status_code}: {resp.text[:200]}")


async def test_embed() -> None:
    """Test embed endpoint."""
    print("\nTesting cohere_embed...")

    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        print("Error: COHERE_API_KEY not found")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    body = {
        "model": "embed-english-v3.0",
        "texts": ["Hello world", "This is a test"],
        "input_type": "search_document",
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.cohere.ai/v1/embed",
            headers=headers,
            json=body,
            timeout=30,
        )

    if resp.status_code == 200:
        data = resp.json()
        print(f"✓ Embed successful")
        embeddings = data.get("embeddings", [])
        if embeddings:
            print(f"  Got {len(embeddings)} embeddings, dim={len(embeddings[0])}")
    else:
        print(f"✗ Error {resp.status_code}: {resp.text[:200]}")


async def main() -> None:
    """Run all direct API tests."""
    print("=" * 50)
    print("Cohere Direct API Tests")
    print("=" * 50)
    print()

    await test_chat()
    await test_embed()

    print()
    print("=" * 50)
    print("Tests completed!")


if __name__ == "__main__":
    asyncio.run(main())