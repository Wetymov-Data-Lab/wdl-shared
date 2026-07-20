from pydantic import BaseModel
from uuid import UUID
from wdl_shared.schemas.engine.enums import DataBaseName

class Project(BaseModel):
    """Project validation model"""

    id: UUID
    name: str
    realm_id: UUID
    database_name: DataBaseName
    description: str | None
    color: str | None
    