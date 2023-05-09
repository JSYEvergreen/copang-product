from overrides import override
from typing import List

from domain.product.repo.productRepo import ProductRepoModel
from domain.product.repo.product import (
    Product, ProductPolicy,
    GetOneProductByIdIn,
    GetOneProductByCodeIn,
    GetProductPolicyIn,
    GetProductStatusIn, GetProductStatusOut,
    GetPluralProductByIdIn,
    GetPluralProductByCodeIn
)
from infra.postgresql.core import PostGreSQLCore


class ProductRepoModule(ProductRepoModel, PostGreSQLCore):
    def __init__(self):
        super().__init__()
        PostGreSQLCore.__init__(self)

    @override
    def get_one_product_by_id(self, get_product_in: GetOneProductByIdIn) -> Product:
        pass

    @override
    def get_plural_product_by_id(self, get_product_in: GetPluralProductByIdIn) -> List[Product]:
        pass

    @override
    def get_one_product_by_code(self, get_product_in: GetOneProductByCodeIn) -> Product:
        pass

    @override
    def get_plural_product_by_code(self, get_product_in: GetPluralProductByCodeIn) -> List[Product]:
        pass

    @override
    def get_product_policy(self, get_policy_in: GetProductPolicyIn) -> ProductPolicy:
        pass

    @override
    def get_product_status(self, get_status_in: GetProductStatusIn) -> GetProductStatusOut:
        pass


