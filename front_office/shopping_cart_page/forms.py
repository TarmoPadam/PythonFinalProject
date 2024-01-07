from django import forms
from back_office.products.models import Product


class AddToCartForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(), label='Product')
    quantity = forms.IntegerField(
        min_value=1, initial=1)  # Example quantity field
