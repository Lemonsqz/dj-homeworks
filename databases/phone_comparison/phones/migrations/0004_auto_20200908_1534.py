# Generated by Django 2.2.10 on 2020-09-08 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_auto_20200908_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='d_camera',
            field=models.TextField(null=True, verbose_name='Двойная камера'),
        ),
    ]