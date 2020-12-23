# Generated by Django 2.2.12 on 2020-12-23 03:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20201223_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 23, 6, 0, 9, 555868), verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 23, 6, 0, 9, 556835), verbose_name='Дата'),
        ),
    ]
