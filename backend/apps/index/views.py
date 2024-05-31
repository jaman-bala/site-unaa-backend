from typing import List
from ninja import Router

from backend.apps.index.schemas import IndexSchema
from backend.apps.index.models import Index

router = Router()


@router.get("/video", response=List[IndexSchema])
def get_all_sliders(request):
    qs = Index.objects.all()
    return qs

