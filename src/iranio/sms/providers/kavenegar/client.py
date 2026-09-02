from typing import Any

from iranio.core.config import ProviderConfig
from iranio.sms.base import BaseSMSProvider
from iranio.sms.models import (
    BulkSMSRequest,
    OTPRequest,
    SendSMSRequest,
    SMSResponse,
    SMSStatus,
)
from iranio.sms.providers.base.client import (
    SMSProviderClient,
)

from .endpoints import (
    ACCOUNT_INFO,
    BASE_URL,
    SMS_SEND,
    SMS_SEND_ARRAY,
    SMS_STATUS,
    VERIFY_LOOKUP,
)
from .request_mapper import KavenegarMapper
from .response_mapper import (
    map_response,
    map_status,
)


class Kavenegar(BaseSMSProvider):

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        super().__init__(config)

        self.client = SMSProviderClient(config)

        self.mapper = KavenegarMapper()

    def _url(
        self,
        endpoint: str,
    ) -> str:

        return f"{BASE_URL}/" f"{self.config.api_key}/" f"{endpoint}"

    def send(
        self,
        request: SendSMSRequest,
    ) -> SMSResponse:

        payload = self.mapper.map_send(request)

        if request.sender:
            payload["sender"] = request.sender

        response = self.client.request(
            "POST",
            self._url(SMS_SEND),
            data=payload,
        )

        return map_response(response)

    def send_bulk(
        self,
        request: BulkSMSRequest,
    ) -> SMSResponse:

        payload = self.mapper.map_bulk(request)

        if request.sender:

            payload["sender"] = [request.sender for _ in request.phones]

        response = self.client.request(
            "POST",
            self._url(SMS_SEND_ARRAY),
            data=payload,
        )

        return map_response(response)

    def send_otp(
        self,
        request: OTPRequest,
    ) -> SMSResponse:

        payload = self.mapper.map_otp(request)

        for key, value in request.tokens.items():

            payload[key] = value

        response = self.client.request(
            "POST",
            self._url(VERIFY_LOOKUP),
            data=payload,
        )

        return map_response(response)

    def status(
        self,
        message_id: str,
    ) -> SMSStatus:

        response = self.client.request(
            "GET",
            self._url(SMS_STATUS),
            params={"messageid": message_id},
        )

        return map_status(response)

    def account_info(
        self,
    ) -> dict[str, Any]:

        return self.client.request(
            "GET",
            self._url(ACCOUNT_INFO),
        )
