from uuid import uuid4

import pytest
from pydantic import ValidationError

from wdl_shared.schemas.engine.models import (
    CanvasStateModel,
    ColumnCreateModel,
    RelationshipCreateModel,
    TableCreateModel,
)


def test_canvas_coordinates_and_viewport() -> None:
    database_id = uuid4()
    author_id = uuid4()

    table = TableCreateModel(
        name="users",
        database_id=database_id,
        position={"x": 120.5, "y": -40},
        author_id=author_id,
    )
    canvas = CanvasStateModel(
        database_id=database_id,
        user_id=author_id,
        viewport={"x": 10, "y": 20, "zoom": 1.5},
    )

    assert table.position.x == 120.5
    assert canvas.viewport.zoom == 1.5


@pytest.mark.parametrize(
    "attributes",
    [
        {"type": "custom"},
        {"type": "decimal", "precision": 2, "scale": 3},
        {"type": "enum"},
    ],
)
def test_incompatible_column_attributes_are_rejected(attributes: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        ColumnCreateModel(
            name="value",
            table_id=uuid4(),
            author_id=uuid4(),
            **attributes,
        )


def test_relationship_supports_composite_keys_and_manual_routing() -> None:
    relationship = RelationshipCreateModel(
        database_id=uuid4(),
        source_table_id=uuid4(),
        target_table_id=uuid4(),
        columns=[
            {"source_column_id": uuid4(), "target_column_id": uuid4()},
            {"source_column_id": uuid4(), "target_column_id": uuid4()},
        ],
        on_delete="cascade",
        waypoints=[{"x": 100, "y": 200}],
        author_id=uuid4(),
    )

    assert len(relationship.columns) == 2
    assert relationship.waypoints[0].y == 200
