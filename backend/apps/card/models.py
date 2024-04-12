from django.db import models





# Create your models here.
class ServiceORM(models.Model):
    title = models.CharField('Наименование', max_length=105)
    descriptions = models.CharField('Описание', max_length=145)
    url_link = models.URLField('Ссылка на страницу', max_length=699, blank=True)
    image = models.ImageField('Картина', upload_to="service/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы для гл стр'