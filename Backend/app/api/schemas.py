
class ChatResponse(BaseModel):
    """Response from the chat endpoint"""   
    label: str
    answer: str