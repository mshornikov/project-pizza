from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItems

# Create your views here.
menu = [
    {'title': "Главная", 'url': 'home'},
    {'title': "Акции", 'url':'stocks'},
    {'title': "Контакты", 'url':'contacts'},
    {'title': "О нас", 'url':'about'},
]


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
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
            return render(request, 'orders/orderCreated.html', {'order':order, 'menu': menu, 'title':'.MakeOrder'})

    else:
        form = OrderCreateForm()
    return render(request, 'orders/orderCreate.html', {'cart':cart, 'form':form, 'menu': menu, 'title':'.OrderComplete'})
