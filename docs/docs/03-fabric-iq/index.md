# Module 3: Fabric IQ - Connect Data

Documents tell part of the story, but **business decisions require data**. Sales numbers, inventory levels, customer metrics — this structured data lives in databases and warehouses, not PDFs.

**Fabric IQ** is a semantic intelligence platform that connects your AI agents to business data. It goes beyond simple database queries by understanding the **meaning** of your data through an **Ontology**.

## What is an Ontology?

An Ontology is the semantic foundation that helps AI understand your business:

| Component | Purpose | Example |
|-----------|---------|---------|
| **Entities** | Business objects | Products, Customers, Orders |
| **Relationships** | How entities connect | Customer → Orders → Products |
| **Rules** | Business logic | "Premium Customer = $10K+ lifetime value" |
| **Actions** | What can be queried | GetTopProducts, GetSalesSummary |

With an ontology, the AI agent doesn't just translate words to SQL — it understands your **business context**.

## The Power of Combined Intelligence

| Question Type | Source | Example |
|---------------|--------|---------|
| Policy/Process | Documents (RAG) | "What's our return policy?" |
| Metrics/Numbers | Fabric (NL→SQL) | "What's our return rate?" |
| Combined | Both | "Are we meeting our SLA for returns?" |

## How It Works

```
"What were total sales last quarter?"
     │
     ▼
┌─────────────┐     ┌─────────────┐
│  AI Agent   │────▶│  Fabric IQ  │
│             │     │  Ontology   │
└─────────────┘     └─────────────┘
     │                    │
     │              ┌─────▼─────┐
     │              │  OneLake  │
     │              │  (Data)   │
     │              └───────────┘
     ▼
"Q4 sales totaled $2.4M, up 12% from Q3"
```

The ontology tells the agent that "sales" means `SUM(TotalAmount)` from the `Orders` entity, and "last quarter" maps to a date filter.

!!! info "No Fabric Workspace?"
    If you don't have Fabric access, you can skip this module. The agent will work with document search only.
