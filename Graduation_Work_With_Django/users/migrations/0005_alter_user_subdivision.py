# Generated by Django 4.2.5 on 2024-04-18 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subdivisions', '0006_alter_subdivisions_abbreviation_and_more'),
        ('users', '0004_user_subdivision_alter_user_lastname_alter_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subdivision',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='user_subdivision', to='Subdivisions.subdivisions', verbose_name='Подразделение'),
        ),
    ]
