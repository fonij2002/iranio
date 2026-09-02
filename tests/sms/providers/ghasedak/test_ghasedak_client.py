import httpx

from iranio.core.config import ProviderConfig
from iranio.sms.models import (
    SendSMSRequest,
)
from iranio.sms.providers.ghasedak import (
    Ghasedak,
)


def test_ghasedak_send(
    respx_mock,
):

    respx_mock.post("https://gateway.ghasedak.me/rest/api/v1/SendSMS").mock(
        return_value=httpx.Response(
            200,
            json={
                "result": 200,
                "message": "success",
                "items": ["12345"],
            },
        )
    )

    client = Ghasedak(ProviderConfig(api_key="test"))

    response = client.send(
        SendSMSRequest(
            phone="09121234567",
            message="hello",
        )
    )

    assert response.success is True

    assert response.message_ids == ["12345"]
