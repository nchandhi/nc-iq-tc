# Module 3: Fabric IQ - Connect Data

Documents tell part of the story, but **business decisions require data**. Sales numbers, inventory levels, customer metrics — this structured data lives in databases and warehouses, not PDFs.

**Fabric IQ** bridges this gap by letting your AI agent query Microsoft Fabric using natural language. Users ask "What were Q4 sales?" and the agent translates that to SQL, executes it, and explains the results.

## The Power of Combined Intelligence

| Question Type | Source | Example |
|---------------|--------|---------|
| Policy/Process | Documents (RAG) | "What's our return policy?" |
| Metrics/Numbers | Fabric (SQL) | "What's our return rate?" |
| Combined | Both | "Are we meeting our SLA for returns?" |

## How It Works

```
"What were total sales last quarter?"
     │
     ▼
┌─────────────┐     ┌─────────────┐
│  AI Agent   │────▶│  Fabric IQ  │
│             │     │  (NL → SQL) │
└─────────────┘     └─────────────┘
     │                    │
     │              ┌─────▼─────┐
     │              │  OneLake  │
     │              │  (Data)   │
     │              └───────────┘
     ▼
"Q4 sales totaled $2.4M, up 12% from Q3"
```

!!! info "No Fabric Workspace?"
    If you don't have Fabric access, you can skip this module. The agent will work with document search only.
