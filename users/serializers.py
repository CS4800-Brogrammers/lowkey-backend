from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from rest_framework import serializers
from LowKey.models import Shop


class UserSerializer(ModelSerializer):
    shops = serializers.PrimaryKeyRelatedField(many=True, queryset=Shop.objects.all())
    
    class Meta:
        model = CustomUser
        fields = ('email', 'last_login', 'data_joined', 'is_staff')