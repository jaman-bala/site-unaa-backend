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
