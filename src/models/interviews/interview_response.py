from typing import Optional
from pydantic import BaseModel
from .questions_model import Questions
class InterviewResponse(BaseModel):
    success: bool
    data: Optional[Questions] = None
    error: Optional[str] = None