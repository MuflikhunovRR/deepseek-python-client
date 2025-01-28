import os
from datetime import timedelta
from typing import Optional
from .core.config import ClientConfig
from .core.logging import ClientLogger
from .api.transport import APITransport
from .api.services import ChatCompletionService

class DeepSeekClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        config: Optional[ClientConfig] = None
    ):
        if not config:
            api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
            if not api_key:
                raise ValueError("API key must be provided or set in environment")

            config = ClientConfig(
                api_key=api_key,
                base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1"),
                timeout=timedelta(seconds=int(os.getenv("DEEPSEEK_TIMEOUT", 30))),
                max_retries=int(os.getenv("DEEPSEEK_MAX_RETRIES", 3)),
                log_level=os.getenv("DEEPSEEK_LOG_LEVEL", "INFO"),
            )

        self.config = config
        self.logger = ClientLogger(level=config.log_level).logger
        self.transport = APITransport(config)

        # Initialize services
        self.chat = ChatCompletionService(self.transport)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.transport.session:
            self.transport.session.close()
            self.logger.info("Client session closed")