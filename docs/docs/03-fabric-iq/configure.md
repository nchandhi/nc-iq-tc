# 3.1 Configure Connection

Set up the connection to your Fabric workspace.

## Get Workspace ID

1. Go to [Microsoft Fabric](https://app.fabric.microsoft.com)
2. Open your workspace
3. Copy the ID from the URL: `https://app.fabric.microsoft.com/groups/{workspace-id}/...`

## Set Environment Variables

```bash
azd env set FABRIC_WORKSPACE_ID "your-workspace-id"
azd env set FABRIC_SEMANTIC_MODEL "SalesData"
```

!!! info "No Fabric Workspace?"
    If you don't have a Fabric workspace, you can skip this module and proceed to Testing. The agent will still work with document search only.
