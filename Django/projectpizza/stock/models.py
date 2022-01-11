from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from main.models import Product
# Create your models here.

stock_id_validator = RegexValidator(regex='[a-zA-Z0-9]{10}', message='Недопустимый вид кода акции - ровно 10 символов')

class Stock(models.Model):
    stock_key = models.CharField(max_length=10, validators=[stock_id_validator], verbose_name='Код акции')
    stock_product = models.OneToOneField(Product, on_delete=models.PROTECT, verbose_name='Акционный товар')
    stock_value = models.IntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(100)], verbose_name='Размер скидки')

    def __str__(self):
        return self.stock_key

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ['id']


