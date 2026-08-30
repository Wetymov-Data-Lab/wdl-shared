from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, SecretStr

from .enums import AccountStatus, AccountSubject


class TwoFactorPolicyUpdateModel(BaseModel):
    enforced: bool


class ProfileCreateModel(BaseModel):
    display_name: str = Field(min_length=1, max_length=255)
    given_name: str | None = Field(default=None, max_length=255)
    family_name: str | None = Field(default=None, max_length=255)
    bio: str | None = Field(default=None, max_length=1_000)
    job_title: str | None = Field(default=None, max_length=255)
    organization: str | None = Field(default=None, max_length=255)
    locale: str | None = Field(default=None, max_length=64)
    time_zone: str | None = Field(default=None, max_length=64)
    picture_url: str | None = Field(default=None, max_length=2_048)
    website_url: str | None = Field(default=None, max_length=2_048)


class ProfileUpdateModel(ProfileCreateModel):
    pass


class ProfileResponseModel(ProfileUpdateModel):
    id: UUID
    account_id: UUID
    created_at: datetime
    updated_at: datetime | None


class PasswordSetModel(BaseModel):
    password: SecretStr = Field(min_length=12, max_length=1_024)


class PasswordResponseModel(BaseModel):
    id: UUID
    account_id: UUID
    set_at: datetime
    version: int = Field(ge=1)


class IdentifierCreateModel(BaseModel):
    type: str = Field(min_length=1, max_length=64)
    value: str = Field(min_length=1, max_length=2_048)
    provider: str | None = Field(default=None, max_length=128)
    provider_user_id: str | None = Field(default=None, max_length=2_048)
    is_public_contact: bool = False
    receive_notifications: bool = False


class AccountRegistrationModel(BaseModel):
    email: EmailStr
    password: SecretStr = Field(min_length=12, max_length=1_024)
    profile: ProfileCreateModel


class IdentifierPreferencesUpdateModel(BaseModel):
    is_public_contact: bool
    receive_notifications: bool


class IdentifierResponseModel(IdentifierCreateModel):
    id: UUID
    account_id: UUID
    is_verified: bool
    verified_at: datetime | None
    last_used_at: datetime | None
    created_at: datetime


class SecondFactorCreateModel(BaseModel):
    type: str = Field(min_length=1, max_length=64)
    secret: str = Field(min_length=1, max_length=4_096)
    name: str | None = Field(default=None, max_length=255)


class SecondFactorResponseModel(BaseModel):
    id: UUID
    account_id: UUID
    type: str
    name: str | None
    confirmed_at: datetime | None
    created_at: datetime


class RecoveryCodeCreateModel(BaseModel):
    hash: str = Field(min_length=1, max_length=4_096)


class RecoveryCodeResponseModel(BaseModel):
    id: UUID
    account_id: UUID
    used_at: datetime | None
    created_at: datetime


class SessionCreateModel(BaseModel):
    ip: str = Field(min_length=1, max_length=255)
    refresh_token_hash: str = Field(min_length=1, max_length=4_096)
    user_agent: str = Field(min_length=1, max_length=2_048)
    expires_at: datetime


class SessionRefreshModel(BaseModel):
    refresh_token_hash: str = Field(min_length=1, max_length=4_096)
    expires_at: datetime


class SessionResponseModel(BaseModel):
    id: UUID
    account_id: UUID
    ip: str
    user_agent: str
    expires_at: datetime
    created_at: datetime
    last_refreshed_at: datetime


class AccountResponseModel(BaseModel):
    id: UUID
    subject: AccountSubject
    status: AccountStatus
    is_2fa_enforced: bool
    created_at: datetime
    updated_at: datetime | None
    last_active_at: datetime | None
    version: int = Field(ge=1)
    profile: ProfileResponseModel | None
    password: PasswordResponseModel | None
    identifiers: list[IdentifierResponseModel]
    second_factors: list[SecondFactorResponseModel]
    recovery_codes: list[RecoveryCodeResponseModel]
    sessions: list[SessionResponseModel]


class OAuthTokenResponseModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: Literal["bearer"] = "bearer"
    expires_in: int = Field(gt=0)


class UserInfoResponseModel(BaseModel):
    sub: UUID
    email: EmailStr | None = None
    name: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    picture: str | None = None
    locale: str | None = None
