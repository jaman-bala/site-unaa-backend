from django.contrib import admin

from backend.apps.service.models import CalculatorAllList, CalculatorCar, CalculatorVolume, CalculatorYear, CalculatorEngine, CalculatorStatus


@admin.register(CalculatorAllList)
class CalculatorAllList(admin.ModelAdmin):
    list_display = ('car', 'volume', 'year', 'engine', 'sum', 'id', 'status')
    search_fields = ('car', 'volume', 'year', 'sum')
    save_on_top = True


@admin.register(CalculatorCar)
class CalculatorCar(admin.ModelAdmin):
    list_display = ('car',)


@admin.register(CalculatorVolume)
class CalculatorVolume(admin.ModelAdmin):
    list_display = ('volume',)


@admin.register(CalculatorYear)
class CalculatorYear(admin.ModelAdmin):
    list_display = ('year',)


@admin.register(CalculatorEngine)
class CalculatorEngine(admin.ModelAdmin):
    list_display = ('engine',)


@admin.register(CalculatorStatus)
class CalculatorStatus(admin.ModelAdmin):
    list_display = ('status',)


