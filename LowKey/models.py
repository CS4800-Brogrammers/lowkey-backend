from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200)

    description = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return self.name