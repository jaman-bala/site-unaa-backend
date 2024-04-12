from django.contrib import admin

from backend.apps.news.models import News, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 3


@admin.register(News)
class News(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('id', 'title_ru', 'created_date', 'is_active')
    list_display_links = ('id', 'title_ru')
    search_fields = ('title_ru',)
    list_editable = ('is_active',)
    list_filter = ('is_active', 'created_date')
    save_on_top = True
