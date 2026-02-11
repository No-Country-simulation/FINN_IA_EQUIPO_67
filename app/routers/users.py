from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.database import get_session
from app.auth import verify_token

router = APIRouter()

@router.get("/", response_model=list[UserRead])
async def list_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(User.__table__.select())
    rows = result.fetchall()
    return [UserRead.from_orm(r) for r in rows]

@router.post("/", response_model=UserRead)
async def create_user(data: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(uid=data.uid, email=data.email, name=data.name)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
