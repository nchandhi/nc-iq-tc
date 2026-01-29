# 1.2 Deploy Infrastructure

## Login to Azure

```bash
azd auth login
```

This opens a browser for authentication.

## Deploy Resources

```bash
azd up
```

When prompted:

| Prompt | Value |
|--------|-------|
| Environment name | `iq-lab-yourname` |
| Azure subscription | Select your subscription |
| Azure location | `eastus2` or `westus2` |

!!! warning "Deployment Time"
    Deployment takes approximately **5-7 minutes**. Wait for completion before proceeding.

## Verify Deployment

You should see:

```
SUCCESS: Your application was provisioned in Azure.
```

## Check Azure Portal

1. Go to [Azure Portal](https://portal.azure.com)
2. Find resource group `rg-iq-lab-yourname`
3. Verify resources are created
