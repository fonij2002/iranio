
from iranio.core.client import BaseClient
from iranio.core.config import ProviderConfig


class SMSProviderClient(BaseClient):
    """
    Base HTTP client for SMS providers.
    """

    def __init__(
        self,
        config: ProviderConfig,
        timeout: float = 10.0,
    ) -> None:

        super().__init__(timeout=timeout)

        self.config = config
