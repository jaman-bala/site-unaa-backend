import pytest
from ninja.testing import TestClient
from freezegun import freeze_time

from backend.apps.about.views import router
from backend.apps.about.models import History, Management, Contact


@pytest.fixture
def client():
    return TestClient(router)


@freeze_time("2024-04-09 12:00:00")
@pytest.mark.django_db
def test_get_all_history(client):
    # Создаем тестовые данные
    History.objects.create(title="Test History 1")
    # Вызываем эндпоинт
    response = client.get("/history")
    # Проверяем успешность запроса
    assert response.status_code == 200
    # Проверяем соответствие данных
    assert response.json() == [
        {"title": "Test History 1"},
    ]


@freeze_time("2024-04-09 12:00:00")
@pytest.mark.django_db
def test_get_all_management(client):
    # Create test data
    Management.objects.create(
        title="Test Title Management",

    )
    response = client.get("/management")

    assert response.status_code == 200

    assert response.json() == [
        {
            "title": "Test Title Management",

        }
    ]


@freeze_time("2024-04-09 12:00:00")
@pytest.mark.django_db
def test_get_all_contact(client):
    Contact.objects.create(
        title="Test Contact",
        address="Test Address",
        phone="123456789",
        time_job="9am-5pm",
    )

    response = client.get("/contact")

    assert response.status_code == 200

    assert response.json() == [
        {
         "title": "Test Contact",
         "address": "Test Address",
         "phone": "123456789",
         "time_job": "9am-5pm",
        }
    ]


@freeze_time("2024-04-09 12:00:00")
@pytest.mark.django_db
def test_get_contact_pk(client):
    contact = Contact.objects.create(
        title="Test Contact",
        address="Test Address",
        phone="123456789",
        time_job="9am-5pm",
    )

    response = client.get(f"/contact/{contact.id}")

    assert response.status_code == 200
    assert response.json() == {
        "title": "Test Contact",
        "address": "Test Address",
        "phone": "123456789",
        "time_job": "9am-5pm",
    }
