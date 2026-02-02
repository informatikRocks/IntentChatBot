
from fastapi import APIRouter
from app.api.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model = ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    
    analysis = NLP_Engine.analyze(request.message)
    response = IntentHandler.handle_intent(analysis)
    return ChatResponse(answer=response)
   

