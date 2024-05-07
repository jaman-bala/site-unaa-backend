from django.db import models


class License(models.Model):
    """Класс модели лицензия"""

    title_ru = models.CharField('Наименование на русском', max_length=599)
    title_kg = models.CharField('Наименование на кыргызском', max_length=599)
    address_ru = models.TextField('Адрес на русском', max_length=599)
    address_kg = models.TextField('Адрес на кыргызском', max_length=599)
    category = models.TextField('Категория', max_length=599)
    date = models.DateTimeField('Дата выдачи')

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лизензии'
