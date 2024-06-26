from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class History(models.Model):
    """Класс модели истории"""

    title = RichTextUploadingField('История', blank=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'


class Management(models.Model):
    """Класс модели руководства"""

    title = models.CharField('Должность', max_length=255)
    name = models.CharField('ФИО', max_length=255)
    description_ru = RichTextUploadingField('Биограция на русском')
    description_kg = RichTextUploadingField('Биограция на кыргызском')
    avatar = models.ImageField('Аватар', upload_to="avatar/", blank=True)

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Руководства'
        verbose_name_plural = 'Руководители'


class Contact(models.Model):
    """Класс модели контактов"""

    title = models.CharField("Наименование отдела", max_length=555, null=True, blank=True)
    address = RichTextUploadingField('Адрес', max_length=555, null=True, blank=True)
    phone = models.CharField('Контактные данные', max_length=555, null=True, blank=True)
    time_job = RichTextUploadingField('Время и график работы', max_length=255, null=True, blank=True)

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
