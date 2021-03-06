# Generated by Django 2.2.10 on 2020-09-01 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('release_date', models.TimeField()),
                ('lte_exists', models.BooleanField(null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
