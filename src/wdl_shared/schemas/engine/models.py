from uuid import UUID
from typing import Optional
from pydantic import BaseModel

class EntityBase(BaseModel):
    id: UUID
    name : str
    notice: Optional[str] = None

    class Config:
        orm_mode = True