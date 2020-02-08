# Generated by Django 3.0.3 on 2020-02-08 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200205_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bankcard',
            name='end_date',
            field=models.DateField(default=datetime.date(2021, 2, 7)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sum',
            field=models.IntegerField(),
        ),
    ]