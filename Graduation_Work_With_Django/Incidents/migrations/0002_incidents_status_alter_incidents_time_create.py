# Generated by Django 4.2.5 on 2024-04-19 11:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidents',
            name='status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Incidents.status', verbose_name='Спецификация происшествия'),
        ),
        migrations.AlterField(
            model_name='incidents',
            name='time_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 19, 14, 27, 18, 136225), verbose_name='Дата и время обнаружения происшествия'),
        ),
    ]