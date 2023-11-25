from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse('<h1>Home Page</h1>')

def about(response):
    return HttpResponse('<h2>About Us page</h2>')

def sum(response):
    a = 12
    b = 32
    return HttpResponse(f'<h1>sum : {a+b}</h1>')
