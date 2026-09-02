from typing import Any

from iranio.core.config import ProviderConfig
from iranio.sms.registry import get_sms_provider
from iranio.sms.service import SMSService


class Iranio:
    """
    Main entry point for iranio SDK.
    """

    def __init__(
        self,
        sms: dict[str, Any] | None = None,
    ) -> None:

        self.sms: SMSService | None = None

        if sms:

            self._initialize_sms(sms)

    def _initialize_sms(
        self,
        config: dict[str, Any],
    ) -> None:

        provider = config.get("provider")

        api_key = config.get("api_key")

        if not provider:
            raise ValueError("SMS provider is required")

        if not api_key:
            raise ValueError("SMS api_key is required")

        provider_instance = get_sms_provider(
            provider,
            ProviderConfig(api_key=api_key),
        )

        self.sms = SMSService(provider_instance)
