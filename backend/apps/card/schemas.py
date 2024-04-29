from ninja import Schema


class ServiceORM(Schema):
    id: int
    title_ru: str
    title_kg: str
    descriptions_ru: str
    descriptions_kg: str
    url_link: str
    image: str
    is_active: bool


class ServiceORMOut(Schema):
    title_ru: str
    title_kg: str
    descriptions_ru: str
    descriptions_kg: str
    url_link: str
    image: str

    class Config:
        orm_mode = True