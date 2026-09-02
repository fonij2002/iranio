class IranioException(Exception):
    """
    Base exception for all iranio errors.
    """


class AuthenticationError(IranioException):
    """
    Raised when authentication with provider fails.
    """


class InvalidRequestError(IranioException):
    """
    Raised when request data is invalid.
    """


class ProviderError(IranioException):
    """
    Raised when provider returns an error.
    """


class NetworkError(IranioException):
    """
    Raised when network communication fails.
    """


class SMSProviderError(ProviderError):
    """
    SMS provider error.
    """
