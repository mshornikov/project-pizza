from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .utils import DataMixin
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, UserLoginForm
from django.urls import reverse_lazy
from django.contrib.auth import logout, login

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from swagger_tools.serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
# Create your views here.


class RegistrationView(DataMixin, CreateView):
    template_name = 'users/registerPage.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_context = self.get_user_context(title='.Register')
        return dict(list(context.items()) + list(menu_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')

class UserLoginView(DataMixin, LoginView):
    template_name ='users/loginPage.html'
    form_class = UserLoginForm

    def get_context_data(self, *, ogject_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_context = self.get_user_context(title='.Authorization')
        return dict(list(context.items()) + list(menu_context.items()))

    def get_success_url(self):
        return reverse_lazy('profile')

    
class LogoutUserView(FormView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

