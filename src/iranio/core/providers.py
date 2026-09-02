from abc import ABC, abstractmethod
from typing import Any

from iranio.core.models import APIResponse


class BaseProvider(ABC):
    """
    Base interface for all providers.
    """

    @abstractmethod
    def send(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> APIResponse:
        """
        Send request to provider.
        """
        pass
