# Generated by Django 4.2.5 on 2024-04-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subdivisions', '0004_subdivisions_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdivisions',
            name='latitude',
            field=models.FloatField(default='1', verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='subdivisions',
            name='longitude',
            field=models.FloatField(default='1', verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='subdivisions',
            name='address',
            field=models.CharField(default='г. Москва', max_length=250, verbose_name='Адрес подразделения'),
        ),
        migrations.AlterField(
            model_name='subdivisions',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Описание подразделения'),
        ),
    ]
