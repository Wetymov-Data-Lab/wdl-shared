from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from ..common.mixins import IdMixin
from ..enums.realms import RealmStatus, RealmVisibility


class RealmCreateModel(BaseModel):
    """Realm creation validation model."""

    name: str = Field(min_length=1, max_length=255, description="Name of the realm")
    slug: str = Field(
        min_length=1,
        max_length=255,
        description="URL-safe unique realm identifier",
    )
    status: RealmStatus = RealmStatus.ACTIVE
    visibility: RealmVisibility = RealmVisibility.PRIVATE
    settings: dict[str, Any] = Field(default_factory=dict)
    notice: str | None = Field(default=None, max_length=255, description="Notice for the realm")
    author_id: UUID = Field(description="Identifier of the realm author")


class RealmUpdateModel(BaseModel):
    """Complete set of mutable realm attributes."""

    name: str = Field(min_length=1, max_length=255, description="Name of the realm")
    slug: str = Field(
        min_length=1,
        max_length=255,
        description="URL-safe unique realm identifier",
    )
    status: RealmStatus
    visibility: RealmVisibility
    settings: dict[str, Any]
    notice: str | None = Field(default=None, max_length=255, description="Notice for the realm")
    updated_by: UUID


class RealmResponseModel(IdMixin, RealmCreateModel):
    """Realm validation model."""

    created_at: datetime = Field(description="Timestamp of realm creation")
    updated_at: datetime | None = Field(default=None, description="Timestamp of last realm update")
    deleted_at: datetime | None = Field(default=None, description="Timestamp of soft deletion")
    updated_by: UUID | None = Field(default=None, description="Identifier of the last editor")
