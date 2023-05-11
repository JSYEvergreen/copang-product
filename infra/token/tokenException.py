from fastapi.exceptions import HTTPException
from typing import Any


class TokenException(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: Any = None
    ):
        super().__init__(
            status_code=status_code,
            detail=detail
        )

