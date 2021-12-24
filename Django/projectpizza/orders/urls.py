from django.conf.urls import url


from .views import *

urlpatterns =[
    path('create/', order_create, name='order_create')
]