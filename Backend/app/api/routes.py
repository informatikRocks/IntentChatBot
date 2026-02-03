
from fastapi import APIRouter
from app.api.schemas import ChatRequest, ChatResponse
from app.model.nlp_engine import engine
from app.model.intent_handler import IntentHandler

router = APIRouter()
intent_handler = IntentHandler()


@router.post("/chat", response_model = ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    
    analysis = engine.analyze(request.message)
    response = intent_handler.handle_intent(analysis)
    return ChatResponse(answer=response)
   

