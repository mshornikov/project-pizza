from django.urls import path
from .yasg import urlpatterns as docs
from .views import *

urlpatterns = [
    path('cart/detail/', CartDetailAPIView.as_view()),
    path('cart/add/product_id=<int:pk>&quantity=<int:quant>/', CartAddAPIView.as_view()),
    path('cart/add/key=<str:key>/', CartAddStockAPIView.as_view()),
    path('cart/del/product_id=<int:pk>&type=<str:type>', CartRemoveAPIView().as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('orders/', OrderListAPIView.as_view()),
    path('orders/items/', OrderItemsListAPIView.as_view()),
    path('usercreation/', CustomUserCreateView.as_view()),
    path('stocks/', StockListAPIView.as_view()),
    path('vacancies/', VacancyListAPIView.as_view()),
]

urlpatterns += docs