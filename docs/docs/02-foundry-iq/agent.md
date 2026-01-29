# Create & Test Agent

## Create the Agent

```bash
python 02_create_agent.py
```

The agent is configured with:

| Setting | Value |
|---------|-------|
| Model | GPT-4o-mini |
| Tool | Azure AI Search |
| Query Type | Vector + Semantic Hybrid |

**Output:**
```
Creating AI Search Agent...
Agent created successfully!
  ID: asst_abc123xyz
  Name: search-agent
```

## Test Interactively

```bash
python 03_test_agent.py
```

**Try these questions:**

```
You: What products does Contoso offer?
Agent: Based on the documents, Contoso offers cloud services including 
       Contoso Cloud Platform, Contoso Data Lake, and Contoso AI Services...

You: What is the return policy?
Agent: According to the Contoso policies document, products may be 
       returned within 30 days of purchase...

You: exit
```

!!! success "Checkpoint"
    Verify the agent responds with information **from your documents**, not generic knowledge.
