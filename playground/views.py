from django.http import HttpResponse
from django.shortcuts import render

# request handler

# Create your views here.

def say_hello(resquest):
    return HttpResponse('Hello Leute')
