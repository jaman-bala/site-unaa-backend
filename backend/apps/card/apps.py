from django.apps import AppConfig


class CardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.card'
    verbose_name = "Карточки услуг"
