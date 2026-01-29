# Module 4: Evaluations

Building an AI agent is the first step. Before deploying to production, you want **confidence** that it:

1. **Provides accurate, relevant answers** — grounded in your data
2. **Maintains appropriate boundaries** — responds professionally to all inputs
3. **Meets quality standards** — delivers consistent performance across queries

Azure AI Evaluation automates this validation with industry-standard metrics.

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

The adversarial simulator validates that your agent:

- Maintains professional, helpful responses
- Protects system configuration and user privacy
- Follows content guidelines consistently

A well-configured agent handles challenging inputs gracefully.
