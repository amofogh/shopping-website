# Generated by Django 3.2.9 on 2021-12-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.TextField(max_length=90),
        ),
    ]
