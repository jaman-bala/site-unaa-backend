from django.contrib import admin
from backend.apps.index.models import Index


@admin.register(Index)
class Slider(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active', 'id')


admin.site.site_title = 'ГАРТСВС при КМ КР'
admin.site.site_header = 'Админ-панель ГАРТСВС при КМ КР'
admin.site.index_title = 'СПИСОК ДАННЫХ'