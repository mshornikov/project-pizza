from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    productName = models.CharField(max_length=50)
    productDescription = models.CharField(max_length=300)
    productIngredients = models.CharField(max_length=300)
    productPrice = models.FloatField()
    productPhoto = models.ImageField()
    productCategory = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.productName

    def get_absolute_url(self):
        return reverse('showProduct', kwargs={'productID': self.pk})

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName 

