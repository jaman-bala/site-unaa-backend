from typing import List
from ninja import Router

from backend.apps.information.models import Register_Car01, Register_Car02, Issue_Car01, Issue_Car02, Confirmation
from backend.apps.information.schemas import RegisterCar01, RegisterCar02, IssueCar01, IssueCar02, ConfirmationOut, FaqOUT
from backend.apps.information.faq import FaqModels

router = Router()


@router.get("/info01", response=List[RegisterCar01])
def get_register01(request):
    qs = Register_Car01.objects.all()
    return [RegisterCar01.from_orm(info01).dict() for info01 in qs]


@router.get("/info02", response=List[RegisterCar02])
def get_register02(request):
    qs = Register_Car02.objects.all()
    return qs


@router.get("/issu01", response=List[IssueCar01])
def get_issu01(request):
    qs = Issue_Car01.objects.all()
    return qs


@router.get("/issu02", response=List[IssueCar02])
def get_issu02(request):
    qs = Issue_Car02.objects.all()
    return qs


@router.get("/conf", response=List[ConfirmationOut])
def get_conf(request):
    qs = Confirmation.objects.all()
    return qs


@router.get("/faq", response=List[FaqOUT])
def get_faq(request):
    qs = FaqModels.objects.all()
    return qs
