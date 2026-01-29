import React, { useState, useRef, useEffect } from 'react';
import {
  Button,
  Input,
  Card,
  Spinner,
  Text,
  makeStyles,
  tokens,
} from '@fluentui/react-components';
import { Send24Regular, Bot24Regular, Person24Regular } from '@fluentui/react-icons';
import ReactMarkdown from 'react-markdown';

const useStyles = makeStyles({
  container: {
    display: 'flex',
    flexDirection: 'column',
    height: '100vh',
    maxWidth: '900px',
    margin: '0 auto',
    padding: '20px',
  },
  header: {
    textAlign: 'center',
    marginBottom: '20px',
  },
  title: {
    fontSize: '24px',
    fontWeight: 'bold',
    color: tokens.colorBrandForeground1,
  },
  subtitle: {
    fontSize: '14px',
    color: tokens.colorNeutralForeground3,
  },
  chatContainer: {
    flex: 1,
    overflowY: 'auto',
    marginBottom: '20px',
    padding: '10px',
  },
  message: {
    display: 'flex',
    gap: '12px',
    marginBottom: '16px',
  },
  userMessage: {
    flexDirection: 'row-reverse',
  },
  messageContent: {
    maxWidth: '70%',
    padding: '12px 16px',
    borderRadius: '12px',
  },
  userContent: {
    backgroundColor: tokens.colorBrandBackground,
    color: tokens.colorNeutralForegroundOnBrand,
  },
  assistantContent: {
    backgroundColor: tokens.colorNeutralBackground3,
  },
  icon: {
    width: '32px',
    height: '32px',
    borderRadius: '50%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: tokens.colorNeutralBackground3,
  },
  inputContainer: {
    display: 'flex',
    gap: '10px',
  },
  input: {
    flex: 1,
  },
  citations: {
    marginTop: '8px',
    fontSize: '12px',
    color: tokens.colorNeutralForeground3,
  },
});

interface Message {
  role: 'user' | 'assistant';
  content: string;
  citations?: Array<{ source: string; quote: string }>;
}

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const styles = useStyles();
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const chatEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: [...messages, userMessage],
          conversation_id: conversationId,
        }),
      });

      if (!response.ok) throw new Error('Failed to get response');

      const data = await response.json();
      
      setConversationId(data.conversation_id);
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: data.message.content,
          citations: data.citations,
        },
      ]);
    } catch (error) {
      console.error('Error:', error);
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: 'Sorry, there was an error processing your request.',
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <Text className={styles.title}>IQ Agent</Text>
        <Text className={styles.subtitle}>
          Powered by Foundry IQ + Fabric IQ
        </Text>
      </div>

      <Card className={styles.chatContainer}>
        {messages.length === 0 && (
          <Text style={{ textAlign: 'center', color: tokens.colorNeutralForeground3 }}>
            Ask a question about your documents or data...
          </Text>
        )}
        
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`${styles.message} ${msg.role === 'user' ? styles.userMessage : ''}`}
          >
            <div className={styles.icon}>
              {msg.role === 'user' ? <Person24Regular /> : <Bot24Regular />}
            </div>
            <div
              className={`${styles.messageContent} ${
                msg.role === 'user' ? styles.userContent : styles.assistantContent
              }`}
            >
              <ReactMarkdown>{msg.content}</ReactMarkdown>
              {msg.citations && msg.citations.length > 0 && (
                <div className={styles.citations}>
                  <strong>Sources:</strong>
                  {msg.citations.map((c, i) => (
                    <div key={i}>• {c.source}</div>
                  ))}
                </div>
              )}
            </div>
          </div>
        ))}
        
        {loading && (
          <div className={styles.message}>
            <div className={styles.icon}>
              <Bot24Regular />
            </div>
            <div className={`${styles.messageContent} ${styles.assistantContent}`}>
              <Spinner size="tiny" label="Thinking..." />
            </div>
          </div>
        )}
        
        <div ref={chatEndRef} />
      </Card>

      <div className={styles.inputContainer}>
        <Input
          className={styles.input}
          placeholder="Type your message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          disabled={loading}
        />
        <Button
          appearance="primary"
          icon={<Send24Regular />}
          onClick={sendMessage}
          disabled={loading || !input.trim()}
        >
          Send
        </Button>
      </div>
    </div>
  );
}

export default App;
