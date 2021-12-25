from django import forms
from .models import Order
from django.http import request

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = [
            'first_name',
            'last_name',
            'address',
            'city',
        ]
        
    # Из заполнения исключены поля Идентификатор пользователя и Почта
    # Заполнение происходит непосредственно на основании данных профиля
    # Сумма заказа заполена на основании данных корзины сессии
    
    def my_save(self, commit=True, request=None, cart=None):
        instance = super(OrderCreateForm, self).save(commit=False)
        instance.user_id = request.user.id
        instance.email = request.user.email
        instance.total_cost = cart.get_total_price()
        if commit:
            instance.save()
        return instance
        