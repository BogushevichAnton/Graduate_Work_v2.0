# Generated by Django 4.2.5 on 2024-04-19 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0002_incidents_status_alter_incidents_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='time_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 19, 14, 49, 5, 430955), verbose_name='Дата и время обнаружения происшествия'),
        ),
    ]
