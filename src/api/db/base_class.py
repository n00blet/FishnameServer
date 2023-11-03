from typing import Any

from sqlalchemy import Engine, Inspector, text
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative


@as_declarative()
class Base:
    id: Any
    __name__: str

    # to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # check if table exists and not empty
    @classmethod
    def table_exists(cls, engine: Engine) -> bool:
        inspector = Inspector.from_engine(engine)
        table_name = cls.__tablename__
        if table_name in inspector.get_table_names():
            with engine.connect() as connection:
                query = f"SELECT 1 FROM {table_name} LIMIT 1"
                result = connection.execute(text(query))
                return result.fetchone() is not None
        return False




