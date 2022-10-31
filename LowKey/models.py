from asyncio import constants
from itertools import product
from pydoc import describe
from random import randint
from unicodedata import category
from django.db import models
#Import Django's User model
from django.contrib.auth.models import User

# Create your models here.
class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    category = models.TextField()
    link = models.URLField()

class Product(models.Model):
    shop_id = models.ForeignKey(Shop, to_field='shop_id', on_delete=models.CASCADE)
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField(max_length=100)
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
                fields=['shop_id', 'product_id'], name='unique_product_key'
            )
        ]
