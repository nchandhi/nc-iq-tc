# Run Evaluations

## Quality Evaluation

```bash
python 06_run_evals.py
```

**Expected Output:**

```
Starting agent evaluation...
  Agent ID: asst_def456uvw
  Data file: evals/ground_truth.jsonl

--- Summarized Metrics ---
{
  'relevance.relevance': 4.2,
  'groundedness.groundedness': 4.5
}
```

### Interpreting Scores

| Score | Meaning |
|-------|---------|
| **5** | Excellent — production ready |
| **4** | Good — minor improvements possible |
| **3** | Fair — review prompts and retrieval |
| **1-2** | Poor — requires significant changes |

---

## Safety Evaluation

```bash
python 07_safety_evals.py --max_simulations 20
```

**Expected Output:**

```
Running adversarial simulation...
--- Summarized Metrics ---
{
  'safety.violence': 'Very low',
  'safety.self_harm': 'Very low',
  'safety.hate_unfairness': 'Very low'
}
```

## View in Azure AI Foundry

1. Go to [ai.azure.com](https://ai.azure.com)
2. Open your project → **Evaluation**
3. Review detailed results and drill into specific responses

!!! success "Checkpoint"
    - Quality scores should be **≥ 4.0**
    - Safety levels should show **"Very low"** risk
