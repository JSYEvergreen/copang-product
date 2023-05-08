from abc import ABCMeta, abstractmethod

from domain.product.service.product import (
    GetProductIn,
    GetProductOut,
    GetProductsDateOut
)


class ProductRepo(metaclass=ABCMeta):
    @abstractmethod
    def get_one_product(self, get_one_in: GetProductIn) -> GetProductOut:
        pass

    @abstractmethod
    def get_plural_products(self, get_plural_in: GetProductIn) -> GetProductOut:
        pass

    @abstractmethod
    def get_products_with_date(self) -> GetProductsDateOut:
        pass
