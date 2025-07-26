from src.models.interviews import InterviewRequest, InterviewResponse
from src.services.process_interview_request import process_interview_request

async def get_interview_questions(request_data: InterviewRequest) -> InterviewResponse:
        return await process_interview_request(message=request_data.message,)
