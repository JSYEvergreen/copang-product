from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from domain.product.service.productService import ProductServiceModel
from domain.token.service.token import TakeUserInfoOut
from container.product.productContainer import ProductContainer
from container.token.tokenContainer import TokenContainer
from api.product.product import (
    ProductPolicyRequest,
    ProductPolicyResponse,
    ProductDuplicateRequest,
    ProductDuplicateResponse,
    ProductSearchRequest,
    ProductSearchResponse,
    ProductStatusRequest,
    ProductStatusResponse,
    ProductPaidRequest,
    ProductPaidResponse,
    ProductBaseRequest,
    ProductBaseResponse
)


product_router: APIRouter = APIRouter()


@product_router.get("/policy", response_model=ProductPolicyResponse)
@inject
async def get_policy(
        request: ProductPolicyRequest,
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    pass


@product_router.get("/info/duplicate", response_model=ProductDuplicateResponse)
@inject
async def get_info_duplicate(
        request: ProductDuplicateRequest,
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    pass


@product_router.post("/info/search", response_model=ProductSearchResponse)
@inject
async def post_info_search(
        request: ProductSearchRequest,
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    pass


@product_router.get("/status", response_model=ProductStatusResponse)
@inject
async def get_status(
        request: ProductStatusRequest,
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    pass


@product_router.get("/info/paid", response_model=ProductPaidResponse)
@inject
async def get_info_paid(
        request: ProductPaidRequest,
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    pass


@product_router.get("/info/base", response_model=ProductBaseResponse)
@inject
async def get_info_base(
        request: ProductBaseRequest,
        user_info: TakeUserInfoOut = Depends(TokenContainer.token_service),
        product_service: ProductServiceModel = Depends(Provide[ProductContainer.product_service])
):
    pass


