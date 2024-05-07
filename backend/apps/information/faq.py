from django.db import models


class FaqModels(models.Model):
    """Класс модели FAQ"""

    question_ru = models.TextField('Вопрос на русском', max_length=255)
    question_kg = models.TextField('Вопрос на кыргызском', max_length=255)
    answer_ru = models.TextField('Ответ на русском')
    answer_kg = models.TextField('Ответ на кыргызском')

    is_active = models.BooleanField("Активный", default=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.question_ru

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
