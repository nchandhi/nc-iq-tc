# Module 5: Deploy Application

Now that you have a working AI agent, let's deploy it as a full application with a **Python API** backend and **React** frontend.

## Application Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   React App     │────▶│   Python API    │────▶│   AI Agent      │
│   (Frontend)    │◀────│   (FastAPI)     │◀────│   (Foundry IQ)  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
     Port 3000              Port 8000
```

## What's Included

| Component | Technology | Location |
|-----------|------------|----------|
| **API** | Python FastAPI | `src/api/` |
| **Frontend** | React + TypeScript | `src/frontend/` |
| **UI Library** | Fluent UI React | Chat interface |

## Features

- **Chat interface** with message history
- **Streaming responses** for real-time feedback
- **Citation display** showing document sources
- **Conversation management** (create, view, delete)
