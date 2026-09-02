from abc import ABC, abstractmethod
from typing import Generic, TypeVar

RequestType = TypeVar("RequestType")

ResponseType = TypeVar("ResponseType")


class BaseProvider(ABC, Generic[RequestType, ResponseType]):
    """
    Generic provider interface.
    """

    @abstractmethod
    def send(
        self,
        request: RequestType,
    ) -> ResponseType:
        """
        Execute provider operation.
        """
