from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


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
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class ProductPolicy(BaseModel):
    id: str
    type: str
    policy: str
    product_id: int
    created_at: datetime
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


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


class GetRandomProduct(BaseModel):
    count: int


class GetProductsByCodeIn(BaseModel):
    productCode: str
    userId: str

