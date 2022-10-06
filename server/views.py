from django.db.utils  import OperationalError
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connections
import bcrypt
import googlemaps
import psycopg2
from . import settings

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