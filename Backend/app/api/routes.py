
from fastapi import APIRouter
from app.api.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest) -> ChatResponse:
    return ChatResponse(answer=request.message)
   

