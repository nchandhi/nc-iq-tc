# Run the Application

## Start the API

1. Navigate to the API folder:
```bash
cd src/api
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
copy .env.sample .env
```

Edit `.env` with your values:
```
AZURE_AI_PROJECT_ENDPOINT=<your-endpoint>
AZURE_AGENT_ID=<your-agent-id>
```

5. Start the API server:
```bash
python app.py
```

The API runs at `http://localhost:8000`

## Start the Frontend

1. Open a new terminal and navigate to the frontend:
```bash
cd src/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment (optional):
```bash
copy .env.sample .env
```

4. Start the development server:
```bash
npm start
```

The frontend opens at `http://localhost:3000`

## Test the Application

1. Open `http://localhost:3000` in your browser
2. Type a question like: "What is the return policy?"
3. The agent will search your knowledge base and respond with citations

!!! success "Checkpoint"
    You should see a chat interface where you can ask questions and receive answers from your AI agent.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/api/chat` | POST | Send message, get response |
| `/api/chat/stream` | POST | Stream response |
| `/api/conversations/{id}` | GET | Get conversation history |
| `/api/conversations/{id}` | DELETE | Delete conversation |

## Troubleshooting

**API won't start:**
- Check that `AZURE_AI_PROJECT_ENDPOINT` is set correctly
- Verify you're logged in with `az login`

**Frontend can't connect to API:**
- Ensure the API is running on port 8000
- Check CORS settings if deploying to different domains

**Agent returns errors:**
- Verify `AZURE_AGENT_ID` matches an existing agent
- Check that the agent was created with the correct tools
