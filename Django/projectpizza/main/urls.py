from django.http import request
from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import *
from users.views import *
from cart.views import CartAddItemView
urlpatterns =[
    path('', MainPageView.as_view(), name='home'),
    path('stock/', StockPageView.as_view(), name='stocks'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('profile/register', RegistrationView.as_view(), name='register'),
    path('profile/login', UserLoginView.as_view(),name='login'),
    path('profile/logout/', LogoutUserView.as_view(), name='logout'),
    path('add/<int:product_id>', CartAddItemView.as_view(), name='cart_add_main')
]