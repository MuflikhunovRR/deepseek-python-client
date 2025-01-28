from pydantic import BaseModel, Field, SecretStr, field_validator
from datetime import timedelta
import os

class ClientConfig(BaseModel):
    api_key: SecretStr = Field(..., alias="DEEPSEEK_API_KEY")
    base_url: str = Field("https://api.deepseek.com/v1", alias="DEEPSEEK_BASE_URL")
    timeout: timedelta = Field(timedelta(seconds=30))
    max_retries: int = Field(3, ge=0, le=5)
    log_level: str = Field("INFO", pattern=r"^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$")

    @field_validator("base_url")
    def validate_base_url(cls, v: str) -> str:
        if not v.startswith(("http://", "https://")):
            raise ValueError("Invalid base URL format")
        return v.rstrip("/")
    
    class Config:
        arbitrary_types_allowed = True
        env_file = ".env"