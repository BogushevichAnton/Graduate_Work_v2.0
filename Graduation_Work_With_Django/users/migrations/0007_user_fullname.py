# Generated by Django 4.2.5 on 2024-04-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_subdivision'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(default='Нет полного имени', max_length=255, verbose_name='Полное имя'),
        ),
    ]
