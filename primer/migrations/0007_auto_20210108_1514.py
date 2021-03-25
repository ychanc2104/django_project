# Generated by Django 3.1.4 on 2021-01-08 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primer', '0006_primer_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='primer',
            name='dir',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AddField(
            model_name='primer',
            name='in_vector',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='primer',
            name='position',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AddField(
            model_name='primer',
            name='vector',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vector', to='primer.vector'),
        ),
    ]