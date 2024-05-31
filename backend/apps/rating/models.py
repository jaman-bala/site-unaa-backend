from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class RegionCategories(models.Model):
    """Класс модели Регионы"""

    title = models.CharField('Регион', max_length=599, blank=True)
    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регионы'
        verbose_name_plural = 'Регион'


class RatingSchool(models.Model):
    """Класс модели Рейтинг автошкол"""

    regions = models.ForeignKey(RegionCategories, verbose_name='Регион', on_delete=models.CASCADE)
    logo = models.ImageField('Логотип', upload_to="license/logo", blank=True)
    title_ru = RichTextUploadingField('Наименование на русском', max_length=599, blank=True)
    title_kg = RichTextUploadingField('Наименование на кыргызском', max_length=599, blank=True)
    percent_true = models.CharField('Процент прошедших', max_length=599, blank=True)
    percent_false = models.CharField('Процент непрошедших', max_length=599, blank=True)
    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг автошкол'
