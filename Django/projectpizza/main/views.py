from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
from .models import *

menu = [
    {'title': "Главная", 'url': 'home'},
    {'title': "Акции", 'url':'stocks'},
    {'title': "О нас", 'url':'about'},
    {'title': "Контакты", 'url':'contacts'},
]

def mainPage(request):
    product = Product.objects.all()
    print(product[0])
    context = {
        'menu':menu,
        'title':'.ProjectPizza',
        'productList':product,
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
    context = {
        'menu':menu,
        'title':'.Profile'
    }
    return render(request, 'main/profilePage.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")