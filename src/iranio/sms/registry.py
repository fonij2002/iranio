from collections.abc import Callable

from iranio.core.config import ProviderConfig
from iranio.sms.base import BaseSMSProvider
from iranio.sms.providers.ghasedak import Ghasedak
from iranio.sms.providers.kavenegar import Kavenegar
from iranio.sms.providers.smsir import SMSIR

SMSProviderFactory = Callable[
    [ProviderConfig],
    BaseSMSProvider,
]


SMS_PROVIDERS: dict[
    str,
    SMSProviderFactory,
] = {
    "kavenegar": Kavenegar,
    "ghasedak": Ghasedak,
    "smsir": SMSIR,
}


def get_sms_provider(
    name: str,
    config: ProviderConfig,
) -> BaseSMSProvider:

    factory = SMS_PROVIDERS.get(name)

    if factory is None:

        raise ValueError(f"Unsupported SMS provider: {name}")

    return factory(config)
