from pydantic import BaseModel, Field


class SendSMSRequest(BaseModel):
    """
    Standard SMS sending request.
    """

    phone: str = Field(description="Destination phone number")

    message: str = Field(description="SMS message content")


class SendSMSResponse(BaseModel):
    """
    Standard SMS sending response.
    """

    success: bool

    message_id: str | None = None

    message: str | None = None
