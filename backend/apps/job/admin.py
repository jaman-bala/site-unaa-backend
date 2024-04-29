from django.contrib import admin

from backend.apps.job.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'city', 'note_ru', 'created_date', 'is_active')
    search_fields = ('title_ru',)
