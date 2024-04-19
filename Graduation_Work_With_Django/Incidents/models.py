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

class Status(models.Model):
    status = models.CharField(max_length=100, verbose_name='Статус происшествия')
    description = models.CharField(max_length=100, verbose_name='Описание статуса происшествия')

    list_display = ('status', 'description')
    search_fields = ['status', 'description']

    class Meta:
        verbose_name = "Статус происшествия"
        verbose_name_plural = "Статусы происшествий"

    def __str__(self):
        return self.status

class Incidents(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')
    description = models.CharField(max_length=255, verbose_name='Описание',)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    specification = models.ForeignKey(Specifications, on_delete = models.SET_DEFAULT, default=1, verbose_name='Спецификация происшествия')

    time_create = models.DateTimeField(verbose_name='Дата и время обнаружения происшествия', default=datetime.datetime.now(), blank=True)

    status = models.ForeignKey(Status, on_delete = models.SET_DEFAULT,  verbose_name='Статус происшествия',default=3, blank=True, )

    user_create = models.ForeignKey(User, on_delete = models.SET_DEFAULT, default=1, verbose_name='Обнаружитель происшествия', blank=True, related_name='user_create')
    user_responsible = models.ForeignKey(User, on_delete = models.SET_DEFAULT, default=1, verbose_name='Ответственный за происшествие', blank=False, related_name='user_responsible')

    taken_measures = models.CharField(max_length=255, verbose_name='Принятые меры по ликвидации', null=True, blank=True)



    #электрики сообщат о происшествии диспетчеру, диспетчер - создание заявки о происшествии

    list_display = ('address','description', 'specification', 'user_create', 'status')
    search_fields = ['address', 'description','user_create']
    class Meta:
        verbose_name = "инцидент"
        verbose_name_plural = "Инциденты"

    def __str__(self):
        return self.address



