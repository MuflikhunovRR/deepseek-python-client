import pytest
from src.deepseek.client import DeepSeekClient
from src.deepseek.core.exceptions import AuthenticationError

def test_client_initialization():
    # Test with missing API key
    with pytest.raises(ValueError):
        DeepSeekClient(api_key=None)

    # Test with invalid API key format
    with pytest.raises(AuthenticationError):
        with DeepSeekClient(api_key="invalid-key") as client:
            client.chat.create(messages=[{"role": "user", "content": "test"}])