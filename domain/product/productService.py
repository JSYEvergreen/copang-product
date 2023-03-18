from abc import ABCMeta, abstractmethod

from domain.product.product import (
    FindProductIn,
    FindProductOut,
    FindProductsIn,
    FindProductsOut,
    FindBaseProductsOut
)


class ProductInterface(metaclass=ABCMeta):
    @abstractmethod
    def find_product(self, find_product_in: FindProductIn) -> FindProductOut:
        pass

    @abstractmethod
    def find_products(self, find_products_in: FindProductsIn) -> FindProductsOut:
        pass

    @abstractmethod
    def find_base_products(self) -> FindBaseProductsOut:
        pass


