from django.contrib import admin, messages

from backend.apps.news.models import News, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 3


@admin.register(News)
class News(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('title_ru', 'is_published', 'created_date', 'is_active')
    list_display_links = ('title_ru', )
    search_fields = ('title_ru',)
    list_editable = ('is_published',)
    actions = ['set_published', 'set_draft']
    list_filter = ('is_active', 'created_date')
    list_per_page = 15
    save_on_top = True

    @admin.display(description="Краткое описание", ordering='content')
    def brief_info(self, news: News):
        return f"Описание {len(news.text_ru)} символов."

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=self.model.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=self.model.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)

