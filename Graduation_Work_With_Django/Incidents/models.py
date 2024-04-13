from django.db import models
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
    specification = models.ForeignKey(Specifications, on_delete = models.SET_DEFAULT, default=1)

    list_display = ('address','description', 'latitude', 'longitude', 'specification')
    search_fields = ['address', 'description']
    class Meta:
        verbose_name = "инцидент"
        verbose_name_plural = "Инциденты"

    def __str__(self):
        return self.address



