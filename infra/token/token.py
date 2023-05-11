from pydantic import BaseModel


class TokenConfig(BaseModel):
    request_url: str
