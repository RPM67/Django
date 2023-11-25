from django.shortcuts import render

def fees(request):
    return render(request,'fees/index.html',{'hm':'/'})
