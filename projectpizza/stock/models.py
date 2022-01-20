from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from main.models import Product
from users.models import CustomUser
# Create your models here.


class Stock(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    stock_key = models.CharField(max_length=10, verbose_name='Код акции')
    stock_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Акционный товар')
    stock_value = models.IntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(100)], verbose_name='Размер скидки')
    stock_type = models.CharField(max_length=50, verbose_name='Тип акции', null=True)
    active_intil = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата окончания')

    def __str__(self):
        return self.stock_key

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ['stock_key']


