from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router
from django.views.decorators.cache import cache_page

from backend.apps.index.schemas import IndexSchema, IndexOUT
from backend.apps.index.models import Index

router = Router()


@router.get("/video", response=List[IndexSchema])
@cache_page(60 * 30)
def get_all_index(request):
    cached_data = cache.get('all_index_data')
    if cached_data is None:
        qs = Index.objects.all()
        cached_data = [IndexOUT.from_orm(video).dict() for video in qs]
        cache.set('all_index_data', cached_data, timeout=60 * 30)
    return JsonResponse(cached_data, safe=False)


@router.get("/video/{index_pk}", response=IndexOUT)
@cache_page(60 * 30)
def get_index(request, index_pk: int):
    cache_key = f'index_{index_pk}'
    cached_data = cache.get(cache_key)
    if cached_data is None:
        video = get_object_or_404(Index, id=index_pk)
        cached_data = IndexOUT.from_orm(video).dict()
        cache.set(cache_key, cached_data, timeout=60 * 30)
    return JsonResponse(cached_data)
