from django.contrib import admin

from backend.apps.job.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'note', 'created_date', 'is_active')