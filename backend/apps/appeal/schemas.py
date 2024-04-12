from ninja import Schema
from datetime import datetime


class CityOUT(Schema):
    id: int
    title: str


class DepartmentOUT(Schema):
    id: int
    title: str


class AppealInput(Schema):
    category_id: int
    nearest_department_id: int
    full_name: str
    phone_number: str
    email: str
    car_number: str
    created_date: datetime
    is_active: bool

    class Config:
        orm_mode = True


class AppealOUT(Schema):
    id: int
    category_id: int
    nearest_department_id: int
    full_name: str
    phone_number: str
    email: str
    car_number: str

    class Config:
        orm_mode = True
