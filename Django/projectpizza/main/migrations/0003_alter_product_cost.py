# Generated by Django 3.2.9 on 2022-01-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.FloatField(verbose_name='Цена'),
        ),
    ]