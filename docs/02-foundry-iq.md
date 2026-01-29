# Module 2: Foundry IQ - Create AI Agent

**⏱️ Duration: 15 minutes**

In this module, you'll upload documents to Azure AI Search and create an intelligent agent using Foundry IQ.

---

## Step 2.1: Understanding Foundry IQ

**Foundry IQ** is Microsoft's platform for building enterprise AI agents. Key capabilities:
- **AI Agents**: Autonomous assistants that can use tools and data
- **RAG (Retrieval-Augmented Generation)**: Ground responses in your data
- **Observability**: Built-in tracing with Application Insights

---

## Step 2.2: Upload Documents to Search Index

Make sure you're in the `scripts` folder with your virtual environment activated.

```bash
python 01_upload_data.py
```

This script:
1. Reads PDF documents from the `data/` folder
2. Chunks text with sentence-aware boundaries
3. Generates embeddings using Azure OpenAI
4. Uploads to Azure AI Search with vector indexing

**Expected output:**
```
Found 2 PDF file(s)
Processing: contoso_products.pdf
Processing: contoso_policies.pdf
Uploading 45 chunks to search index...
Uploaded 45/45 documents
Done!
```

---

## Step 2.3: Create the AI Agent

Create an agent with Azure AI Search integration:

```bash
python 02_create_agent.py
```

This creates an agent configured with:
- **Model**: GPT-4o-mini
- **Tool**: Azure AI Search (vector + semantic hybrid search)
- **Instructions**: Helpful assistant grounded in document content

**Expected output:**
```
Creating AI Search Agent...

Agent created successfully!
  ID: asst_abc123xyz
  Name: search-agent

Saved AZURE_AGENT_ID to .env
```

---

## Step 2.4: Test the Agent

Let's verify the agent works:

```bash
python 03_test_agent.py
```

Try asking questions about your documents:
```
You: What products does Contoso offer?
Agent: Based on the documents, Contoso offers...

You: What is the return policy?
Agent: According to the Contoso policies document...

You: exit
```

---

## Step 2.5: View in Azure AI Foundry Portal

1. Go to [Azure AI Foundry](https://ai.azure.com)
2. Select your project
3. Navigate to **Agents** in the left menu
4. You should see your `search-agent` listed

---

## ✅ Checkpoint

Before proceeding, verify:
- [ ] Documents uploaded to search index
- [ ] Agent created successfully
- [ ] Agent responds to questions with grounded answers

---

**Next:** [Module 3: Fabric IQ - Connect Data →](03-fabric-iq.md)

[← Back to Module 1](01-setup.md) | [Back to Home](index.md)
