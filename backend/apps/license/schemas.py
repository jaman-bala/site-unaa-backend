from datetime import datetime
from ninja import Schema


class DocumentsSchemas(Schema):
    id: int
    title_ru: str
    title_kg: str
    text_ru: str
    text_ky: str

    is_active: bool
    created_date: datetime


class DocumentsOUT(Schema):
    id: int
    title_ru: str
    title_kg: str
    text_ru: str
    text_ky: str

    class Config:
        orm_mode = True


class DocumentsNPASchemas(Schema):
    id: int
    title_ru: str
    title_kg: str
    text_ru: str
    text_ky: str

    is_active: bool
    created_date: datetime


class DocumentsNPAOUT(Schema):
    id: int
    title_ru: str
    title_kg: str
    text_ru: str
    text_ky: str

    class Config:
        orm_mode = True


class DopDocSchemas(Schema):
    id: int
    title_ru: str
    title_kg: str
    text_ru: str
    text_ky: str

    is_active: bool
    created_date: datetime
    update_date: datetime


class DopDocSchemasOUT(Schema):
    id: int
    title_ru: str
    title_kg: str
    text_ru: str
    text_ky: str

    class Config:
        orm_mode = True


class LicenseSchema(Schema):
    id: int
    logo: str
    title_ru: str
    title_kg: str
    register_number: str
    address_ru: str
    address_kg: str
    category: str
    issued_authority_ru: str
    issued_authority_kg: str
    data: datetime

    is_active: bool
    created_date: datetime
    update_date: datetime


class LicenseOUT(Schema):
    id: int
    logo: str
    title_ru: str
    title_kg: str
    register_number: str
    address_ru: str
    address_kg: str
    category: str
    issued_authority_ru: str
    issued_authority_kg: str
    data: datetime

    class Config:
        orm_mode = True


class PDFBase(Schema):
    title: str

    banner: str
    file: str

    created_date: datetime
    update_date: datetime
    is_active: bool


class PDFOut(Schema):
    id: int
    title: str

    banner: str
    file: str

    class Config:
        orm_mode = True


class RegionCategoriesBase(Schema):
    title: str

    is_active: bool
    created_date: datetime
    update_date: datetime


class RegionCategoriesOUT(Schema):
    id: int
    title: str

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
    regions: int
    logo: str
    title_ru: str
    title_kg: str
    percent_true: str
    percent_false: str

    class Config:
        orm_mode = True