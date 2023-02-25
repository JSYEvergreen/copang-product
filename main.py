import uvicorn
import sys

from fastapi import FastAPI

from tool.postgresql.initializer import PostgresqlInitializer


app: FastAPI = FastAPI()


if __name__ == "__main__":
    if sys.argv[1] == "db_initialize":
        PostgresqlInitializer()
    else:
        uvicorn.run(
            app=app
        )


