
from fastapi import APIRouter
from app.api.schemas import ChatRequest, ChatResponse
from app.model.nlp_engine import get_response
from app.api.schemas import ChatRequest, ChatResponse

router = APIRouter()



@router.post("/chat", response_model = ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Dieser Endpunkt nimmt die Nachricht entgegen, jagt sie durch das 
    PyTorch-Modell und gibt die Antwort aus der profile.json zurück.
    """

    print(f"User fragt: {request.message}")
    bot_answer = get_response(request.message)
    print(f"Bot antwortet: {bot_answer}")
    return ChatResponse(answer=bot_answer)



    

