# Generated by Django 3.2.9 on 2021-12-30 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop_orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
