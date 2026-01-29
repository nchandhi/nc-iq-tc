"""Interactive chat with the Fabric IQ Agent."""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
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


def get_agents_client():
    """Create AI Agents client."""
    endpoint = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
    if not endpoint:
        raise ValueError("AZURE_AI_PROJECT_ENDPOINT not set")
    
    return AgentsClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
    )


def chat_with_agent(agents_client: AgentsClient, agent_id: str):
    """Interactive chat loop."""
    thread = agents_client.threads.create()
    print(f"Thread created: {thread.id}")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit', 'q']:
            break
        
        if not user_input:
            continue
        
        agents_client.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input
        )
        
        run = agents_client.runs.create_and_process(
            thread_id=thread.id,
            agent_id=agent_id,
        )
        
        messages = agents_client.messages.list(
            thread_id=thread.id, 
            order=ListSortOrder.ASCENDING
        )
        
        for msg in messages:
            if msg.role == "assistant" and msg.text_messages:
                print(f"\nAgent: {msg.text_messages[-1].text.value}\n")
                break


def main():
    agent_id = os.environ.get("AZURE_FABRIC_AGENT_ID")
    if not agent_id:
        # Fall back to regular agent
        agent_id = os.environ.get("AZURE_AGENT_ID")
    
    if not agent_id:
        print("Error: No agent ID set. Run '04_create_fabric_agent.py' first.")
        return
    
    print(f"Connecting to agent: {agent_id}")
    agents_client = get_agents_client()
    
    chat_with_agent(agents_client, agent_id)
    print("Goodbye!")


if __name__ == "__main__":
    main()
