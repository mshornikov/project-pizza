from django.urls import path, include

from .views import *

urlpatterns = [
    path('', mainPage, name="mainPage"), 
    path('about/', about, name='aboutPage'),
    path('stocks/', stocks, name='stocksPage'),
    path('communication/', communications, name = 'communicationPage'),
    path('menuitem/<int:productID>/', showProduct, name='showProduct')
]