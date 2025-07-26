import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router.api import router
from src.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="API para agente de entrevistas con IA",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "API de Agente de Entrevistas activa", "status": "online"}

if __name__ == "__main__":
    workers_count = settings.WORKERS if hasattr(settings, 'WORKERS') else 4
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        workers=workers_count,
        limit_concurrency=100,    
        timeout_keep_alive=160   
    )