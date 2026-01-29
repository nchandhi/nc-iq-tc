"""Chat endpoints for the AI Agent."""

import os
import json
from typing import Optional
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


router = APIRouter()


class ChatMessage(BaseModel):
    """A single chat message."""
    role: str
    content: str


class ChatRequest(BaseModel):
    """Chat request payload."""
    messages: list[ChatMessage]
    conversation_id: Optional[str] = None
    stream: bool = False


class ChatResponse(BaseModel):
    """Chat response payload."""
    message: ChatMessage
    conversation_id: str
    citations: list[dict] = []


def get_project_client() -> AIProjectClient:
    """Create AI Project client."""
    endpoint = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
    if not endpoint:
        raise HTTPException(status_code=500, detail="AZURE_AI_PROJECT_ENDPOINT not configured")
    
    return AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
    )


def get_agent_id() -> str:
    """Get the configured agent ID."""
    agent_id = os.environ.get("AZURE_AGENT_ID")
    if not agent_id:
        raise HTTPException(status_code=500, detail="AZURE_AGENT_ID not configured")
    return agent_id


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Send a message to the AI agent and get a response."""
    
    client = get_project_client()
    agent_id = get_agent_id()
    
    try:
        # Create or continue thread
        if request.conversation_id:
            thread_id = request.conversation_id
        else:
            thread = client.agents.threads.create()
            thread_id = thread.id
        
        # Add user message
        user_message = request.messages[-1]
        client.agents.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_message.content,
        )
        
        # Run the agent
        run = client.agents.runs.create_and_process(
            thread_id=thread_id,
            agent_id=agent_id,
        )
        
        # Get response
        messages = client.agents.messages.list(thread_id=thread_id)
        
        # Find the latest assistant message
        assistant_message = None
        citations = []
        
        for msg in messages:
            if msg.role == "assistant":
                content = msg.content[0].text.value if msg.content else ""
                assistant_message = ChatMessage(role="assistant", content=content)
                
                # Extract citations if available
                if hasattr(msg.content[0], 'annotations'):
                    for annotation in msg.content[0].annotations:
                        if hasattr(annotation, 'file_citation'):
                            citations.append({
                                "source": annotation.file_citation.file_id,
                                "quote": annotation.text,
                            })
                break
        
        if not assistant_message:
            assistant_message = ChatMessage(role="assistant", content="I couldn't generate a response.")
        
        return ChatResponse(
            message=assistant_message,
            conversation_id=thread_id,
            citations=citations,
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """Stream a response from the AI agent."""
    
    client = get_project_client()
    agent_id = get_agent_id()
    
    async def generate():
        try:
            # Create or continue thread
            if request.conversation_id:
                thread_id = request.conversation_id
            else:
                thread = client.agents.threads.create()
                thread_id = thread.id
            
            # Add user message
            user_message = request.messages[-1]
            client.agents.messages.create(
                thread_id=thread_id,
                role="user",
                content=user_message.content,
            )
            
            # Stream the response
            with client.agents.runs.stream(
                thread_id=thread_id,
                agent_id=agent_id,
            ) as stream:
                for event in stream:
                    if hasattr(event, 'data') and hasattr(event.data, 'delta'):
                        delta = event.data.delta
                        if hasattr(delta, 'content') and delta.content:
                            for content_part in delta.content:
                                if hasattr(content_part, 'text'):
                                    yield f"data: {json.dumps({'content': content_part.text.value})}\n\n"
            
            yield f"data: {json.dumps({'conversation_id': thread_id, 'done': True})}\n\n"
            
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")


@router.get("/conversations/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Get conversation history."""
    
    client = get_project_client()
    
    try:
        messages = client.agents.messages.list(thread_id=conversation_id)
        
        history = []
        for msg in reversed(list(messages)):
            content = msg.content[0].text.value if msg.content else ""
            history.append(ChatMessage(role=msg.role, content=content))
        
        return {"conversation_id": conversation_id, "messages": history}
        
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Conversation not found: {e}")


@router.delete("/conversations/{conversation_id}")
async def delete_conversation(conversation_id: str):
    """Delete a conversation."""
    
    client = get_project_client()
    
    try:
        client.agents.threads.delete(thread_id=conversation_id)
        return {"status": "deleted", "conversation_id": conversation_id}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
