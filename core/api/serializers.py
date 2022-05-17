from rest_framework import serializers

from core.models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    situation = serializers.CharField(
        source='get_situation_name',
        read_only=True)

    class Meta:
        model = Product
        fields = ('name','value','quantity','situation')


class OrderSerializer(serializers.ModelSerializer):
    situation = serializers.CharField(
        source='get_situation_name',
        read_only=True)

    class Meta:
        model = Order
        fields = (
            'product',
            'value',
            'quantity',
            'requester',
            'zip_code',
            'city',
            'address',
            'district',
            'number',
            'dispatcher',
            'situation',
            'created_at',
            'sent_at',
            'received_at',
            'updated_at',
            )