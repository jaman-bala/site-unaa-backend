from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from typing import List
from django.views.decorators.cache import cache_page
from ninja import Router

from backend.apps.news.schemas import NewsOUT
from backend.apps.news.models import News

router = Router()


@router.get("/news", response=List[NewsOUT])
def get_all_news(request):
    qs = News.objects.all()
    return [NewsOUT.from_orm(news).dict() for news in qs]


@router.get("/news/{news_pk}", response=NewsOUT)
@cache_page(60 * 60 * 20)
def get_news(request, news_pk: int):
    cache_key = f'news_{news_pk}'
    cached_news = cache.get(cache_key)
    if cached_news is None:
        news = get_object_or_404(News, id=news_pk)
        cached_news = NewsOUT.from_orm(news).dict()
        cache.set(cache_key, cached_news, timeout=60 * 60 * 20)
    return JsonResponse(cached_news)


