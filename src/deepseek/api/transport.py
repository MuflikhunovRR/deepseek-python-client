import httpx
from typing import Dict, Any
from ..core.exceptions import APIError, AuthenticationError, RateLimitError
from ..core.config import ClientConfig
from ..core.logging import ClientLogger

class APITransport:
    def __init__(self, config: ClientConfig):
        self.config = config
        self.logger = ClientLogger().logger
        self.session = httpx.Client(
            base_url=config.base_url,
            timeout=config.timeout.total_seconds(),
            transport=httpx.HTTPTransport(retries=config.max_retries),
        )
        self.session.headers.update({
            "Authorization": f"Bearer {config.api_key.get_secret_value()}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        try:
            response = self.session.request(method, endpoint, **kwargs)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            self._handle_http_error(e)
        except Exception as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise APIError(str(e)) from e

    def _handle_http_error(self, e: httpx.HTTPStatusError):
        self.logger.error(f"API Error: {e.response.status_code} - {e.response.text}")
        if e.response.status_code == 401:
            raise AuthenticationError("Invalid API credentials")
        elif e.response.status_code == 429:
            raise RateLimitError("API rate limit exceeded")
        raise APIError(
            f"API request failed with status {e.response.status_code}",
            e.response.status_code
        )