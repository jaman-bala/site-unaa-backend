from django.contrib import admin

from backend.apps.appeal.models import City, Department, Appeal


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active', 'id')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active', 'id')


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'created_date',
        'nearest_department',
        'full_name',
        'phone_number',
        'email',
        'car_number',
        'is_active',
        'id'
    )