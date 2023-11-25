from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fees(request):
    return HttpResponse('<h1>Fees Related Details Displayed Here</h1>')
