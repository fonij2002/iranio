from typing import Any

from iranio.sms.models import (
    SMSResponse,
    SMSStatus,
)


def map_response(
    data: dict[str, Any],
) -> SMSResponse:

    status = data.get("status")

    success = status in (
        1,
        200,
        "1",
    )

    message_ids: list[str] = []

    data_items = data.get(
        "data",
        [],
    )

    if isinstance(data_items, list):

        message_ids = [str(item) for item in data_items]

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
        description=data.get("message"),
    )
