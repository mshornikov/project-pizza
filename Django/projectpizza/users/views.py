from django.http import request
from django.shortcuts import render, redirect
from .utils import DataMixin
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, UserLoginForm
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
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

    


def logout_user(request):
    logout(request) 
    return redirect('login')
