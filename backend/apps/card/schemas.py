from ninja import Schema


class ServiceORM(Schema):
    id: int
    title: str
    descriptions: str
    url_link: str
    image: str
    is_active: bool


class ServiceORMOut(Schema):
    title: str
    descriptions: str
    url_link: str
    image: str

    class Config:
        orm_mode = True