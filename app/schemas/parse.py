from pydantic import BaseModel
from typing import Any

class ParseRequest(BaseModel):
    text: str
    metadata: Any = None

class ParseResult(BaseModel):
    parsed: Any
