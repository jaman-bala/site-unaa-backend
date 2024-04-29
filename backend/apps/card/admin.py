from django.contrib import admin
from django.utils.safestring import mark_safe

from backend.apps.card.models import ServiceORM


@admin.register(ServiceORM)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'descriptions_ru', 'get_html_photo', 'id',)
    search_fields = ('title_ru',)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=80>")

    get_html_photo.short_description = "Картинка"
