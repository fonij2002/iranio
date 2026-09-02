from iranio.core import APIResponse


def test_api_response():
    response = APIResponse(success=True, message="ok")
    assert response.success is True
