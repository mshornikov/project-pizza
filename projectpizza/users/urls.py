from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns =[
    path('', ProfilePageView.as_view(), name='profile'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password-reset'),
    path('reset_password_sent/', CustomPasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', CustomPasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    path('reset_password_complete/', CustomPasswordResetCompleteView.as_view(), name ='password_reset_complete'),
]