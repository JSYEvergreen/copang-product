from dataclasses import dataclass

from application.product.productException import ProductException


@dataclass
class ProductExceptions:
    product_exception: ProductException = ProductException


product_exceptions: ProductExceptions = ProductExceptions()
