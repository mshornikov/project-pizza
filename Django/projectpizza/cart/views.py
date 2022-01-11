from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from projectpizza.utils import DataMixin

from stock.forms import StockForm

class CartDetailView(DataMixin, TemplateView):
    template_name = 'cart/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.CartDetail'))
        return context

    def get(self, request, **kwargs):
        cart = Cart(request)

        for item in cart.cart['default'].values():
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})

        context = self.get_context_data()
        context['cart'] = cart
        context['length'] = len(cart)
        context['stock_form'] = StockForm()

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
    def post(self, request, product_id, type, *args, **kwargs):
        print(type)
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product, type)
        return redirect('cart')




