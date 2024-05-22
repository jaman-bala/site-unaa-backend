from django.contrib import admin

from backend.apps.information.models import Register_Car01, Register_Car02, Issue_Car01, Issue_Car02, Confirmation
from backend.apps.information.faq import FaqModelsTS, FaqModelsVS
from backend.apps.information.pdf import PdfGet


@admin.register(Register_Car01)
class Register_Car01Admin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_date', 'is_active', 'id')


@admin.register(Register_Car02)
class Register_Car02Admin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_date', 'is_active', 'id')


@admin.register(Issue_Car01)
class Issue_Car01Admin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_date', 'is_active', 'id')


@admin.register(Issue_Car02)
class Issue_Car02Admin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_date', 'is_active', 'id')


@admin.register(Confirmation)
class ConfirmationAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_date', 'is_active', 'id')


@admin.register(FaqModelsTS)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question_ru', 'is_active', 'created_date')


@admin.register(FaqModelsVS)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question_ru', 'is_active', 'created_date')


@admin.register(PdfGet)
class PdfAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_date')

