from django.contrib import admin

from backend.apps.rating.models import RatingSchool, RegionCategories


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

