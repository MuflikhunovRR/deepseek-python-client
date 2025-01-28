class DeepSeekError(Exception):
    """Base exception for all client errors."""
    pass

class AuthenticationError(DeepSeekError):
    """Invalid authentication credentials."""
    pass

class RateLimitError(DeepSeekError):
    """API rate limit exceeded."""
    pass

class APIError(DeepSeekError):
    """Generic API error with status code."""
    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.status_code = status_code

class PaymentRequiredError(APIError):
    """Specific error for HTTP 402 Payment Required."""
    def __init__(self, message: str = "Payment is required to access this resource."):
        super().__init__(message, status_code=402)
