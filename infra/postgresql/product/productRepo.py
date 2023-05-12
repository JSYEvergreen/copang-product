from overrides import override
from typing import List
from sqlalchemy.orm import sessionmaker

from domain.product.repo.productRepo import ProductRepoModel
from domain.product.repo.product import (
    Product, ProductPolicy,
    GetOneProductByIdIn,
    GetOneProductByCodeIn,
    GetProductPolicyIn,
    GetProductStatusIn, GetProductStatusOut,
    GetPluralProductByIdIn,
    GetPluralProductByCodeIn,
    GetRandomProduct
)
from infra.postgresql.core import PostGreSQLCore
from infra.postgresql.product.productSchema import (
    ProductSchema,
    ProductPolicySchema
)


class ProductRepoModule(ProductRepoModel, PostGreSQLCore):
    def __init__(self):
        super().__init__()
        PostGreSQLCore.__init__(self)

    @override
    def get_one_product_by_id(self, get_product_in: GetOneProductByIdIn) -> Product:
        session: sessionmaker = self.create_session()

        try:
            product_info: ProductSchema = session.query(
                ProductSchema
            ).filter(
                ProductSchema.id == get_product_in.productId
            ).one()

            return Product(
                id=product_info.id,
                name=product_info.name,
                code=product_info.code,
                description=product_info.description,
                information=product_info.information,
                quantity=product_info.quantity,
                cost=product_info.cost,
                is_sale=product_info.is_sale,
                seller_id=product_info.seller_id,
                created_at=product_info.created_at,
                updated_at=product_info.updated_at,
                deleted_at=product_info.deleted_at,
            )

        # Todo: Exception Block Add
        except Exception:
            session.close()

        finally:
            session.close()

    @override
    def get_plural_product_by_id(self, get_product_in: GetPluralProductByIdIn) -> List[Product]:
        session: sessionmaker = self.create_session()

        try:
            product_info: List[ProductSchema] = session.query(
                ProductSchema
            ).filter(
                ProductSchema.id.in_(get_product_in.productIds)
            ).all()

            return [
                Product(
                    id=info.id,
                    name=info.name,
                    code=info.code,
                    description=info.description,
                    information=info.information,
                    quantity=info.quantity,
                    cost=info.cost,
                    is_sale=info.is_sale,
                    seller_id=info.seller_id,
                    created_at=info.created_at,
                    updated_at=info.updated_at,
                    deleted_at=info.deleted_at,
                ) for info in product_info
            ]

        # Todo: Exception Block Add
        except Exception:
            session.close()

        finally:
            session.close()

    @override
    def get_one_product_by_code(self, get_product_in: GetOneProductByCodeIn) -> Product:
        session: sessionmaker = self.create_session()

        try:
            product_info: ProductSchema = session.query(
                ProductSchema
            ).filter(
                ProductSchema.code == get_product_in.productCode
            ).one()

            return Product(
                id=product_info.id,
                name=product_info.name,
                code=product_info.code,
                description=product_info.description,
                information=product_info.information,
                quantity=product_info.quantity,
                cost=product_info.cost,
                is_sale=product_info.is_sale,
                seller_id=product_info.seller_id,
                created_at=product_info.created_at,
                updated_at=product_info.updated_at,
                deleted_at=product_info.deleted_at,
            )

        # Todo: Exception Block Add
        except Exception:
            session.close()

        finally:
            session.close()

    @override
    def get_plural_product_by_code(self, get_product_in: GetPluralProductByCodeIn) -> List[Product]:
        session: sessionmaker = self.create_session()

        try:
            product_info: List[ProductSchema] = session.query(
                ProductSchema
            ).filter(
                ProductSchema.id.in_(get_product_in.productCodes)
            ).all()

            return [
                Product(
                    id=info.id,
                    name=info.name,
                    code=info.code,
                    description=info.description,
                    information=info.information,
                    quantity=info.quantity,
                    cost=info.cost,
                    is_sale=info.is_sale,
                    seller_id=info.seller_id,
                    created_at=info.created_at,
                    updated_at=info.updated_at,
                    deleted_at=info.deleted_at,
                ) for info in product_info
            ]

        # Todo: Exception Block Add
        except Exception:
            session.close()

        finally:
            session.close()

    @override
    def get_product_policy(self, get_policy_in: GetProductPolicyIn) -> ProductPolicy:
        session: sessionmaker = self.create_session()

        try:
            policy_info: ProductPolicySchema = session.query(
                ProductPolicySchema
            ).filter(
                ProductPolicySchema.id == get_policy_in.productId
            ).one()

            return ProductPolicy(
                id=policy_info.id,
                type=policy_info.type,
                policy=policy_info.policy,
                product_id=policy_info.product_id,
                created_at=policy_info.created_at
            )

        # Todo: Exception Block Add
        except Exception:
            session.close()

        finally:
            session.close()

    @override
    def get_product_status(self, get_status_in: GetProductStatusIn) -> GetProductStatusOut:
        session: sessionmaker = self.create_session()

        try:
            policy_info: ProductSchema = session.query(
                ProductSchema
            ).filter(
                ProductSchema.id == get_status_in.productId
            ).one()

            return GetProductStatusOut(
                status=policy_info.is_sale
            )

        # Todo: Exception Block Add
        except Exception:
            session.close()

        finally:
            session.close()

    @override
    def get_random_product(self, get_random_product: GetRandomProduct) -> List[Product]:
        session: sessionmaker = self.create_session()

        try:
            product_info: List[ProductSchema] = session.query(
                ProductSchema
            ).all()

            return [
                Product(
                    id=info.id,
                    name=info.name,
                    code=info.code,
                    description=info.description,
                    information=info.information,
                    quantity=info.quantity,
                    cost=info.cost,
                    is_sale=info.is_sale,
                    seller_id=info.seller_id,
                    created_at=info.created_at,
                    updated_at=info.updated_at,
                    deleted_at=info.deleted_at,
                ) for info in product_info
            ][:get_random_product.count]

        # Todo: Exception Block Add
        except IndexError:
            return [
                Product(
                    id=info.id,
                    name=info.name,
                    code=info.code,
                    description=info.description,
                    information=info.information,
                    quantity=info.quantity,
                    cost=info.cost,
                    is_sale=info.is_sale,
                    seller_id=info.seller_id,
                    created_at=info.created_at,
                    updated_at=info.updated_at,
                    deleted_at=info.deleted_at,
                ) for info in product_info
            ]

        finally:
            session.close()


