from rest_framework import serializers
from .models import Shop, Product

# Serializers are basically used to convert complex data to native 
# Python datatypes that can then be easily rendered into 
# JSON(Which we are going to use in React i.e. Client side). 

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['user',
        'shop_id',
        'name',
        'address',
        'category',
        'link']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id',
        'profile_id',
        'product_name',
        'price',
        'description',
        'rating',
        'shop']