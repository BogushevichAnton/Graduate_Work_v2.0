# Generated by Django 4.2.5 on 2024-04-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0008_incidents_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidents',
            name='address',
            field=models.CharField(default='rere', max_length=250, verbose_name='Адрес'),
        ),
    ]
