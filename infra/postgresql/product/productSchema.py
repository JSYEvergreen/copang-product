from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    BIGINT,
    Integer,
    Boolean,
    ForeignKey
)


BaseUnit = declarative_base()


class SellerSchema(BaseUnit):
    __tablename__: str = "seller"
    id: str = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    user_id: str = Column(String(40), nullable=False)
    password: str = Column(String(100), nullable=False)
    ceo_name: str = Column(String(100), nullable=False)
    company_name: str = Column(String(100), nullable=False)
    created_at: DateTime = Column(DateTime, nullable=False)
    updated_at: DateTime = Column(DateTime, nullable=False)
    deleted_at: DateTime = Column(DateTime, nullable=True)


class BuyerSchema(BaseUnit):
    __tablename__: str = "buyer"
    id: str = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    user_id: str = Column(String(40), nullable=False)
    password: str = Column(String(100), nullable=False)
    nick_name: str = Column(String(100), nullable=False)
    email: str = Column(String(100), nullable=False)
    phone_number: str = Column(String(100), nullable=False)
    created_at: DateTime = Column(DateTime, nullable=False)
    updated_at: DateTime = Column(DateTime, nullable=False)
    deleted_at: DateTime = Column(DateTime, nullable=True)


class ReviewSchema(BaseUnit):
    __tablename__: str = "review"
    id: str = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    star: DOUBLE_PRECISION = Column(DOUBLE_PRECISION, nullable=False)
    content: str = Column(Text, nullable=False)
    product_id: int = Column(Integer, ForeignKey(column="product.id"), nullable=False)
    buyer_id: int = Column(Integer, ForeignKey(column="buyer.id"), nullable=False)
    parent_id: int = Column(Integer, nullable=False)
    created_at: DateTime = Column(DateTime, nullable=False)
    updated_at: DateTime = Column(DateTime, nullable=False)
    deleted_at: DateTime = Column(DateTime, nullable=True)


class ProductSchema(BaseUnit):
    __tablename__: str = "product"
    id: str = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name: str = Column(String(100), nullable=False)
    code: str = Column(String(100), nullable=False)
    description: str = Column(String(100), nullable=False)
    information: str = Column(String(100), nullable=False)
    quantity: int = Column(Integer, nullable=False)
    cost: int = Column(Integer, nullable=False)
    is_sale: bool = Column(Boolean, nullable=False)
    seller_id: int = Column(Integer, ForeignKey(column="seller.id"), nullable=False)
    created_at: DateTime = Column(DateTime, nullable=False)
    updated_at: DateTime = Column(DateTime, nullable=False)
    deleted_at: DateTime = Column(DateTime, nullable=True)


class ProductPolicySchema(BaseUnit):
    __tablename__: str = "product_policy"
    id: str = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    type: str = Column(String(100), nullable=False)
    policy: str = Column(String(100), nullable=False)
    product_id: int = Column(Integer, ForeignKey(column="product.id"), nullable=False)
    created_at: DateTime = Column(DateTime, nullable=False)
    updated_at: DateTime = Column(DateTime, nullable=False)
    deleted_at: DateTime = Column(DateTime, nullable=True)


class CartSchema(BaseUnit):
    __tablename__: str = "cart"
    id: str = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    product_quantity: int = Column(Integer, nullable=False)
    status: str = Column(String(100), nullable=False)
    buyer_id: int = Column(Integer, ForeignKey(column="buyer.id"), nullable=False)
    product_id: int = Column(Integer, ForeignKey(column="product.id"), nullable=False)
    created_at: DateTime = Column(DateTime, nullable=False)
    updated_at: DateTime = Column(DateTime, nullable=False)
    deleted_at: DateTime = Column(DateTime, nullable=True)


class OrderHistorySchema(BaseUnit):
    __tablename__: str = "order_history"
    id: str = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    order_code: str = Column(String(100), nullable=False)
    buyer_id: int = Column(Integer, ForeignKey(column="buyer.id"), nullable=False)
    created_at: DateTime = Column(DateTime, nullable=False)
    updated_at: DateTime = Column(DateTime, nullable=False)
    deleted_at: DateTime = Column(DateTime, nullable=True)


class OrderProductSchema(BaseUnit):
    __tablename__: str = "order_product"
    id: str = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    code: str = Column(String(100), nullable=False)
    cost: int = Column(Integer, nullable=False)
    name: str = Column(String(100), nullable=False)
    description: str = Column(String(100), nullable=False)
    information: str = Column(String(100), nullable=False)
    quantity: int = Column(Integer, nullable=False)
    status: str = Column(String(100), nullable=False)
    order_history_id: int = Column(Integer, ForeignKey(column="order_history.id"), nullable=False)
    created_at: DateTime = Column(DateTime, nullable=False)
    updated_at: DateTime = Column(DateTime, nullable=False)
    deleted_at: DateTime = Column(DateTime, nullable=True)


