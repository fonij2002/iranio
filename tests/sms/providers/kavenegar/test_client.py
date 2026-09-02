import httpx

from iranio.core.config import ProviderConfig
from iranio.sms.models import SendSMSRequest
from iranio.sms.providers.kavenegar import Kavenegar


def test_kavenegar_send(respx_mock):

    respx_mock.post("https://api.kavenegar.com/v1/test/sms/send.json").mock(
        return_value=httpx.Response(
            200,
            json={
                "return": {
                    "status": 200,
                    "message": "Success",
                },
                "entries": [{"messageid": "12345"}],
            },
        )
    )

    client = Kavenegar(ProviderConfig(api_key="test"))

    response = client.send(SendSMSRequest(phone="09121234567", message="hello"))

    assert response.success is True
    assert response.message_ids == ["12345"]
