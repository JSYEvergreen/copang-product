import httpx
from fastapi import Header
from overrides import override
from typing import Optional

from domain.token.service.tokenService import TokenServiceModel
from domain.token.service.token import (
    TakeUserInfoOut
)
from infra.token.token import (
    TokenConfig
)
from infra.token.tokenException import TokenException


class TokenServiceModule(TokenServiceModel):
    def __init__(
            self,
            config: TokenConfig
    ):
        self.config: TokenConfig = config

    @override
    async def take_user_info(self, Token: Optional[str] = Header(...)) -> TakeUserInfoOut:
        try:
            response: httpx.Response = httpx.get(
                url=self.config.request_url,
                headers=dict(
                    Authorization=f"Bearer {Token}",
                )
            )
        except httpx.ConnectError:

            # Todo: Error Detail Msg Update
            raise TokenException(
                status_code=500,
                detail=dict(msg="test")
            )

        json_response: dict = response.json()

        if response.status_code == 500 and json_response.get("errorCode"):
            raise TokenException(
                status_code=response.status_code,
                detail=json_response
            )

        else:
            return TakeUserInfoOut(
                id=json_response.get("content").get("id"),
                userId=json_response.get("content").get("userId")
            )


