from django.db import models


class PdfGet(models.Model):
    """Класс модели PDF"""

    title = models.CharField('Наименование', max_length=599, blank=True)
    banner = models.ImageField("Банер", blank=True)
    documents_pdf = models.FileField('Вставка файла', upload_to="pdf/", blank=True)

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Форму'
        verbose_name_plural = 'Форма бланков'
