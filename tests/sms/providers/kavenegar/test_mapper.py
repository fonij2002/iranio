from iranio.sms.models import (
    SendSMSRequest,
)
from iranio.sms.providers.kavenegar.request_mapper import (
    KavenegarMapper,
)


def test_kavenegar_send_mapping():

    mapper = KavenegarMapper()

    payload = mapper.map_send(
        SendSMSRequest(
            phone="09121234567",
            message="hello",
        )
    )

    assert payload == {
        "receptor": "09121234567",
        "message": "hello",
    }
