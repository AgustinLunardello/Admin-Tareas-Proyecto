from pydantic import BaseModel
from typing import Optional

class taskModel(BaseModel):
    tittle: str
    description: Optional[str]
    state: Optional[str]
    author: str