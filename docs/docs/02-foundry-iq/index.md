# Module 2: Foundry IQ - Create AI Agent

Large Language Models excel at reasoning and language, and they perform best when grounded in **your actual data**. **RAG (Retrieval-Augmented Generation)** connects the model to your documents — enabling AI applications that provide accurate, citable answers based on real content.

**Foundry IQ** is Microsoft's platform for building these intelligent AI applications. It handles:

- **Tool orchestration** — agents decide when to search, query, or reason
- **Context management** — conversation history and retrieved content
- **Enterprise security** — Azure AD, RBAC, and data residency

## How It Works

```
User Question
     │
     ▼
┌─────────────┐     ┌─────────────┐
│  AI Agent   │────▶│  AI Search  │
│  (GPT-4o)   │◀────│  (Vectors)  │
└─────────────┘     └─────────────┘
     │
     ▼
Grounded Answer + Citations
```

1. User asks a question
2. Agent searches documents using vector similarity
3. Relevant chunks are passed to GPT-4o as context
4. Model generates answer grounded in retrieved content

## What You'll Do

1. **Upload documents** to Azure AI Search with embeddings
2. **Create an agent** configured with the search tool
3. **Test interactively** to verify grounded responses
