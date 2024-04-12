from django.db import models


class Job(models.Model):
    title = models.CharField('Название вакансии', max_length=299, null=True, blank=True)
    city = models.CharField('Название отдела и города', max_length=299, null=True, blank=True)
    note = models.CharField('Примичание', max_length=299, null=True, blank=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
