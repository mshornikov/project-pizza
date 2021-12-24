from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input_name'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input_first_name'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input_last_name'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class':'form-input_email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input_pass'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class':'form-input_checkpass'}))

    class Meta:
        model= User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input_auth_login'}))
    password=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input_auth_password'}))