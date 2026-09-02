from iranio.core.providers import BaseProvider
from iranio.sms.models import (
    SendSMSRequest,
    SendSMSResponse,
)


class BaseSMSProvider(
    BaseProvider[
        SendSMSRequest,
        SendSMSResponse,
    ]
):
    """
    Base SMS provider interface.
    """
