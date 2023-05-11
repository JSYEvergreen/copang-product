import tomlkit
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Engine, Connection

from infra.postgresql.postgresql import DBConfig


class PostGreSQLCore:
    def __init__(self):
        with open("core/Postgresql.toml", "r") as toml_file:
            self.config: DBConfig = DBConfig(**tomlkit.load(toml_file))
        self.connection_string: str = f"{self.config.name}://{self.config.user}:{self.config.password}@{self.config.host}:{self.config.port}/{self.config.database}"
        self.engine: Engine = create_engine(self.connection_string, pool_recycle=500)

    def create_session(self):
        session = sessionmaker(bind=self.engine)
        return session()

    def create_connection(self) -> Connection:
        return self.engine.connect()

