from django.http import request
from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import *
from cart.views import cart_add, cart_remove
from users.views import *

urlpatterns =[
    path('', MainPageView.as_view(), name='home'),
    path('stock/', StockPageView.as_view(), name='stocks'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('profile/register', RegistrationView.as_view(), name='register'),
    path('profile/login', UserLoginView.as_view(),name='login'),
    path('profile/logout/', LogoutUserView.as_view(), name='logout'),
    path('add/<int:product_id>', cart_add, name='cart_add_main')
]