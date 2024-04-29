from django.db import models


class ServiceORM(models.Model):
    """Класс модели сервиса"""

    title_ru = models.CharField('Наименование на русском', max_length=105)
    title_kg = models.CharField('Наименование на кыргызском', max_length=105)
    descriptions_ru = models.TextField('Описание на русском', max_length=145)
    descriptions_kg = models.TextField('Описание на кыргызском', max_length=145)
    url_link = models.URLField('Ссылка на страницу', max_length=699, blank=True)
    image = models.ImageField('Картина', upload_to="service/", blank=True)

    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы для гл стр'