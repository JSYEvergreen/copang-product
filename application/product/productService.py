from overrides import override
from typing import List

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
from domain.product.repo.productRepo import (
    GetProductStatusIn, GetProductStatusOut,
    GetPluralProductByIdIn,
    GetProductPolicyIn,
    GetRandomProduct,
    GetProductsByCodeIn,
    Product,
    ProductPolicy
)
from application.product.productException import (
    ProductException,
    ProductErrorTemplate
)


class ProductServiceModule(ProductServiceModel):
    def __init__(
            self,
            repo: ProductRepoModel
    ) -> None:
        self.repo: ProductRepoModel = repo

    @override
    def take_base_product_info(self, take_base_info_in: TakeBaseInfoIn) -> List[TakeBaseInfoOut]:
        random_products_in: GetRandomProduct = GetRandomProduct(
            count=take_base_info_in.productCount
        )

        random_products_out: List[Product] = self.repo.get_random_product(
            get_random_product=random_products_in
        )

        if not random_products_out:
            raise ProductException(
                status_code=500,
                detail=ProductErrorTemplate(
                    message="물품 리스트가 없습니다."
                )
            )

        return [
            TakeBaseInfoOut(
                productName=info.name,
                productDescription=info.description,
                productInformation=info.information,
                productQuantity=info.quantity,
                productCost=info.cost,
                productSellerId=info.seller_id,
                productId=int(info.id),
                productCode=info.code,
                productIsSale=info.is_sale
            ) for info in random_products_out
        ]

    @override
    def take_paid_product_info(self, take_paid_info_in: TakePaidInfoIn) -> TakePaidInfoOut:
        # Todo: Update After 5/14 Meeting...
        raise ProductException(
            status_code=500,
            detail=ProductErrorTemplate(
                message="현재 구현되지 않은 요청입니다."
            )
        )

    @override
    def take_status_of_product(self, take_status_in: TakeStatusIn) -> TakeStatusOut:
        product_status_in: GetProductStatusIn = GetProductStatusIn(
            productId=str(take_status_in.productId),
            userId=take_status_in.userId
        )

        product_status_out: GetProductStatusOut = self.repo.get_product_status(
            get_status_in=product_status_in
        )

        if product_status_out is None:
            raise ProductException(
                status_code=500,
                detail=ProductErrorTemplate(
                    message="해당 물품이 없습니다."
                )
            )

        return TakeStatusOut(
            productStatus=product_status_out.status
        )

    @override
    def take_search_product_info(self, take_search_in: TakeSearchInfoIn) -> List[TakeSearchInfoOut]:
        product_search_in: GetPluralProductByIdIn = GetPluralProductByIdIn(
            productIds=[
                str(product_id) for product_id in take_search_in.productIds
            ],
            userId=take_search_in.userId
        )

        product_search_out: List[Product] = self.repo.get_plural_product_by_id(
            get_product_in=product_search_in
        )

        if not product_search_out:
            raise ProductException(
                status_code=500,
                detail=ProductErrorTemplate(
                    message="물품 리스트가 없습니다."
                )
            )

        return [
            TakeSearchInfoOut(
                productName=info.name,
                productDescription=info.description,
                productInformation=info.information,
                productQuantity=info.quantity,
                productCost=info.cost,
                productSellerId=info.seller_id,
                productId=int(info.id),
                productCode=info.code,
                productIsSale=info.is_sale
            ) for info in product_search_out
        ]

    @override
    def take_duplicate_product_info(self, take_duplicate_in: TakeDuplicateInfoIn) -> List[TakeDuplicateInfoOut]:
        duplicate_in: GetProductsByCodeIn = GetProductsByCodeIn(
            productCode=take_duplicate_in.productCode,
            userId=take_duplicate_in.userId
        )

        duplicate_out: List[Product] = self.repo.get_products_by_code(
            get_products=duplicate_in
        )

        if not duplicate_out:
            raise ProductException(
                status_code=500,
                detail=ProductErrorTemplate(
                    message="물품 리스트가 없습니다."
                )
            )

        return [
            TakeDuplicateInfoOut(
                productName=info.name,
                productDescription=info.description,
                productInformation=info.information,
                productQuantity=info.quantity,
                productCost=info.cost,
                productSellerId=info.seller_id,
                productId=int(info.id),
                productIsSale=info.is_sale,
                productCreatedAt=info.created_at,
                productUpdatedAt=info.updated_at
            ) for info in duplicate_out
        ]

    @override
    def take_product_policy(self, take_policy_in: TakePolicyIn) -> TakePolicyOut:
        policy_in: GetProductPolicyIn = GetProductPolicyIn(
            productId=str(take_policy_in.productId),
            userId=take_policy_in.userId
        )

        policy_out: ProductPolicy = self.repo.get_product_policy(
            get_policy_in=policy_in
        )

        if policy_out is None:
            raise ProductException(
                status_code=500,
                detail=ProductErrorTemplate(
                    message="해당 물품이 없습니다."
                )
            )

        return TakePolicyOut(
            productPolicy=int(policy_out.policy),
            productType=policy_out.type
        )

