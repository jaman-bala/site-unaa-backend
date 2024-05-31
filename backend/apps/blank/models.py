from django.db import models


class PDF(models.Model):
    """Класс модели PDF"""

    title = models.CharField('Наименование', max_length=599, blank=True)

    banner = models.ImageField("Банер", upload_to="banner/", blank=True)
    file = models.FileField('Вставка файла', upload_to="pdf/", blank=True)

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бланк'
        verbose_name_plural = 'Бланки'


