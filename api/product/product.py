from pydantic import BaseModel
from typing import Optional, List


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
    productCode: int


class ProductDuplicateResponse(BaseResponse):

    class ProductInfo(BaseModel):
        productId: int
        productName: str
        productDescription: str
        productInformation: str
        productQuantity: int
        productCost: int
        productIsSale: bool
        productSellerId: int
        productCreateAt: str
        ProductDeletedAt: Optional[str]
        productUpdatedAt: str

    content: ProductInfo


class ProductSearchRequest(BaseModel):
    productIds: List[int]


class ProductSearchResponse(BaseResponse):

    class ProductInfo(BaseModel):
        productId: int
        productCode: str
        productName: str
        productDescription: str
        productInformation: str
        productQuantity: int
        productCost: int
        productIsSale: bool
        productSellerId: int

    content: ProductInfo


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

    class ProductInfo(BaseModel):
        productCode: str
        productName: str
        productDescription: str
        productInformation: str
        productQuantity: int
        productCost: int
        productSellerId: int
        productStatus: str

    content: ProductInfo


class ProductBaseRequest(BaseModel):
    productCount: int


class ProductBaseResponse(BaseResponse):

    class ProductInfo(BaseModel):
        productId: int
        productCode: str
        productName: str
        productDescription: str
        productInformation: str
        productQuantity: int
        productCost: int
        productIsSale: bool
        productSellerId: int

    content: List[ProductInfo]
