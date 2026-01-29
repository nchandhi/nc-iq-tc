"""Create an AI Agent with Fabric IQ and Azure AI Search tools."""

import os
import json
from pathlib import Path
from dotenv import load_dotenv, set_key
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import AzureAISearchTool, AzureAISearchQueryType

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


def create_fabric_agent(agents_client: AgentsClient):
    """Create an agent with Fabric IQ and Search tools."""
    model = os.environ.get("AZURE_CHAT_MODEL", "gpt-4o-mini")
    search_connection_id = os.environ.get("AZURE_AI_SEARCH_CONNECTION_ID", "search-connection")
    index_name = os.environ.get("AZURE_SEARCH_INDEX_NAME", "documents")
    
    # Azure AI Search tool
    ai_search = AzureAISearchTool(
        index_connection_id=search_connection_id,
        index_name=index_name,
        query_type=AzureAISearchQueryType.VECTOR_SEMANTIC_HYBRID,
        top_k=5,
    )
    
    # Note: Fabric IQ tool would be added here when available
    # fabric_iq = FabricIQTool(workspace_id=..., semantic_model=...)
    
    agent = agents_client.create_agent(
        model=model,
        name="fabric-search-agent",
        instructions="""You are a helpful assistant that can answer questions using multiple data sources:
1. Use the search tool to find information from documents
2. For structured data questions, explain that Fabric IQ integration would query the semantic model

Always cite your sources and provide accurate information.
If you cannot find relevant information, say so clearly.""",
        tools=ai_search.definitions,
        tool_resources=ai_search.resources,
    )
    
    return agent


def save_agent_id(agent_id: str):
    """Save agent ID to .env file."""
    if env_path.exists():
        set_key(str(env_path), "AZURE_FABRIC_AGENT_ID", agent_id)
        print(f"Saved AZURE_FABRIC_AGENT_ID={agent_id} to .env")


def main():
    print("Creating Fabric IQ Agent...")
    
    agents_client = get_agents_client()
    agent = create_fabric_agent(agents_client)
    
    print(f"\nAgent created successfully!")
    print(f"  ID: {agent.id}")
    print(f"  Name: {agent.name}")
    
    save_agent_id(agent.id)
    print("\nRun '05_test_fabric_agent.py' to test this agent.")


if __name__ == "__main__":
    main()
