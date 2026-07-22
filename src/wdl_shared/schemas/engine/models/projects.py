from uuid import UUID

from pydantic import BaseModel, Field

from ..common.mixins import AuditResponseMixin, IdMixin


class ProjectCreateModel(BaseModel):
    """Payload used to create a project."""

    name:      str        = Field(min_length=1, max_length=255, description="Name of the project")
    realm_id:  UUID       = Field(description="Identifier of the parent realm")
    notice:    str | None = Field(default=None, max_length=255, description="Notice for the project")
    author_id: UUID       = Field(description="Identifier of the project author")


class ProjectUpdateModel(BaseModel):
    """Complete set of mutable project attributes."""

    name:   str        = Field(min_length=1, max_length=255, description="Name of the project")
    notice: str | None = Field(default=None, max_length=255, description="Notice for the project")


class ProjectResponseModel(IdMixin, ProjectCreateModel, AuditResponseMixin):
    """Project returned by the API."""


# Backwards-compatible public name. New code should use ProjectResponseModel.
Project = ProjectResponseModel
