# Module 4: Evaluations

Building an AI agent is only half the work. Before deploying to production, you need **evidence** that it:

1. **Provides accurate, relevant answers** — not hallucinations
2. **Stays safe** — resists jailbreaks and harmful content generation
3. **Meets quality standards** — consistent performance across queries

Azure AI Evaluation automates this testing with industry-standard metrics.

## Evaluation Types

| Type | What It Measures | How |
|------|------------------|-----|
| **Quality** | Relevance, groundedness, coherence | LLM-as-judge scores (1-5) |
| **Safety** | Harmful content, jailbreak resistance | Adversarial simulation |

## Quality Metrics Explained

| Metric | Question It Answers |
|--------|---------------------|
| **Relevance** | Does the response address the user's question? |
| **Groundedness** | Is the response supported by retrieved content? |
| **Coherence** | Is the response well-organized and readable? |

## Safety Testing

The adversarial simulator attempts to make your agent:

- Generate harmful or offensive content
- Leak system prompts or PII
- Bypass safety guidelines

A well-configured agent should resist these attacks.
