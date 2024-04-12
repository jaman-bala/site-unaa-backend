from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router

from backend.apps.news.schemas import NewsOUT
from backend.apps.news.models import News

router = Router()


@router.get("/news", response=List[NewsOUT])
def get_all_news(request):
    qs = News.objects.all()
    return [NewsOUT.from_orm(news).dict() for news in qs]


@router.get("/news/{news_pk}", response=NewsOUT)
def get_news(request, news_pk: int):
    news = get_object_or_404(News, id=news_pk)
    return NewsOUT.from_orm(news).dict()


