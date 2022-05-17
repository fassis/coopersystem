from django import forms

from core.models import Order, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['create_at']
        labels = {
            "name": "Nome",
            "value": "Valor Unitário",
            "quantity": "Quantidade"
        }

class ProductUpdateForm(forms.ModelForm):
    name = forms.CharField(disabled = True)
    class Meta:
        model = Product
        exclude = ['create_at']
        
        labels = {
            "name": "Nome",
            "value": "Valor Unitário",
            "quantity": "Quantidade"
        }
        

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['create_at','situation','sent_at','received_at','value']
        labels = {
            "product": "produto",
            "quantity": "Quantidade",
            "requester": "Requisitante",
            "zip_code": "CEP",
            "city": "Cidade",
            "address": "Endereço",
            "district": "Bairro",
            "number": "Número",
            "dispatcher": "Despachante",
        }
