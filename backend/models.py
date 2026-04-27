# WHY THIS FILE EXISTS:
# FastAPI uses Pydantic models to:
#   1. Validate incoming request data automatically
#   2. Serialize outgoing response data to JSON
#   3. Give us clear documentation in the auto-generated /docs page
#
# Think of these as "data contracts" — both sides of an API call must agree
# on the exact shape of the data.
# ─────────────────────────────────────────────────────────────────

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#   REQUEST MODELS (what the client sends to us)
class ChatRequest(BaseModel):
    """
    Shape of the JSON body sent in a POST /chat request.

    Example JSON the frontend will send:
    {
        "message": "What is machine learning?",
        "system_prompt": "You are a helpful teacher"
    }
    """
    message: str
    system_prompt: Optional[str] = None

#   RESPONSE MODELS (what we send BACK to the client)
class ChatResponse(BaseModel):
    """
     Shape of the JSON we return from POST /chat.

    Example JSON we'll return:
    {
        "original_query":  "What is ML?",
        "expanded_query":  "Can you explain machine learning in simple terms, including its types and real-world applications?",
        "response":        "Machine learning is a branch of AI...",
        "timestamp":       "2024-01-15T10:30:00Z"
    }

    We include original_query AND expanded_query so the user can see
    what query expansion actually did — this is great for debugging and learning.
    """

class HistoryItem(BaseModel):
    """
    Represents a single row from our Supabase chat_history table.

    Example:
    {
        "id":        "550e8400-e29b-41d4-a716-446655440000",
        "role":      "user",
        "message":   "What is ML?",
        "timestamp": "2024-01-15T10:30:00Z"
    }
    """
    id: str
    role: str
    message: str
    timestamp: datetime

class HistoryResponse(BaseModel):
    """
    Shape of the GET /history response - just a list of messages.

    Example:
    {
        "messages": [ ...list of HistoryItem objects... ]
    }
    """
    messages: list[HistoryItem]