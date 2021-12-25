from django.urls import path, include
from django.urls.base import clear_script_prefix
from .views import *
from orders.views import order_create


urlpatterns = [
    path('', cart_detail ,name='cart'),
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path('del/<int:product_id>', cart_remove, name='cart_remove'),
    path('order/', order_create, name='order_create')
]