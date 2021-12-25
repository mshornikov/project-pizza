from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItems
# Create your views here.


def order_create(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            
            for item in cart:
                OrderItems.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()

            return render(request, 'orders/orderCreated.html', {'order':order})

    else:
        form = OrderCreateForm()
    return render(request, 'orders/orderCreate.html', {'cart':cart, 'form':form})
