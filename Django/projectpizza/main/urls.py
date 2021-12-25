from django.http import request
from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import *
from cart.views import cart_add, cart_remove


urlpatterns =[
    path('', mainPage, name='home'),
    path('stock/', stockPage, name='stocks'),
    path('about/', aboutPage, name='about'),
    path('contacts/', contactsPage, name='contacts'),
    path('profile/', profilePage, name='profile'),
    path('profile/register/', RegisterUser.as_view(), name='register'),
    path('profile/login/', LoginUser.as_view(), name='login'),
    path('profile/logout/', logout_user, name='logout'),
    path('add/<int:product_id>', cart_add, name='cart_add_main')
]