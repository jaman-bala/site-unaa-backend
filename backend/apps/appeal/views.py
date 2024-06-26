from ninja import Router
from typing import List

from backend.apps.appeal.models import Appeal, Department
from backend.apps.appeal.schemas import AppealInput, DepartmentOUT, AppealOUT


router = Router()


@router.get("/departments", response={200: List[DepartmentOUT]})
def get_departments(request):
    departments = Department.objects.all()
    return departments


@router.post("/create_appeal")
def create_appeal(request, data: AppealInput):
    nearest_department = Department.objects.get(id=data.nearest_department_id)
    appeal = Appeal.objects.create(
        nearest_department=nearest_department,
        full_name=data.full_name,
        phone_number=data.phone_number,
        email=data.email,
        car_number=data.car_number
    )
    return {"message": "Обращение успешно создано"}


@router.get("/get_appeal", response=List[AppealOUT]) # auth=django_auth
def get_appeal(request):
    get_appeal_all = Appeal.objects.all()
    return get_appeal_all
