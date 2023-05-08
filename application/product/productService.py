from overrides import override

from domain.product.service.productService import ProductInterface
from domain.product.repo.productRepo import ProductRepo
from domain.product.service.product import (
    FindProductIn,
    FindProductOut,
    FindProductsIn,
    FindProductsOut,
    FindBaseProductsOut
)


class ProductService(ProductInterface):
    def __init__(
        self,
        db: ProductRepo
    ):
        self.db: ProductRepo = db

    @override
    def find_product(self, find_product_in: FindProductIn) -> FindProductOut:
        pass

    @override
    def find_products(self, find_products_in: FindProductsIn) -> FindProductsOut:
        pass

    @override
    def find_base_products(self) -> FindBaseProductsOut:
        pass 
