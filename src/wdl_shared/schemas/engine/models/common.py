from uuid import UUID

from pydantic import BaseModel, ConfigDict


class EntityBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    notice: str | None = None
