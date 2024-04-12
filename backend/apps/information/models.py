from django.db import models


class Register_Car01(models.Model):
    number = models.CharField('№', max_length=599, blank=True, null=True)
    title = models.CharField('Наименование услуги', max_length=599, blank=True, null=True)
    price = models.CharField('Стоимость', max_length=599, blank=True, null=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация прав собственности на автотранспорт'


class Register_Car02(models.Model):
    number = models.CharField('№', max_length=599, blank=True, null=True)
    title = models.CharField('Наименование услуги', max_length=599, blank=True, null=True)
    price = models.CharField('Стоимость', max_length=599, blank=True, null=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация прав собственности на трактора и оборудование'


class Issue_Car01(models.Model):
    number = models.CharField('№', max_length=599, blank=True, null=True)
    title = models.CharField('Наименование услуги', max_length=599, blank=True, null=True)
    price = models.CharField('Стоимость', max_length=599, blank=True, null=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Выдача'
        verbose_name_plural = 'Выдача водительского удостоверения на право управления транспортными средствами'


class Issue_Car02(models.Model):
    number = models.CharField('№', max_length=599, blank=True, null=True)
    title = models.CharField('Наименование услуги', max_length=599, blank=True, null=True)
    price = models.CharField('Стоимость', max_length=599, blank=True, null=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Выдача'
        verbose_name_plural = 'Выдача удостоверения тракториста машиниста на право управления самоходными технологическими машинами'


class Confirmation(models.Model):
    number = models.CharField('№', max_length=599, blank=True, null=True)
    title = models.CharField('Наименование услуги', max_length=599, blank=True, null=True)
    price = models.CharField('Стоимость', max_length=599, blank=True, null=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подтверждение'
        verbose_name_plural = 'Подтверждение сведений о транспортных средствах и водительских удостоверениях'