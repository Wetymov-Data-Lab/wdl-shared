from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class IdMixin(BaseModel):
    """Mixin for models with an ID attribute."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(..., description="Unique identifier of the model")


class AuditResponseMixin(BaseModel):
    """Timestamps common to persisted API responses."""

    created_at: datetime        = Field(description="Timestamp of creation")
    updated_at: datetime | None = Field(default=None, description="Timestamp of last update")
