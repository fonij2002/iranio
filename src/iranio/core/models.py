from typing import Any

from pydantic import BaseModel


class APIResponse(BaseModel):
    """
    Common response model.
    """

    success: bool
    message: str | None = None
    data: dict[str, Any] | None = None
    raw: dict[str, Any] | None = None
