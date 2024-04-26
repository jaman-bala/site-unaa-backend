from typing import List
from datetime import datetime
from ninja import Schema


class ImageSchema(Schema):
    id: int
    image: str


class NewsSchema(Schema):
    title_ru: str
    title_ky: str
    text_ru: str
    text_ky: str
    url_youtube_ru: str
    url_youtube_kg: str
    created_date: datetime
    published_date: datetime
    images: List[ImageSchema]
    is_published: bool
    viewed: int
    is_active: bool


class NewsOUT(Schema):
    id: int
    title_ru: str
    title_ky: str
    text_ru: str
    text_ky: str
    url_youtube_ru: str
    url_youtube_kg: str
    published_date: datetime
    images: List[ImageSchema]

    class Config:
        orm_mode = True