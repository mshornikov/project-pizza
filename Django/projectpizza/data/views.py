from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import *

siteNavigation = [
    "О нас",
    "Акции",
    "Карта",
    "Еще",
    "Чтото",
]
productCategory = [
    "Pizza",
    "Rolls",
    "Drinks",
    "Ice-cream",
]



def mainPage(request):
    products = Product.objects.all()
    print(products)
    
    return render(request, 'data/siteMainPage.html', {
        # передача данных по имени, на основании которых строится представление на сайте
        'title':'.projectPizza',
        'siteNavigation':siteNavigation,
        'productCategory':productCategory,
        'items':products
    })