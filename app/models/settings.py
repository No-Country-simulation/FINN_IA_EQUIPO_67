from sqlalchemy import Column, Integer, String
from app.database import Base

class SettingsModel(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(128), nullable=False, unique=True)
    value = Column(String, nullable=True)
