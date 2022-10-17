from asyncio import constants
from itertools import product
from pydoc import describe
from unicodedata import category
from django.db import models

# Create your models here.
class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)

class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.TextField(max_length=30)
    description = models.TextField()

class Shop(models.Model):
    profile_id = models.OneToOneField(Profile, primary_key=True, on_delete=models.CASCADE)
    address = models.TextField()
    category = models.TextField()
    link = models.URLField()

class Product(models.Model):
    profile_id = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['profile_id', 'product_name'], name='unique_product_key'
            )
        ]
