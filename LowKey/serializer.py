from rest_framework import serializers
from .models import *

# Serializers are basically used to convert complex data to native 
# Python datatypes that can then be easily rendered into 
# JSON(Which we are going to use in React i.e. Client side). 
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
        'username',
        'email',
        'password'
        ]

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
        'username',
        'password'
        ]

    # def create(self, validated_data):
    #     password = validated_data.pop('password',None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    

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