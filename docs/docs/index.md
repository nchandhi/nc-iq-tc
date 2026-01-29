# Foundry IQ & Fabric IQ Lab

Build an AI-powered assistant that combines **unstructured document knowledge** with **structured enterprise data** — enabling natural language queries across your entire data estate.

## The Challenge

Organizations struggle to unlock value from data scattered across documents (PDFs, policies, manuals) and structured systems (databases, data warehouses). Traditional search fails to connect these silos, forcing users to manually hunt through multiple systems.

## The Solution

This lab demonstrates how **Foundry IQ** and **Fabric IQ** solve this by creating an intelligent agent that:

- **Understands documents** using RAG (Retrieval-Augmented Generation)
- **Queries structured data** in Microsoft Fabric using natural language
- **Combines both** to answer complex business questions

## What You'll Build

| Component | Technology | Purpose |
|-----------|------------|---------|
| AI Agent | Azure AI Foundry | Orchestrates tools and generates responses |
| Document Search | Azure AI Search | Vector + semantic search over documents |
| Data Queries | Fabric IQ | Natural language to SQL over Fabric |
| Evaluation | Azure AI Evaluation | Quality and safety testing |

## Prerequisites

- Azure subscription with Contributor access
- [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)
- [Python 3.10+](https://www.python.org/downloads/)

[**Start Lab →**](01-setup/index.md)
