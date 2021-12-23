from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=255)
    cost = models.FloatField()
    category = models.ForeignKey("ProductCategory", on_delete=PROTECT, null=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name