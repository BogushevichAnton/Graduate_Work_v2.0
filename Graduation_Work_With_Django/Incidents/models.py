from django.db import models
import datetime

from users.models import User


# Create your models here.

class Specifications(models.Model):
    pattern = models.CharField(max_length=100, verbose_name='Характеристика инцидента')
    color = models.CharField(max_length=20, verbose_name='Цвет инцидента')

    list_display = ('pattern', 'color')
    search_fields = ['pattern', 'color']

    class Meta:
        verbose_name = "Спецификация инцидентов"
        verbose_name_plural = "Спецификации инцидентов"

    def __str__(self):
        return self.pattern
class Incidents(models.Model):
    address = models.CharField(max_length=250, verbose_name='Адрес')
    description = models.CharField(max_length=250, verbose_name='Описание',)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    specification = models.ForeignKey(Specifications, on_delete = models.SET_DEFAULT, default=1, verbose_name='Спецификация происшествия')
    time_create = models.DateTimeField(verbose_name='Дата и время обнаружения происшествия', default=datetime.datetime.now(), blank=True)
    user_create = models.ForeignKey(User, on_delete = models.SET_DEFAULT, default=1, verbose_name='Обнаружитель происшествия', blank=True)

    list_display = ('address','description', 'specification', 'user_create')
    search_fields = ['address', 'description','user_create']
    class Meta:
        verbose_name = "инцидент"
        verbose_name_plural = "Инциденты"

    def __str__(self):
        return self.address



