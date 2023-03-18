from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide


from domain.product.productService import ProductInterface
from api.product.product import (
    GetOneRequest,
    GetOneResponse,
    GetPluralRequest,
    GetPluralResponse
)
from container.product.productContainer import ProductContainer


product_router: APIRouter = APIRouter()


@product_router.post("/product/get-one", response_model=GetOneResponse)
@inject
def get_one_product(
    request: GetOneRequest,
    product_service: ProductInterface = Depends(Provide[ProductContainer.product_service])
):  
    return GetOneResponse()



