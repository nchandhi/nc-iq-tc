# Module 4: Integration & Testing

**⏱️ Duration: 10 minutes**

In this module, you'll run evaluations to test the quality and safety of your AI agent.

---

## Step 4.1: Quality Evaluations

Run evaluations to measure agent response quality:

```bash
python 06_run_evals.py
```

This evaluates:
- **Relevance**: Are responses relevant to the question?
- **Groundedness**: Are responses grounded in retrieved content?
- **Coherence**: Are responses well-structured?

**Expected output:**
```
Starting agent evaluation...
  Agent ID: asst_def456uvw
  Data file: evals/ground_truth.jsonl
  Evaluators: relevance, groundedness

--- Summarized Metrics ---
{
  'relevance.relevance': 4.2,
  'groundedness.groundedness': 4.5
}

--- Evaluation Complete ---
Results saved to: evals/results.jsonl
```

---

## Step 4.2: Understanding Evaluation Results

| Metric | Score Range | Your Target |
|--------|-------------|-------------|
| Relevance | 1-5 | ≥ 4.0 |
| Groundedness | 1-5 | ≥ 4.0 |
| Coherence | 1-5 | ≥ 4.0 |

**Interpreting scores:**
- **5**: Excellent - Production ready
- **4**: Good - Minor improvements possible
- **3**: Fair - Review and improve prompts
- **1-2**: Poor - Requires significant changes

---

## Step 4.3: Safety Evaluations

Run adversarial safety testing:

```bash
python 07_safety_evals.py --max_simulations 20
```

This uses an adversarial simulator to test:
- Harmful content generation
- Jailbreak resistance
- PII handling

**Expected output:**
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

---

## Step 4.4: View Results in AI Foundry

1. Go to [Azure AI Foundry](https://ai.azure.com)
2. Select your project
3. Navigate to **Evaluation** in the left menu
4. View detailed results and drill into specific responses

---

## Step 4.5: Iterate and Improve

Based on evaluation results, you can:

**Improve Relevance:**
```python
# Update agent instructions in 04_create_fabric_agent.py
instructions = """You are a helpful assistant. 
ALWAYS use the search tool before answering.
If you cannot find relevant information, say so clearly.
"""
```

**Improve Groundedness:**
```python
# Add citation requirements
instructions = """...
ALWAYS cite your sources with [Source: document_name].
Do not make claims without supporting evidence.
"""
```

---

## ✅ Checkpoint

Before proceeding, verify:
- [ ] Quality evaluations completed with scores ≥ 4.0
- [ ] Safety evaluations show "Very low" risk levels
- [ ] Results visible in AI Foundry portal

---

**Next:** [Module 5: Cleanup →](05-cleanup.md)

[← Back to Module 3](03-fabric-iq.md) | [Back to Home](index.md)
