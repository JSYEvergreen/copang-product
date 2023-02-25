from pydantic import BaseModel


class DBConfig(BaseModel):
    name: str
    user: str
    password: str
    host: str
    port: int
    database: str
