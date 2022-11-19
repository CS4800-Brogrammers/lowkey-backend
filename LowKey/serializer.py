from rest_framework import serializers
from .models import Shop, Product

# Serializers are basically used to convert complex data to native 
# Python datatypes that can then be easily rendered into 
# JSON(Which we are going to use in React i.e. Client side). 

class ShopSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='auth.User.id')
    products = serializers.StringRelatedField(many=True)

    class Meta:
        lookup_field = "shop_id"
        model = Shop
        fields = ['user' ,
        'shop_id',
        'name',
        'address',
        'category',
        'description',
        'products']

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        lookup_field = "product_id"
        model = Product
        fields = ['product_id',
        'shop_id',
        'product_name',
        'price',
        'description',
        'rating']