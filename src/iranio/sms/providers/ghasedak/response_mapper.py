from typing import Any

from iranio.sms.models import (
    SMSResponse,
    SMSStatus,
)


def map_response(
    data: dict[str, Any],
) -> SMSResponse:

    status = data.get("result")

    success = status in (
        200,
        "200",
        True,
    )

    message_ids = []

    if "items" in data:

        message_ids = [str(item) for item in data["items"]]

    return SMSResponse(
        success=success,
        message=data.get("message"),
        message_ids=message_ids,
        raw=data,
    )


def map_status(
    data: dict[str, Any],
) -> SMSStatus:

    return SMSStatus(
        message_id=str(
            data.get(
                "messageId",
                "",
            )
        ),
        status=str(
            data.get(
                "status",
                "",
            )
        ),
        description=data.get("description"),
    )
