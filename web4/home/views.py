from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    username = {'uname':'RPM'}
    return render(request,'home/home.html',context=username)
    # return render(request,'home/home.html',username)  # above line and this line is same