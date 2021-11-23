from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import *

siteNavigation = [
    {'title': "О нас", 'url_name' : 'aboutPage'},
    {'title': "Акции", 'url_name' : 'stocksPage'},
    {'title': "Контакты", 'url_name' : 'communicationPage'},
    #{'title': "Карта", 'url_name' : 'mapin'},
    #{'title': "Чтото", 'url_name' : 'smt'}
]
productCategory = [
    "All",
    "Pizza",
    "Rolls",
    "Drinks",
    "Ice-cream",
]




def mainPage(request):
    products = Product.objects.all()
    context = {
        'title':'.projectPizza',
        'siteNavigation':siteNavigation,
        'productCategory':productCategory,
        'items':products
    }

    return render(request, 'data/siteMainPage.html', context=context)

def about(request):
    context = {
        'title':'О .projectPizza',
        'siteNavigation':siteNavigation,
    }
    return render(request, 'data/siteAboutPage.html', context=context) 

def stocks(request):
    context = {
        'title': 'Акции от .projectPizza',
        'siteNavigation':siteNavigation
    }
    return render(request, 'data/siteStocksPage.html', context=context)

def communications(request):
    context = {
        'title': 'Контакты от .projectPizza',
        'siteNavigation':siteNavigation
    }
    return render(request, 'data/siteCommunicationPage.html', context=context)

def showProduct(request, productID):
    test = Product.objects.get(id = 1)
    print(test)
    context = {
        'siteNavigation':siteNavigation, 
        'test': test,
    }
    return render(request, 'data/siteProductPage.html', context=context)  