# Generated by Django 3.2.9 on 2021-12-24 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adrress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
