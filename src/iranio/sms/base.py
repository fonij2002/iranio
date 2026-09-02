from abc import abstractmethod

from iranio.core.config import ProviderConfig
from iranio.core.providers import BaseProvider
from iranio.sms.models import (
    BulkSMSRequest,
    OTPRequest,
    SendSMSRequest,
    SMSAccountInfo,
    SMSResponse,
    SMSStatus,
)


class BaseSMSProvider(
    BaseProvider[
        SendSMSRequest,
        SMSResponse,
    ]
):

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        self.config = config

    @abstractmethod
    def account_info(
        self,
    ) -> SMSAccountInfo:
        pass

    @abstractmethod
    def send(
        self,
        request: SendSMSRequest,
    ) -> SMSResponse:
        pass

    @abstractmethod
    def send_bulk(
        self,
        request: BulkSMSRequest,
    ) -> SMSResponse:
        pass

    @abstractmethod
    def send_otp(
        self,
        request: OTPRequest,
    ) -> SMSResponse:
        pass

    @abstractmethod
    def status(
        self,
        message_id: str,
    ) -> SMSStatus:
        pass
