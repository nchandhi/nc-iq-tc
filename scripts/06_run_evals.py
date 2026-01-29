"""Run quality evaluations on the AI Agent."""

import os
import json
import contextlib
import multiprocessing
from pathlib import Path
from typing import TypedDict
from pprint import pprint

import pandas as pd
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.evaluation import evaluate
from azure.ai.evaluation import RelevanceEvaluator, GroundednessEvaluator
from azure.ai.evaluation import AzureOpenAIModelConfiguration
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import ListSortOrder

# Load environment from azd
azure_dir = Path(__file__).parent.parent / ".azure"
env_name = os.environ.get("AZURE_ENV_NAME", "")
if not env_name and (azure_dir / "config.json").exists():
    with open(azure_dir / "config.json") as f:
        config = json.load(f)
        env_name = config.get("defaultEnvironment", "")

env_path = azure_dir / env_name / ".env"
if env_path.exists():
    load_dotenv(env_path)


class AgentResponse(TypedDict):
    response: str
    context: str


_agents_client = None


def get_agents_client():
    """Get or create agents client."""
    global _agents_client
    if _agents_client is None:
        endpoint = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
        _agents_client = AgentsClient(
            endpoint=endpoint,
            credential=DefaultAzureCredential(),
        )
    return _agents_client


def evaluate_agent(question: str) -> AgentResponse:
    """Call agent and return response for evaluation."""
    agents_client = get_agents_client()
    agent_id = os.environ.get("AZURE_AGENT_ID")
    
    if not agent_id:
        return AgentResponse(response="Error: AZURE_AGENT_ID not set", context="")
    
    try:
        thread = agents_client.threads.create()
        
        agents_client.messages.create(
            thread_id=thread.id,
            role="user",
            content=question
        )
        
        run = agents_client.runs.create_and_process(
            thread_id=thread.id,
            agent_id=agent_id,
        )
        
        messages = agents_client.messages.list(
            thread_id=thread.id, 
            order=ListSortOrder.ASCENDING
        )
        
        response_text = ""
        context_text = ""
        
        for msg in messages:
            if msg.role == "assistant" and msg.text_messages:
                response_text = msg.text_messages[-1].text.value
                if hasattr(msg.text_messages[-1].text, 'annotations'):
                    citations = msg.text_messages[-1].text.annotations
                    context_parts = [str(c) for c in citations] if citations else []
                    context_text = "\n".join(context_parts)
        
        return AgentResponse(response=response_text, context=context_text)
        
    except Exception as e:
        print(f"Error calling agent: {e}")
        return AgentResponse(response=f"Error: {str(e)}", context="")


if __name__ == "__main__":
    with contextlib.suppress(RuntimeError):
        multiprocessing.set_start_method("spawn", force=True)
    
    agent_id = os.environ.get("AZURE_AGENT_ID")
    if not agent_id:
        print("Error: AZURE_AGENT_ID not set. Run 02_create_agent.py first.")
        exit(1)
    
    azure_ai_project = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
    if not azure_ai_project:
        print("Error: AZURE_AI_PROJECT_ENDPOINT not set")
        exit(1)
    
    model_config = AzureOpenAIModelConfiguration(
        azure_endpoint=os.environ.get("AZURE_AI_ENDPOINT"),
        azure_deployment=os.environ.get("AZURE_CHAT_MODEL", "gpt-4o-mini"),
        api_version="2024-08-01-preview",
    )
    
    relevance_eval = RelevanceEvaluator(model_config)
    groundedness_eval = GroundednessEvaluator(model_config)
    
    data_path = Path(__file__).parent.parent / "evals" / "ground_truth.jsonl"
    output_path = Path(__file__).parent.parent / "evals" / "results.jsonl"
    
    if not data_path.exists():
        print(f"Error: Data file not found at {data_path}")
        print("Creating sample evaluation data...")
        
        data_path.parent.mkdir(exist_ok=True)
        sample_data = [
            {"question": "What products are available?", "truth": "Product information from documents"},
            {"question": "What is the return policy?", "truth": "Return policy details"},
        ]
        with open(data_path, "w") as f:
            for item in sample_data:
                f.write(json.dumps(item) + "\n")
    
    print(f"\nStarting agent evaluation...")
    print(f"  Agent ID: {agent_id}")
    print(f"  Data file: {data_path}")
    
    result = evaluate(
        data=str(data_path),
        target=evaluate_agent,
        evaluation_name="evaluate_agent",
        evaluators={
            "relevance": relevance_eval,
            "groundedness": groundedness_eval,
        },
        evaluator_config={
            "relevance": {
                "column_mapping": {
                    "query": "${data.question}",
                    "response": "${target.response}"
                }
            },
            "groundedness": {
                "column_mapping": {
                    "query": "${data.question}",
                    "response": "${target.response}",
                    "context": "${data.truth}"
                }
            }
        },
        azure_ai_project=azure_ai_project,
        output_path=str(output_path),
    )
    
    tabular_result = pd.DataFrame(result.get("rows"))
    
    print("\n" + "=" * 50)
    print("--- Summarized Metrics ---")
    pprint(result["metrics"])
    print("\n--- Results Preview ---")
    print(tabular_result.head())
    print("\n--- Evaluation Complete ---")
    print(f"Results saved to: {output_path}")
    
    if "studio_url" in result:
        print(f"\nView results in AI Foundry:")
        print(f"  {result['studio_url']}")
    
    print("=" * 50)
