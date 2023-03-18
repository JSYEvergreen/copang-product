from pydantic import BaseModel
from typing import Any, List


class BaseResponse(BaseModel):
    resultCode: int
    resultMsg: str
    resultBody: Any


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


class GetOneRequest(BaseModel):
    code: str


class GetOneResponse(BaseResponse):
    resultBody: Product


class GetPluralRequest(BaseModel):
    codes: List[str]


class GetPluralResponse(BaseResponse):
    resultBody: List[Product]

