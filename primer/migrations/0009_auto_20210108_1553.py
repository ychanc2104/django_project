# Generated by Django 3.1.4 on 2021-01-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer', '0008_primer_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primer',
            name='length',
            field=models.IntegerField(blank=True),
        ),
    ]
