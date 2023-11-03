from sqlalchemy import Column, Integer, String, Boolean

from src.api.db.base_class import Base


class FishDB(Base):
    __tablename__ = "fishnames"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    used = Column(Boolean, default=False)
