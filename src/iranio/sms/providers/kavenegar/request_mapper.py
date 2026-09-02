from typing import Any

from iranio.sms.mappers.base import BaseSMSMapper
from iranio.sms.models import (
    BulkSMSRequest,
    OTPRequest,
    SendSMSRequest,
)


class KavenegarMapper(BaseSMSMapper):
    """
    Maps internal iranio SMS models
    to Kavenegar API payloads.
    """

    def map_send(
        self,
        request: SendSMSRequest,
    ) -> dict[str, Any]:
        """
        Map single SMS request.
        """

        payload: dict[str, Any] = {
            "receptor": request.phone,
            "message": request.message,
        }

        if request.sender:
            payload["sender"] = request.sender

        return payload

    def map_bulk(
        self,
        request: BulkSMSRequest,
    ) -> dict[str, Any]:
        """
        Map bulk SMS request.

        Kavenegar expects arrays of receptors,
        messages and senders.
        """

        payload: dict[str, Any] = {
            "receptor": request.phones,
            "message": [request.message for _ in request.phones],
        }

        if request.sender:
            payload["sender"] = [request.sender for _ in request.phones]

        return payload

    def map_otp(
        self,
        request: OTPRequest,
    ) -> dict[str, Any]:
        """
        Map verify/lookup OTP request.
        """

        payload: dict[str, Any] = {
            "receptor": request.phone,
            "template": request.template,
        }

        payload.update(request.tokens)

        return payload
