from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns =[
    path('', mainPage, name='home'),
    path('stock/', stockPage, name='stocks'),
    path('about/', aboutPage, name='about'),
    path('contacts/', contactsPage, name='contacts'),
    path('basket/', basketPage, name='basket'),
    path('profile/', profilePage, name='profile'),
    path('profile/register/', RegisterUser.as_view(), name='register'),
    path('profile/login/', LoginUser.as_view(), name='login'),
    path('profile/logout/', logout_user, name='logout'),
]