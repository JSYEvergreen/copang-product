from overrides import override

from domain.product.repo.productRepo import ProductRepo
from domain.product.service.product import (
    GetProductIn,
    GetProductOut,
    GetProductsDateOut
)
from infra.postgresql.core import PostGreSQLCore


class PostgresProductRepo(ProductRepo, PostGreSQLCore):
    def __init__(self):
        super().__init__()
        PostGreSQLCore.__init__(self=self)

    @override
    def get_one_product(self, get_one_in: GetProductIn) -> GetProductOut:
        pass

    @override
    def get_plural_products(self, get_plural_in: GetProductIn) -> GetProductOut:
        pass

    @override
    def get_products_with_date(self) -> GetProductsDateOut:
        pass


