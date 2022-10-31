from multiprocessing import AuthenticationError
from urllib.request import Request
from django.db.utils  import OperationalError
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.db import connections
from django.conf import settings
from django.contrib.auth.models import User
import bcrypt
import googlemaps
import psycopg2

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import views
from rest_framework import generics, status
from .models import *
from .serializer import *

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class RegisterView(generics.CreateAPIView):
    """Used for the creation of a user"""
    serializer_class = UserCreateSerializer

class LoginView(views.APIView):
    """Used for the login and authentication of a user"""
    def post(self, request):
        user_email = request.data['email']
        user_password = request.data['password']
        user_name = request.data['username']
        user = User.objects.get(email=user_email, username=user_name)
        
        if user is None: #Did not find a user
            raise AuthenticationError("User not found")
        if not user.check_password(user_password): #Incorrect Password
            raise AuthenticationError("Incorrect Password")
        return Response({
            "message":"Logged In!"
        })

    
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product',
    }
    return Response(api_urls)

def test(response):
    return HttpResponse("Testing my first HTTP API for CS4800 Assignment 3")

def ketan(request):
    return HttpResponse("Hello from Ketan")

def ben(request):
    gmaps = googlemaps.Client(key='AIzaSyDFw4ACDhwC-e3agDxw_8Oo4xvya2APvoI')
    
    return HttpResponse("I have a light semester. Why do I feel so swamped with work still? Q_Q")

def alfred(request):
    return HttpResponse("Hi this is Alfred")
    
def garrett(request):
    return HttpResponse("My name is Garrett and I have so much swag")

def lam(request):
    return HttpResponse("Hey there its Lam")

def bcrypt_test(request):
    text = "hello world".encode("utf-8")
    hash = bcrypt.hashpw(text, bcrypt.gensalt())
    return HttpResponse(hash)

def database_status(request):
    db_info = settings.DATABASES['default']
    db_name = db_info['NAME']
    db_password = db_info['PASSWORD']
    db_user = db_info['USER']
    conn = connections['default']
    try:
        c = conn.cursor()
    except OperationalError:
        reachable = False
    else:
        reachable = True

    try:
        conn=psycopg2.connect(database=db_name, user=db_user, password=db_password)
        db_status = conn.status
    except Exception as e:
        print(e)
        db_status = e

    return HttpResponse("Database Reachable: "+str(reachable)+"\n\n"+str(db_status), content_type="text/plain")



# from django.shortcuts import render
# from rest_framework.views import APIView
# from . models import *
# from rest_framework.response import Response
# from . serializer import *
# # Create your views here.
  
# class ReactView(APIView):
    
#     serializer_class = ReactSerializer
  
#     def get(self, request):
#         detail = [ {"name": detail.name,"detail": detail.detail} 
#         for detail in React.objects.all()]
#         return Response(detail)
  
#     def post(self, request):
  
#         serializer = ReactSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return  Response(serializer.data)
