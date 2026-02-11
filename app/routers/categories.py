from fastapi import APIRouter
from app.schemas.category import CategoryRead, CategoryBase

router = APIRouter()

@router.get("/", response_model=list[CategoryRead])
async def list_categories():
    return []

@router.post("/", response_model=CategoryRead)
async def create_category(data: CategoryBase):
    return {"id": 1, "name": data.name}
