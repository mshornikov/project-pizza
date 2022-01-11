from decimal import Decimal 
from django.conf import settings
from main.models import Product
import requests
class Cart(object):
    # создание пустой корзины, если ее нет в сессии
    # создание наполненной корзины, если в текущей сессии таковая нашлась
    def __init__(self, request):
        self.session = request.session
        self.session_id = request.session.session_key
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Добавить в корзину
    def add(self, product, quant):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quant, 'price': product.cost}
        else:
            self.cart[product_id]['quantity'] += quant
        self.save()

    # Обновить корзину
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    # Удалить из корзины
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # итератор для отображения корзины на сайте
    def __iter__(self):
        product_ids=self.cart.keys()
        productList = Product.objects.filter(id__in=product_ids)
        for product in productList:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # количество позиций в корзине
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # общая стоимость корзины
    def get_total_price(self) :
        return sum(Decimal(item['price']) * item['quantity'] for item in
               self.cart.values())
               
    # очистить корзину сессии
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True