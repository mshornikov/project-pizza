# Generated by Django 3.2.9 on 2021-12-24 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211223_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='productImages', verbose_name='Фото'),
        ),
    ]
