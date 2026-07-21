from uuid import UUID

from pydantic import BaseModel

from ..enums.database import DataBaseName


class Project(BaseModel):
    """Project validation model."""

    id: UUID
    name: str
    realm_id: UUID
    database_name: DataBaseName
    description: str | None
    color: str | None
