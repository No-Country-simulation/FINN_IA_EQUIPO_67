from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class AppFinancial(Base):
    __tablename__ = "apps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    enabled = Column(Boolean, default=True)
    external_id = Column(String(128), nullable=True)
