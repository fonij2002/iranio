from typing import Any

from iranio.sms.mappers.base import BaseSMSMapper
from iranio.sms.models import (
    BulkSMSRequest,
    OTPRequest,
    SendSMSRequest,
)


class SMSIRMapper(BaseSMSMapper):
    """
    Convert iranio SMS models
    to SMS.ir payloads.
    """

    def map_send(
        self,
        request: SendSMSRequest,
    ) -> dict[str, Any]:

        payload: dict[str, Any] = {
            "lineNumber": request.sender,
            "MobileNumbers": [request.phone],
            "Messages": [request.message],
        }

        return payload

    def map_bulk(
        self,
        request: BulkSMSRequest,
    ) -> dict[str, Any]:

        payload: dict[str, Any] = {
            "MobileNumbers": request.phones,
            "Messages": [request.message for _ in request.phones],
        }

        if request.sender:

            payload["LineNumber"] = request.sender

        return payload

    def map_otp(
        self,
        request: OTPRequest,
    ) -> dict[str, Any]:

        payload: dict[str, Any] = {
            "Mobile": request.phone,
            "TemplateId": request.template,
        }

        parameters = []

        for key, value in request.tokens.items():

            parameters.append(
                {
                    "Name": key,
                    "Value": value,
                }
            )

        payload["Parameters"] = parameters

        return payload
