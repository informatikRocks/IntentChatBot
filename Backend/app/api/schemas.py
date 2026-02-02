from pydantic import BaseModel

class ChatResponse(BaseModel):
    """Response from the chat endpoint"""   
    answer: str


class ChatRequest(BaseModel):
    """Request for the chat endpoint"""   
    message: str