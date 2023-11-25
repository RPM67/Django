from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fees(request):
    return HttpResponse("<h1>Student Fees will be displayed here.</h1>")