import uvicorn
import tomlkit
from typing import List
from argparse import Namespace
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from tool.app.app import AppConfig
from tool.postgresql.initializer import PostgresqlInitializer
from application.exceptions import product_exceptions
from infra.exceptions import infra_exceptions


class AppConstructor:
    def __init__(
            self,
            parser: Namespace,
            app: FastAPI
    ):
        if parser.initialize:
            PostgresqlInitializer()

        else:
            self.app: FastAPI = app

            self.infra_exceptions: List[Exception] = [
                exception for exception in infra_exceptions.__dict__.values()
            ]

            self.product_exceptions: List[Exception] = [
                exception for exception in product_exceptions.__dict__.values()
            ]

            for exception in self.infra_exceptions:
                self._inject_exception(exception=exception)

            for exception in self.product_exceptions:
                self._inject_exception(exception=exception)

            with open("core/AppConfig.toml") as config_file:
                config: AppConfig = AppConfig(
                    **tomlkit.load(config_file)
                )

            uvicorn.run(
                app=self.app,
                **config.dict()
            )

    def _inject_exception(self, exception: Exception):
        @self.app.exception_handler(exception)
        async def http_exception_convertor(request: Request, exc: HTTPException):
            return JSONResponse(
                status_code=exc.status_code,
                content=exc.detail
            )



