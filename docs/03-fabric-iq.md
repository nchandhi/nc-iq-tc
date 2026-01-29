# Module 3: Fabric IQ - Connect Data

**⏱️ Duration: 10 minutes**

In this module, you'll connect your AI agent to enterprise data sources using Fabric IQ.

---

## Step 3.1: Understanding Fabric IQ

**Fabric IQ** enables AI agents to query structured data in Microsoft Fabric:
- **OneLake**: Unified data lake for all your enterprise data
- **Semantic Models**: Business-friendly data definitions
- **Natural Language Queries**: Ask questions in plain English

---

## Step 3.2: Configure Fabric Connection

Update your environment with Fabric workspace details:

```bash
# Set Fabric workspace ID (get from Fabric portal URL)
azd env set FABRIC_WORKSPACE_ID "your-workspace-id"

# Set the semantic model name
azd env set FABRIC_SEMANTIC_MODEL "SalesData"
```

> 💡 **Tip**: Find your workspace ID in the Fabric portal URL:
> `https://app.fabric.microsoft.com/groups/{workspace-id}/...`

---

## Step 3.3: Create Fabric-Enabled Agent

Create an agent that can query both documents AND Fabric data:

```bash
python 04_create_fabric_agent.py
```

This agent has two tools:
1. **Azure AI Search** - For document retrieval
2. **Fabric IQ** - For structured data queries

**Expected output:**
```
Creating Fabric IQ Agent...

Agent created successfully!
  ID: asst_def456uvw
  Name: fabric-search-agent
  Tools: AzureAISearch, FabricIQ
```

---

## Step 3.4: Test Fabric Queries

Test the agent with data questions:

```bash
python 05_test_fabric_agent.py
```

**Example interactions:**
```
You: What were total sales last quarter?
Agent: Based on the SalesData model, total sales for Q4 2025 were $2.4M...

You: Which product category has the highest revenue?
Agent: Querying Fabric... Electronics leads with $890K in revenue...

You: Summarize our return policy and current return rate
Agent: [Combines document search + Fabric query]
       Policy: 30-day returns for unused items...
       Current return rate: 3.2% based on Q4 data...
```

---

## Step 3.5: View Query Traces

Check Application Insights for detailed traces:

1. Go to Azure Portal → Application Insights
2. Select **Transaction search**
3. Filter by operation name `agent-run`
4. Click any trace to see:
   - Tool calls (Search, Fabric)
   - Latency breakdown
   - Token usage

---

## ✅ Checkpoint

Before proceeding, verify:
- [ ] Fabric connection configured
- [ ] Agent can query structured data
- [ ] Traces visible in Application Insights

---

**Next:** [Module 4: Integration & Testing →](04-integration.md)

[← Back to Module 2](02-foundry-iq.md) | [Back to Home](index.md)
