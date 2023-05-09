from pydantic import BaseModel
from datetime import datetime
from typing import List


class Product(BaseModel):
    id: str
    name: str
    code: str
    description: str
    information: str
    quantity: int
    cost: int
    is_sale: bool
    seller_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime


class ProductPolicy(BaseModel):
    id: str
    type: str
    policy: str
    product_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime


class GetOneProductByIdIn(BaseModel):
    productId: str
    userId: str


class GetPluralProductByIdIn(BaseModel):
    productIds: List[str]
    userId: str


class GetOneProductByCodeIn(BaseModel):
    productCode: str
    userId: str


class GetPluralProductByCodeIn(BaseModel):
    productCodes: List[str]
    userId: str


class GetProductPolicyIn(BaseModel):
    productId: str
    userId: str


class GetProductStatusIn(BaseModel):
    productId: str
    userId: str


class GetProductStatusOut(BaseModel):
    status: bool
