# Generated by Django 3.2.9 on 2021-12-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20211225_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.BigIntegerField(verbose_name='Индентификатор пользователя'),
        ),
    ]
