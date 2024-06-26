# Generated by Django 5.0.6 on 2024-05-15 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_gasstation_code_gastype_code_stationimage_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasstation',
            name='code',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='gastype',
            name='code',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='stationimage',
            name='code',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
