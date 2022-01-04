from django.urls import path, include
from .views import *
from cart.views import CartAddItemView

urlpatterns =[
    path('', MainPageView.as_view(), name='home'),
    path('stock/', StockPageView.as_view(), name='stocks'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('profile/', include('users.urls')),
    path('add/<int:product_id>', CartAddItemView.as_view(), name='cart_add_main'),
]