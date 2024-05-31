from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from backend.apps.license.models import RegionCategories


class RatingSchool(models.Model):
    """Класс модели Рейтинг автошкол"""

    regions = models.ForeignKey(RegionCategories, verbose_name='Регион', on_delete=models.CASCADE)
    logo = models.ImageField('Логотип', upload_to="license/logo", blank=True)
    title_ru = RichTextUploadingField('Наименование на русском', max_length=599, blank=True)
    title_kg = RichTextUploadingField('Наименование на кыргызском', max_length=599, blank=True)
    percent_true = models.IntegerField('Процент прошедших', blank=True)
    percent_false = models.IntegerField('Процент непрошедших', blank=True)

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг автошкол'
