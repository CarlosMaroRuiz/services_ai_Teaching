from pydantic import BaseModel
from typing import  Optional
class InterviewRequest(BaseModel):
    message: str
    options: Optional[dict] = None