from wdl_shared.schemas.common import HealthResponse
from wdl_shared.schemas.engine.common.health import HealthResponse as LegacyHealthResponse


def test_health_response_is_available_from_common_namespace() -> None:
    assert HealthResponse(status="ok").model_dump() == {"status": "ok"}
    assert LegacyHealthResponse is HealthResponse
