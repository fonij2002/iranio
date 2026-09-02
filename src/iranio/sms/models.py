from typing import Any

from pydantic import BaseModel, Field


class SMSAccountInfo(BaseModel):
    """
    Provider account information.
    """

    data: dict[str, Any] | None = None

    raw: dict[str, Any] | None = None


class SendSMSRequest(BaseModel):
    phone: str
    message: str
    sender: str | None = None


class BulkSMSRequest(BaseModel):
    phones: list[str]
    message: str
    sender: str | None = None


class OTPRequest(BaseModel):
    phone: str
    template: str
    tokens: dict[str, str]


class SMSResponse(BaseModel):

    success: bool

    message: str | None = None

    message_ids: list[str] = Field(default_factory=list)

    raw: dict[str, Any] | None = None


class SMSStatus(BaseModel):

    message_id: str

    status: str

    description: str | None = None
