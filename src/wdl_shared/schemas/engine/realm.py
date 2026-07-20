from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field
from .mixins.base_mixins import IdMixin

class RealmCreateModel(BaseModel):
    """Realm creation validation model"""

    # Base attributes
    name:   str        = Field(..., description="Name of the realm")
    notice: str | None = Field(None, description="Notice for the realm")


class RealmUpdateModel(RealmCreateModel):
    pass  # Inherits all attributes from RealmCreateModel
    

class RealmResponseModel(IdMixin, RealmCreateModel):
    """Realm validation model"""

    # Additional attributes
    created_at: datetime        = Field(..., description="Timestamp of realm creation")
    updated_at: datetime | None = Field(None, description="Timestamp of last realm update")
    author_id:  UUID | str      = Field(..., description="Identifier of the author of the realm")