from typing import List
from ninja import Router
from ninja.errors import HttpError
from django.contrib.auth.models import User

from backend.apps.account.schemas import RegistrationInput, RegisterOUT

router = Router()


@router.post("/register")
def register(request, data: RegistrationInput):
    if User.objects.filter(username=data.username).exists():
        raise HttpError(400, "Пользователь с таким именем уже существует")

    user = User.objects.create_user(
        username=data.username,
        password=data.password,
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
    )

    return {"message": "Пользователь успешно зарегистрирован"}


@router.get("/register", response=List[RegisterOUT])
def get_register(request,):
    qs = User.objects.all()
    return qs
