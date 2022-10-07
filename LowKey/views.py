from django.http import HttpResponse
from django.shortcuts import render
import bcrypt
import googlemaps

def home(response):
    return HttpResponse("This is the home page")
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