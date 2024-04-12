from django.contrib import admin
from django.utils.safestring import mark_safe

from backend.apps.about.models import History, Management, Contact


@admin.register(History)
class History(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Management)
class Management(admin.ModelAdmin):
    list_display = ('name', 'title', 'get_html_photo', 'created_date', 'is_active', 'id', )
    list_editable = ('is_active',)
    fields = ('name', 'title', 'avatar', 'get_html_photo', 'created_date', 'is_active',)
    readonly_fields = ('created_date', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=80>")

    get_html_photo.short_description = "Аватар"


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'is_active')
