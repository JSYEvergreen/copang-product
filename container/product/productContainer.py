from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton

from domain.product.service.productService import ProductServiceModel
from application.product.productService import ProductServiceModule
from infra.postgresql.product.productRepo import ProductRepoModule


class ProductContainer(DeclarativeContainer):
    product_service: ProductServiceModel = Singleton(
        ProductServiceModule,
        repo=Singleton(
            ProductRepoModule
        )
    )

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            "api.product.productController"
        ]
    )
