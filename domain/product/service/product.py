from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


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
    deleted_at: Optional[datetime]


class FindProductIn(BaseModel):
    code: str


class FindProductOut(Product):
    super().__init__()


class FindProductsIn(BaseModel):
    codes: List[str]


class FindProductsOut(BaseModel):
    products: List[Product]


class FindBaseProductsOut(BaseModel):
    products: List[Product]


class GetProductIn(BaseModel):
    code: str


class GetProductOut(Product):
    super().__init__()


class GetProductsIn(BaseModel):
    codes: List[str]


class GetProductsOut(BaseModel):
    products: List[Product]


class GetProductsDateOut(BaseModel):
    products: List[Product]
