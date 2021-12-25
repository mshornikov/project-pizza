from django.db import models
from django.db.models.deletion import PROTECT
from main.models import Product
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=PROTECT, verbose_name='Идентификатор Пользователя', default=1)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    address = models.CharField(max_length=300, verbose_name='Адресс')
    city = models.CharField(max_length=50, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    paid = models.BooleanField(default=False, verbose_name='Статус оплаты')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.DO_NOTHING, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.DO_NOTHING, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return '{}'.format(self.id)
    
    def get_cost(self):
        return self.price * self.quantity