from typing import List
from ninja import Router

from backend.apps.card.models import ServiceORM
from backend.apps.card.schemas import ServiceORMOut

router = Router()


@router.get("/card", response={200: List[ServiceORMOut]})
def get_all_service(request):
    qs = ServiceORM.objects.all()
    return [ServiceORMOut.from_orm(service).dict() for service in qs]
