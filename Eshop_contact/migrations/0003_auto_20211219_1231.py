# Generated by Django 3.2.9 on 2021-12-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_contact', '0002_contact_us_is_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact_us',
            options={'verbose_name': 'پیام ها', 'verbose_name_plural': 'پیام های کاربران'},
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='موضوع'),
        ),
    ]
