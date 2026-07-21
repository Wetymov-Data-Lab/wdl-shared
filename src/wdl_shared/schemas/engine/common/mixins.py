from uuid import UUID

from pydantic import BaseModel, Field


class IdMixin(BaseModel):
    """Mixin for models with an ID attribute."""

    id: UUID = Field(..., description="Unique identifier of the model")
