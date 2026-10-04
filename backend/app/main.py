from fastapi import FastAPI

from app.config import settings
from app.api.routes.research import router as research_router


app = FastAPI(
    title=settings.app_name,
    description="Multi-Agent AI Research Platform",
    version=settings.app_version
)


app.include_router(research_router)


@app.get("/")
async def root():
    return {
        "message": "ResearchMind AI API is running",
        "version": settings.app_version,
        "environment": settings.environment
    }