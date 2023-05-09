from overrides import override

from domain.product.service.productService import ProductServiceModel
from domain.product.repo.productRepo import ProductRepoModel
from domain.product.service.product import (
    TakeBaseInfoIn, TakeBaseInfoOut,
    TakePaidInfoIn, TakePaidInfoOut,
    TakeStatusIn, TakeStatusOut,
    TakeSearchInfoIn, TakeSearchInfoOut,
    TakeDuplicateInfoIn, TakeDuplicateInfoOut,
    TakePolicyIn, TakePolicyOut
)


class ProductServiceModule(ProductServiceModel):
    def __init__(
            self,
            repo: ProductRepoModel
    ) -> None:
        self.repo: ProductRepoModel = repo

    @override
    def take_base_product_info(self, take_base_info_in: TakeBaseInfoIn) -> TakeBaseInfoOut:
        pass

    @override
    def take_paid_product_info(self, take_paid_info_in: TakePaidInfoIn) -> TakePaidInfoOut:
        pass

    @override
    def take_status_of_product(self, take_status_in: TakeStatusIn) -> TakeStatusOut:
        pass

    @override
    def take_search_product_info(self, take_search_in: TakeSearchInfoIn) -> TakeSearchInfoOut:
        pass

    @override
    def take_duplicate_product_info(self, take_duplicate_in: TakeDuplicateInfoIn) -> TakeDuplicateInfoOut:
        pass

    @override
    def take_product_policy(self, take_policy_in: TakePolicyIn) -> TakePolicyOut:
        pass

