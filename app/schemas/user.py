from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    uid: str
    email: Optional[str]
    name: Optional[str]

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
