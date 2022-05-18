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
    
    def __init__(self, product, *args, **kwargs):
        
        self.product = product
        super(OrderForm, self).__init__(*args, **kwargs)

        products = Product.objects.filter(pk=product.pk)
        self.fields['product'] = forms.ModelChoiceField(products,
                    disabled = True,
                    label='Produto')
    
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity > self.product.quantity:
            raise forms.ValidationError("Quantidade está acima do disponível!")
        return quantity

class OrderEditForm(forms.ModelForm):
    
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
    
    def __init__(self, *args, **kwargs):
        
        super(OrderEditForm, self).__init__(*args, **kwargs)

        products = Product.objects.filter(pk=self.instance.product.pk)
        self.fields['product'] = forms.ModelChoiceField(products,
                    disabled = True,
                    label='Produto')
    
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity > self.instance.quantity + self.instance.product.quantity:
            raise forms.ValidationError("Quantidade está acima do disponível!")
        return quantity
