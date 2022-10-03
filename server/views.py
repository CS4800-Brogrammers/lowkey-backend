from django.http import HttpResponse
from django.shortcuts import render

def test(response):
    return HttpResponse("Testing my first HTTP API for CS4800 Assignment 3")

def ketan(request):
    return HttpResponse("Hello from Ketan")