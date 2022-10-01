from django.http import HttpResponse

def test(response):
    return HttpResponse("Testing my first HTTP API for CS4800 Assignment 3")