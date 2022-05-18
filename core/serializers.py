from rest_framework import serializers

from core.models import Product, Order
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

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