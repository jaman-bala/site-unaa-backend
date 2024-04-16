from typing import List
from django.http import JsonResponse
from ninja import Router
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from backend.apps.information.models import Register_Car01, Register_Car02, Issue_Car01, Issue_Car02, Confirmation
from backend.apps.information.schemas import RegisterCar01, RegisterCar02, IssueCar01, IssueCar02, ConfirmationOut

router = Router()


@router.get("/info01", response=List[RegisterCar01])
@cache_page(60 * 15)  # кэшировать страницу на 15 минут
def get_register01(request):
    cached_data = cache.get('register01_data')
    if cached_data is None:
        qs = Register_Car01.objects.all()
        cached_data = [RegisterCar01.from_orm(info01).dict() for info01 in qs]
        cache.set('register01_data', cached_data, timeout=60 * 15)  # кэшировать на 15 минут
    return JsonResponse(cached_data, safe=False)


@router.get("/info02", response=List[RegisterCar02])
@cache_page(60 * 15)  # кэшировать страницу на 15 минут
def get_register02(request):
    cached_data = cache.get('register02_data')
    if cached_data is None:
        qs = Register_Car02.objects.all()
        cached_data = [RegisterCar02.from_orm(info02).dict() for info02 in qs]
        cache.set('register02_data', cached_data, timeout=60 * 15)  # кэшировать на 15 минут
    return JsonResponse(cached_data, safe=False)


@router.get("/issu01", response=List[IssueCar01])
@cache_page(60 * 15)  # кэшировать страницу на 15 минут
def get_issu01(request):
    cached_data = cache.get('issue01_data')
    if cached_data is None:
        qs = Issue_Car01.objects.all()
        cached_data = [IssueCar01.from_orm(issue01).dict() for issue01 in qs]
        cache.set('issue01_data', cached_data, timeout=60 * 15)  # кэшировать на 15 минут
    return JsonResponse(cached_data, safe=False)


@router.get("/issu02", response=List[IssueCar02])
@cache_page(60 * 15)  # кэшировать страницу на 15 минут
def get_issu02(request):
    cached_data = cache.get('issue02_data')
    if cached_data is None:
        qs = Issue_Car02.objects.all()
        cached_data = [IssueCar02.from_orm(issue02).dict() for issue02 in qs]
        cache.set('issue02_data', cached_data, timeout=60 * 15)  # кэшировать на 15 минут
    return JsonResponse(cached_data, safe=False)


@router.get("/conf", response=List[ConfirmationOut])
@cache_page(60 * 15)  # кэшировать страницу на 15 минут
def get_conf(request):
    cached_data = cache.get('confirmation_data')
    if cached_data is None:
        qs = Confirmation.objects.all()
        cached_data = [ConfirmationOut.from_orm(conf).dict() for conf in qs]
        cache.set('confirmation_data', cached_data, timeout=60 * 15)  # кэшировать на 15 минут
    return JsonResponse(cached_data, safe=False)


@router.get("/issu02", response=List[IssueCar02])
def get_issu02(request):
    qs = Issue_Car02.objects.all()
    return qs


@router.get("/conf", response=List[ConfirmationOut])
def get_conf(request):
    qs = Confirmation.objects.all()
    return qs
