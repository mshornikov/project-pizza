from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404

from cart.cart import Cart

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

class CartRemoveAPIView(APIView):
    """Удаление товара из корзины"""
    def post(self, request, pk, **kwargs):
        cart = Cart(request)
        cart.remove(get_object_or_404(Product, id=pk))
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
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomUserSerializer
