# Generated by Django 3.1.4 on 2021-01-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer', '0011_auto_20210113_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='primer',
            name='modification_5',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
    ]