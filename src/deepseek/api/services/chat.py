from typing import Dict, Any, List
from ...core.logging import ClientLogger
from ..transport import APITransport

class ChatCompletionService:
    def __init__(self, transport: APITransport):
        self.transport = transport
        self.logger = ClientLogger().logger

    def create(
        self,
        messages: List[Dict[str, Any]],
        model: str = "deepseek-chat",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> Dict[str, Any]:
        payload = {
            "messages": messages,
            "model": model,
            "temperature": max(0, min(2.0, temperature)),
            "max_tokens": max(1, min(4096, max_tokens)),
            **kwargs
        }
        self.logger.info(f"Creating chat completion with model {model}")
        return self.transport.request("POST", "/chat/completions", json=payload)