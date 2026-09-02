from typing import Any

import httpx

from iranio.core.exceptions import NetworkError


class BaseClient:
    """
    Base HTTP client used by all providers.
    """

    def __init__(
        self,
        timeout: float = 10.0,
    ) -> None:

        self.client = httpx.Client(timeout=timeout)

    def request(
        self,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> dict[str, Any]:

        try:

            response = self.client.request(
                method,
                url,
                **kwargs,
            )

            response.raise_for_status()

            data: Any = response.json()

            if not isinstance(data, dict):
                raise NetworkError("API response is not a JSON object")

            return data

        except httpx.HTTPError as exc:

            raise NetworkError(str(exc)) from exc
