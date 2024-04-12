from typing import List
from ninja import Router

from backend.apps.service.models import (
    CalculatorAllList,
)
from backend.apps.service.schemas import (
    CalculatorAllListSchema,
)

router = Router()


@router.get("/calculator", response={ 200: List[CalculatorAllListSchema]})
def get_calculator(request):
    qs = CalculatorAllList.objects.all()
    return qs



