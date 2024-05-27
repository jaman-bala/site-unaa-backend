from django.contrib import admin

from backend.apps.blank.models import PDF


@admin.register(PDF)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_date', 'update_date')
