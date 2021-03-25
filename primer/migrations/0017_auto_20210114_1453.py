# Generated by Django 3.1.4 on 2021-01-14 06:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer', '0016_auto_20210114_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primer',
            name='length',
            field=models.IntegerField(blank=True, default=-1, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)]),
        ),
    ]