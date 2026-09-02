from iranio.core.config import ProviderConfig
from iranio.sms.providers.kavenegar import (
    Kavenegar,
)


def test_create_kavenegar():

    client = Kavenegar(ProviderConfig(api_key="test"))

    assert client.config.api_key == "test"
