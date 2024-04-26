from datetime import datetime
from ninja import Schema


class HistorySchem(Schema):
    id: int
    title: str
    created_date: datetime
    is_active: bool


class HistorySchemOUT(Schema):
    title: str

    class Config:
        orm_mode = True


class Management(Schema):
    id: int
    title: str
    name: str
    description_ru: str
    description_kg: str
    avatar: str
    is_active: bool
    created_date: datetime


class ManagementOUT(Schema):
    title: str
    name: str
    description_ru: str
    description_kg: str
    avatar: str

    class Config:
        orm_mode = True


class Contact(Schema):
    id: int
    title: str
    address: str
    phone: str
    time_job: str
    is_active: bool
    created_date: datetime


class ContactOUT(Schema):
    title: str
    address: str
    phone: str
    time_job: str

    class Config:
        orm_mode = True
