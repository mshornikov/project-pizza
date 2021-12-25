from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'id', 
            'first_name',
            'last_name',
            'email',
            'address',
            'city',
        ]