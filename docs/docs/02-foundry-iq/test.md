# 2.3 Test Agent

Test the agent interactively.

## Run Test Script

```bash
python 03_test_agent.py
```

## Sample Conversation

```
You: What products does Contoso offer?
Agent: Based on the documents, Contoso offers cloud services 
       including Contoso Cloud Platform, Contoso Data Lake, 
       and Contoso AI Services...

You: What is the return policy?
Agent: According to the Contoso policies document, products 
       may be returned within 30 days of purchase...

You: exit
Goodbye!
```

## View in Azure AI Foundry

1. Go to [Azure AI Foundry](https://ai.azure.com)
2. Select your project
3. Navigate to **Agents**
4. Find `search-agent`

!!! success "Checkpoint"
    Before proceeding, verify:
    
    - [x] Documents uploaded to search index
    - [x] Agent created successfully  
    - [x] Agent responds with grounded answers
