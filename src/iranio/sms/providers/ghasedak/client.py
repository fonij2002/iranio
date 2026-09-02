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
    ACCOUNT,
    BASE_URL,
    OTP,
    SEND,
    STATUS,
)
from .request_mapper import (
    GhasedakMapper,
)
from .response_mapper import (
    map_response,
    map_status,
)


class Ghasedak(BaseSMSProvider):

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        super().__init__(config)

        self.client = SMSProviderClient(config)

        self.mapper = GhasedakMapper()

    def _url(
        self,
        endpoint: str,
    ) -> str:

        return f"{BASE_URL}" f"{endpoint}"

    def _headers(self) -> dict[str, str]:

        return {
            "apikey": self.config.api_key,
            "Content-Type": "application/json",
        }

    def send(
        self,
        request: SendSMSRequest,
    ) -> SMSResponse:

        response = self.client.request(
            "POST",
            self._url(SEND),
            headers=self._headers(),
            json=self.mapper.map_send(request),
        )

        return map_response(response)

    def send_bulk(
        self,
        request: BulkSMSRequest,
    ) -> SMSResponse:

        response = self.client.request(
            "POST",
            self._url(SEND),
            headers=self._headers(),
            json=self.mapper.map_bulk(request),
        )

        return map_response(response)

    def send_otp(
        self,
        request: OTPRequest,
    ) -> SMSResponse:

        response = self.client.request(
            "POST",
            self._url(OTP),
            headers=self._headers(),
            json=self.mapper.map_otp(request),
        )

        return map_response(response)

    def status(
        self,
        message_id: str,
    ) -> SMSStatus:

        response = self.client.request(
            "GET",
            self._url(STATUS),
            headers=self._headers(),
            params={"messageId": message_id},
        )

        return map_status(response)

    def account_info(
        self,
    ) -> dict[str, Any]:

        return self.client.request(
            "GET",
            self._url(ACCOUNT),
            headers=self._headers(),
        )
