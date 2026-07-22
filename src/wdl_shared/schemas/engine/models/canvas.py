from uuid import UUID

from pydantic import BaseModel, Field


class CanvasPosition(BaseModel):
    """Absolute position of an object on the infinite canvas."""

    x: float = Field(description="Horizontal canvas coordinate")
    y: float = Field(description="Vertical canvas coordinate")


class CanvasViewport(BaseModel):
    """Last saved camera position for a diagram."""

    x:    float = 0
    y:    float = 0
    zoom: float = Field(default=1, gt=0, le=8)


class CanvasStateModel(BaseModel):
    """Saved presentation preferences for a database diagram."""

    database_id: UUID
    user_id:                  UUID | None     = Field(
        default=None,
        description="Owner of a personal viewport; null means diagram default",
    )
    viewport:                  CanvasViewport = Field(default_factory=CanvasViewport)
    grid_size:                 int            = Field(default=20, ge=1, le=200)
    snap_to_grid:              bool           = True
    show_relationship_labels:  bool           = True


class DiagramGroupModel(BaseModel):
    """Visual grouping of related tables on the canvas."""

    id:           UUID
    database_id:  UUID
    name:         str            = Field(min_length=1, max_length=255)
    position:     CanvasPosition
    width:        float          = Field(gt=0)
    height:       float          = Field(gt=0)
    color:        str | None     = Field(default=None, pattern=r"^#[0-9A-Fa-f]{6}$")
    is_collapsed: bool           = False
    table_ids:    list[UUID]     = Field(default_factory=list)


class DiagramNoteModel(BaseModel):
    """Free-form documentation placed on the canvas."""

    id:          UUID
    database_id: UUID
    text:        str            = Field(min_length=1, max_length=10_000)
    position:    CanvasPosition
    width:       float          = Field(default=240, gt=0)
    height:      float          = Field(default=160, gt=0)
    color:       str | None     = Field(default=None, pattern=r"^#[0-9A-Fa-f]{6}$")
