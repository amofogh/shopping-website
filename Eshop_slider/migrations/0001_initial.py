# Generated by Django 3.2.9 on 2021-12-17 21:00

import Eshop_slider.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('description', models.TextField()),
                ('link', models.URLField(verbose_name='لینک')),
                ('image', models.ImageField(upload_to=Eshop_slider.models.upload_image_path, verbose_name='تصویر')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'اسلایدرها',
                'verbose_name_plural': 'اسلایدر',
            },
        ),
    ]
