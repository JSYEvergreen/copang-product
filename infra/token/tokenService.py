import httpx
from fastapi import Header
from overrides import override
from typing import Optional

from domain.token.service.tokenService import TokenServiceModel
from domain.token.service.token import (
    TakeUserInfoOut
)


class TokenServiceModule(TokenServiceModel):
    @classmethod
    @override
    async def take_user_info(cls, token: Optional[str] = Header(...)) -> TakeUserInfoOut:
        pass


