from django.shortcuts import render
from Django.projectpizza.users.utils import DataMixin
from django.views.generic import CreateView
from .forms import RegisterForm
from django.urls import reverse_lazy
# Create your views here.

class RegistrationView(DataMixin, CreateView):
    template_name = 'users/registerPage.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_context = self.get_user_context(title='.Register')
        return dict(list(context.items()) + list(menu_context.items()))
