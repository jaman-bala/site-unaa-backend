from django.apps import AppConfig


class IndexConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.index'
    verbose_name = "Главная страница"
