import httpx


class AsyncBaseClient:

    def __init__(
        self,
        timeout: float = 10.0,
    ) -> None:

        self.client = httpx.AsyncClient(timeout=timeout)
