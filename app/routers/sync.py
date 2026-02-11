from fastapi import APIRouter

router = APIRouter()

@router.post("/pull")
async def sync_pull():
    return {"ok": True}
