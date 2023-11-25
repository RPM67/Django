from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def result(request):
    return HttpResponse('<h1>Student result will be displayed here.</h1>')