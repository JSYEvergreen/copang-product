from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class ProductBaseInfo(BaseModel):
    productName: str
    productDescription: str
    productInformation: str
    productQuantity: int
    productCost: int
    productSellerId: int


class TakeBaseInfoIn(BaseModel):
    productCount: int
    userId: str


class TakeBaseInfoOut(ProductBaseInfo):
    productId: int
    productCode: str
    productIsSale: bool


class TakePaidInfoIn(BaseModel):
    orderCode: int
    productCode: str
    userId: str


class TakePaidInfoOut(ProductBaseInfo):
    productCode: str
    productStatus: str


class TakeStatusIn(BaseModel):
    productId: int
    userId: str


class TakeStatusOut(BaseModel):
    productStatus: bool


class TakeSearchInfoIn(BaseModel):
    productIds: List[int]
    userId: str


class TakeSearchInfoOut(ProductBaseInfo):
    productId: int
    productCode: str
    productIsSale: bool


class TakeDuplicateInfoIn(BaseModel):
    productCode: str
    userId: str


class TakeDuplicateInfoOut(ProductBaseInfo):
    productId: int
    productIsSale: bool
    productCreatedAt: datetime
    productDeletedAt: Optional[datetime]
    productUpdatedAt: datetime


class TakePolicyIn(BaseModel):
    productId: int
    userId: str


class TakePolicyOut(BaseModel):
    productType: str
    productPolicy: int

