# Deploy Infrastructure

## Clone the Repository

```bash
git clone https://github.com/nchandhi/nc-iq-tc.git
cd nc-iq-tc
```

## Login to Azure

```bash
azd auth login
```

This opens a browser for authentication.

## Deploy Resources

```bash
azd up
```

When prompted, enter:

| Prompt | Recommended Value |
|--------|-------------------|
| Environment name | `iq-lab-yourname` |
| Azure subscription | Your subscription |
| Azure location | `eastus2` or `westus2` |

!!! warning "Wait for Completion"
    Deployment takes **5-7 minutes**. Don't proceed until you see the success message.

## Verify Deployment

You should see:

```
SUCCESS: Your application was provisioned in Azure.
```

Verify in [Azure Portal](https://portal.azure.com) that your resource group contains all resources.
