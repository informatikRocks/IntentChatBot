from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class ChatResponse(BaseModel):
    """Response from the chat endpoint"""   
    answer: str
    sentiment:str
    intent:str


class ChatRequest(BaseModel):
    """Request for the chat endpoint"""   
    message: str


class Contact(BaseModel):
    email:str
    linkedin: Optional[str]=None
    github: Optional[str]=None


class Project(BaseModel):
    id: str
    name: str
    description: str
    tech_stack: List[str]
    url: Optional[str]=None


class Profile(BaseModel):
    name: str
    role: str
    location:str
    bio:str
    contact: Contact




