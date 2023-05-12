from pydantic import BaseModel
from typing import Optional, List


class ProductBaseInfo(BaseModel):
    productName: str
    productDescription: str
    productInformation: str
    productQuantity: int
    productCost: int
    productSellerId: int


class BaseResponse(BaseModel):
    isSuccess: bool
    content: BaseModel


class ProductPolicyRequest(BaseModel):
    productId: int


class ProductPolicyResponse(BaseResponse):

    class Policy(BaseModel):
        productType: str
        productPolicy: int

    content: Policy


class ProductDuplicateRequest(BaseModel):
    productCode: str


class ProductDuplicateResponse(BaseResponse):

    class ProductInfo(ProductBaseInfo):
        productId: int
        productIsSale: bool
        productCreateAt: str
        ProductDeletedAt: Optional[str]
        productUpdatedAt: str

    content: ProductInfo


class ProductSearchRequest(BaseModel):
    productIds: List[int]


class ProductSearchResponse(BaseResponse):

    class ProductInfo(ProductBaseInfo):
        productId: int
        productCode: str
        productIsSale: bool

    content: List[ProductInfo]


class ProductStatusRequest(BaseModel):
    productId: int


class ProductStatusResponse(BaseResponse):

    class ProductStatus(BaseModel):
        productStatus: bool

    content: ProductStatus


class ProductPaidRequest(BaseModel):
    orderCode: int
    productCode: str


class ProductPaidResponse(BaseResponse):

    class ProductInfo(ProductBaseInfo):
        productCode: str
        productStatus: str

    content: ProductInfo


class ProductBaseRequest(BaseModel):
    productCount: int


class ProductBaseResponse(BaseResponse):

    class ProductInfo(ProductBaseInfo):
        productId: int
        productCode: str
        productIsSale: bool

    content: List[ProductInfo]
