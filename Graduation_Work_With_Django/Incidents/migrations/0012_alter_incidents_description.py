# Generated by Django 4.2.5 on 2024-04-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0011_alter_incidents_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Описание'),
        ),
    ]