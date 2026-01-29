# Module 2: Foundry IQ - Create AI Agent

Large Language Models are powerful, but they **hallucinate** when asked about data they weren't trained on. **RAG (Retrieval-Augmented Generation)** solves this by grounding the model's responses in your actual documents — ensuring accurate, citable answers.

**Foundry IQ** is Microsoft's platform for building these intelligent agents. It handles:

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
