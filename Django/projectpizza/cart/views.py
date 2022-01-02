from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from main.utils import DataMixin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import CartDetailSerializer

class CartDetailView(DataMixin, TemplateView):
    template_name = 'cart/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.CartDetail'))
        return context

    def get(self, request, **kwargs):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})

        context = self.get_context_data()
        context['cart'] = cart
        
        return render(request, self.template_name, context=context)

class CartAddItemView(FormView):
    def post(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            quant = cd['quantity']
            cart.add(product, quant)
        if request.path.split('/')[1] == 'add':
            return redirect('home')
        return redirect('cart')
        
class CartRemoveItemView(FormView):
    def post(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart')

# <--------REST FRAMWORK VIEWS-------->

class CartDetailAPIView(APIView):
    """Вывод содержимого корзины в данной сессии"""
    def get(self, request, **kwargs):
        cart = Cart(request)
        serializer = CartDetailSerializer(cart)
        return Response(serializer.data)
    

class CartAddAPIView(APIView):
    """Добавление в корзину некоторого количества товаров"""
    def post(self, request, pk, quant, **kwargs):
        cart = Cart(request)
        cart.add(get_object_or_404(Product, id=pk), quant)
        serializer = CartDetailSerializer(cart) 
        return Response(serializer.data)


class CartRemoveAPIView(APIView):
    """Удаление товара из корзины"""
    def post(self, request, pk, **kwargs):
        cart = Cart(request)
        cart.remove(get_object_or_404(Product, id=pk))
        serializer = CartDetailSerializer(cart) 
        return Response(serializer.data)
    


