from django.contrib import admin

from backend.apps.license.models import License, Documents, DocumentsNPA, DopDoc, RatingSchool, RegionCategories


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


@admin.register(RatingSchool)
class RatingSchoolAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'regions', 'is_active', 'created_date', 'update_date', 'id')
    list_display_links = ('title_ru',)
    search_fields = ('title_ru',)
    list_filter = ('is_active', 'created_date')
    list_per_page = 15
    save_on_top = True


@admin.register(RegionCategories)
class RegionCategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_date', 'update_date')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('is_active', 'created_date')
    list_per_page = 15
    save_on_top = True
