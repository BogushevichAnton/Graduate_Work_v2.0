from django.db import models

class Subdivisions(models.Model):
    abbreviation = models.CharField(max_length=10, verbose_name='Aббревиатура', null=False, blank=False, default='123')
    description = models.CharField(max_length=50, verbose_name='Описание подразделения', null=False, blank=False)

    list_display = ('abbreviation', 'description')
    search_fields = ['abbreviation', 'description']

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return self.abbreviation
