from django.contrib.auth import authenticate, login
from ninja import Router
from ninja.errors import HttpError
from ninja.security import django_auth

from backend.apps.account.schemas import LoginInput

router = Router()


@router.post("/login")
def login_user(request, data: LoginInput):
    user = authenticate(request, username=data.username, password=data.password)
    if user is not None:
        login(request, user)
        return {"message": "Вход выполнен успешно"}
    else:
        raise HttpError(401, "Неверные учетные данные")