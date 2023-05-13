from abc import ABCMeta, abstractmethod
from typing import List

from domain.product.service.product import (
    TakeBaseInfoIn, TakeBaseInfoOut,
    TakePaidInfoIn, TakePaidInfoOut,
    TakeStatusIn, TakeStatusOut,
    TakeSearchInfoIn, TakeSearchInfoOut,
    TakeDuplicateInfoIn, TakeDuplicateInfoOut,
    TakePolicyIn, TakePolicyOut
)


class ProductServiceModel(metaclass=ABCMeta):
    @abstractmethod
    def take_base_product_info(self, take_base_info_in: TakeBaseInfoIn) -> List[TakeBaseInfoOut]:
        pass

    @abstractmethod
    def take_paid_product_info(self, take_paid_info_in: TakePaidInfoIn) -> TakePaidInfoOut:
        pass

    @abstractmethod
    def take_status_of_product(self, take_status_in: TakeStatusIn) -> TakeStatusOut:
        pass

    @abstractmethod
    def take_search_product_info(self, take_search_in: TakeSearchInfoIn) -> List[TakeSearchInfoOut]:
        pass

    @abstractmethod
    def take_duplicate_product_info(self, take_duplicate_in: TakeDuplicateInfoIn) -> List[TakeDuplicateInfoOut]:
        pass

    @abstractmethod
    def take_product_policy(self, take_policy_in: TakePolicyIn) -> TakePolicyOut:
        pass
