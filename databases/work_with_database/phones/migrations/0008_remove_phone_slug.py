# Generated by Django 2.2.10 on 2020-09-06 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0007_phone_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='slug',
        ),
    ]
