from datetime import datetime
from ninja import Schema


class LicenseSchema(Schema):
    id: int
    title_ru: str
    title_kg: str
    address_ru: str
    address_kg: str
    category: str
    data: datetime
    is_active: bool
    created_date: datetime


class LicenseOUT(Schema):
    id: int
    title_ru: str
    title_kg: str
    address_ru: str
    address_kg: str
    category: str
    data: datetime

    class Config:
        orm_mode = True