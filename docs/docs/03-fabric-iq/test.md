# 3.3 Test Queries

Test the agent with both document and data questions.

## Run Test Script

```bash
python 05_test_fabric_agent.py
```

## Sample Queries

```
You: What were total sales last quarter?
Agent: Based on the SalesData model, total sales for Q4 were $2.4M...

You: Which product category has the highest revenue?
Agent: Querying Fabric... Electronics leads with $890K in revenue...

You: Summarize our return policy and current return rate
Agent: [Combines document search + Fabric query]
       Policy: 30-day returns for unused items...
       Current return rate: 3.2% based on Q4 data...
```

!!! success "Checkpoint"
    Before proceeding, verify:
    
    - [x] Fabric connection configured
    - [x] Agent can query structured data
    - [x] Agent combines document + data answers
