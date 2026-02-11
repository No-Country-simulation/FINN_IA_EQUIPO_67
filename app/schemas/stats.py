from pydantic import BaseModel
from typing import Any

class StatsResponse(BaseModel):
    summary: Any
