from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Documents(models.Model):
    """Класс модели перечень"""

    title_ru = models.CharField('Наименование на русском', max_length=599, blank=True)
    title_kg = models.CharField('Наименование на кыргызском', max_length=599, blank=True)
    text_ru = RichTextUploadingField('Статья на русском', blank=True)
    text_ky = RichTextUploadingField('Статья на кыргызском', blank=True)

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Перечень'
        verbose_name_plural = 'Перечни'


class DocumentsNPA(models.Model):
    """Класс модели НПА"""

    title_ru = models.CharField('Наименование на русском', max_length=599, blank=True)
    title_kg = models.CharField('Наименование на кыргызском', max_length=599, blank=True)
    text_ru = RichTextUploadingField('Статья на русском', blank=True)
    text_ky = RichTextUploadingField('Статья на кыргызском', blank=True)

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'НПА'
        verbose_name_plural = 'НПА'


class DopDoc(models.Model):
    """Класс модели Доп. требований"""

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
        verbose_name = 'Доп'
        verbose_name_plural = 'Доп. требований'


class License(models.Model):
    """Класс модели лицензия"""

    logo = models.ImageField('Логотип', upload_to="license/logo", blank=True)
    title_ru = models.CharField('Наименование на русском', max_length=599, blank=True)
    title_kg = models.CharField('Наименование на кыргызском', max_length=599, blank=True)
    register_number = models.CharField('Регистрационный номер', max_length=599, blank=True)
    address_ru = RichTextUploadingField('Адрес на русском', max_length=599, blank=True)
    address_kg = RichTextUploadingField('Адрес на кыргызском', max_length=599, blank=True)
    category = RichTextUploadingField('Категория', max_length=599, blank=True)
    issued_authority_ru = RichTextUploadingField('Выданный орган на русском', max_length=599, blank=True)
    issued_authority_kg = RichTextUploadingField('Выданный орган на кыргызском', max_length=599, blank=True)
    date = models.DateTimeField('Дата выдачи')

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лизензии для автошкол'


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
    title_ru = models.CharField('Наименование на русском', max_length=599, blank=True)
    title_kg = models.CharField('Наименование на кыргызском', max_length=599, blank=True)
    percent_true = models.CharField('Процент прошедших', max_length=6, blank=True)
    percent_false = models.CharField('Процент непрошедших', max_length=6, blank=True)

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг автошкол'


