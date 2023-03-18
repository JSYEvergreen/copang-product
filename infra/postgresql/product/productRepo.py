from overrides import override

from domain.product.productRepo import ProductRepo
from domain.product.product import (
    GetProductIn,
    GetProductOut,
    GetProductsIn,
    GetProductsOut,
    GetProductsDateOut
)
from infra.postgresql.core import PostGreSQLCore
from infra.postgresql.product.productSchema import Product


class PostgresProductRepo(ProductRepo, PostGreSQLCore):
    def __init__(self):
        super().__init__()

    @override
    def get_one_product(self, get_one_in: GetProductIn) -> GetProductOut:
        pass

    @override
    def get_plural_products(self, get_plural_in: GetProductIn) -> GetProductOut:
        pass

    @override
    def get_products_with_date(self) -> GetProductsDateOut:
        pass


