from typing import List
from pydantic import BaseModel, validator

class Question(BaseModel):
    question: str
    good_answer: str
    bad_answers: List[str]

    @validator("bad_answers")
    def check_three_bad_answers(cls, v):
        if len(v) != 3:
            raise ValueError("Debes proporcionar exactamente 3 respuestas incorrectas.")
        return v

#Esta se usara para que use el agente para sus respuesta
class Questions(BaseModel):
    msg_aditional:str
    questions: List[Question]