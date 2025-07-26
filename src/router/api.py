from fastapi import APIRouter
from src.models.interviews import InterviewRequest, InterviewResponse
from src.controller.interview_controller import get_interview_questions
from src.config import settings

router = APIRouter(prefix=settings.API_PREFIX)

@router.post("/interview", response_model=InterviewResponse, tags=["Entrevista"])
async def get_interview(request_data: InterviewRequest):
    return await get_interview_questions(request_data)