from fastapi import APIRouter, Depends
from app.schemas.transaction import TransactionCreate, TransactionRead
from app.auth import verify_token

router = APIRouter()

@router.post("/", response_model=TransactionRead)
async def create_transaction(payload: TransactionCreate, user=Depends(verify_token)):
    # TODO: persistir transacción
    return {"id": 1, "user_id": payload.user_id, "amount": payload.amount, "currency": payload.currency}
