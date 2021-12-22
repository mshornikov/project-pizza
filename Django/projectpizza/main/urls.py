from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns =[
    path('', mainPage, name='home'),
    path('stock/', stockPage, name='stocks'),
    path('about/', aboutPage, name='about'),
    path('contacts/', contactsPage, name='contacts'),
    path('basket/', basketPage, name='basket'),
    path('profile/', profilePage, name='profile'),
]