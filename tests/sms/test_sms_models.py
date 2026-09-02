from iranio.sms import SendSMSRequest


def test_send_sms_request():

    request = SendSMSRequest(phone="09121234567", message="hello")

    assert request.phone == "09121234567"
