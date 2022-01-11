from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from rest_framework.generics import ListAPIView
from swagger_tools.serializers import OrderItemSerializer, OrderSerializer

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItems
from projectpizza.utils import DataMixin

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

