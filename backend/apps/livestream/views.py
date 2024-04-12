from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404

from backend.apps.livestream.models import IPCamera
from backend.apps.livestream.schemas import StreamSchema


router = Router()


@router.get("/live-streams", response=List[StreamSchema])
def get_streams_all(request):
    qs = IPCamera.objects.all()
    return qs


@router.get("/live-streams/{stream_id}", response=StreamSchema)
def get_stream_id(request, stream_id: int):
    qs = get_object_or_404(IPCamera, id=stream_id)
    return StreamSchema.from_orm(qs).dict()
