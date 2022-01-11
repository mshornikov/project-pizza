from decimal import Decimal 
from django.conf import settings
from django.http.request import RawPostDataException
from main.models import Product

class Cart(object):
    # создание пустой корзины, если ее нет в сессии
    # создание наполненной корзины, если в текущей сессии таковая нашлась
    def __init__(self, request):
        self.session = request.session
        self.session_id = request.session.session_key
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {'default':{}, 'stock_cart':{}}
        self.cart = cart

    # Добавить в корзину обычный товар
    def add(self, product, quant):
        product_id = str(product.id)
        if product_id not in self.cart['default']:
            self.cart['default'][product_id] = {'quantity': quant, 'price': product.cost}
        else:
            self.cart['default'][product_id]['quantity'] += quant
        self.save()

    # Добавить в корзину товар акции
    def stock_add(self, stock_object):
        product_id = str(stock_object.stock_product.id)
        if product_id not in self.cart['stock_cart']:
            self.cart['stock_cart'][product_id] = {'quantity': 1, 'price': (1 - stock_object.stock_value/100) * stock_object.stock_product.cost}
            self.save()

    # Обновить корзину
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    # Удалить из корзины
    def remove(self, product, cart_type):
        product_id = str(product.id)
        if product_id in self.cart[cart_type]:
            del self.cart[cart_type][product_id]
            self.save()

    # итератор для отображения корзины на сайте
    def __iter__(self):
        product_ids = list(self.cart['default'].keys()) + list(self.cart['stock_cart'].keys())

        productList = Product.objects.filter(id__in=list(set(product_ids)))

        for product in productList:
            if str(product.id) in self.cart['default']:
                self.cart['default'][str(product.id)]['product'] = product
            if str(product.id) in self.cart['stock_cart']:
                self.cart['stock_cart'][str(product.id)]['product'] = product
                
        for cart_type in self.cart:
            for item in self.cart[cart_type].values():
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * item['quantity']
                yield {'type':str(cart_type), 'item':item}

    # количество позиций в корзине
    def __len__(self):
        result = 0
        for type in self.cart:
            for item in self.cart[type].values():
                result += item['quantity']
        return result
    # общая стоимость корзины
    def get_total_price(self):
        result = 0
        for type in self.cart:
            for item in self.cart[type].values():
                result += Decimal(item['price'] * item['quantity'])
        return result
    # очистить корзину сессии

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True