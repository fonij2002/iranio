from pydantic import BaseModel


class ProviderConfig(BaseModel):

    api_key: str

    base_url: str | None = None

    timeout: float = 10.0
