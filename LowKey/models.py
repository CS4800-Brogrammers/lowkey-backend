from asyncio import constants
from itertools import product
from pydoc import describe
from random import randint
from unicodedata import category
from django.db import models

# Create your models here.
class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)

class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    name = models.TextField(unique=True)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.TextField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return str(self.name)

    class Meta:
        """Creates uniqueness with the name and profile_id"""
        constraints = [
            models.UniqueConstraint(
                fields=['profile_id', 'name'], name = 'unique_profile'
            )
        ]

class Shop(models.Model):
    
    profile_id = models.OneToOneField(Profile, on_delete=models.CASCADE)
    shop_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Profile, related_name="shop_name", to_field='name', on_delete=models.CASCADE, default=str(Profile.name))
    address = models.TextField()
    category = models.TextField()
    link = models.URLField()

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
