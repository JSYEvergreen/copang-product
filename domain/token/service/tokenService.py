from abc import ABCMeta, abstractmethod
from fastapi import Header
from typing import Optional

from domain.token.service.token import (
    TakeUserInfoOut
)


class TokenServiceModel(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    async def take_user_info(cls, token: Optional[str] = Header(...)) -> TakeUserInfoOut:
        pass

