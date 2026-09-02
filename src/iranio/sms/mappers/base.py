from abc import ABC, abstractmethod
from typing import Any

from iranio.sms.models import (
    BulkSMSRequest,
    OTPRequest,
    SendSMSRequest,
)


class BaseSMSMapper(ABC):
    """
    Base mapper for converting internal models
    to provider specific payloads.
    """

    @abstractmethod
    def map_send(
        self,
        request: SendSMSRequest,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def map_bulk(
        self,
        request: BulkSMSRequest,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def map_otp(
        self,
        request: OTPRequest,
    ) -> dict[str, Any]:
        pass
