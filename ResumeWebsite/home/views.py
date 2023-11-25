from django.shortcuts import render

def home(request):
    context = {'home':'activePage'}
    return render(request,'home\home.html',context)
