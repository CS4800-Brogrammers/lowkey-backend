from asyncio import constants
from itertools import product
from pydoc import describe
from random import randint
from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import *
from django.conf import settings
from django.contrib.auth import get_user_model

def product_upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)

#Reference the user model being used in the framework
User = get_user_model()
# Create your models here.

# Create your models here.
class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    category = models.TextField()
    description = models.TextField()
    rating = models.IntegerField(blank=True, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=12, null=True)

    def get_shop_id(self):
        return self.shop_id


    
        
    ## Used to have a unique constraint using the user_id and shop_id

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['user', 'shop_id'], name='unique_shop_key'
    #         )
    #     ]

class Product(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    rating = models.IntegerField(blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to=product_upload_to, default="placeholder.jpg")

    def __str__(self):
        return self.product_name


    class Meta:
        """This is used to have both the profile and product id be a unique product key"""
        constraints = [
            models.UniqueConstraint(
                fields=['shop_id', 'product_id'], name='unique_product_key'
            )
        ]
