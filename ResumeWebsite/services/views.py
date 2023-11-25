from django.shortcuts import render

def services(request):
    context = {'services':'activePage'}
    return render(request,'services/services.html',context)
