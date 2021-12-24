from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import CreateView
from .forms import RegisterUserForm
from django.urls import reverse_lazy
# Create your views here.
from .models import *

menu = [
    {'title': "Главная", 'url': 'home'},
    {'title': "Акции", 'url':'stocks'},
    {'title': "Контакты", 'url':'contacts'},
    {'title': "О нас", 'url':'about'},
]

def mainPage(request):
    context = {
        'menu':menu,
        'title':'.ProjectPizza',
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

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registerPage.html'
    success_url = reverse_lazy('home')

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")