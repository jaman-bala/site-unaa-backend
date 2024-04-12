from ninja import Schema
from datetime import datetime


class JobIn(Schema):
    id: int
    title: str
    city: str
    note: str
    created_date: datetime
    is_active: bool


class JobOUT(Schema):
    id: int
    title: str
    city: str
    note: str

    class Config:
        orm_mode = True
