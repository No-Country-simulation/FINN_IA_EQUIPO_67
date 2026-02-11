from pydantic import BaseModel

class SettingRead(BaseModel):
    key: str
    value: str

    class Config:
        orm_mode = True
