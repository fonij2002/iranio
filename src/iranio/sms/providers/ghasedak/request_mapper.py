from typing import Any

from iranio.sms.mappers.base import BaseSMSMapper
from iranio.sms.models import (
    BulkSMSRequest,
    OTPRequest,
    SendSMSRequest,
)


class GhasedakMapper(BaseSMSMapper):
    """
    Maps iranio SMS models
    to Ghasedak API payloads.
    """

    def map_send(
        self,
        request: SendSMSRequest,
    ) -> dict[str, Any]:

        payload: dict[str, Any] = {
            "receptors": [request.phone],
            "message": request.message,
        }

        if request.sender:

            payload["lineNumber"] = request.sender

        return payload

    def map_bulk(
        self,
        request: BulkSMSRequest,
    ) -> dict[str, Any]:

        payload: dict[str, Any] = {
            "receptors": request.phones,
            "message": request.message,
        }

        if request.sender:

            payload["lineNumber"] = request.sender

        return payload

    def map_otp(
        self,
        request: OTPRequest,
    ) -> dict[str, Any]:

        payload: dict[str, Any] = {
            "receptor": request.phone,
            "template": request.template,
        }

        payload.update(request.tokens)

        return payload
