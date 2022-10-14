from django.forms import ModelForm
from .models import Item
from django.contrib.auth.models import User

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        #this line removes the fields in models/room from being displayed
        exclude = ['owner']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
