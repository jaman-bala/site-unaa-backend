from django.db import models


class Department(models.Model):
    """Класс модели отделов"""

    title = models.CharField('Отдел', max_length=299)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Appeal(models.Model):
    """Класс модели обращения"""

    nearest_department = models.ForeignKey(Department, verbose_name='Отдел', on_delete=models.CASCADE)
    full_name = models.CharField('Ф.И.О', max_length=255)
    phone_number = models.CharField('Номер сотового телефона', max_length=15)
    email = models.EmailField('Почта')
    car_number = models.CharField('Гос номер транспорта', max_length=20)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Обращения'
        verbose_name_plural = 'Обращение'
