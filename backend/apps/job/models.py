from django.db import models


class Job(models.Model):
    """Класс модели вакансия"""

    title_ru = models.CharField('Название вакансии на руссском', max_length=299, null=True, blank=True)
    title_kg = models.CharField('Название вакансии на кыргызском', max_length=299, null=True, blank=True)
    city = models.CharField('Название отдела и города', max_length=299, null=True, blank=True)
    note_ru = models.CharField('Примичание на русском', max_length=599, null=True, blank=True)
    note_kg = models.CharField('Примичание на кыргызском', max_length=599, null=True, blank=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
