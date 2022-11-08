from asyncio import constants
from itertools import product
from pydoc import describe
from random import randint
from unicodedata import category
from django.db import models
from users.models import *

# Create your models here.

class Shop(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=0)
    shop_id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    category = models.TextField()
    link = models.URLField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'shop_id'], name='unique_shop_key'
            )
        ]

class Product(models.Model):
    profile_id = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    rating = models.IntegerField(default=randint(1,5))
    shop = models.TextField(max_length=100, default="Brogrammers")

    def __str__(self):
        return self.product_name


    class Meta:
        """This is used to have both the profile and product id be a unique product key"""
        constraints = [
            models.UniqueConstraint(
                fields=['profile_id', 'product_id'], name='unique_product_key'
            )
        ]
