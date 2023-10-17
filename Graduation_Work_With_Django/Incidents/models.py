from django.db import models
# Create your models here.

class Incidents(models.Model):
    description = models.CharField(max_length=250, verbose_name='Описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    list_display = ('description', 'latitude', 'longitude')
    class Meta:
        verbose_name = "инцидент"
        verbose_name_plural = "Инциденты"

    def __str__(self):
        return self.description

