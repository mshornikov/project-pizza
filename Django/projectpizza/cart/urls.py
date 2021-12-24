from django.urls import path, include
from django.urls.base import clear_script_prefix
from .views import *


urlpatterns = [
    path('', cart_detail ,name='cart'),
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path('del/<int:product_id>', cart_remove, name='cart_remove')
]