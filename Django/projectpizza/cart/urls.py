from django.urls import path, include
from django.urls.base import clear_script_prefix
from .views import *
from orders.views import OrderHandlerPage



urlpatterns = [
    path('', CartDetailView.as_view() ,name='cart'),
    path('add/<int:product_id>', CartAddItemView.as_view(), name='cart_add'),
    path('del/<int:product_id>', CartRemoveItemView.as_view(), name='cart_remove'),
    path('order/', OrderHandlerPage.as_view(), name='order_create')
]