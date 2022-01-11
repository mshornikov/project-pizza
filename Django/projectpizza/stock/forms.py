from django import forms
from django.forms import TextInput
from .models import Stock

from .models import stock_id_validator

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('stock_key',)

        widgets = {
        'stock_key': TextInput(
            attrs={
            'class': 'stock_key_input',
            'placeholder':'ХХХХХ-ХХХХХ',
            })
        }
