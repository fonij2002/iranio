import httpx

from iranio.core.config import ProviderConfig
from iranio.sms.models import (
    SendSMSRequest,
)
from iranio.sms.providers.smsir import (
    SMSIR,
)


def test_smsir_send(
    respx_mock,
):

    respx_mock.post("https://api.sms.ir/v1/send/bulk").mock(
        return_value=httpx.Response(
            200,
            json={
                "status": 1,
                "message": "Success",
                "data": ["12345"],
            },
        )
    )

    client = SMSIR(ProviderConfig(api_key="test"))

    response = client.send(
        SendSMSRequest(
            phone="09121234567",
            message="hello",
        )
    )

    assert response.success is True

    assert response.message_ids == ["12345"]
