from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormView
from .forms import StockForm
from django.contrib import messages

from .models import Stock
from cart.cart import Cart
# Create your views here.

class StockAcceptView(FormView):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        form = StockForm(request.POST)
        if form.is_valid():
            try:
                stock = Stock.objects.get(stock_key=form.cleaned_data['stock_key'])
                cart.stock_add(stock)
            except:
                messages.error(request, 'На данный момент нет акции с таким кодом')
        else:
            messages.error(request, 'Неверный формат ввода :(')
        return redirect('cart')