from rest_framework import serializers
from .models import Product, Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# class AddProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']