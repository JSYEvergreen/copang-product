from pydantic import BaseModel


class TakeUserInfoOut(BaseModel):
    id: int
    userId: str


