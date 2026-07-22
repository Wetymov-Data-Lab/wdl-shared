from uuid import UUID

from pydantic import BaseModel, Field, model_validator

from ..common.mixins import AuditResponseMixin, IdMixin
from ..enums.database import (
    ColumnType,
    DataBaseName,
    IndexType,
    ReferentialAction,
    RelationshipCardinality,
    SortOrder,
)
from .canvas import CanvasPosition

NameField   = Field(min_length=1, max_length=255)
NoticeField = Field(default=None, max_length=255)


class DatabaseCreateModel(BaseModel):
    """Payload used to create a database."""

    name:           str          = NameField
    project_id:     UUID         = Field(description="Identifier of the parent project")
    type:           DataBaseName = Field(description="Database engine")
    notice:         str | None   = NoticeField
    default_schema: str | None   = Field(default=None, min_length=1, max_length=255)
    charset:        str | None   = Field(default=None, min_length=1, max_length=64)
    collation:      str | None   = Field(default=None, min_length=1, max_length=128)
    author_id:      UUID         = Field(description="Identifier of the database author")


class DatabaseUpdateModel(BaseModel):
    """Complete set of mutable database attributes."""

    name:           str          = NameField
    type:           DataBaseName = Field(description="Database engine")
    notice:         str | None   = NoticeField
    default_schema: str | None   = Field(default=None, min_length=1, max_length=255)
    charset:        str | None   = Field(default=None, min_length=1, max_length=64)
    collation:      str | None   = Field(default=None, min_length=1, max_length=128)


class DatabaseResponseModel(IdMixin, DatabaseCreateModel, AuditResponseMixin):
    """Database returned by the API."""


class TableCreateModel(BaseModel):
    """Payload used to create a table."""

    name:         str            = NameField
    database_id:  UUID           = Field(description="Identifier of the parent database")
    schema_name:  str | None     = Field(default=None, min_length=1, max_length=255)
    description:  str | None     = Field(default=None, max_length=255)
    notice:       str | None     = NoticeField
    color:        str | None     = Field(
        default=None,
        pattern=r"^#[0-9A-Fa-f]{6}$",
        description="Table color in #RRGGBB format",
    )
    position:     CanvasPosition = Field(default_factory=lambda: CanvasPosition(x=0, y=0))
    width:        float | None   = Field(default=None, gt=0, description="Custom table-card width")
    is_collapsed: bool           = False
    sort_order:   int            = Field(default=0, ge=0)
    author_id:    UUID           = Field(description="Identifier of the table author")


class TableUpdateModel(BaseModel):
    """Complete set of mutable table attributes."""

    name:         str            = NameField
    schema_name:  str | None     = Field(default=None, min_length=1, max_length=255)
    description:  str | None     = Field(default=None, max_length=255)
    notice:       str | None     = NoticeField
    color:        str | None     = Field(default=None, pattern=r"^#[0-9A-Fa-f]{6}$")
    position: CanvasPosition
    width:        float | None   = Field(default=None, gt=0)
    is_collapsed: bool           = False
    sort_order:   int            = Field(default=0, ge=0)


class TableResponseModel(IdMixin, TableCreateModel, AuditResponseMixin):
    """Table returned by the API."""


class ColumnCreateModel(BaseModel):
    """Payload used to create a column."""

    name:             str        = NameField
    table_id:         UUID       = Field(description="Identifier of the parent table")
    type:             ColumnType = Field(description="Column data type")
    custom_type:      str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
        description="Vendor-specific type name when type is custom",
    )
    length:           int | None = Field(default=None, gt=0)
    precision:        int | None = Field(default=None, gt=0)
    scale:            int | None = Field(default=None, ge=0)
    array_dimensions: int        = Field(default=0, ge=0, le=8)
    nullable:         bool       = True
    primary_key:      bool       = False
    unique:           bool       = False
    auto_increment:   bool       = False
    unsigned:         bool       = False
    default:          str | None = Field(default=None, max_length=2_000)
    check:            str | None = Field(default=None, max_length=4_000)
    enum_values:      list[str]  = Field(default_factory=list)
    sort_order:       int        = Field(default=0, ge=0)
    notice:           str | None = NoticeField
    author_id:        UUID       = Field(description="Identifier of the column author")

    @model_validator(mode="after")
    def validate_type_options(self) -> "ColumnCreateModel":
        if self.type == ColumnType.CUSTOM and self.custom_type is None:
            raise ValueError("custom_type is required when type is custom")
        if self.scale is not None and self.precision is None:
            raise ValueError("precision is required when scale is set")
        if self.precision is not None and self.scale is not None and self.scale > self.precision:
            raise ValueError("scale cannot exceed precision")
        if self.type == ColumnType.ENUM and not self.enum_values:
            raise ValueError("enum_values are required when type is enum")
        return self


class ColumnUpdateModel(BaseModel):
    """Complete set of mutable column attributes."""

    name:             str        = NameField
    type:             ColumnType = Field(description="Column data type")
    custom_type:      str | None = Field(default=None, min_length=1, max_length=255)
    length:           int | None = Field(default=None, gt=0)
    precision:        int | None = Field(default=None, gt=0)
    scale:            int | None = Field(default=None, ge=0)
    array_dimensions: int        = Field(default=0, ge=0, le=8)
    nullable:         bool       = True
    primary_key:      bool       = False
    unique:           bool       = False
    auto_increment:   bool       = False
    unsigned:         bool       = False
    default:          str | None = Field(default=None, max_length=2_000)
    check:            str | None = Field(default=None, max_length=4_000)
    enum_values:      list[str]  = Field(default_factory=list)
    sort_order:       int        = Field(default=0, ge=0)
    notice:           str | None = NoticeField

    @model_validator(mode="after")
    def validate_type_options(self) -> "ColumnUpdateModel":
        if self.type == ColumnType.CUSTOM and self.custom_type is None:
            raise ValueError("custom_type is required when type is custom")
        if self.scale is not None and self.precision is None:
            raise ValueError("precision is required when scale is set")
        if self.precision is not None and self.scale is not None and self.scale > self.precision:
            raise ValueError("scale cannot exceed precision")
        if self.type == ColumnType.ENUM and not self.enum_values:
            raise ValueError("enum_values are required when type is enum")
        return self


class ColumnResponseModel(IdMixin, ColumnCreateModel, AuditResponseMixin):
    """Column returned by the API."""


class IndexColumnModel(BaseModel):
    """An ordered column reference inside a composite index."""

    column_id: UUID
    sort_order: SortOrder = SortOrder.ASC
    position:   int       = Field(ge=0)


class IndexCreateModel(BaseModel):
    """Payload used to create a table index or constraint."""

    table_id: UUID
    name:      str | None             = Field(default=None, min_length=1, max_length=255)
    type:      IndexType              = IndexType.INDEX
    columns:   list[IndexColumnModel] = Field(min_length=1)
    method:    str | None             = Field(default=None, min_length=1, max_length=64)
    where:     str | None             = Field(default=None, max_length=4_000)
    author_id: UUID


class IndexUpdateModel(BaseModel):
    """Complete set of mutable index attributes."""

    name:    str | None             = Field(default=None, min_length=1, max_length=255)
    type:    IndexType              = IndexType.INDEX
    columns: list[IndexColumnModel] = Field(min_length=1)
    method:  str | None             = Field(default=None, min_length=1, max_length=64)
    where:   str | None             = Field(default=None, max_length=4_000)


class IndexResponseModel(IdMixin, IndexCreateModel, AuditResponseMixin):
    """Index returned by the API."""


class RelationshipColumnPair(BaseModel):
    """One source/target column pair in a foreign key."""

    source_column_id: UUID
    target_column_id: UUID


class RelationshipCreateModel(BaseModel):
    """Payload used to create a foreign-key relationship."""

    database_id: UUID
    name:               str | None                   = Field(default=None, min_length=1, max_length=255)
    source_table_id: UUID
    target_table_id: UUID
    columns:            list[RelationshipColumnPair] = Field(min_length=1)
    source_cardinality: RelationshipCardinality      = RelationshipCardinality.ZERO_OR_MANY
    target_cardinality: RelationshipCardinality      = RelationshipCardinality.EXACTLY_ONE
    on_delete:          ReferentialAction            = ReferentialAction.NO_ACTION
    on_update:          ReferentialAction            = ReferentialAction.NO_ACTION
    waypoints:          list[CanvasPosition]         = Field(
        default_factory=list,
        description="Optional bend points for manually routed relationship lines",
    )
    author_id: UUID


class RelationshipUpdateModel(BaseModel):
    """Complete set of mutable relationship attributes."""

    name:               str | None                   = Field(default=None, min_length=1, max_length=255)
    columns:            list[RelationshipColumnPair] = Field(min_length=1)
    source_cardinality: RelationshipCardinality
    target_cardinality: RelationshipCardinality
    on_delete: ReferentialAction
    on_update: ReferentialAction
    waypoints:          list[CanvasPosition]         = Field(default_factory=list)


class RelationshipResponseModel(IdMixin, RelationshipCreateModel, AuditResponseMixin):
    """Relationship returned by the API."""
