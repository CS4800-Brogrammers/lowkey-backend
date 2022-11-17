from asyncio import constants
from itertools import product
from pydoc import describe
from random import randint
from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _

def product_upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)


# Create your models here.
class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    category = models.TextField()
    description = models.TextField(null=True)

class Product(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    rating = models.IntegerField(default=randint(1,5))
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
