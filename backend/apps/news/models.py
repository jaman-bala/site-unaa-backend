from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Image(models.Model):
    """Модель для изображений"""

    news = models.ForeignKey(
        'News',
        verbose_name="Новость",
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField("Путь к фотографиям", upload_to="news/", blank=True)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображении'


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=News.Status.PUBLISHED)


class News(models.Model):
    """Класс модели новостей"""

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title_ru = models.CharField("Тема на русском", max_length=500)
    title_ky = models.CharField("Тема на кыргызском", max_length=500)
    text_ru = RichTextUploadingField('Статья на русском')
    text_ky = RichTextUploadingField('Статья на кыргызском')
    url_youtube_ru = models.URLField("URL с Ютуба на русском", max_length=500, blank=True)
    url_youtube_kg = models.URLField("URL с Ютуба на кыргызском", max_length=500, blank=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    published_date = models.DateTimeField(
        "Дата публикации",
        default=timezone.now,
        blank=True,
        null=True
    )

    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLISHED, verbose_name="Статус")
    viewed = models.IntegerField("Просмотрено", default=0)
    is_active = models.BooleanField("Активный", default=True)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title_ru

    class Meta:
        ordering = ["-created_date"]
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

