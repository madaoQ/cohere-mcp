# Cohere MCP Server

A Type 3 DAuth MCP server for [Cohere AI](https://cohere.ai) API. Provides chat, embeddings, reranking, classification, and summarization using Cohere's AI models.

## Features

- **Chat** — Conversational AI similar to chat completions
- **Embed** — Text embeddings with multiple input types
- **Rerank** — Rerank documents by relevance
- **Classify** — Classify text into categories
- **Summarize** — Text summarization
- **List Models** — View available Cohere models

## Authentication

This server uses **Type 3 DAuth** (Dedalus Auth) — your API key is encrypted client-side and decrypted in a secure Dedalus enclave.

### Get Your Cohere API Key

1. Go to https://cohere.ai/AI-API
2. Sign up and get an API key
3. Copy the key

## Installation

```bash
git clone https://github.com/dedalus-labs/cohere-mcp.git
cd cohere-mcp
pip install -e .
cp .env.example .env
# Edit .env and add COHERE_API_KEY
```

## Available Tools

### `cohere_chat`

Chat with Cohere AI.

```python
cohere_chat(
    message="Hello!",
    model="command",
    temperature=0.7,
    max_tokens=500,
)
```

### `cohere_embed`

Generate text embeddings.

```python
cohere_embed(
    texts=["Hello world", "This is a test"],
    model="embed-english-v3.0",
    input_type="search_document",
)
```

### `cohere_rerank`

Rerank documents by relevance.

```python
cohere_rerank(
    query="What is AI?",
    documents=["AI is great", "Python is a language"],
    model="rerank-english-v3.0",
    top_n=10,
)
```

### `cohere_classify`

Classify texts.

```python
cohere_classify(
    texts=["This is great", "This is terrible"],
    model="embed-english-v3.0",
)
```

### `cohere_summarize`

Summarize text.

```python
cohere_summarize(
    text="Long text to summarize...",
    model="command",
    length="medium",
    format="paragraph",
)
```

### `cohere_list_models`

List available Cohere models.

```python
cohere_list_models()
```

## Pricing

Cohere offers pay-per-token pricing. Check https://cohere.ai/pricing for details.

## Deploy to Dedalus

1. Push to GitHub (public repo)
2. Go to https://www.dedaluslabs.ai/dashboard
3. Add Server → Connect GitHub repo
4. Set `COHERE_API_KEY` as Required Credential
5. Deploy

## License

MIT