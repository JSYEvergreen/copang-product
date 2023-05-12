from dataclasses import dataclass
from dependency_injector.containers import DeclarativeContainer

from container.product.productContainer import ProductContainer
from container.token.tokenContainer import TokenContainer


@dataclass
class ContainerConstructor:
    product_container: DeclarativeContainer = ProductContainer()
    token_container: DeclarativeContainer = TokenContainer()

