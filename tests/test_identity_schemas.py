from datetime import UTC, datetime
from uuid import uuid4

from pydantic import ValidationError
from pytest import raises

from wdl_shared.schemas.identity import (
    AccountRegistrationModel,
    OAuthTokenResponseModel,
    PasswordSetModel,
    SessionCreateModel,
    UserInfoResponseModel,
)


def test_account_registration_accepts_email_password_and_profile() -> None:
    model = AccountRegistrationModel.model_validate(
        {
            "email": "Denis@Example.com",
            "password": "correct horse battery staple",
            "profile": {
                "display_name": "Denis",
                "given_name": "Denis",
                "job_title": "Software Engineer",
                "organization": "WDL",
                "bio": "Designing databases",
                "locale": "ru-RU",
                "time_zone": "Europe/Moscow",
                "website_url": "https://example.test",
            },
        }
    )

    assert str(model.email) == "Denis@example.com"
    assert model.password.get_secret_value() == "correct horse battery staple"
    assert model.profile.display_name == "Denis"
    assert model.profile.organization == "WDL"


def test_password_input_is_masked() -> None:
    model = PasswordSetModel(password="correct horse battery staple")

    assert "correct horse battery staple" not in repr(model)


def test_session_requires_non_empty_sensitive_fields() -> None:
    with raises(ValidationError):
        SessionCreateModel(
            ip="127.0.0.1",
            refresh_token_hash="",
            user_agent="pytest",
            expires_at=datetime.now(UTC),
        )


def test_oauth_response_models_are_shared_between_services() -> None:
    tokens = OAuthTokenResponseModel(
        access_token="access-token",
        refresh_token="refresh-token",
        expires_in=900,
    )
    user_info = UserInfoResponseModel(
        sub=uuid4(),
        email="user@example.com",
        name="Test User",
    )

    assert tokens.token_type == "bearer"
    assert str(user_info.email) == "user@example.com"
