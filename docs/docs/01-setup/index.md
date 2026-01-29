# Module 1: Environment Setup

Before building AI solutions, you need a foundation of Azure services that work together. **Infrastructure as Code (IaC)** ensures every participant gets identical, reproducible environments — making setup fast and consistent across the team.

## What Gets Deployed

The `azd up` command provisions a complete AI development environment:

![Architecture Diagram](../images/architecture.png)

| Resource | Purpose |
|----------|---------|
| **Azure AI Services** | Hosts GPT-4o and embedding models via Foundry IQ |
| **Azure AI Search** | Vector database for semantic document retrieval |
| **Storage Account** | Stores documents and agent artifacts |
| **Application Insights** | Traces agent calls for debugging and monitoring |
