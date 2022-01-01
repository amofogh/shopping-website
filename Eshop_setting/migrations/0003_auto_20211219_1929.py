# Generated by Django 3.2.9 on 2021-12-19 15:59

import Eshop_products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_setting', '0002_site_setting_copyright'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site_setting',
            options={'verbose_name': 'تنظیمات سایت', 'verbose_name_plural': 'مدیریت تنظیمات'},
        ),
        migrations.AddField(
            model_name='site_setting',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=Eshop_products.models.upload_image_path, verbose_name='لوگو سایت'),
        ),
    ]
