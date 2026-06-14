# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Tool registry for cohere-mcp.

Modules:
  chat     -- cohere_chat
  embed    -- cohere_embed
  rerank   -- cohere_rerank
  classify -- cohere_classify
  summarize -- cohere_summarize
  models   -- cohere_list_models
"""

from __future__ import annotations

from cohere.tools.chat import chat_tools
from cohere.tools.classify import classify_tools
from cohere.tools.embed import embed_tools
from cohere.tools.models import model_tools
from cohere.tools.rerank import rerank_tools
from cohere.tools.summarize import summarize_tools

cohere_tools = [
    *chat_tools,
    *embed_tools,
    *rerank_tools,
    *classify_tools,
    *summarize_tools,
    *model_tools,
]