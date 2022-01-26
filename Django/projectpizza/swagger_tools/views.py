from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404

from django.utils.timezone import now

from cart.cart import Cart
from stock.models import Stock
# <----SESSION CART---->
class CartDetailAPIView(APIView):
    """Вывод содержимого корзины в данной сессии"""
    def get(self, request, **kwargs):
        cart = Cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
class CartAddAPIView(APIView):
    """Добавление заданного количества товара в корзину"""
    def post(self, request, pk, quant, **kwargs):
        cart = Cart(request)
        cart.add(get_object_or_404(Product, id=pk), quant)
        serializer = CartSerializer(cart) 
        return Response(serializer.data)

class CartAddStockAPIView(APIView):
    """Добавление в корзину акционного товара"""
    def post(self, request, key, **kwargs):
        cart = Cart(request)
        serializer = CartSerializer(cart)
        response = Response()
        try:
            stock = Stock.objects.get(stock_key=key)
            if (stock.user_id.id == request.user.id):
                if stock.active_intil > now() :
                    cart.stock_add(stock)
                    return Response(serializer.data)
                else:
                    return response(data={'message':"Неверный ключ"})
            else:
                return response(data={'message':"На данный момент нет акции с таким кодом"})
        except:
            return response(data={'message':"Неверный формат ввода :("})

class CartRemoveAPIView(APIView):
    """Удаление товара из корзины"""
    def post(self, request, pk, type, **kwargs):
        if type not in ['default', 'stock_cart']:
            return Response(data={'message':'Неверный формат адреса'})
        cart = Cart(request)
        cart.remove(get_object_or_404(Product, id=pk), type)
        serializer = CartSerializer(cart) 
        return Response(serializer.data)

# <----PRODUCT AND CATEGORY---->
class ProductListAPIView(ListAPIView):
    """Вывод списка всех существующих товаров"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class CategoryListAPIView(ListAPIView):
    """Вывод списка всех существующих категорий"""
    serializer_class=CategorySerializer

    def get_queryset(self):
        return ProductCategory.objects.all()

# <----ORDER AND ORDERITEMS---->
class OrderListAPIView(ListAPIView):
    """Вывод списка всех совершенных заказов"""
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.all()

class OrderItemsListAPIView(ListAPIView):
    """Вывод списка пунктов всех существующих заказов"""
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItems.objects.all()

# <----CUSTOM USER---->
class CustomUserCreateView(CreateAPIView):
    """Создание пользователя"""
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomUserSerializer

# <----STOCK---->
class StockListAPIView(ListAPIView):
    """Вывод список всех акций пользователей"""
    serializer_class = StockSerializer
    def get_queryset(self):
        return Stock.objects.all()

# <----Vacancy---->
class VacancyListAPIView(ListAPIView):
    """Вывод списка всех существующий вакансий"""
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.all()