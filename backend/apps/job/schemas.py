from ninja import Schema
from datetime import datetime


class JobIn(Schema):
    id: int
    title_ru: str
    title_kg: str
    city: str
    note_ru: str
    note_kg: str
    created_date: datetime
    is_active: bool


class JobOUT(Schema):
    id: int
    title_ru: str
    title_kg: str
    city: str
    note_ru: str
    note_kg: str

    class Config:
        orm_mode = True
