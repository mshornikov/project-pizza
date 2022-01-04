from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns =[
    path('', ProfilePageView.as_view(), name='profile'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/passwordResetPage.html'), name='password-reset'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='users/passwordResetDonePage.html'), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='users/passwordResetConfirmPage.html'), name ='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='users/passwordResetCompletePage.html'), name ='password_reset_complete'),
]