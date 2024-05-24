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


class PdfBase(Schema):
    title: str
    banner: str
    pdf: str
    created_date: datetime
    is_active: bool


class PdfOUT(Schema):
    id: int
    title: str
    banner: str
    pdf: str

    class Config:
        orm_mode = True
