import asyncio
from src.models.interviews import InterviewResponse
from agent import agente_entrevista

async def process_interview_request(message: str) -> InterviewResponse:
        try:            
            result = await agente_entrevista.run(message)
            return InterviewResponse(success=True,data=result.output.dict())     
        except asyncio.TimeoutError:
            return InterviewResponse(success=False,error="La solicitud ha excedido el tiempo límite")
        except Exception as e:
            return InterviewResponse(success=False,error=f"Error al procesar la solicitud: {str(e)}")
