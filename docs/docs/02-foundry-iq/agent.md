# 2.2 Create Agent

Create an AI agent with Azure AI Search integration.

## Run Create Script

```bash
python 02_create_agent.py
```

## Agent Configuration

The agent is created with:

| Setting | Value |
|---------|-------|
| Model | GPT-4o-mini |
| Tool | Azure AI Search |
| Query Type | Vector + Semantic Hybrid |

## Expected Output

```
Creating AI Search Agent...

Agent created successfully!
  ID: asst_abc123xyz
  Name: search-agent

Saved AZURE_AGENT_ID to .env
```

!!! tip "Agent ID"
    The agent ID is automatically saved to your `.env` file for use in subsequent scripts.
