from fastapi.exceptions import HTTPException
from pydantic import BaseModel


class ProductErrorTemplate(BaseModel):
    message: str


class ProductException(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: ProductErrorTemplate
    ):
        super().__init__(
            status_code=status_code,
            detail=dict(
                isSuccess=False,
                errorCode=500,
                message=detail.message
            )
        )

