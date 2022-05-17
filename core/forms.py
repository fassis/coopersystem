from django import forms

from core.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fiels = fields = ['name', 'value', 'quantity']