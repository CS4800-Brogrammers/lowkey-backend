from django.http import HttpResponse
from django.shortcuts import render
import bcrypt

def test(response):
    return HttpResponse("Testing my first HTTP API for CS4800 Assignment 3")

def ketan(request):
    return HttpResponse("Hello from Ketan")

def ben(request):
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