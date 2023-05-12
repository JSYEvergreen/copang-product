from fastapi import APIRouter, Depends
from typing import List
from dependency_injector.wiring import inject, Provide

from domain.product.service.productService import ProductServiceModel
from domain.token.service.token import TakeUserInfoOut
from domain.product.service.product import (
    TakeBaseInfoIn, TakeBaseInfoOut,
    TakePaidInfoIn, TakePaidInfoOut,
    TakeStatusIn, TakeStatusOut,
    TakeSearchInfoIn, TakeSearchInfoOut,
    TakeDuplicateInfoIn, TakeDuplicateInfoOut,
    TakePolicyIn, TakePolicyOut
)
from container.product.productContainer import ProductContainer
from container.token.tokenContainer import TokenContainer
from api.product.product import (
    ProductPolicyRequest, ProductPolicyResponse,
    ProductDuplicateRequest, ProductDuplicateResponse,
    ProductSearchRequest, ProductSearchResponse,
    ProductStatusRequest, ProductStatusResponse,
    ProductPaidRequest, ProductPaidResponse,
    ProductBaseRequest, ProductBaseResponse
)


product_router: APIRouter = APIRouter(
    prefix="/product"
)


@product_router.get("/policy", response_model=ProductPolicyResponse)
@inject
async def get_policy(
        request: ProductPolicyRequest = Depends(),
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    policy_in: TakePolicyIn = TakePolicyIn(
        productId=request.productId,
        userId=user_info.userId
    )

    policy_out: TakePolicyOut = product_service.take_product_policy(
        take_policy_in=policy_in
    )

    return ProductPolicyResponse(
        isSuccess=True,
        content=ProductPolicyResponse.Policy(
            productPolicy=policy_out.productPolicy,
            productType=policy_out.productType
        )
    )


@product_router.get("/info/duplicate", response_model=ProductDuplicateResponse)
@inject
async def get_info_duplicate(
        request: ProductDuplicateRequest = Depends(),
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    duplicate_in: TakeDuplicateInfoIn = TakeDuplicateInfoIn(
        productCode=request.productCode,
        userId=user_info.userId
    )

    duplicate_out: TakeDuplicateInfoOut = product_service.take_duplicate_product_info(
        take_duplicate_in=duplicate_in
    )

    return ProductDuplicateResponse(
        isSuccess=True,
        content=ProductDuplicateResponse.ProductInfo(
            productId=duplicate_out.productId,
            productCost=duplicate_out.productCost,
            productName=duplicate_out.productName,
            productQuantity=duplicate_out.productQuantity,
            productDescription=duplicate_out.productDescription,
            productInformation=duplicate_out.productInformation,
            productIsSale=duplicate_out.productIsSale,
            productCreateAt=duplicate_out.productCreatedAt,
            productSellerId=duplicate_out.productSellerId,
            productUpdatedAt=duplicate_out.productUpdatedAt
        )
    )


@product_router.post("/info/search", response_model=ProductSearchResponse)
@inject
async def post_info_search(
        request: ProductSearchRequest,
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    search_in: TakeSearchInfoIn = TakeSearchInfoIn(
        productIds=request.productIds,
        userId=user_info.userId
    )

    search_out: List[TakeSearchInfoOut] = product_service.take_search_product_info(
        take_search_in=search_in
    )

    return ProductSearchResponse(
        isSuccess=True,
        content=[
            ProductSearchResponse.ProductInfo(
                productInformation=info.productInformation,
                productDescription=info.productDescription,
                productId=info.productId,
                productName=info.productName,
                productQuantity=info.productQuantity,
                productCost=info.productCost,
                productCode=info.productCode,
                productIsSale=info.productIsSale,
                productSellerId=info.productSellerId
            ) for info in search_out
        ]
    )


@product_router.get("/status", response_model=ProductStatusResponse)
@inject
async def get_status(
        request: ProductStatusRequest = Depends(),
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    status_in: TakeStatusIn = TakeStatusIn(
        productId=request.productId,
        userId=user_info.userId
    )

    status_out: TakeStatusOut = product_service.take_status_of_product(
        take_status_in=status_in
    )

    return ProductStatusResponse(
        isSuccess=True,
        content=ProductStatusResponse.ProductStatus(
            productStatus=status_out.productStatus
        )
    )


@product_router.get("/info/paid", response_model=ProductPaidResponse)
@inject
async def get_info_paid(
        request: ProductPaidRequest = Depends(),
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    paid_in: TakePaidInfoIn = TakePaidInfoIn(
        orderCode=request.orderCode,
        productCode=request.productCode,
        userId=user_info.userId
    )

    paid_out: TakePaidInfoOut = product_service.take_paid_product_info(
        take_paid_info_in=paid_in
    )

    return ProductPaidResponse(
        isSuccess=True,
        content=ProductPaidResponse.ProductInfo(
            productCode=paid_out.productCode,
            productStatus=paid_out.productStatus,
            productCost=paid_out.productCost,
            productName=paid_out.productName,
            productQuantity=paid_out.productQuantity,
            productInformation=paid_out.productInformation,
            productDescription=paid_out.productDescription,
            productSellerId=paid_out.productSellerId
        )
    )


@product_router.get("/info/base", response_model=ProductBaseResponse)
@inject
async def get_info_base(
        request: ProductBaseRequest = Depends(),
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    base_in: TakeBaseInfoIn = TakeBaseInfoIn(
        productCount=request.productCount,
        userId=user_info.userId
    )

    base_out: List[TakeBaseInfoOut] = product_service.take_base_product_info(
        take_base_info_in=base_in
    )

    return ProductBaseResponse(
        isSuccess=True,
        content=[
            ProductBaseResponse.ProductInfo(
                productDescription=product.productDescription,
                productInformation=product.productInformation,
                productName=product.productName,
                productCost=product.productCost,
                productCode=product.productCode,
                productQuantity=product.productQuantity,
                productId=product.productId,
                productSellerId=product.productSellerId,
                productIsSale=product.productIsSale
            ) for product in base_out
        ]
    )


