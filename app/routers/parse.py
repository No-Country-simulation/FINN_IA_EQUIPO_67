from fastapi import APIRouter, Depends
from app.schemas.parse import ParseRequest, ParseResult
from app.ai import call_llm
from app.auth import verify_token

router = APIRouter()

@router.post("/", response_model=ParseResult)
async def parse(req: ParseRequest, user=Depends(verify_token)):
    # núcleo: procesar texto y devolver parse
    parsed = await call_llm(req.text)
    return {"parsed": parsed}
