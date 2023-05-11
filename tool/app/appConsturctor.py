import uvicorn
import tomlkit
from argparse import Namespace
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from tool.app.app import AppConfig
from tool.postgresql.initializer import PostgresqlInitializer
from infra.token.tokenException import TokenException


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

            @self.app.exception_handler(TokenException)
            async def http_exception_convertor(request: Request, exc: HTTPException):
                return JSONResponse(
                    status_code=exc.status_code,
                    content=exc.detail
                )

            with open("core/AppConfig.toml") as config_file:
                config: AppConfig = AppConfig(
                    **tomlkit.load(config_file)
                )

            uvicorn.run(
                app=self.app,
                **config.dict()
            )



