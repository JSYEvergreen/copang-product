from fastapi import FastAPI
from dataclasses import dataclass
from typing import Optional


def route_injection(app: FastAPI, routers: dataclass, prefix: Optional[str] = None) -> FastAPI:
    for k, v in routers.__dict__.items():
        if prefix is None:
            app.include_router(v)
        else:
            app.include_router(v, prefix=prefix)
    return app
