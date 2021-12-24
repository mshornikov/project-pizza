from django.urls import path, include
from django.urls.base import clear_script_prefix
from .views import *


urlpatterns = [
    path('', cart_detail ,name='cart'),
]