from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from typing import Callable

from infra.token.tokenService import TokenServiceModule


class TokenContainer(DeclarativeContainer):
    token_service: Callable = TokenServiceModule.take_user_info
