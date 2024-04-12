from datetime import datetime
from ninja import Schema


class IndexSchema(Schema):
    id: int
    title: str
    file: str
    created_date: datetime
    is_active: bool


class IndexOUT(Schema):
    id: int
    title: str
    image: str

    class Config:
        orm_mode = True
