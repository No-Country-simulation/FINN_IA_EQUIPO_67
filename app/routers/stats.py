from fastapi import APIRouter
from app.schemas.stats import StatsResponse

router = APIRouter()

@router.get("/", response_model=StatsResponse)
async def stats():
    return {"summary": {}}
