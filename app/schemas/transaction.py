from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime

class TransactionBase(BaseModel):
    amount: Decimal
    currency: str = "USD"
    description: Optional[str]

class TransactionCreate(TransactionBase):
    user_id: int

class TransactionRead(TransactionBase):
    id: int
    user_id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
