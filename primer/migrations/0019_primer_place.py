# Generated by Django 3.1.4 on 2021-01-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer', '0018_auto_20210115_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='primer',
            name='place',
            field=models.CharField(default='Project box', max_length=50),
        ),
    ]