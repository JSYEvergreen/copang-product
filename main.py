import uvicorn
from fastapi import FastAPI


app: FastAPI = FastAPI()


if __name__ == "__main__":
    uvicorn.run(
        app=app
    )

