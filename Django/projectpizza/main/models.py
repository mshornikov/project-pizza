from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    discription = models.CharField(max_length=255, verbose_name='Описание')
    cost = models.FloatField(verbose_name='Цена')
    image = models.ImageField(upload_to="productImages", null=True, verbose_name='Фото')
    category = models.ForeignKey('ProductCategory', on_delete=PROTECT, null=True, verbose_name='Категория')
   
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering=['id']

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
