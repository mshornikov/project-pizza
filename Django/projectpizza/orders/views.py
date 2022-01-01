from django.http import request
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderDetailSerializer, OrderItemListSerializer, OrderListSerializer, OrderItemDetailSerializer

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItems
from main.utils import DataMixin

# Create your views here.

class OrderHandlerPage(DataMixin, TemplateView):
    template_name = 'orders/orderHandlerPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context())
        return context

    def post(self, request, **kwargs):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.my_save(request=request, cart=cart)
            for item in cart:
                OrderItems.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            context = self.get_context_data()
            context.update({'order_id':order.id, 'type':'post', 'title':'.OrderCreate'})
            return render(request, self.template_name, context=context)

        
    def get(self, request, **kwargs):   
        form = OrderCreateForm()
        cart = Cart(request)
        context = self.get_context_data()
        context.update({'form':form, 'cart':cart, 'type':'get', 'title':'.MakeOrder'})
        return render(request, self.template_name, context=context)


#  <------------------------------------------>
#  <-----------Rest Framework Views----------->

class OrderListView(APIView):
    """Вывод списка всех совершенных заказов"""
    def get(self, request):
        order_list = Order.objects.all()
        serializer = OrderListSerializer(order_list, many=True)
        return Response(serializer.data)

class OrderDetailView(APIView):
    """Вывод информации о конкретном заказе"""
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)

class OrderItemsListView(APIView):
    """Вывод списка пунктов всех существующих заказов"""
    def get(self, request):
        order_item = OrderItems.objects.all()
        serializer = OrderItemListSerializer(order_item, many=True)
        return Response(serializer.data)

class OrderItemsDetailView(APIView):
    """Вывод списка пунктов всех существующих заказов"""
    def get(self, request, pk):
        #order_item = OrderItems.objects.get(id=pk)
        order_item = get_object_or_404(OrderItems, id=pk)
        serializer = OrderItemDetailSerializer(order_item)
        return Response(serializer.data)