from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(Profile, UserAdmin)
admin.site.register(Product)
admin.site.register(Shop)