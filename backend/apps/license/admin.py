from django.contrib import admin

from backend.apps.license.models import License, Documents, DocumentsNPA, DopDoc
from backend.apps.blank.documents import VisualDocuments, BusinessContact


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'created_date', 'is_active')


@admin.register(DocumentsNPA)
class DocumentsNPAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'is_active', 'created_date')


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'address_ru', 'created_date', 'is_active')
    list_display_links = ('title_ru', )
    search_fields = ('title_ru',)
    list_filter = ('is_active', 'created_date')
    list_per_page = 15
    save_on_top = True


@admin.register(DopDoc)
class DopDocAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'is_active', 'created_date', 'update_date')


@admin.register(VisualDocuments)
class PropsAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'is_active', 'created_date', 'update_date')


@admin.register(BusinessContact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'is_active', 'created_date', 'update_date')
