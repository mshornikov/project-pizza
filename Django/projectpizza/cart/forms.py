from django import forms

product_choise = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label='Количество', choices=product_choise, coerce=int)