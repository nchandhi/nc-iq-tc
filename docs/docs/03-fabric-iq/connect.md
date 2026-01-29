# Connect & Query Data

## Step 1: Create the Ontology

First, define your business ontology — the semantic model that helps AI understand your data:

```bash
python 04a_create_ontology.py
```

This creates `data/contoso_ontology.json` with:

- **Entities**: Products, Customers, Orders, OrderLines
- **Relationships**: Customer → Orders → Products
- **Business Rules**: Premium Customer, Gross Margin, Low Stock
- **Actions**: GetTopProducts, GetSalesSummary, etc.

Review the output to see how the ontology maps business concepts to data.

## Step 2: Configure Fabric Connection

Get your workspace ID from the Fabric portal URL:
```
https://app.fabric.microsoft.com/groups/{workspace-id}/...
```

Set environment variables:

```bash
azd env set FABRIC_WORKSPACE_ID "your-workspace-id"
azd env set FABRIC_SEMANTIC_MODEL "SalesData"
```

## Step 3: Create Fabric-Enabled Agent

```bash
python 04_create_fabric_agent.py
```

This creates an agent with **two tools**:

| Tool | Purpose |
|------|---------|
| Azure AI Search | Document retrieval |
| Fabric IQ | Structured data queries via ontology |

## Step 4: Test Combined Queries

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
