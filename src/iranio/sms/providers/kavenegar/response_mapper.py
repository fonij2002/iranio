from typing import Any

from iranio.sms.models import (
    SMSResponse,
    SMSStatus,
)


def map_response(
    data: dict[str, Any],
) -> SMSResponse:
    """
    Map Kavenegar API response
    into iranio unified response model.
    """

    result = data.get(
        "return",
        {},
    )

    status = result.get("status")

    entries = data.get(
        "entries",
        [],
    )

    message_ids = [
        str(entry.get("messageid")) for entry in entries if entry.get("messageid")
    ]

    return SMSResponse(
        success=status == 200,
        message=result.get("message"),
        message_ids=message_ids,
        raw=data,
    )


def map_status(
    data: dict[str, Any],
) -> SMSStatus:
    """
    Map Kavenegar message status response.
    """

    entries = data.get(
        "entries",
        [],
    )

    entry = entries[0] if entries else {}

    return SMSStatus(
        message_id=str(
            entry.get(
                "messageid",
                "",
            )
        ),
        status=str(
            entry.get(
                "status",
                "",
            )
        ),
        description=entry.get("statustext"),
    )
