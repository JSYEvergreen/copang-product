from dataclasses import dataclass
from dependency_injector.containers import DeclarativeContainer

from container.product.productContainer import ProductContainer


@dataclass
class ContainerConstructor:
    product_container: DeclarativeContainer = ProductContainer()


BASE_CONTAINER: dataclass = ContainerConstructor()


