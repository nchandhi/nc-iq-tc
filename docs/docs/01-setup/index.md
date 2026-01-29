# Module 1: Environment Setup

Before building AI solutions, you need a foundation of Azure services that work together. **Infrastructure as Code (IaC)** ensures every participant gets identical, reproducible environments — eliminating "works on my machine" problems and enabling rapid iteration.

## What Gets Deployed

The `azd up` command provisions a complete AI development environment:

| Resource | Purpose |
|----------|---------|
| **Azure AI Services** | Hosts GPT-4o and embedding models via Foundry IQ |
| **Azure AI Search** | Vector database for semantic document retrieval |
| **Storage Account** | Stores documents and agent artifacts |
| **Application Insights** | Traces agent calls for debugging and monitoring |

## Architecture

```
┌─────────────────────────────────────────┐
│           Azure AI Foundry              │
│  ┌─────────────┐    ┌────────────────┐  │
│  │   GPT-4o    │    │  Embeddings    │  │
│  └─────────────┘    └────────────────┘  │
└─────────────────────────────────────────┘
         │                    │
         ▼                    ▼
┌─────────────────┐   ┌─────────────────┐
│  AI Search      │   │  Storage        │
│  (Vector Index) │   │  (Documents)    │
└─────────────────┘   └─────────────────┘
```

!!! info "Cost Estimate"
    This lab costs approximately **$5-10** for a few hours. Remember to clean up when done.
