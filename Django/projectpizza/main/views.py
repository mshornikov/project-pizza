from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import CreateView
from .forms import LoginUserForm, RegisterUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
# Create your views here.
from .models import *
from .utils import DataMixin
from cart.forms import CartAddProductForm

menu = [
    {'title': "Главная", 'url': 'home'},
    {'title': "Акции", 'url':'stocks'},
    {'title': "Контакты", 'url':'contacts'},
    {'title': "О нас", 'url':'about'},
]

def mainPage(request):
    cart_product_form = CartAddProductForm()
    context = {
        'menu':menu,
        'title':'.ProjectPizza',
        'cart_product_form':cart_product_form,
    }
    return render(request, 'main/mainPage.html',context=context)

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
    context = {
        'menu':menu,
        'title':'.Profile'
    }
    return render(request, 'main/profilePage.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registerPage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_context = self.get_user_context(title='.Register')
        return dict(list(context.items()) + list(menu_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name ='main/loginPage.html'

    def get_context_data(self, *, ogject_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_context = self.get_user_context(title='.Authorization')
        return dict(list(context.items()) + list(menu_context.items()))

    def get_success_url(self):
        return reverse_lazy('profile')


def logout_user(request):
    logout(request) 
    return redirect('login')

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")