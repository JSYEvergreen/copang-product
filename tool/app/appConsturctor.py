import uvicorn
import tomlkit
from argparse import Namespace
from fastapi import FastAPI

from tool.app.app import AppConfig
from tool.postgresql.initializer import PostgresqlInitializer


class AppConstructor:
    def __init__(self, parser: Namespace):
        if parser.initialize:
            PostgresqlInitializer()

        else:
            self.app: FastAPI = FastAPI()

            with open("core/AppConfig.toml") as config_file:
                config: AppConfig = AppConfig(
                    **tomlkit.load(config_file)
                )

            uvicorn.run(
                app=self.app,
                **config.dict()
            )



