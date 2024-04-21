from django.db import models
import datetime

from users.models import User


# Create your models here.

class Specifications(models.Model):
    pattern = models.CharField(max_length=100, verbose_name='Характеристика происшествия')
    color = models.CharField(max_length=20, verbose_name='Цвет происшествия')

    list_display = ('pattern', 'color')
    search_fields = ['pattern', 'color']

    class Meta:
        verbose_name = "Спецификацию происшествия"
        verbose_name_plural = "Спецификации происшествий"

        permissions = [
            ("specification_add", "Добавление спецификации происшествия"),
            ("specification_change", "Изменение спецификации происшествия"),
            ("specification_delete", "Удаление спецификации происшествия"),
            ("specification_id", "Просмотр спецификации происшествия"),

            ("specification_all", "Просмотр всех спецификаций в таблице"),
        ]

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
        permissions = [
            ("status_add", "Добавление статуса происшествия"),
            ("status_change", "Изменение статуса происшествия"),
            ("status_delete", "Удаление статуса происшествия"),
            ("status_id", "Просмотр статуса происшествия"),

            ("status_all", "Просмотр всех статусов в таблице"),
        ]

    def __str__(self):
        return self.status

class Incidents(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')
    description = models.CharField(max_length=255, verbose_name='Описание',)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    specification = models.ForeignKey(Specifications, on_delete = models.SET_DEFAULT, default=1, verbose_name='Спецификация происшествия')
    complete = models.BooleanField(default=False, null=True, blank=True)



    time_create = models.DateTimeField(verbose_name='Дата и время обнаружения происшествия', default=datetime.datetime.now(), blank=True)
    time_start = models.DateTimeField(verbose_name='Дата и время принятия решения',null=True, blank=True)
    time_end = models.DateTimeField(verbose_name='Дата и время ликвидирования происшествия',null=True, blank=True)


    status = models.ForeignKey(Status, on_delete = models.SET_DEFAULT,  verbose_name='Статус происшествия',default=3, blank=True, )

    user_create = models.ForeignKey(User, on_delete = models.SET_DEFAULT, default=1, verbose_name='Обнаружитель происшествия', blank=True, related_name='user_create')
    user_responsible = models.ForeignKey(User, on_delete = models.SET_DEFAULT, default=1, verbose_name='Ответственный за происшествие', blank=False, related_name='user_responsible')

    taken_measures = models.CharField(max_length=255, verbose_name='Принятые меры по ликвидации', null=True, blank=True)



    #электрики сообщат о происшествии диспетчеру, диспетчер - создание заявки о происшествии

    list_display = ('address','description', 'specification', 'user_create', 'status')
    search_fields = ['address', 'description','user_create']
    class Meta:
        verbose_name = "Происшествие"
        verbose_name_plural = "Происшествия"
        permissions = [
            ("incidents_add", "Добавление происшествий"),
            ("incidents_change", "Изменение происшествий"),
            ("incidents_delete", "Удаление происшествий"),
            ("incidents_id", "Просмотр происшествия"),
            ("incidents_map", "Просмотр всех происшествий на карте"),

            ("incidents_all", "Просмотр всех происшествий в таблице"),
        ]

    def __str__(self):
        return self.address



