from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router

from backend.apps.index.schemas import IndexSchema, IndexOUT
from backend.apps.index.models import Index

router = Router()


@router.get("/video", response=List[IndexSchema])
def get_all_sliders(request):
    qs = Index.objects.all()
    return qs


@router.get("/video/{index_pk}", response=IndexOUT)
def get_slider(request, slider_pk: int):
    video = get_object_or_404(Index, id=slider_pk)
    return video
