[← Module 4](04-integration) · [Home](index)

# Module 5: Cleanup

⏱️ **5 minutes** · Delete Azure resources to avoid charges

---

## Step 5.1: Delete Azure Resources

To avoid ongoing charges, delete all resources:

```bash
azd down
```

When prompted, confirm the deletion:
```
? Total resources to delete: 8, are you sure you want to continue? (y/N) y
```

**Expected output:**
```
Deleting all resources and deployed code on Azure (azd down)

  Deleted: Azure AI Services
  Deleted: Azure AI Search  
  Deleted: Storage Account
  Deleted: Application Insights
  Deleted: Log Analytics Workspace
  Deleted: Resource Group

SUCCESS: Your application was removed from Azure.
```

---

## Step 5.2: Verify Deletion

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to **Resource groups**
3. Confirm your lab resource group no longer exists

> ⚠️ **Note**: Some resources may take a few minutes to fully delete.

---

## Step 5.3: Clean Local Environment (Optional)

Remove local files if desired:

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment
rm -rf scripts/.venv

# Remove azd environment
azd env delete <your-env-name>
```

---

## 🎉 Congratulations!

You've successfully completed the Foundry IQ & Fabric IQ Lab!

### What You Accomplished

✅ Deployed Azure AI infrastructure with IaC  
✅ Created a RAG-enabled AI agent with Foundry IQ  
✅ Connected enterprise data with Fabric IQ  
✅ Ran quality and safety evaluations  

---

## 📚 Continue Learning

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [Build AI Agents with Azure](https://learn.microsoft.com/azure/ai-services/agents/)
- [Microsoft Fabric IQ](https://learn.microsoft.com/fabric/)
- [Responsible AI Practices](https://www.microsoft.com/ai/responsible-ai)

---

## 🙋 Feedback

We'd love your feedback on this lab!

- **GitHub Issues**: [Report issues or suggestions](https://github.com/nchandhi/nc-iq-tc/issues)
- **Questions**: Ask your presenter or reach out on Teams

---

**Thank you for participating!** 🚀

---

[← Module 4](04-integration) · [Home](index)
