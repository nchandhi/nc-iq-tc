# 4.1 Quality Evaluations

Measure agent response quality.

## Run Evaluations

```bash
python 06_run_evals.py
```

## Metrics Evaluated

| Metric | Description | Target |
|--------|-------------|--------|
| Relevance | Are responses relevant to the question? | ≥ 4.0 |
| Groundedness | Are responses grounded in content? | ≥ 4.0 |

## Expected Output

```
Starting agent evaluation...
  Agent ID: asst_def456uvw
  Data file: evals/ground_truth.jsonl

--- Summarized Metrics ---
{
  'relevance.relevance': 4.2,
  'groundedness.groundedness': 4.5
}

--- Evaluation Complete ---
```

## Interpreting Scores

| Score | Meaning |
|-------|---------|
| 5 | Excellent - Production ready |
| 4 | Good - Minor improvements possible |
| 3 | Fair - Review and improve prompts |
| 1-2 | Poor - Requires significant changes |
