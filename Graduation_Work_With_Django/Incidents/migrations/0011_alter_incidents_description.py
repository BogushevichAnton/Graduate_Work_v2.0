# Generated by Django 4.2.5 on 2024-04-13 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0010_alter_incidents_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='description',
            field=models.CharField(max_length=250, null=True, verbose_name='Описание'),
        ),
    ]
