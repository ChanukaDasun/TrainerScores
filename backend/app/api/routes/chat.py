from fastapi import APIRouter, HTTPException
from app.config import get_chat_model
from app.models.chat_schema import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/")
def chat(request : ChatRequest) -> ChatResponse:
    llm = get_chat_model()
    if not llm:
        raise HTTPException(status_code=500, detail="Chat model not initialized")
    content = llm.invoke(request.message).content
    return ChatResponse(response=content)