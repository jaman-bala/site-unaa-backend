from django.db import models


class CalculatorCar(models.Model):
    car = models.CharField('Тип', max_length=155)

    def __str__(self):
        return self.car

    class Meta:
        verbose_name_plural = "Транспортные средства"


class CalculatorVolume(models.Model):
    volume = models.CharField('Объём', max_length=155)

    def __str__(self):
        return self.volume

    class Meta:
        verbose_name_plural = "Объём"


class CalculatorYear(models.Model):
    year = models.CharField('Год', max_length=155)

    def __str__(self):
        return self.year

    class Meta:
        verbose_name_plural = "Год"


class CalculatorEngine(models.Model):
    engine = models.CharField('Двигатель', max_length=155)

    def __str__(self):
        return self.engine

    class Meta:
        verbose_name_plural = "Двигатель"


class CalculatorStatus(models.Model):
    status = models.CharField('Статус', max_length=155)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "Статус оформления"


class CalculatorAllList(models.Model):
    car = models.ForeignKey(CalculatorCar, verbose_name="Тип", on_delete=models.CASCADE)
    volume = models.ForeignKey(CalculatorVolume, verbose_name="Объём", on_delete=models.CASCADE, )
    year = models.ForeignKey(CalculatorYear, verbose_name="Год", on_delete=models.CASCADE)
    engine = models.ForeignKey(CalculatorEngine, verbose_name="Двигатель", on_delete=models.CASCADE)
    status = models.ForeignKey(CalculatorStatus, verbose_name="Статус", on_delete=models.CASCADE)

    sum = models.CharField(max_length=155)

    def __str__(self):
        return f'{self.status} {self.sum}'

    class Meta:
        verbose_name_plural = "Вывод данных калькулятора"



