from django.db.utils  import OperationalError
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.db import connections
from django.conf import settings
import bcrypt
import googlemaps
import psycopg2

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, status, authentication, authtoken
from .models import *
from users.models import *
from .serializer import *
from django.contrib.auth.decorators import login_required
from .permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication

class ProductList(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProductSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
    

    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    lookup_field = "product_id"

    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly]

    def patch(self, request, *args, **kwargs):
        super().patch(request, *args, **kwargs)
        return HttpResponse("Product Successfully Updated")

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return HttpResponse("Product Successfully Deleted")

#Shop API Endpoints

class ShopList(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    model = Shop
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, email=self.request.user.__getattribute__('email'))


class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly]

    def patch(self, request, *args, **kwargs):
        super().patch(request, *args, **kwargs)
        return HttpResponse("Shop Successfuly Updated")

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return HttpResponse("Shop Deleted Successfully")

class ShopUser(generics.ListAPIView):
    serializer_class = ShopSerializer

    lookup_field = "user_id"

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly]

    def get_queryset(self):
        print(self.request.user.pk)
        queryset = Shop.objects.filter(user=self.request.user.pk)
        return queryset

#Shop Product Endpoints
class ShopProductList(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProductSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly]

    def get_queryset(self):
        shop_path = self.request.get_full_path()
        shop_id_path = shop_path.split('/')[2]
        print(shop_id_path)
        queryset = Product.objects.filter(shop_id=shop_id_path)
        return queryset
    
    

    def perform_create(self, serializer):
        shop_path = self.request.get_full_path()
        print(shop_path)
        shop_id_path = int(shop_path.split('/')[2])
        print(shop_id_path)
        shop = Shop.objects.get(pk=shop_id_path)
        serializer.save(user=self.request.user, shop_id=shop, shop_name=shop.name)

class ShopProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    lookup_field = "product_id"

    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly]

    def get_queryset(self):
        shop_path = self.request.get_full_path()
        shop_id_path = shop_path.split('/')[2]
        print(shop_id_path)
        queryset = Product.objects.filter(shop_id=shop_id_path)
        return queryset

    def patch(self, request, *args, **kwargs):
        super().patch(request, *args, **kwargs)
        return HttpResponse("Product Successfully Updated")

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return HttpResponse("Product Successfully Deleted")

    
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
