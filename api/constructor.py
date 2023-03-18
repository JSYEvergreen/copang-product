from dataclasses import dataclass
from fastapi import APIRouter

from api.product.productController import product_router


@dataclass
class RouteConstructor:
    product_router: APIRouter = product_router


BASE_ROUTER: dataclass = RouteConstructor()

