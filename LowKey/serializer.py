from rest_framework import serializers
from .models import *

# Serializers are basically used to convert complex data to native 
# Python datatypes that can then be easily rendered into 
# JSON(Which we are going to use in React i.e. Client side). 

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
        'shop_id',
        'name',
        'address',
        'category',
        'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
        'shop_id',
        'product_name',
        'price',
        'description',
        'rating']