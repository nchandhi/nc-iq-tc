# Connect & Query Data

## Configure Fabric Connection

Get your workspace ID from the Fabric portal URL:
```
https://app.fabric.microsoft.com/groups/{workspace-id}/...
```

Set environment variables:

```bash
azd env set FABRIC_WORKSPACE_ID "your-workspace-id"
azd env set FABRIC_SEMANTIC_MODEL "SalesData"
```

## Create Fabric-Enabled Agent

```bash
python 04_create_fabric_agent.py
```

This creates an agent with **two tools**:

| Tool | Purpose |
|------|---------|
| Azure AI Search | Document retrieval |
| Fabric IQ | Structured data queries |

## Test Combined Queries

```bash
python 05_test_fabric_agent.py
```

**Example conversation:**

```
You: What were total sales last quarter?
Agent: Based on the SalesData model, total sales for Q4 were $2.4M...

You: Summarize our return policy and current return rate
Agent: Policy: 30-day returns for unused items (from documents)
       Current return rate: 3.2% (from Fabric data)
```

!!! success "Checkpoint"
    The agent should combine document knowledge with live data queries.
