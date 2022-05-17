from itertools import product
from termios import VEOL
from django.db import models

from core.custom_validators import validate_interval, validate_situation

INDISPONIVEL = 0
DISPONIVEL = 1

PENDENTE = 0
ENVIADO = 1
ENTREGUE = 2

PRODUCT_SITUATION = {
    INDISPONIVEL :'Indisponível',
    DISPONIVEL:'Disponível'
}

ORDER_SITUATION = {
    PENDENTE :'Pendente de envio',
    ENVIADO:'Enviado',
    ENTREGUE:'Entregue',
}

class Product(models.Model):
    name = models.CharField(max_length=253)
    value = models.FloatField(validators=[validate_interval])
    quantity = models.FloatField(validators=[validate_interval])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        """Product head representation"""
        return str(self.name)
    
    def get_situation(self):
        """Product situation"""
        return DISPONIVEL if self.quantity > 0 else INDISPONIVEL
    
    def get_situation_display(self):
        """Product situation"""
        sit = DISPONIVEL if self.quantity > 0 else INDISPONIVEL
        return PRODUCT_SITUATION[sit]
    
    def field_list(self):
        return [
                (u'Cod', self.pk),
                (u'Nome', self.name),
                (u'Valor unitário', self.value),
                (u'Quantidade', self.quantity),
                (u'Situação', self.get_situation_display()),
                ]

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    value = models.FloatField(validators=[validate_interval])
    quantity = models.FloatField(validators=[validate_interval])
    requester = models.CharField(max_length=253)
    zip_code = models.CharField(max_length=9)
    city = models.CharField(max_length=253)
    address = models.CharField(max_length=253)
    district = models.CharField(max_length=253)
    number = models.PositiveIntegerField()
    dispatcher = models.CharField(max_length=253)
    situation = models.PositiveIntegerField(validators=[validate_interval])
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    received_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        """Order head representation"""
        return str(self.pk)
    
    def get_situation_display(self):
        """Order situation"""
        return PRODUCT_SITUATION[self.get_situation]
    
    def field_list(self):
        return [
                (u'Cod', self.pk),
                (u'Produto', self.product),
                (u'Valor unitário', self.value),
                (u'Quantidade', self.quantity),
                (u'Situação', self.get_situation_display()),
                ]
