from fastapi import APIRouter

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
async def get_policy(
        request: ProductPolicyRequest
):
    pass


@product_router.get("/info/duplicate", response_model=ProductDuplicateResponse)
async def get_info_duplicate(
        request: ProductDuplicateRequest
):
    pass


@product_router.post("/info/search", response_model=ProductSearchResponse)
async def post_info_search(
        request: ProductSearchRequest
):
    pass


@product_router.get("/status", response_model=ProductStatusResponse)
async def get_status(
        request: ProductStatusRequest
):
    pass


@product_router.get("/info/paid", response_model=ProductPaidResponse)
async def get_info_paid(
        request: ProductPaidRequest
):
    pass


@product_router.get("/info/base", response_model=ProductBaseResponse)
async def get_info_base(
        request: ProductBaseRequest
):
    pass


