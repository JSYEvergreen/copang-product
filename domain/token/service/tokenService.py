from abc import ABCMeta, abstractmethod
from fastapi import Header
from typing import Optional

from domain.token.service.token import (
    TakeUserInfoOut
)


class TokenServiceModel(metaclass=ABCMeta):
    @abstractmethod
    async def take_user_info(self, Token: Optional[str] = Header(...)) -> TakeUserInfoOut:
        pass

