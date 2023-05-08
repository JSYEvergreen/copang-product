from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton

from domain.product.service.productService import ProductInterface
from application.product.productService import ProductService
from infra.postgresql.product.productRepo import ProductRepo


class ProductContainer(DeclarativeContainer):
    product_service: ProductInterface = Singleton(
        ProductService,
        db=Singleton(
            ProductRepo
        )
    )

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            "None"
        ],
        packages=[
            "None"
        ]
    )
