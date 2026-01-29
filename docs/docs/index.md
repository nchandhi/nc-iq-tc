---
hide:
  - navigation
  - toc
---

# Introduction

Build AI applications that combine unstructured document knowledge with structured enterprise data using knowledge bases, ontology, and natural language queries.

## The Opportunity

Organizations have valuable knowledge spread across documents (PDFs, policies, manuals) and structured systems (databases, data warehouses). By connecting these sources through AI, users can get unified answers from a single conversational interface.

## The Solution

This lab demonstrates how **Foundry IQ** and **Fabric IQ** solve this by creating an intelligent agent that:

- **Creates knowledge bases** from documents with agentic retrieval (plan, iterate, reflect)
- **Defines business ontology** to understand entities, relationships, and rules
- **Queries data** using natural language over both documents and structured data
- **Combines both** to answer complex business questions

## What You'll Build

| Component | Technology | Purpose |
|-----------|------------|---------|
| AI Agent | Azure AI Foundry | Orchestrates tools and generates responses |
| Knowledge Base | Foundry IQ | Agentic retrieval over documents |
| Business Ontology | Fabric IQ | Entities, relationships, and NL→SQL |
| Evaluation | Azure AI Evaluation | Quality and safety testing |

## Prerequisites

- Azure subscription with Contributor access
- [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)
- [Python 3.10+](https://www.python.org/downloads/)

[**Start Lab →**](01-setup/index.md)
