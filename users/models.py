from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import authentication

# Create your models here.
class CustomUser(AbstractUser):
    #add any extra fields here
    
    def __str__(self):
        return self.email 

class TokenAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer'