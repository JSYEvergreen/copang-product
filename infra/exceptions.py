from dataclasses import dataclass

from infra.token.tokenException import TokenException


@dataclass
class InfraExceptions:
    token_exception: TokenException = TokenException


infra_exceptions: InfraExceptions = InfraExceptions()

