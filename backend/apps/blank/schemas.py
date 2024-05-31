from datetime import datetime
from ninja import Schema


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


class VisualDocumentsSchemas(Schema):
    id: int
    title_ru: str
    title_kg: str
    text_ru: str
    text_ky: str

    is_active: bool
    created_date: datetime
    update_date: datetime


class VisualDocumentsSchemasOUT(Schema):
    id: int
    title_ru: str
    title_kg: str
    text_ru: str
    text_ky: str

    class Config:
        orm_mode = True


class BusinessContactSchemas(Schema):
    id: int
    title_ru: str
    title_kg: str
    text_ru: str
    text_ky: str

    is_active: bool
    created_date: datetime
    update_date: datetime


class BusinessContactSchemasOUT(Schema):
    id: int
    title_ru: str
    title_kg: str
    text_ru: str
    text_ky: str

    class Config:
        orm_mode = True

