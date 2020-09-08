from django.db import models


# Create your models here.
class Phones(models.Model):
    model_name = models.CharField(max_length=25, blank=True, null=True, verbose_name='Название модели')
    price = models.IntegerField(null=True, verbose_name='Цена')
    os = models.TextField(blank=True, null=True, verbose_name='Операционная система')
    ram = models.IntegerField(null=True, verbose_name='Оперативная память')
    ppi = models.CharField(max_length=25, null=True, verbose_name='Пикселей на дюйм')
    d_camera = models.TextField(null=True, verbose_name='Двойная камера')
    cpu = models.TextField(blank=True, null=True, verbose_name='Процессор')
    screen = models.TextField(blank=True, null=True, verbose_name='Разрешение экрана')

    def __str__(self):
        return self.model_name


class Samsung(models.Model):
    model = models.ForeignKey(Phones, on_delete=models.CASCADE, verbose_name='Название модели')
    compass = models.TextField(null=True, verbose_name='компас')
    gyroscope = models.TextField(null=True, verbose_name='гироскоп')

    def __str__(self):
        return self.model.model_name


class Xiaomi(models.Model):
    model = models.ForeignKey(Phones, on_delete=models.CASCADE, verbose_name='Название модели')
    radio = models.TextField(null=True, blank=True, verbose_name='FM-радио')
    recorder = models.TextField(null=True, blank=True, verbose_name='Диктофон')

    def __str__(self):
        return self.model.model_name


