from django.contrib import admin

from backend.apps.card.models import ServiceORM


@admin.register(ServiceORM)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions', 'id',)
    search_fields = ('title',)
