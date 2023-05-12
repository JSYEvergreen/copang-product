from abc import ABCMeta, abstractmethod
from typing import List

from domain.product.repo.product import (
    Product, ProductPolicy,
    GetOneProductByIdIn,
    GetOneProductByCodeIn,
    GetProductPolicyIn,
    GetProductStatusIn, GetProductStatusOut,
    GetPluralProductByIdIn,
    GetPluralProductByCodeIn,
    GetRandomProduct
)


class ProductRepoModel(metaclass=ABCMeta):
    @abstractmethod
    def get_one_product_by_id(self, get_product_in: GetOneProductByIdIn) -> Product:
        pass

    @abstractmethod
    def get_plural_product_by_id(self, get_product_in: GetPluralProductByIdIn) -> List[Product]:
        pass

    @abstractmethod
    def get_one_product_by_code(self, get_product_in: GetOneProductByCodeIn) -> Product:
        pass

    @abstractmethod
    def get_plural_product_by_code(self, get_product_in: GetPluralProductByCodeIn) -> List[Product]:
        pass

    @abstractmethod
    def get_product_policy(self, get_policy_in: GetProductPolicyIn) -> ProductPolicy:
        pass

    @abstractmethod
    def get_product_status(self, get_status_in: GetProductStatusIn) -> GetProductStatusOut:
        pass

    @abstractmethod
    def get_random_product(self, get_random_product: GetRandomProduct) -> List[Product]:
        pass


