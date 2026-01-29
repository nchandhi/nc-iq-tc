# 4.2 Safety Evaluations

Run adversarial safety testing.

## Run Safety Evaluation

```bash
python 07_safety_evals.py --max_simulations 20
```

## What This Tests

- Harmful content generation
- Jailbreak resistance  
- PII handling

## Expected Output

```
Running adversarial simulation with 20 max simulations...
Saved 18 valid outputs

Starting safety evaluation...
--- Summarized Metrics ---
{
  'safety.violence': 'Very low',
  'safety.self_harm': 'Very low',
  'safety.hate_unfairness': 'Very low'
}
```

## View in Azure AI Foundry

1. Go to [Azure AI Foundry](https://ai.azure.com)
2. Select your project
3. Navigate to **Evaluation**
4. View detailed results

!!! success "Checkpoint"
    Before proceeding, verify:
    
    - [x] Quality scores ≥ 4.0
    - [x] Safety levels show "Very low" risk
    - [x] Results visible in AI Foundry portal
