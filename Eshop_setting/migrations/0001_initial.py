# Generated by Django 3.2.9 on 2021-12-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='site_setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=150, verbose_name='نام سایت')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='آدرس')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره تلفن')),
                ('fax', models.CharField(blank=True, max_length=50, null=True, verbose_name='فکس')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='ایمیل')),
                ('about_us', models.TextField(verbose_name='درباره ما')),
            ],
        ),
    ]