from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class VisualDocuments(models.Model):
    """Класс модели Реквизита"""

    title_ru = models.CharField('Наименование на русском', max_length=599, blank=True)
    title_kg = models.CharField('Наименование на кыргызском', max_length=599, blank=True)
    text_ru = RichTextUploadingField('Статья на русском', blank=True)
    text_ky = RichTextUploadingField('Статья на кыргызском', blank=True)

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'реквизит'
        verbose_name_plural = 'Реквизиты'


class BusinessContact(models.Model):
    """Класс модели Контактов"""

    title_ru = models.CharField('Наименование на русском', max_length=599, blank=True)
    title_kg = models.CharField('Наименование на кыргызском', max_length=599, blank=True)
    text_ru = RichTextUploadingField('Статья на русском', blank=True)
    text_ky = RichTextUploadingField('Статья на кыргызском', blank=True)

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'Контакты'
