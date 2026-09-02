from collections.abc import Callable

from iranio.core.config import ProviderConfig
from iranio.sms.base import BaseSMSProvider
from iranio.sms.providers.kavenegar import Kavenegar

SMSProviderFactory = Callable[
    [ProviderConfig],
    BaseSMSProvider,
]


SMS_PROVIDERS: dict[str, SMSProviderFactory] = {
    "kavenegar": Kavenegar,
}


def get_sms_provider(
    name: str,
    config: ProviderConfig,
) -> BaseSMSProvider:

    provider = SMS_PROVIDERS.get(name)

    if provider is None:
        raise ValueError(f"Unsupported SMS provider: {name}")

    return provider(config)
