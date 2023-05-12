from fastapi import FastAPI

from api.constructor import BASE_ROUTER
from container.constructor import ContainerConstructor
from tool.app.appConsturctor import AppConstructor
from tool.app.argParser import ArgParser
from tool.app.routeInjector import route_injection


if __name__ == "__main__":
    ContainerConstructor()
    AppConstructor(
        app=route_injection(
            app=FastAPI(),
            routers=BASE_ROUTER
        ),
        parser=ArgParser().name
    )

