# Generated by Django 3.2.9 on 2021-12-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_setting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_setting',
            name='copyright',
            field=models.CharField(default='default', max_length=500, verbose_name='متن کپی رایت'),
            preserve_default=False,
        ),
    ]
