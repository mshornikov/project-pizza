from typing import Text
from django import forms
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.forms import TextInput
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        
        fields = ['first_name', 'last_name','phone', 'date_of_birth', 'email','password']
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder':'Иван'}),
            'last_name' : forms.TextInput(attrs={'placeholder':'Иванов'}),
            'phone' : forms.TextInput(attrs={'placeholder':'+79876543210'}),
            'date_of_birth' : forms.DateInput(attrs={'placeholder':'31.12.2000'}),
            'email' : forms.EmailInput(attrs={'placeholder':'example@ex.ru'}),
            'password' : forms.PasswordInput(attrs={'placeholder':'s0-Strong!_pass'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'placeholder':'example@ex.ru'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder':'s0-Strong!_pass'}))

    class Meta:
        model = User


# <----FOR ADMIN---->
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'date_of_birth', 'email', 'password', 'is_staff', 'is_superuser')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone', 'date_of_birth', 'password', 'is_active', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]


        

