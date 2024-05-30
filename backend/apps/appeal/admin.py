from django.contrib import admin

from backend.apps.appeal.models import Department, Appeal


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active', 'id')


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'nearest_department',
        'phone_number',
        'email',
        'car_number',
        'created_date',
        'is_active',
        'id'
    )
