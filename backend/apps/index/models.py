from django.db import models


class Index(models.Model):
    """Класс модели видео"""

    title = models.CharField("Наименование видео", max_length=500)
    file = models.FileField("Путь к видео", upload_to="file-video/", blank=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'