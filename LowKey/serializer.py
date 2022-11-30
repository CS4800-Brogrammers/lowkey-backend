from rest_framework import serializers
from .models import *

# Serializers are basically used to convert complex data to native 
# Python datatypes that can then be easily rendered into 
# JSON(Which we are going to use in React i.e. Client side). 

class ShopSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='auth.User.id')
    products = serializers.StringRelatedField(many=True, allow_null=True, read_only=True)
    
    class Meta:
        lookup_field = "shop_id"
        model = Shop
        fields = ['user' ,
        'shop_id',
        'name',
        'address',
        'category',
        'description',
        'rating',
        'products',
        'email',
        'phone_number',
        'image']

class ProductSerializer(serializers.ModelSerializer):
    shop_id = ShopSerializer(read_only=True).data.get('shop_id')
    class Meta:
        lookup_field = "product_id"
        model = Product
        fields = ['product_id',
        'shop_id',
        'product_name',
        'price',
        'description',
        'image',
        'rating']
        read_only_fields = ['shop_id']

class SearchSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return instance

