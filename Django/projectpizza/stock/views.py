from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormView
from .forms import StockForm
from django.contrib import messages

from .models import Stock
from cart.cart import Cart
from django.utils.timezone import now

# Create your views here.

class StockAcceptView(FormView):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        form = StockForm(request.POST)
        print(form.errors)
        if form.is_valid():
            try:
                stock = Stock.objects.get(stock_key=form.cleaned_data['stock_key'])
                if (stock.user_id.id == request.user.id):
                    if (stock.active_intil > now()):
                        cart.stock_add(stock)
                    else:
                        messages.error(request, 'Срок действия акции закончен')
                        stock.delete()
            except:
                messages.error(request, 'На данный момент нет акции с таким кодом')
        else:
            messages.error(request, 'Неверный формат ввода :(')
        return redirect('cart')