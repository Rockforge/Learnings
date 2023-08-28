from typing import Union

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str

    class Config:
            orm_mode = True
