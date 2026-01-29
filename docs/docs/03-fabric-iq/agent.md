# 3.2 Create Fabric Agent

Create an agent that can query both documents and Fabric data.

## Run Create Script

```bash
python 04_create_fabric_agent.py
```

## Agent Tools

This agent has two tools:

| Tool | Purpose |
|------|---------|
| Azure AI Search | Document retrieval |
| Fabric IQ | Structured data queries |

## Expected Output

```
Creating Fabric IQ Agent...

Agent created successfully!
  ID: asst_def456uvw
  Name: fabric-search-agent
  Tools: AzureAISearch, FabricIQ
```
