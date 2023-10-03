from django.db import models
# Create your models here.

class Incidents(models.Model):
    description = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = "Инцидент"
        verbose_name_plural = "Инциденты"

    def __str__(self):
        return self.description

