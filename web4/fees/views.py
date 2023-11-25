from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def fees(request):
    name = 'rahul'
    title = 'mishra'
    dt = datetime.now()
    fee = 2354.120021
    details = {'nm':name,'lstnm':title,'dt':dt,'fee':fee}
    return render(request,'fees/fees.html',details)