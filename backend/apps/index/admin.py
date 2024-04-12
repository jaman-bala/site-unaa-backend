from django.contrib import admin
from backend.apps.index.models import Index


@admin.register(Index)
class Slider(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active', 'id')


admin.site.site_title = 'Админ-панель сайта УНАА'
admin.site.site_header = 'Админ-панель сайта УНАА'
admin.site.index_title = 'СПИСОК ДАННЫХ'