from rest_framework import serializers
from .models import React, Profile, Shop, Product

# Serializers are basically used to convert complex data to native 
# Python datatypes that can then be easily rendered into 
# JSON(Which we are going to use in React i.e. Client side). 
class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['name', 'detail']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_id', 
        'name',
        'phone_number',
        'email',
        'password',
        'description']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['profile_id',
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