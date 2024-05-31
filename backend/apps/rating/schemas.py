from datetime import datetime
from ninja import Schema


class RegionCategoriesBase(Schema):
    title: str
    is_active: bool
    created_date: datetime
    update_date: datetime


class RegionCategoriesOUT(Schema):
    id: int
    title: str
    is_active: bool
    created_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True


class RatingSchoolBase(Schema):
    regions: int
    logo: str
    title_ru: str
    title_kg: str
    percent_true: str
    percent_false: str
    is_active: bool
    created_date: datetime
    update_date: datetime


class RatingSchoolOUT(Schema):
    id: int
    regions: RegionCategoriesOUT
    logo: str
    title_ru: str
    title_kg: str
    percent_true: str
    percent_false: str
    is_active: bool
    created_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True
