import tomlkit

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from tool.postgresql.fullSchema import BaseUnit
from tool.postgresql.postgresql import DBConfig


class PostgresqlInitializer:
    def __init__(self):
        with open("core/Postgresql.toml", "r") as toml_file:
            self.config: DBConfig = DBConfig(**tomlkit.load(toml_file)["BaseSetting"])
        self.engine: Engine = create_engine(
            f"{self.config.name}://{self.config.user}:{self.config.password}@{self.config.host}:{self.config.port}/{self.config.database}"
        )
        self._initialize_db()
        self.engine.dispose()
        del self

    def _create_session(self):
        session = sessionmaker(bind=self.engine)
        return session()

    def _initialize_table(self):
        BaseUnit.metadata.create_all(self.engine)

    def _initialize_db(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            self._initialize_table()
            print("Successfully created database")
        else:
            print("Database already exists")
            pass

