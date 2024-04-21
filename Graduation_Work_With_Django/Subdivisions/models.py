from django.db import models

class Subdivisions(models.Model):
    abbreviation = models.CharField(max_length=10, verbose_name='Aббревиатура', null=False, blank=False)
    description = models.CharField(max_length=250, verbose_name='Описание подразделения', null=False, blank=False)
    address = models.CharField(max_length=250, verbose_name='Адрес подразделения', null=False, blank=False)
    latitude = models.FloatField(verbose_name='Широта', null=False)
    longitude = models.FloatField(verbose_name='Долгота', null=False)

    list_display = ('abbreviation', 'description', 'address')
    search_fields = ['abbreviation', 'description', 'address']

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

        permissions = [
            ("Subdivisions.subdivision_add", "Добавление подразделения"),
            ("Subdivisions.subdivision_change", "Изменение подразделения"),
            ("Subdivisions.subdivision_delete", "Удаление подразделения"),
            ("Subdivisions.subdivision_id", "Просмотр подразделения"),
            ("Subdivisions.subdivision_map", "Просмотр всех подразделений на карте"),

            ("Subdivisions.subdivision_all", "Просмотр всех подразделений в таблице"),
        ]

    def __str__(self):
        return self.abbreviation
