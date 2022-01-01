from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, request
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

# Create your views here.
from .models import *
from .utils import DataMixin
from cart.forms import CartAddProductForm
from orders.models import Order

menu = [
    {'title': "Главная", 'url': 'home'},
    {'title': "Акции", 'url':'stocks'},
    {'title': "Контакты", 'url':'contacts'},
    {'title': "О нас", 'url':'about'},
]

class MainPageView(DataMixin, TemplateView):

    template_name = "main/mainPage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='.ProjectPizza'))
        cat_list = {product_category:Product.objects.filter(category=product_category) for product_category in ProductCategory.objects.all()}
        context['cat_list'] = cat_list
        context['cart_product_form'] = CartAddProductForm()
        print(cat_list)
        return context

def stockPage(request):
    context = {
        'menu':menu,
        'title':'.Stocks'
    }
    return render(request, 'main/stockPage.html', context=context)

def aboutPage(request):
    context = {
        'menu':menu,
        'title':'.About'
    }
    return render(request, 'main/aboutPage.html', context=context)

def contactsPage(request):
    context = {
        'menu':menu,
        'title':'.Contacts'
    }
    return render(request, 'main/contactsPage.html', context=context)

def basketPage(request):
    context = {
        'menu':menu,
        'title':'.Basket'
    }
    return render(request, 'main/basketPage.html', context=context)

def profilePage(request):
    # форма пльзователя, либо регистрация, либо авторизация
    user_id_orders = Order.objects.filter(user_id=request.user.id)
    context = {
        'menu':menu,
        'title':'.Profile',
        'orders':user_id_orders,
    }
    return render(request, 'main/profilePage.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")