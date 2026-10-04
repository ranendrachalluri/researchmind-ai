from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/research",
    tags=["Research"]
)


@router.get("/health")
async def research_health():
    return {
        "status": "Research API is working"
    }