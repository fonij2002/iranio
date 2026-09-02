from iranio.sms.base import BaseSMSProvider
from iranio.sms.models import (
    BulkSMSRequest,
    OTPRequest,
    SendSMSRequest,
    SMSAccountInfo,
    SMSResponse,
    SMSStatus,
)


class SMSService:
    """
    Public SMS API.
    """

    def __init__(
        self,
        provider: BaseSMSProvider,
    ) -> None:

        self.provider = provider

    def send(
        self,
        phone: str,
        message: str,
        sender: str | None = None,
    ) -> SMSResponse:

        request = SendSMSRequest(
            phone=phone,
            message=message,
            sender=sender,
        )

        return self.provider.send(request)

    def send_bulk(
        self,
        phones: list[str],
        message: str,
        sender: str | None = None,
    ) -> SMSResponse:

        request = BulkSMSRequest(
            phones=phones,
            message=message,
            sender=sender,
        )

        return self.provider.send_bulk(request)

    def send_otp(
        self,
        phone: str,
        template: str,
        tokens: dict[str, str],
    ) -> SMSResponse:

        request = OTPRequest(
            phone=phone,
            template=template,
            tokens=tokens,
        )

        return self.provider.send_otp(request)

    def status(
        self,
        message_id: str,
    ) -> SMSStatus:

        return self.provider.status(message_id)

    def account_info(
        self,
    ) -> SMSAccountInfo:

        return self.provider.account_info()
