from django.apps import AppConfig


class BlankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.blank'
    verbose_name = "Бланки для лицензии"
