from pydantic import BaseModel


class SMSSettings(BaseModel):

    provider: str

    api_key: str


class IranioSettings(BaseModel):

    sms: SMSSettings | None = None
