import tomlkit
from dependency_injector.containers import DeclarativeContainer
from typing import Callable

from domain.token.service.tokenService import TokenServiceModel
from infra.token.token import TokenConfig
from infra.token.tokenService import TokenServiceModule


class TokenContainer(DeclarativeContainer):
    with open("core/tokenConfig.toml") as config_file:
        config: TokenConfig = TokenConfig(**tomlkit.load(config_file))

    token_class: TokenServiceModel = TokenServiceModule(
        config=config
    )

    token_service: Callable = token_class.take_user_info
