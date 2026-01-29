# Module 2: Foundry IQ - Create AI Agent

Large Language Models excel at reasoning and language, and they perform best when grounded in **your actual data**. **Foundry IQ** is Azure AI Foundry's unified knowledge layer that enables agents to access enterprise knowledge through intelligent retrieval.

## Key Capabilities

| Feature | Description |
|---------|-------------|
| **Knowledge Bases** | Automatic indexing and vectorization of your documents |
| **Agentic Retrieval** | AI-driven search with planning, iteration, and reflection |
| **Enterprise Security** | Built-in Entra ID authentication and Purview integration |
| **Multi-format Support** | PDFs, Word, PowerPoint, and unstructured text |

## How Agentic Retrieval Works

```
User Question
     │
     ▼
┌─────────────┐     ┌─────────────┐
│  AI Agent   │────▶│ Knowledge   │
│  (GPT-4o)   │◀────│    Base     │
└─────────────┘     └─────────────┘
     │                    │
     │              Planning &
     │              Iteration
     ▼
Grounded Answer + Citations
```

Unlike simple vector search, **agentic retrieval** enables the agent to:

1. **Plan** — decompose complex questions into sub-queries
2. **Iterate** — refine searches based on initial results
3. **Reflect** — evaluate answer quality before responding

## What You'll Do

1. **Upload documents** to create a knowledge base with automatic vectorization
2. **Create an agent** configured with the knowledge base tool
3. **Test interactively** to verify grounded, citable responses
