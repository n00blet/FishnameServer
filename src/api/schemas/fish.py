from pydantic import BaseModel, BaseConfig


class FishName(BaseModel):
    name: str

    class Config(BaseConfig):
        orm_mode = True
