from iranio import Iranio


def test_create_sdk():

    client = Iranio(
        sms={
            "provider": "kavenegar",
            "api_key": "test",
        }
    )

    assert client.sms is not None
